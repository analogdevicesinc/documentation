.. _eval-cn0396-ardz hardware:

Hardware
========

This page describes the hardware setup and connector configuration for the
:ref:`eval-cn0396-ardz` shield board.

Hardware Setup
--------------

- Connect the EVAL-CN0396-ARDZ board to the microprocessor board using mating
  headers: POWER, ANALOG, DIGI0, DIGI1, and ICSP.
- Connect your 4-electrode electrochemical gas sensor to socket **M1**.
- The EVAL-CN0396-ARDZ board is powered by the POWER header when using an
  Arduino form factor compatible processor board. Ensure that **5V** (ANALOG
  Pin 5), **IOREF** (ANALOG Pin 2), and **GND** (ANALOG Pin 6/7) pins are
  connected.

Connectors, Sensors, and Configurations
-----------------------------------------

.. figure:: cn0396_board_label_wiki.png
   :align: center
   :width: 600px

   EVAL-CN0396-ARDZ board connectors and component layout.

Gas Sensors
~~~~~~~~~~~

The evaluation board comes packaged with an Alphasense COH-A2 sensor. Sockets
are provided for easy installation of the sensor.

**Pin-Compatible Sensors:**

- `Alphasense COH-A2
  <https://www.alphasense.com/WEB1213/wp-content/uploads/2019/09/CO-H2S.pdf>`__
- `Alphasense SOH-A2
  <https://www.alphasense.com/WEB1213/wp-content/uploads/2017/03/SO2-H2S.pdf>`__
- DD-Scientific GS+4DT

**Sensor Socket Connection:**

.. figure:: sensorsocket.png
   :align: center
   :width: 200px

   Sensor socket pin layout.

.. list-table:: Sensor Socket Pin Mapping
   :header-rows: 1

   * - Pin Name
     - Description
   * - WE1
     - Working Electrode (CO gas electrode for COH-A2 sensor)
   * - CE
     - Counter Electrode
   * - WE2
     - Working Electrode (H2S gas electrode for COH-A2 sensor)
   * - RE
     - Reference Electrode

.. note::

   Not all sensors listed have been tested with the EVAL-CN0396-ARDZ. Using
   different sensors may require modifications to the software and/or
   hardware.

Chip Select Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Three headers on the board allow selection of the digital pin used as the Chip
Select (CS) signal for the AD7798, AD5270, and ADT7310 SPI communications.

**AD7798_CS** -- Selects either Arduino Pin D9 or D10 as CS for the AD7798
ADC:

.. list-table::
   :header-rows: 1

   * - AD7798_CS Connection
     - Arduino Pin
   * - Jumper Pin 1 and Pin 2
     - D10
   * - Jumper Pin 2 and Pin 3
     - D9

**AD5270_CS** -- Selects either Arduino Pin D5 or D6 as CS for the AD5270
digital rheostat:

.. list-table::
   :header-rows: 1

   * - AD5270_CS Connection
     - Arduino Pin
   * - Jumper Pin 1 and Pin 2
     - D6
   * - Jumper Pin 2 and Pin 3
     - D5

**ADT7310_CS** -- Selects either Arduino Pin D3 or D4 as CS for the ADT7310
digital temperature sensor:

.. list-table::
   :header-rows: 1

   * - ADT7310_CS Connection
     - Arduino Pin
   * - Jumper Pin 1 and Pin 2
     - D4
   * - Jumper Pin 2 and Pin 3
     - D3

Setting Up with EVAL-ADICUP360
-------------------------------

1. To program the base board, set the jumpers/switches as shown in the figure
   below. The important jumpers/switches are highlighted in red.

   .. figure:: cn0216_hw_config.png
      :align: center
      :width: 500px

      EVAL-ADICUP360 jumper/switch configuration for programming mode.

2. Connect the **EVAL-CN0396-ARDZ** to the Arduino connectors **P2, P5, P6,
   P7, P8** of the **EVAL-ADICUP360** board.

3. Set the jumpers on the EVAL-CN0396-ARDZ board as shown in the figure below.

   .. figure:: cn0396_demo_4.png
      :align: center
      :width: 600px

      EVAL-CN0396-ARDZ jumper configuration.

4. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB (P14).

Setting Up with Arduino Uno
----------------------------

1. Plug the **EVAL-CN0396-ARDZ** shield on top of the **Arduino Uno**
   development board by matching up the **POWER, ANALOG, DIGI0, DIGI1**
   connectors. The boards should only plug together one way, preventing
   reverse connections.

2. Connect your electrochemical gas sensor to the EVAL-CN0396-ARDZ via
   **M1**.

3. Set the jumpers on the EVAL-CN0396-ARDZ board as shown in the jumper
   configuration figure above.

4. Plug in the Type B USB cable into the USB port on the Arduino Uno, and
   the other end into the PC or laptop.

.. figure:: cn0396_arduino_setup.jpg
   :align: center
   :width: 500px

   EVAL-CN0396-ARDZ shield mounted on Arduino Uno.
