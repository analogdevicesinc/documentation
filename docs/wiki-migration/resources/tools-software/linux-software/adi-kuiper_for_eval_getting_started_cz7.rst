.. important::

   Please Note,The CoraZ7 support with ACE is still in progress and not yet released!


Getting Started with ADI Kuiper Linux for Evaluation on Cora Z7
===============================================================

This is to help you quickly setup an ADI Product Evaluation Board that is supported by a controller board that uses ADI Kuiper Linux and ADI ACE software. The EVAL-SD-CZ7-KUIPERZ SD Card contains a pre-configured version ADI Kuiper Linux intended for use with ACE and is included as part of the supported Product Evaluation Board kit.

.. note::

   If you are looking for the normal ADI Kuiper Linux SD card image, that is available from this page: :doc:`Kuiper Linux </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`.


Additional System Requirements
------------------------------

-  ADI Product Evaluation Board supported by ADI Kuiper Linux and ACE on Cora Z7
-  Micro SD Card with ADI Kuiper Linux for Evaluation

   -  This is included with supported Product Evaluation Boards, but can also be created by following the instructions here: :doc:`ADI Kuiper Linux with support for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`

-  PC - Windows 10 (64-bit) or later is recommended.
-  `Digilent Cora Z7 kit <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`__, Ethernet cable (for network connection) and a USB-A to Micro-B cable (for power and UART)

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

-  Insert the EVAL-SD-CZ7-KUIPERZ SD card into the SD card slot on the underside of the CoraZ7.

.. note::

   If there is a need to re-image or create a new SD card, instructions are available here: :doc:`ADI Kuiper Linux with support for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`.


::

   *Ensure the Cora Z7 boot and power configuration jumpers are set as shown.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/combinedjumpers_cz7.png
   :align: center
   :width: 400px

+-----------------+--------------------------------------------------------------------------------+---------------------------------+
| Jumper Location | Description                                                                    | Shunt Placement                 |
+=================+================================================================================+=================================+
| JP2             | Selects how the CoraZ7-07s board boots. We want to boot from the microSD card  | Across Pins 1 & 2               |
+-----------------+--------------------------------------------------------------------------------+---------------------------------+
| JP3             | Selects how the CoraZ7-07s board is powered. We are powering from the USB port | Across Pins 2 & 3 (labeled USB) |
+-----------------+--------------------------------------------------------------------------------+---------------------------------+

-  Connect the Product Evaluation Board to the Arduino connector on the Cora Z7. There may be additional steps and hardware, e.g., function generators connections and setup. This information may be included with the eval kit or can be found in the User Guide on the corresponding Product Evaluation Boards page on www.analog.com

-  Connect the Ethernet cable directly from the PC to the Ethernet port on the Cora Z7 (May need to use an adapter if there's no Ethernet port on your PC).

-  Connect the USB from the PC to the micro-USB port on the CoraZ7. The red LD7/POWER LED should turn on.

-  The green LD1 LED then starts blinking ~20-30 seconds later which indicates the boot process is complete.

-  Launch the ACE software from the Analog Devices folder in the Windows Start menu. The Evaluation Board should appear in the ACE Start Tab >> Attached Hardware view.

.. image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/ace_attached_hw-screen.png
   :align: center
   :width: 400px

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
