SHARC Audio Module Audio Project Fin
====================================

The :doc:`SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module>` Audio Project Fin is designed to support various DIY audio and music projects.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-diy-top.png
   :width: 400px

\*\* The Audio Project Fin \*\*

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/diy_fin_annotated.png
   :width: 400px

\*\* Block Diagram of the Audio Project Fin*\*

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   SHARC Audio Module Audio Project Fin Design and Integration Files

   
   -  `Schematics (PDF) <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/adi_diy_fin_schematics_v3.21.pdf>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/adi_diy_board_v3.21_bom.xlsx>`_
   -  `CAD Files (EAGLE format) <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/adi_audio_proj_v3.21_eagle_files.zip>`_
   


1/4" Instrument Interfaces
--------------------------

The Audio Project fin includes stereo 1/4" input and output jacks. These signals are routed to the AUX input and HP output interfaces on the ADAU1761 audio codec.

MIDI Interfaces
---------------

The Audio Project Fin includes MIDI IN, OUT and THRU connectors. The MIDI IN and OUT signals are routed to UART1 on the ADSP-SC589. MIDI events can be generated on any of the three cores using the UART_Simple driver in the baremetal framework.

Pushbuttons
-----------

The Audio Project Fin includes four pushbuttons (SW1-4). These buttons can be accessed from any of the three cores although by default they're managed by the ARM core. The pushbuttons can also be routed to external switches, such as those mounted to the chassis of a stomp box, using the expansion header. These signals already contains pull-up resistors and de-bouncing logic so the SW1-4 connectors on the expansion header can be connected directly to an external switch with no additional components.

\*\* Push button GPIO connections \*\*

======= ==============
``SW1`` Port E, Pin 08
``SW2`` Port E, Pin 09
``SW3`` Port E, Pin 10
``SW4`` Port E, Pin 12
======= ==============

POTS / HADC
-----------

The Audio Project Fin includes three POTs which connect to the Housekeeping ADC (HADC) on the ADSP-SC589. Four additional analog inputs are available in the expansion header which connect to HADC3-6. These signals are buffered via unity gain, non-inverting op-amp circuit that also provides a low-pass filter around 1KHz. This expansion header also includes 3.3V and GND so this three pin connector (described in more detail below in the Expansion Header section) can be connected directly to a Pot.

Power Supplies and Prototyping Area
-----------------------------------

The Audio Project Fin includes a local 5V linear regulator which is available on the prototyping area and also used to power the MIDI circuitry. There is also a 9V linear regulator that is used to power the analog input and output circuits between 1/4" jacks and the ADAU1761. See the schematics for more information.

LEDs
----

There are a total of 8 LEDs on the Audio Project Fin. An LED is located below each push button which can be used to indicate when certain effects are active, for example. There are also four additional LEDs configured as a VU meter in the prototyping area.

\*\* Push-button LEDs GPIO connections \*\*

==================== ==============
``LED6 (under SW1)`` Port E, Pin 03
``LED5 (under SW2)`` Port E, Pin 02
``LED4 (under SW3)`` Port E, Pin 01
``LED3 (under SW4)`` Port E, Pin 00
==================== ==============

\*\* VU Meter LEDs GPIO connections \*\*

======================= ==============
``LED7 (bottom of VU)`` Port E, Pin 04
``LED8``                Port E, Pin 05
``LED9``                Port E, Pin 06
``LED10 (top of VU)``   Port E, Pin 07
======================= ==============

In addition to the LEDs on the Audio Project Fin, there is also a connection to four external LEDs in the Expansion Header which is described in more detail below. These

\*\* External LEDs GPIO connections \*\*

======= ==============
``P15`` Port D, Pin 04
``P14`` Port D, Pin 05
``P13`` Port D, Pin 06
``P12`` Port D, Pin 07
======= ==============

Expansion Header
----------------

A small expansion header is provided to connect to external LEDs, POTs, push buttons and MIDI interfaces that might be located on a stomp box or rack-mount chassis. The diagram below shows which signals the pins on this header connect to.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/diy_fin_-_expansion_header.png
   :align: center
   :width: 400px

--------------

`Main Board#..hardware|Hardware Reference#.class-d|Class-D Amplifier Module <https://wiki.analog.com/_media/navigation SHARC Audio Module#.main-board>`_
