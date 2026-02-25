.. _eval-m355-ardz-int:

EVAL-M355-ARDZ-INT
===================

ADuCM355 Arduino Interposer.

Overview
--------

The Arduino interface can be found on many microprocessor development platforms
and is a great way to begin prototyping a design. The
:adi:`EVAL-M355-ARDZ-INT` was developed to enable quick and easy connection of
the :adi:`ADuCM355` based sensor boards to the :adi:`EVAL-ADICUP3029`
development board or any equivalent Arduino MCU controller board. This allows
for testing the functionality as well as the performance of the circuit using a
controlled evaluation environment.

Product Overview
----------------

ADuCM355 base Sensor Shield Board Interface Connectors:

.. figure:: pin_header.jpg
   :align: center

   ADuCM355 sensor shield board interface connectors (P1--P4)

.. important::

   Check if connectors P1, P2, P3 and P4 were correctly installed. The notch
   found for all headers should be at the bottom left near the header number 14
   of the silk screen.

Arduino Shield Board Interface Connectors:

.. figure:: arduino_shield_board_actual.png
   :align: center

   EVAL-M355-ARDZ-INT interposer board -- Arduino shield board interface

The EVAL-M355-ARDZ-INT interposer board was developed to quickly and easily
connect to the ADICUP3029 development board or any equivalent Arduino MCU
controller board.

Sensor Connector
----------------

The EVAL-M355-ARDZ-INT takes customized connectors to the ADuCM355 sensor surf
boards, and allows up to four channels of sensor boards to be used with the
EVAL-ADICUP3029 platform. Because the ADICUP3029 is an Arduino form factor
compatible development board, many other equivalent Arduino form factor
compatible development boards can also be used simply by writing custom code.
Below is the pinout of the custom connector of the sensor surf boards.

.. figure:: sensor_board_connector_header.png
   :align: center

   Sensor board connector header pinout

Power Rails
-----------

The EVAL-M355-ARDZ-INT provides 3.3 V power supply to ADuCM355 base sensor
shield board modules from the ADICUP3029 development board or any equivalent
Arduino MCU controller board.

Switch Matrix
-------------

.. figure:: swithch_matrix_actual.png
   :align: center

   Switch matrix (S1) on the EVAL-M355-ARDZ-INT

Digital Communication Interfaces
---------------------------------

The EVAL-M355-ARDZ-INT can accommodate up to four ADuCM355 sensor surf boards
at the same time. The software and hardware support communications via:

- **SPI** -- Available on P7 and P9
- **I2C** -- Available on P7
- **UART** -- Available on P8

Arduino shield boards follow a standard pinout for the Arduino form factor
compatible development boards.

.. figure:: arduino_schematic_config.png
   :align: center

   Arduino shield board interface schematic configuration

SWD/JTAG Connector
------------------

The debugger from the ADICUP3029 can be used and can be linked to the
interposer board through the SWD_DEBUG connector (P10). The user can use a
standard 10-pin ARM JTAG/SWD ribbon cable to connect the ADICUP3029 debugger
to the interposer board.

.. figure:: aducm3029_to_daughter_board_swd.png
   :align: center

   ADuCM3029 to daughter board SWD connection diagram

.. figure:: jtag_swd_10_connector.png
   :align: center

   10-pin JTAG/SWD connector pinout

.. figure:: swd_debugger_connectors_actual_1.png
   :align: center

   SWD debugger connectors on the EVAL-M355-ARDZ-INT

There is a way to cut the SWD traces on the ADICUP3029 board right at the
breakaway section of the board. By cutting the traces for the SWD_DIO, SWD_CLK
and SWD_RST located near P12, the user can program both the ADICUP3029 and
M355-INT boards without losing the ability to stream serial data back to the
USB port. There are two traces on the top of the board that must be cut using a
knife, and one trace found at the bottom of the ADICUP3029 (the outermost
trace).

.. figure:: adicup3029_primary_cut.png
   :align: center

   ADICUP3029 primary SWD trace cuts (top side)

.. figure:: adicup3029_secondary_cut.png
   :align: center

   ADICUP3029 secondary SWD trace cut (bottom side)

Debug/Programming Channel Selector
-----------------------------------

The EVAL-M355-ARDZ-INT can accommodate up to four ADuCM355 sensor surf boards
and communicate with these boards at the same time through SPI communication
protocol. Debugging and programming is done independently for each channel by
configuring the switch matrix labeled SWD_DEBUG_CH_SW (S1) found on the
silkscreen of the interposer board, with a corresponding LED indicator
identifying which sensor board is being accessed.

.. list-table::
   :header-rows: 1

   * - SWD_DEBUG_CH_SW
     - LED
   * - CH1
     - DS1
   * - CH2
     - DS2
   * - CH3
     - DS3
   * - CH4
     - DS4

Communication Protocol Selector
--------------------------------

By default the ADuCM355 sensor surf boards come preloaded with SPI
communication protocol back to the ADICUP3029.

Sensor shield boards can also communicate either through UART or I2C depending
on the firmware loaded on the sensor surf board and on the switch (S2) located
on the EVAL-M355-ARDZ-INT.

.. important::

   The software and the hardware must be set to the same digital communication
   protocol in order to correctly receive and display data.

Hardware Setup Procedure
------------------------

If you are using the ADICUP3029 development board with the EVAL-M355-ARDZ-INT
adaptor board, use the following setup procedure:

1. Set the SWD_DEBUG_CH_SW (S1) of the EVAL-M355-ARDZ-INT initially to CH1.
2. Set the UART switch (S2) on the EVAL-ADICUP3029 to the "USB" position in
   order to stream data back to the serial terminal.
3. Place the EVAL-M355-ARDZ-INT on top of the EVAL-ADICUP3029.

.. figure:: shield_board_to_adicup_connections_actual.png
   :align: center

   EVAL-M355-ARDZ-INT placed on top of EVAL-ADICUP3029

4. Place the desired number of ADuCM355 sensor daughter boards on top of the
   interposer board (up to 4).

.. figure:: sensor_shield_connections_actual.png
   :align: center

   ADuCM355 sensor daughter boards connected to the interposer

5. Plug in the EVAL-ADICUP3029 into the USB port of the computer using the
   micro-USB cable. You may need to wait for the ADICUP3029 device drivers to
   install if this is the first time the device is plugged in.

ADuCM355 Compatible Boards
---------------------------

The following table lists current ADuCM355 base sensor shield boards offered
by Analog Devices that connect to the EVAL-M355-ARDZ-INT adaptor board.

.. list-table::
   :header-rows: 1

   * - Board
     - Application
     - EVAL-ADICUP3029 Software
   * - :ref:`EVAL-CN0428-EBZ <eval-cn0428-ebz>`
     - Water Quality
     - Yes
   * - :ref:`EVAL-CN0429-EBZ <eval-cn0429-ebz>`
     - Gas Sensor
     - Yes

Software
--------

Combined firmware for CN0428 and CN0429 applications is available on GitHub:

- `EVAL-ADICUP3029 Source Code for CN0428 and CN0429
  <https://github.com/analogdevicesinc/EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_cn0428_cn0429>`__

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-M355-ARDZ-INT Design & Integration Files
   <https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-m355-ardz-int-designsupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- :adi:`ADuCM355 Product Page <ADUCM355>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
