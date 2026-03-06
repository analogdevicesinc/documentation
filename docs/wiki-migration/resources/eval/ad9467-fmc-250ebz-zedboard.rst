EVALUATING THE AD9467-FMC-250EBZ ANALOG-TO-DIGITAL CONVERTER using ZedBoard
===========================================================================

Preface
-------

This user guide describes on how :adi:`AD9467` evaluation board :adi:`(AD9467-FMC-250EBZ) <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` works with the `ZedBoard/AES-Z7EV-7Z020-G <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ development platform. The :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` board can be configured using SPI interface with `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__. The `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ will boot the ADI Kuiper Linux Image that supports several ADI hardware. :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>` is now supporting IIO hardware, in which ACE released a generic IIO plugin that can be used to evaluate IIO devices that has no specific IIO plugins.

:adi:`AD9467` is a 16-bit, monolithic, IF sampling analog-to-digital converter (ADC) that operates at a 250 MSPS conversion rate. The :adi:`AD9467` data sheet provides additional information and should be consulted when using the board. For additional information or questions send an email to highspeed.converters@analog.com.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. AD9467-FMC-250EBZ (Right) + Zedboard (Left) Setup*\


Features
--------

-  Full feature evaluation board for the :adi:`AD9467 <en/products/ad9467.html>`.
-  SPI interface for setup and control.
-  Uses 12V, 3.3V, VADJ(2.5V) from the FMC connection.
-  Internal and external reference options.
-  ACE Generic IIO Plugin software interfaces.

Helpful Links
-------------

-  :adi:`AD9467 Data Sheet <media/en/technical-documentation/data-sheets/AD9467.pdf>`
-  :doc:`Analog Devices Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  Boards:

   -  :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>`
   -  `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

-  Application Note:

   -  :doc:`ADI Serial Control Interface Standard </wiki-migration/resources/technical-guides/adispi>`
   -  :adi:`AN-835: Understanding ADC Testing and Evaluation <en/resources/app-notes/an-835.html>`

-  Other User Guide:

   -  :doc:`EVALUATING THE AD9467-FMC-250EBZ ANALOG-TO-DIGITAL CONVERTER </wiki-migration/resources/eval/ad9467-fmc-250ebz>`
   -  :doc:`AD9467 Native FMC Card / Xilinx Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad9467>`

Software Needed
---------------

-  `ADI Kuiper Linux Image 2022_r2 <https://swdownloads.analog.com/cse/kuiper/image_2023-12-13-ADI-Kuiper-full.zip>`__
-  `SD Card Formatter <https://www.sdcardformatter.com/>`__
-  `WinMD5 <http://www.winmd5.com/>`__ (Image Verifier)
-  `Win32DiskImager <https://sourceforge.net/projects/win32diskimager/files/latest/download?source=navbar>`__ (Image Flasher)
-  `PuTTY <https://apps.microsoft.com/store/detail/XPFNZKSKLBP7RJ?ocid=pdpshare>`__ (Terminal Emulator)
-  :adi:`Analysis \| Control \| Evaluation (ACE) Software <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

Design and Integration Files
----------------------------

-  `Schematics (Rev C) <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/9467fmc01c_sch.pdf>`__
-  `Bill of Materials (Rev C) <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/9467fmc01c_bom.xls>`__
-  `Gerber/Layout Fabrication Files <https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/9467fmc01c.zip>`__

Equipment Needed
----------------

-  :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>`
-  `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
-  Analog signal source and antialiasing filter
-  Sample clock source
-  2 SMA cable
-  PC running Windows® (Windows 10 or higher)
-  12V/5A power supply with US, European AC adapter.
-  SD Card (16GB or larger)
-  2 USB-A to Micro-USB-B cable
-  (Optional) Gigabit Ethernet cable

Getting Started
---------------

This section provides quick start procedures for evaluating the :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` board with `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ using **ACE Generic IIO Plugin**.

Preparing SD Card
~~~~~~~~~~~~~~~~~

Ensure that the :doc:`ADI Kuiper Linux Image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` is properly flashed on the SD card to properly evaluate the :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` board with `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__. Complete instructions on how to properly download, write, and read the ADI Kuiper Linux Image to SD card, and copy the specific files to the root of SD Card. Analog Devices Kuiper Linux Image is an embedded Linux system based on Raspberry Pi OS which incorporates thousands of Linux device drivers for ADI products which minimize the barriers in integrating ADI hardware devices in Linux environment. You can also check all the :doc:`supported projects </wiki-migration/resources/tools-software/linux-software/kuiper-linux/project-list>` of ADI Kuiper Linux Image that lists all ADI evaluation boards with its corresponding development platform.

-  Download

.. admonition:: Download
   :class: download

   \ `ADI Kuiper Linux Image 2022_r2 <https://swdownloads.analog.com/cse/kuiper/image_2023-12-13-ADI-Kuiper-full.zip>`__\


.

   -  MD5sum image_2023-12-13-ADI-Kuiper-full.zip: ``9dfd5d57573e14e06715a08b19a6a26a``
   -  MD5sum 2023-12-13-ADI-Kuiper-full.img: ``e3620b6d36ad0481b79eee6041769f38``

