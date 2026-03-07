ADALM1000 Firmware Upgrade Procedures
=====================================

The firmware on the device can be upgraded using the smu executable or directly from Pixelpulse.

Update using the smu executable
-------------------------------

The ``smu`` executable (part of the :doc:`libsmu </wiki-migration/university/tools/m1k/libsmu>` library) provides some basic functionalities . In the following image you can see these functionalities and their corresponding call arguments:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      C:\WINDOWS\system32> **smu**
      smu: utility for managing M1K devices
   
       -h, --help                   print this help message and exit
       --version                    show libsmu version
       -l, --list-devices           list supported devices currently attached to the system
       -p, --hotplug-devices        simple session device hotplug testing
       -s, --stream-samples         stream samples to stdout from a single attached device
       -d, --display-calibration    display calibration data from all attached devices
       -r, --reset-calibration      reset calibration data to the defaults on all attached devices
       -w, --write-calibration <cal file> write calibration data to a single attached device
       -f, --flash <firmware image> flash firmware image to a single attached device
   


As you can see in the above, the ``smu`` application provides an option for flashing a firmware to an ADALM1000 board (the ``-f`` or ``--flash`` option). Before running this command, you must first download the firmware image from :git-m1k-fw:`m1k-fw <releases>` project. We recommend to always use the latest firmware release in order to be able to access all supported features. You should download the m1000.bin file.

After downloading the firmware binary, run the following command in your OS specific preferred terminal:

::

   C:\WINDOWS\system32> **smu -f /path/to/m1000.bin**

After installing ''libsmu, the smu executable's path is automatically added in the system path. If you build libsmu manually, you can find the smu executable in the build folder, under /src/cli.

Automatic update from Pixelpulse
--------------------------------

Pixelpulse is capable of detecting whether the connected devices have the latest firmware and provides an easy way to upgrade the firmware. It automatically searches on the internet for the latest firmware, downloads it and checks if the connected devices need to be upgraded. The firmware status of the connected devices can be seen by opening the Pixelpulse Device Manager.

.. image:: https://wiki.analog.com/_media/university/tools/dev_manager.png
   :alt: Device Manager
   :width: 200px

.. tip::

   In case Pixelpulse does not have the *Device Manager* option please update Pixelpulse. This option is available starting from version 0.86.


The Device Manager displays a list of all connected devices and the firmware status of each device.



|Device Manager devices list|

In case the PC is not connected to the internet Pixelpulse cannot check the version of the latest firmware nor download it and will display an error message. In this case the firmware update is not possible on any device.


|Device Manager no internet connection error|

Each device that needs a firmware update has an **Update Firmware** button next to its name. A device can be in one of these 3 states:

-  the firmware is up to date
-  has an older firmware
-  is in programming mode

The devices that are in programming mode need to be programmed first. If multiple devices are in programming mode Pixelpulse will display just one of them in the devices list. Once this device is programmed and reconnected to the PC another device that is in programming mode will appear in the list.

After a firmware update the device status will change showing the firmware update status. The device will become functional only after it is reconnected to the PC.

|Old firmware update status| |Programming mode update status|

The list of connected devices is automatically updated when a device which is not in programming mode is disconnected/connected to the PC. To force a refresh of the devices list press the **Refresh Devices List** button.

| 
| ==== Troubleshooting ==== When installing Pixelpulse2, the drivers for ADALM1000 should be correctly installed. In order to be able to update the firmware using Pixelpulse2, you can check the installed drivers using Windows Device Manager. Ideally, ADALM1000 should appear under *Universal Serial Bus devices* as:

-  **ADALM1000 SAM-BA WinUSB** - if the board is in programming mode
-  **ADALM1000 WinUSB** - if the board is not in programming mode

If that is the case, the firmware upgrade should work properly.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pp-correct.png
   :align: center

| 
| Otherwise, the board will appear in the *Ports (COM &LPT)* section.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pp-com.png
   :align: center

In this case, you need to make sure you installed the latest Pixelpulse2 release and follow the next steps:

-  Right click on the driver entry in the list and choose *Update Driver Software*
-  Choose *Browse my computer for driver software*.
-  Choose *Let me pick from a list of device drivers on my computer*.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pp-choose2.png
   :align: center

-  Check the box labeled *Show compatible hardware*
-  Choose the **ADALM1000 WinUSB driver** or **ADALM1000 SAM-BA WinUSB**.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/pp-choose.png
   :align: center

After performing these steps, Pixelpulse2 should be able to detect your device and upgrade the firmware.

.. |Device Manager devices list| image:: https://wiki.analog.com/_media/university/tools/fw_multiple_devices.png
   :width: 600px
.. |Device Manager no internet connection error| image:: https://wiki.analog.com/_media/university/tools/fw_no_internet_error.png
   :width: 600px
.. |Old firmware update status| image:: https://wiki.analog.com/_media/university/tools/fw_old_update_ok.png
   :width: 300px
.. |Programming mode update status| image:: https://wiki.analog.com/_media/university/tools/fw_programming_mode_update_ok.png
   :width: 300px
