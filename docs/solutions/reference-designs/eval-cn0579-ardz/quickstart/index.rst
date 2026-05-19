.. _eval-cn0579-ardz quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-CN0579-ARDZ` evaluation
board on the supported FPGA development board. This guide covers how to
program the bitstream and boot a Linux distribution.

.. toctree::

   DE10-Nano <de10-nano>
   Cora Z7 <coraz7>

.. _eval-cn0579-ardz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0579-ARDZ` connects to the FPGA carrier via the
Arduino headers. No additional adapter is required.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-CN0579-ARDZ`
   * - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Arduino headers
   * - `Cora Z7 <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`__
     - Arduino headers

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - ---
   * - `Cora Z7 <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - ---

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0579-ARDZ` connects to the carrier board via the
Arduino headers.

Both carriers share the same Arduino form factor, so the
:adi:`EVAL-CN0579-ARDZ` mounts identically on the De10-Nano and Cora Z7. The
only difference is that the Cora Z7 uses a Micro-USB cable while the DE10-Nano
uses a Mini-USB cable for the UART connection.

DE10-Nano + EVAL-CN0579-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/de10_nano_setup_top.jpeg
   :alt: DE10-Nano with EVAL-CN0579-ARDZ mounted (top view)
   :width: 800

   DE10-Nano with EVAL-CN0579-ARDZ mounted (top view).

.. figure:: ../images/de10_nano_setup_side.jpeg
   :alt: DE10-Nano with EVAL-CN0579-ARDZ mounted (side view)
   :width: 800

   DE10-Nano with EVAL-CN0579-ARDZ mounted (side view).

Cora Z7 + EVAL-CN0579-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/cora_setup_top.jpeg
   :alt: Cora Z7 with EVAL-CN0579-ARDZ mounted (top view)
   :width: 800

   Cora Z7 with EVAL-CN0579-ARDZ mounted (top view).

.. figure:: ../images/cora_setup_side.jpeg
   :alt: Cora Z7 with EVAL-CN0579-ARDZ mounted (side view)
   :width: 800

   Cora Z7 with EVAL-CN0579-ARDZ mounted (side view).
