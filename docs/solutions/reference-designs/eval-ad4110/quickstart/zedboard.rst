.. _eval-ad4110 quickstart zedboard:

ZedBoard Quick Start
===============================================================================

.. figure:: ../images/zed_board.jpeg
   :alt: Digilent ZedBoard (Zynq-7000 ARM/FPGA SoC development board)
         with labeled PMOD, UART, Ethernet, and power connectors
   :width: 800

   Digilent ZedBoard

.. esd-warning::

This guide provides step-by-step instructions for setting up the
:adi:`EVAL-AD4110-1SDZ` on the Digilent ZedBoard using the ADI HDL reference
design and No-OS baremetal firmware.

Required hardware
-------------------------------------------------------------------------------

- :adi:`EVAL-AD4110-1SDZ` evaluation board
- `Digilent ZedBoard
  <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
  (Zynq-7000 ARM/FPGA SoC development board)
- Jumper wires for PMOD connections
- External ±15 V power supply for the evaluation board
- Micro-USB cable for UART console access
- Micro-USB cable for JTAG

Required software and files
-------------------------------------------------------------------------------

The following must be available before programming the ZedBoard:

- HDL hardware platform export (``system_top.xsa``), built from the
  :external+hdl:ref:`build_hdl`
- No-OS AD4110-1 project:
  :git-no-OS:`projects/ad4110 <projects/ad4110>`
- Xilinx Vitis (includes ``xsct`` and the ARM cross-compilation
  toolchain)

More details can be found at :ref:`eval-ad4110 prerequisites`.

Building the HDL project
-------------------------------------------------------------------------------

The design is built on ADI's generic HDL reference design framework. To build
from source, clone the HDL repository and build the project:

.. shell::

   $cd hdl/projects/ad4110/zed
   $make

A comprehensive build guide is available in the
:external+hdl:ref:`build_hdl` user guide.

Setting up the hardware
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4110-1SDZ` connects to the ZedBoard via the SPI PMOD
connector (J2) on the evaluation board and the JA/JB PMOD headers on the
ZedBoard. The evaluation board is powered by the 3.3 V voltage from the
ZedBoard PMOD (LED1 green indicates a valid SDP connection). The evaluation
board also requires ±15 V applied to J14 for the high-voltage analog front
end (LED3 green indicates 5 V supply).

Follow these steps in order to avoid damaging components:

#. Ensure the ZedBoard and the evaluation board are powered off.
#. Connect ±15 V and GND to J14 on the evaluation board.
#. Wire the SPI and GPIO signals from J2 on the evaluation board to
   the ZedBoard PMOD headers as listed in the
   :external+hdl:ref:`ad4110`.
#. Connect the micro-USB cable to the UART port on the ZedBoard.
#. Connect the JTAG cable from the ZedBoard to the host PC.
#. Configure a UART terminal (PuTTY, Tera Term, or Minicom) at
   115200 baud, 8N1.
#. Power on the ZedBoard.
#. Power on the evaluation board external supply.
#. Verify that LED3 (green) on the evaluation board is illuminated,
   indicating 5 V supply is present.
#. Navigate to the no-OS directory in the AD4110-1 project and run ``make run``
   to program the FPGA.

.. figure:: ../images/ad4110_setup.jpeg
   :alt: EVAL-AD4110-1SDZ connected to the Digilent ZedBoard via
         PMOD headers with ±15 V supply connected to J14
   :align: center
   :width: 800

   Completed EVAL-AD4110-1SDZ and ZedBoard hardware setup

Verifying the setup
-------------------------------------------------------------------------------

Once the No-OS application is running, the UART terminal displays the
initialization output.


.. note::

   A signal source is required at the analog input connector (J6 for high
   voltage, J8 for low voltage, J10 for thermocouple) before capturing
   meaningful data.
