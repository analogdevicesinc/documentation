.. _adrv9009_zu11eg:

ADRV9009-ZU11EG RF System-on-Module
===================================

.. image:: ./images/adrv9009.png
   :align: left
   :width: 150

Overview
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

Features:

- Quad transmitters
- Quad receivers
- Quad input Observation Receiver for DPD
- Max Rx BW: 200 MHz
- Max Tunable Tx synthesis BW: 450 MHz
- Max Observation Rx BW: 450MHz
- Fully integrated fractional-N RF synthesizers
- Multi-chip phase synchronization for all RF LO and baseband clocks
- Tuning range: 75 MHz to 6000 MHz

Applications:

- 3G, 4G, and 5G TDD macrocell base stations
- TDD active antenna systems
- Massive multiple input, multiple output (MIMO)
- Phased array radar
- Electronic warfare
- Military communications
- Portable test equipment

.. image:: ./images/adrv9009-zu11eg.png
   :align: center
   :width: 600px

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:ref:`ask <help-and-support>`.

Table of Contents
-----------------

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

Warning
-------------------------------------------------------------------------------

.. esd-warning::
