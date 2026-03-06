ZCU102 Setup for X-Band Developer Platform
==========================================

This guide will walk you through setting up the ZCU102 FPGA platform to work with the X-Band Developer's Kit.

--------------

SD Card Setup
-------------



.. raw:: html

   <details><summary>Click to expand</summary>

-  Follow the instructions on one of the below pages to install the |latest Linux kernel| on the SD card.

   -  :doc:`Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
   -  :doc:`Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

-  Determine which version of the MxFE board you have. The version is printed in copper on the bottom right corner of the board with the RF connectors facing North. The writing is covered in soldermask and can be somewhat difficult to read. The board version should either be "B", "C", or "D".
-  There are three pertinent files to copy to the root of the SD card's /BOOT/ section:

   -  Image
   -  BOOT.BIN
   -  system.dtb

.. note::

   Be sure to rename the correct \*.dtb file for your version of the AD9081 board to "system.dtb"


.. warning::

   \ **If your computer encrypts removable media for security purposes, it's easiest to use a personal computer to do this step.**\


| 
| `ZCU102 Configuration Files, 100MHz VCXO <https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_configuration_files_100mhz_vcxo.zip>`__

`ZCU102 Configuration Files, 100MHz VCXO, AD9081 Direct Clock <https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_configuration_files_100mhz_vcxo_ad9081_direct_clk.zip>`__

.. raw:: html

   </details>


| 
| ===== ZCU102 Configuration =====

Boot from SD Card
~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click to expand</summary>

To configure the ZCU102 to boot from the SD card, set SW6 as shown below. SW6 is halfway between the SD card input and the vertical SMA connectors on the ZCU102.


|SW6 Configuration for SD Card Boot|

.. raw:: html

   </details>


| 
| ==== USB Host Mode ==== 

.. raw:: html

   <details><summary>Click to expand</summary>

Setting up the ZCU102 in USB Host Mode allows the use of USB peripherals such as a keyboard and mouse. This can be useful for operating the board directly rather than having to use the UART connection or some other form of indirect control. Configure the jumpers as indicated below:

-  Shunt J7
-  J109 -> Shunt pins 2-3
-  J110 -> Shunt pins 2-3
-  J112 -> Shunt pins 1-2
-  J113 -> Shunt pins 1-2

|Jumper Configuration for USB Host Mode|

.. raw:: html

   </details>


| 
| ==== DisplayPort Not Working ==== Once you have the board up and running (and control using the UART connection through PuTTy), :doc:`try this procedure at the bottom of the page </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`.

| 
| ==== USB to UART Bridge ==== The ZCU102 uses a mini-B USB cable to connect the USB UART port on the board to a host PC. If the USB to UART bridge is not installed or automatically recognized, then a drive must be installed. This will allow control using the UART connection through PuTTy or other SSH/Telnet Client, `select Downloads tab for Driver download <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers>`__.

| 
| ==== Network Configuration ==== The ZCU102 uses a RJ45 ethernet cable to connect the ethernet port on the board a host PC or network port to enable network access. Modifications to the network settings can be made following the guidance detailed on the :doc:`Network Configuration </wiki-migration/resources/tools-software/linux-software/network-config>` wiki.

.. |latest Linux kernel| image:: http://swdownloads.analog.com/cse/2019_R1-2020_06_22.img.xz
.. |SW6 Configuration for SD Card Boot| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_sw6_sdcard.jpg
.. |Jumper Configuration for USB Host Mode| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-dev-kit/zcu102_usb_host_mode.jpg
