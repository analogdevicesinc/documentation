.. _eval-ad4110 prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. The AD4110-1 evaluation board: :adi:`EVAL-AD4110-1SDZ`
#. A Digilent ZedBoard (Zynq-7000 ARM/FPGA SoC development board)
#. Jumper wires for PMOD connections
#. An external ±15 V power supply for the evaluation board
#. A micro-USB cable for UART console access

SDP-B (legacy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. The AD4110-1 evaluation board: :adi:`EVAL-AD4110-1SDZ`
#. The :adi:`SDP-B` controller board

   - Acts as the USB communication link between the PC and the
     evaluation board.

#. A USB cable
#. An external ±12 V to ±20 V power supply

   - A ±15 V supply is recommended and must be connected to J14 on
     the evaluation board.
   - GND must be connected to the GND pin on J14.

#. A signal source appropriate for the desired demo mode

   - Voltage mode: ±10 V signal
   - Current mode: ±20 mA signal
   - Thermocouple: Type-K or similar thermocouple
   - RTD: 3-wire PT100 or similar RTD sensor

Software prerequisites
-------------------------------------------------------------------------------

ZedBoard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following must be available before programming the ZedBoard:

- HDL hardware platform export (``system_top.xsa``), built from the
  :external+hdl:ref:`build_hdl`
- No-OS AD4110-1 project:
  :git-no-OS:`projects/ad4110 <projects/ad4110>`
- Xilinx Vitis

SDP-B (legacy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following must be installed on a PC running Windows before connecting the
evaluation board:

#. AD4110-1 evaluation software

   - Provides the graphical interface for configuring and evaluating
     the device.
   - Must be installed before connecting the :adi:`SDP-B` board to the PC.

#. :adi:`SDP-B` board drivers (ADI SDP Drivers)

   - Installed as part of the evaluation software setup.
   - The PC must be restarted after driver installation.

Refer to :ref:`eval-ad4110 quickstart sdp-b` for step-by-step
installation instructions.

Mbed IIO firmware (SDP-K1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. The AD4110-1 evaluation board: :adi:`EVAL-AD4110-1SDZ`
#. An :adi:`SDP-K1` controller board
#. A USB cable for connecting :adi:`SDP-K1` to the PC
#. On the host PC:

   - `Keil Studio <https://studio.keil.arm.com/>`_ for building
     and flashing the firmware
   - Libiio Windows installer
   - IIO Oscilloscope Windows installer

.. note::

   :adi:`ADI <>` does not offer FPGA carrier boards or :adi:`SDP-K1` boards
   for sale or loan; obtaining the hardware is the normal part of development
   and evaluation.
