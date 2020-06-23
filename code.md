---
layout: default
title: Code
---

---

#### *Side Channel Freedom*

---

###### oo7 (Spectre Checker)
[oo7](https://github.com/winter2020/oo7) is a binary analysis framework to detect and patch Spectre vulnerabilities. See the paper [oo7: Low-overhead Defense against Spectre Attacks via Program Analysis](https://asset-group.github.io/papers/oo7.pdf) for more details.

###### KLEESpectre
[KLEESpectre](https://github.com/winter2020/kleespectre) is a symbolic execution framework enhanced with speculative semantics and an accurate cache model. See the paper [KLEESpectre: Detecting Information Leakage through Speculative Cache Attacks via Symbolic Execution](https://asset-group.github.io/papers/KLEESpectre_TOSEM_main.pdf) for more details.

###### GDivAn
[GDivAn](https://bitbucket.org/AdrianHorga/gdivan/src/master/) is a measurement based execution time and side-channel analysis tool using a systematic combination of symbolic execution(SE) and genetic algorithm (GA). The inputs to GDivAn are GPU programs (CUDA). See the paper [Genetic Algorithm Based Estimation of Non-Functional Properties for GPGPU Programs](https://asset-group.github.io/papers/GDivan_JSA.pdf) for more details. 

###### Fuzzing Cache Side Channel
[This repository](https://github.com/tiyashbasu/Cache_Side_Channel_Tester) contains our search-based software testing tool to discover cache side-channel leakage. It covers both timing and access-based cache attacks and is effective both in a controlled environment and real hardware (PC and Raspberry Pi). See the paper [An Exploration of Effective Fuzzing for Side-channel Cache Leakage](https://asset-group.github.io/papers/STVR-cache-side-channel-fuzz.pdf) for more details.  

---

#### *IoT Wireless Security*

---

###### ESP8266/ESP32 Wi-Fi Attacks

[This repository](https://github.com/Matheus-Garbelini/esp32_esp8266_attacks) contains the proof-of-concept code for three Wi-Fi attacks ([CVE-2019-12586](https://nvd.nist.gov/vuln/detail/CVE-2019-12586), [CVE-2019-12587](https://nvd.nist.gov/vuln/detail/CVE-2019-12587), [CVE-2019-12588](https://nvd.nist.gov/vuln/detail/CVE-2019-12588)) against the popular ESP32/8266 IoT devices. 

###### SweynTooth

[This repository](https://github.com/Matheus-Garbelini/sweyntooth_bluetooth_low_energy_attacks) contains the proof-of-concept code for [SweynTooth vulnerability](https://asset-group.github.io/disclosures/sweyntooth/) in major BLE System-on-chips (SoCs) such as Texas Instruments, Cypress, NXP, Microchip, ST Microelectronics, Telink and Dialog semiconductors. 

###### Mirai4IIoT

[Mirai4IIoT](https://gitlab.com/asset-sutd/public/mirai4iiot) is a repository to reproduce Mirai attacks in Industrial Internet-of-things (IIoT) systems. The attacks can be reproduced in both stealthy and non-stealthy mode. See the paper [An Experimental Analysis of Security Vulnerabilities in Industrial IoT Devices](https://asset-group.github.io/papers/iiot_security_journal.pdf) for more details.  
###### Stitcher
[Stitcher](https://github.com/poppopretn/Stitcher) is a tool designed to classify and correlate evidence from IoT devices. See the paper 
[“STITCHER: Correlating Digital Forensic Evidence on Internet-of-Things Devices”](https://arxiv.org/abs/2003.07242) for details.

---

#### *AI Safety and Security*

---

###### Aequitas 
[Aequitas](https://github.com/sakshiudeshi/Aequitas) is a directed fairness testing framework for machine learning models. See the paper [Automated Directed Fairness Testing](https://arxiv.org/abs/1807.00468) for more details.

###### Ogma
[Ogma](https://github.com/sakshiudeshi/Ogma) provides a systematic test framework for machine-learning systems that accept grammar-based inputs. See the paper [Grammar Based Directed Testing of Machine Learning Systems](https://arxiv.org/pdf/1902.10027) for more details.

###### Callisto 
[Callisto](https://github.com/sakshiudeshi/Callisto/) is a novel test generation and data quality assessment framework. Callisto  leverages the uncertainty in the prediction to systematically generate new test cases and evaluate data quality for Machine Learning classifiers. See the paper [Callisto: Entropy based test generation and data quality assessment for Machine Learning Systems](https://asset-group.github.io/papers/Callisto.pdf) for more details.

###### Aegis 
[Aegis](https://github.com/sakshiudeshi/Expose-Robust-Backdoors) is a novel tool to detect backdoor attacks in adversarially robust machine-learning models. Aegis leverages intrinsic properties of adversarially robust models to break the stealthy nature of backdoors. See the preprint [AEGIS: Exposing Backdoors in Robust Machine Learning Models](https://arxiv.org/abs/2003.00865) for more details.

###### RAIDS
[RAIDS](https://github.com/cd-wang/RAIDS) is an intrusion detection system for autonomous cars. It extracts and analyzes sensory information (e.g., camera images and distance sensor values) to validate frames transmitted on the in-vehicle network (e.g., CAN bus). See the paper [Road Context-aware Intrusion Detection System for Autonomous Cars](https://asset-group.github.io/papers/ICICS19-RAIDS.pdf) for more details. 

---

#### *Verification*

---

###### AIG-AC
[AIG-AC](https://gitlab.com/asset-sutd/public/aig-ac) is a tool that performs attacker classification on systems represented with And-inverter Graphs (AIGs) via bounded model checking. See the paper [Systematic Classification of Attackers via Bounded Model Checking](https://asset-group.github.io/papers/VMCAI20.pdf) for more details. 

###### AGRID
[AGRID](https://gitlab.com/asset-sutd/public/agrid) aims at encoding discrete models of robotic systems to support 
verification of robotic software. It is able to encode models as either Satisfiability Modulo Theory or Bounded Model 
Checking problems.


