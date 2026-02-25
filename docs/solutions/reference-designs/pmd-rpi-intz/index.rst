.. _pmd-rpi-intz:

PMD-RPI-INTZ
=============

Raspberry Pi PMOD Adapter Board.

Overview
--------

The :adi:`PMD-RPI-INTZ` is an add-on adapter board for the Raspberry Pi that
allows interfacing with up to 4 Pmod boards (2 SPI devices, 2 I2C devices),
1 QuikEval demo board and 1 :adi:`DC1613A`-compatible demonstration board.

.. figure:: pmd-rpi-intz_angle.jpg
   :align: center
   :width: 400px

   PMD-RPI-INTZ adapter board

The :adi:`PMD-RPI-INTZ` follows the standard Raspberry Pi HAT mechanical
specifications, minus the cutouts for the camera and display flexis. An ID
EEPROM is also included on the board to allow auto-configuration.

Evaluation Kit Contents
~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`PMD-RPI-INTZ` Adapter Board

Adapter Board Hardware
----------------------

.. figure:: pmd-rpi-intz_top_labels.png
   :align: center
   :width: 600px

   PMD-RPI-INTZ board top view with component labels

.. warning::

   There is no level translation provided on the :adi:`PMD-RPI-INTZ`. Only
   connect devices that operate with 3.3 V logic levels. Do not apply higher
   logic levels on the IO pins to avoid damaging the Raspberry Pi.

