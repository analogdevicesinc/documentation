.. _admx6001 quickstart:

Quickstart
===============================================================================

The quick start guides provide simple step-by-step instructions on how to do
an initial system setup for the :adi:`ADMX6001-EBZ` board using various
evaluation platforms.

.. toctree::
   :maxdepth: 1

   On VCU118 <vcu118>

.. _admx6001 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`ADMX6001-EBZ` uses an FMC+ HSPC connector; it needs a carrier to
plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Platform
     - Connector
     - Notes
   * - :xilinx:`VCU118`
     - FMC+ HSPC
     - FPGA carrier, Linux software

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Platform
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`VCU118`
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

On the :xilinx:`VCU118`, the :adi:`ADMX6001-EBZ` connects to the **FMC+ HSPC**
connector. The setup requires two independent 12 V power supplies, Ethernet
(for IIO applications), and Micro-USB (UART console).

VCU118 + ADMX6001_EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/vcu118_admx6001_setup.png
   :width: 800
   :align: center
   :alt: ADMX6001_EBZ on VCU118 setup

Go to :ref:`the VCU118 quickstart guide <admx6001 quickstart vcu118>`.
