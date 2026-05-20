(adc x-band-dev-kit)=
# X-Band Phased Array Development Platform

The [**X-Band Phased Array Development Platform**](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform.html) is a complete system solution designed for phased array radars, electronic warfare, and ground-based SATCOM applications. It provides a testbed for demonstrating hybrid beamforming phased array radar as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms.

```{image} xbdev-box.png
:alt: X-Band Development Platform Kit
```

The platform consists of three main components:
- **[AD9081-FMCA-EBZ](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9081.html)** - AD9081 MxFE Evaluation Board
- **[ADXUD1AEBZ](https://wiki.analog.com/resources/eval/user-guides/xud1a)** - X/C Band Up/Down Converter  
- **[ADAR1000EVAL1Z](https://wiki.analog.com/resources/eval/user-guides/stingray/userguide)** - X/Ku-Band Analog Beamforming Board (Stingray)

The system is designed to mate with a [ZCU102](https://www.xilinx.com/ZCU102) Evaluation Board from Xilinx®, featuring the Zynq® UltraScale+™ ZU9EG FPGA, with provided reference software, HDL code, and MATLAB/Python system-level interfacing.

## Target Applications

The X-Band Development Platform enables quick time-to-market development programs for:

- **ADEF (Phased-Array, RADAR, EW, SATCOM)**
- **Hybrid Beamforming**
- **Electronic Test and Measurement**

## Table of Contents
```{toctree}
:maxdepth: 2

Hardware Introduction <hardware/index>
Unboxing and Initial Setup <setup/index>
pyRadar <pyradar/index>
Troubleshooting <troubleshooting/index>
Additional Resources <resources/index>
```

## System Overview

The X-Band Development Platform highlights a complete system solution specifically targeting a 32-channel transmit/32 receive hybrid beamforming phased array. It is intended as a testbed for demonstrating phased array system level calibrations, hybrid beam forming (analog/digital) algorithms, and other signal processing algorithms.

```{note}
For questions or help with the X-Band Development Platform, please visit:\
[https://ez.analog.com/adef-system-platforms/](https://ez.analog.com/adef-system-platforms/)
```  

