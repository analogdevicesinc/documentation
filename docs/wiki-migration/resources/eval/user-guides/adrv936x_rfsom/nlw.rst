ADI AD9361 System on Module (SOM) SDR
=====================================

.. image:: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :alt: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :align: right

The :adi:`ADRV9361-Z7035` and :adi:`ADRV9364-Z7020` are built on a portfolio of highly integrated System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC. Built on the AD9361, it is schematically & HDL similar to the `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`__.

The purpose of the RF SOM is to provide an RF platform to software developers, system architects, product developers, etc, who want a single platform which operates over a wide tuning range (70 MHz – 6 GHz) that is capable of both being used for prototype and evaluation, as well as production volume.

Table of Contents
-----------------

-  `Introduction <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/introduction>`__
-  `RF SOM Hardware <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/adrv936x_rfsom/hardware>`__
-  `User Guide <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/adrv936x_rfsom/user-guide>`__
-  `Tuning the system <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/hardware/tuning>`__
-  `Environmental Testing <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/adrv936x_rfsom/testing>`__
-  Carriers

   -  `FMC Carrier (PZSDRCC-FMC) <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/pzsdr/carriers/fmc>`__
   -  `Breakout Carrier (PZSDRCC-BRK) <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/pzsdr/carriers/brk>`__
   -  `PCIe Carrier (PZSDRCC-PCIE) <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/pzsdr/carriers/pcie>`__
   -  `PackRF Carrier (PZSDRCC-PackRF) <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/pzsdr/carriers/packrf>`__

-  `Power and Sequencing <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/pzsdr/power-and-sequencing>`__
-  Use the RF SOM Hardware to better understand the AD9361

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/prerequisites>`__
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/quickstart>`__

      -  `Linux on RF SOM <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/quickstart/zynq>`__
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/zynq_images>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
      -  :doc:`AD9361 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`
      -  :doc:`AD9361 Advanced Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`__

   -  Push custom data into/out of the RF SOM SDR.

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/basic_iq_datafiles>`__
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/datafiles>`__
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      -  :doc:`AD9361 libiio streaming example </wiki-migration/resources/tools-software/linux-software/libiio>`

-  Design with the AD9361

   -  `Understanding the AD9361 <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/ad9361>`__

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard for AD9361 <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/filters>`__

   -  Simulation

      -  `MathWorks SimRF Models of the AD9361 <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/simrf>`__

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         -  :doc:`Beacon Frame Receiver Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :doc:`QPSK Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :doc:`LTE Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/lte_example>`
         -  :doc:`ADS-B Airplane Tracking Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/adsb_example>`

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`FM Radio/Tuner </wiki-migration/resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :doc:`C example </wiki-migration/resources/tools-software/linux-software/libiio>`

   -  Targeting

      -  :doc:`Analog Devices BSP for MathWorks HDL Workflow Advisor </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

   -  Complete Workflow

      -  :doc:`ADS-B Airplane Tracking Tutorial </wiki-migration/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`

   -  Design a custom AD9361 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux>`__

         -  :doc:`Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         -  `Build the demo on ZC702, ZC706, or ZED from source <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux/zynq>`__
         -  `Build the demo on KC705 or VC707 for Microblaze from source <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux/microblaze>`__
         -  `Build the 2014_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`__
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`__

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/software/baremetal>`__
      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/reference_hdl>`__ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/interface_timing_validation>`__

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms1-ebz/math>`__

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/ad-fmcomms2-ebz/help_and_support>`__
-  Videos and Webinars

   -  `Radio Deployment on SoC Platforms <https://www.mathworks.com//videos/radio-deployment-on-soc-platforms-1513346830203.html>`__

Warning
-------

.. esd-warning::

