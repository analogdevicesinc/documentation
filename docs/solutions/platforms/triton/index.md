(adc triton)=
# Triton (Quad Apollo) Development Platform

The Quad-Apollo MxFE™ (mixed-signal front-end) X-band direct sampling digital beamforming platform is an advanced, every-element digital, direct RF-sampling solution that serves as a complete reference architecture for next-generation digital beamforming systems. Designed to highlight the capabilities of Analog Devices’ MxFE® technology, the platform integrates all critical subsystems—RF signal conditioning, precision clocking, multichip synchronization, and DC power management—into a unified, high performance environment that supports coherent, scalable signal processing across multiple channels.

The platform enables quick time-to-market development programs for: Phased-Array, RADAR, Electronic Warfare and SATCOM

The system is designed to mate with a [VCU118](https://www.xilinx.com/VCU118) Evaluation Board from Xilinx®, featuring the Virtex™ UltraScale+™ XCVU9P-L2FLGA2104E FPGA, with provided reference software, HDL code, and MATLAB/Python system-level interfacing.

```{image} images/adxband16ebz-top-angle-evaluation-board.png
:width: 700px
:align: center
```


## Triton Documentation Support 

As a released platform, Triton has its own product page where the user guide, bring up guide and associated technical articles are hosted to assist users of the system. Below are the links:

```{warning}
 Weblinks must be updated following release - placeholder only
```

- [**Triton Development Platform - Product Page**](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
- [**Triton Development Platform - User Guide**](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
- [**Triton Development Platform - Bring Up Guide**](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
- [**Triton Development Platform - Technical Articles**](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)

## Triton Software Support 

The Triton Quad Apollo has two HDL Images (Hardware Description Language) available for users. As outlined in the table below, both images are operating at 12.8 GHz Sample Clock and the only difference between the two configurations is the resulting usable instantaneous Bandwidth (iBW); 320 MHz vs. 640 MHz
Below are the links to the two images and the user should reference the Bring Up Guide documentation for the steps to program the system.

```{warning}
 Weblinks must be updated following release - placeholder only
```
- [** 320 MHz iBW **](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)
- [** 640 MHz iBW **](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adxband16ebz.html)

```{image} images/adxband16ebz-available-configurations.png
:width: 700px
:align: center
```

## Triton System Platforms - Demo & Pilots

The System Platform team are here to support customers in the integration of this platform, whether that is as a standalone system or a sub-assembly in a larger system, we can help. To this end, we have generated the following pilot we believe you will find useful


```{toctree}
:maxdepth: 2

Dual Triton MultiChip Sync (MCS) Pilot <dual-triton-mcs/index>
```

```{note}
For questions or help with the Triton Development Platform, please visit:
<br>
[https://ez.analog.com/adef-system-platforms/](https://ez.analog.com/adef-system-platforms/)
```  

