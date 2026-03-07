EV-COG-AGILE-900Z
=================

Features
--------

-  Small form factor (3.5 cm x 7.5 cm)
-  Sub-GHz mesh networking module on board
-  On-board debugging capability through the ARM® Mbed™ DAPLink software
-  Multiple test points to monitor current consumption
-  Multiple options to power up evaluation board
-  On-board sensors such as the SHT31 temperature sensor and an accelerometer for fast prototyping
-  Access to all GPIOs through expansion connectors

DESCRIPTION
-----------

The EV-COG-AGILE-900Z board deploys and tests custom applications built with the AgileNet-6T protocol, a sub-GHz mesh networking solution. The EV-COG-AGILE-900Z is an evaluation board with an EV-MOD-AGILE-900Z assembled on board. The EV-MOD-AGILE-900Z contains the ADuCM4050 microcontroller (MCU), an ultra low power, mixed-signal microcontroller system and the ADF7030-1, a low power, sub GHz radio.

FUNCTIONAL BLOCK DIAGRAM
------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig1_final.png
   :width: 400px

Figure.1

EVALUATION BOARD HARDWARE
-------------------------

The EV-COG-AGILE-900Z comes with the EV-MOD-AGILE-900Z assembled on board which provides multiple connectors, interfaces, buttons, and switches to power up, flash, and communicate with the EV-COG-AGILE-900Z board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig2_final.png
   :width: 400px

Figure.2 Primary Side of the EV-COG-AGILE-900Z

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig3_final.png
   :width: 400px

Figure.3 Secondary Side of the EV-COG-AGILE-900Z

EVALUATION BOARD COMPONENTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The components in the EV-COG-AGILE-900Z are distributed between the primary side and the secondary side of the board (see Figure 4 and Figure 5).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig4_final.png
   :width: 400px

Figure.4 Components on the Primary Side of the EV-COG-AGILE-900Z

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig5_final.png
   :width: 400px

Figure.5 Components on the Secondary Side of the EV-COG-AGILE-900Z

EV-MOD-AGILE-900Z MODULE
~~~~~~~~~~~~~~~~~~~~~~~~

The EV-MOD-AGILE-900Z consists of the ADuCM4050, a low power microcontroller, and the ADF7030-1, a low power sub-GHz radio. This module is connected to the EV-COG-AGILE-900Z through 51 castellation pins soldered to the board. These castellation pins are soldered to connect the universal asynchronous receiver/transmitter (UART), I2C, serial peripheral interface (SPI), and general purpose input/output (GPIO) lines of the EV-MOD-AGILE-900Z to the EV-COG-AGILE-900Z. The EV-COG-AGILE-900Z power supply is routed to the EV-MOD-AGILE-900Z. The EV-MOD-AGILE-900Z also has an MMCX antenna connector to attach an antenna.

POWER SUPPLY OPTIONS
~~~~~~~~~~~~~~~~~~~~

Depending on the end application of the customer, the EV-COG-AGILE-900Z can be powered on through a USB, battery, or external supply. A three-position switch, S7, is used to select the power supply (see Figure 6). The S7 configurations for the different power options are described in Table 1.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig6_final.png
   :width: 400px

Figure.6 Power Selection Switch

Table 1

The power sources can be used with or without the ADP5300 step-down regulator. The ADP5300 regulates the power supplied to the MCU, the radio, and components on the EV-COG-AGILE-900Z. The ADP5300 is configured to supply a constant 3 V output to the ADuCM4050 MCU processor and the ADF7030-1 radio. The bypass configurations for the different power options are described in Table 2.

Table 2

LEDs
~~~~

Power (PWR)
^^^^^^^^^^^

The power LED indicates the EV-COG-AGILE-900Z is powered on.

Reset (RSTLED)
^^^^^^^^^^^^^^

The reset LED indicates the ADuCM4050 is in reset. The reset occurs by pressing the RST push button.

Radio Reset (DS2)
^^^^^^^^^^^^^^^^^

