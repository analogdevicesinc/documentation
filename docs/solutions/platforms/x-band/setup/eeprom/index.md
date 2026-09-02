(x-band-eeprom)=
# EEPROM Programming

This guide covers programming the FMC EEPROM on the ADXUD1AEBZ interposer board, which is required for proper system operation.

## Overview

The ADXUD1AEBZ interposer board contains an FMC (FPGA Mezzanine Card) EEPROM that stores critical configuration information. **This EEPROM is not factory programmed** and must be programmed before the system can operate correctly.

### Why EEPROM Programming is Required

The FMC EEPROM contains:
- **Board identification** information
- **VADJ voltage requirements** (1.8V for AD9081)
- **Power-on sequence** parameters
- **FMC connector configuration**

```{important}
**Without proper EEPROM programming, the ZCU102 will not provide 1.8V VADJ power to the AD9081-FMCA-EBZ board**, preventing it from powering on correctly.
```

## Prerequisites

Before programming the EEPROM, ensure:

1. **System is assembled** with all boards connected:
   - ZCU102 powered and booted
   - AD9081-FMCA-EBZ connected via FMC
   - ADXUD1AEBZ interposer installed
2. **Network or UART connection** to ZCU102
3. **Root access** to the Linux system
4. **FRU tools** installed (included in Kuiper Linux)

## EEPROM Programming Procedure

### Step 1: Access the System

Connect to your ZCU102 via:

**Option A: UART Console**
- Baud rate: 115200, 8N1
- Connect USB cable to J83 on ZCU102

**Option B: SSH**
```bash
ssh root@<zcu102_ip_address>
```

Default credentials:
- Username: `root`
- Password: `analog`

### Step 2: Locate EEPROM Devices

First, verify the EEPROM device is detected:

```bash
root@analog:~# find /sys -name eeprom
```

Expected output should include:
```
/sys/bus/i2c/devices/15-0050/eeprom
/sys/bus/i2c/devices/15-0051/eeprom
```

```{note}
The exact I2C bus number (e.g., `15-0050`) may vary depending on your system configuration. Use the address that corresponds to the ADXUD1AEBZ FMC connector.
```

### Step 3: Program the FMC EEPROM

Program the EEPROM with the FMC FRU (Field Replaceable Unit) data:

```bash
root@analog:~# fru-dump -i /usr/local/src/fru_tools/masterfiles/AD-FMCOMMS2-EBZ-FRU.bin -o /sys/bus/i2c/devices/15-0050/eeprom
```

```{note}
**Why AD-FMCOMMS2-EBZ FRU?** While the ADXUD1AEBZ interposer is a different board, we use the AD-FMCOMMS2-EBZ FRU binary because it encodes the critical **1.8V VADJ voltage requirement** needed by the AD9081-FMCA-EBZ. The board product name will show as "AD-FMCOMMS2-EBZ" in the readback output—this is intentional and correct.
```

Command breakdown:
- `fru-dump`: FRU programming utility
- `-i`: Input FRU binary file
- `-o`: Output target (EEPROM device)

Expected output:
```
Writing FRU data to /sys/bus/i2c/devices/15-0050/eeprom...
Success: 256 bytes written
```

```{warning}
**Verify the I2C device path** (e.g., `15-0050`) matches your system. Using the wrong path may program the incorrect EEPROM or fail entirely.
```

### Step 4: Verify EEPROM Programming

Read back the programmed EEPROM to verify:

```bash
root@analog:~# fru-dump -i /sys/bus/i2c/devices/15-0050/eeprom -b
```

Expected output should display:
```
Board Manufacturer: Analog Devices
Board Product Name: AD-FMCOMMS2-EBZ
Board Serial Number: <serial>
Board Part Number: <part_number>
FRU File ID: AD-FMCOMMS2-EBZ
```

```{tip}
If the readback shows valid FRU data matching the expected board information, programming was successful.
```

### Step 5: Power Cycle the System

After programming, a complete power cycle is required:

```bash
root@analog:~# poweroff
```

**After shutdown:**
1. **Disconnect all power** from the system
2. **Wait 10 seconds** for complete discharge
3. **Reconnect power** and boot the system
4. **Verify 1.8V VADJ** is present (see verification section below)

```{important}
A reboot is **not sufficient** - you must perform a complete power cycle (power off, wait, power on) for the VADJ changes to take effect.
```

## Verification

### Check VADJ Power Rail

After power cycling, verify 1.8V VADJ is present:

**Option A: Measure with Multimeter**
- Locate VADJ test point on AD9081-FMCA-EBZ
- Measure voltage: should read **1.8V ± 0.1V**

**Option B: Check IIO Devices**
```bash
root@analog:~# iio_attr -d
```

If VADJ is correct, you should see the AD9081 device (typically `axi-ad9081-rx-hpc`).

**Option C: Check System Logs**
```bash
root@analog:~# dmesg | grep -i vadj
```

Look for messages indicating 1.8V VADJ configuration.

### Verify FMC Detection

Check that the FMC board is properly detected:

```bash
root@analog:~# cat /sys/bus/i2c/devices/15-0050/eeprom | hexdump -C | head -20
```

The output should show valid FRU data (not all 0x00 or 0xFF).

## Additional Resources

- [FMC Standard Specification](https://www.vita.com/fmc)
- {ref}`ADI FRU Tools Documentation <software fru-dump>`
