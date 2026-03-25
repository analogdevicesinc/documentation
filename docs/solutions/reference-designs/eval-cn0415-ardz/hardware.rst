.. _eval-cn0415-ardz hardware:

Hardware Guide
==============

This section describes the hardware configuration and connector settings for
the :adi:`EVAL-CN0415-ARDZ <CN0415>` evaluation board.

Power Supply Requirements
--------------------------

The CN0415 requires a power supply voltage between 6 V and 24 V. The current
requirement can be as high as 3 A, depending on the solenoid's DC resistance.

Solenoid Requirements
----------------------

A Deltrol model
`TAU0730T-02 <https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/412_Web.pdf>`__
12 V solenoid is provided with the CN0415 as an example. In general, CN0415
will drive any solenoid actuator with an operating voltage of 24 V or less and
an operating current of 3 A.

.. figure:: images/cn0415_solenoid_interface.png
   :align: center
   :width: 500

   Solenoid Interface

When driving low-voltage solenoids from a high input supply voltage, solenoid
current can be limited in software and by adjusting the overcurrent latch-off
threshold set by R10-11.

.. figure:: images/cn0415_oc_threshold.png
   :align: center
   :width: 500

   Overcurrent Threshold Configuration

LED Indicators
--------------

.. list-table::
   :header-rows: 1

   * - LED
     - Initial State
     - Description
   * - DS1
     - ON
     - Indicates that the LT4367 supply input voltage is within range
   * - DS2
     - OFF
     - Indicates input overvoltage fault (turns on when input exceeds 24 V)
   * - DS3
     - ON
     - Indicates +3.3 V voltage source from the Arduino MCU board
   * - DS4
     - ON
     - Indicates +VCC voltage source to the system (from +3.3 V Arduino or
       +5 V LT3433 output, set by JP3)

.. figure:: images/cn0415_power_led.png
   :align: center
   :width: 500

   Power and LED Indicators

ADC Chip Select Jumper Pin Selection (P2)
------------------------------------------

The chip select jumper settings allow the user to stack multiple boards on the
microcontroller board when using SPI digital communication protocol.

.. figure:: images/cn0415_chip_select.png
   :align: center
   :width: 500

   Chip Select Jumper Configuration

.. list-table::
   :header-rows: 1

   * - Jumper Name
     - Position
     - Description
   * - P2
     - 1 and 2
     - Set the chip select to P6-3 of the Arduino MCU GPIO pin terminal
   * - P2
     - 3 and 4
     - Set the chip select to P6-2 of the Arduino MCU GPIO pin terminal
   * - P2
     - 5 and 6
     - Set the chip select to P6-1 of the Arduino MCU GPIO pin terminal

PWM Jumper Pin Selection (P34)
-------------------------------

The PWM jumper pin selection allows the user to choose from the GPIO pins of
the microcontroller to generate the excitation rectangular pulse which drives
the N-channel MOSFET gate driver.

.. figure:: images/cn0415_pwm_select.png
   :align: center
   :width: 500

   PWM Jumper Configuration

.. list-table::
   :header-rows: 1

   * - Jumper Name
     - Position
     - Description
   * - P34
     - 1 and 2
     - Set the PWM output from P7-7 of the Arduino MCU GPIO pin terminal
   * - P34
     - 3 and 4
     - Set the PWM output from P7-6 of the Arduino MCU GPIO pin terminal
   * - P34
     - 5 and 6
     - Set the PWM output from P7-4 of the Arduino MCU GPIO pin terminal

Other Configuration Options
-----------------------------

Default positions are indicated.

.. list-table::
   :header-rows: 1
   :widths: 25 10 15 50

   * - Board Function
     - Jumper
     - Position
     - Description
   * - Current Monitor Offset
     - JP1
     - 1 and 2
     - ADC Midscale (2.048 V)
   * -
     - JP1
     - 2 and 3 (default)
     - 0 V
   * - ADC Selection
     - JP2
     - 1 and 2
     - Current Monitor to Arduino ADC
   * -
     - JP2
     - 2 and 3 (default)
     - Current Monitor to onboard ADC
   * - Vcc Supply Selection
     - JP3
     - 1 and 2 (default)
     - Vcc supply from +5 V on board LDO
   * -
     - JP3
     - 2 and 3
     - Vcc supply from +3.3 V Arduino pin
   * - Burst-Mode Selection
     - JP5
     - 1 and 2 (default)
     - Disabled Burst-Mode functionality
   * -
     - JP5
     - 2 and 3
     - Enabled Burst-Mode functionality
   * - HW Fault Detection (Input)
     - P6
     - 1 and 2 (default)
     - Enable hardware fault detection via LED
   * -
     - P6
     - 2 and 3
     - Disable hardware fault detection
   * - HW Fault Detection (Output)
     - P7
     - 1 and 2
     - Enable hardware fault detection via LED
   * -
     - P7
     - 2 and 3 (default)
     - Disable hardware fault detection
   * - Overcurrent Latch Off
     - JP8
     - 1 and 2 (default)
     - Latch off enabled
   * -
     - JP8
     - 2 and 3
     - Latch off disabled
   * - Arduino ADC Channel
     - P10--P15
     - P10 (default)
     - Select Arduino analog input for current monitor
   * - OC/UC Select
     - P21--P22
     - P22 (default)
     - Select fault polarity (overcurrent or undercurrent)
   * - Logic Signal Control
     - P32, P36
     - P32
     - Disable on Fault
   * -
     -
     - P36 (default)
     - Always Enabled
   * - Output Enable
     - P26--P28
     - P26
     - Always Enabled
   * -
     -
     - P27
     - GPIO/Software control
   * -
     -
     - P28 (default)
     - Disable on Fault
   * - Arduino Vref
     - P9
     - Open
     - Short to set Arduino Vref to 4.096 V
   * - ADC CS
     - P2
     - 1 and 2 (default)
     - GPIO to use for ADC CS

Arduino Interface
-----------------

The EVAL-CN0415-ARDZ is compatible with the :adi:`EVAL-ADICUP3029` platform.
Because the ADICUP3029 is an Arduino form factor compatible development board,
many other equivalent Arduino form factor development boards can also be used
by writing custom code.

.. figure:: images/cn0415_arduino_interface.png
   :align: center
   :width: 500

   CN0415 Arduino Connector Pinout
