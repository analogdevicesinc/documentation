# ADXUD1A Up/Down Converter

The ADXUD1AEBZ is a quad-channel X/C band frequency converter that bridges the gap between X-Band RF signals (8–12 GHz) used by the ADAR1000 beamforming board and the C-Band IF signals (4.2–6.3 GHz) that the AD9081 MxFE can process.

```{figure} eval-adxud1aebz_angle.jpg
:width: 300px
:align: center

ADXUD1AEBZ Up/Down Converter Board
```

## Overview

The ADXUD1AEBZ provides four independent up/down converter channels. Each channel contains a mixer (HMC773A), IF amplifiers (ADL8111, HMC8411), TX/RX amplifiers (HMC903), and an RF switch (ADRF5020) for TX/RX path selection. A common LO distribution network feeds all four channels from either an external source or the on-board ADF4371 PLL.

```{tip}
**Schematics & Resources**
- {download}`ADXUD1AEBZ Schematic (Rev D) <resources/adxud1a_schematic_revD.pdf>`
- {download}`ADXUD1AEBZ BOM <resources/adxud1a_bom.zip>`

**Interposer Board**
- {download}`Interposer Schematic (Rev B) <resources/interposer_schematic_revB.pdf>`
- {download}`Interposer BOM (Rev B) <resources/interposer_bom_revB.zip>`

**Component Product Pages**
- :adi:`ADF4371 <en/products/adf4371.html>` - Microwave Wideband Synthesizer with Integrated VCO
- :adi:`HMC773A <en/products/hmc773a.html>` - GaAs MMIC Fundamental Mixer
- :adi:`ADL8111 <en/products/adl8111.html>` - IF Variable Gain Amplifier
- :adi:`HMC8411 <en/products/hmc8411.html>` - GaAs pHEMT MMIC Low Noise Amplifier
- :adi:`HMC903 <en/products/hmc903.html>` - GaAs pHEMT MMIC Driver Amplifier
- :adi:`ADRF5020 <en/products/adrf5020.html>` - Silicon SPDT Switch
```

## Block Diagram

```{figure} xud1a_revd_blockdiagram.png
:width: 75%
:align: center

ADXUD1AEBZ Rev D Block Diagram
```

## Key Specifications

| Parameter | Value |
|-----------|-------|
| **RF Frequency Range** | 8 – 12 GHz |
| **IF Frequency Range** | 4.2 – 6.3 GHz |
| **Number of Channels** | 4 (independent TX/RX) |
| **RF Connectors** | 4× SMA-F |
| **IF Connectors** | 8× SMPM (4 TX + 4 RX) |
| **LO Input** | SMA-F (external) or on-board ADF4371 |
| **Supply Voltage** | 12V DC |
| **Power Consumption** | ~15W |

## RF Performance

### Receive — High Gain Mode

| Frequency | Gain (dB) | Noise Figure (dB) | IIP3 (dBm) |
|-----------|-----------|-------------------|------------|
| **8 GHz** | 14.63 | 14.72 | 7.59 |
| **12 GHz** | 13.38 | 16.17 | 10.40 |

```{figure} rx_hg_s21.png
:width: 50%
:align: center

RX High Gain — Conversion Gain (S21)
```

```{figure} rx_hg_nf.png
:width: 50%
:align: center

RX High Gain — Noise Figure
```

```{figure} rx_hg_iip3.png
:width: 50%
:align: center

RX High Gain — IIP3
```

### Receive — Low Gain Mode

Approximately 14 dB lower gain than high-gain mode with improved linearity.

```{figure} rx_lg_s21.png
:width: 50%
:align: center

RX Low Gain — Conversion Gain (S21)
```

```{figure} rx_lg_nf.png
:width: 50%
:align: center

RX Low Gain — Noise Figure
```

```{figure} rx_lg_iip3.png
:width: 50%
:align: center

RX Low Gain — IIP3
```

### Transmit Mode

| Parameter | Value |
|-----------|-------|
| **Conversion Gain** | −12 to −14 dB |
| **OIP3** | Comparable to RX IIP3 |

```{figure} tx_s21.png
:width: 50%
:align: center

TX — Conversion Gain (S21)
```

```{figure} tx_oip3.png
:width: 50%
:align: center

TX — OIP3
```

### Return Loss

```{figure} rx_hg_s11.png
:width: 50%
:align: center

RX High Gain — S11 (RF Input)
```

```{figure} rx_hg_s22.png
:width: 50%
:align: center

RX High Gain — S22 (IF Output)
```

```{figure} rx_lg_s11.png
:width: 50%
:align: center

RX Low Gain — S11 (RF Input)
```

```{figure} rx_lg_s22.png
:width: 50%
:align: center

RX Low Gain — S22 (IF Output)
```

```{figure} tx_s11.png
:width: 50%
:align: center

TX — S11 (IF Input)
```

```{figure} tx_s22.png
:width: 50%
:align: center

TX — S22 (RF Output)
```

## Board Architecture

### Key Components

| Component | Function |
|-----------|----------|
| **ADRF5020** | RF TX/RX switch (4× per board) |
| **HMC773A** | Mixer — frequency conversion |
| **HMC903** | TX/RX RF amplifier |
| **ADL8111** | IF variable-gain amplifier |
| **HMC8411** | IF amplifier |
| **ADF4371** | On-board wideband PLL/VCO (optional LO) |

### Connector Layout

```{figure} eval-adxud1aebz_top-web.gif
:width: 50%
:align: center

ADXUD1AEBZ Top View — Connector Locations
```

```{figure} eval-adxud1aebz_bottom.jpg
:width: 50%
:align: center

ADXUD1AEBZ Bottom View
```

## Control Interface

```{figure} xud1a_controlblockdiagram.png
:width: 50%
:align: center

XUD1A Control Block Diagram
```

Digital control operates at **1.8V logic** with on-board level translation to 3.3V. Two interface options are available:

### PMOD Interface

```{figure} xud1a_pmod.png
:width: 50%
:align: center

XUD1A PMOD Connector Pinout
```

The PMOD connector enables GPIO and SPI communication for:
- Per-channel TX/RX switching
- Switchable receive gain (high/low)
- SPI programming of the ADF4371 PLL

### SDP-S Interface

```{figure} xud1a_sdps.png
:width: 50%
:align: center

XUD1A SDP-S Connector
```

Alternative control path via the SDP-S connector for standalone evaluation without an FPGA.

### Connection to ZCU102

- **ZCU102 HPC1 Connector** → FMC extension cable → Interposer Board → PMOD cable → XUD1A
- **Optional**: 14-pin 6-inch PMOD cable for easier RF access when shields are installed

## LO Configuration

The ADXUD1AEBZ supports both **external** and **internal** LO sources:

- **External LO (default)**: Signal fed via SMA-F connector, distributed to all four channels through an on-board splitter network
- **On-board ADF4371 PLL**: Generates LO internally using a 100 MHz on-board VCXO reference or an external reference clock

Refer to the {ref}`Clocking Configuration <x-band-clocking>` page for details on switching between these options.

## Switching Speed

Measured TX/RX switching performance:
- **Rising edge**: ~159 ns average
- **Falling edge**: ~14 ns average

```{note}
The on-board IF bandpass filters (FL3, FL6, FL7, FL8) provide basic filtering. Additional external filters (VLF-8400+, VLF-5500+) are recommended for optimized system performance to suppress mixing products, LO feedthrough, and DAC images.
```
