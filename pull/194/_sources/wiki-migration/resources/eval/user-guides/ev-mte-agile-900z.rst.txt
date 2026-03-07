EV-MTE-AGILE-900Z
=================

Features
--------

-  Small form factor (2.5 cm × 7.2 cm) for remote node deployment
-  Multiple options to power up evaluation board
-  LEDs and buttons to develop custom applications
-  SPI, UART, and I2C communication interfaces through castellations to enable a variety of applications

Description
-----------

The EV-MTE-AGILE-900Z board deploys and tests custom applications built with the AgileNet-6T protocol, a subGHz mesh networking solution. The EV-MTE-AGILE-900Z evaluation board is embedded with the EV-MOD-AGILE-900Z board and can be used to develop a wide variety of applications.

The EV-MOD-AGILE-900Z evaluation board contains the ADuCM4050 microcontroller (MCU), an ultra low power, mixed-signal microcontroller system. The MCU provides digital peripheral interfaces such as an I2C interface and multiple serial peripheral interfaces (SPIx where x is the SPI number). The EV-MOD-AGILE-900Z evaluation board also contains the ADF7030 radio, a subGHz radio chip for a variety of applications.

Functional block diagram
------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig_1_final.png
   :width: 400px

Figure.1

EVALUATION BOARD HARDWARE
-------------------------

The EV-MTE-AGILE-900Z evaluation board consists of a module portion, the EV-MOD-AGILE-900Z evaluation board, with an MCU processor and radio. There is also a breakoff portion provided that helps in flashing the MCU and provides multiple options to power up the board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig2_final.png
   :width: 400px

Figure.2 Front Side of the EV-MTE-AGILE-900Z Board

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig3_final.png
   :width: 400px

Figure.3 Back Side of the EV-MTE-AGILE-900Z Board

EVALUATION BOARD COMPONENTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig4_final.png
   :width: 400px

Figure.4 EV-MTE-AGILE-900Z Evaluation Board Components

POWER SUPPLY OPTIONS
~~~~~~~~~~~~~~~~~~~~

The EV-MTE-AGILE-900Z can be powered on in the following two ways: battery power and external power. Both the battery power and external power sourced can be used with or without the ADP5300 regulator. The ADP5300, the ultra low power step-down regulator, is present on the evaluation board and regulates the power supplied to the MCU and radio. The ADP5300 is configured to supply a constant 3 V output to the ADuCM4050 MCU processor and ADF7030 radio.

Different power configurations can power up the EV-MTE-AGILE-900Z evaluation board. The user can select the powering options by placing jumper shunts on the 1.27 mm headers (P7). The configuration of the jumper shunts for different power options are described in Table 1.

Table 1

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig5_final.png
   :width: 400px

Figure 5. Default Power Jumper for Powering BT1

LEDs
~~~~

The evaluation board contains a power LED and three GPIO LEDs that are described in the Power section and the GPIO LEDs section.

Power
^^^^^

The power LED (DS4) is lit if the EV-MTE-AGILE-900Z board is powered on.

GPIO LEDs
^^^^^^^^^

Three LEDs (DS1, DS2, DS3) are connected to the general-purpose input/output (GPIO) pin of the ADuCM4050 processor. The LEDs are active high and are turned on by writing a 1 to the corresponding GPIO lines. The pin mapping between the GPIOs and LEDs is described in Table 2.

Table 2

Switches
~~~~~~~~

Boot Mode Select (S2)
^^^^^^^^^^^^^^^^^^^^^

The push-button switch (see Figure 6) determines the boot mode of the ADuCM4050 processor. Table 3 shows the available boot mode settings. By default, the processor boots from the internal flash memory.

Table 3

Reset Push-Button (S3)
^^^^^^^^^^^^^^^^^^^^^^

The reset push-button resets the ADuCM4050 processor when pressed.

GPIO Push-Button (S1)
^^^^^^^^^^^^^^^^^^^^^

The GPIO push-button is connected to the pin of the ADuCM4050 processor, P2_10.

UART HEADERS
~~~~~~~~~~~~

To enable the user to easily download the firmware to the EV-MTE-AGILE-900Z evaluation board, UART lines are provided to the MCU through 1.27 mm headers. UART lines can also be used to monitor the program execution and to send commands from the PC to the MCU on the EV-MTE-AGILE-900Z board. The pin description of the 1.27 mm P9 header is shown in Table 4.

Table 4

RF INTERFACE
~~~~~~~~~~~~

The RF signal is brought outside of the board through either the on-board MMCX connector (see Figure 6 and Figure 7), or through the castellations (see Figure 6 and Figure 8), depending on the capacitor configuration.

