Embedded Linux
==============

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

Theoretical content
~~~~~~~~~~~~~~~~~~~
This workshop targets freshmen and second year students with a passion for electronics and electrical engineering, feeding their needs for an overview
of what this domain look like.

The purpose and structure are adapted to their knowledge and introduces them into the wonders of Electronics and chips.

- theoretical background for instrumentation devices
- ADALM2000 board overview, features, description
- ADALM2000 connectivity
- Scopy software overview and instruments description

*What is Software Defined Instrumentation?*

A single device encapsulating more instruments used for measurements, signal generation, signal acquisition, etc., powered by a PC open-source software that allows the user to customize the measurements, since the software is residing more on the host PC/mobile device instead of on the instrument.

Bonus: it has a pocket size!

.. figure:: ../workshops_software_defined_instrumentation/sdi_1.png
   :align: center

   SDI then vs now

`ADALM2000`

The ADALM2000 (M2K) Advanced Active Learning Module is an affordable USB-powered data acquisition module, that can be used to introduce fundamentals of electrical engineering in a self or instructor lead setting.

With 12-bit ADCs and DACs running at 100 MSPS, brings the power of high-performance lab equipment to the palm of your hand, enabling electrical engineering students and hobbyists to explore signals and systems into the tens of MHz without the cost and bulk associated with traditional lab gear.

When coupled with Analog Devices' Scopy™ graphical application software running on a computer, provides the user with high performance instrumentation.

.. figure:: ../workshops_software_defined_instrumentation/m2k.png
   :align: left

.. figure:: ../workshops_software_defined_instrumentation/scopy.png
   :align: center

   M2k and Scopy software

Hands-on activity
~~~~~~~~~~~~~~~~~

By the end of this lab, you will learn:

- How to use a desktop Oscilloscope and Signal generator channels by operating a Network Analyzer, as well as Digital Pattern generator
- How to interface an analog front end simple circuit with M2K channels
- How to generate and display signals with the lab tools Analog Devices provides

**Activities**

- breadboard Low-Pass filter implementation, two stages,
- Bode plot visualisation,
- usage of power supplies and scope inputs
- SPI communication with ADALP2000 AD5626 part, DAC converter,
- usage of Pattern Generator SPI interface and Scope channels for analog signals

**Pre-requisites**

- :git-plutosdr-m2k-drivers-win:`ADALM2000 drivers installation <releases+>`
- :git-scopy:`Install Scopy software <releases/tag/v1.4.1+>`

**Demo 1 - Scope and Signal generator channels – Cascaded LP filters**

*Materials*

- ADALM2000 Active Learning Module
- Solder-less breadboard, and jumper wire kit
- 2 x 1 KΩ resistors
- 2 x 0.1 uF capacitors (marked 104)

**First Stage Filter**

*Hardware setup*

Steps:

1. Connect the Scope Channel 2 after the first RC group and do a single sweep
2. Take a signal snapshot to preserve the result as a reference
3. Connect the Scope Channel 2 after the second RC stage and perform another sweep

.. figure:: ../workshops_software_defined_instrumentation/demo1waves1.png
   :align: center

   Results for Bode Diagram

**Demo 2 - Digital Pattern Generator and Scope – AD5626 component – SPI controlled and analog signal visualized using Scope**

*Materials*

- ADALM2000 Active Learning Module
- Solder-less breadboard
- Jumper wires
- 1 - AD5626 12-bit nanoDAC
- 1 x 2.2 KΩ resistor
- 1 x 0.001 uF capacitor(marked 102)
- 1 x 0.1 uF capacitor(marked 104)
- 1 x 10 uF capacitor

*Theory of operation*

   Schematic and Breadboard connections

Steps:

- Connect the Vp power supply to the Vdd of the chip, set it to 5V

- Connect the GND pin to the GND of the M2K

- Beware not to connect the supply pins of the chip to the positive power of ADALM2000 and GND in a reversed order!

- Connect the digital pins to the corresponding chip pins as shown in the schematic.

- Configure the SPI interface in pattern generator to match the timing diagram of the AD5626 datasheet.

*Pattern generator signals*

- DIO0 - /CS

- DIO1 – SCLK

- DIO2 – SDIN

- DIO3 - /LDAC

- DIO4 - /CLR

   SPI messages

*Scopy instruments setup*

- Open Scope instrument and connect Scope channel 1 to output pin of the AD5626 (pin 8 of the IC)
- Enable the positive 5V Power supply
- Set some values in the Data control of the pattern generator SPI configurator
- Enable Channel 1 measurements to view the analog values
- Change the initially transmitted values

Slide Deck and Booklet
~~~~~~~~~~~~~~~~~~~~~~

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

.. ADMONITION:: Download

   :download:`Software Defined Instrumentation Slide Deck <../workshops_software_defined_instrumentation/SDI_Workshop_2023.pptx>`

A complete booklet of the hands-on activity is also provided, either as a companion to
following the tutorial yourself:

.. ADMONITION:: Download

  :download:`Software Defined Instrumentation Booklet <../workshops_software_defined_instrumentation/SDI_Booklet.docx>`

Takeaways
~~~~~~~~~~~

ADALM2000 is a very versatile tool suited to use in various applications:

Lab setups

Advanced measurements

Learning platforms

Research


Resources
~~~~~~~~~~~

* :ref:`m2k`

*ADALM2000 Wiki*

* :dokuwiki:`university/tools/m2k`
* :dokuwiki:`university/tools/m2k/accessories/bnc`
* :dokuwiki:`university/tools/m2k/accessories/power`

*ADALM2000 Lab Activities*

* :dokuwiki:`university/courses/electronics/labs`

*Virtual classroom*

* :ez:`community/university-program`