The radio reset LED indicates the ADF7030-1 is in reset. The radio reset is controlled through firmware programmed into the board.

Mbed Power (MBED)
^^^^^^^^^^^^^^^^^

The Mbed power LED indicates power is supplied to the Arm® Mbed™ chip.

GPIO LEDs (DS1, DS3, DS4)
^^^^^^^^^^^^^^^^^^^^^^^^^

DS1, DS3, and DS4 are three LEDs connected to the GPIO pins of the ADuCM4050. The LEDs are active high and are turned on by driving logic 1. The pin mapping between the GPIOs and the LEDs is described in Table 3.

Table 3

SWITCHES
~~~~~~~~

Boot Mode Select (BOOT)
^^^^^^^^^^^^^^^^^^^^^^^

The BOOT push button determines the boot mode of the ADuCM4050 during reset. By default, the ADuCM4050 MCU processor boots from the internal flash memory.

Reset Push Button (RST)
^^^^^^^^^^^^^^^^^^^^^^^

The reset push button resets the ADuCM4050. RSTLED indicates the ADuCM4050 is in reset.

GPIO Push Button (BTN2)
^^^^^^^^^^^^^^^^^^^^^^^

The GPIO push button is connected to pin P1_12 of the ADuCM4050. The GPIO push button is available for user defined applications.

CONNECTORS
~~~~~~~~~~

MCU Debug Interface (P26)
^^^^^^^^^^^^^^^^^^^^^^^^^

P26 is a 0.05 inch 10-pin header that programs the ADuCM4050. The serial wire debug (SWD) lines of the ADuCM4050 are available through the 10-pin interface.

Shaker Connector (P10)
^^^^^^^^^^^^^^^^^^^^^^

P10 provides an interface to allow external sensors to connect to the MCU through the I2C protocol. The pinout of the shaker connector is as follows:

Table 4

