ADI Kuiper Linux for Evaluation
===============================

This is a version of the standard ADI Kuiper Linux SD card image that has been customized to support product evaluation with the ACE software. There are two separate images for the currently supported controller boards, the first is pre-configured to boot Linux on the `ZedBoard <http://zedboard.org/product/zedboard>`__ and also enables the ZedBoard USB OtG port. The second image is configured to boot Linux on the `CoraZ7 <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__.

.. note::

   If you are looking for the normal ADI Kuiper Linux SD card image, that is available from this page: :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


Requirements
------------

-  You need a Host PC (Windows or Linux).
-  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).
-  You need an SD card that is at least 16GB.

Download Linux Image
--------------------

.. container:: leftalign

   ADI Kuiper Linux for Evaluation greatly simplifies the SD-Card configuration and enables a plug & play Embedded Linux experience with ACE and ZedBoard/Cora Z7 for supported products.

   
   .. note::

      For the Cora Z7 image and for the Zedboard version 2024-08-27, all board configuration is handled from within the ACE plugin, scripts are no longer required.

   
   The two versions of the image are available for download below


Zedboard
~~~~~~~~

.. admonition:: Download
   :class: download

   \ `Get Latest ADI Kuiper for Evaluation (Zedboard) <https://swdownloads.analog.com/cse/kuiper/ADI-Kuiper-for-Evaluation-2024-08-27.zip>`__

   
   Release Version: 2024-08-27
   
   md5sum ADI-Kuiper-for-Evaluation-2024-08-27.zip 10AC4111B331DB4FF6551EA96B3623BB
   
   md5sum ADI-Kuiper-for-Evaluation-2024-08-27.img 08DD878BB416EEA9FE645B6ADDFA8D05


Cora Z7
~~~~~~~

.. admonition:: Download
   :class: download

   \ `Get Latest ADI Kuiper for Evaluation (CoraZ7) <https://packages.analog.com/public/raw/files/image_2026-02-04-ADI-Kuiper-Linux-for-Evaluation-coraz7s.zip>`__

   
   Release Version: 2026-02-04
   
   md5sum image_2026-02-04-ADI-Kuiper-Linux-for-Evaluation-coraz7s.zip 2561E23C583C7B1A3D970EB064622FB9
   
   md5sum image_2026-02-04-ADI-Kuiper-Linux-armhf.img A9D21D4D7C6AEC16C3A3E4BA6C703D32


.. important::

   Make sure you unzip the image using either `7-zip <https://www.7-zip.org/>`__ or on Linux it can be done via command-line **unzip <image_name>.zip**. The actual file that needs to be dumped to the SD card has to have the **\*.img** extension.


.. important::

   Your SD-card needs to be at least 16 GB.


.. warning::

   If your computer has security restrictions imposed by your company's IT department, which prevent you from writing data to SD-cards (or the data is encrypted when written on the SD-card), then consider using a computer that doesn't have such restrictions or communicating with your IT department to find a solution.




.. raw:: html

   <details><summary>Older Releases, Zedboard(Click to expand)</summary>

