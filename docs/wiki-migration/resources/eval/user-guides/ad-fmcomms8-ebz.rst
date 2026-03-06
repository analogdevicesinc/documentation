AD-FMCOMMS8-EBZ
===============

Introduction
------------

The :adi:`AD-FMCOMMS8-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcomms8-ebz.html>` is an integrated RF design containing two Analog Devices :adi:`ADRV9009` wideband transceivers. By connecting to a compatible FPGA development board that supports FMC HPC mechanical connector and JESD204B bus interface it can be used for evaluation and prototyping with upto 4 Transmit and Receive channels that can be synchronised in phase and frequency. Additionally it can be used with the ADRV9009-ZU11EG RF-SOM system. This gives a path to evaluating and prototyping with upto 8 phase and frequency synchronised Transmit and Receive channels for complex multi-stream applications ensuring end-to-end deterministic latency.

The ADRV9009 Transceivers include integrated LO and phase synchronization. Overall system frequency & phase synchronization is maintained with a clock tree structure using ADI high performance low jitter :adi:`HMC7044` device, making it ideal for applications requiring RF phase alignment with a large number of channels.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/fmcomms8-top.png
   :align: right
   :width: 400px

Highlevel Specification
-----------------------

-  Two ADRV9009 devices, providing (in total):

   -  Quad transmitters
   -  Quad receivers
   -  Quad input Observation Receiver for DPD
   -  Max Rx BW: 200 MHz
   -  Max Tunable Tx synthesis BW: 450 MHz
   -  Max Observation Rx BW: 450 MHz
   -  Fully integrated fractional-N RF synthesizers
   -  Multi-chip phase synchronization for all RF LO and baseband clocks
   -  Tuning range: 75 MHz to 6000 MHz

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/fmcomms8-bot.png
   :align: right
   :width: 400px

::

     * FMC HPC Compatible interface
     * Complies with VITA 57.1 mechanical dimensions 84mm x 69mm (not full compliance with keep out areas)
   * Platform development environment support includes Industry standard Linux Industrial I/O (IIO) Applications, MATLAB®, Simulink®, and GNU Radio, and streaming interfaces for custom C, C++, python, and C# applications
   * HDL reference designs and drivers to allow zero day development

--------------

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`AD-FMCOMMS8-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/ad-fmcomms8-ebz-designsupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Getting Started
~~~~~~~~~~~~~~~

The following is leveraged directly from the ADRV9009-ZU11EG RF-SOM site.

::

     * Quick Start Guides
       * [[/resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide|FMCOMMS8 Quick Start Guide]]
       * [[/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide|ADRV9009-ZU11EG Quick Start Guide]]
       * [[/resources/tools-software/linux-software/kuiper-linux|Configure a pre-existing SD-Card]]
     * Linux Applications
       * [[/resources/tools-software/linux-software/iio_oscilloscope|IIO Scope]]
         * [[/resources/tools-software/linux-software/adrv9009_osc_main|ADRV9009/ADRV9008 IIO Scope View]]
         * [[/resources/tools-software/linux-software/adrv9009_plugin|ADRV9009/ADRV9008 Control IIO Scope Plugin]]
         * [[/resources/tools-software/linux-software/adrv9009_advanced_plugin|Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin]]
       * [[/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump|FRU EEPROM Utility]]
     * Push custom data into/out of the ADRV9009
       * [[/resources/eval/user-guides/adrv9009/software/basic_iq_datafiles|Basic Data files and formats]]
       * [[/resources/tools-software/linux-software/libiio/clients/matlab_simulink|Stream data into/out of MATLAB]]
   * Design with the ADRV9009
     * [[/resources/eval/user-guides/adrv9009/adrv9009|Understanding the ADRV9009]]
       * [[:adi:`ADRV9009|ADRV9009` Product page]]
       * [[:adi:`en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources`.html|Full Datasheet and chip design package]]
       * [[:adi:`media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2`.4.zip|MATLAB Filter Wizard / Profile Generator for ADRV9009]] 
     * Hardware in the Loop / How to design your own custom BaseBand
       * [[/resources/tools-software/linux-software/gnuradio|GNU Radio]]
       * [[/resources/eval/user-guides/matlab_bsp|Board Support Package for MathWorks Tools]]
     * Design with the ADRV9009-ZU11EG based platform 
       * Linux software
         * [[/resources/tools-software/linux-drivers/iio-transceiver/adrv9009|ADRV9009/ADRV9008 Linux Device Driver]]
           *  [[/resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization|ADRV9009/ADRV9008 Device Driver Customization]]
           *  [[/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks|Customizing the devicetree on the target]]
         * [[/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework|JESD204 (FSM) Interface Linux Kernel Framework]]
         * [[/resources/tools-software/linux-drivers/iio-pll/hmc7044|HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver]]
         * [[/resources/tools-software/linux-drivers/axi-dmac|AXI-DMAC DMA Controller Linux Driver]]
         * [[/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx|JESD204B Transmit Linux Driver]]
           * [[/resources/tools-software/linux-software/jesd_status|JESD204B Status Utility]] 
         * [[/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx|JESD204B Receive Linux Driver]]
           * [[/resources/tools-software/linux-software/jesd_status|JESD204B Status Utility]] 
         * [[/resources/tools-software/linux-drivers/jesd204/axi_adxcvr|ADI JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver]]
           * [[/resources/tools-software/linux-software/jesd_eye_scan|JESD204 Eye Scan]]
         * [[/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl|AXI ADC HDL Linux Driver]]
         * [[/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl|AXI DAC HDL Linux Driver]]
       * [[/resources/eval/user-guides/adrv9009/no-os-setup|ADRV9009/ADRV9008 No-OS System Level Design Setup]]
       * [[/resources/eval/user-guides/adrv9009-zu11eg/hdl|HDL Reference Design]]

Functional Test
~~~~~~~~~~~~~~~

Details on how the AD-FMCOMMS8-EBZ is functionally tested can be found here.

-  :doc:`AD-FMCOMMS8-EBZ Production Test </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz/testing>`
