Pre-release SD Card Creation
============================

The project will be release as part of 2019_r1 release.Before then, the SD image for 2018_r2 can be used.

Writing the SD Card
-------------------

Details on how to write the SD card can be found at https://wiki.analog.com/resources/tools-software/linux-software/zynq_images.

ADRV9009-ZU11EG Specific Boot Files
-----------------------------------

After writing the image, on the boot partition root, the ADRV9009-ZU11EG specific files can be added from any folder matching \**zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb\* \*\* from boot partition. More information can be found in boot partition ReadMe.txt.

Video Configuration
-------------------

The default configuration for most of the projects is to use the HDMI output, but for this project the DisplayPort is used. In order for it to work, you should follow the steps described here: `DisplayPort - no picture? <https://wiki.analog.com/https/wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`__ After following the steps, the board should be rebooted.
