<!--
Tasks left to be done:
    1. Decide what should be said for the I/O section. Maybe take out bit about I/O in first paragraph
    2. Add a link to the more in depth hardware explanation (on github)
    3. General Formatting/Proof-reading
 -->
(adc-jupiter-hardware)=
# Hardware
This page covers the basics of Jupiter hardware and what a user should know to use the hardware. An in-depth hardware guide can be found {ref}`here <jupiter-sdr hardware-overview>`.

## I/O

 In terms of I/O, Jupiter exposes 10 SMA connectors on the front panel for Tx, Rx, MCS, and external device clock (DEV CLK) signals. Host interfaces include Gigabit Ethernet, USB 3.1, DisplayPort, and a GPIO interface. The board supports two power input options, USB-C and Power over Ethernet (PoE).

```{image} resources/ad-jupiter-ebz-angle-web.jpg
:alt: Put Text Here to Describe the Image
:width: 600px
:align: left
```

```{image} resources/ad-jupiter-ebz-back-web.png
:alt: Put Text Here to Describe the Image
:width: 800px
:align: right
```

```{clear-content}
```
### Configurations
There are two configurations for Jupiter: Host Computer Mode and Standalone Mode.

**Host Computer Mode**
- Micro-USB cable
- USB Type-C cable (or Ethernet cable)
- USB Type-C Power Supply


```{image} resources/hostcomputer-mode.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

**Standalone Mode**
- DisplayPort compatible Monitor
- USB Type-C multiport hub, mouse and keyboard
- USB Type-C Power Supply


```{image} resources/stand-alone-mode.png
:alt: Put Text Here to Describe the Image
:width: 500px
:align: center
```


<!-- - **Processing**
  - XCZU3EG Zynq UltraScale+ MPSoC
  - Integrated programmable logic and ARM processing system

- **Memory & Storage**
  - 2 GB DDR4 system memory
  - 64 MB QSPI flash
  - microSD card slot for removable storage

- **RF Subsystem**
  - ADRV9002 dual‑channel RF transceiver
  - Independent transmit and receive paths
  - Dedicated RF front‑end section

- **Clocking & Synchronization**
  - AD9542 clock generator
  - ADCLK925 clock fanout devices
  - Support for LO and multichip synchronization
  - External clock, LO, and sync inputs

- **Power**
  - Onboard power supply with power‑path selection
  - Supports 5 V and 9 V inputs
  - Power‑over‑Ethernet (PoE) support

- **Interfaces**
  - Micro‑USB UART via FT230XQ bridge -->

<!-- Jupiter integrates the XCZU3EG Zynq UltraScale+ MPSoC at the center of the design, interfacing with a 2 GB DDR4 memory subsystem and 64 MB of QSPI flash. The MPSoC communicates directly with the ADRV9002 RF transceiver, which provides dual‑channel transmit and receive paths feeding a dedicated RF front‑end section. Clocking is managed through an AD9542 clock generator, along with ADCLK925 fanout devices for LO and multichip synchronization distribution. Power is provided through an onboard supply capable of sourcing 5V and 9V inputs, including PoE support, with a power‑path selector. The system also incorporates microSD storage, a micro‑USB UART interface through an FT230XQ bridge, and an external clock, LO, and synchronization inputs to support RF timing.  -->

## RF Front-End

```{image} resources/jupiter-rf-fe.png
:alt: Put Text Here to Describe the Image
:width: 400px
:align: right
```


- **Receive Channels (Main Board – RX A)**
  - RX1A and RX2A exposed on the front panel
  - Connected to ADRV9002 Rx A channels
  - Wideband frequency range: **100 MHz to 6 GHz**
  - Bypassable HMC8414 LNA
  - HMC8038 non‑reflective SPDT switch
    - Supports internal calibration with 50 Ω termination
  - TCM1‑83X+ Mini‑Circuits balun
  - Calibration switch controlled by driver (not user‑accessible)

- **Receive Channels (Main Board – RX B)**
  - RX1B and RX2B connected to ADRV9002 Rx B channels
  - Routed to the RF Add‑On board via u.FL cables
  - Includes the same SPDT switch and balun as RX A paths

- **Transmit Channels**
  - TX1A and TX2A exposed on the front panel
  - Connected to ADRV9002 Tx channels
  - TCM1‑83X+ balun on each transmit path
  - ADRF5040 three‑way non‑reflective RF switch
    - Supports TX output disconnection during internal calibration
    - Supports routing TX path to RF Add‑On board
  - User‑selectable attributes for:
    - TX1A vs TX1B
    - TX2A vs TX2B

<!-- The main board expose to the front panel two wide band receive channels RX1A and RX2A which are connected to the ADRV9002 transceiver Rx A channels. The receive path consist of a by-passable LNA HMC8414, a non-reflective SPDT switch HMC8038 that allows to terminate with 50 ohms the RX input during internal calibration and a TCM1-83X+ MiniCircuits balun. The control of calibration switch is done by the driver and is not exposed to the user. The frequency range of the main board RX1A and RX2A paths is 100 MHz to 6 GHz.

On the main board there are another two receive channels RX1B and RX2B which are connected to Rx B channels of ADRV9002. These receive channels are connected to the RF add-on board through uFL cables and also have the same SPDT switch and balun as on the RX A channels.

The main board also expose to the front panel two transmit channels TX1A and TX2A which consists of a TCM1-83X+ balun and a three way non-reflective switch ADRF5040 which allows disconnecting the TX output during internal calibration or connecting the transmit path to the RF Add-on board. There are some attributes exposed to the user that allows selecting between TX1A and TX1B respective TX2A and TX2B. (link to command example) -->

```{clear-content}
```
## Block Diagram

```{image} resources/jupiter-hardware-bd.png
:alt: Figure 1: Jupiter Block Diagram
:width: 800px
:align: center
```



```{list-table}
:widths: 33 33 33
:class: feature-grid

* - **Processing**
    - XCZU3EG Zynq UltraScale+ MPSoC  
    - ARM PS
    - Integrated PL
  - **Memory & Storage**
    - 2 GB DDR4  
    - 64 MB QSPI  
    - microSD card
  - **RF Subsystem**
    - ADRV9002 dual‑channel  
    - Independent TX/RX  
    - RF front‑end

* - **Clocking & Sync**
    - AD9542 clock generator  
    - ADCLK925 fanout  
    - Multichip sync
  - **Power**
    - 5V input
    - 9V input
    - PoE support
  - **Interfaces**
    - Micro‑USB UART
    - Display Port
    - USB 3.1

```



<!-- ## Hardware Pages
```{toctree}
:maxdepth: 1

Hardware
RF_Splitter_Antenna/index

``` -->

 <!-- Jupiter also has USB 3.1, supported by a USB 3.0 PHY, a USB Type‑C power‑delivery controller, and a signal mux/redriver. Additional I/O includes Gigabit Ethernet via the ADIN1300 PHY, SATA, DisplayPort, GPIO, and MIPI connections, all routed into the MPSoC’s general‑purpose interfaces. -->
```{clear-content}
```
```{note}
For questions or help with the Jupiter SDR, please visit:
<br>
{ez}`fpga`
```

