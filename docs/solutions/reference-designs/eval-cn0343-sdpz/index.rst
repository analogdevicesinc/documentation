.. _eval-cn0343-sdpz:

EVAL-CN0343-SDPZ
=================

Ultrasonic Distance Measurement System.

Overview
--------

The :adi:`CN0343` is a completely self-contained distance sensor that utilizes
an ultrasonic transmitter and sensitive analog receiver in conjunction with a
precision analog microcontroller to provide distance measurements. The CN0343
approximate range is from 50 cm to 10 m with a resolution of about 2 cm.
Temperature compensation is provided by the integrated temperature sensor and
analog-to-digital converter (ADC) contained in the :adi:`ADuC7126`
microcontroller.

The CN0343 can run in standalone mode or connect multiple CN0343 units into one
RS-485 network to make group measurements.

Required Equipment
------------------

- EVAL-CN0343-EB1Z evaluation board
- :adi:`EVAL-CFTL-6V-PWRZ <EVAL-CFTL-6V-PWRZ>` +6 V power supply or
  equivalent
- PC with USB interface (optional, for firmware development)
- `SEGGER J-Link debug probe
  <https://www.segger.com/products/debug-probes/j-link>`__ (optional, for
  firmware programming)
- `Keil Embedded Development Tools <http://www.keil.com/>`__ IDE (optional, for
  custom firmware)

Hardware Connections
--------------------

The CN0343 has three connectors:

- **J1** -- Power supply connector
- **J2** -- RS-485 communication interface connector
- **J3** -- :adi:`ADuC7126 <ADUC7126>` JTAG/SWD debug interface connector

.. figure:: cn0343_connectors.png
   :align: center

   CN0343 board connector locations

Power Supply Connections
~~~~~~~~~~~~~~~~~~~~~~~~

The CN0343 **J1** connector is used for the power supply with the
:adi:`EVAL-CFTL-6V-PWRZ <EVAL-CFTL-6V-PWRZ>`. Before powering on the CN0343,
make sure all the necessary connectors are connected well and firm.

RS-485 Interface Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **J2** connector on the CN0343 is used for the RS-485 communication
interface. The CN0343 RS-485 interface works in half-duplex mode; only one
twisted pair cable is needed to build the RS-485 network.

.. figure:: cn0343_rs485.png
   :align: center

   CN0343 RS-485 connector (J2) pin mapping

.. note::

   The RS-485 interface has limitations on the total number of devices in the
   same network and cable type and length. For details on CN0343 RS-485
   interface characteristics, refer to the :adi:`ADM3483` data sheet.

JTAG/SWD Connections
~~~~~~~~~~~~~~~~~~~~

The **J3** connector on the CN0343 is used for the :adi:`ADuC7126 <ADUC7126>`
MCU JTAG debug and firmware programming. The CN0343 **J3** JTAG 20-pin 0.1
inch pitch connector pinout is compatible with the `SEGGER J-Link debug probe
<https://www.segger.com/products/debug-probes/j-link>`__.

.. figure:: cn0343_jtag.png
   :align: center

   CN0343 JTAG/SWD connector (J3) pin mapping

Usage Instructions
------------------

The CN0343 user interface consists of one LCD screen and one buzzer for
information output, and six tactile buttons for user input.

LCD Screen and Buttons User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CN0343 LCD has a contrast adjustment potentiometer **R1**.

The CN0343 has six tactile buttons: **UP**, **DOWN**, **LEFT**, **RIGHT**,
**OK**, and **CANCEL**.

.. tip::

   In this section, *press button* or *button pressed* means a single click of
   the tactile button.

.. figure:: cn0343_usage.png
   :align: center

   CN0343 LCD, buttons, and contrast potentiometer (R1)

.. note::

   If the CN0343 powers up with the beep and the LCD screen appears murky or
   dull, adjust **R1** with a screwdriver gently to make the LCD clear.

The CN0343 has the following running states:

**SPLASH**
   When powered up, the CN0343 enters the SPLASH state. The screen displays::

      ANALOG DEVICES
      EVAL-CN0343-EB1Z

   .. tip::

      At the SPLASH state the CN0343 will not respond to any button press or
      RS-485 input. Wait for 3 seconds and the CN0343 will enter the MEASURING
      state.

**MEASURING**
   At MEASURING state, the CN0343 displays::

      Distance: 1.253m
       Temp: 25.2 C

   The distance and temperature values vary based on the CN0343 operating
   conditions.

**MENU**
   If the **OK** button is pressed in the MEASURING state, the CN0343 enters
   the MENU state. The MENU state displays one of the following screens::

      Calibrate
          Temperature?

   ::

      Set address?

   ::

      Set baud rate?

**SETTINGS**
   If the **OK** button is pressed in the MENU state, the corresponding setting
   state is entered. At any SETTINGS state, the screen displays a blinking
   cursor.