-  Download and install

.. admonition:: Download
   :class: download

   \ `WinMD5 <http://www.winmd5.com/>`__ (Image Verifier)


to ensure the version is correct and the image was not corrupted.

   -  Open **WinMD5 application** and browse the downloaded image file.
   -  Check the MD5 checksum value is matched from **Step 1**.

.. container:: centeralign

   \


   |image2|

   *Figure 2. Verifying ADI Kuiper Linux Image File using WinMD5*\


-  If SD Card format is unknown or needs to be reconfigured/reformatted. Download and install

.. admonition:: Download
   :class: download

   \ `SD Card Formatter <https://www.sdcardformatter.com/>`__\


if no formatter software installed on your computer.

   -  Open **SD Card Formatter**, select SD card you want to reformat and make sure that it is the **correct** one.
   -  Check the **card information** if it **matches** the SD card.
   -  Input **Volume label** of the SD Card, usually named as **BOOT**.
   -  Select **Quick Format** as Formatting Options, then click **Format**.
   -  Once **completed**, it will pop-up a notification providing the **details of the SD Card** formatted.

.. container:: centeralign

   \


   |image3|

   *Figure 3. Formatting the Selected SD Card*\


-  Download and install

.. admonition:: Download
   :class: download

   \ `Win32DiskImager <https://sourceforge.net/projects/win32diskimager/files/latest/download?source=navbar>`__ (Image Flasher)


, to write the ADI Kuiper Linux Image to SD Card.

   -  Open **Win32DiskImager** then browse the ADI Kuiper Linux Image using the **small folder button**.
   -  **Select** the correct **Device**, double check the **Driver Letter** of your volume label (SD Card).
   -  **Click Write** button to flash the ADI Kuiper Linux Image. The software will alert you to make sure you want to write the selected device.
   -  It will take several minutes to completely flash the image to the SD card. If completed, it will notify as **Write Successful** indicating that the SD card is now ready.

.. container:: centeralign

   \


   |image4|

   *Figure 4. Flashing Image to SD Card using Win32DiskImager*\