SPI Pmod Connectors (P1 and P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: pmd-rpi-intz_spi_pmod_connectors.png
   :align: center
   :width: 250px

   SPI Pmod connectors P1 and P2

Pmod devices that use the SPI interface should be connected to either of the
two 2x6 female headers located on the left-hand side of the
:adi:`PMD-RPI-INTZ`. Each header pin is connected to a Raspberry Pi GPIO pin
through the 40-pin connector (P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P1
pins and their corresponding functions.

.. list-table:: SPI Pmod Connector #1 (P1) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Number
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1
     - Pin 24 (GPIO8) :sup:`1`
     - **SPI Pmod #1 CS1.** SPI Chip Select #1 from the Raspberry Pi to the
       Pmod device.
   * - 2
     - Pin 19 (SPI0 MOSI) :sup:`2`
     - **MOSI.** SPI Data from the Raspberry Pi to the Pmod device.
   * - 3
     - Pin 21 (SPI0 MISO) :sup:`2`
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 4
     - Pin 23 (SPI0 SCLK) :sup:`2`
     - **SCLK.** SPI Clock from the Raspberry Pi to the Pmod device.
   * - 5
     - GND
     - **Ground**
   * - 6
     - 3V3 Power
     - **SPI Pmod #1 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.
   * - 7
     - Pin 35 (GPIO19)
     - **SPI Pmod #1 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 8
     - Pin 40 (GPIO21)
     - **SPI Pmod #1 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 9
     - Pin 38 (GPIO20)
     - **SPI Pmod #1 CS2.** SPI Chip Select #2 from the Raspberry Pi to the
       Pmod device.
   * - 10
     - Pin 12 (GPIO18)
     - **SPI Pmod #1 CS3.** SPI Chip Select #3 from the Raspberry Pi to the
       Pmod device.
   * - 11
     - GND
     - **Ground**
   * - 12
     - 3V3 Power
     - **SPI Pmod #1 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.

| :sup:`1` IO pin shared with the QuikEval Demo Board Connector (P5).
| :sup:`2` IO pins shared with the SPI Pmod Connector #2 (P2) and the QuikEval
  Demo Board Connector (P5).

.. figure:: pmd-rpi-intz_spi_pmod_labels.png
   :align: center
   :width: 200px

   SPI Pmod connector pin labels

Similarly, the table below lists the default Raspberry Pi GPIO pin assignments
for the P2 pins and their corresponding functions.

.. list-table:: SPI Pmod Connector #2 (P2) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Number
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1
     - Pin 26 (GPIO7)
     - **SPI Pmod #2 CS1.** SPI Chip Select #1 from the Raspberry Pi to the
       Pmod device.
   * - 2
     - Pin 19 (SPI0 MOSI) :sup:`1`
     - **MOSI.** SPI Data from the Raspberry Pi to the Pmod device.
   * - 3
     - Pin 21 (SPI0 MISO) :sup:`1`
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 4
     - Pin 23 (SPI0 SCLK) :sup:`1`
     - **SCLK.** SPI Clock from the Raspberry Pi to the Pmod device.
   * - 5
     - GND
     - **Ground**
   * - 6
     - 3V3 Power
     - **SPI Pmod #2 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.
   * - 7
     - Pin 22 (GPIO25)
     - **SPI Pmod #2 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 8
     - Pin 32 (GPIO12)
     - **SPI Pmod #2 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 9
     - Pin 29 (GPIO5)
     - **SPI Pmod #2 CS2.** SPI Chip Select #2 from the Raspberry Pi to the
       Pmod device.
   * - 10
     - Pin 31 (GPIO6)
     - **SPI Pmod #2 CS3.** SPI Chip Select #3 from the Raspberry Pi to the
       Pmod device.
   * - 11
     - GND
     - **Ground**
   * - 12
     - 3V3 Power
     - **SPI Pmod #2 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.

:sup:`1` IO pins shared with the SPI Pmod Connector #1 (P1) and the QuikEval
Demo Board Connector (P5).

I2C Pmod Connectors (P3 and P4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: pmd-rpi-intz_i2c_pmod_connectors.png
   :align: center
   :width: 250px

   I2C Pmod connectors P3 and P4

Pmod devices that use the I2C interface should be connected to either of the
two 2x6 female headers located on the lower side of the :adi:`PMD-RPI-INTZ`.
Each header pin is connected to a Raspberry Pi GPIO pin through the 40-pin
connector (P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P3
pins and their corresponding functions.

.. list-table:: I2C Pmod Connector #1 (P3) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Numbers
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1 & 7
     - Pin 37 (GPIO26)
     - **I2C Pmod #1 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 2 & 8
     - Pin 33 (GPIO13)
     - **I2C Pmod #1 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 3 & 9
     - Pin 5 (I2C SCL) :sup:`1`
     - **SCL.** I2C Clock from the Raspberry Pi to the Pmod device.
   * - 4 & 10
     - Pin 3 (I2C SDA) :sup:`1`
     - **SDA.** I2C Data from the Raspberry Pi to the Pmod device.
   * - 5 & 11
     - GND
     - **Ground**
   * - 6 & 12
     - 3V3 Power
     - **I2C Pmod #1 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.

:sup:`1` IO pins shared with the I2C Pmod Connector #2 (P4), the QuikEval Demo
Board Connector (P5) and the :adi:`DC1613A`-Compatible Demo Board Connector
(P6).

Similarly, the table below lists the default Raspberry Pi GPIO pin assignments
for the P4 pins and their corresponding functions.

.. list-table:: I2C Pmod Connector #2 (P4) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Numbers
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1 & 7
     - Pin 13 (GPIO27)
     - **I2C Pmod #2 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 2 & 8
     - Pin 11 (GPIO17)
     - **I2C Pmod #2 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 3 & 9
     - Pin 5 (I2C SCL) :sup:`1`
     - **SCL.** I2C Clock from the Raspberry Pi to the Pmod device.
   * - 4 & 10
     - Pin 3 (I2C SDA) :sup:`1`
     - **SDA.** I2C Data from the Raspberry Pi to the Pmod device.
   * - 5 & 11
     - GND
     - **Ground**
   * - 6 & 12
     - 3V3 Power
     - **I2C Pmod #2 VCC.** Connected to the 3.3 V Regulator Output of the
       Raspberry Pi.

:sup:`1` IO pins shared with the I2C Pmod Connector #1 (P3), the QuikEval Demo
Board Connector (P5) and the :adi:`DC1613A`-Compatible Demo Board Connector
(P6).

.. note::

   **Connecting Hardware Designed for Digilent I2C Pmod Interface Specification
   Ver. 1.0.0:**

   Version 1.0.0 of the Digilent Pmod Interface Specification required 2x4
   headers to be used for I2C devices; Pmod boards that follow this old standard
   should be connected to either P3 or P4 as shown below:

   .. figure:: pmd-rpi-intz_i2c_pmod_2x4.png
      :align: center
      :width: 250px

      Connecting old 2x4 I2C Pmod devices

QuikEval Demo Board Connector and SPI/I2C Switch (P5 and SW1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QuikEval demonstration boards should be connected to the 14-pin shrouded header
through a :adi:`CA2440` ribbon cable (included with each demo board). Each
header pin is connected to a Raspberry Pi GPIO pin through the 40-pin connector
(P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P5
pins and their corresponding functions.

.. figure:: pmd-rpi-intz_quikeval_connector.png
   :align: center
   :width: 250px

   QuikEval demo board connector P5

.. list-table:: QuikEval Demo Board Connector (P5) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Number
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1
     - 5V Power
     - **QuikEval Demo Board Auxiliary Power.** Normally connected to 5 V but
       external power can be applied using JP1 and EXT_V+.
   * - 2
     - 3V3 Power
     - **QuikEval Demo Board VCCIO.** Connected to the 3.3 V Regulator Output
       of the Raspberry Pi.
   * - 3
     - GND
     - **Ground**
   * - 4
     - Pin 23 (SPI0 SCLK) :sup:`1` or Pin 5 (I2C1 SCL) :sup:`2`
     - **SCLK (SPI)** or **SCL (I2C).** Select the appropriate clock pin for
       the demo board using SW1.
   * - 5
     - Pin 21 (SPI0 MISO) :sup:`1`
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 6
     - Pin 24 (GPIO8) :sup:`1`
     - **QuikEval Demo Board CS.** SPI Chip Select Signal from the Raspberry
       Pi to the demo board.
   * - 7
     - Pin 19 (SPI0 MOSI) :sup:`1` or Pin 3 (I2C1 SDA) :sup:`2`
     - **MOSI (SPI)** or **SDA (I2C).** Select the appropriate data pin for
       the demo board using SW1.
   * - 8
     - GND
     - **Ground**
   * - 9
     - Pin 3 (I2C1 SDA) :sup:`2`
     - **QuikEval Demo Board EESDA.** I2C Data exchanged between the
       Raspberry Pi and the demo board EEPROM.
   * - 10
     - 5V Power
     - **QuikEval Demo Board EEVCC.** Connected to the 5 V Input Power of
       the Raspberry Pi. Used to supply power to the demo board EEPROM.
   * - 11
     - Pin 5 (I2C1 SCL) :sup:`2`
     - **QuikEval Demo Board EESCL.** I2C Clock from the Raspberry Pi to the
       demo board EEPROM.
   * - 12
     - GND
     - **Ground**
   * - 13
     - GND
     - **Ground**
   * - 14
     - Pin 15 (GPIO22)
     - **QuikEval Demo Board GPIO.** Actual function depends on the demo
       board.

| :sup:`1` IO pins shared with the SPI Pmod Connector #1 (P1) and the SPI Pmod
  Connector #2 (P2).
| :sup:`2` IO pins shared with the I2C Pmod Connector #1 (P3), the I2C Pmod
  Connector #2 (P4) and the :adi:`DC1613A`-Compatible Demo Board Connector (P6).

QuikEval demonstration boards will use either the SPI or the I2C interface,
depending on the model. Change the setting of the slide switch SW1 accordingly.

.. figure:: pmd-rpi-intz_sw1.jpg
   :align: center
   :width: 150px

   SW1 SPI/I2C selection switch

.. note::

   Some QuikEval demonstration boards have the option of being powered via an
   auxiliary power pin (Pin 1 of P6). To accomplish this with the
   :adi:`PMD-RPI-INTZ`, connect an external power supply to EXT_V+ and change
   the setting of the solder jumper JP1.

   .. list-table:: JP1 Configuration
      :header-rows: 1
      :widths: 20 80

      * - JP1 Setting
        - EXT_V+ Configuration
      * - Open (Default)
        - Tied to +5 V power supply of the Raspberry Pi
      * - Shorted
        - Can use an external power supply via the EXT_V+ test point

DC1613A-Compatible Demo Board Connector (P6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`DC1613A`-Compatible demonstration boards should be connected to the
12-pin shrouded header above P4. Each header pin is connected to a Raspberry Pi
GPIO pin through the 40-pin connector (P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P6
pins and their corresponding functions.

.. figure:: pmd-rpi-intz_psm_connector.png
   :align: center
   :width: 250px

   DC1613A-compatible demo board connector P6

.. list-table:: DC1613A-Compatible Demo Board Connector (P6) Pinout
   :header-rows: 1
   :widths: 10 30 60

   * - Pin Number
     - Default Raspberry Pi Pin Assignment
     - Pin Function on the PMD-RPI-INTZ
   * - 1
     - 5V Power
     - **DC1613A-Compatible Demo Board AUXP.** Connected to the 5 V Input
       Power of the Raspberry Pi. Used to supply power to the demo board
       EEPROM.
   * - 2
     - Pin 3 (I2C1 SDA) :sup:`1`
     - **SDA.** PMBus Data from the Raspberry Pi to the demo board. Connected
       to I2C1 SDA.
   * - 3
     - GND
     - **Ground**
   * - 4
     - Pin 5 (I2C1 SCL) :sup:`1`
     - **SCL.** PMBus Clock from the Raspberry Pi to the demo board. Connected
       to I2C1 SCL.
   * - 5
     - 3V3 Power
     - **DC1613A-Compatible Demo Board LGKPWR.** Connected to the 3.3 V
       Regulator Output of the Raspberry Pi.
   * - 6
     - Pin 7 (GPIO4)
     - **ALERTB.** PMBus/SMBus Interrupt Signal from the demo board to the
       Raspberry Pi.
   * - 7
     - Pin 16 (GPIO23) :sup:`2`
     - **DC1613A-Compatible Demo Board GPIO_1.** Actual function depends on
       the demo board.
   * - 8
     - Pin 18 (GPIO24) :sup:`2`
     - **DC1613A-Compatible Demo Board GPIO_2.** Actual function depends on
       the demo board.
   * - 9
     - Pin 36 (GPIO16) :sup:`2`
     - **DC1613A-Compatible Demo Board OUTEN.** Enable Signal from the
       Raspberry Pi to the demo board.
   * - 10
     - GND
     - **Ground**
   * - 11
     - Pin 5 (I2C1 SCL) :sup:`1`
     - **DC1613A-Compatible Demo Board AUXEESCL.** I2C Clock from the
       Raspberry Pi to the demo board EEPROM.
   * - 12
     - Pin 3 (I2C1 SDA) :sup:`1`
     - **DC1613A-Compatible Demo Board AUXSDA.** I2C Data exchanged between
       the Raspberry Pi and the demo board EEPROM.

| :sup:`1` IO pins shared with the I2C Pmod Connector #1 (P3), the I2C Pmod
  Connector #2 (P4) and the QuikEval Demo Board Connector (P5).
| :sup:`2` IO pins normally disconnected from the Raspberry Pi. Short the
  appropriate solder pads between P10 and P11 to enable these pins.

Changing the Raspberry Pi GPIO Assignments
------------------------------------------

The :adi:`PMD-RPI-INTZ` maps the GPIO pins of the Raspberry Pi as shown in the
table below. For easy access to these signals, the evaluation board uses a
stacking header for the Raspberry Pi connector.

.. figure:: pmd-rpi-intz_rpi_connector.jpg
   :align: center
   :width: 500px

   Raspberry Pi 40-pin connector (P9)

.. list-table:: Raspberry Pi Connector (P9) Pinout
   :header-rows: 1
   :widths: 25 10 5 5 10 25

   * - Pin Function on the PMD-RPI-INTZ
     - GPIO Pin
     - Pin
     - Pin
     - GPIO Pin
     - Pin Function on the PMD-RPI-INTZ
   * - 3.3 V Power
     - 3V3 Power
     - 1
     - 2
     - 5V Power
     - 5 V Power
   * - I2C SDA
     - GPIO 2
     - 3
     - 4
     - 5V Power
     - 5 V Power
   * - I2C SCL
     - GPIO 3
     - 5
     - 6
     - Ground
     - Ground
   * - PMBus/SMBus ALERTB
     - GPIO 4
     - 7
     - 8
     - GPIO 14
     - No connection
   * - Ground
     - Ground
     - 9
     - 10
     - GPIO 15
     - No connection
   * - I2C Pmod #2 RESET
     - GPIO 17
     - 11
     - 12
     - GPIO 18
     - SPI Pmod #1 CS3
   * - I2C Pmod #2 INT
     - GPIO 27
     - 13
     - 14
     - Ground
     - Ground
   * - QuikEval Demo Board GPIO
     - GPIO 22
     - 15
     - 16
     - GPIO 23
     - DC1613A-Compatible Demo Board GPIO_1
   * - 3.3 V Supply Voltage
     - 3V3 Power
     - 17
     - 18
     - GPIO 24
     - DC1613A-Compatible Demo Board GPIO_2
   * - SPI MOSI
     - GPIO 10
     - 19
     - 20
     - Ground
     - Ground
   * - SPI MISO
     - GPIO 9
     - 21
     - 22
     - GPIO 25
     - SPI Pmod #2 INT
   * - SPI SCLK
     - GPIO 11
     - 23
     - 24
     - GPIO 8
     - SPI Pmod #1 CS1 & QuikEval Demo Board CS
   * - Ground
     - Ground
     - 25
     - 26
     - GPIO 7
     - SPI Pmod #2 CS1
   * - ID EEPROM SDA
     - GPIO 0
     - 27
     - 28
     - GPIO 1
     - ID EEPROM SCL
   * - SPI Pmod #2 CS2
     - GPIO 5
     - 29
     - 30
     - Ground
     - Ground
   * - SPI Pmod #2 CS3
     - GPIO 6
     - 31
     - 32
     - GPIO 12
     - SPI Pmod #2 RESET
   * - I2C Pmod #1 RESET
     - GPIO 13
     - 33
     - 34
     - Ground
     - Ground
   * - SPI Pmod #1 INT
     - GPIO 19
     - 35
     - 36
     - GPIO 16
     - DC1613A-Compatible Demo Board OUTEN
   * - I2C Pmod #1 INT
     - GPIO 26
     - 37
     - 38
     - GPIO 20
     - SPI Pmod #1 CS2
   * - Ground
     - Ground
     - 39
     - 40
     - GPIO 21
     - SPI Pmod #1 RESET

The adapter board is designed so that most of these IO signals pass through the
rows of test points and solder jumpers at the center. This way, if a different
set of GPIO pin assignments is needed (or desired), the default connections can
be changed by simply removing the appropriate solder jumper(s) and then placing
a wire between the test points of interest.

Refer to the pictures and tables below for the signal names available on each
test point. Raspberry Pi GPIO pins are connected to P8 and P10; PMD-RPI-INTZ
Pmod and demo board pins are connected to P7 and P11.

.. figure:: pmd-rpi-intz_gpio_jumpers.jpg
   :align: center
   :width: 400px

   GPIO jumper block P7/P8

.. list-table:: P8/P7 Jumper Assignments
   :header-rows: 1
   :widths: 10 15 10 30 10

   * - P8 Pin
     - Raspberry Pi GPIO
     - Jumper
     - PMD-RPI-INTZ Signal
     - P7 Pin
   * - 1
     - GPIO 4
     - JP2
     - PMBus/SMBus ALERTB
     - 1
   * - 2
     - GPIO 17
     - JP3
     - I2C Pmod #2 RESET
     - 2
   * - 3
     - GPIO 27
     - JP4
     - I2C Pmod #2 INT
     - 3
   * - 4
     - GPIO 22
     - JP5
     - QuikEval Demo Board GPIO
     - 4
   * - 5
     - GPIO 10
     - JP6
     - SPI MOSI
     - 5
   * - 6
     - GPIO 9
     - JP7
     - SPI MISO
     - 6
   * - 7
     - GPIO 11
     - JP8
     - SPI SCLK
     - 7
   * - 8
     - GPIO 5
     - JP9
     - SPI Pmod #2 CS2
     - 8
   * - 9
     - GPIO 6
     - JP10
     - SPI Pmod #2 CS3
     - 9
   * - 10
     - GPIO 13
     - JP11
     - I2C Pmod #1 RESET
     - 10
   * - 11
     - GPIO 19
     - JP12
     - SPI Pmod #1 INT
     - 11
   * - 12
     - GPIO 26
     - JP13
     - I2C Pmod #1 INT
     - 12

.. figure:: pmd-rpi-intz_gpio_jumpers_2.jpg
   :align: center
   :width: 400px

   GPIO jumper block P10/P11

.. list-table:: P10/P11 Jumper Assignments
   :header-rows: 1
   :widths: 10 15 10 30 10

   * - P10 Pin
     - Raspberry Pi GPIO
     - Jumper
     - PMD-RPI-INTZ Signal
     - P11 Pin
   * - 1
     - GPIO 14
     - JP14
     - No connection
     - 1
   * - 2
     - GPIO 15
     - JP15
     - No connection
     - 2
   * - 3
     - GPIO 18
     - JP16
     - SPI Pmod #1 CS3
     - 3
   * - 4
     - GPIO 23
     - JP17
     - DC1613A-Compatible Demo Board GPIO_1
     - 4
   * - 5
     - GPIO 24
     - JP18
     - DC1613A-Compatible Demo Board GPIO_2
     - 5
   * - 6
     - GPIO 25
     - JP19
     - SPI Pmod #2 INT
     - 6
   * - 7
     - GPIO 8
     - JP20
     - SPI Pmod #1 CS1 & QuikEval Demo Board CS
     - 7
   * - 8
     - GPIO 7
     - JP21
     - SPI Pmod #2 CS1
     - 8
   * - 9
     - GPIO 12
     - JP22
     - SPI Pmod #2 RESET
     - 9
   * - 10
     - GPIO 16
     - JP23
     - DC1613A-Compatible Demo Board OUTEN
     - 10
   * - 11
     - GPIO 20
     - JP24
     - SPI Pmod #1 CS2
     - 11
   * - 12
     - GPIO 21
     - JP25
     - SPI Pmod #1 RESET
     - 12

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

`PMD-RPI-INTZ Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/pmd-rpi-intz-designsupport.zip>`__

- Schematic
- PCB Layout
- Bill of Materials
- Allegro Project

Additional Information
----------------------

- :adi:`PMD-RPI-INTZ Product Page <PMD-RPI-INTZ>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
