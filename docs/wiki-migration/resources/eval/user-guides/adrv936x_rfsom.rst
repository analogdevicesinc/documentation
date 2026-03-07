ADI ADRV936x System on Module (SOM) SDR
=======================================

.. image:: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :alt: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :align: right

The :adi:`ADRV9361-Z7035` and :adi:`ADRV9364-Z7020` are built on a portfolio of highly integrated System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC.

:adi:`ADRV9361-Z7035` is built on the Analog Devices :adi:`AD9361` and the Xilinx XC7Z035-L2FBG676I, it is schematically & HDL similar to the `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`_. It requires Vivado license.

:adi:`ADRV9364-Z7020` is built on the :adi:`AD9361` and the Xilinx XC7Z020-1CLG400I, it is schematically & HDL similar to the `ad-fmcomms4-ebz <https://wiki.analog.com/ad-fmcomms4-ebz>`_.

The purpose of the RF SOM is to provide an RF platform to software developers, system architects, product developers, etc, who want a single platform which operates over a wide tuning range (70 MHz – 6 GHz) that is capable of both being used for prototype, evaluation and reference design to help with production volume.

Table of Contents
-----------------

-  Introduction

   -  :doc:`Introduction to boards based on the AD9361 </wiki-migration/resources/eval/user-guides/adrv936x/introduction>`
   -  :doc:`Introduction to ADRV9361-Z7035 </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/user-guide/introduction>`
   -  :doc:`ADRV9361-Z7035 Quick start guide </wiki-migration/resources/eval/user-guides/adrv9361-z7035/quickstart>`

-  Hardware

   -  :doc:`Schematic and Layout revisions </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/hardware>`
   -  :doc:`Power and Sequencing </wiki-migration/resources/eval/user-guides/pzsdr/power-and-sequencing>`
   -  :doc:`Performance </wiki-migration/resources/eval/user-guides/adrv9361-z7035/performance>`
   -  :doc:`Electrical specifications </wiki-migration/resources/eval/user-guides/adrv9361-z7035/electrical-specifications>`
   -  :doc:`Cable brackets </wiki-migration/resources/eval/user-guides/pzsdr/cable-brackets>`
   -  :doc:`Additional information </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/user-guide/additional-information>`
   -  :doc:`Certifications and Environmental Testing </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/testing>`

-  Carriers

   -  :doc:`FMC Carrier (ADRV1CRR-FMC) </wiki-migration/resources/eval/user-guides/pzsdr/carriers/fmc>`
   -  :doc:`Breakout Carrier (ADRV1CRR-BOB) </wiki-migration/resources/eval/user-guides/pzsdr/carriers/brk>`
   -  :doc:`PCIe Carrier (PZSDRCC-PCIE) </wiki-migration/resources/eval/user-guides/pzsdr/carriers/pcie>`
   -  :doc:`PackRF Carrier (PZSDRCC-PackRF) </wiki-migration/resources/eval/user-guides/pzsdr/carriers/packrf>`

-  Use the RF SOM Hardware to better understand the AD9361

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      -  :doc:`Linux on RF SOM </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
      -  :doc:`AD9361 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_plugin>`
      -  :doc:`AD9361 Advanced Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      -  :doc:`Command Line/Shell scripts </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   -  Push custom data into/out of the RF SOM SDR.

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      -  :doc:`Create and analyze data files in MATLAB </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      -  :doc:`AD9361 libiio streaming example </wiki-migration/resources/tools-software/linux-software/libiio>`

-  Design with the AD9361

   -  :doc:`Understanding the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :doc:`MATLAB Filter Design Wizard for AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   -  :doc:`Tuning the AD9361/AD9364 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`
   -  Simulation

      -  :doc:`MathWorks SimRF Models of the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         -  :doc:`Beacon Frame Receiver Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :doc:`QPSK Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :doc:`LTE Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/lte_example>`
         -  :doc:`ADS-B Airplane Tracking Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/adsb_example>`
         -  :doc:`AGC Optimization Example </wiki-migration/resources/eval/user-guides/ad9361_agc_tuning>`

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`FM Radio/Tuner </wiki-migration/resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :doc:`C example </wiki-migration/resources/tools-software/linux-software/libiio>`

   -  Targeting

      -  :doc:`Analog Devices BSP for MathWorks HDL Workflow Advisor </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

   -  Complete Workflow

      -  :doc:`ADS-B Airplane Tracking Tutorial </wiki-migration/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`
      -  :doc:`Frequency Hopping Controller </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/frequency_hopping>`
      -  :doc:`QPSK Modem Design Workflow </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`
      -  :doc:`Implementing a Loopback Delay Estimation Algorithm </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/tutorials/loopback_delay_estimation>`

   -  Design a custom AD9361 based platform

      -  :doc:`Linux software </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         -  :doc:`Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         -  :doc:`Build the demo on ZC702, ZC706, or ZED from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         -  :doc:`Build the demo on KC705 or VC707 for Microblaze from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`
         -  :doc:`Build the 2014_R2 Release Linux kernel from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         -  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      -  :doc:`No-OS Driver </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`
      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>` which you must use in your FPGA.

         -  :doc:`Digital Interface Timing Validation </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

-  Additional Documentation about SDR Signal Chains

   -  :doc:`The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`
-  Videos and Webinars

   -  `Radio Deployment on SoC Platforms <https://www.mathworks.com//videos/radio-deployment-on-soc-platforms-1513346830203.html>`_

Warning
-------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_

