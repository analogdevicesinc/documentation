SDP-K1 Hardware Description
===========================

This describes the hardware design of the EVAL-SDP-CK1Z board.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-k1/k1_top_labelled.png
   :width: 600px

Figure 1: SDP-K1 Board

LEDs
----

There are six LEDs located on the SDP-K1 board. Refer to Figure 1.

Connector Details
-----------------

The SDP-B board contains one identical Hirose FX8-120P-SV1(91), 120 pin header, connector and one Arduino Uno header. The peripheral communication lines of the STM32F469NIH6 microcontroller are exposed through these.

Arduino Uno Header Details
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Arduino Uno header supports the following peripherals:

-  SPI
-  I\ :sup:`2`\ C
-  GPIO
-  UART
-  Timers

SDP Connector Details
~~~~~~~~~~~~~~~~~~~~~

The 120-pin SDP connector supports the following peripherals:

-  SPI
-  I\ :sup:`2`\ C
-  GPIO
-  UART
-  Timers
-  SPORT
-  QSPI

Also, included on the connector specifications are input and output power pins, ground pins, and pins reserved for future use.

For further details on the peripheral interfaces, including timing diagrams, see the `STM32F469NIH6 Processor Hardware Reference <https://www.st.com/resource/en/datasheet/stm32f469ae.pdf>`__

Connector Pin Assignments
-------------------------

.. _sdp-connector-details-1:

SDP Connector Details
~~~~~~~~~~~~~~~~~~~~~

Figure HWD2: 120 Pin Connector Outline

Pin Sharing
~~~~~~~~~~~

SB!SB!SB!SB!

Power
~~~~~

Daughter Board Design Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connector Location
~~~~~~~~~~~~~~~~~~

Keep Out Area
~~~~~~~~~~~~~

Restriction on Right Angle Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mechanical Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~
