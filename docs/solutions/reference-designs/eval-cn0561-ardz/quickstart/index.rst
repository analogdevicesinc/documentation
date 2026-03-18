.. _eval-cn0561-ardz quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`CN0561 Circuit Evaluation Board (EVAL-
CN0561-ARDZ) <CN0561>` boards on various FPGA development boards. In these
guides, we will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

.. toctree::

   Zedboard <zed>
   CoraZ7-07s <coraz7s>
   DE10-Nano <de10nano>
   Nucleo-H563ZI <nucleo-h563zi>

.. _eval-cn0561-ardz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0561 <CN0561>`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-CN0561-ARDZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
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
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
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

The :adi:`CN0561` board connects to the Arduino
Shield connector (unless otherwise noted). The carrier setup requires power,
UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

ZedBoard + EVAL-CN0561-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/cn0561_setup_hardware_zed.jpeg
   :align: center
   :width: 500

   ZedBoard + EVAL-CN0561-ARDZ hardware setup.

CoraZ7-07s + EVAL-CN0561-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/cn0561_setup_hardware_coraz7s.jpeg
   :align: center
   :width: 500

   CoraZ7-07s + EVAL-CN0561-ARDZ hardware setup.

DE10-Nano + EVAL-CN0561-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/cn0561_setup_hardware_de10nano.jpg
   :align: center
   :width: 500

   DE10-Nano + EVAL-CN0561-ARDZ hardware setup.
