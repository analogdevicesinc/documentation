SDP-S Hardware Description
==========================

This describes the hardware design of the EVAL-SDP-CS1Z board.

LEDs
----

There are two LEDs located on the SDP-S board. Refer to Figure HWD1.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/leds.jpg

Figure HWD1: SDP-S Board LEDs

LED 1
~~~~~

The orange LED is an LED to be used as a diagnostic tool for evaluation application developers.

POWER LED (PWR)
~~~~~~~~~~~~~~~

The green power LED indicates that the SDP-S board is powered. This is not an indication of USB connectivity between the SDP-B and the PC.

Connector Details
-----------------

The SDP-S board contains one Hirose FX8-120P-SV1(91), 120-pin header connector. Through this connector, the peripheral communication interfaces of the USB-to-serial engine are exposed. The exposed peripherals are:

-  SPI
-  I\ :sup:`2`\ C/TWI
-  GPIO

Also, included on the connector specification are input and output power pins, ground pins, and pins reserved for future use.

Connector Pin Assignments
-------------------------

The connector pin assignments have been defined independently of the any internal pin sharing, which occurs on the Blackfin processor. The table lists the connector pins and identifies the functionality assigned to each connector pin on the SDP-S board.

The pinout of this connector is consistent with other connectors across the SDP family.

120 Pin Connector Pin Assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= ======== ===========
Pin No. Pin Name Description
======= ======== ===========
======= ======== ===========

+-----+-------------+-----------------------------------------------------------------------------------------------+
| 1   | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 2   | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 3   | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 4   | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 5   | USB_VBUS    | Connected directly to the USB 5 V supply.                                                     |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 6   | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 7   | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 8   | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 9   | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 10  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 11  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 12  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 13  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 14  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 15  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 16  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 17  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 18  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 19  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 20  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 21  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 22  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 23  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 24  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 25  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 26  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 27  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 28  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 29  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 30  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 31  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 32  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 33  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 34  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 35  | SPI_HOLD    | Detects the ready state of the daughter board for SPI transfer.                               |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 36  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 37  | SPI_SEL_B   | SPI Chip Select B. Use this to control a second device on the SPI bus.                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 38  | SPI_SEL_C   | SPI Chip Select C. Use this to control a third device on the SPI bus.                         |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 39  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 40  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 41  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 42  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 43  | GPIO0       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 44  | GPIO2       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 45  | GPIO4       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 46  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 47  | GPIO6       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 48  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 49  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 50  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 51  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 52  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 53  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 54  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 55  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 56  | EEPROM_A0   | EEPROM A0. Connect to the A0 address line of the EEPROM.                                      |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 57  | RESET_OUT   | Active low pin for resetting the daughter board. Driven by SDP-S.                             |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 58  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 59  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 60  | RESET_IN    | Active low pin to reset EVAL-SDP-CS1Z board.                                                  |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 61  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 62  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 63  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 64  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 65  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 66  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 67  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 68  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 69  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 70  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 71  | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 72  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 73  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 74  | GPIO7       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 75  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 76  | GPIO5       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 77  | GPIO3       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 78  | GPIO1       | General-purpose input/output.                                                                 |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 79  | SCL_0       | I2C Clock 0. The daughter board EEPROM must be connected to this bus.                         |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 80  | SDA_0       | I2C Data 0. The daughter board EEPROM must be connected to this bus.                          |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 81  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 82  | SPI_CLK     | SPI clock.                                                                                    |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 83  | SPI_MISO    | SPI master in, slave out data.                                                                |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 84  | SPI_MOSI    | SPI master out, slave in data.                                                                |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 85  | SPI_SEL_A   | SPI Chip Select A.                                                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 86  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 87  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 88  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 89  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 90  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 91  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 92  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 93  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 94  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 95  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 96  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 97  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 98  | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 99  | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 100 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 101 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 102 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 103 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 104 | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 105 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 106 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 107 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 108 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 109 | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 110 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 111 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 112 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 113 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 114 | DNU         | Do not use. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 115 | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 116 | VIO (+3.3V) | 3.3 V output. 20 mA maximum current available to power the I/O voltage on the daughter board. |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 117 | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 118 | GND         | Connect to the ground plane of the daughter board.                                            |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 119 | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+
| 120 | NC          | No connect. Leave this pin unconnected. Do not ground.                                        |
+-----+-------------+-----------------------------------------------------------------------------------------------+

