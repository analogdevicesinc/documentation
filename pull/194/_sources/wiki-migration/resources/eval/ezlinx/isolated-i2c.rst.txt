| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`
| ====== ezLINX™ Isolated I2C Implementation======

The Isolated I2C port is implemented using the :adi:`ADuM1250` I2C Isolator and :adi:`ADuM5000` *iso*\ Power Isolated DC to DC converter. The :adi:`ADuM1250` connects to TW1 of the ADSP-BF548 and is capable of functioning at a maximum frequency of 1MHz. Figure 1 below shows a circuit diagram of the implementation of the :adi:`ADuM1250` and :adi:`ADuM5000` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedi2c.png
   :alt: Figure 1. Isolated I2C schematic
   :align: center
   :width: 600px

VDD1 of the :adi:`ADuM1250` and VDD1 of the :adi:`ADuM5000` are both powered by 3.3V. The ADuM5000 will generate an isolated 3.3V which is used to supply power to VDD2 of the :adi:`ADuM1250`.

A three pin screw terminal connector, J22, is used for easy access to the SDA (Pin 1), SCL (Pin 2) and I2C_ISO_GND (Pin 3) connections.
