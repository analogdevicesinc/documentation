SHARC Audio Module User Interface Fin
=====================================

The :doc:`SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module>` User Interface Fin is designed to add more user interface options to the SAM platform.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/ui_fin_top.jpg
   :width: 600px

It provides the following features:

-  On-board Arduino compatible Micro-controller
-  3.5" 320*RGB*480 TFT LCD
-  2 rotary encoders
-  2 instrumental level 1/4" audio jack
-  ADXL345 3-axis accelerometer
-  TWI EEPROM

Additional features implemented by the Arduino:

-  USB to MIDI bridge
-  Emulated potentiometer

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

To be published on GitHub.

1/4" Instrument Interfaces
--------------------------

The User Interface fin includes stereo 1/4" input and output jacks, as found on Audio Project Fin. These signals are routed to the AUX input and HP output interfaces on the ADAU1761 audio codec.

LCD
---

The User Interface fin features a 3.5" 320x480 TFT LCD, connected to SC589's ePPI, allowing display motion images at 60Hz. The LCD need to be initialized via the SPI to function properly. On the User Interface fin, by default it would be initialized by the on-board microcontroller. However user may also initialize it using SAM's GPIO.

\*\* LCD to SAM connections \*\*

============ ==============
``LCD SCK``  Port C, Pin 09
``LCD DI``   Port C, Pin 11
``LCD CSn``  Port C, Pin 08
``LCD RSTn`` Port B, Pin 10
============ ==============

*ePPI connections are not shown since there is no pin multiplexing options. Refer to schematics for details.*

Accelerometer
-------------

The User Interface fin features a 3-axis accelerometer (ADXL345) on the board. It can be accessed using TWI at address 0x1D.

Rotary encoder
--------------

The User Interface fin has 2 on-board rotary encoder. For the SAM, there are two ways to access them:

-  Access them using the TWI. Both can be accessed using TWI at address 0x20. It would return the delta value since last read.
-  Access them using the HADC. An analog voltage representing the position would be present on the HADC line/ This allows software written to work with potentiometer on the Audio Project fin to utilize the rotary encoder on the User Interface fin.

USB-MIDI Bridge
---------------

The User Interface Fin has a USB Micro B port. By default the MCU would function as a USB-MIDI bridge, allowing the SAM to be connected to PC as a MIDI instrument. The MIDI IN and OUT signals are routed to UART2 on the ADSP-SC589 (Note this is different from that on the Audio Project Fin, which uses UART1 for MIDI). MIDI events can be generated on any of the three cores using the UART_Simple driver in the baremetal framework.

Few changes are required to make Baremetal SDK to use the UART2 as MIDI interface:

In the system.svc for Core 0, enable the pinmux for UART2.

In bm_uart.h, set UART_AUDIOPROJ_DEVICE_MIDI to UART2.

Linux Support
-------------

The LCD can be used as a framebuffer device under SAM Linux.

Source code based on CCES Linux Addin 1.3.0 can be found at the GitHub repository of the User Interface Fin.

Arduino-compatible Microcontroller
----------------------------------

The expansion fin has one on-board microcontroller (MCU) for USB-to-MIDI bridge, initializing the LCD, and reading the rotary encoder.

The core design is compatible with Arduino Micro (Arduino Leonardo), except running at 3.3V / 8MHz rather than 5V / 16MHz.

Normally, the MCU firmware will be installed by the POST automatically, and the user doesn't need to reprogram the MCU. These information are provided in case user want to modify the firmware.

SAM connections
~~~~~~~~~~~~~~~

The following table shows how the MCU is connected to the SAM (ADSP-SC589):

============ ==============
``AVR RST``  Port C, Pin 07
``AVR SCK``  Port C, Pin 09
``AVR MOSI`` Port C, Pin 11
``AVR MISO`` Port C, Pin 10
``AVR SSEL`` Port B, Pin 09
``AVR PB4``  Port C, Pin 08
``AVR PB5``  Port B, Pin 10
``AVR PB6``  HADC VIN0
``AVR PC7``  HADC VIN1
``AVR PD0``  TWI1 SCL
``AVR PD1``  TWI1 SDA
============ ==============

GPIO connectiosn
~~~~~~~~~~~~~~~~

The following table shows how on-board devices are connected to the MCU (numbers in the parentheses are Arduino numbering):

============ ================
``LCD CSn``  PB4 (Digital 8)
``LCD RSTn`` PB5 (Digital 9)
``LCD SCK``  PB1 (Digital 15)
``LCD DI``   PB2 (Digital 16)
``TWI SCL``  PD0 (Digital 3)
``TWI SDA``  PD1 (Digital 2)
``SW1 A``    PF0 (Analog 5)
``SW1 B``    PF1 (Analog 4)
``SW1 PB``   PF2 (Analog 3)
``SW2 A``    PF3 (Analog 2)
``SW2 B``    PF4 (Analog 1)
``SW2 PB``   PF5 (Analog 0)
``PWM B``    PB6 (Digital 10)
``PWM A``    PC7 (Digital 13)
============ ================

Programming
~~~~~~~~~~~

The on-board MCU requires a bootloader to be flashed into its internal memory before it can be programmed by the Arduino IDE. This process can be done by running the POST, and it only need to be done once. Once that's done, the on-board MCU can be directly programmed by the Arduino IDE through the on-board Micro USB port.

Arduino Board Support
~~~~~~~~~~~~~~~~~~~~~

It is necessary to install the SparkFun Pro Micro BSP to use the board. In the Arduino Preferences, add the following URL to the third-party board library list:

https://raw.githubusercontent.com/sparkfun/Arduino_Boards/master/IDE_Board_Manager/package_sparkfun_index.json

Install the SparkFun AVR Boards package.

USB to MIDI
~~~~~~~~~~~

The USB to MIDI can be implemented by using the MIDIUSB library provided in the Arduino IDE. The library can be installed by using the Library Manager in the Arduino IDE.

LCD Initialization
~~~~~~~~~~~~~~~~~~

The LCD uses 9-bit SPI rather than 8-bit, which is not supported by the MCU. Bit-banging SPI is then required to interface with the LCD.

The MCU handles LCD initialization through SPI. Once the initialization is done, it will check PB0 (connected to SAM PB9). If it is low, it will continue to clear the screen and display a SAM logo on the screen. If it is high, it will set the LCD to receive pixel from SAM's PPI.

Note: If the PPI pixel transfer is somehow interrupted (for example, a reset), the LCD need to be reinitialized as well. This can be done by resetting the MCU by pulling RST (SAM PC7) low.

.. _rotary-encoder-1:

Rotary Encoder
~~~~~~~~~~~~~~

The Encoder library is used to interface with rotary encoders. The TimerOne library is used to use timer interrupts. The MCU will keeps polling the encoder to update status. The SAM can read the result from the MCU at a lower speed.

PWM DAC
~~~~~~~

Reading encoder value from TWI isn't hard, but that's not something supported by the Baremetal Framework out-of-the-box. Sometimes when just experimenting with different settings, using HADC to read a potentiometer would be easier as the framework has built-in support for that. Many of the demos written for the Baremetal Framework also utilize the potentiometer. Reading rotary encoder value with HADC is supported on the User Interface fin. User can use it as if it is a potentiometer. This is achieved by using the on-board MCU to output a voltage that can be then read by the HADC. The MCU doesn't have a DAC builtin, so PWM output + first order RC filter is used.

I2C Slave
~~~~~~~~~

Wire library (installed by default) is used to transfer data to the SAM over I2C slave port. Two callback functions are used to receive and transmit data to the host.
