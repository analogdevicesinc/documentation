| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ Isolated RS-232 Implementation
======================================

The Isolated RS-232 port is implemented using the ADM3252E Signal and Power isolated RS-232 transceiver. The :adi:`adm3252e` connects to UART3 of the ADSP-BF548 and is capable of functioning at data rates of up to 460kbit/s. Figure 1 below shows a circuit diagram of the implementation of the :adi:`adm3252e` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedrs-232.png
   :alt: Figure 1. Isolated RS-232 schematic
   :align: center
   :width: 600px

The VCC of the :adi:`adm3252e` is powered with 3.3V and will generate an isolated 3.3V on VISO using ADI’s *iso*\ Power technology.

A three pin screw terminal connector, J6 is used for easy access to the TOUT1(pin 2), RIN1(pin 3) and RS232_ISO_GND(Pin 1) connections. The jumper JP2 when fitted will connect the transmitter output(TOUT1) to the receiver input(RIN1), implementing a loopback feature.
