# Unboxing and Initial Setup

This section provides step-by-step instructions for unboxing, assembling, and performing initial setup of the X-Band Phased Array Development Platform.

## Quick Start Guide

For complete setup of your X-Band platform, follow these guides in order:

1. **[Hardware Assembly](assembly/index.md)** - Assemble all boards and make connections
2. **[ZCU102 Configuration](zcu102config/index.md)** - Configure boot mode, USB, and network settings
3. **[SD Card Configuration](sdcard/index.md)** - Format, flash, and prepare the boot media
4. **[EEPROM Programming](eeprom/index.md)** - Program the FMC EEPROM for proper VADJ power


```{tip}
**First Time Setup**: Follow the guides above in sequence. Each step builds on the previous one.
```

## What's Included

The X-Band Phased Array Development Platform includes:

**In the Box:**

- **1x AD9081-FMCA-EBZ** - AD9081 MxFE Evaluation Board
- **1x ADXUD1AEBZ** - X/C Band Up/Down Converter
- **1x ADAR1000EVAL1Z** - X/Ku-Band Analog Beamforming Board (Stingray)
- **Power adapters** for ADXUD1AEBZ and ADAR1000EVAL1Z (12V)
- **Interconnect cables** and adapters
- **Documentation** and quick start guides

**Required (Not Included):**

- **Xilinx ZCU102 Evaluation Board** - Required for FPGA processing
- **Host computer** for development and control
- **Additional RF test equipment** (signal generators, spectrum analyzers, etc.)

## Power Requirements

**ADAR1000EVAL1Z (Stingray)**

- **12V DC power adapter**
- On-board power regulation provides all required voltages

**ADXUD1AEBZ**

- **12V DC power adapter**
- On-board power regulation provides all required voltages


**AD9081-FMCA-EBZ**

- **Powered via FMC connector** from ZCU102 board
- No external power required
- ZCU102 must provide adequate power via FMC

## Configuration Overview

The X-Band platform requires several configuration steps before first use. Each topic has a dedicated guide:

### SD Card Setup

Prepare the SD card with ADI Kuiper Linux operating system.

**Steps Include:**
- Format SD card properly
- Flash Kuiper Linux image
- Copy boot files (BOOT.BIN, Image, system.dtb)
- Verify boot operation

**📖 See**: [SD Card Configuration Guide](sdcard/index.md)

### ZCU102 Hardware Configuration

Configure switches and jumpers on the ZCU102 board for proper operation.

**Key Settings:**
- Boot mode switches (SW6) for SD card boot
- USB host mode jumpers for peripherals
- UART connection for console access
- Network configuration for remote access

**📖 See**: [ZCU102 Configuration Guide](zcu102config/index.md)

### EEPROM Programming

Program the FMC EEPROM on the ADXUD1AEBZ interposer board.

**Required For:**
- Proper 1.8V VADJ power to AD9081
- FMC board identification
- System initialization

**📖 See**: [EEPROM Programming Guide](eeprom/index.md)

## Configuration Quick Reference

### Essential Settings Summary

| Component | Configuration | Guide |
|-----------|---------------|-------|
| **ZCU102 Boot Mode** | SW6: ON-OFF-OFF-OFF | [ZCU102 Config](zcu102config/index.md) |
| **USB Host Mode** | J7, J109-113 configured | [ZCU102 Config](zcu102config/index.md) |
| **SD Card** | Kuiper Linux + boot files | [SD Card Guide](sdcard/index.md) |
| **FMC EEPROM** | Programmed for VADJ | [EEPROM Guide](eeprom/index.md) |
| **UART Console** | 115200 baud, 8N1 | [ZCU102 Config](zcu102config/index.md) |

## Initial Power-On

**Power-On Sequence:**

1. **First**: Power on ADAR1000EVAL1Z (12V adapter)
2. **Second**: Power on ADXUD1AEBZ (12V adapter)
3. **Third**: Power on ZCU102 (which powers AD9081-FMCA-EBZ)
4. **Fourth**: Boot ZCU102 with reference design

**Verification Steps:**

1. Check that all power LEDs are illuminated
2. Verify ZCU102 boots properly with FPGA design loaded
3. Test basic communication with each board
4. Run initial system verification tests

```{seealso}
**Detailed Instructions:**
- [Hardware Assembly Guide](assembly/index.md) - Complete assembly and power connection details
```

## Safety Considerations

```{warning}
- Always power down all equipment before making connections
- Use proper ESD protection when handling boards
- Verify power supply voltages before connecting
- Do not exceed maximum RF input levels
```

```{caution}
- The X-Band platform operates at high frequencies
- Ensure proper RF shielding and safety practices
- Be aware of local regulations for X-Band emissions
```

```{toctree}
:maxdepth: 1

Hardware Assembly <assembly/index>
ZCU102 Configuration <zcu102config/index>
SD Card Setup <sdcard/index>
EEPROM Programming <eeprom/index>

```

```{note}
For additional setup support, please refer to the individual evaluation board quick start guides linked in the Resources section.
```
