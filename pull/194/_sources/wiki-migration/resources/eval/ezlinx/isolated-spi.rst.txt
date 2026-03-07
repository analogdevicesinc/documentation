| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`
| ====== ezLINX™ Isolated SPI Implementation======

Two Isolated SPI ports are implemented using the :adi:`adum3401` and the :adi:`adum3402` *i*\ Coupler signal isolators and the :adi:`adum5000` *iso*\ Power Isolated DC to DC converter. The :adi:`adum3401` of the isolated SPI1 is connected to SPI0 of the ADSP-BF548. The :adi:`adum3402` is used for isolating the SPI slave select lines. Figure 1 below shows a circuit diagram of the implementation of Isolated SPI1 using the :adi:`adum3401`, :adi:`adum3402`, and :adi:`adum5000` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedspi1.png
   :alt: Figure 1. Isolated SPI1 schematic
   :align: center
   :width: 900px

To connect Isolated SPI1 as a master, connect jumpers JP5, JP7, JP9, JP11, JP13, JP15, JP21 and JP36 while leaving jumpers JP6, JP8, JP10, JP12, JP14, JP16, JP20 and JP37 open. To connect Isolated SPI1 as a slave, connect jumpers JP6, JP8, JP10, JP12, JP14, JP16, JP20 and JP37 while leaving jumpers JP5, JP7, JP9, JP11, JP13, JP15, JP21 and JP36 open. When connecting SPI1 as a slave, connecting JP20 enables the slave select and serial clock inputs on the :adi:`adum3402`.

These jumper settings are given in the table below:

+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|             | JP5     | JP6     | JP7     | JP8     | JP9     | JP10    | JP11    | JP12    | JP13    | JP14    | JP15    | JP16    | JP20    | JP21    | JP36    | JP37    |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| SPI1 Master | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Open    | Connect | Connect | Open    |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| SPI1 Slave  | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Connect | Open    | Open    | Connect |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

| 

The :adi:`adum3401` of the isolated SPI2 is connected to SPI2 of the ADSP-BF548. The :adi:`adum3402` is used for isolating the SPI slave select lines. Figure 2 below shows a circuit diagram of the implementation of Isolated SPI2 using the :adi:`adum3401`, :adi:`adum3402` and :adi:`adum5000` on the *ez*\ LINX hardware.

.. image:: https://wiki.analog.com/_media/ezlinx/isolatedspi2.png
   :alt: Figure 2. Isolated SPI2 schematic
   :align: center
   :width: 900px

To connect Isolated SPI2 as a master, connect jumpers JP22, JP24, JP26, JP28, JP30, JP32, JP35 and JP38 while leaving jumpers JP23, JP25, JP27, JP29, JP31, JP33, JP34 and JP39 open. To connect Isolated SPI2 as a slave, connect jumpers JP23, JP25, JP27, JP29, JP31, JP33, JP34 and JP39 while leaving jumpers JP22, JP24, JP26, JP28, JP30, JP32, JP35 and JP38 open. When connecting SPI2 as a slave JP34 should also be connected, enabling the slave select and serial clock inputs on the :adi:`adum3402`.

These jumper settings are given in the table below:

+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|             | JP22    | JP23    | JP24    | JP25    | JP26    | JP27    | JP28    | JP29    | JP30    | JP31    | JP32    | JP33    | JP34    | JP35    | JP38    | JP39    |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| SPI2 Master | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Open    | Connect | Connect | Open    |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| SPI2 Slave  | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Open    | Connect | Connect | Open    | Open    | Connect |
+-------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

| 
| VDD1 of the :adi:`adum3401`, :adi:`adum3402` and VDD1 of the :adi:`adum5000` are powered by 3.3V. The :adi:`adum5000` will generate an isolated 3.3V and is used to supply power to VDD2 of the :adi:`adum3401` and :adi:`adum3402`.

Two seven pin screw terminal connectors, J10 and J25 are used for easy access to the SPISCK (Pin 1), SPIMOSI (Pin 2), SPISEL1/SPISS (Pin 3), SPIMISO (Pin 4). SPISEL2 (Pin 5), SPISEL3 (Pin 6) and SPI_ISO_GND (Pin 7).
