Formatting and Flashing SD Cards using Windows
==============================================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated. Please see here the updated documentation https://analogdevicesinc.github.io/documentation/linux/kuiper/sdcard/index.html


This page will explain how you should go about formatting and flashing the SD card with the software required to use many of platforms Analog Devices supports. There are several steps that need to be completed before your SD Card will be ready to use.

-  Download the compressed software image file
-  Extract the software image file
-  Connect the SD Card to the computer
-  Verify the software image file (Optional)
-  Format the SD Card (Optional)
-  Flash the SD Card

Download the SD Card File
-------------------------

Download the software image file you want to write onto your SD Card. Typically this is going to be the standard :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`, but in some instances specialized pre-compiled images are created for projects that are not yet included on the standard image. So be sure you have the correct file.

-  Save the .Zip file or .Xz file to your local hard drive, and remember the file location.

Extract the Software Image File
-------------------------------

This step will decompress the large software image file you downloaded. Ensure you have a decompression utility installed on your computer, capable of extracting `.Zip file format <https://en.wikipedia.org/wiki/Zip_(file_format)>`_ or `.Xz file format <https://en.wikipedia.org/wiki/Xz>`_ such as:

.. admonition:: Download
   :class: download

   
   -  `7-Zip <http://www.7-zip.org/>`_
   


-  Extract the software image file to a known location on your computer.

   


|image1|

Connect the SD Card to the Computer
-----------------------------------

Connect the SD Card to either an internal or external SD Card reader which is connected to your computer. Most newer computers have an SD Card reader, but there are plenty of USB connectable SD Card reader devices available.

Verify the Download (Optional)
------------------------------

This step is used to validate that the image you downloaded. Ensuring that it is the version is correct and that the software wasn't corrupted during download.

Ensure you have the following application installed on your computer.

.. admonition:: Download
   :class: download

   
   -  `WinMD5 <http://www.winmd5.com/>`_
   


-  Open up WinMD5 application on your computer.
-  Browse to the extracted file location.
-  Check the m5dsum of the resulting file.

|image2|

Format the SD Card (Optional)
-----------------------------

This step should be used if the SD Card format is unknown or needs to be reconfigured.

Using SD Card Formatter
~~~~~~~~~~~~~~~~~~~~~~~

Ensure you have the following application installed on your computer.

.. admonition:: Download
   :class: download

   
   -  `SD Card Formatter <https://www.sdcardformatter.com/>`_
   


Open the SD Card Formatter application on your computer, and set the following fields:

-  **Select Card** = SD Card drive you want to format (usually says "boot" or "volume")
-  **Card Information** = Make sure the disc size approximately matches your SD Card capacity
-  **Formatting Options** = Select Quick Format\

|image3|

-  Once set, click the **Format** button
-  The program will notify you that the formatting is complete.(could take several minutes)\

|image4|

Using DISKPART via Windows command prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows command prompt has **DISKPART** that is also capable of reformatting SD cards and other drives.

-  Run Windows command prompt as administrator.
-  Type 'list disk'. All current dives will be shown.
-  Type 'select disk X' where X is the SD card drive number. (Do not mistake this part)
-  Type 'clean' to clean the drive. If an error occurs simply retry typing 'clean'.
-  Type 'create partition primary'.
-  Type 'format fs=FAT32'. The formatting may take 45 minutes or so. FAT32 is the tested file system type.
-  After the progress is at 100%, type 'assign' to finalize the drive letter for Windows.

Flash the SD Card
-----------------

This step will physically write the software image file onto the SD Card so it will be ready for use.

There are several Windows applications that can flash SD Cards, we will describe how to do it using two common tools. Ensure you have at least one of the following tools installed on your computer.

.. admonition:: Download
   :class: download

   
   -  `Win32DiskImager from Sourceforge <https://sourceforge.net/projects/win32diskimager/files/latest/download?source=navbar>`_
      OR
   -  `Etcher from Sourceforge <https://sourceforge.net/projects/etcher.mirror/>`_
   


.. important::

   If you are unsure, or don't understand these directions - STOP. If you are not careful, you could accidentally write a Linux image to your PC hard drive. Your PC will not function properly after this, and your IT department should not blame ADI.


Win32DiskImager
~~~~~~~~~~~~~~~

-  Open up the Win32DiskImager application on your PC\


|image5|

-  Using the small folder button in the **Image File** section, navigate to the location of your software image file you want to flash and select it.\

|image6|

-  Double check that the **Device** location in the upper-right corner, matches the SD Card drive location.

.. warning::

   You DO NOT want to accidently re-image your hard drive, so this step is critical to ensure you are flashing the SD Card and not anything else.


-  When you are ready to flash the SD Card, click on the "Write" button.
-  Win32DiskImager will also alert you to make sure you want to write to this drive, acting as another failsafe so that you don't accidently image the wrong drive.\

|image7|

-  Flashing the image to the SD Card typically take 10-15 minutes, but a progress bar is provided during the process. So grab yourself a coffee.
-  "Write Successful" will appear when the program is finished, letting you know the SD Card is ready.\

|image8|

-  Exit the Win32DiskImager program, and use the Windows "safely remove hardware" function to eject the disk, before physically removing the SD card from the reader.

Etcher
~~~~~~

-  Open Balena Etcher and select the .img file you want to write to the SD card.\ |image9|\


|image10|

-  Select the drive you want to write your image to.(should display as an SD Card)\ |image11|\

|image12|

-  Review your selections and click 'Flash!' to begin writing data to the SD card.\ |image13|\

|image14|

-  After flashing, Etcher will automatically validate the image flash correctly. You can either wait for this to finish or click skip.\

|image15|

-  After the validation is complete, your SD card is finished and ready for use.\

|image16|

-  Go to the toolbar of your Windows OS, and click on "safely remove hardware", and remove your completed SD card.

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/7zip.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/quickstart/winmd5free2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_formatter_gui.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_format_success.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_flash_gui.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_flash_file_select.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_flash_write_confirm.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/sd_card_flash_success.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_start.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_file_select.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_disk_select.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_disk_selection.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_sd_card_selected.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_flashing_sd_card.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_verifying.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zynq_images/etcher_finished.png
   :width: 400px
