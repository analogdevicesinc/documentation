System Update
=============

This page covers the methods of updating the flash.

Firmware Update
---------------

Firmware can be updated via the bin file.

In general, the data_collect executable is used to update the firmware. This can be done from the host or on the device.

The firmware binary file for the latest version is available on the respective flash image. The binary file can also be obtained from the ADSD3500 installer. From the installer package, under the directory ADSD3500_Release_Firmware, the binary file required, in this case, for the 4.1.5 firmware release:

-  Fw_Update_4.1.5.bin

From the host:

::

   cd "C:\Analog Devices\ADTF3175D\TOF_Evaluation_ADTF3175D-Rel4.1.1\bin"
   data_collect --fw ..\image\NXP-Img-Rel4.1.1-ADTF3175D-0A8ED2B5\Fw_Update_4.1.5.bin --ip 10.42.0.1 tof-viewer_config.json

In either case wait for 60s before restarting the system.
