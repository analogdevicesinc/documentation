.. _adaq8092 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-ADAQ8092` board on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZED <zed>
   On ZED with ACE Evaluation <ace_zed>

.. _adaq8092 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADAQ8092` is, by definition a "FPGA mezzanine card" (FMC);
that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-ADAQ8092
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - EVAL-ADAQ8092
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-ADAQ8092` board connects to the FMC LPC
connector (unless otherwise noted). The carrier setup requires power, UART
(115200), Ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections. A few typical setups are shown below.

ZED + EVAL-ADAQ8092
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adaq8092_zed_setup.jpg
   :width: 800

Go to :ref:`the setup guide <adaq8092 quickstart zed>`.