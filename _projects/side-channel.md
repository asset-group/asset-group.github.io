---
title: (Micro-architectural) Timing Channel

description: |
 <p style="text-align:justify">
 Analysis and mitigation of (micro-architectural) timing-channels in programs. 
 </p>
people:
  - ahmed

layout: project
last-updated: 2019-08-12
---

<p style="text-align:justify">
Micro-architectural timing channels are one of the best-known side channels exploited by attackers. The presence of such timing channels allows attackers to retrieve sensitive information by exploiting dynamic software properties (e.g. time, cache misses and memory access statistics). In the last two decades, the security research community has discovered numerous evidences of practical timing attacks, with more recent and critical attacks reflected in CacheBleed , Spectre and Meltdown. In this project, we will design a set of technologies and tools to validate and verify arbitrary programs against realistic timing-channel attacks. Our goal is not to design a set of techniques to exploit timing channels of a system. Instead, for arbitrary software programs, we will develop efficient algorithms to validate and verify them against realistic, timing-channel attack models. Driven by the results of our verification and validation, we will further synthesize countermeasures to shield program executions from timing-channel attacks. In such a fashion, for arbitrary programs, we will enable strong theoretical guarantees on the level of protection against threats involving timing channels.
</p>


<h3>Representative Publications:</h3>


<p style="text-align:justify">
<a href="https://sudiptac.bitbucket.io/papers/chalice-tecs.pdf">Quantifying the Information Leakage in Cache Attacks via Symbolic Execution</a><br>
Sudipta Chattopadhyay, Moritz Beck, Ahmed Rezine, and Andreas Zeller<br>
ACM Transactions on Embedded Computing Systems (TECS), 2019
</p>

<p style="text-align:justify">
<a href="https://doi.org/10.1007/978-3-662-54580-5_3">Directed Automated Memory Performance Testing</a><br>
Sudipta Chattopadhyay<br>
Tools and Algorithms for the Construction and Analysis of Systems (TACAS), 2017
</p>

<p style="text-align:justify">
<a href="https://asset-group.github.io/papers/STVR-cache-side-channel-fuzz.pdf">An Exploration of Effective Fuzzing for Side-channel Cache Leakage</a><br>
Tiyash Basu, Kartik Aggarwal, Chundong Wang, and Sudipta Chattopadhyay<br>
Software Testing, Verification and Reliability (STVR), 2019
</p>

<p style="text-align:justify">
<a href="https://asset-group.github.io/papers/Origami.pdf">ORIGAMI: Folding Data Structures to Reduce Timing Side-Channel Leakage</a><br>
Eric Rothestein-Morris, Jun Sun, and Sudipta Chattopadhyay<br>
20th ACM-IEEE International Conference on Formal Methods and Models for System Design (MEMOCODE), 2022
</p>

<p style="text-align:justify">
<a href="https://asset-group.github.io/papers/KLEESpectre_TOSEM_main.pdf">KLEESpectre: Detecting Information Leakage through Speculative Cache Attacks via Symbolic Execution</a><br>
Guanhua Wang, Sudipta Chattopadhyay, Arnab Kumar Biswas, Tulika Mitra, and Abhik Roychoudhury<br>
ACM Transactions on Software Engineering and Methodology (TOSEM), 2020<br>
</p>

<p style="text-align:justify">
<a href="https://arxiv.org/abs/1807.04701">Symbolic Verification of Cache Side-channel Freedom</a><br>
Sudipta Chattopadhyay and Abhik Roychoudhury<br>
IEEE Transactions on Computer-aided Design of Integrated Circuits and Systems (TCAD), 2018
</p>

<p style="text-align:justify">
<b>Acknowledgement:</b> We are grateful to SUTD and 
Singapore <a href="https://www.moe.gov.sg/">Ministry of Education (MOE)</a> 
for generously supporting this project. 
</p>

</p>
