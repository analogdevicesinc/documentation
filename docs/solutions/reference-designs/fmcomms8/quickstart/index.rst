.. _fmcomms8 quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on
how to do an initial system setup for the
:adi:`EVAL-AD-FMCOMMS8-EBZ` board on various FPGA development boards. In these
guides, we will discuss how to program the bitstream and boot a Linux
distribution.

.. toctree::
   :hidden:

   On ZCU102 <zcu102>
   On Arria10 SoC <a10soc>

.. _fmcomms8 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS8-EBZ` is, by definition, a "FPGA mezzanine card"
(FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - Eval board
     - FMC port
   * - ADRV9009-ZU11EG + ADRV2CRR-FMC
     - AD-FMCOMMS8-EBZ
     - FMC HPC
   * - :xilinx:`ZCU102`
     - AD-FMCOMMS8-EBZ
     - FMC HPC0
   * - :intel:`Arria10 SoC Development Kit <content/www/us/en/products/details/fpga/arria/10.html>`
     - AD-FMCOMMS8-EBZ
     - FMC HPC (rework required)

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - ADRV9009-ZU11EG + ADRV2CRR-FMC
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes
   * - :intel:`Arria10 SoC Development Kit <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD-FMCOMMS8-EBZ` connects to the HPC connector
(unless otherwise noted). The carrier setup requires power, UART
(115200), Ethernet, optionally DisplayPort connections and/or JTAG connections.
A few typical setups are shown below.

ADRV9009-ZU11EG + ADRV2CRR-FMC + AD-FMCOMMS8-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. image:: ../images/fmcomms8_adrv9009zu11eg_adrv2crr.jpeg
..    :width: 800

.. Go to :ref:`the setup guide <adrv9009-zu11eg fmcomms8-quick-start>`.

ZCU102 + AD-FMCOMMS8-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms8_zcu102.jpg
   :width: 800

Go to :ref:`the setup guide <fmcomms8 quickstart zcu102>`.

Arria10 SoC + AD-FMCOMMS8-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/fmcomms8_a10soc.jpeg
   :width: 800

Go to :ref:`the setup guide <fmcomms8 quickstart a10soc>`.
