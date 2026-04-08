.. _eval-cn0577-fmcz quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`EVAL-CN0577-FMCZ <CN0577>` board on various
FPGA development boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They cover
bitstream programming and Linux boot.

.. toctree::

   On ZedBoard <zed>

.. _eval-cn0577-fmcz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0577-FMCZ <CN0577>` is, by definition, a "FPGA mezzanine card"
(FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-CN0577-FMCZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
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
     - No

Hardware setup
-------------------------------------------------------------------------------

The :adi:`EVAL-CN0577-FMCZ <CN0577>` board connects to the FMC LPC connector on
the ZedBoard. The carrier setup requires power, UART (115200), Ethernet
connections and HDMI (if available).

ZED + EVAL-CN0577-FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/power_supply_1.png
   :width: 800

Go to :ref:`the setup guide <eval-cn0577-fmcz quickstart zed>`.
