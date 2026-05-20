# Hardware Introduction

The X-Band Phased Array Development Platform consists of three main evaluation boards that work together to provide a complete hybrid beamforming phased array system. The platform is designed to demonstrate phased array concepts for radar, electronic warfare, and SATCOM applications.

```{image} XBDEV_BD_#2.png
:alt: X-Band Development Platform Block Diagram
```

## System Components

The X-Band Development Platform consists of 3 main parts, all designed to work together:

1. **AD9081-FMCA-EBZ MxFE Evaluation Board**

   The MxFE board provides the digital signal processing and data conversion capabilities. It features high-speed ADCs and DACs with flexible digital processing.

2. **ADXUD1AEBZ X/C Band Up/Down Converter**

   The up/down converter translates between X-Band RF frequencies and C-Band IF frequencies, providing the frequency translation needed for the system.

3. **ADAR1000EVAL1Z X/Ku-Band Analog Beamforming Board (Stingray)**

   The analog beamforming board provides 32-channel phased array capability with individual phase and amplitude control for each channel.

4. **Xilinx ZCU102 Evaluation Board (Not Included)**

   The FPGA development board provides the processing platform and interfaces with the MxFE board via FMC connector.

## Architecture Overview

The X-Band platform implements a hybrid beamforming architecture combining:
- **32-channel analog beamforming** via ADAR1000 ICs
- **4-channel digital beamforming** via AD9081 MxFE  
- **X-Band to C-Band frequency conversion** via ADXUD1A
- **FPGA-based control and processing** via ZCU102

This hybrid approach provides the efficiency of analog beamforming with the flexibility of digital processing, enabling complex radar, EW, and SATCOM applications.

```{toctree}
:maxdepth: 1

AD9081 MxFE <mxfe/index>
ADXUD1A Up/Down Converter <converter/index>
ADAR1000 Beamforming Board <beamforming/index>
System Integration <integration/index>
Clocking Architecture <clocking/index>
Time Division Duplexing <tdd/index>
```

```{note}
For detailed specifications and schematics for each board, please refer to the individual evaluation board documentation linked in the Resources section.
```
