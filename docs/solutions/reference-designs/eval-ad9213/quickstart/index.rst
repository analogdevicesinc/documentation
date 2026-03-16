.. _ad9213 evb quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9213` evaluation
board on the supported FPGA development board. This guide covers how to
program the bitstream and boot a Linux distribution over JTAG.

.. toctree::

   On VCU118 + EVAL-AD9213 <vcu118>
   On ADS8-V1EBZ + EVAL-AD9213/EVAL-AD9217 <ads8-v1ebz_ad9213_ad9217>
   On ADS8-V1EBZ + AD9213-10GEBZ-B <ads8-v1ebz_ad9213-10gebz-b>

.. _ad9213 evb carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9213` connects to the FPGA carrier via an
FMC+ connector. Because the evaluation board does not natively expose
the JTAG chain, a ZX180V-HSPC breakout adapter is required.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD9213`
     - :adi:`EVAL-AD9217`
   * - :xilinx:`VCU118`
     - FMC+
     - ---
   * - :adi:`ADS8-V1EBZ`
     - FMC+
     - FMC+

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`VCU118`
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9213` connects to the AMD Xilinx
:xilinx:`VCU118` via the FMC+ breakout adapter. The carrier setup requires a
power supply, UART (115200 baud), and JTAG connections via Micro-USB cables.

VCU118 + EVAL-AD9213
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad9213_vcu118_setup.jpeg
   :alt: VCU118 FPGA board with EVAL-AD9213 mounted via FMC+ breakout adapter
   :width: 800

   VCU118 with EVAL-AD9213 hardware setup

ADS8-V1EBZ + EVAL-AD9213/EVAL-AD9217
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad9213_ads8v1_setup.jpeg
   :alt: ADS8-V1EBZ capture board with AD9213/9217 evaluation board connected
   :width: 1200

   ADS8-V1EBZ with EVAL-AD9213/EVAL-AD9217 hardware setup


ADS8-V1EBZ + AD9213-10GEBZ-B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad9213-b_quick_start_diagram.jpeg
   :alt: ADS8-V1EBZ capture board with AD9213-10GEBZ-B evaluation board connected
   :width: 1200

   ADS8-V1EBZ with AD9213-10GEBZ-B hardware setup

Go to :ref:`the quick start guide <ad9213 evb quickstart vcu118>`.
