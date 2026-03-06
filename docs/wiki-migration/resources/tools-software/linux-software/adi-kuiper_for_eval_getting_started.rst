Getting Started with ADI Kuiper Linux for Evaluation on ZedBoard
================================================================

This is to help you quickly setup an ADI Product Evaluation Board that is supported by a controller board that uses ADI Kuiper Linux and ADI ACE software. The EVAL-SD-KUIPERZ SD Card contains a pre-configured version ADI Kuiper Linux intended for use with ACE and is included as part of the supported Product Evaluation Board kit.

.. note::

   If you are looking for the normal ADI Kuiper Linux SD card image, that is available from this page: :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


Hardware Required
-----------------

-  ADI Product Evaluation Board supported by ADI Kuiper Linux and ACE on ZedBoard
-  SD Card with ADI Kuiper Linux for Evaluation

   -  This is included with supported Product Evaluation Boards, but can also be created by following the instructions here: :doc:`ADI Kuiper Linux with support for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

-  PC - Windows 7 or later, Windows 10 is recommended.
-  `Digilent ZedBoard kit <https://digilent.com/reference/programmable-logic/zedboard/start>`__, including PSU and USB A to micro-B cable

Getting Started
---------------

-  Download and install the ACE Software tool from the :adi:`ACE` download page. If ACE is already installed, make sure you have the latest version by using the ‘Check For Updates’ option in the ACE sidebar.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ace_sidebar-check-for-updates.png
   :align: center
   :width: 200px

-  Run ACE and select ‘Plug-in Manager’ from the ACE sidebar to install the board plug-in that supports the Product Evaluation Board and select Available Packages. You can use the search field to help filter the list of boards to find the relevant one. An ACE Quickstart guide is available here: :doc:`ACE Quickstart - Using ACE and Installing Plug-ins </wiki-migration/resources/tools-software/ace/userguide/quickstart>`

.. container:: column

   \ |image1|\


.. container:: column right



|image2|

-  Insert the EVAL-SD-KUIPERZ SD card into the SD card slot on the underside of the ZedBoard.

.. note::

   If there is a need to re-image or create a new SD card, instructions are available here: :doc:`ADI Kuiper Linux with support for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`.


-  Ensure the ZedBoard boot configuration jumpers are set to use the SD card as shown.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zedboard-sd-card-boot-jumpers.png
   :align: center
   :width: 200px

.. important::

   To avoid potential damage, ensure the VADJ SELECT jumper is set to the correct voltage for the Product Evaluation Board.


-  Connect the Product Evaluation Board to the FMC connector on the ZedBoard.

.. note::

   There may be additional steps and hardware required for a given Product Evaluation Board, for example, function generators connections and setup. This information may be included with the eval kit or in the User guide for the corresponding Product Evaluation Boards page that can be found by searching :adi:`Product Evaluation Boards and Kits <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits.html>`.


-  Connect the USB cable from the PC to the J13/USB OTG port and the PSU to J20/DC input.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zedboard-usb_otg-power.png
   :align: center
   :width: 200px

-  Slide SW8/POWER switch to the ON position. The green LD13/POWER LED should turn on.
-  The blue LD12/DONE LED & red LD0 LED should start blinking ~20-30 seconds later which indicates the boot process is complete.

.. tip::

   Linux versions prior to ADI Kuiper Linux for Evaluation version 2024-8-27 will instead boot with the BLUE LD12/DONE LED blinking immediately and LD7 blinking after ~20-30Seconds. This may indicate that an improved version of the ACE plugin is available if the SD-Card is updated to the latest version.


-  Launch the ACE software from the Analog Devices folder in the Windows Start menu. The Evaluation Board should appear in the ACE Start Tab >> Attached Hardware view.

.. image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/ace_attached_hw-screen.png
   :align: center
   :width: 200px

Beyond Evaluation…
------------------

-  :doc:`ADI Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` supports development of software that interfaces with the Linux Industrial I/O (IIO) system using :doc:`libiio </wiki-migration/resources/tools-software/linux-software/libiio>`.
-  Python can also be used to interact with ADI Kuiper Linux and IIO devices. The ADI :doc:`pyadi-iio </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` package makes using IIO devices from python much easier.
-  MATLAB support for IIO devices is provided by :doc:`ADI Toolboxes for MATLAB and Simulink </wiki-migration/resources/tools-software/matlab>`
-  Source code for the :git-linux>`__, `HDL <https::`Linux drivers and kernel </github.com/analogdevicesinc/hdl>` and related software is available from `analogdevicesinc on GitHub <repo>>`__

Getting Support
---------------

-  If you are having difficulties getting up and running, refer to the following for assistance - :doc:`Troubleshooting Guide for ADI Kuiper Linux for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_ace_troubleshooting>`
-  Should there be a need to create a new or update an existing SD card image, instructions are available here - :doc:`wiki.analog.com/resources/tools-software/linux-software/adi-kuiper_images_for_ace </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`
-  Finally, if you need additional support, please contact ADI using the `EngineerZone <ez>>`__ forums.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ace_sidebar-plug-in_manager.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ace_plug-in_manager-avaialable_selected.png
   :width: 200px
