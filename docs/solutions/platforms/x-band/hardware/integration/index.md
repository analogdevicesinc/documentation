# System Integration

```{image} ../XBDEV_BD_#2.png
:alt: X-Band Development Platform Block Diagram
:width: 100%
```

This section covers how the three main boards of the X-Band platform work together to create a complete hybrid beamforming phased array system.

## System Architecture Overview

The X-Band Development Platform implements a hybrid beamforming architecture that combines:
- **Analog beamforming** via ADAR1000EVAL1Z (32 channels)
- **Digital beamforming** via AD9081-FMCA-EBZ (4 digital channels)
- **Frequency conversion** via ADXUD1AEBZ (X-Band ↔ C-Band)
- **FPGA processing** via ZCU102 (control and algorithms)

## Signal Flow Architecture

**Receive Path**

```
Antenna → ADAR1000 → XUD1A → AD9081 → ZCU102
(32ch)     (32→4)    (X→C)    (4)     (Processing)
```

1. **32 Antenna Elements** collect RF signals at X-Band frequencies
2. **ADAR1000 Analog Beamforming** combines 8 channels into 4 subarrays
3. **XUD1A Up/Down Conversion** translates X-Band RF to C-Band IF
4. **AD9081 Digitization** converts 4 analog IF to 8 digital channels
5. **ZCU102 Processing** performs digital beamforming and signal processing

**Transmit Path**

```
ZCU102      → AD9081 → XUD1A → ADAR1000 → Antenna
(Processing)   (4)     (C→X)    (4→32)     (32ch)
```

1. **ZCU102 Processing** generates digital waveforms (up to 8 channels)
2. **AD9081 DACs** convert digital signals to 4 analog IF channels
3. **XUD1A Up Conversion** translates C-Band IF to X-Band RF
4. **ADAR1000 Power Division** distributes 4 channels to 32 antenna elements
5. **32 Antenna Elements** radiate coherent X-Band signals

## Subarray Architecture

**Four 8:1 Subarrays**

The system is organized into four identical subarrays, each containing:
- **2x ADAR1000 ICs** (8 channels total per subarray)
- **1x Power Splitter/Combiner** (ZX10-2-183-S+)
- **1x XUD1A Channel** for frequency conversion
- **1x AD9081 ADC/DAC pair** for digitization

```
Subarray 1: ADAR1000 Ch 1-8  ↔ Combiner ↔ XUD1A Ch 1 ↔ AD9081 ADC0/DAC0
Subarray 2: ADAR1000 Ch 9-16 ↔ Combiner ↔ XUD1A Ch 2 ↔ AD9081 ADC1/DAC1  
Subarray 3: ADAR1000 Ch17-24 ↔ Combiner ↔ XUD1A Ch 3 ↔ AD9081 ADC2/DAC2
Subarray 4: ADAR1000 Ch25-32 ↔ Combiner ↔ XUD1A Ch 4 ↔ AD9081 ADC3/DAC3
```

**Hybrid Beamforming Benefits**

This architecture provides:
- **Analog beamforming**: Fast, low-power steering within each subarray
- **Digital beamforming**: Flexible, adaptive processing between subarrays
- **Reduced digital complexity**: Only 4 digital channels vs 32
- **Maintained flexibility**: Full beam control through combined analog/digital processing

## Frequency Plan

**X-Band RF Operation**

- **Target Frequency**: 10 GHz (center of X-Band)
- **RF Range**: 8-12 GHz (X-Band)
- **Element Spacing**: 15mm (optimized for 10 GHz)

**IF Processing**

- **IF Frequency**: C-Band — recommended **4.5 GHz – 4.8 GHz** between XUD1A and AD9081
- **LO Options**: External or ADF4371 internal PLL
- **Default LO**: Configurable based on application
- **IF Bandwidth**: Determined by AD9081 settings

**Digital Processing**

- **ADC Sampling**: Up to 4 GSPS per channel
- **DAC Sampling**: Up to 12 GSPS per channel
- **Digital Channels**: 8 RX, 8 TX (from 4 RF channels)
- **NCO Flexibility**: Channel and main NCOs for fine frequency control

## Control Architecture

**IIO Devices**

All system components are controlled through IIO (Industrial I/O) devices:

| Device | IIO Name | Function |
|--------|----------|----------|
| ADAR1000 #1-8 | adar1000_csb_x_x | Analog beamforming control |
| ADF4371 | adf4371-0 | LO generation (if used) |
| AD9081 RX | axi-ad9081-rx-hpc | Digital receive processing |
| AD9081 TX | axi-ad9081-tx-hpc | Digital transmit processing |
| XUD1A | xud_control | X-Band up/down converter control |
| TDD Core | axi-core-tdd | Time division duplexing |


## Interconnect Requirements

**Digital Connections**

- **AD9081 ↔ ZCU102**: FMC HPC0 connection with riser
- **Interposer ↔ ZCU102**: FMC HPC1 connection with cable extension
- **Stingray ↔ ZCU102**: Dual PMOD connections with adapters

**RF Connections**

- **8x SMA-SMPM cables**: AD9081 ↔ XUD1A
- **4x Power splitters**: XUD1A → splits each channel to 2 input/outputs
- **8x SMA-SMPM cables**: Power splitters ↔ Stingray ADAR1000s
- **32x SMPM bullets**: Stingray ADTR1107s ↔ Antenna tiles

**Optional Inline Filters** *(recommended for improved spectral purity)*

| Filter | Path | Qty |
|--------|------|-----|
| Mini-Circuits VLF-8400+ | AD9081 ADC ↔ XUD1A (RX) | 4 |
| Mini-Circuits VLF-5500+ | AD9081 DAC ↔ XUD1A (TX) | 4 |

**Power Distribution**

- **ZCU102**: 12V supply powers AD9081 via FMC
- **XUD1A**: Dedicated 12V supply (~15W)
- **Stingray**: Dedicated 12V supply (~30W)

## Timing and Synchronization

**Clock Distribution**

- **Master Clock**: 100 MHz reference (external or internal)
- **HMC7044**: Clock distribution and jitter attenuation
- **AD9081**: On-chip PLLs for ADC/DAC clocks
- **Phase Coherence**: Maintained across all channels

**TDD Coordination**

- **TDD Engine**: FPGA-based timing control
- **Global Sync**: Coordinates all three boards
- **ADC/DAC Sync**: Synchronized sampling and generation across all channels

## Calibration Strategy

**System-Level Calibration**

1. **Individual Channel Cal**: Per-ADAR1000 channel calibration
2. **Subarray Cal**: Per-subarray amplitude/phase matching
3. **Digital Cal**: AD9081 channel matching
4. **End-to-End Cal**: Full system calibration via known signals

**Calibration Tools**

- **Built-in Detectors**: ADAR1000 power detection
- **Digital Loopback**: AD9081 internal test modes
- **External Signals**: Controlled calibration sources
- **Over-the-Air**: Pattern measurement and correction

```{note}
The hybrid architecture provides both the flexibility of digital beamforming and the efficiency of analog beamforming, making it ideal for radar, EW, and SATCOM applications requiring both performance and power efficiency.
```
