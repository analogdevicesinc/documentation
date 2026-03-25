.. _eval-cn0338-ardz hardware:

Hardware
========

This page describes the hardware setup and connector configuration for the
:ref:`eval-cn0338-ardz` shield board used with the EVAL-ADICUP360 development
platform.

Connectors and Configuration
-----------------------------

The CN0338 firmware uses P0.1 and P0.2 ports of the ADuCM360 as UART
communication ports. The UART interface can be connected to the USER USB or
DEBUG USB on the EVAL-ADICUP360 base board.

CN0338 Shield Board
~~~~~~~~~~~~~~~~~~~

The shield board contains the lamp connector, light tube, and mechanical
mounting for the sensor board.

- The lamp is connected through the **DS1** connector and is powered by the
  external wall power supply provided on the EVAL-ADICUP360.
- The light tube is made of PVC piping and is located in the large rectangular
  blocked-off section of the EVAL-CN0338-ARDZ, and secured to the board using
  tie wraps.
- **J1**, **J2**, **J3**, and **J4** provide electrical and mechanical
  connector mounts to the sensor board.

CN0338 Sensor Board
~~~~~~~~~~~~~~~~~~~

The sensor board contains the thermopile and is mounted vertically to the
shield board.

- The sensor board should be mounted to the shield board vertically. Plug the
  sensor board contact wing (lower part of sensor board without solder mask)
  into the slot (at the right part of the board between J1 and J4) of the
  shield board. Ensure headers J1, J2, J3, J4 at the shield board plug into
  receptacles J4, J3, J2, J1 at the sensor board firmly.
- The thermopile sensor is located at reference designator **T1**, which is at
  the opposite end of the light tube from where the lamp plugs in.
- The sensor output goes directly from the EVAL-CN0338-ARDZ to the on-board
  24-bit sigma-delta ADCs of the EVAL-ADICUP360, where the signals are
  converted and processed into CO2 concentrations.

Setting Up the Hardware
-----------------------

.. figure:: cn0338_hw_combined.png
   :width: 550px

   EVAL-CN0338-ARDZ connected to EVAL-ADICUP360.

1. Set the jumpers/switches on the EVAL-ADICUP360 base board for programming
   mode.
2. Connect the **EVAL-CN0338-ARDZ** to the Arduino connectors **P2, P3, P5,
   P6, P7, P8, P9** of the **EVAL-ADICUP360** board.
3. Plug in the DC power supply into the DC barrel jack (P11) on the
   EVAL-ADICUP360.
4. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).
