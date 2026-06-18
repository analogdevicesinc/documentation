.. _eval-ad469x-quickstart:

Quick start guide
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`EVAL-AD4692-ARDZ` and :adi:`EVAL-AD4696FMCZ`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zed>
   On CoraZ7-07S <coraz7s>
   On DE10-Nano <de10nano>

.. _eval-ad469x-carriers:

Supported carriers
-------------------------------------------------------------------------------

The carriers we support are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - Form Factor
     - Board
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - FMC LPC
     - EVAL-AD4696FMCZ
   * - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Arduino Uno Shield
     - EVAL-AD4692-ARDZ
   * - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Arduino Uno Shield
     - EVAL-AD4692-ARDZ

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - Yes
     - Yes
     - Yes
   * - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - No
   * - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

The EVAL-AD4696FMCZ board connects to the FMC LPC connector, while the
EVAL-AD4692-ARDZ connects to the Arduino Uno Shield connector. The carrier
setup requires power, UART (115200), Ethernet (Linux), and/or JTAG (no-OS)
connections.

ZedBoard + EVAL-AD4696FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad4696_zed_setup_top.jpg
   :width: 900

Go to
:ref:`the setup guide <eval-ad469x-quickstart-zedboard>`.

CoraZ7-07S + EVAL-AD4692ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad4692_coraz7s_setup_top.jpg
   :width: 900

Go to
:ref:`the setup guide <eval-ad469x-quickstart-coraz7s>`.

DE10-Nano + EVAL-AD4692ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad4692_de10nano_setup_top.jpg
   :width: 900

Go to
:ref:`the setup guide <eval-ad469x-quickstart-de10nano>`.
