.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0537

.. _eval-cn0537-ardz:

EVAL-CN0537-ARDZ
=================

Smoke Detector Reference Design Based on ADPD188BI Integrated Optical Module.

Overview
--------

The :adi:`EVAL-CN0537-ARDZ <CN0537>` is the evaluation board for the
:adi:`CN0537`, a smoke detector reference design based on the
:adi:`ADPD188BI` Integrated Optical Module. Intended to ease development of
smoke detection algorithms and systems, the hardware can be interfaced
directly with the :adi:`EVAL-ADICUP3029` (and other standard Arduino
form-factor development boards) without the need for additional sensors or
signal conditioning.

Since the 1970s, smoke detectors have become a staple in commercial and
residential buildings. The photoelectric type uses a light source aimed at an
angle away from a photodetector and checks for an increase in photodetector
current. New standards such as ANSI/UL-217 and ANSI/UL-268 place more complex
requirements on modern smoke detector designs, including the ability to
accurately distinguish real threats from nuisance sources such as cooking and
bathroom steam. The use of the :adi:`ADPD188BI` makes this significantly
simpler to implement.

.. figure:: cn0537_board.png
   :align: center

   EVAL-CN0537-ARDZ Evaluation Board

Included with the evaluation board is application software for the
:adi:`EVAL-ADICUP3029` which can be used to stream blue and IR data from the
:adi:`ADPD188BI` and save them to a micro-SD card.

Connectors and Jumper Configurations
-------------------------------------

