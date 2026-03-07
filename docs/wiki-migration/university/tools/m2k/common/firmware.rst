ADALM2000 (M2K) Firmware Updates
================================

The easiest way to update the firmware is to use the mass storage device included in the default image. There are times when this might not be possible (when you aren't using the default image).

.. important::

   There are very legitimate `Security Risks <https://en.wikipedia.org/wiki/Firmware#BADUSB>`_ about loading random firmware images onto devices like the ADALM2000, however, we decided early on that a learning tool must be open and accessible for people to experiment on. Please only use firmware images you have received from trusted locations.


.. admonition:: Download
   :class: download

   ADI default firmware images:

   
   -  :git-m2k-fw:`Latest ADALM2000 (M2k) Release <releases/latest>`
   
   This zip file should include these files:
   
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   | Filename          | Purpose                                                                                                                 |
   +===================+=========================================================================================================================+
   | ``boot.dfu``      | DFU file for First Stage Boot Loader, and U-Boot                                                                        |
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   | ``boot.frm``      | Firmware file for First Stage Boot Loader, U-Boot and its default environment                                           |
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   | ``m2k.dfu``       | DFU file for M2k Firmware, this would include FPGA Bit File, Linux kernel (all drivers), and ram based file system      |
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   | ``m2k.frm``       | Firmware file for M2k Firmware, this would include FPGA Bit File, Linux kernel (all drivers), and ram based file system |
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   | ``uboot-env.dfu`` | DFU file which includes the default U-Boot environment                                                                  |
   +-------------------+-------------------------------------------------------------------------------------------------------------------------+
   


Mass Storage Update
-------------------

Copy the ``m2k.frm`` file onto the mass storage device, and then eject it. LED1 will start blinking rapidly.

.. warning::

   Don't disconnect the device until rapid blinking stops!


Windows/OSX
~~~~~~~~~~~

-  Open the M2K mass storage device
-  Download and open the firmware file
-  Copy the file to the Mass Storage device
-  Eject **(don't unplug)** the M2K mass storage device via the context menu of the associated drive available in the file explorer.

   -  Windows (only eject as shown below!)


   |image1|

-  This will cause ``LED1`` to blink rapidly. This means programming is taking place. Do not remove power (or USB) while the device is blinking rapidly. It does take approximately 4 minutes to properly program the device.
-  Still do not unplug things. Try to be more patient.
-  Once the device is done programming, it will re-appear as a mass storage device.
-  Now you can unplug it, and use it as normal.

Linux
~~~~~

GUI
^^^

Command Line
^^^^^^^^^^^^

It's exactly the same as the GUI instructions, copy it, and then eject it, then power cycle it. It's a little more tricky since ``eject`` needs the base device (it wants ``/dev/sdb`` not ``/dev/sdb1``).

.. container:: box

   
   ::
   
      analog@imhotep:~/m2k$ **cp ./m2k.frm /media/analog/ADALM2000/**
      analog@imhotep:~/m2k$ **mount | grep ADALM2000 | awk '{print $1}'**
      /dev/sdb1 
      analog@imhotep:~/m2k$ **sudo eject /dev/sdb**
   


DFU Update
----------

`USB Device Firmware Upgrade <https://en.wikipedia.org/wiki/USB#Device_Firmware_Upgrade>`_ (DFU) is an official USB device class specification of the USB Implementers Forum. It specifies a vendor and device independent way of updating the firmware of a USB device. The concept is to have only one vendor-independent update tool as part of the operating system, which can then (given a particular firmware image) be downloaded into the device. During the firmware upgrade operation (when the M2K is in "DFU" mode), the M2K change its operating mode ( no longer uses its standard PID/VID, but becomes a flash programmer).

Entering DFU mode
~~~~~~~~~~~~~~~~~

How to manually enter DFU mode?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In general the preferred firmware upgrade is via the mass storage device. There are 3 ways to enter the DFU mode manually:

-  **Press and hold the** `device button <https://wiki.analog.com/../../pluto/hacking/hardware>`_ with a toothpick, paper-clip or similar while applying power by plugging in the USB cable.
-  From the device linux console type **``device_reboot sf``**. There are three ways to access the linux console:

   -  The USB console USB CDC ACM aka. ttyACM0 using putty, minicom, tera Term, etc.
   -  The UART console using :doc:`ADALM-JTAGUART </wiki-migration/university/tools/uartjtag>`.
   -  The network console using ssh/slogin.

-  Directly from u-boot serial console type: **run dfu_sf**. Access to the uboot command console is only available using :doc:`ADALM-JTAGUART </wiki-migration/university/tools/uartjtag>`

When does the device automatically enter DFU mode?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The device enters DFU mode in case booting the multi component FIT image (Flattened Image Tree) fails. This may happen due to checksum failure caused by a corrupted previous firmware update.

How can I check if the device is in DFU mode?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the device is in DFU mode, the **DONE LED** is **OFF**, while **LED1** is constantly **ON**.

Update using DFU mode
~~~~~~~~~~~~~~~~~~~~~

How to update the firmware using DFU mode? How to rewrite the default uboot environment?

Windows
^^^^^^^

The M2K driver package bundles also a dfu utility. There is a windows command console batch script called `UPDATE.BAT <https://raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/UPDATE.BAT>`_ which eases the update procedure.

-  Download and save `UPDATE.BAT <https://raw.githubusercontent.com/analogdevicesinc/plutosdr_scripts/master/UPDATE.BAT>`_
-  Download and unzip the latest M2k release :git-m2k-fw:`M2k Release <releases>`
-  Open a windows command prompt
-  Execute UPDATE.BAT with the path to the m2k.dfu file. (In case you need to rewrite the default uboot environment the use the uboot-env.dfu file)
-  Wait for the script to complete

::

   Microsoft Windows [Version 6.1.7601]
   Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

   C:\tmp>UPDATE.BAT c:\tmp\m2k.dfu
   dfu-util 0.9

   Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
   Copyright 2010-2016 Tormod Volden and Stefan Schmidt
   This program is Free Software and has ABSOLUTELY NO WARRANTY
   Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

   Opening DFU capable USB device...
   ID 0456:b674
   Run-time device DFU version 0110
   Claiming USB DFU Interface...
   Setting Alternate Setting #1 ...
   Determining device status: state = dfuIDLE, status = 0
   dfuIDLE, continuing
   DFU mode device DFU version 0110
   Device returned transfer size 4096
   Copying data from PC to DFU device
   Download        [=========================] 100%      8694467 bytes
   Download done.
   state(7) = dfuMANIFEST, status(0) = No error condition is present
   state(2) = dfuIDLE, status(0) = No error condition is present
   Done!

   C:\tmp>

.. _linux-1:

Linux
^^^^^

::

   dfu-util -a firmware.dfu -D m2k.dfu

``m2k.dfu`` is your firmware file in the dfu format.

OSX
^^^

``dfu-util`` does not come with a default OSX install. You can install it with brew as:

::

   brew install dfu-util

Updating the firmware is the same as Linux:

::

   dfu-util -a firmware.dfu -D m2k.dfu

``m2k.dfu`` is your firmware file in the dfu format.

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/common/windows-eject.png
   :width: 600px
