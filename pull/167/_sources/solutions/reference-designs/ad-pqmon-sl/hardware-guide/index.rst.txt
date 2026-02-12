.. _ad-pqmon-sl hardware-guide:

Hardware User Guide
===================

Introduction
------------

The :adi:`AD-PQMON-SL` provides a complete software and hardware
platform for prototyping and evaluating high performance class S polyphase
energy quality monitors. The design incorporates the :adi:`ADE9430`
high performance, polyphase energy monitoring IC that has an advanced metrology
feature set (total and fundamental active power, volt amperes reactive (VAR),
volt amperes (VA), watthour, VAR hour, VA hour, total and fundamental IRMS and
VRMS, power factor) and the :adi:`MAX32650` ultralow power ARM cortex-M4 
with FPU-based microcontroller with 3 MB flash and 1 MB SRAM. The :adi:`ADE9430` 
enables accurate energy monitoring over a wide dynamic range through its 
superior analog performance and digital signal processing (DSP) core. 
The :adi:`ADE9430` simplifies the implementation and certification 
of energy and power quality monitoring systems by providing tight
integration of acquisition and calculation engines. This solution can be used on
a 3-phase system or up to three single-phase systems.

The design also features the :adi:`MAX32650`, which is a part of a
new breed of low-power microcontrollers built to thrive in the rapidly evolving
Internet of Things (IoT) named DARWIN. These MCUs are smart, with the biggest
memories in their class and a massively scalable memory architecture. The MCU
exposes all the necessary debug and programming features to enable a complete
software development experience with the system. It is coupled with 512 Mb RAM
and 64 Mb flash external memories to provide flexibility. The system’s firmware
is based on ADI’s open-source no-OS framework and ADI proprietary ADSW-PQ-CLS
library.

.. figure:: main_components_3.jpg

   AD-PQMON-SL Main Components

Front-end
---------

.. figure:: input_stage.jpg
   :width: 600px

   AD-PQMON-SL Input Stage

The :adi:`AD-PQMON-SL` uses all seven second order Σ-Δ ADCs of the :adi:`ADE9430`. 
There are 4 current inputs and 3 voltage ones that can be seen in the following image. 
The fourth voltage input is used for NULL if it is the case or it is connected 
to the reference phase, see
:dokuwiki:`ADE9430 user guide </resources/eval/user-guides/ade9430#applying_the_ade9430_to_different_metering_configurations>`.

Current transformers (CT) for all four channels are provided with the kit. To
connect the current transformers provided with the kit, the connectors of the
current transformers must be replaced with the ones included in the box. The
center tapped burden resistors are calculated for the provided CTs.

If one decides to change the CTs, these resistances need to be recalculated and
replaced with the new values. The board is populated with 5.1 Ω resistances,
resulting a current transfer function for a 3000:1 current transformer ratio
equal with:

.. math::

   10.2 / 3000 = 0.0034 V rms/ A rms

The current gain in this case will be *3000 / 10.2 = 294.11* (the default value
in the firmware). If the burden resistances are changed the value of the current
gain has to be updated from the Scopy interface.

For the voltage input the voltage gain is computed considering the upper
resistance from the divider approximately 1 MΩ and the lower resistance equal
with 1 kΩ resulting a value of 1001. The voltage transfer function is:

.. math::

   (1 / (1000 + 1)) = 0.001 V rms

.. figure:: burden_resistors.jpg
   :width: 400px

   Burden Resistors for Current Transformers

.. figure:: current_transformer.jpg
   :width: 400px

   Current Transformer Connection

Power Supply
------------

The board can be supplied from the AC input through an isolated AC/DC converter
or from the USB through the :adi:`LTC3306`, a 1.75A Synchronous
Step-Down Regulator. A logic based on several :adi:`MAX40203`, an
Ultra-Tiny nanoPower, 1A Ideal Diodes with Ultralow-Voltage Drop, selects
based on availability the supply input with priority to the AC input.

