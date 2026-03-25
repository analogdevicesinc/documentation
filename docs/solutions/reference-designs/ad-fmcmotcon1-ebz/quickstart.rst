Quick Start
===========

Supported Carrier
-----------------

`ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
(Rev C or later).

Required Hardware
-----------------

- AD-FMCMOTCON1-EBZ controller board
- AD-DRVLV1-EBZ low voltage drive board
- ZedBoard
- 24 V, 3 A capable lab power supply
- USB keyboard and mouse for the Zynq device
- HDMI display (monitor or TV)
- AD-DYNO1-EBZ dynamometer (optional)

Linux on Zynq Quick Start
--------------------------

1. Create an SD card image following the
   :doc:`Kuiper Linux </linux/kuiper/index>` instructions.
2. Connect the low voltage drive board to the controller board.
3. Connect the controller + drive board assembly to the FMC connector of the
   ZedBoard.
4. Insert the 6-pin Hall connector into P7 (pin 1 is the empty slot). For
   encoder use, connect pins one-to-one with the P7 connector.
5. Connect the motor to P1 and the lab power supply to P4.
6. Ensure the emergency stop button P2 is pressed before powering on.
7. Boot the ZedBoard from the SD card.
8. After boot, the IIO Oscilloscope application launches on the HDMI display.
9. Release the emergency stop button P2 and press the reset switch S1 for a
   few seconds to start the motor.
10. Use the IIO Oscilloscope application for monitoring and control (see the
    :doc:`software` section).

This platform uses a persistent file system. Always perform a clean shutdown
before removing power:

.. code-block:: bash

   sudo shutdown -h now

ISE Project with Chipscope Quick Start
---------------------------------------

This flow uses the Xilinx ISE 14.6 HDL project with Chipscope Pro 14.6 for
manual control and monitoring without Linux.

1. Follow the hardware setup steps above (steps 2--6).
2. Program the FPGA with the ``top.bit`` bitstream from the ISE project using
   the iMPACT tool.
3. Open the Chipscope project for monitoring and control.

.. figure:: chipscope.png
   :align: center

   Chipscope interface overview

The Chipscope interface is divided into four sections:

**Section A -- Control Parameters:**

.. list-table::
   :header-rows: 1

   * - Name
     - Width
     - Description
   * - PWM
     - 32
     - PWM value (must be between 0x480 and 0x800)
   * - GAIN
     - 2
     - ADC signal chain amplification (0=x1, 1=x4, 2=x2, 3=x8)
   * - RUN_MOTOR
     - 1
     - Start / Stop the motor
   * - STAR_MOTOR
     - 1
     - 1 for star-wired motors, 0 for delta-wired motors
   * - CW_DIR
     - 1
     - 1 for clockwise, 0 for counter-clockwise

**Section B -- Monitoring signals:** IA, IB, IT (from both controller and
drive boards), VBUS, SPEED (in 100 ns units between Hall state changes), and
POSITION (Hall sensor reading).

**Section C** -- Graphical speed plot.

**Section D** -- Current and voltage waveform plots.
