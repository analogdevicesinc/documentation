AD-FMCOMMS8-EBZ
===============

Introduction
------------

The :adi:`AD-FMCOMMS8-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcomms8-ebz.html>` is an integrated RF design containing two Analog Devices :adi:`ADRV9009` wideband transceivers. By connecting to a compatible FPGA development board that supports FMC HPC mechanical connector and JESD204B bus interface it can be used for evaluation and prototyping with upto 4 Transmit and Receive channels that can be synchronised in phase and frequency. Additionally it can be used with the ADRV9009-ZU11EG RF-SOM system. This gives a path to evaluating and prototyping with upto 8 phase and frequency synchronised Transmit and Receive channels for complex multi-stream applications ensuring end-to-end deterministic latency.

The ADRV9009 Transceivers include integrated LO and phase synchronization. Overall system frequency & phase synchronization is maintained with a clock tree structure using ADI high performance low jitter :adi:`HMC7044` device, making it ideal for applications requiring RF phase alignment with a large number of channels.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms8-ebz/fmcomms8-top.png
   :align: right
   :width: 400

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
   :width: 400

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

- Quick Start Guides
  - :doc:`FMCOMMS8 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`
  - :doc:`ADRV9009-ZU11EG Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`
  - :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
- Linux Applications
  - :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
    - :doc:`ADRV9009/ADRV9008 IIO Scope View </wiki-migration/resources/tools-software/linux-software/adrv9009_osc_main>`
    - :doc:`ADRV9009/ADRV9008 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/adrv9009_plugin>`
    - :doc:`Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/adrv9009_advanced_plugin>`
  - :doc:`FRU EEPROM Utility </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`
- Push custom data into/out of the ADRV9009
  - :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/adrv9009/software/basic_iq_datafiles>`
  - :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
   * Design with the ADRV9009
     * :doc:`Understanding the ADRV9009 </wiki-migration/resources/eval/user-guides/adrv9009/adrv9009>`
       * :adi:`ADRV9009 Product page <ADRV9009>`
       * :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
       * :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`
     * Hardware in the Loop / How to design your own custom BaseBand
       * :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
       * :doc:`Board Support Package for MathWorks Tools </wiki-migration/resources/eval/user-guides/matlab_bsp>`
     * Design with the ADRV9009-ZU11EG based platform
       * Linux software
         * :doc:`ADRV9009/ADRV9008 Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
           *  :doc:`ADRV9009/ADRV9008 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`
           *  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`
         * :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         * :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
         * :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
         * :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           * :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`
         * :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           * :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`
         * :doc:`ADI JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           * :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`
         * :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         * :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
       * :doc:`ADRV9009/ADRV9008 No-OS System Level Design Setup </wiki-migration/resources/eval/user-guides/adrv9009/no-os-setup>`
       * :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/hdl>`

Functional Test
~~~~~~~~~~~~~~~

Details on how the AD-FMCOMMS8-EBZ is functionally tested can be found here.

-  :doc:`AD-FMCOMMS8-EBZ Production Test </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz/testing>`
