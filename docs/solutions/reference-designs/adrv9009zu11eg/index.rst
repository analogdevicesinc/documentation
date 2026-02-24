.. _adrv9009zu11eg:

ADRV9009-ZU11EG User Guide
===========================

Introduction
------------

The :adi:`ADRV9009-ZU11EG` is a highly integrated RF System-on-Module
(RF-SOM) based on the Analog Devices :adi:`ADRV9009` and the Xilinx Zynq
UltraScale+ MPSoC (ZU11EG). The RF-SOM is a platform for evaluation and
prototyping. To use the RF-SOM, a carrier board is required. The Analog
Devices ADRV2CRR-FMC carrier board is designed for this purpose.

An additional RF transceiver board (:ref:`AD-FMCOMMS8-EBZ <ad-fmcomms8-ebz>`)
can be fitted to the carrier to expand the system up to 8 Tx and Rx radio
channels.

**The RF-SOM box includes:**

- ADRV9009-ZU11EG RF-SOM
- Heat spreader plate (fitted to the RF-SOM during manufacturing)

**The Carrier box includes:**

- ADRV2CRR-FMC carrier board (needed to evaluate the RF-SOM), SD card, fan
  heatsink, and other accessories to get the user up and running

.. figure:: adrv9009_zu11eg_block_diagram.png
   :align: center

   ADRV9009-ZU11EG RF-SOM high-level block diagram

High-Level Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~

- Two ADRV9009 devices providing:

  - Quad transmitters / Quad receivers
  - Quad input observation receiver for DPD
  - Max Rx BW: 200 MHz
  - Max tunable Tx synthesis BW: 450 MHz
  - Max observation Rx BW: 450 MHz
  - Fully integrated fractional-N RF synthesizers
  - Multi-chip phase synchronization for all RF LO and baseband clocks
  - Tuning range: 75 MHz to 6000 MHz

- Zynq UltraScale+ ZU11EG:

  - Quad-core ARM Cortex-A53 (up to 1.5 GHz)
  - Dual-core Cortex-R5 real-time processors
  - Mali-400 MP2 GPU (up to 667 MHz)
  - PCIe Gen2 x4, 2x USB 3.0, SATA 3.1, DisplayPort, 4x Gigabit Ethernet
  - 2x USB 2.0, 2x SD/SDIO, 2x UART, 2x CAN 2.0B, 2x I2C, 2x SPI, 4x GPIO
  - 653k system logic cells (16 nm FinFET+)

- On-board memory:

  - PS: 4 GB DDR4 (x64) with ECC
  - PL: Two independent banks of 2 GB DDR4 (x32) for RF data
  - 1 Gbit serial flash for image storage
  - Removable SD card

- On-SOM peripherals: Ethernet PHY, USB 2.0 PHY, uSD card holder
- Storage temperature: -40 C to +65 C
- Operating temperature for prototyping with supplied heatsink: +25 C

Supported Devices
-----------------

- :adi:`ADRV9009`

Supported Carriers
------------------

- ADRV2CRR-FMC Carrier Board

Application Development
-----------------------

Multiple ADRV9009-ZU11EG RF-SOMs can be synchronized together, enabling a
complete solution for complex multi-stream applications ensuring end-to-end
deterministic latency. The ADRV9009 transceivers include integrated LO and
phase synchronization. Overall system frequency and phase synchronization is
maintained with a clock tree structure using :adi:`HMC7044` devices, making
it ideal for applications requiring RF phase alignment with a large number of
channels.

The ADRV9009-ZU11EG has extensive I/O capability. Combined with the
ADRV2CRR-FMC carrier board, a variety of high-speed I/O can be evaluated,
including USB 3.0, USB 2.0, PCIe 3.0 x8, QSFP+, SFP+, 1 Gb Ethernet x2,
and CPRI capability.

An additional High Pin Count FMC daughter board
(:ref:`AD-FMCOMMS8-EBZ <ad-fmcomms8-ebz>`) can be plugged into the carrier
board with a further two ADRV9009 transceivers, increasing to a total of
eight Tx and Rx channels. A design can be evaluated and then integrated
seamlessly into a custom carrier for further prototyping or a final product,
greatly accelerating time to market.

Platform development support includes examples of Linux Industrial I/O (IIO)
applications, MATLAB, Simulink, GNU Radio, and streaming interfaces for
custom C, C++, Python, and C# applications.

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

- :git-linux:`drivers/iio/adc/adrv9009.c`

Linux Software References
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Reference
   * - JESD204 (FSM) Framework
     - :git-linux:`drivers/jesd204`
   * - HMC7044 Clock Driver
     - :git-linux:`drivers/iio/frequency/hmc7044.c`
   * - AXI-DMAC DMA Controller
     - :git-linux:`drivers/dma/dma-axi-dmac.c`
   * - AXI ADC HDL Driver
     - :git-linux:`drivers/iio/adc/cf_axi_adc_core.c`
   * - AXI DAC HDL Driver
     - :git-linux:`drivers/iio/dac/cf_axi_dds.c`

More Information
----------------

- :ref:`AD-FMCOMMS8-EBZ User Guide <ad-fmcomms8-ebz>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- `Software Defined Radio for Engineers <https://www.analog.com/en/education/education-library/software-defined-radio-for-engineers.html>`__

.. toctree::
   :hidden:

   hardware
   quickstart
   reference_hdl

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