Expansion Connectors (C1 and C2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The C1 expansion connector and C2 expansion connector provide signals from the SPI, UART, I2C, synchronous serial peripheral port (SPORT), and GPIO interfaces of the ADuCM4050. C1 and C2 are present on the bottom side of the board. These expansion connectors enable daughter boards to connect to the EV-COG-AGILE-900Z and enable the user to develop a variety of applications. The pinouts of the expansion connectors are seen in Fig 7, 8

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig7_final.png
   :width: 400px

Figure 7. Pinout of Expansion Connector C1

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig8_final.png
   :width: 400px

Figure 8. Pinout of Expansion Connector C2

SENSORS
~~~~~~~

For quick prototyping and development purposes, sensors are present onboard the EV-COG-AGILE-900Z. The SHT31 temperature sensor is present on the EV-COG-AGILE-900Z and can be used in user developed applications. A shunt jumper should be inserted in P9 to power up the sensor. SHT31 communicates with the ADuCM4050 through I2C0 lines.

SHUNT JUMPERS
~~~~~~~~~~~~~

The on-board jumpers multiplex GPIO lines for various functionalities. The shunt jumpers, or shunts, are 1.27 mm headers with shorted pins. By default, the shunt jumpers are inserted in the positions listed in Table 5

Table 5 To change the jumper settings, remove the shunt jumper from the default position and insert the jumper in the new position. The pin numbers are written on the silk screen.

JH1
^^^

JH1 connects VDD_MCU with VDD_MCU_B line to pull up the I2C lines and power any sensors connected via expansion connectors.

JH2
^^^

JH2 connects the power supply input to the regulator. The EV-COG-AGILE-900Z is not powered if the shunts are not inserted at JH2.

JH3
^^^

JH3 is a 4-pin header. Pin 1 and Pin 2 are shorted by default and connect VDD_MAIN to VDD_BOARD. Inserting shunts at Pin 3 and Pin 4 connects VDD_BOARD to GND.

JH4
^^^

JH4 is a 6-pin header that determines whether the ADP5300 is bypassed. Inserting shunts at Pin 1 and Pin 2 connects the output of the regulator to VDD_MAIN. Shunts at Pin 3 and Pin 4 bypass the regulator and connect EXT_VDD_IN to VDD_MAIN. Shunts at Pin 5 and Pin 6 bypass the regulator and connect VIN to VDD_MAIN. The ADP5300 should never by bypassed when the EV-COG-AGILE-900Z is powered through a USB supply.

JH5
^^^

JH5 is a 4-pin header that enables the Mbed chip. Shunts a Pin 1 and Pin 2 connect VDD_MAIN to VDD_MBED, which powers the Mbed chip.

JH6
^^^

Shunts at Pin 1 and Pin 2 route the Mbed chip signals to the ADuCM4050. If the shunts are removed, the Mbed chip routes the signals to P26. Connecting a 10-pin cable between P26 on EV-COG-AGILE-900Z and a supported external board allows the Mbed chip on the EV-COG-AGILE-900Z to program the external board.

JH9
^^^

Shunts at Pin 1 and Pin 2 power VDD_RF_H to VDD_MAIN. Removing the shunts disables the power supply to the ADF7030-1.

SOLDER JUMPERS
~~~~~~~~~~~~~~

Solder jumpers are shorted by soldering required points. There are five solder jumpers on the board. Four of the solder jumpers are located on the bottom side of the EV-COG-AGILE-900Z. To change a solder jumper using a hot soldering iron, melt a blob of solder and move the jumper to the new position.

Table 6

JP1
^^^

JP1 determines the routing of the GPIO28 and GPIO29 lines. By soldering Pin 1 and Pin 2, the GPIO28 and GPIO29 lines are routed to A_GPIO28 on the C1 expansion connector. By soldering Pin 2 and Pin 3, the GPIO28 and GPIO29 lines are routed to A_GPIO29 on P3.

JP2
^^^

JP2 determines the routing of the GPIO43 and GPIO27 lines. By soldering Pin 1 and Pin 2, the GPIO43 and GPIO27 lines are routed to A_GPIO43 on P2. By soldering Pin 2 and Pin 3, the GPIO43 and GPIO27 lines are routed to A_GPIO27 on P7.

JP4
^^^

JP4 routes the INT_WAKE2 line. By soldering Pin 1 and Pin 2, the INT_WAKE2 line is routed to the EXT_INT_WAKE2 line on the C1 expansion connector.

JP5
^^^

JP5 routes the SPI1_CS3 line. By soldering Pin 1 and Pin 2, the SPI1_CS3 line is routed to the EXT_SPI1_CS3 line on the C1 expansion connector.

JP6
^^^

JP6 determines the routing of the SWO line. By soldering Pin 1 and Pin 2, the SWO line is routed to the UART0_TXD line. By soldering Pin 2 and Pin 3, the SWO line is routed to the SPI1_CS0 line.

Other shunts
~~~~~~~~~~~~

P2
^^

By default, shunts are inserted at Pin 1 and Pin 2. P2 connects the on-board accelerometer or the RTC sensorstrobe line to a GPIO depending on shunt position.

P3
^^

P3 provides an option to mux the GPIO14 line for different functionalities. By default, shunts are inserted at Pin 1 and Pin 2 and Pin 7 and Pin 8. To support add on boards, the default position of P3 needs to be changed accordingly. For the EV-GEAR-EINK1Z add-on board, connect Pin 3 and Pin 4 instead of Pin 1 and Pin 2.

P4
^^

P4 enables the GPIO34 line to be used for different functionalities. By default, shunts are inserted at Pin 1 and Pin 2.

P7
^^

By default, shunts are inserted at Pin 1 and Pin 2. P7 connects one of two GPIOs (A_GPIO27 or GPIO12) to a GPIO mux depending on shunt position.

P8
^^

P8 is a UART header that provides an option to route the UART lines to different interfaces. The shunts are placed at Pin 1 and Pin 2 and Pin 7 and Pin 9 by default, which routes the UART lines from the Mbed chip to the UART lines to the ADuCM4050.

P9
^^

To power up the SHT31 temperature sensor, shunts must be inserted at P9.

CURRENT MEASURING TEST POINTS
-----------------------------

The EV-COG-AGILE-900Z enables a user to measure and profile the current consumption throughout board. The EV-COG-AGILE-900Z also enables the isolation of current consumption hotspots. The current measuring test points shown in Table 1 can be used with a digital multimeter to profile the current consumption. These test points measure the board level current, ADuCM4050 current, and ADF7030-1 radio frequency (RF) current.

Table 7

PROGRAMMING AND DEBUGGING THE EV-COG-AGILE-900Z
-----------------------------------------------

INSTALLING THE AGILENET-6T SOFTWARE PACKAGE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the AgileNet-6T software by filling in the request form at https://form.analog.com/form_pages/softwaremodules/SRF.aspx. Take the following steps after navigating to the software request form:

-  Fill in the requested information under the Software Recipient Information and Commercial information sections.
-  Under the Software requested section, set the options to the following values: Target hardware to Ultra Low Power Microcontrollers, Product Number to ADuCM4050, and select the AgileNet 6T checkbox for Software requested.
-  After the request is approved, a link to download the software is sent to the provided email address.

Use the link to install the AgileNet-6T software package.

PROGRAMMING THE EV-COG-AGILE-900Z BOARD via DAPLINK interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program the EV-COG-AGILE-900Z board with the binary (.bin) and hex (.hex) file formats provided in the provided in the AgileNet-6T software package by taking the following steps:

-  Make sure the antenna is connected to the EV-COG-AGILE-900Z board as shown in Figure 9. Note that excluding the antenna can damage the board.
-  To connect the EV-COG-AGILE-900Z evaluation board to the PC, connect the microUSB end of the USB to microUSB cable to the board, and connect the USB end to the PC. All the necessary drivers are downloaded when using the Windows® operating system (OS).
-  After the drivers are installed, a new drive named DAPLINK appears on the computer (see Figure 10). This virtual drive allows the user to reprogram the EV-COG-AGILE-900Z using a simple drag and drop method.
-  Open the DAPLINK drive and drag and drop the .hex file provided in the software package from the computer onto this drive.
-  After the file is copied, the file disappears and then reappears from the DAPLINK window. which indicates that the new firmware has been flashed.
-  Press the middle button labeled RST on the EV-COG-AGILE-900Z to reset the board and to run the new firmware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig9_final.png
   :width: 400px

Figure 9. The EV-COG-AGILE-900Z with an Antenna Connected

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig10_final.png
   :width: 400px

Figure 10. DAPLINK Drive

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig11_final.png
   :width: 400px

Figure 11. Flashing Through Drag-and-Drop Procedure

FLASHING ANOTHER BOARD USING THE EV-COG-AGILE-900Z
==================================================

The DAPLink interface can download firmware onto either the EV-COG-AGILE-900Z or onto an external board, such as the EV-MTE-AGILE-900Z, that is connected to P26 on the EV-COG-AGILE-900Z. The procedure to flash an external board is as follows:

-  Ensure both the EV-COG-AGILE-900Z and the external board are disconnected from any power source.
-  Connect a 10-pin ribbon cable between P26 on the EV-COG-AGILE-900Z and the equivalent 10-pin header on the external board.
-  Remove the jumper JH6 on the EV-COG-AGILE-900Z to redirect the MBED signals to P26.
-  Power up both boards and connect the EV-COG-AGILE-900Z board to a PC using a USB to microUSB cable
-  After the DAPLINK drive appears on the PC, perform the same drag and drop operation as detailed in Step 4 of the Programming Through DAPLink section.
-  After resetting the board by pressing the on-board button labeled RST, reinstall the JH6 jumper that was removed in Step 3 to flash the EV-COG-AGILE-900Z board at any later point.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-agile-900z/fig12_final.png
   :width: 400px

Figure 12 Flashing a Different Board Using the EV-COG-AGILE-900Z

Additional resources
--------------------

:doc:`AgileNet-6T wiki page </wiki-migration/resources/eval/user-guides/agilenet6t>`
