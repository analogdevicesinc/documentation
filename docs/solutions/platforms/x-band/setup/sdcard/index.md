(x-band-sdcard)=
# SD Card Configuration

This guide covers the complete process for preparing, formatting, flashing, and configuring an SD card for the X-Band Phased Array Development Platform.

## Prerequisites

Before starting, ensure you have:

- **SD Card**: Minimum 16GB recommended (32GB preferred)
- **SD Card Formatter**: [Download from SD Association](https://www.sdcard.org/downloads/formatter/)
- **BalenaEtcher**: [Download from balena.io](https://www.balena.io/etcher/)
- **ADI Kuiper Linux Image**
- **SD Card Reader**: USB or built-in card reader
- **Host Computer**: Windows, Mac, or Linux

```{important}
**This version of Kuiper Linux is not yet released publicly.**  
Reach out to an ADI FAE for a copy
```

## Step 1: Format the SD Card

Before programming the SD Card, it must be properly formatted and erased.

1. **Insert the SD Card** into your card reader
2. **Open SD Card Formatter** software
3. **Select your SD Card** from the drive dropdown
   - Verify you've selected the correct drive
4. **Choose Quick Format** option
5. **Label the SD Card** (optional, e.g., `XBand_2024`)
6. **Click Format** and confirm
7. **Wait for completion** - you should see a success prompt
8. **Close SD Card Formatter**



```{warning}
Double-check that you've selected the correct drive. Formatting will erase all data on the selected drive.
```

```{note}
Use the SD Card Formatter program rather than Windows/Mac built-in formatting tools to ensure proper SD card structure.
```

## Step 2: Flash the Kuiper Linux Image

1. **Open BalenaEtcher** application
2. **Click "Flash from file"**
3. **Select the Kuiper Linux image**:
   - Navigate to your downloaded `.img` file
   - Example: `2024-06-18-ADI-Kuiper-full.img`
4. **Click "Select target"**
5. **Select your SD Card**:
   - **CRITICAL**: Double-check you've selected the correct drive
   - Selecting the wrong drive will erase its contents
6. **Click "Flash!"**
   - This may require administrator privileges
   - The flashing process takes approximately 10-15 minutes
   - A verification process will follow the flashing

```{important}
**The verification will always fail at the end - this is expected and can be ignored.** Simply close BalenaEtcher when the flashing completes.
```

### Flashing Progress

During the flashing process, BalenaEtcher will show:
- **Flashing**: Writing the image to the SD card (~10 minutes)
- **Validating**: Verifying the written data (~5 minutes)
- **Fail message**: Expected - ignore and close the application

## Step 3: Prevent SD Card Encryption (For automatic PC encryptions)

```{important}
**ADI Internal Users Only**: Within ADI networks, if files are moved directly in Windows Explorer, the SD Card will get encrypted and fail to boot. Follow these steps to work around this issue.
```

### Map Network Drive to Avoid Encryption

After flashing is complete, you must move specific files to the SD Card. To avoid encryption:

1. **Remove and re-insert the SD Card** into your PC
   - Windows will mount it as two drives: **BOOT** and **rootfs**
2. **Open Windows Explorer** (but don't navigate to the SD Card yet)
3. **Right-click the BOOT drive** and select **Properties**
4. **Go to the Sharing tab**
5. **Copy the network drive path** (e.g., `\\COMPUTERNAME\BOOT`)
6. **Right-click "This PC"** and select **Map Network Drive**
7. **Paste the network path** you copied
8. **Click Finish**
9. **Use this mapped network drive** for all file operations
   - Files copied through the network drive will not be encrypted

```{tip}
**External Users**: You can skip the network drive mapping and copy files directly to the BOOT partition.
```

## Step 4: Copy Required Files

The SD card needs specific boot files copied to the root directory of the **BOOT** partition.

### File Locations

You need to copy three files from your HDL build or reference design:

1. **Image**: Linux kernel image
   - Source: `zynqmp-common/Image`
2. **BOOT.BIN**: First-stage bootloader and FPGA bitstream
   - Source: `zynqmp-zcu102-rev10-stingray/BOOT.BIN`
3. **system.dtb**: Device tree blob
   - Source: `zynqmp-zcu102-rev10-stingray/<clock_config>/system.dtb`

```{note}
The `system.dtb` file location depends on your clocking configuration. Common options:
- `vcxo100/system.dtb` - 100 MHz VCXO reference
- `xo122p88/system.dtb` - 122.88 MHz XO reference
Select the system.dtb that matches your hardware clocking setup.
```

### Copy Procedure

1. **Navigate to the BOOT drive** (or mapped network drive for ADI users)
2. **Copy Image file**:
   - From: `<build_directory>/zynqmp-common/Image`
   - To: Root of BOOT drive
3. **Copy BOOT.BIN**:
   - From: `<build_directory>/zynqmp-zcu102-rev10-stingray/BOOT.BIN`
   - To: Root of BOOT drive
   - Overwrite if it already exists
4. **Copy system.dtb**:
   - From: `<build_directory>/zynqmp-zcu102-rev10-stingray/<clock_config>/system.dtb`
   - To: Root of BOOT drive
   - Overwrite if it already exists

```{warning}
Ensure you copy the correct `system.dtb` for your clocking configuration. Using the wrong device tree will cause boot failures or hardware misconfiguration.
```

### File Verification

After copying, the root of your BOOT partition should contain:
```
BOOT/
├── Image
├── BOOT.BIN
└── system.dtb
```

## Step 5: Safely Remove SD Card

1. **Close Windows Explorer** and any programs accessing the SD card
2. **Unmount/Eject the SD Card**:
   - Right-click the drive and select "Eject"
   - Or use the "Safely Remove Hardware" icon in the system tray
3. **Wait for confirmation** that it's safe to remove
4. **Remove the SD Card** from your card reader

## Step 6: Install and Boot

### Installation

1. **Power down the X-Band platform** completely
2. **Remove any existing SD Card** from the ZCU102
3. **Insert the newly programmed SD Card** into the ZCU102 SD card slot
4. **Ensure ZCU102 is configured for SD boot** (see {ref}`ZCU102 Configuration <x-band-zcu102config>`)

### First Boot

1. **Open a serial terminal** on your host PC:
   - Baud rate: **115200**
   - Data bits: 8
   - Parity: None
   - Stop bits: 1
   - Flow control: None
2. **Connect USB-UART cable** from PC to ZCU102 (J83)
3. **Power on the X-Band platform** (see power-on sequence in main Setup guide)
4. **Monitor boot process** in the serial terminal:
   - U-Boot messages appear (~5 seconds)
   - Linux kernel boot messages (~15 seconds)
   - System initialization (~20 seconds)
   - Login prompt appears (~30-40 seconds total)

### Verify Boot Success

1. **Login** with credentials:
   - Username: `root`
   - Password: `analog`
2. **Wait 60 seconds** for system initialization to complete
3. **Check IIO devices**:
   ```bash
   root@analog:~# iio_attr -d
   ```
   - You should see **40 IIO devices** listed

   ```{image} xbdp_iio_device_verification.png
   :alt: IIO Device Verification
   ```

4. **Verify Kuiper version**:
   ```bash
   root@analog:~# cat /boot/VERSION.txt
   ```
   - Confirm it matches your downloaded image version

   ```{image} xbdp_sd_card_image_verification.png
   :alt: SD Card Image Verification
   ```

5. **Verify Stingray LED status**:
   - Inspect the Stingray board and confirm the following LEDs are illuminated:
     - **Red LED**: Power good
     - **Yellow LED**: System activity
     - **Green LED**: Boot complete
   - All three LEDs lit simultaneously confirm a successful boot

   ```{image} IMG_0337.jpeg
   :alt: Stingray LED Status
   :width: 50%
   ```

```{tip}
Boot is confirmed successful when **40 IIO devices** appear in the terminal **and** the red, yellow, and green LEDs are all illuminated on the Stingray board. Your SD Card is properly configured and ready for use with MATLAB/Python scripts.
```

## Additional Resources

- [SD Association - SD Card Formatter](https://www.sdcard.org/downloads/formatter/)
- [BalenaEtcher Download](https://www.balena.io/etcher/)
- {ref}`ADI Kuiper Linux Images <kuiper>`
- [ZCU102 Documentation](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)

```{seealso}
- {ref}`ZCU102 Configuration <x-band-zcu102config>` - Configure boot mode and peripherals
- {ref}`EEPROM Programming <x-band-eeprom>` - Program FMC EEPROM for proper VADJ
- {ref}`Assembly Guide <x-band-assembly>` - Complete hardware assembly instructions
```
