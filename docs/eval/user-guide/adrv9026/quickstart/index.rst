.. _adrv9026 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do
an initial system setup for the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`
boards on various FPGA development boards. They will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   ZCU102 <zynqmp>
   VCK190 <versal>

.. _adrv9026 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`, is, by definition a "FPGA
mezzanine card" (FMC), that means it needs a carrier to plug into.
The carriers we support are:

.. list-table::
   :header-rows: 1

   - - Board
     - EVAL-ADRV9026
     - EVAL-ADRV9029
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
   - - :xilinx:`KC705`
     -
     -
   - - :xilinx:`VC707`
     -
     -
   - - :xilinx:`KCU105`
     -
     -
   - - :xilinx:`ZC706`
     -
     -
   - - :xilinx:`VCU118`
     - Yes
     - Yes
   - - :xilinx:`VCK190`
     - Yes
     - Yes
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes

Supported Environments
-------------------------------------------------------------------------------

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
     -
     -
     -
   - - :xilinx:`VCU118`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`VCK190`
     - Yes
     - Yes
     - Yes
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes
     -

Hardware Setup
-------------------------------------------------------------------------------

In most carriers, the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>` boards
connects to the HPC1 connector (unless otherwise noted). The carrier setup
requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZCU102 + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: adrv9026_zcu102_quickstart.jpg
   :width: 800px


VCK190 + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: adrv9026_vck190_quickstart.jpg
   :width: 800px

Unboxing guide
-------------------------------------------------------------------------------

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9026-setup-with-ZCU102-or-ZC706-April2019.pdf>`

