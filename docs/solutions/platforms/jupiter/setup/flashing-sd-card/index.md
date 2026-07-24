# SD Card Flashing

The AD-JUPITER-EBZ ships with an SD card, but this SD card MUST be updated with the latest Kuiper image. This image can be found {git-kuiper}`here <main:+actions/workflows/kuiper2_0-build.yml?query=branch:main>`. There are several ways to burn an image onto the SD Card, but the following way is recommended.


Before the SD Card gets programmed it must be formatted and erased. This can be done with the SD Card Formatter application (https://www.sdcardformatter.com/).

## Using SD Card Formatter
1. Insert the SD Card and select it, choose Quick Format option and label the SD Card, e.g. jupiterTest
2. Press the Format button and wait for the prompt to say it is successful
3. The SD Formatter software can be closed

## SD Card Flash
Now BalenaEtcher is needed to flash the SD Card with an image. BalenaEtcher is a free, open-source utility for flashing operating system images (.iso, .img, .zip) onto SD cards and USB drives to create bootable media.

Ensure you have the image downloaded and unzipped so you have a *.img file to program.
1. Select the *.img file to program to the SD Card
2. Select the SD Card to program (double check that this is the correct drive)
3. Press the Flash button, this may require admin privileges on your laptop. It takes about 10 mins


```{image} balena-etcher-error.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

## Setup SD Card
You need to move files to the root directory of the SD Card based on the FPGA platform in your system. *Within ADI, if this is done directly in Windows Explorer, the SD Card will get encrypted and it will fail to boot when
you use it in the Jupiter platform, this is a work around for this issue.*

1. Following programming, remove the SD Card and re-insert it into the PC/Laptop
2. Open Windows Explorer, do not select the SD Card Drive, this may encrypt the SD Card prompting a restart
3. Right click the BOOT drive and select properties and go to the Sharing Tab, copy the network drive
<!-- 4. Share the network path -->
4. Check if the network path is shared: Right click the BOOT drive and select properties and go to the Sharing Tab

```{image} checking-network-path.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

5. If the network path says not shared, go to Advanced Sharing



6. Click Share this folder

```{image} share-this-folder.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

7. Next, click permissions and make sure that Full Control is selected under Permissions for Everyone

```{image} full-access-permissions.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

8. Click apply and ok in the Permissions and Properties tabs, respectively
9. Create a Map Network Drive to this, right click “This PC” and select Map Network Drive and enter the path copied
10. A new drive will be created and when you use this drive, there is no encryption. This drive will pop up automatically

## File Manipulation
Now that the new drive is up, all of the files needed are accessible without encrypting the device. For Jupiter, four files need to be moved to the root directory: Image.img, BOOT.BIN, system.dtb, and boot.scr.

1. Scroll down until the zynqmp-common folder, open it
    - This folder has the Image.img folder in it

```{image} jupiter-common-folder.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

2. Copy the Image file, go up one level (to the root directory) and paste the file

```{image} inside-common-folder.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

3. Scroll down to the zynqmp-jupiter-sdr folder

```{image} jupiter-sdr-folder.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

4. Copy the BOOT.BIN file, boot.scr file, and system.dtb file

```{image} inside-sdr-folder.png
:alt: Put Text Here to Describe the Image
:width: 600px
:align: center
```

5. Go up one level (to the root directory) and paste the files
6. Everything is ready to go, close the file explorer and safely eject the SD Card

## Testing the SD Card
- With a successfully programmed SD Card, power the Jupiter System down and remove the existing SD Card (if there is one) from the setup
- Insert the newly flashed SD Card
- Use a UART connection and connect to the Jupiter with a baud rate of 115200 (PuTTy is used here, but any one would work)
- Power the Jupiter platform, if everything is successful the terminal will show the Jupiter booting up


```{note}
For questions or help with the Jupiter SDR, please visit:

{ez}`fpga`
```