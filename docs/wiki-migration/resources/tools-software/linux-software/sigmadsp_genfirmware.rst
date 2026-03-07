SigmaDSP Firmware Utility for Linux
===================================

The SigmaDSP Firmware Utility for Linux allows to generate a firmware file which can be loaded by the Linux SigmaDSP device drivers.

Export XML firmware file from SigmaStudio
-----------------------------------------

1) Open your design in SigmaStudio and click the "Link Compile Connect" button for your Project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/sigmastudio_export1.png
   :width: 500px

2) Click the "Export System Files" button and select a location and a name for the exported system files.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/sigmastudio_export2.png
   :width: 500px

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/sigmastudio_export3.png
   :width: 500px

3) Open up the location where you stored the exported system files and look for a file with the .xml extension.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/sigmastudio_export4.png
   :width: 500px

Generate the binary firmware file
---------------------------------

Currently the SigmaDSP Firmware Utility for Linux only runs on a Linux system and can be downloaded from `here <https://raw.githubusercontent.com/analogdevicesinc/sigmadsp-genfirmware/master/sigmadsp_fwgen>`_.

::

   > wget %%https://raw.githubusercontent.com/analogdevicesinc/sigmadsp-genfirmware/master/sigmadsp_fwgen%%
   > chmod +x sigmadsp_fwgen

The next step is to copy the XML file from the previous instructions to a Linux machine.

The fwgen utility expects at least 3 parameters. The first parameter is the filename of the XML file exported from SigmaStudio, the second parameter is the samplerate that the XML file was generated for and the third parameter is the output file name.

::

   > ./sigmadsp_fwgen design.xml 48000 adau1761.bin

If you want to support multiple samplerates with your firmware file you need to export a XML file for each samplerate. Each file needs to be specified on the command line followed by the samplerate it was generated for. The last parameter is the name of the output file.

E.g.

::

   > ./sigmadsp_fwgen design_48000.xml 48000 design_32000.xml 32000 design_16000.xml 16000 ... adau1761.bin

When such a firmware file with support for multiple samplerates is loaded the kernel driver will automatically take care of programming the correct design for the currently selected samplerate to the SigmaDSP.

Load the firmware on the target system
--------------------------------------

In order to load firmware files the kernel needs to have firmware support (``CONFIG_FW_LOADER``) enabled.

::

   Device Drivers  --->
       Generic Driver Options  --->
         ...
         <*> Userspace firmware loading support
         ...

The firmware can either be built into the kernel or can be installed on the root file systen. If both the firmware is built into the kernel and present on the root file system the firmware built into the kernel will always take precedence.

Built into the kernel
~~~~~~~~~~~~~~~~~~~~~

To built the firmware into the kernel copy the firmware file to the kernel's **"firmware"** folder. In your kernel config enable ``CONFIG_FIRMWARE_IN_KERNEL`` and set ``CONFIG_EXTRA_FIRMWARE`` to the name of the firmware file.

::

   Device Drivers  --->
       Generic Driver Options  --->
         ...
         <*> Userspace firmware loading support
         [*]   Include in-kernel firmware blobs in kernel binary
         ("adau1761.bin") External firmware blobs to build into the kernel binary
         ...

Example .config:

::

   CONFIG_FIRMWARE_IN_KERNEL=y
   CONFIG_EXTRA_FIRMWARE="adau1761.bin"

Now rebuild the kernel image.

Installed on the root filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to install the firmware file on the root filesystem. This allows to update it without having to update the whole kernel. To install it on the root file system copy it to the **"/lib/firmware/"** folder on the target system.

.. important::

   If the firmware is installed on the root filesystem the driver needs to be built as a module, otherwise it will try to load the firmware before the root filesystem has been mounted.


More information
----------------

-  :doc:`SigmaStudio </wiki-migration/resources/tools-software/sigmastudio>`

.. include:: ../linux-drivers/need_help.rst
