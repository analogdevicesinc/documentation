.. _adrv9009_zu11eg:

ADRV9009-ZU11EG RF System-on-Module
===================================

Introduction
------------

The :adi:`ADRV9009-ZU11EG` is a highly integrated RF System-On-Module (RF-SOM)
based on the Analog Devices :adi:`ADRV9009` and Xilinx
`Zynq UltraScale+ MPSoC <https://www.xilinx.com/products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`__.
The RF-SOM is a platform for evaluation and prototyping. To use the RF-SOM a
carrier board is required. The Analog Devices ADRV2CRR-FMC Carrier board is
designed for this purpose. An additional RF Transceiver board can also be
fitted to the carrier to further expand the system up to 8 Tx and Rx radio
channels.

**The RF-SOM box includes:**

- ADRV9009-ZU11EG RF-SOM
- Heat spreader plate (fitted to the RF-SOM during manufacturing)

**The Carrier box includes:**

- ADRV2CRR-FMC carrier board, SD-Card, Fan Heatsink and other accessories
- Full details found in the Carrier section

ADRV9009-ZU11EG High-Level Specification
-----------------------------------------

- Two ADRV9009 devices, providing (in total):

   - Quad transmitters
   - Quad receivers
   - Quad input Observation Receiver for DPD
   - Max Rx BW: 200 MHz
   - Max Tunable Tx synthesis BW: 450 MHz
   - Max Observation Rx BW: 450MHz
   - Fully integrated fractional-N RF synthesizers
   - Multi-chip phase synchronization for all RF LO and baseband clocks
   - Tuning range: 75 MHz to 6000 MHz

.. image:: ./images/adrv9009-zu11eg.png
   :align: right
   :width: 200

- Zynq UltraScale+ ZU11EG:

   - Quad-core ARM® Cortex-A53 platform running up to 1.5GHz
   - L1 Cache 32KB I / D per core, L2 Cache 1MB, on-chip Memory 256KB
   - Dual-core Cortex-R5 real-time processors
   - L1 Cache 32KB I / D per core, Tightly Coupled Memory 128KB per core
   - Mali-400 MP2 graphics processing unit up to 667 MHz
   - PCIe® Gen2 x4, 2x USB3.0, SATA 3.1, DisplayPort, 4x Tri-mode Gigabit
     Ethernet
   - 2xUSB 2.0, 2x SD/SDIO, 2x UART, 2x CAN 2.0B, 2x I2C, 2x SPI, 4x 32b GPIO
   - 16nm FinFET+ programmable logic
   - 653k System Logic Cells

- On Board Memory:

   - Processing System (Dedicated for ARM Cores) : 4 GByte DDR4(x64) (with ECC)
   - Programmable Logic (Dedicated for RF Data) : Two independent banks of 2
     GByte DDR4(x32)
   - 1Gbit serial flash for image storage
   - removable SD-Card for secure file storage

- On SOM Peripherals:

   - Ethernet Phy
   - USB 2.0 Phy
   - 12V supply via FMC connectors
   - uSD Card holder

- Storage & Operating Temperature:

   - Storage temperature range supported is -40⁰C to +65⁰C
   - Operating temperature for prototyping with the heatsink supplied is +25C.
     For specific use cases thermal analysis is required to cover varying
     environmental conditions and required performance levels.

Hardware Design Details
-----------------------

.. warning::

   For Clock Distribution Synchronization, some passive components must be
   replaced on the :dokuwiki:`ADRV2CRR-FMC Carrier Board </resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>`.

   **Rev C:**

      - Replace C18, C19, C236, C240 with 0 Ohm resistors
      - Replace C289, C290 with 0 Ohm resistors
      - Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111

   **Rev C.1:**

      - Replace C289, C290 with 0 Ohm resistors
      - Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111

Additional hardware documentation:

- :dokuwiki:`ADRV9009-ZU11EG <resources/eval/user-guides/adrv9009-zu11eg/hardware>`
- Included are further details on the RF-SOM schematics, BOM, system clocking
  tree, mechanical specs, power tree, electrical interface.

- :dokuwiki:`ADRV2CRR-FMC <resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>`
- Included are schematics, BOM, mechanical specs, high level system view.

- :dokuwiki:`AD-FMCOMMS8-EBZ <resources/eval/user-guides/ad-fmcomms8-ebz>`
- Included are schematics, BOM, mechanical specs, high level system view, Start
  Guide with link the the required software to get up and running.

Application Development
-----------------------

Multiple :adi:`ADRV9009-ZU11EG`s can be synchronized together enabling a
complete solution for complex multi-stream applications ensuring end-to-end
deterministic latency. The :adi:`ADRV9009` Transceivers include integrated LO
and phase synchronization. Overall system frequency & phase synchronization is
maintained with a clock tree structure using ADI high performance low jitter
:adi:`HMC7044` devices, making it ideal for applications requiring RF phase
alignment with a large number of channels.

The :adi:`ADRV9009-ZU11EG` has extensive I/O capability. Combined with the
:adi:`ADRV2CRR-FMC` evaluation carrier board a variety of high speed I/O can be
evaluated, including USB3, USB2, PCIe 3.0 x8, QSFP+, SFP+, 1Gb Ethernet x2, and
CPRI capability. Please review the I/O functionality reference table provided
in the :dokuwiki:`ADRV2CRR-FMC <resources/eval/user-guides/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>`
homepage for more details on the functionality provided.

