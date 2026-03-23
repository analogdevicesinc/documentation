AD-FMCOMMS2-EBZ User Guide
==========================

The :adi:`AD-FMComms2-EBZ` is an FMC board for the :adi:`AD9361` (:adi:`design package <en/license/licensing-agreement/ad9361.html>`), a highly integrated RF Agile Transceiver™. While the complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the AD-FMComms2-EBZ is to provide an RF platform which shows maximum performance of the AD9361. It’s expected that the RF performance of this platform can meet the datasheet specifications without issues at 2.4 GHz, and not much anywhere else. This is due to the external Johanson Technology's `2450BL15B050E <https://www.johansontechnology.com/datasheets/2450BL15B050/2450BL15B050.pdf>`_ 2.45 GHz Balun that is on the board. This balun is rated for a operating frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of various waveforms from a RF team before their custom hardware is complete, where they want to see waveforms at their frequency of interest, and are not afraid of changing out the balun if necessary. (Have a look in the :doc:`Configuration </solutions/reference-designs/fmcomms2/hardware/configuration_options>` sections).

The AD-FMComms2-EBZ board is very similar to the `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`_ board with only one exception, the RX/TX RF differential to single ended balun/transformer. The AD-FMComms3-EBZ is more targetted for wider tuning range applications, that is why we use the `TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`_ from mini Circuits as the RF transformer of choice. We affectionately call the FMCOMMS3-EBZ the "Software Engineers" platform, and the FMCOMMS2-EBZ, the "RF Engineers" platform to denote the difference.

.. image:: images/fmcomms2c_top.png
   :align: right
   :width: 400

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </solutions/reference-designs/fmcomms2/help_and_support>`.

-  :doc:`Introduction </solutions/reference-designs/fmcomms2/introduction>`
-  :doc:`Hardware </solutions/reference-designs/fmcomms2/hardware>`: This provides a brief description of the board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </solutions/reference-designs/fmcomms2/hardware>` (including :doc:`schematics </solutions/reference-designs/fmcomms2/hardware>`)

      -  :doc:`Functional Overview & Specifications </solutions/reference-designs/fmcomms2/hardware/functional_overview>`
      -  :doc:`Characteristics & Performance </solutions/reference-designs/fmcomms2/hardware/card_specification>`
      -  :doc:`Configuration options </solutions/reference-designs/fmcomms2/hardware/configuration_options>`
      -  :doc:`FCC or CE certification </solutions/reference-designs/fmcomms2/certification>`
      -  :doc:`Tuning the system </solutions/reference-designs/fmcomms2/hardware/tuning>`

   -   :doc:`Production Testing Process </solutions/reference-designs/fmcomms2/testing>`

-  Use the board to better understand the AD9361

   -  :doc:`What you need to get started </solutions/reference-designs/fmcomms2/prerequisites>`
   -  :doc:`Quick Start Guides </solutions/reference-designs/fmcomms2/quickstart>`

      -  :doc:`Linux on ZC702, ZC706, ZED, Altera SoCKit </solutions/reference-designs/fmcomms2/quickstart/zynq>`
      -  :doc:`Linux on ZCU102 </solutions/reference-designs/fmcomms2/quickstart/zynqmp>`
      -  :doc:`Linux on KC705, VC707 </solutions/reference-designs/fmcomms2/quickstart/microblaze>`
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

         -  `AD9361 Control in the IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_plugin>`_
         -  `Advanced AD9361 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_

      -  :doc:`Shell scripts </solutions/reference-designs/fmcomms2/software/linux/applications/shell_scripts>`
      -  `FRU EEPROM Utility <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`_

   -  Push custom data into/out of the AD9361

      -  :doc:`Basic Data files and formats </solutions/reference-designs/fmcomms2/software/basic_iq_datafiles>`
      -  :doc:`Create and analyze data files in MATLAB </solutions/reference-designs/fmcomms2/software/datafiles>`
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_
      -  `Python Interfaces <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_

-  Design with the AD9361

   -  :doc:`Understanding the AD9361 </solutions/reference-designs/fmcomms2/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :doc:`MATLAB Filter Design Wizard for AD9361 </solutions/reference-designs/fmcomms2/software/filters>`

   -  Simulation

      -  :doc:`MathWorks RF Blockset (formerly SimRF) Models of the AD9361 </solutions/reference-designs/fmcomms2/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_
         -  `ADS-B Airplane Tracking Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/adsb_example>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Targeting

      -  `Analog Devices Transceiver Toolbox for MATLAB and Simulink <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_

   -  Complete Workflow

      -  `ADS-B Airplane Tracking Tutorial <https://wiki.analog.com/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`_

   -  Design a custom AD9361 based platform

      -  Linux software

         -  :doc:`AD-FMCOMMS2/3/4-EBZ on Microblaze </solutions/reference-designs/fmcomms2/software/linux/microblaze>`
         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  :doc:`Build the demo on ZC702, ZC706, ZED or Altera SoCKit from source </solutions/reference-designs/fmcomms2/software/linux/zynq>`
         -  :doc:`Build the demo on KC705 or VC707 for Microblaze from source </solutions/reference-designs/fmcomms2/software/linux/microblaze>`
         -  :doc:`Build ZynqMP/MPSoC Linux kernel and devicetrees from source </solutions/reference-designs/fmcomms2/software/linux/zynqmp>`
         -  :doc:`Build the 2015_R2 Release Linux kernel from source </solutions/reference-designs/fmcomms2/software/linux/zynq_2015r2>`
         -  :doc:`Customizing the devicetree on the target </solutions/reference-designs/fmcomms2/software/linux/zynq_tips_tricks>`
         -  `AD7291 IIO ADC Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/ad7291>`_

      -  No-OS Driver

         -  :doc:`No-OS Application Programming Interface </solutions/reference-designs/fmcomms2/software/no-os-functions>`
         -  :doc:`No-OS Setup </solutions/reference-designs/fmcomms2/software/no-os-setup>`

      -  :doc:`HDL Reference Design </solutions/reference-designs/fmcomms2/reference_hdl>` which you must use in your FPGA.

         -  :doc:`Digital Interface Timing Validation </solutions/reference-designs/fmcomms2/interface_timing_validation>`

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_

-  :doc:`Help and Support </solutions/reference-designs/fmcomms2/help_and_support>`

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

`iiosdr.mp4 <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`_

ADI Articles
~~~~~~~~~~~~

-   Four Quick Steps to Production: Using Model-Based Design for
    Software-Defined Radio

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

.. esd-warning::


.. toctree::
   :hidden:

   ad9361
   additional_docs
   certification
   downloads
   hardware
   hardware/card_specification
   hardware/configuration_options
   hardware/functional_overview
   hardware/tuning
   help_and_support
   interface_timing_validation
   introduction
   iq_rotation
   prerequisites
   quickstart
   quickstart/microblaze
   quickstart/zynq
   quickstart/zynqmp
   reference_hdl
   software
   software/baremetal
   software/baremetal-filter
   software/baremetal/arradio_noos
   software/basic_iq_datafiles
   software/datafiles
   software/filters
   software/filters/license
   software/linux
   software/linux/applications/fru_dump
   software/linux/applications/shell_scripts
   software/linux/microblaze
   software/linux/zynq
   software/linux/zynq_2014r2
   software/linux/zynq_2015r2
   software/linux/zynq_tips_tricks
   software/linux/zynqmp
   software/matlab_bsp
   software/matlab_bsp_modem
   software/no-os-functions
   software/no-os-setup
   software/rfblkset_mdls_install
   software/rfblkset_mdls_run_testbench
   software/simrf
   testing
