.. _adrv9009 quickstart:

Quickstart
==========

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

.. toctree::

   ZCU102 <zynqmp>

.. _adrv9009 carriers:

Supported carriers
------------------

The :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` is, by definition a "FPGA
mezzanine card" (FMC), that means it needs a carrier to plug into.
The carriers we support are:

.. list-table::
   :header-rows: 1

   - - Board
     - ADRV9009-W/PCBZ
     - ADRV9008-1W/PCBZ
     - ADRV9008-2W/PCBZ
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`KC705`
     -
     -
     -
   - - :xilinx:`VC707`
     -
     -
     -
   - - :xilinx:`KCU105`
     -
     -
     -
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - WIP
     - WIP

Supported Environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - WIP
   - - :xilinx:`KC705`
     -
     -
     -
   - - :xilinx:`VC707`
     -
     -
     -
   - - :xilinx:`KCU105`
     -
     -
     -
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     -
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes
     -

Hardware Setup
--------------

In most carriers, the :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` boards connects to the HPC1
connector (unless otherwise noted). The carrier setup requires power, UART
(115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections.
A few typical setups are shown below.

ZCU102 + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~

.. image:: adrv9009_zcu102_quickstart.png

Unboxing guide
~~~~~~~~~~~~~~

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`