An additional High Pin Count FMC Daughter Board (:adi:`AD-FMCOMMS8-EBZ`) can be
plugged into the carrier board with a further two :adi:`ADRV9009` Transceivers
increasing to a total of Eight Tx and Rx channels. A design can easily be
evaluated and then integrated seamlessly into a custom carrier for further
prototyping, or a final product greatly accelerating time to market.

Platform development support includes examples of Linux Industrial I/O (IIO)
Applications, MATLAB®, Simulink®, GNU Radio, and streaming interfaces for
custom C, C++, python, and C# applications. HDL reference designs and drivers
will be provided to help users get up and running faster. Due to varying
implementation options for the various I/O interfaces different levels of
functionality will be provided for each one, further details will be available
in the applications section.

System Setup & Evaluation
-------------------------

The :adi:`ADRV9009-ZU11EG` can be booted from the onboard SD card slot or the
SD card slot on the :adi:`ADRV2CRR-FMC` carrier board. An SD card containing
a bootable image ships in the ADRV2CRR-FMC carrier kit.

Users should check that they have the appropriate Vivado license in place to be
able to use and build the reference HDL code provided for the Ultrascale+ MPSOC
in the system.

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:ref:`ask <help-and-support>`.

#. Getting started with the ADRV9009-ZU11EG

   #. :ref:`ADRV9009-ZU11EG User Guide <adrv9009-zu11eg user-guide>`
   #. :ref:`What you need to get started <adrv9009-zu11eg prerequisites>`
   #. :ref:`ADRV9009-ZU11EG Quick Start Guide <adrv9009-zu11eg quickstart>`

      #. :dokuwiki:`Configure a pre-existing SD-Card <resources/tools-software/linux-software/kuiper-linux>`
      #. :dokuwiki:`Update the old card you received with your hardware <resources/tools-software/linux-software/kuiper-linux>`

      .. The links above are the same on Wiki. Why? TODO

   #. :dokuwiki:`Performance Characteristics 'Pending Update' </resources/eval/user-guides/adrv9009-zu11eg/hardware/performance>`
   #. Linux Applications

      #. :ref:`iio-oscilloscope`

         #. :dokuwiki:`ADRV9009/ADRV9008 IIO Scope View <resources/tools-software/linux-software/adrv9009_osc_main>`
         #. :dokuwiki:`ADRV9009/ADRV9008 Control IIO Scope Plugin <resources/tools-software/linux-software/adrv9009_plugin>`
         #. :dokuwiki:`Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin <resources/tools-software/linux-software/adrv9009_advanced_plugin>`

   #. :dokuwiki:`FRU EEPROM Utility <resources/tools-software/linux-software/fru_dump>`
   #. Push custom data into/out of the ADRV9009

      #. :dokuwiki:`Basic Data files and formats <resources/eval/user-guides/adrv9009/software/basic_iq_datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/transceiver-toolbox>`

   #. Design with the ADRV9009

      #. Understanding the ADRV9009

         #. :adi:`ADRV9009` Product page
         #. `Full Datasheet and chip design package <https://www.analog.com/en/lp/001/integrated-rf-agile-transceiver-design-resources.html>`__
         #. `MATLAB Filter Wizard / Profile Generator for ADRV9009 <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`__

      #. Hardware in the Loop / How to design your own custom BaseBand

         #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
         #. :dokuwiki:`Board Support Package for MathWorks Tools <resources/tools-software/transceiver-toolbox>`

      #. Design with the ADRV9009-ZU11EG based platform

         #. Linux software

            #. :dokuwiki:`ADRV9009/ADRV9008 Linux Device Driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`

               #. :dokuwiki:`ADRV9009/ADRV9008 Device Driver Customization <resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`
               #. :dokuwiki:`Customizing the devicetree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

            #. :dokuwiki:`JESD204 (FSM) Interface Linux Kernel Framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
            #. :dokuwiki:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <resources/tools-software/linux-drivers/iio-pll/hmc7044>`
            #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
            #. :dokuwiki:`JESD204B Transmit Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

               #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

            #. :dokuwiki:`JESD204B Receive Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

               #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

            #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

               #. :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

            #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
            #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

         #. :dokuwiki:`ADRV9009/ADRV9008 No-OS System Level Design Setup <resources/eval/user-guides/adrv9009/no-os-setup>`
         #. :external+hdl:ref:`HDL Reference Design <adrv9009zu11eg>`
         #. :dokuwiki:`ADRV9009-ZU11EG Multi-SOM Synchronization <resources/eval/user-guides/adrv9009-zu11eg/syncronization>`

Reference Material
------------------

.. image:: ./images/sdr_book.png
   :align: right
   :width: 200

- `Software Defined Radio for Engineers <https://www.analog.com/en/education/education-library/software-defined-radio-for-engineers.html>`__
- :dokuwiki:`Additional SDR Maths Documentation <resources/eval/user-guides/ad-fmcomms1-ebz/mathh>`

Functional Test
---------------

Details on functional testing for the ADRV9009-ZU11EG:

- :dokuwiki:`ADRV2CRR-FMC Production Test <resources/eval/user-guides/adrv2crr-fmc/testing>`
- :dokuwiki:`ADRV9009-ZU11EG Production Test <resources/eval/user-guides/adrv9009-zu11eg/testing>`

Pre-requisites and quickstart
-------------------------------------------------------------------------------

.. toctree::
   :caption: The prerequisites and quickstart guides are provided at:
   :titlesonly:
   :maxdepth: 1

   user-guide
   prerequisites
   quickstart/index

.. _adrv9009-zu11eg block-diagram:

Functional Block Diagram
-------------------------------------------------------------------------------

.. image:: ./images/adrv9009_blockdiagram.png
   :width: 600

Help and Support
----------------

:ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