Each interface provided by the SDP-B is available on unique pins of the SDP-S’s 120 pin connector. The connector pin numbering scheme is out-line in Figure HWD2.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/connector_outline.jpg

Figure HWD2: 120 Pin Connector Outline

Power
~~~~~

The SDP-S board is powered by the USB connector. It does not require power to be supplied by the daughter board. The SDP-S board provides 3.3 V at 20 mA on Pin 116 (VIO_3.3) to connected daughter boards as the VIO voltage for the daughterboard. Pin 5 (USB_VBUS) is connected to the 5 V line of the USB connector, providing 5 V ±10% as an output of the SDP board.

Daughter Board Design Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The daughter board design guidelines specify the layout, connector positioning, keep out areas, and dimensions of potential daughter boards. This guidance is to ensure that a daughter board can connect to any controller board from the SDP family. Following these guidelines ensures that the connector on the SDP-S or any other controller board in the SDP family can have any one of the available daughter boards physically attached.

Connector Location
~~~~~~~~~~~~~~~~~~

The daughter board connector and securing screw holes are located in the top left hand corner. This arrangement for a daughter board is shown in Figure 5. If a daughter board exceeds these dimensions, it may not be possible to connect it to the other controller or interposer boards in the SDP family. Every effort was made to extend the 5.9 mm dimension as large as possible to allow space for vias between the connector and the edge of the board. These are absolute maximum dimensions and must not be exceeded. The full specification drawing for the connector location on the daughter board is shown in Figure 6. The mating daughter board 120-pin connector is the Hirose FX8-120S-SV(21), 120-pin receptacle, FEC 132-4660, Digi-Key H1219-ND. Consult the connector data sheet for full details on the connector. Note that Pin 1 to Pin 60 are placed on the left side of the connector and Pin 61 to Pin 120 are placed on the right side of the connector.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/connector_location.jpg

Figure HWD3: Maximum Board Dimensions for Connector Placement

The full specification drawing for the connector location on the daughter board can be seen in Figure HWD4.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/connector_placement.jpg

Figure HWD4: Connector Placement on Compatible Daughter Board

The mating daughter board 120 pin connector is the Hirose FX8-120S-SV(21), 120-pin receptacle, FEC 132-4660, Digikey H1219-ND. Please consult the connector's data sheet for full details on the connector. Note pins 1 to 60 are placed on the left side of the connector and pins 61 to 120 are placed on the right side of the connector.

Keep Out Area
~~~~~~~~~~~~~

To allow the greatest flexibility for future controller boards, a keep out area is established for components higher that 3 mm. The keep out area is 12.65 mm wide and extends down the entire left side of the daughter board.

Restriction on Right Angle Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Due to the layout of other boards in the SDP family, and their daughter boards, right angle connectors are not allowed on the top and left edges of the daughter boards and (if required) should be placed on the right or bottom edges. A right angle connector describes any con¬nector that requires the connection to protrude over the edge of the board (for example, right angle SMB or screw terminal).

Mechanical Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~

TThe mechanical specifications of the SDP-S board are 2.36 inch × 0.87 inch (60 mm × 22 mm). The tallest component on the top is approximately 0.17 inch (4.3 mm), and the tallest compo¬nents on the bottoms are the 120-pin connectors at approximately 0.152 inch (3.86 mm). Refer to Figure HWD5.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-s/connector_mechspec2.jpg

Figure HWD5: SDP-S Board Mechanical Specification
