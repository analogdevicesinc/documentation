# Jupiter MCS Pilot
The Jupiter MCS pilot uses two Jupiters and a Synchrona to perform MCS and beamforming. The official MCS Pilot can be found [here]({wiki}`resources/eval/user-guides/jupiter_sdr/mcs?s%5b%5d=jupiter`). This guide aims to be a comprehensive summary that provides a clear user experience. 

This pilot will go over the following:

- Theory
- How to configure the Jupiter
- Sine Sync 
- Reload Profile Sync
- DOA
- DOA Tracking


```{image} mcs-quick-start/jupiter-mcs-pilot-cartoon.jpg
:alt: MCS Block Diagram
:width: 800px
:align: center
```

## Table of Contents
```{toctree}
:maxdepth: 1

Pilot specific Hardware <rf-splitter-antenna/index>
Synchrona <synchrona/index>
Setting up Pilot Hardware <mcs-quick-start/index>
Walkthrough <walkthrough/index>

```

The code for this pilot exists in the PyADI-IIO library under the folder labeled "adrv9002_mcs_sync".
```{clear-content}
```
```{note}
For questions or help with the Jupiter SDR, please visit:
<br>
{ez}`fpga`
```

