.. _adrv904x quickstart:

Quick start
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`EVAL-ADRV904x` boards on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZCU102 <zcu102>

.. _adrv904x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV904x`, is, by definition a "FPGA mezzanine card" (FMC); that
means it needs a carrier to plug into.

The carriers we support are listed below:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-ADRV9040
     - EVAL-ADRV9044
   - - :xilinx:`ZCU102`
     - FMC HPC0 port with FMC extender standard SAMTEC
     - FMC HPC0 port with FMC extender standard SAMTEC

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

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-ADRV904X` boards connects to the HPC0 connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few
typical setups are shown below.

ZCU102 + EVALUATION BOARD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv904x-linux-setup.png
   :width: 800

Go to the :ref:`ZCU102 quickstart guide <adrv904x quickstart zcu102>`.
