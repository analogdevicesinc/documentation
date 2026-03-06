ADRV9009-ZU11EG RF System-on-Module
===================================

Introduction
------------

The :adi:`ADRV9009-ZU11EG` :adi:`Export Info <ADRV9009-ZU11EG>` is a highly integrated RF System-On-Module(RF-SOM) based on the Analog Devices :adi:`ADRV9009` and Xilinx `Zynq UltraScale+ MPSoC <https://www.xilinx.com//products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`__. The RF-SOM is a platform for evaluation and prototyping. To use the RF-SOM a carrier board is required. The Analog Devices ADRV2CRR-FMC Carrier board is designed for this purpose. An additional RF Transceiver board can also be fitted to the carrier to further expand the system up to 8 Tx and Rx radio channels.

**The RF-SOM box includes:**

-  ADRV9009-ZU11EG RF-SOM
-  Heat spreader plate(fitted to the RF-SOM during manufacturing)

**The Carrier box includes:**

-  ADRV2CRR-FMC carrier board(needed to evaluate the RF-SOM), SD-Card, Fan Heatsink and other accessories to get the user up and running
-  Full details found in the Carrier section

--------------

ADRV9009-ZU11EG Highlevel specification
---------------------------------------

-  Two ADRV9009 devices, providing (in total):

   -  Quad transmitters
   -  Quad receivers
   -  Quad input Observation Receiver for DPD
   -  Max Rx BW: 200 MHz
   -  Max Tunable Tx synthesis BW: 450 MHz
   -  Max Observation Rx BW: 450MHz
   -  Fully integrated fractional-N RF synthesizers
   -  Multi-chip phase synchronization for all RF LO and baseband clocks
   -  Tuning range: 75 MHz to 6000 MHz

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg.png
   :align: right
   :width: 200px

-  Zynq UltraScale+ ZU11EG

   -  Quad-core ARM® Cortex-A53 platform running up to 1.5GHz

      -  L1 Cache 32KB I / D per core, L2 Cache 1MB, on-chip Memory 256KB

   -  Dual-core Cortex-R5 real-time processors

      -  L1 Cache 32KB I / D per core, Tightly Coupled Memory 128KB per core

   -  Mali-400 MP2 graphics processing unit up to 667 MHz
   -  PCIe® Gen2 x4, 2x USB3.0, SATA 3.1, DisplayPort, 4x Tri-mode Gigabit Ethernet
   -  2xUSB 2.0, 2x SD/SDIO, 2x UART, 2x CAN 2.0B, 2x I2C, 2x SPI, 4x 32b GPIO
   -  16nm FinFET+ programmable logic

      -  653k System Logic Cells

-  On Board Memory:

   -  Processing System (Dedicated for ARM Cores) : 4 GByte DDR4(x64) (with ECC)
   -  Programmable Logic (Dedicated for RF Data) : Two independent banks of 2 GByte DDR4(x32)
   -  1Gbit serial flash for image storage
   -  removable SD-Card for secure file storage

-  On SOM Peripherals

   -  Ethernet Phy
   -  USB 2.0 Phy
   -  12V supply via FMC connectors
   -  uSD Card holder

-  Storage and operating temperature

   -  Storage temperature range supported is -40⁰C to +65⁰C
   -  Operating temperature for prototyping with the heatsink supplied is +25C. For specific use cases thermal analysis is required to cover varying environmental conditions and required performance levels.

--------------

Hardware Design Details
-----------------------

.. important::

   For Clock Distribution Synchronization some passive components need to be changed on the :doc:`ADRV2CRR-FMC </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>` Carrier Board.

   
   Rev C:
   
   -  Replace C18, C19, C236, C240 with 0 Ohm resistors
   -  Replace C289, C290 with 0 Ohm resistors
   -  Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111
   
   Rev C.1:
   
   -  Replace C289, C290 with 0 Ohm resistors
   -  Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111
   


-  :doc:`ADRV9009-ZU11EG </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/hardware>`
-  Included are further details on the RF-SOM schematics, BOM, system clocking tree, mechanical specs, power tree, electrical interface.

-  :doc:`ADRV2CRR-FMC </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>`
-  Included are schematics, BOM, mechanical specs, high level system view.

-  :doc:`AD-FMCOMMS8-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz>`
-  Included are schematics, BOM, mechanical specs, high level system view, Start Guide with link the the required software to get up and running.

--------------

Application Development
-----------------------

