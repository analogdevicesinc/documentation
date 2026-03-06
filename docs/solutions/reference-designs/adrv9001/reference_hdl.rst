.. _adrv9001-hdl:

ADRV9001/ADRV9002 HDL Reference Design
========================================

.. note::

   The latest HDL documentation can be found at
   `projects/adrv9001/index.rst <https://analogdevicesinc.github.io/hdl/projects/adrv9001/index.html>`__.

This design allows controlling, receiving and transmitting sample streams
from/to an ADRV9001/ADRV9002 device through two independent source synchronous
interfaces. Supports both CMOS and LVDS interface, but not at the same time.
The selection of the I/O standard must be done with a parameter during build.

The design supports SDR or DDR modes in CMOS mode with one or four lanes, and
in LVDS mode one or two lane mode. This is runtime selectable. The complete
list of supported modes can be consulted in the
:doc:`AXI_ADRV9002 Interface Core <axi_adrv9002>` documentation.

Source Code
-----------

- :git-hdl:`projects/adrv9001`

Build Instructions
------------------

For an LVDS interface the project must be built with:

.. code-block:: bash

   make CMOS_LVDS_N=0

For a CMOS interface the project must be built with:

.. code-block:: bash

   make CMOS_LVDS_N=1

Block Design
------------

The design has two receive paths and two transmit paths. One of the receive
paths (Rx12) has four channels and the other (Rx2) two channels. These can
work independently having each two active channels, or just the Rx12 path
having four active channels, while Rx2 is disabled. The same applies to the
transmit path but in the other direction.

When only the Rx12 path is active with four channels mode the core will take
ownership of both source synchronous interfaces. The requirement in this case
is that both interfaces run at the same rate.

.. figure:: adrv9002_bd.png
   :align: center

   ADRV9001/ADRV9002 block diagram

FMC Locations
-------------

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` — HPC0 (FMC0)
- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` — LPC FMC (CMOS only)
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ — FMC (CMOS only)
- :intel:`Arria 10 SoC
  <content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>` — FMCA (CMOS only)

DAC Interface
-------------

- Has DDS (dual tone generation)
- Has PRBS generation

ADC Interface
-------------

- Has PN checking
- Has data formatter
- Has programmable input delay

Register Map
------------

.. list-table::
   :header-rows: 1

   * - Address
     - IP
   * - 0x44A0_0000
     - :doc:`axi_adrv9001 <axi_adrv9002>`
   * - 0x44A3_0000
     - axi_adrv9001_rx1_dma
   * - 0x44A4_0000
     - axi_adrv9001_rx2_dma
   * - 0x44A5_0000
     - axi_adrv9001_tx1_dma
   * - 0x44A6_0000
     - axi_adrv9001_tx2_dma

ZC706 VADJ Protection
~~~~~~~~~~~~~~~~~~~~~~

For ZC706, after bitfile loading all FPGA outputs are high-Z.

- Software should wait until the VADJ is set to 1.8V.
- Set **GPIO[52]** to enable the output lines.
- Pull out of reset the RX and TX channels (ADC/DAC common REG_RSTN register,
  RSTN bit).

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