The other 1.1V and 1.8V voltage rails needed by the MCU are converted from the
3.3V input by the :adi:`ADP225`, a Dual, 300 mA Adjustable Output,
Quick Output Discharge, Low Noise, High PSRR Voltage Regulator.

Isolation
---------

.. figure:: isolation_barrier.jpg

   AD-PQMON-SL Isolation Barrier

The solution has an on-board :adi:`ADuM6424A` Quad-Channel Isolator with 
Integrated DC-to-DC Converter. This DC-DC converter is used to supply all the 
components on the high voltage side. The :adi:`ADUM6424A` and the
:adi:`ADUM4152`, which is a 5 kV, 7-Channel, SPIsolator™ Digital
Isolator for SPI (with 1/2 Aux channel directionality), are used to isolate the
connection between the :adi:`ADE9430` and :adi:`MAX32650`.

In case the AC input is used to supply the board, the AC-DC flyback converter
isolates the two sides.

LED Indicators
--------------

There are 8 LEDs on the :adi:`PQMON <AD-PQMON-SL>` motherboard. Five of them
are on the ADE side and three on the isolated side. 

.. figure:: ade-leds.jpg
   :width: 400px

   LEDs on the ADE side

The five on the ADE side are connected as follows:

- LED1 - IRQ0 ADE
- LED2 - CF3/ZX ADE
- LED3 - CF4/DREADY ADE
- LED5 - 3V3 on the ADE side
- LED5 - IRQ1 ADE

.. figure:: mcu_leds.jpg
   :width: 400px

   LEDs on the MCU side

The three on the MCU side are connected as:

- DS1 - 3V3 MCU side
- DS2 - user led 0
- DS3 - user led 1

Daughter Board Expansion
------------------------

.. figure:: daughter_board.jpg 

   AD-PQMON-SL with Daughter Board

The add-on board includes a standalone interface (a 64 x 4 display, 2 LEDs,
and 5 buttons), an SD card for long time data logging, several
industrial connectivity ports, and exposes an I/O prototyping area for I2C, SPI,
GPIO, UART, 3V3, GND. The prototyping area can be also used for GPS / GNSS
(e.g., Accurate Synchrophasor Measurement) or for external control signals.

Conectivity Options
~~~~~~~~~~~~~~~~~~~

The following possibilities are available for industrial connectivity:

- T1L through the :adi:`ADIN1110`, an ultralow power, single port,
  10BASE-T1L transceiver design for industrial Ethernet applications
- RS-485 implemented using the :adi:`ADM2587E`, a 2.5 kV Signal and
  Power Isolated, ±15 kV ESD Protected, Full/Half Duplex RS-485 Transceiver 
  (500 kbps)
- Ethernet

System Setup
-------------

Single Phase Setup Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

For single phase testing, an example on how to connect the evaluation board can
be seen in the following images:

.. figure:: board.jpg

   AD-PQMON-SL Board for Single Phase Testing

A block schematic of the setup is provided in the following image.

.. figure:: single_phase_block_schematic.jpg
   :width: 600px

   Single Phase Block Schematic

An example of a cable assembly that replicates the block schematic connections
is presented in the following image. With this cable, tests can be made using
different loads.

.. figure:: cable_single_phase.jpg

   Cable Assembly for Single Phase Testing

The cable is connected to the board as shown in the following image.

.. figure:: single_phase_board_connection.jpg

   Single Phase Board Connection

Setup for Testing All Channels Using a Single-Phase Input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For testing all the channels provided by the :adi:`ADE9430`, the
following setup can be used.

.. figure:: single_phase_all_inputs.jpg

   Single Phase Setup for Testing All Inputs

The mains voltage can also be connected to the load if a switch with more poles
is used. With this setup one can observe the influence of the input power supply
and of different types of loads on the power quality.

For 3-phase setups, consult the :adi:`ADE9430` technical reference 
manual :dokuwiki:`here </resources/eval/user-guides/ade9430#applying_the_ade9430_to_different_metering_configurations>`.
