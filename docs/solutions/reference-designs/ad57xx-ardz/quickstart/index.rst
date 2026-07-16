.. _ad57xx-ardz quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions
on how to do an initial system setup for the AD57xx evaluation
boards (EVAL-AD5780ARDZ, EVAL-AD5781ARDZ, EVAL-AD5791ARDZ) on
various FPGA development boards. In these guides, we will discuss
how to program the bitstream, run a no-OS program or boot a
Linux distribution.

.. toctree::

   CoraZ7-07s <coraz7s>
   DE10-Nano <de10nano>

.. _ad57xx-ardz carriers:

Supported carriers
-------------------------------------------------------------------------------

The AD57xx evaluation boards support precision, single-channel
voltage output DACs with various resolution and range options.
These compact evaluation boards are designed to work with
multiple FPGA development platforms via Arduino shield
connectors.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - AD57xx evaluation boards
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Arduino shield connector
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Arduino shield connector

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - Yes
   - - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - No

Hardware Setup
-------------------------------------------------------------------------------

The AD57xx evaluation boards connect to the Arduino Shield
connector (unless otherwise noted). The carrier setup requires
power, UART (115200), ethernet (Linux), and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

CoraZ7-07s + AD57xx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad57xx_setup_hardware_coraz7s.jpeg
   :align: center
   :width: 600

   CoraZ7-07s + AD57xx hardware setup.

DE10-Nano + AD57xx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ad57xx_setup_hardware_de10nano.jpg
   :align: center
   :width: 600

   DE10-Nano + AD57xx hardware setup.