Button Function Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 15 15 15 20 20

   * - Button
     - SPLASH
     - MEASURING
     - MENU
     - SETTINGS
   * - **UP**
     - none
     - none
     - previous item
     - increase number at cursor
   * - **DOWN**
     - none
     - none
     - next item
     - decrease number at cursor
   * - **LEFT**
     - none
     - none
     - previous item
     - move cursor left
   * - **RIGHT**
     - none
     - none
     - next item
     - move cursor right
   * - **OK**
     - none
     - enter MENU
     - enter selected SETTING
     - save and return to MENU
   * - **CANCEL**
     - none
     - none
     - return to MEASURING
     - don't save and return to MENU

RS-485 Interface
~~~~~~~~~~~~~~~~

The CN0343 software-supported RS-485 address range is 1--255 (this is not
equal to the :adi:`ADM3483` hardware-limited device count).

The CN0343 software-supported RS-485 baud rate range is 75 bps to 250 kbps.

.. important::

   If you use multiple CN0343 units in the same RS-485 network, make sure all
   the CN0343 units and the host have the same RS-485 baud rate and no address
   conflicts. Because the CN0343 operates in half-duplex RS-485 mode, make sure
   only one RS-485 device transmits data at a time.

The CN0343 responds to the following command:

.. code-block:: none

   xxx query\r\n

where ``xxx`` is the CN0343 decimal address, and ``\r\n`` is the return
characters.

For example:

.. code-block:: none

   109 query

will trigger the CN0343 with RS-485 address 109 to send the measurement result
data to the RS-485 network.

.. important::

   Do not omit the space character between the address ``109`` and the
   ``query`` command.

Software Programming
--------------------

The CN0343 software is developed using the `Keil Embedded Development Tools
<http://www.keil.com/>`__ and debugged with `SEGGER J-Link Debug Probes
<https://www.segger.com/products/debug-probes/j-link/>`__. For details on
using Keil or J-Link, refer to the links above.

Software Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After downloading and installing the `Keil Embedded Development Tools for ARM
<http://www.keil.com/>`__, open the Keil software IDE.

.. figure:: keil_open.png
   :align: center

   Opening the CN0343 project in Keil IDE

To open the CN0343 source code in Keil IDE:

#. Click the **Open** button.
#. Enter the CN0343 source code folder path.
#. Select the file type filter to **Project files \*.uvproj**.
#. Double-click the **V5.0.uvproj** file.

For details on Keil usage, refer to the `ARM Product Manuals
<http://www.keil.com/support/man_arm.htm>`__.

Downloading Firmware to the CN0343
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After software development, to download the binary firmware to the internal
flash of :adi:`ADuC7126 <ADUC7126>`:

.. figure:: keil_download.png
   :align: center

   Building and downloading firmware in Keil IDE

#. Click the **Build All** button. Wait for the build to finish.
#. Click the **Load** button. Wait for the download to finish.

Software Structure
~~~~~~~~~~~~~~~~~~

The following is the directory structure of the CN0343 software package:

.. code-block:: none

   V5.0
   +-- source/
   |   +-- applications/
   |   |   +-- dialog/
   |   |   |   +-- AddressDialog.cpp
   |   |   |   +-- BaudRateDialog.cpp
   |   |   |   +-- CalibrateTemperatureDialog.cpp
   |   |   |   +-- HomeDialog.cpp
   |   |   |   +-- SetDialog.cpp
   |   |   |   +-- Wnd.cpp
   |   |   +-- main.cpp
   |   |   +-- Message.cpp
   |   |   +-- Options.cpp
   |   |   +-- UARTCommand.cpp
   |   +-- bios/
   |   |   +-- ADuC7126Bits.cpp
   |   |   +-- ADuC712x.s
   |   |   +-- Exceptions.cpp
   |   |   +-- Initial.cpp
   |   |   +-- Interrupt.cpp
   |   |   +-- Retarget.cpp
   |   |   +-- UART.cpp
   |   +-- drivers/
   |   |   +-- ADCDriver.cpp
   |   |   +-- BuzzerDriver.cpp
   |   |   +-- KeyDriver.cpp
   |   |   +-- LCDDriver.cpp
   |   |   +-- PWMDriver.cpp
   |   |   +-- RTOSTimer.cpp
   |   |   +-- UARTDriver.cpp
   |   +-- include/
   |       +-- applications/
   |       +-- bios/
   |       +-- Drivers/
   |       +-- library/
   +-- V5.0.uvproj

Documents
---------

- :adi:`CN0343 Circuit Note <CN0343>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0343-EB1Z Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0343-DesignSupport.zip>`__

   - Schematics
   - Gerber Files
   - PADS Layout
   - Bill of Materials
   - Source Code

Additional Information
----------------------

- :adi:`ADuC7126 Product Page <ADUC7126>`
- :adi:`ADM3483 Product Page <ADM3483>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
