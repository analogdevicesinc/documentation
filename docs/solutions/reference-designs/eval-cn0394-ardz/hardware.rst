.. _eval-cn0394-ardz hardware:

Hardware
========

This page describes the hardware setup and connector configuration for the
:ref:`eval-cn0394-ardz` shield board used with the EVAL-ADICUP360 development
platform.

General Setup
-------------

- Connect the EVAL-CN0394-ARDZ to the EVAL-ADICUP360 board.
- Connect up to 4 thermocouples to EVAL-CN0394-ARDZ **P1** to **P4**, marked
  on PCB with **CH0** to **CH3**.
- Connect the EVAL-ADICUP360 **USER** USB port to PC with USB cable.

Connectors and Configurations
------------------------------

Thermocouple Connectors
~~~~~~~~~~~~~~~~~~~~~~~~

Each of the four channels uses an Omega-style universal connector for the
thermocouples, which makes it easy to plug in and out different thermocouple
types. Type U was selected so that all channels on the board (P1 to P4) are
universal and interchangeable.

There is an RTD beneath the copper tabs of each connector which is used to
measure the cold junction temperature. No external cold junction measurement is
needed with this board.

Analog Sensor Inputs
~~~~~~~~~~~~~~~~~~~~~

The analog outputs of each thermocouple channel and each RTD channel are
connected directly to connector P6. Each of these analog voltages is passed
directly to the ADuCM360 on the EVAL-ADICUP360 board and processed using the
24-bit sigma-delta ADCs integrated into that IC.

.. list-table:: P6 Pin Connections
   :header-rows: 1

   * - P6 Pin
     - Sensor/Channel
   * - Pin 1
     - Thermocouple+ (P1)
   * - Pin 2
     - Thermocouple+ (P2)
   * - Pin 3
     - Thermocouple+ (P3)
   * - Pin 4
     - Thermocouple+ (P4)
   * - Pin 5
     - RTD Output (R1)
   * - Pin 6
     - RTD Output (R2)
   * - Pin 7
     - RTD Output (R3)
   * - Pin 8
     - RTD Output (R4)

.. list-table:: P7 Pin Connections
   :header-rows: 1

   * - P7 Pin
     - Sensor/Channel
   * - Pin 1
     - RTD Common
   * - Pin 4
     - Thermocouple Common (-)
   * - Pin 7
     - Voltage Reference

Setting Up the Hardware
-----------------------

1. To program the base board, set the jumpers/switches as shown in the
   following figure. The important jumpers/switches are highlighted in red.

   .. figure:: cn0216_hw_config.png
      :width: 600px
      :align: center

      EVAL-ADICUP360 jumper/switch configuration for programming mode.

2. Connect the **EVAL-CN0394-ARDZ** to the Arduino connectors **P2, P3, P5,
   P6, P7, P8, P9** of the **EVAL-ADICUP360** board.
3. Connect your thermocouples to the EVAL-CN0394-ARDZ via **P1** to **P4**.
4. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).
