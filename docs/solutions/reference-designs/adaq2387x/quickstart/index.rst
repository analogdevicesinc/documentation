.. _eval-adaq23875-fmcz quickstart:

Quickstart
===============================================================================

The quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`EVAL-ADAQ23875FMCZ` board on supported FPGA
development boards. In these guides, we will discuss how to program the
bitstream and boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On ZedBoard <zedboard>

.. _eval-adaq23875-fmcz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADAQ23875FMCZ` is an FMC (FPGA Mezzanine Card), meaning it
requires a compatible carrier board. The officially supported carriers are
listed below.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - EVAL-ADAQ23875FMCZ
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported Environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - No

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`EVAL-ADAQ23875FMCZ` connects to the ZedBoard FMC LPC connector. The
carrier setup requires a 12 V power supply, an Ethernet (LAN) connection, and
an analog signal source connected via SMA cable and XLR-to-SMA adapter.

ZedBoard + EVAL-ADAQ23875FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adaq23875x_zed.jpg
