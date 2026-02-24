.. _adrv904x quickstart:

Quick start
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-ADRV904x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv904x.html>`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZCU102 <zcu102>

.. _adrv904x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV904x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv904x.html>`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-ADRV9040
     - EVAL-ADRV9044
   - - :xilinx:`ZCU102`
     - FMC HPC1
     - FMC HPC1

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware Setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-ADRV904x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv904x.html>` boards
connects to the HPC1 connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZCU102 + EVAL-ADRV904x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-ADRV904x evaluation board connects to the FMC HPC1 connector on the
ZCU102. Typical hardware setup includes:

- Power supply for ZCU102
- FMC connection between EVAL-ADRV904x and ZCU102 HPC1
- UART connection (115200 baud)
- Ethernet connection for Linux networking
- HDMI connection to monitor (optional)
- SD card with boot files and Linux distribution

For detailed connection information and setup photos, please refer to the
:adi:`ADRV904x Evaluation System User Guide <media/en/technical-documentation/user-guides/eval-adrv904x-ug-2229.pdf>`.
