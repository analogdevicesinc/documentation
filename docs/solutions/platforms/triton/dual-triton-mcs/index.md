# Dual Triton MultiChip Sync (MCS) Pilot Overview

This section provides the steps required to setup the Dual Triton MCS Demo, which consists of two 16T/16R Triton Development Platforms and a [**Aion (ADF4030) Evaluation Board**](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adf4030.html). The pilot demonstrates the usage of the Aion sync device to align the BSYNCs from the EVAL-ADF4030 and have these drive each Triton as external BSYNC inputs. The pilot then has the Leader Triton transmit a DAC signal and loop it back into one of its own ADCs and also send it to an ADC on the Follower Triton. The ADC data from both platforms are then post processed and the delay calculated to demonstrate accuracy of +/-5 picoseconds.

## Block Diagram

The figure below provides a high level block diagram of the required connections for the system as well as the PMOD connections required for triggering of the system.

```{image} images/dual-triton-mcs-block-diagram.png
:width: 700px
:align: center
```

```{image} images/dual-triton-mcs-pmod-connections.png
:width: 700px
:align: center
```

## Hardware Requirements

The following hardware is needed to successfully setup this pilot:
- 2 x [Triton Development Platforms](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
- 1 x [Aion (ADF4030) Evaluation Platform + Interposer Board](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adf4030.html)
- 2 x [Xilinx/AMD VCU118 FPGA Board](https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/vcu118.html)
- 1 x RF Signal Generator supporting up to 400MHz as a reference frequency for each Triton
- 1 x RF Power Splitter to distribute the 400MHz to each Triton [2-Way Power Splitter 0.5 - 600MHz (Mini-Circuits)](https://www.minicircuits.com/WebStore/dashboard.html?model=Z99SC-62-S%2B)
- 1 x RF Power Splitter to distribute the DAC Transmission at X-Band to the Leader & Follower ADC's [4-Way Power Splitter 500 - 26500 MHz (Mini-Circuits)](https://www.minicircuits.com/WebStore/dashboard.html?model=ZC4PD-5R263-S%2B)

## Software Requirements

As there are two Triton Platforms used in this pilot, one as a Leader and the other a Follower, we need to load these with two different HDL images.

```{warning}
 Weblinks are to the System Platforms Teams Channel, these will be updated following release
```

- [Triton Leader HDL Image](https://analog.sharepoint.com/:f:/r/sites/ADC_System_Platforms_Team/Shared%20Documents/General/Transfer/Temp_Dual_Triton_MCS/primary?csf=1&web=1&e=bQhbBD)
- [Triton Follower HDL Image](https://analog.sharepoint.com/:f:/r/sites/ADC_System_Platforms_Team/Shared%20Documents/General/Transfer/Temp_Dual_Triton_MCS/second?csf=1&web=1&e=0MEBLD)

## Bring Up Steps 
```{toctree}
:maxdepth: 4

Aion EVB Initialisation <aion-init/index>
Triton Initialisation <triton-init/index>
Python Script Execution <python-exe/index>

```

```{note}
This resource list is regularly updated. For the most current information and additional resources, please visit the individual product pages and the ADI wiki.
```


## Additional Links

- [Analog Devices Main Website](https://www.analog.com/)
- [ADI Wiki](https://wiki.analog.com/)
- [Engineering Zone Forums](https://ez.analog.com/)
- [Triton Development Platform Product Page](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
