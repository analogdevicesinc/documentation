Quick Start
===========

Supported Carrier
-----------------

`ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
(Rev C or later).

Required Hardware
-----------------

- AD-FMCMOTCON2-EBZ kit (controller board + AD-DRVLV2-EBZ drive board)
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- Lab power supply (12 V to 48 V, up to 20 A)
- AD-DYNO2-EBZ dynamometer (optional)
- USB keyboard/mouse and HDMI display for the ZedBoard

Setup
-----

.. figure:: connections.jpg
   :align: center

   Hardware connections for the AD-FMCMOTCON2-EBZ with ZedBoard

1. Connect the drive board to the controller board.
2. Connect the controller + drive board assembly to the FMC connector of the
   ZedBoard.
3. Make sure the **Emergency Stop** switch on the drive board is pressed.
4. Connect the DYNO sensor wire to the P3 connector on the controller board
   with the black wire towards the ZedBoard (if using the dynamometer).
5. Connect the motor wire to the P2 connector on the drive board.
6. Connect the power supply to the P1 connector on the drive board (and P3 if
   using a second motor).
7. Verify the following LEDs are ON:

   - DS1, DS2, DS3, DS4 on the controller board
   - DS1, DS2 on the drive board

8. If using the dynamometer, connect its 5 V supply.
9. Create an SD card image following the
   :doc:`Kuiper Linux </linux/kuiper/index>`
   and boot the ZedBoard.
10. After the ZedBoard is programmed, release the **Emergency Stop** switch and
    press the **Reset** switch for a few seconds to enable the power stage.
11. Use the IIO Oscilloscope application for monitoring and control (see the
    :doc:`software` section).
12. To shut down, use ``sudo shutdown -h now`` from the terminal rather than
    switching off the power directly.
