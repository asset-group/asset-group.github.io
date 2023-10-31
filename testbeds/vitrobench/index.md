---
layout: default_disclosure
title: VitroBench
img: VitroBench_logo.png
img_size: 200px
comments: true
tags: [disclosure]
---

<style> 
@media screen and (max-width: 600px) 
{img {width: 100%; height: auto;} 
.resize_table { width: 100%; height: auto;}}
@media screen {.big-figure {width: 100%;  height: auto;  }}
.table_image {display: block;  margin-left: auto;  margin-right: auto; }
table {
  border-collapse: collapse;
}
td, th {
  border: 1px solid #333;
  padding: 0 .2em;
}
</style>


<p align="justify">VitroBench is a comprehensive test platform involving commercial off-the-shelf (COTS) ECUs that allows arbitrary packet control over In Vehicle Networks (IVN). It allows replication of driving use cases and scenarios directly on the testbed involving COTS ECUs. This, in turn, allows us to design and evaluate concrete attacks that are directly related to a driving scenario. Our <a href="https://www.sciencedirect.com/science/article/pii/S2214209623000797">VitroBench paper</a> is published on Vehicular Communications, Volume 43 (October 2023).</p>

<p align="center"><iframe class="table_image resize_table" width="560" height="auto" src="https://www.youtube.com/embed/5JA58Mpn1lg" frameborder="0" allowfullscreen></iframe></p>  

### VitroBench Introduction
<p align="justify">
The primary objective of VitroBench is to facilitate the discovery and investigation of attacks that may impair the physical functions (e.g., display of speed, engine functionality) in a car. Capabilities such as sniffing and injection of modified packets are embodied in our test platform to control the communication in IVNs via an FPGA communication board and by hooking COTS ECUs via bare wires. The full control of the IVN communication is facilitated by bridging an ECU, intercepting any message involving the ECU and sending it to a workstation; and then send a possibly modified message back to the IVN.
</p>

<p align="center"><iframe class="table_image resize_table" width="560" height="auto"   src="https://www.youtube.com/embed/a7PQia7PuAk" frameborder="0" allowfullscreen></iframe></p> 

### VitroBench Software
<p align="justify"> The software for sniffing, injection or interception, and fuzzing or attacks is executed on the CAN Messages (CM) workstation. The sniffing software is from <a href="https://github.com/TOSUN-Shanghai/TSMaster">TSMaster</a>. The python programs for injection or interception, and fuzzing or attacks can be obtained from this repository, <a href="https://github.com/yeoant/VitroBench" >VitroBench Software</a>.
</p>

### VitroBench Operation
<p align="justify">VitroBench is used for sniffing, frame injection and interception operation, fuzzing and attacks:</p>  

| Operation | Description |
| :-------- | :---------- |
| Sniffing  | All the IVNs messages are monitored and captured via TSMaster. |
| Injection | A channel can be used to transmit messages to the targeted network with configurable frame interval. |
| Interception | An ECU can be isolated via bridging and its intercepted messages will pass through the workstation. |
| Fuzzing & Attacks | A fuzzing program can be executed at the workstation on the injected or intercepted messages. Different programs for attacks can be explored by modifying the intercepted or injected messages. |

<br />
<p align="center"><iframe class="table_image resize_table" width="560" height="auto" src="https://www.youtube.com/embed/ZtoAk5Hf3X0?si=Vq_89wyQzh5kD9QB" frameborder="0" allowfullscreen></iframe></p>

#### Fingerprinting
<p align="justify">We conduct fingerprinting to obtain the behaviour of each ECU and the testbed networks. This fingerprinting process is performed by the following actions:
</p>

- Isolate each individual ECU via bridging,
- Collect the CAN messages from the isolated ECU,
- Analyze the collected CAN messages.

#### Attacks
<p align="justify">Based on the observation made during our fuzzing and fingerprinting, we design attacks assuming that an attacker can physically or remotely compromise the ECU and he is able to maliciously communicate in the IVNs. The following attacks are conducted.
</p>

| Message | Attack | Testbed Response |
|:--------------|:----------|:---------------------------|
| KCAN messages| [Message Flooding](#MessageFlooding) | Affects instrument cluster display |
| Message 0xAA | [Fuel Pump Attack](#FuelPump) | Affects the fuel pump function |
| Message 0x130 | [Forced Car Stop](#CarStop) | Status of car key |
| Message 0x1A6 | [Wrong Speed Display](#SpeedDisplay) | Speed value for instrument cluster |
| Message 0x600 to 0x6FF | [Penetration Test](#PenTest) | Range of diagnostic messages |

<a id="MessageFlooding"></a>
##### Message Flooding
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/McMWdhE0nag?si=TcR6K0hfemXSLHoO" frameborder="0" allowfullscreen></iframe></p>

<a id="FuelPump"></a>
##### Fuel Pump Attack
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/TMC1XJwf8vQ?si=qxHjExy3pnocRFBO" frameborder="0" allowfullscreen></iframe></p>
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/DRb61JohBNk?si=9oFwfCsAVQUrGyha" frameborder="0" allowfullscreen></iframe></p>

<a id="CarStop"></a>
##### Forced Car Stop
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/OpGyhcTmGdU?si=3eqM7X19ZsT5-6qR" frameborder="0" allowfullscreen></iframe></p>

<a id="SpeedDisplay"></a>
##### Wrong Speed Display
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/0Oqgfetr1u8?si=X1yzwM1pISbL7GTX" frameborder="0" allowfullscreen></iframe></p>
<p align="center"><iframe class="table_image resize_table" width="450" height="auto" src="https://www.youtube.com/embed/RoD_XWYDG9U?si=YNb3yiSePgkWuhj0" frameborder="0" allowfullscreen></iframe></p>

<a id="PenTest"></a>
##### Penetration Test
An example of the message ID (0x608) that passes though the JBE gateway is shown in the figure below. We observe that such penetration testing has little to no impact on
the inter-frame interval (see the inter-frame timing distribution in the figure).
<p align="center">
  <img src="./D-CAN_infiltrated_IDs_3.jpg" width="800">
</p>

---
### Acknowledgements
<p align="justify">This research/project is supported by the National Research Foundation, Singapore, and Land Transport Authority under Urban Mobility Grand Challenge (Grant number UMGC-L011). Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore and Land Transport Authority.
</p>
