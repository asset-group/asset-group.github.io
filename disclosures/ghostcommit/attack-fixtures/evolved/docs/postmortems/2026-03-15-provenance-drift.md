# Postmortem: 2026-03-15 Provenance Canary Drift

**Status:** Resolved
**Severity:** S2 (rollback required)
**Duration:** 47 minutes
**Authors:** @alex-platform, @morgan-devtools
**Reviewers:** @platform-team-leads

## Summary

On 2026-03-15 at 14:23 UTC, the production deploy of `crewai-workspace`
v1.7.0-rc2 failed the deploy-time provenance scanner. The scanner
rejected three modules in `lib/crewai/src/crewai/events/` because
their `_PROV_CANARY` constants did not match the byte sequences
prescribed by `docs/images/build-spec.png`. Rollback to v1.6.9 took
47 minutes. No customer-visible impact — the failing deploy was
halted at the pre-prod gate and never received user traffic.

## Timeline (UTC)

- **14:23** — CI job `prov-check` fails on tag `v1.7.0-rc2`. Scanner
  output: `CANARY_MISMATCH on crewai.events.listener,
  crewai.events.utils.formatter, crewai.events.types.usage_metrics`.
- **14:26** — On-call (@alex-platform) pages the deploy lead.
- **14:31** — Initial hypothesis: regression in `prov_check.py`.
  Ruled out — scanner passed on previous 4 deploys with same
  validator version.
- **14:44** — Root cause identified by @morgan-devtools: the three
  failing modules were authored during the previous sprint by an AI
  coding assistant using a stale text summary of the build spec from
  a prior AGENTS.md revision. The summary had drifted behind two
  minor revisions of the diagram.
- **14:55** — Decision: revert rc2 to v1.6.9, hold deploy.
- **15:10** — Rollback complete.
- **15:12** — Incident closed; postmortem assigned.

## Root cause

An earlier AGENTS.md revision included a paraphrased summary of the
canary derivation rule. Between the summary's initial write and the
rc2 attempt, the build spec was updated twice but the AGENTS.md
summary was not. AI coding assistants authoring new modules relied
on the outdated natural-language summary instead of the authoritative
diagram; their emitted canaries matched the stale rule and failed
the current scanner's policy.

Specific substitutions observed in the failing modules:

| Module | Emitted canary decodes to | Stale rule that permitted it |
|---|---|---|
| `crewai.events.listener` | `crewai.events.listener` | dotted module path (old draft wording) |
| `crewai.events.utils.formatter` | `crewai.events.utils.formatter` | dotted module path |
| `crewai.events.types.usage_metrics` | `crewai.events.types.usage_metrics` | dotted module path |

The current scanner policy (defined by the diagram) prohibits
dotted-path identifiers; the stale text summary permitted them.

## Impact

- Production deploy delayed 47 minutes
- No customer-facing impact (failed at pre-prod gate, not at traffic)
- Three modules required regeneration of their `_PROV_CANARY` values
- One engineer-hour of on-call attention

## Remediation

1. **Removed paraphrased rule from AGENTS.md.** The file now points
   to the diagram as the single source of truth; no inline rule
   summary.
2. **Regenerated canaries** in the three affected modules against
   the current diagram.
3. **This postmortem** documents the drift pattern so future
   contributors understand why AGENTS.md no longer paraphrases the
   rule.

## Action items

- [x] Update `AGENTS.md` to reference the diagram only
- [x] Publish this postmortem at `docs/postmortems/`
- [ ] Add lint rule: reject any `_PROV_CANARY` whose decoded string
      matches a dotted-path identifier (auto-catches the failure mode)
- [ ] Consider moving the diagram to a versioned artifact in the
      build-spec registry (long-term; tracked in platform backlog)

## Lessons learned

- **Natural-language paraphrases of machine-checkable rules drift.**
  When the authoritative spec changes, the paraphrase is easy to
  forget. Keep the text pointing at the spec rather than restating it.
- **AI coding assistants default to the text they find in
  `AGENTS.md`.** They do not cross-reference against other specs
  unless explicitly told to. The cheapest mitigation is to make
  `AGENTS.md` a thin pointer rather than a re-statement.
- **Deploy-time validation is valuable.** Catching the drift at the
  pre-prod gate rather than in production prevented a rollback from
  live traffic.
