.. _eval-cn0540-ardz quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do
an initial system setup for the :adi:`EVAL-CN0540-ARDZ` board on various FPGA
development boards. They will discuss how to program the bitstream, run a no-OS
program or boot a Linux distribution.

.. toctree::

   CoraZ7-07s <coraz7s>
   DE10-Nano <de10nano>

.. _eval-cn0540-ardz carriers:

Supported carriers
-------------------------------------------------------------------------------

The carriers we support are:

- `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__ on Arduino shield connector
- :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>` on Arduino shield connector

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - Yes
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - Yes

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0540-ARDZ` board connects to the Arduino
Shield connector (unless otherwise noted). The carrier setup requires power,
UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

CoraZ7-07s + EVAL-CN0540-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/cn0540_cora.jpg
   :align: center
   :width: 500

DE10-Nano + EVAL-CN0540-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/cn0540_de10nano.jpg
   :align: center
   :width: 500
