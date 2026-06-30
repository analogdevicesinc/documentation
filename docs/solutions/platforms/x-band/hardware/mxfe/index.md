# AD9081 MxFE Details

The AD9081-FMCA-EBZ is the heart of the digital signal processing in the X-Band platform, providing high-speed data conversion and flexible digital processing capabilities.

```{image} ad9081-fmca-ebzangle-web.gif
:alt: AD9081-FMCA-EBZ Board
```

## Overview

The AD9081 Mixed-Signal Front End (MxFE) combines high-performance ADCs and DACs with advanced digital signal processing in a single chip solution. When paired with the ZCU102 FPGA board, it provides a complete digital RF processing platform.

```{tip}
**Schematics & Resources**
- [AD9081-FMCA-EBZ Schematic (Rev C)](https://www.analog.com/media/en/technical-documentation/eval-board-schematic/ad9081-mxfe-fmca-revc-eval-board-schematic.pdf)
- [AD9081-FMCA-EBZ Design Files Rev. D (ZIP)](https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/ad9081-ad9082.zip)
- [AD9081 Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad9081.pdf)
- [AD9081-FMCA-EBZ User Guide (UG-1829)](https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf)
- :external+linux:doc:`Linux Driver Documentation <drivers/iio-mxfe/ad9081>`

**Component Product Pages**
- [AD9081](https://www.analog.com/en/products/ad9081.html) - MxFE Quad, 16-Bit, 12 GSPS DAC / Quad, 12-Bit, 4 GSPS ADC
- [AD9081 Eval Board (EVAL-AD9081)](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9081.html)
```

## Key Features

**Receive Path (ADC)**

- **4x RF Receive (Rx) Channels (8x Digital Rx Channels)**
- **Total 4x 12-bit 4GSPS ADC**
- **8x Digital Down Converters (DDCs)**
- **Complex Numerically-Controlled Oscillators (NCOs)**
- **8x Programmable Finite Impulse Response Filters (pFIRs)**

**Transmit Path (DAC)**

- **4x RF Transmit (Tx) Channels (8x Digital Tx Channels)**
- **Total 4x 16-bit 12GSPS DAC**
- **8x Digital Up Converters (DUCs)**
- **Complex Numerically-Controlled Oscillators (NCOs)**

**Clock Distribution**

- **Flexible Clock Distribution**
- **On-Board Clock Distribution from Single External 100MHz Reference**
- **Support for External Converter Clock**
- **HMC7044 Clock Jitter Attenuator**

## Board Features

**Power Requirements**

- **Powered via FMC connector** from ZCU102 board
- **No external power required**
- **On-Board Power Regulation** via LTM4616 power modules

**Connectivity**

- **Mates with Xilinx ZCU102 Evaluation Board** via HPC0 FMC connector
- **SMA connectors** for ADC and DAC RF interfaces
- **SMPM connectors** for external clock references

## Installation Requirements

**Hardware Requirements**

- **FMC Riser**: Required to raise the AD9081 board for proper ZCU102 fit
- **SMA-SMPM Cables**: 8x cables needed for connections to XUD1A
- **ZCU102 FPGA Board**: Host platform (not included with X-Band kit)
