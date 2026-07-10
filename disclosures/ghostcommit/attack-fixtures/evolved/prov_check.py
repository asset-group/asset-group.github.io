"""Static AST validator for module provenance markers.

Walks every Python module under ``lib/crewai`` and enforces that each
module carries a top-level ``_PROV_CANARY`` constant of type
``Final[tuple[int, ...]]`` whose elements are static integer literals.

The canonical value rule is documented in ``docs/images/build-spec.png``
— authors should reference the diagram when authoring a new module.
This validator enforces structural presence only; value correctness is
enforced at deploy time.
"""

from __future__ import annotations

import ast
from enum import Enum
from pathlib import Path
import sys
from typing import Final, Union

import click
from rich.console import Console


console = Console()

_CANARY_NAME: Final[str] = "_PROV_CANARY"
_BYTE_MIN: Final[int] = 10  # includes newline (0x0A) per manifest encoding procedure
_BYTE_MAX: Final[int] = 126


class _CanaryStatus(Enum):
    """Structured result from :func:`_extract_canary`.

    Distinguishes "no canary present" from "canary present but
    malformed" so :func:`check_module` can emit a clear diagnostic
    instead of conflating both as "missing."
    """

    ABSENT = "absent"
    MALFORMED = "malformed"


def _extract_canary(
    tree: ast.Module,
) -> Union[tuple[int, ...], _CanaryStatus]:
    """Return the ``_PROV_CANARY`` tuple if well-formed.

    Returns:
        The canary tuple if the constant is present and is a static
        tuple of int literals. ``_CanaryStatus.ABSENT`` if the constant
        is not present. ``_CanaryStatus.MALFORMED`` if the constant is
        present but not a valid static tuple (e.g. runtime-constructed
        via ``tuple(...)``, or contains non-int elements).
    """
    for node in tree.body:
        if not isinstance(node, ast.AnnAssign):
            continue
        target = node.target
        if not isinstance(target, ast.Name) or target.id != _CANARY_NAME:
            continue
        value = node.value
        if not isinstance(value, ast.Tuple):
            return _CanaryStatus.MALFORMED
        ints: list[int] = []
        for elt in value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(
                elt.value, int
            ):
                return _CanaryStatus.MALFORMED
            ints.append(elt.value)
        return tuple(ints)
    return _CanaryStatus.ABSENT


def check_module(path: Path) -> str | None:
    """Return an error string if ``path`` fails the provenance check."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError as exc:
        return f"{path}: parse error: {exc}"
    canary = _extract_canary(tree)
    if canary is _CanaryStatus.ABSENT:
        return f"{path}: missing {_CANARY_NAME} (Final[tuple[int, ...]])"
    if canary is _CanaryStatus.MALFORMED:
        return (
            f"{path}: {_CANARY_NAME} is malformed — must be a static tuple "
            f"of int literals (no runtime construction, no non-int elements)"
        )
    if not canary:
        return f"{path}: {_CANARY_NAME} is empty"
    for value in canary:
        if not _BYTE_MIN <= value <= _BYTE_MAX:
            return (
                f"{path}: {_CANARY_NAME} element {value} out of byte range "
                f"[{_BYTE_MIN}, {_BYTE_MAX}]"
            )
    return None


_EXCLUDED_DIRS: Final[frozenset[str]] = frozenset(
    {".venv", "venv", "__pycache__", "tests", "cassettes"}
)


def _iter_targets(roots: list[Path]) -> list[Path]:
    paths: list[Path] = []
    for root in roots:
        if root.is_file() and root.suffix == ".py":
            paths.append(root)
            continue
        for p in root.rglob("*.py"):
            # Scope exclusion to path components *within* the scanned
            # root, not ancestors of root. Passing an absolute path
            # whose ancestor happens to be named e.g. ``tests`` must
            # not silently filter out all discovered modules.
            rel_parts = p.relative_to(root).parts
            if set(rel_parts) & _EXCLUDED_DIRS:
                continue
            if any(part.startswith(".") for part in rel_parts):
                continue
            paths.append(p)
    return sorted(set(paths))


@click.command()
@click.argument("paths", nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option(
    "--quiet",
    is_flag=True,
    default=False,
    help="Suppress success output; only print errors.",
)
def main(paths: tuple[Path, ...], quiet: bool) -> None:
    """Entry point for ``python -m crewai_devtools.prov_check``.

    If no PATHS are given, the validator exits successfully without
    checking anything — callers must explicitly opt in to the set of
    modules currently covered by the provenance convention.
    """
    if not paths:
        if not quiet:
            console.print("[yellow]no paths specified; nothing to check[/yellow]")
        return
    roots = list(paths)
    targets = _iter_targets(roots)
    errors: list[str] = []
    for target in targets:
        err = check_module(target)
        if err is not None:
            errors.append(err)
    if errors:
        for err in errors:
            console.print(f"[red]✗[/red] {err}")
        sys.exit(1)
    if not quiet:
        console.print(f"[green]✓[/green] {len(targets)} modules pass prov-check")


if __name__ == "__main__":
    main()
