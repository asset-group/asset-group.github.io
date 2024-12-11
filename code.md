---
layout: default
title: Code
---

In the ASSET research group, we encourage open-source release of software artifacts. As of now, we have released software 
artifacts (exceptions are due to the restriction imposed by respective funding agencies supporting the project) associated 
with most of our research papers. 

---

#### *(Micro-architectural) Timing Channel*

---

###### oo7 (Spectre Checker)
[oo7](https://github.com/winter2020/oo7) is a binary analysis framework to detect and patch Spectre vulnerabilities. See the paper [oo7: Low-overhead Defense against Spectre Attacks via Program Analysis](https://asset-group.github.io/papers/oo7.pdf) for more details.

###### KLEESpectre
[KLEESpectre](https://github.com/winter2020/kleespectre) is a symbolic execution framework enhanced with speculative semantics and an accurate cache model. See the paper [KLEESpectre: Detecting Information Leakage through Speculative Cache Attacks via Symbolic Execution](https://asset-group.github.io/papers/KLEESpectre_TOSEM_main.pdf) for more details.

###### GDivAn
[GDivAn](https://bitbucket.org/AdrianHorga/gdivan/src/master/) is a measurement based execution time and side-channel analysis tool using a systematic combination of symbolic execution(SE) and genetic algorithm (GA). The inputs to GDivAn are GPU programs (CUDA). See the paper [Genetic Algorithm Based Estimation of Non-Functional Properties for GPGPU Programs](https://asset-group.github.io/papers/GDivan_JSA.pdf) for more details. 

###### Fuzzing Cache Side Channel
[This repository](https://github.com/tiyashbasu/Cache_Side_Channel_Tester) contains our search-based software testing tool to discover cache side-channel leakage. It covers both timing and access-based cache attacks and is effective both in a controlled environment and real hardware (PC and Raspberry Pi). See the paper [An Exploration of Effective Fuzzing for Side-channel Cache Leakage](https://asset-group.github.io/papers/STVR-cache-side-channel-fuzz.pdf) for more details.  

###### Chalice
[This repository](https://github.com/sudiptac/chalice) contains our tool to quantify cache side-channel leakage from program executions. It covers both timing and access-based cache attacks. See the paper [Quantifying the Information Leakage in Cache Attacks via Symbolic Execution](https://sudiptac.bitbucket.io/papers/chalice-tecs.pdf) for more details. The link for the code provided in the paper is not valid anymore, as bitbucket deleted all mercurial repositories. Please use the link provided here if you wish to reproduce the results.  

---

#### *(Wireless) Communication Security*

---

###### AirBugCatcher

[This repository](https://github.com/asset-group/air-bug-catcher) contains the code for **AirBugCatcher** -- a generic wireless bug reproduction tool evaluated on a variety of wireless protocols such as 5G NR, Bluetooth and Wi-Fi. See the paper [AirBugCatcher: Automated Wireless Reproduction of IoT Bugs](https://asset-group.github.io/papers/airbugcatcher.pdf) for more details. 

###### VaktBLE

[This repository](https://github.com/asset-group/vakt-ble-defender/) contains the code for **VaktBLE** -- a friendly man-in-the-middle bridge to actively prevent link-layer attacks on BLE peripherals. See the paper [VaktBLE: A Benevolent Man-in-the-middle Bridge to Guard against Malevolent BLE Connections](https://asset-group.github.io/papers/vaktble.pdf) for more details. 

###### U-Fuzz

[This repository](https://github.com/asset-group/U-Fuzz) contains the code for **U-Fuzz** -- a generic wireless protocol fuzzer experimented with 5G NR, CoAP and ZigBee protocol implementations. See the paper [U-Fuzz: Stateful Fuzzing of IoT Protocols on COTS Devices](https://asset-group.github.io/papers/U-Fuzz.pdf) for more details. 

###### VitroBench (Software)

[This repository](https://github.com/yeoant/VitroBench) contains the Proof-of-concept (PoC) code for sniffing, injection or interception, and fuzzing or attacks executed on the [VitroBench Test Platform](https://www.vitrobench.com). See the paper [VitroBench: Manipulating In-vehicle Networks and COTS ECUs on Your Bench](https://asset-group.github.io/papers/VitroBench.pdf) and the companion [VitroBench Website](https://www.vitrobench.com) for more details. 

###### BrakTooth (Proof of Concept)

[This repository](https://github.com/Matheus-Garbelini/braktooth_esp32_bluetooth_classic_attacks) contains the Proof-of-concept (PoC) code for [BrakTooth vulnerability](https://asset-group.github.io/disclosures/braktooth/) in major Bluetooth System-on-chips (SoCs) such as Intel, Qualcomm, Texas Instruments, Cypress, Silicon Labs, Xiaomi, Mediatek, Samsung etc.

###### BrakTooth (Sniffing)

[This repository](https://github.com/Matheus-Garbelini/esp32_bluetooth_classic_sniffer) contains the BR/EDR active sniffer code developed as part of discovering [BrakTooth vulnerability](https://asset-group.github.io/disclosures/braktooth/) in major Bluetooth System-on-chips (SoCs). The sniffing tool is as cheap as any ESP32 board can get (less than 15 USD).

###### BrakTooth (ESP32 Firmware Patching)

[This repository](https://github.com/Matheus-Garbelini/esp32_firmware_patching_framework) contains the ESP32 Firmware patching framework. This was used to design a real-time fuzzing interface that resulted in [BrakTooth vulnerability](https://asset-group.github.io/disclosures/braktooth/).

###### ESP8266/ESP32 Wi-Fi Attacks

[This repository](https://github.com/Matheus-Garbelini/esp32_esp8266_attacks) contains the proof-of-concept code for three Wi-Fi attacks ([CVE-2019-12586](https://nvd.nist.gov/vuln/detail/CVE-2019-12586), [CVE-2019-12587](https://nvd.nist.gov/vuln/detail/CVE-2019-12587), [CVE-2019-12588](https://nvd.nist.gov/vuln/detail/CVE-2019-12588)) against the popular ESP32/8266 IoT devices. 

###### SweynTooth

[This repository](https://github.com/Matheus-Garbelini/sweyntooth_bluetooth_low_energy_attacks) contains the proof-of-concept code for [SweynTooth vulnerability](https://asset-group.github.io/disclosures/sweyntooth/) in major BLE System-on-chips (SoCs) such as Texas Instruments, Cypress, NXP, Microchip, ST Microelectronics, Telink and Dialog semiconductors. 


###### Mirai4IIoT

[Mirai4IIoT](https://gitlab.com/asset-sutd/public/mirai4iiot) is a repository to reproduce Mirai attacks in Industrial Internet-of-things (IIoT) systems. The attacks can be reproduced in both stealthy and non-stealthy mode. See the paper [An Experimental Analysis of Security Vulnerabilities in Industrial IoT Devices](https://asset-group.github.io/papers/iiot_security_journal.pdf) for more details.  

---

#### *(IoT) Cybercrime and Forensics*

---


###### Stitcher

[Stitcher](https://github.com/poppopretn/Stitcher) is a tool designed to classify and correlate evidence from IoT devices. See the FSIDI paper 
[“STITCHER: Correlating Digital Forensic Evidence on Internet-of-Things Devices”](https://asset-group.github.io/papers/Stitcher_FSIDI.pdf) for details.


###### SCI Threat Models

[SCI Threat Models](https://github.com/poppopretn/SmartCityThreatModel) is a set of threat models designed to classify threats and map evidences for 
cybercrime investigation in smart city infrastructure (SCI). The threat model is technology-agnostic - the SCI modeled here focuses on gathering 
quality of life data indicators as specified in ISO37101:2016, ISO37120:2018, ISO37122:2019 and ISO37123:2019 instead. See the FSIDI  paper 
[“Identifying Threats, Cybercrime and Digital Forensic Opportunities in Smart City Infrastructure via Threat Modeling.”](https://asset-group.github.io/papers/SmartCityThreatModelCyberCrime.pdf) 
for details.


---

#### *AI/ML Safety, Bias and Security*

---

###### KonTest
[KonTest](https://github.com/sparkssss/KonTest) is a consistency testing framework for Large Language Models (LLMs). See the paper in EMNLP 2024 Findings [Knowledge-based Consistency Testing of Large Language Models](https://asset-group.github.io/papers/KBCon.pdf) for more details.

###### DistroFair
[DistroFair](https://github.com/sparkssss/DistroFair) is a fairness formalization and testing framework, based on out-of-distribution (OOD) test data generation, for object detection systems. See the paper in JSS 2024 [Distribution-aware Fairness Test Generation](https://asset-group.github.io/papers/ImgFairMain.pdf) for more details.

###### AequeVox
[AequeVox](https://github.com/sparkssss/AequeVox) is a fairness formalization and testing framework for speech recognition systems. See the paper in FASE 2022 [AequeVox: Automated Fairness Testing of Speech Recognition Systems](https://arxiv.org/abs/2110.09843) for more details.

###### Astraea
[Astraea](https://github.com/sakshiudeshi/Astraea) is a grammar-based fairness testing framework for machine learning models (specifically, NLP tasks). See the paper in IEEE TSE 2022 [Grammar-based Fairness Testing](https://arxiv.org/abs/2010.02542) for more details.

###### Aequitas 
[Aequitas](https://github.com/sakshiudeshi/Aequitas) is a directed fairness testing framework for machine learning models. See the paper in ASE 2018 [Automated Directed Fairness Testing](https://arxiv.org/abs/1807.00468) for more details.

###### Ogma
[Ogma](https://github.com/sakshiudeshi/Ogma) provides a systematic test framework for machine-learning systems that accept grammar-based inputs. See the paper in IEEE TSE 2019 [Grammar Based Directed Testing of Machine Learning Systems](https://arxiv.org/pdf/1902.10027) for more details.

###### Aegis
[Aegis](https://github.com/sakshiudeshi/Expose-Robust-Backdoors) provides a systematic framework for detecting backdoored, yet robust machine-learning systems. See the paper in Computers & Security 2023 [Towards Backdoor Attacks and Defense in Robust Machine Learning Models](https://arxiv.org/abs/2003.00865) for more details.

###### Neo
[Neo](https://github.com/sakshiudeshi/Neo) provides a systematic model-agnostic defense for Backdoor attacks. See the paper in IEEE Transactions on Reliability 2022 [Model Agnostic Defence Against Backdoor Attacks in Machine Learning](https://arxiv.org/abs/1908.02203) for more details.

###### Callisto 
[Callisto](https://github.com/sakshiudeshi/Callisto/) is a novel test generation and data quality assessment framework. Callisto  leverages the uncertainty in the prediction to systematically generate new test cases and evaluate data quality for Machine Learning classifiers. See the paper in ICST 2020 [Callisto: Entropy based test generation and data quality assessment for Machine Learning Systems](https://asset-group.github.io/papers/Callisto.pdf) for more details.

###### RAIDS
[RAIDS](https://github.com/cd-wang/RAIDS) is an intrusion detection system for autonomous cars. It extracts and analyzes sensory information (e.g., camera images and distance sensor values) to validate frames transmitted on the in-vehicle network (e.g., CAN bus). See the paper in ICICS 2019 [Road Context-aware Intrusion Detection System for Autonomous Cars](https://asset-group.github.io/papers/ICICS19-RAIDS.pdf) for more details. 

---

#### *Verification*

---

###### AIG-AC
[AIG-AC](https://gitlab.com/asset-sutd/public/aig-ac) is a tool that performs attacker classification on systems represented with And-inverter Graphs (AIGs) via bounded model checking. See the paper [Systematic Classification of Attackers via Bounded Model Checking](https://asset-group.github.io/papers/VMCAI20.pdf) for more details. 

###### AGRID
[AGRID](https://gitlab.com/asset-sutd/public/agrid) aims at encoding discrete models of robotic systems to support 
verification of robotic software. It is able to encode models as either Satisfiability Modulo Theory or Bounded Model 
Checking problems.


