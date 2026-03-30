(adc pluto)=
# Pluto

## Overview

```{image} ../resources/pluto.png
:alt: PlutoSDR Picture
:width: 400px
:align: right
```  

The [ADALM‑PLUTO](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html), commonly known as the Pluto SDR, is a portable, self‑contained software‑defined radio (SDR). It is designed primarily as an educational platform for students, hobbyists, and engineers to explore radio frequency (RF) concepts, wireless communication, and SDR fundamentals in a hands‑on environment.  PlutoSDR acts as a personal RF lab that easily fits into a pocket and connects to a computer over USB. It supports a wide range of software environments including MATLAB, GNU Radio, C/C++/C#, Python, and SDRangel.

***Key Features and Specs***
- **Hardware:**  Based on the AD9363 RF Transceiver and the Xilinx Zynq Z-7010 FPGA
- **RF Coverage:**  325 MHz to 3.8 GHz (guaranteed), 70MHz to 6 GHz (firmware modification)
- **Instantaneous Bandwidth:**  20 MHz (guaranteed), 56 MHz (firmware modification)
- **Channels:**  1 Transmit (DAC) and 1 Receive (ADC).  Upgradeable to 2 transmit and 2 receive channels.  
- **Platforms:** Compatible with Windows, Linux, and macOS
- **Full Duplex Operation** (can simultaneously send and receive)

Complete documentation, user manuals, and examples for the Pluto are found here:
[https://analogdevicesinc.github.io/documentation/tools/pluto/index.html
](https://analogdevicesinc.github.io/documentation/tools/pluto/index.html
)

The below guide is meant to highlight important aspects of Pluto and guide the user through a couple of complete system level examples.  

## Table of Contents
 
```{toctree}
:maxdepth: 2

Hardware Introduction <hardware/index>
Unboxing and Getting Started <get-started/index>
Additional Setup Tips <setup/index>
Simple Programming <software/index>
System Examples (Pilots) <pilots/index>
```

 ---

 
This video is a quick introduction to the Pluto platform along with some simple examples:

```{video} https://www.youtube.com/watch?v=ZnCi-LHJ0GQ
:align: left
```

```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