To route the RF signal through the MMCX connector, connect Capacitor C34 as shown in Figure 7, and leave Capacitor C33 unconnected. To route the RF signal to the castellations, Capacitor C33 must be connected and Capacitor C34 must be open (see Figure 8).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig6_final.png
   :width: 400px

Figure.6 Switch Positions and RF Castellations

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig7_final.png
   :width: 400px

Figure.7 Capacitor Connection to Route RF Signal to the MMCX Connector

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig8_final.png
   :width: 400px

Figure.8 Capacitor Connection to Route RF Signal to Castellations

PINOUT OF THE MODULE
~~~~~~~~~~~~~~~~~~~~

From the module portion of the EV-MTE-900Z board, the EV-MOD-AGILE-900Z board (see Figure 9), a total of 51 pins are accessible through castellations to allow the user to develop a wide variety of applications using the EV-MTE-AGILE-900Z evaluation board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig9_final.png
   :width: 400px

Figure.9 EV-MOD-AGILE-900Z Evaluation Board

The pinout of the EV-MOD-AGILE-900Z evaluation board is shown in Figure 10.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig10_final.png
   :width: 400px

Figure.10 EV-MOD-AGILE-900Z Pinout

Table 5 provides more information about the pins that are accessible through castellations.

Table 5

PROGRAMMING AND DEBUGGING OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing the AgileNet-6T Software Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download the AgileNet-6T software package by filling in the software request form at https://form.analog.com/form_pages/ softwaremodules/SRF.aspx. Take the following steps after navigating to the software request form:

-  Fill in the requested information under the Software Recipient Information and Commercial information sections.
-  Under the Software requested section, set the options to the following values: Target hardware to Ultra Low Power Microcontrollers, Product Number to ADuCM4050, and select the AgileNet 6T checkbox for Software requested.
-  After the request is approved, a link to download the software is sent to the provided email address.
-  Use the link to install the AgileNet-6T software package.

Programming the EV-MTE-AGILE-900Z via the EV-COG-AGILE-900Z
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The EV-MTE-AGILE-900Z board can be programmed via the EV-COG-AGILE-900Z board. To program the EV-MTE-AGILE-900Z board with a hexadecimal/binary file provided in the software package, use the following steps:

-  Make sure both boards are disconnected from any power source. The USB cable must be disconnected from the EV-COG-AGILE-900Z board and the battery must be removed from the EV-MTE-AGILE-900Z board.
-  Install a ribbon cable between the 10-pin header (P26) on EV-COG-AGILE-900Z board and the 10-pin header on the EV-MTE-AGILE-900Z board (P6). Figure 13 shows how to connect the two boards.
-  Remove Jumper JH6 from the back of the EV-COG-AGILE-900Z board. Removing the jumper instructs the EV-COG-AGILE-900Z to program an external board (the EV-MTE-AGILE-900Z board in this case) instead of the on-board module.
-  Power up the two boards. Connect the EV-COG-AGILE-900Z board to a PC using a USB to microUSB cable and connect the battery to the EV-MTE-AGILE-900Z board.
-  After connecting the EV-COG-AGILE-900Z board to the PC, all the necessary drivers are automatically downloaded when using the Windows® operating system (OS).
-  After the drivers are installed, a new drive called DAPLINK appears on the PC. This is a virtual drive the EV-COG-AGILE-900Z creates to allow the user to reprogram the board by using a simple drag and drop method.
-  Drag and drop the required firmware image (.hex file), provided in the software package, from the PC onto the DAPLINK drive. Figure 12 shows the file transfer window that opens during the drag and drop procedure to show the status of the file transfer.
-  After the firmware image file is copied to the drive, it disappears and then reappears, indicating that the new firmware is ready to run on the EV-MTE-AGILE-900Z evaluation board.
-  Press the reset button on the EV-COG-AGILE-900Z board (labeled RST) to reset the board and load the new firmware.
-  After resetting the board, reinstall the JH6 jumper (removed in Step 3) to flash the EV-COG-AGILE-900Z board at any later point.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig11_final.png
   :width: 400px

Figure.11 DAPLINK Drive

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig12_final.png
   :width: 400px

Figure.12 Drag and Drop Procedure Window

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev_mte_agile_900z/fig13_final.png
   :width: 400px

Figure.13 Connecting the EV-MTE-AGILE-900Z Evaluation Board to the EV-COG-AGILE-900Z Evaluation Board

Additional resources
--------------------

:doc:`AgileNet-6T wiki page </wiki-migration/resources/eval/user-guides/agilenet6t>`