.. admonition:: Download
   :class: download

   
   -  **28 July 2021 ADI Kuiper Linux with support for ACE Evaluation - Release 6, 14 August 2024**
   
      -  Supports the following evaluation boards:
   
         -  EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, EVAL-AD4630-16FMCZ
         -  EVAL-ADAQ8092-FMCZ
         -  EVAL-AD4858FMCZ, EVAL-AD4857FMCZ
         -  EVAL-AD4080FMCZ
   
      -  After writing this image to an SD card, the boot configuration needs to be set to match the evaluation board that is going to be used with ACE.
   
         -  The default boot configuration is for an EVAL-ADA4858FMCZ board.
   
      -  To configure for a different evaluation board, boot the ZedBoard with the imaged SD card, and connect a USB cable to the ZedBoard USB UART or OtG port. Then using a terminal program, e.g. putty or Teraterm, open a serial port at 115200 baud to get a terminal shell.
      -  Then run the script that corresponds to the board you want to use with the options required.
   
         -  ``eval-ad4630`` - same script for EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, EVAL-AD4630-16FMCZ
         -  ``eval-adaq8092``
         -  ``eval-ad4858`` - same script for EVAL-AD4858FMCZ, EVAL-AD4857FMCZ
         -  ``eval-ad4080``
   
      -  Add '' configure'' after the script name to get a list of the different configuration options required by a given script. Each script has specific configure options.
   
         -  For Example: ``eval-ad4858 configure`` to get the options, and then ``eval-ad4858 configure ad4857 cmos`` to do the configuration action
         -  If an invalid set of options is selected, errors will be reported.
   
      -  After a successful configuration, the ``reboot`` or ``shutdown now`` commands can be issued as needed.
      -  Note: If ``eval-ad4630`` is used to configure the SD card and a supported evaluation board in that family is not connected when the board is rebooted, the Linux kernel will panic and the system will fail to boot. In that event, either connect an AD4630 family evaluation board, or follow the instructions on this page :doc:`kuiper-linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` to restore a bootable configuration, such as the 'zynq-zed-adv7511'. Once that configuration has booted, connect to the serial console port on USB UART/J14 on the ZedBoard and issue the commands to reconfigure the board as required.
   
   ::
   
        * [[https://swdownloads.analog.com/cse/kuiper/2021-07-28-ADI-Kuiper-full-for-ace-r6-2024-08-14.zip|Actual file]]
      * md5sum 2021-07-28-ADI-Kuiper-full-for-ace-r6-2024-08-14.zip    ''01BBDB4C174312A37E6566D8C0634019''
      * md5sum 2021-07-28-ADI-Kuiper-full-for-ace-r6-2024-08-14.img    ''39C8444BD9ADF25CAE928E25F7F84F2A''
   


.. admonition:: Download
   :class: download

   
   -  **28 July 2021 ADI Kuiper Linux with support for ACE Evaluation - Release 5, 2 April 2024**
   
      -  Supports the following evaluation boards:
   
         -  EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, EVAL-AD4630-16FMCZ
         -  EVAL-ADAQ8092-FMCZ
         -  EVAL-AD4858FMCZ
         -  EVAL-AD4080FMCZ
   
      -  After writing this image to an SD card, the boot configuration needs to be set to match the evaluation board that is going to be used with ACE.
   
         -  The default boot configuration is for an EVAL-ADAQ8092-FMCZ board.
   
      -  To configure for a different evaluation board, boot the ZedBoard with the imaged SD card, and connect a USB cable to the ZedBoard USB UART or OtG port. Then using a terminal program, e.g. putty or Teraterm, open a serial port at 115200 baud to get a terminal shell.
      -  Then run the script that corresponds to the board you want to use with the options required.
   
         -  ``eval-ad4630`` - same script for EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, EVAL-AD4630-16FMCZ
         -  ``eval-adaq8092``
         -  ``eval-ad4858``
         -  ``eval-ad4080``
   
      -  Add '' configure'' after the script name to get a list of the different configuration options required by a given script. Each script has specific configure options.
   
         -  For Example: ``eval-ad4858 configure`` to get the options, and then ``eval-ad4858 configure cmos`` to do the configuration action
         -  If an invalid set of options is selected, errors will be reported.
   
   ::
   
        * [[https://swdownloads.analog.com/cse/kuiper/2021-07-28-ADI-Kuiper-full-for-ace-r5-2024-04-02.zip|Actual file]]
      * md5sum 2021-07-28-ADI-Kuiper-full-for-ace-r5-2024-04-02.zip    ''56901ab486d6d3f1b5e62b2661f53827''
      * md5sum 2021-07-28-ADI-Kuiper-full-for-ace-r5-2024-04-02.img    ''33349d31cad19197ac706b80486e07f7''

.. raw:: html

   </details>


Now, depending on if you are using Linux or Windows, follow these instructions to write the file to your SD card.

-  :doc:`linux_hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`
-  :doc:`windows_hosts </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

Once the SD card image is programmed it can be inserted into the host controller SD card slot. Follow the hardware setup guide for the evaluation board you are using to complete the setup to get up and running.

-  :doc:`Getting Started with ADI Kuiper Linux for Evaluation on ZedBoard </wiki-migration/resources/tools-software/linux-software/adi-kuiper_for_eval_getting_started>`
-  :doc:`Getting Started with ADI Kuiper Linux for Evaluation on CoraZ7 </wiki-migration/resources/tools-software/linux-software/adi-kuiper_for_eval_getting_started_cz7>`

Getting Support
---------------

-  If you are having difficulties getting up and running, refer to the following for assistance - :doc:`Troubleshooting Guide for ADI Kuiper Linux for Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_ace_troubleshooting>`
-  Finally, if you need additional support, please contact ADI using the `EngineerZone <ez>>`__ forums.