Selecting the Communications Interface (JP1 to JP6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADPD188BI` is capable of communicating using either I2C or SPI.
Short jumpers JP1 to JP2 to connect the I2C lines to the device. Likewise,
short jumpers JP3 to JP6 to connect the SPI lines. Open jumpers corresponding
to the unused lines.

.. figure:: cn0537_comms_select.png
   :align: center

   Communications Interface Jumper Selection (JP1 to JP6)

.. figure:: cn0537_comms_table.jpg
   :align: center

   Communications Interface Jumper Settings

By default, the EVAL-CN0537-ARDZ is configured to use the SPI communication
interface.

Selecting the I2C Address of the Temperature/Humidity Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default on-board temperature/humidity sensor uses I2C communication. Select
the I2C address using JP7.

.. figure:: cn0537_i2c_addr.png
   :align: center

   I2C Address Selection (JP7)

.. figure:: cn0537_jp7_table.png
   :align: center

   JP7 Settings

By default, the I2C address of the temperature/humidity sensor is set to 0x44
(pins 2 and 3 of JP7 are shorted).

Alarm LED, Buzzer and Test Button (DS1, U6 and S1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These components can be used to signal an alarm when smoke is detected by the
:adi:`ADPD188BI`. The LED can be turned on by writing a 0 on pin 3 of
connector P4. The buzzer can be sounded by writing a 1 on pin 1.

.. figure:: cn0537_alarm.png
   :align: center

   Alarm Components

The pin assignments can be changed depending on the settings of JP14/JP15 (for
the LED) and JP16/JP17 (for the buzzer).

The push button S1 can be used to test the alarm. Pressing this button sets pin
3 of connector P4 to 0, turning the LED on. With the demo software running,
pressing and holding S1 for at least 5 seconds will also trigger the buzzer.

GPIO Pin Assignments (JP12 to JP19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some GPIO pin assignments on the EVAL-CN0537-ARDZ can be changed using jumpers
JP14 to JP19, giving the user the option of using the unused pins for other
purposes.

.. figure:: cn0537_gpio.png
   :align: center

   GPIO Pin Assignment Jumpers (JP12 to JP19)

.. figure:: cn0537_gpio_table.png
   :align: center

   GPIO Jumper Settings

Host Processor Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Arduino form factor connectors (P1, P2, P3, P4) provide the interface to
the host processor. When evaluating the EVAL-CN0537-ARDZ, ensure that the chip
select and GPIO pins used by the board are not shared with other hardware.

.. figure:: cn0537_connectors.png
   :align: center

   Host Processor Connectors (P1 to P4)

Smoke Detector Demo Software
------------------------------

The ``ADuCM3029_demo_cn0537`` project provides a solution to implement a smoke
detector with the capability to pass UL-217 specification, using the
EVAL-CN0537-ARDZ and the :adi:`EVAL-ADICUP3029`.

Demo Requirements
~~~~~~~~~~~~~~~~~

**Hardware**

- :adi:`EVAL-ADICUP3029`
- EVAL-CN0537-ARDZ
- Micro USB to USB cable
- PC or laptop with a USB port

**Software**

- Smoke Detector Demo Software (hex file)
- Serial terminal program (e.g. PuTTY or Tera Term)

Hardware Setup
~~~~~~~~~~~~~~

#. Set up the EVAL-CN0537-ARDZ jumpers as described in the connector
   configuration section above.
#. Connect the EVAL-CN0537-ARDZ board to the EVAL-ADICUP3029 via the Arduino
   form factor connectors.
#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer.

Programming the Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~

Connect both boards together through the Arduino form factor connectors and
plug them into a computer through USB. Upon connection, the hardware should
appear as a DAPLINK drive on the computer. Drag and drop the
``ADuCM3029_demo_cn0537.hex`` file to the DAPLINK drive to program the
ADICUP3029.

Software Operation
~~~~~~~~~~~~~~~~~~~

The application has two main stages: initialization and main process.

During initialization, the software modules and part drivers are instantiated
and set to initial values. The application initializes the CLI process on the
UART, sets up the ADPD188BI for smoke detection measurements, reads
calibration data, and initializes the alarm algorithm.

The main process has two modes of operation:

- **Idle mode**: The serial CLI can be used to alter functionality parameters
  such as ADPD188BI registers and output data rate. The CLI can also be used
  to set up SD card logging.
- **Streaming mode**: Smoke data is taken at the set sampling rate. After
  temperature compensation and Power Transfer Ratio (PTR) calculation, data is
  fed to the algorithm to determine the alarm state. If the alarm is triggered,
  the buzzer is activated and can only be reset by pressing the button on the
  shield or using the ``reset_alarm`` command.

Available CLI Commands
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 60 30

   * - Command
     - Description
     - Example
   * - ``h``
     - Display available commands
     -
   * - ``s <no>``
     - Stream data from the device. Optionally specify number of samples.
     - ``s 100``
   * - ``i <opt>``
     - Stop the stream. 1 = idle mode, 0 = stop streaming only.
     - ``i 1``
   * - ``ms <opt>``
     - Set output mode. CODE for codes, PTR for PTR data.
     - ``ms PTR``
   * - ``os <odr>``
     - Set output data rate.
     - ``os 2.45``
   * - ``og``
     - Get current output data rate.
     -
   * - ``ra``
     - Stop the alarm if triggered.
     -
   * - ``ar``
     - Redo algorithm initialization.
     -
   * - ``hc <opt>``
     - Heater control. 1 = on, 0 = off.
     - ``hc 1``
   * - ``fo <name>``
     - Open/create a file on the SD card.
     - ``fo file1``
   * - ``fc``
     - Close and save the last opened file on the SD card.
     -
   * - ``rr <addr>``
     - Read a device register (address in hex).
     - ``rr a``
   * - ``rw <addr> <val>``
     - Write a device register (address and value in hex).
     - ``rw a 12c``
   * - ``rd``
     - Read and display all device registers.
     -

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   `EVAL-CN0537-ARDZ Design & Integration Files
   <https://www.analog.com/cn0537-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information and Useful Links
-----------------------------------------

- :adi:`CN0537 Product Page <CN0537>`
- :adi:`ADPD188BI Product Page <ADPD188BI>`
- :adi:`ADP151 Product Page <ADP151>`
- :adi:`LT8410 Product Page <LT8410>`
- :adi:`EVAL-ADICUP3029 Product Page <EVAL-ADICUP3029>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the :ez:`/`.
