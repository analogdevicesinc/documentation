.. _ad-m2kcompedu-ebz:

AD-M2KCOMPEDU-EBZ
=================

Overview
--------

The :adi:`AD-M2KCOMPEDU-EBZ` is an :adi:`ADALM2000` companion board for 
hands-on electronics education. It combines a standalone arbitrary waveform
generator, onboard supplies, adjustable references, sensing, user controls,
display support, and CAN communication into one compact USB-powered platform.

.. figure:: AD-M2KCOMPEDU-EBZ_top-angle-evaluation-board.png
  :align: center
  :width: 600px

  AD-M2KCOMPEDU-EBZ Board

Features
--------

- USB-C input Power Supply port with 900 mA on-board current limit
- Arduino UNO R4 plug-in option
- ADALM 2K / Discovery plug-in option
- ±12 V on-board power supply generators with foldback current limit
- Two selectable +3.3 V supply sources: Arduino +3.3 V rail or on-board local LDO
- 2x DC Reference Voltage Generators VREF adjustable in a range of ±12 V, buffered, and
  22 mA output current limited
- 1x DC Reference Current Generator IREF adjustable in a range of 360 µA up to 60 mA
  sourced from a 12 V supply rail
- 2Ch Audio amplifier with adjustable gain
- 1x IR port (1x IR LED + 1x IR Phototransistor)
- 1x LDR Photoresistor (10-30 kΩ)
- 1x Temperature sensor with a 5 mV/K PTAT output voltage characteristic
- 4x Trimmer, multi turn: 2 kΩ, 5 kΩ, 10 kΩ, and 100 kΩ
- 6x Switch: 4 sliding + 2 tactile (3 with + 3 without Debounce)
- 7+1 red LEDs (7.1 segments display layout with series resistors)
- Standard CAN transceiver
- On-board Sin/Tri/Square wave Signal Generator (SPI and I2C controls)

  - Sine and Triangle frequency range: 10 Hz to 2 MHz; Square wave frequency range: 100
    Hz to 2 MHz

    - Amplitude range: 0.1 V to 10 V, software limited

  - Output DC offset range: ±10 V, software limited

- On-board PWM Generator with LED indicator, providing 5 V TTL output on the CLK/PWM
  and :math:`\overline{CLK/PWM}` pins

  - Frequency values 1Hz…2 MHz

- Display: Monochrome OLED, 128 x 64 Pixels
- Rotary encoder with push-to-click
- Graphical User Interface / Menu
- Breadboard 400
- Accessories:

  - 1x USB-A to USB-C 3A cable (1m)
  - 1x Trim Screwdriver
  - Jump wires

Applications
------------

- Classroom electronics labs
- :adi:`ADALM2000`-based teaching and demonstrations
- Mixed-signal signal-chain demonstrations
- Student projects and prototyping
- Embedded control and communication exercises
- University, technical faculty, and hobbyist maker learning environments

System Architecture
-------------------

.. figure:: block-diagram.png
  :align: center
  :width: 600px

  LM2K Companion board Block Diagram

.. figure:: Electronic-Board-Silkscreen-Floorplan.png
  :align: center
  :width: 600px

  LM2K Companion electronic board silkscreen and floorplan

Resources
---------

- :adi:`AD9833 Product Page <AD9833>`
- :adi:`AD5443 Product Page <AD5443>`
- :adi:`AD5625R Product Page <AD5625R>`
- :adi:`AD8065 Product Page <AD8065>`
- :adi:`AD8066 Product Page <AD8066>`
- :adi:`ADA4077-1 Product Page <ADA4077-1>`
- :adi:`ADA4511-2 Product Page <ADA4511-2>`
- :adi:`LT3092 Product Page <LT3092>`
- :adi:`ADM1177-2 Product Page <ADM1177>`
- :adi:`ADM7150 Product Page <ADM7150>`
- :adi:`AD8532 Product Page <AD8532>`
- :adi:`TMP01 Product Page <TMP01>`
- :adi:`ADG444 Product Page <ADG444>`
- :adi:`MAX33042 Product Page <MAX33042>`

Support
-------

For questions and more information, please contact us on the :ez:`EngineerZone`.

.. toctree::
  :maxdepth: 1
  :glob:

  hardware-guide/index