AD-FMCOMMS2-EBZ User Guide
==========================

The :adi:`AD-FMComms2-EBZ` is an FMC board for the :adi:`AD9361` (:adi:`design package <en/license/licensing-agreement/ad9361.html>`), a highly integrated RF Agile Transceiver™. While the complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the AD-FMComms2-EBZ is to provide an RF platform which shows maximum performance of the AD9361. It’s expected that the RF performance of this platform can meet the datasheet specifications without issues at 2.4 GHz, and not much anywhere else. This is due to the external Johanson Technology's `2450BL15B050E <https://www.johansontechnology.com/datasheets/2450BL15B050/2450BL15B050.pdf>`_ 2.45 GHz Balun that is on the board. This balun is rated for a operating frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of various waveforms from a RF team before their custom hardware is complete, where they want to see waveforms at their frequency of interest, and are not afraid of changing out the balun if necessary. (Have a look in the :doc:`Configuration </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>` sections).

The AD-FMComms2-EBZ board is very similar to the `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`_ board with only one exception, the RX/TX RF differential to single ended balun/transformer. The AD-FMComms3-EBZ is more targetted for wider tuning range applications, that is why we use the `TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`_ from mini Circuits as the RF transformer of choice. We affectionately call the FMCOMMS3-EBZ the "Software Engineers" platform, and the FMCOMMS2-EBZ, the "RF Engineers" platform to denote the difference.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/fmcomms2c_top.png
   :align: right
   :width: 400px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
-  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware>`: This provides a brief description of the board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware>` (including :doc:`schematics </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware>`)

      -  :doc:`Functional Overview & Specifications </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`
      -  :doc:`Characteristics & Performance </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/card_specification>`
      -  :doc:`Configuration options </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`
      -  :doc:`FCC or CE certification </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/certification>`
      -  :doc:`Tuning the system </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`

   -   :doc:`Production Testing Process </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/testing>`

-  Use the board to better understand the AD9361

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      -  :doc:`Linux on ZC702, ZC706, ZED, Altera SoCKit </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
      -  :doc:`Linux on ZCU102 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynqmp>`
      -  :doc:`Linux on KC705, VC707 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/microblaze>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

         -  :doc:`AD9361 Control in the IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`
         -  :doc:`Advanced AD9361 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`

      -  :doc:`Shell scripts </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`
      -  :doc:`FRU EEPROM Utility </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

   -  Push custom data into/out of the AD9361

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      -  :doc:`Create and analyze data files in MATLAB </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/transceiver-toolbox>`
      -  :doc:`AD9361 libiio streaming example </wiki-migration/resources/tools-software/linux-software/libiio>`
      -  :doc:`Python Interfaces </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`

-  Design with the AD9361

   -  :doc:`Understanding the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :doc:`MATLAB Filter Design Wizard for AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   -  Simulation

      -  :doc:`MathWorks RF Blockset (formerly SimRF) Models of the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/transceiver-toolbox>`
         -  :doc:`Beacon Frame Receiver Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :doc:`QPSK Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :doc:`LTE Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/lte_example>`
         -  :doc:`ADS-B Airplane Tracking Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/adsb_example>`

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`FM Radio/Tuner </wiki-migration/resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :doc:`C example </wiki-migration/resources/tools-software/linux-software/libiio>`

   -  Targeting

      -  :doc:`Analog Devices Transceiver Toolbox for MATLAB and Simulink </wiki-migration/resources/tools-software/transceiver-toolbox>`

   -  Complete Workflow

      -  :doc:`ADS-B Airplane Tracking Tutorial </wiki-migration/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`

   -  Design a custom AD9361 based platform

      -  Linux software

         -  :doc:`AD-FMCOMMS2/3/4-EBZ on Microblaze </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`
         -  :doc:`Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         -  :doc:`Build the demo on ZC702, ZC706, ZED or Altera SoCKit from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         -  :doc:`Build the demo on KC705 or VC707 for Microblaze from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`
         -  :doc:`Build ZynqMP/MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
         -  :doc:`Build the 2015_R2 Release Linux kernel from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2015r2>`
         -  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`
         -  :doc:`AD7291 IIO ADC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7291>`

      -  No-OS Driver

         -  :doc:`No-OS Application Programming Interface </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/no-os-functions>`
         -  :doc:`No-OS Setup </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/no-os-setup>`

      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>` which you must use in your FPGA.

         -  :doc:`Digital Interface Timing Validation </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

-  Additional Documentation about SDR Signal Chains

   -  :doc:`The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Videos
------

Introduction to the AD9361
~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`AD9361 RF Agile Transceiver <en/education/education-library/videos/2752786084001.html>`

Introduction to the AD9361 based ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`AD9361 RF Transceiver and Support Ecosystem <en/education/education-library/videos/2753072929001.html>`

Digital Filter Wizard for the AD9361
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`Digital Filter Design For Integrated RF Transceivers <en/education/education-library/videos/3845680080001.html>`

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4
   :alt: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

-   Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and RF Blockset (formerly SimRF) <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

Warning
-------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_

