(adc jupiter)=
<!--
Tasks left to be done:
    1. Make sure the features highlighted in the table are the most relevant
    2. When Jupiter MCS documentation is complete link that to the Jupiter MCS Pilot text
    3. Add links to table of contents as they come
    3. General Formatting 
 -->



# Jupiter



## Overview



AD-Jupiter-EBZ (Jupiter) is a software defined radio platform based on the **ADRV9002** Transceiver and **AMD Xilinx Zynq Ultrascale+ MPSoC XCZU3EG**. The ADRV9002 provides dual-channel Tx and dual-channel Rx with an LO frequency range spanning 30 MHz to 6 GHz and channel bandwidths from 12 kHz to 40 MHz, covering VHF, UHF, ISM, and cellular frequency bands in both narrowband and wideband operation. 

```{image} ad-jupiter-ebz-angle-web.jpg
:alt: Put Text Here to Describe the Image
:width: 400px
:align: right
```


<!-- ## Key Features
- Multi-Chip Synchronization (MCS)
- Fast profile switching
- Fast frequency hopping
- Integrated digital pre-distortion (DPD)
  -->

## Key Features
- Two fully integrated, fractional-N, RF synthesizers
- Fast profile switching
- Fast frequency hopping
- 2 × 2 highly integrated transceiver




## Some Use Cases
- Multi-Chip Synchronization (MCS)  
- Digital and Adaptive beamforming
- Field‑deployable signal collection and monitoring  
- MIMO 



<!-- Key transceiver capabilities include fast profile switching, fast frequency hopping, multi-chip synchronization (MCS), and integrated digital pre-distortion (DPD) for narrow and wideband waveforms. The device is designed with the RF performance vs. power consumption tradeoff in mind. The XCZU3EG processing device has a wide range of interfaces making the system capable of local processing or streaming to a remote host. 
-->


 <!-- ## Some Use Cases
- Rapid RF prototyping and waveform testing  
- Field‑deployable signal collection and monitoring  
- Multi‑antenna MIMO experimentation  
- Embedded Linux‑based SDR application development  
- Hardware‑in‑the‑loop algorithm validation -->

<!-- Insert Jupiter block Diagram here 
<p align="center">
<img src="ad-jupiter-ebz-angle-web.jpg" width="400">
</p>
-->


## Purpose
<!-- Need to link each one of these sections when they are spelled out in this paragraph -->
This documentation serves as a straight-forward, but detailed start-up guide for Jupiter. Topics covered are {ref}`hardware <adc-jupiter-hardware>`, {ref}`setup <adc-jupiter-setup>`, {ref}`software <adc-jupiter-software>`, and a more detailed {ref}`MCS Pilot <adc-jupiter-mcs-quick-start>`. Additional information regarding the Jupiter Platform can be found in the {ref}`reference design documentation <jupiter-sdr hardware-overview>`.

<!-- After following this documentation a user will be able to:

- Setup the hardware 
- Configure Jupiter 
- Use Python, MATLAB, and Scopy with Jupiter
- Use two Jupiters and a Synchrona for MCS and Beamforming -->



## Table of Contents
```{toctree}
:maxdepth: 1

Jupiter vs. Pluto <jup-v-plut/index>
Hardware <hardware/index>
Getting Started <setup/index>
Software <software/index>
Pilot <pilot/index>
```


<!-- ## Table of Contents - Still in progress
1. [Hardware](#Hardware/index.md)
    - [Synchrona](#Synchrona.md)
2. [Setup](#software-ecosystem)
    - [Assembly](#)
    - [SD Card Imaging](#)
3. [Software](#hardware-overview)
    - [Python Setup](#)
    - [MATLAB Setup](#)
    - [IIO_Oscilloscope](#)
4. [System Examples](#jupiter-vs-pluto) -->

<!-- Could make Jupiter vs. Pluto its own page -->
<!-- ## Jupiter vs. Pluto

A common question is: "How does Jupiter differ from Pluto?" Pluto (ADALM-PLUTO) is a software-defined radio platform that is geared toward flexibility and teaching electrical engineering topics like SDR, RF, and communications. The PlutoSDR is self-contained and is entirely USB-powered with the default firmware. It comes in at about $300 and is based on the AD9363 transceiver and the Zynq Z-7010 SoC. In contrast, the Jupiter SDR is about $4k, has a more powerful SoC, and allows for multiple-unit synchronization, where the Pluto does not. Another difference is that Pluto is more customizable, allowing easier changes to the LOs. While Pluto is typically used for education, Jupiter is typically used for industry applications in aerospace, defense, and communications.



| Feature | AD-JUPITER-EBZ | ADALM-PLUTO |
| --- | --- | --- |
| Transceiver | ADRV9002 | AD9363 |
| Multi-Chip Sync | Yes | No |
| DPD | Yes | No |
| Channels | 2Tx / 2Rx | 1Tx / 1Rx |
| Frequency Range | 30 MHz – 6 GHz | 325 MHz – 3.8 GHz |
| IBW | 12 KHz – 40 MHz | 20 MHz - 20 MHz |
| FPGA/SoC | Zynq Ultrascale+ MPSoC | Zynq Z-7010 |
| Form Factor | Ruggedized aluminum case | Small USB dongle |
| Power | USB-C / PoE | USB |

```{clear-content}
```
 -->

```{note}
For questions or help with the Jupiter SDR, please visit:
<br>
{ez}`fpga`
```