Multiple ADRV9009-ZU11EG’s can be synchronized together enabling a complete solution for complex multi-stream applications ensuring end-to-end deterministic latency. The ADRV9009 Transceivers include integrated LO and phase synchronization. Overall system frequency & phase synchronization is maintained with a clock tree structure using ADI high performance low jitter :adi:`HMC7044` devices, making it ideal for applications requiring RF phase alignment with a large number of channels.

The ADRV9009-ZU11EG has extensive I/O capability. Combined with the ADRV2CRR-FMC evaluation carrier board a variety of high speed I/O can be evaluated, including USB3, USB2, PCIe 3.0 x8, QSFP+, SFP+, 1Gb Ethernet x2, and CPRI capability. Please review the I/O functionality reference table provided in the :doc:`ADRV2CRR-FMC </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>` homepage for more details on the functionality provided.

An additional High Pin Count FMC Daughter Board (AD-FMCOMMS8-EBZ) can be plugged into the carrier board with a further two ADRV9009 Transceivers increasing to a total of Eight Tx and Rx channels. A design can easily be evaluated and then integrated seamlessly into a custom carrier for further prototyping, or a final product greatly accelerating time to market.

Platform development support includes examples of Linux Industrial I/O (IIO) Applications, MATLAB®, Simulink®, GNU Radio, and streaming interfaces for custom C, C++, python, and C# applications. HDL reference designs and drivers will be provided to help users get up and running faster. Due to varying implementation options for the various I/O interfaces different levels of functionality will be provided for each one, further details will be available in the applications section.

--------------

System setup & evaluation
-------------------------

The ADRV9009-ZU11EG can be booted from the onboard SD card slot or the SD card slot on the ADRV2CRR-FMC carrier board. An SD card containing a bootable image ships in the ADRV2CRR-FMC carrier kit.

Users should check that they have the appropriate Vivado license in place to be able to use and build the reference HDL code provided for the Ultrascale+ MPSOC in the system.

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :ez:`ask <fpga>`.

-  Getting started with the ADRV9009-ZU11EG

   -  :doc:`ADRV9009-ZU11EG Quick Start Guide </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`

      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   -  :doc:`Performance Characteristics 'Pending Update' </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/hardware/performance>`
   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

         -  :doc:`ADRV9009/ADRV9008 IIO Scope View </wiki-migration/resources/tools-software/linux-software/adrv9009_osc_main>`
         -  :doc:`ADRV9009/ADRV9008 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/adrv9009_plugin>`
         -  :doc:`Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/adrv9009_advanced_plugin>`

      -  :doc:`FRU EEPROM Utility </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

   -  Push custom data into/out of the ADRV9009

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/adrv9009/software/basic_iq_datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/transceiver-toolbox>`

-  Design with the ADRV9009

   -  :doc:`Understanding the ADRV9009 </wiki-migration/resources/eval/user-guides/adrv9009/adrv9009>`

      -  :adi:`ADRV9009 Product page <ADRV9009>`
      -  :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      -  :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`Board Support Package for MathWorks Tools </wiki-migration/resources/tools-software/transceiver-toolbox>`

   -  Design with the ADRV9009-ZU11EG based platform

      -  Linux software

         -  :doc:`ADRV9009/ADRV9008 Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`

            -   :doc:`ADRV9009/ADRV9008 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`
            -   :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         -  :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         -  :doc:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/hmc7044>`
         -  :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
         -  :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            -  :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`

         -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      -  :doc:`ADRV9009/ADRV9008 No-OS System Level Design Setup </wiki-migration/resources/eval/user-guides/adrv9009/no-os-setup>`
      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/hdl>`
      -  :doc:`ADRV9009-ZU11EG Multi-SOM Synchronization </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/syncronization>`

--------------

Reference Material
------------------

|image1| :adi:`Software Defined Radio for Engineers <en/education/education-library/software-defined-radio-for-engineers.html>`

:doc:`Additional Documentation about SDR Signal Chains - The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`

--------------

Functional Test
---------------

Details on how the ADRV9009-ZU11EG is functionally tested can be found here.

-  :doc:`ADRV2CRR-FMC Production Test </wiki-migration/resources/eval/user-guides/adrv2crr-fmc/testing>`
-  :doc:`ADRV9009-ZU11EG Production Test </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/testing>`

--------------

Help and Support
----------------

For questions and more information please contact us on the Analog Devices Engineer Zone.

.. hint::

   :ez:`fpga`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009_zu11eg/sdr_book.png
   :width: 200px