.. tip::

   \ *For additional details on how to format, and write SD Card with ADI Kuiper Linux Image, you can check the links below:*

   
   -  :doc:`Using Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
   -  :doc:`Using Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`
   


-  After flashing the image to SD Card, it contains several folders in the root directory of the SD Card (BOOT FAT32 Partition) that supports many different ADI hardware boards. See :doc:`Complete Project List </wiki-migration/resources/tools-software/linux-software/kuiper-linux/project-list>`, to check the directories of files needed for ADI Hardware :adi:`(EVAL-AD9467/AD9467-FMC-250EBZ) <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` and Development Platform `(ZedBoard/AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__. Copy the following files onto the root directory of SD Card (BOOT FAT32 Partition):

   -  ``target/zynq-zed-adv7511-ad9467-fmc-250ebz/BOOT.BIN``
   -  ``target/zynq-zed-adv7511-ad9467-fmc-250ebz/devicetree.dtb``
   -  ``target/zynq-common/uImage``\

.. container:: centeralign

   \


   |image5|

   *Figure 5. Copying BOOT.BIN, devicetree.dtb, and uImage to Root Directory of SD Card*\


-  Now, the SD card is **ready**. Always ensure to **safely remove before ejecting** the SD Card.

Hardware Setup
~~~~~~~~~~~~~~

This section will discuss on how to setup and configure the `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ with :adi:`AD9467-FMC-250EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9467.html#eb-overview>` board. This setup configuration will set the `ZedBoard (AES-Z7EV-7Z020-G) <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ to SD Card Boot Mode and will load the ADI Kuiper Linux Image flashed from SD Card onto the board.

.. container:: centeralign

   \ |image6| *Figure 6. ZedBoard Board Configurations*\


-  On the **ZedBoard**, set the Jumper Pins accordingly shown in Figure 6 and Table 1.

.. container:: leftalign

   \ *Table 1. ZedBoard Jumper Configuration for EVAL-AD9467/AD9467-FMC-250EBZ*\


.. container:: centeralign

   \ |image7|\


-  Insert the SD Card into ZedBoard SD Card Interface Connector **(J12)**.
-  Refer to Figure 1, plug-in AD9467-FMC-250EBZ to ZedBoard FMC Connector **(J1)**.
-  Connect the 12V/5A power supply to ZedBoard barrel jack **(J20)**.
-  On the **AD9467-FMC-250EBZ** board, provide a clean, low jitter **250MHz** clock source to connector **J201** and set the amplitude to **16dBm**. Use a shielded, RG-58, 50Ohm, coaxial cable to connect the signal generator output to the Clock Input (ADC Sample Clock) of AD9467-FMC-250EBZ board.
-  On the **AD9467-FMC-250EBZ** board, provide a clean, low jitter clock source to connector **J100**. Use a shielded, RG-58, 50Ohm, coaxial cable to connect the signal generator output to the Analog Input of AD9467-FMC-250EBZ board. For best results, use a narrow-band, pass filter with 50Ohm terminations and appropriate center frequency.
-  To access its terminal, connect USB-A to Micro-USB-B cable from PC to Zedboard USB-UART port **(J14)**.
-  On the **Zedboard**, turn on power switch **(SW8)** and the Green Power LED **(LD13)** should illuminate. After several seconds booting up, the blue Done LED **(LD12)** should illuminate.
-  Choose from either from the options below to access connected devices in ZedBoard:

   -  Connect another USB-A to Micro-USB-B cable from PC to USB-OTG port **(J13)**; **or**
   -  Connect Gigabit ethernet cable from PC to Zedboard Gigabit Ethernet port **(J11)** and **skip Step 10 to Step 12**

-  Open terminal emulator (e.g.

.. admonition:: Download
   :class: download

   \ `PuTTY <https://apps.microsoft.com/store/detail/XPFNZKSKLBP7RJ?ocid=pdpshare>`__\


/Tera Term). Set the following configuration below and click **Open**, see Figure 7:

   -  Serial line: ``<ZedBoard COM Port Number>``
   -  Speed (baud): ``115200``
   -  Data bits: ``8``
   -  Stop bits: ``1``
   -  Parity: ``None``
   -  Flow control: ``None``\

.. container:: centeralign

   \ |image8|\ *Figure 7. PuTTY Serial Connection Configuration*\


-  Enter the following commands into the terminal to **enable** USB-OTG port, see Figure 8:

   -  ``usb_otg.sh enable``
   -  ``usb_otg.sh status``
   -  ``Reboot``\

.. container:: centeralign

   \ |image9|\ *Figure 8. ZedBoard terminal - Configuring USB-OTG Port*\


-  Check device manager under **Port** section, the device must be detected as **ADI USB Serial Port** using USB-OTG connection.

.. container:: centeralign

   \ |image10|\ *Figure 9. Device Manager - ADI USB Serial Port*\


Software Setup
~~~~~~~~~~~~~~

-  Download and install

.. admonition:: Download
   :class: download

   \ :adi:`Analysis \| Control \| Evaluation (ACE) Software <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`\


if it is not already installed.
-  The ACE Generic IIO plug-in can be found through ACE's Plug-In Manager.
-  In the Plug-in Manager, search **ADGenericIIO** under **Available Packages**. Once found, select the **Board.ADGenericIIO** and click **Install Selected** button.
-  After the installation, you can now go back to **Home**. It is located near the upper left corner on the ACE's user interface (UI).
-  The hardware device attached to PC must be detected in ACE, see Figure 10.

.. container:: centeralign

   \ |image11|\ *Figure 10. ACE - Hardware Detected*\


-  Click the **hardware detected** to be redirected to system tab pane. In the **System**, **uncheck** *Operate without Hardware*, and click **Acquire**. See Figure 11.

.. container:: centeralign

   \ |image12|\ *Figure 11. ACE System - Acquiring Hardware Detected*\


-  Go back to **Home** again and click the **hardware detected**.
-  In Figure 12, notice in the tab-pane, **xadc** is connected (greed led). Click **Find devices**, select device **cf-ad9467-core-lpc**, click **Get IIO Info** and click **Go to Detected Chip**.

.. container:: centeralign

   \ |image13|\ *Figure 12. ACE - Generic IIO Board*\


-  Setup the following signal source:

   -  Set Clock Input: ``250MHz @16dBm`` in **J201**
   -  Set Analog Input: ``170MHz`` in **J100**

-  In Figure 13, set Sampling Frequency to **250000000**, and other configuration are in **default** settings/values.

.. container:: centeralign

   \ |image14|\ *Figure 13. ACE - Initial Configuration*\


-  Go to **Direct Register Access** and read **0x00** and to check if it reads the default register values, **0x18**. It is to verify the SPI communication with AD9467-FMC-250EBZ board.
-  Click **Proceed to Analysis** and set the Sample Freq to **250MHz**.
-  Click **FFT** and click **Run Once** to perform single capture. Make sure to adjust the analog input signal level until the fundamental power reaches **-1dBFS**. See Figure 14 to check the sample FFT capture in the analysis.

.. container:: centeralign

   \ |image15|\ *Figure 14. ACE - AD9467-FMC-250EBZ Sample FFT Capture*\


-  To save the capture results, click on **Export** button at **Results** tab and save it to a location of choice.

//End of Document.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad9467_evaluation_board_connection.png
   :width: 900px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9467_verifying_adi_kuiper_linux_image_file_using_winmd5.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad9467_formatting_the_selected_sd_card..png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ad9467_flashing_image_to_sd_card_using_win32diskimager.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad9467_copying_boot_devicetree_and_uimage_to_root_directory_of_sd_card.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zed_sw.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad9467_table1.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad9467_putty_serial_connection_configuration.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ad9467_zedboard_terminal.png
   :width: 900px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ad9467_device_manager.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ad9467_hardware_detected.jpg
   :width: 200px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ad9467_acquire.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ad9467_find_devices.jpg
   :width: 900px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/ad9467_init.jpg
   :width: 900px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ad9467_fft.png
   :width: 900px
