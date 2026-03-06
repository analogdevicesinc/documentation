ADALM1000 Breadboard Adapters
=============================

All of the analog connections to the ADALM1000 learning module are made though the 6/8 pin single row female header (0.1" centers) connector. The 6/8 pin female header provides +5 V and +2.5 V power supplies along with two ground connection points in the center of the header. The two analog input / output pins are on the two outside end pins. A very simplified block diagram of one of the analog channels is shown in figure 1. There are two additional optional input only pins that are not populated on the standard 6 pin header (rev D board), shown with white circles around them in figure 2. The user can optionally populate these extra two pin locations to separate the analog output and input functions which by default share the common analog channel pin. There are extra switches not shown in the figure 1 diagram which allow the voltage measuring "oscilloscope" hardware ( volt meter in diagram ) to be brought out along with the 1 MΩ input load resistor to a separate pin from the analog output source. Note figure 3 extracted from revision D schematic.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_analog_input_f1.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 1 ALM1000 analog input/output diagram


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/m2k-convert-f1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2 Analog I/O connector (left Rev D, right Rev F)


.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3 Detail of analog input switching


As we can see from figure 3 switch S\ :sub:`1` disconnects the CH A/B pins from the output drivers, putting that channel in the high impedance mode. Normally, S\ :sub:`4` is closed connecting the analog input buffer ( voltmeter in figure 1 ) to the CH A/B pins. It is also important to note that the white circle pin(rev D) and AIN/BIN pins (Rev F) is connected to CH A/B when S\ :sub:`4` is closed. If S\ :sub:`4` is opened then the analog input buffer is disconnected from the CH A/B pins and is now only available at the pin with the white circle and AIN/BIN pins.

This female 6/8 pin header is a very common, generic style connector and is simple to attach wires to as with the various cables supplied in the kit. Double length square male pins can serve as gender changers to convert the female end of the wires into male pins that can be easily inserted into the female header and the solder-less breadboards often used in the lab for building prototype circuits. These fly-wires are several inches long and can be awkward to use at times given the relatively small size and light weight of the ADALM1000 module and a small solder-less breadboard.

Adapter board
-------------

A more convenient arrangement would be an adapter PC board that connects to the female connector of ALM1000 and slips over the end of the breadboard connecting the two power supplies and ground to the four common rails of the breadboard. An example 1" by 2" adapter PC board layout is shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f4.jpg
   :align: center
   :width: 160px

.. container:: centeralign

   Figure 4 Breadboard adapter layout


The schematic of the adapter board is shown in figure 5. Solder-less breadboards commonly come with double rows of common bused sockets along the top and bottom. See figure 6. These power and ground busses are usually labeled with + and - signs and colored red and black or blue lines. It is assumed that the adapter is inserted into the left hand end of the solder-less breadboard with the + red line marked bus on the top. The +5 V (red) power supply and ground (blue) will be connected to the top two power rails and the +2.5 V (red) and ground (blue) will be connected to the bottom two power rails.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f5.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5 Breadboard adapter schematic


.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f6.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6 Half size solder-less breadboard


The analog input/output pins are routed to the left two end vertical rows of 5 sockets. Labeled with 29 and 30 in figure 6. Channel A is on the lower set and channel B on the upper set. The board in notched out to allow access to the remaining sockets in those rows.

The signals and power supplies that ADALM1000 can generate are limited by the +5 V USB power available from the computer. The analog inputs can measure 0 to +5 volt signals. This limitation on the allowable voltages that can be measured can be expanded through the use of a resistor voltage divider. Two configurable voltage dividers are included on the board. These work in conjunction with the internal 1 MΩ input resistance of the ALM1000 when in the "high Z" measurement mode. Jumpers JP1 and JP2 allow the divider output to be connected to either the default combined Input/output pin or the optional input only pin. Resistors R2 and R4 are the inputs of the dividers. R1 and R3 can be connected through jumpers JP3 and JP4 to either the +2.5 V or +5 V supplies to inject an offset to allow the measurement of negative voltages. Depending on the resistor values chosen, various ranges can be produced. For example, with R1 equal to 500 KΩ and connected to +5 V and R2 set to 1 MΩ the divider factor will be 4X with an offset such that 0 V in will result in +2.5 V as seen by the M1000, -10 V seen as 0V and +10 V seen as +5 V. This range is only valid for ideal resistors and will vary depending on resistor tolerance and the actual value of the +5V supply. Any differences can be calculated out with software calibration.

The input capacitance of the analog inputs in the high Z mode is approximately 380 pF. This capacitance with relatively high resistance levels can significantly lower the frequency response of the resistor divider. Places for compensation capacitors are provide across the input resistors R2 and R4. Two positions C1,2 and C3,4 are provided to best match the required capacitance using standard off the shelf values. Using Spice simulation and empirical testing it was found that for the example case with R1 = 500 KΩ and R2 = 1 MΩ, two 68 pF capacitors in parallel (total of 136 pF) provided nearly optimal compensation. An adjustable trimmer capacitor could of course be used in one of the capacitor positions to more precisely adjust the compensation. The effective input impedance will be 1.333 MΩ and 96 pF.

Another adapter board
---------------------

Another possibility is to configure a larger PCB with a prototyping area and bring all the ADALM1000 connections to female headers positioned right alongside the breadboard area. By using female headers simple 22 gauge wire jumpers can be used to connect to the breadboard rather than the long female to female fly-wires supplied with the kit. An example 3.1" by 3.4" adapter PC board layout is shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f7.jpg
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 7 Prototyping adapter layout


The board consists of a grid of 21 by 30 plated through holes on 0.1" centers which can be used to solder test circuits. Three of the columns of holes on the left side of the grid are shorted together and tied to the +5V, +2.5V and ground connections on the 6/8 pin right angle male header connector that mates with ALM1000. Three of the columns of holes on the right side of the grid are shorted together and tied to the +9V, -9V and ground connections for use with external batteries or other sources of power. The 6/8 analog I/O connections are brought next to the breakout space with a 2 by 8 pin vertical female header positioned alongside the breadboard area. The row of pins next to the breadboard area are just directly connected from the analog ALM1000 right angle male connector. The remaining pins are connected to a pair of resistor divider networks just as in the previous adapter board.

Space for a 6 pin male header for connecting the ALM1000 digital I/O pins to the breadboard is provided. It simply directly connects to a 6 pin female header slot also positioned alongside the breadboard area. These digital pins will not plug directly into the ALM1000 digital connector because it is not on the same side of the module as the analog connector. A short set of male to female jumper wires can be used for those connections. Figure 8 shows the prototyping adapter schematic.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f8.jpg
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8 Prototyping adapter schematic


The pin mapping for the 2X8 and 2X6 female header connectors are shown in figure 9. The right hand side of the 2X8 header follows the 8 analog pins of the ALM1000 exactly. The left and side provides access to the two resistor dividers. The 2X6 female header breaks-out the connections to the on board dual op-amp and provides connections to the various power and ground rails, GND, +2.5 V, +5 V and the external +9 V and -9 V.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 Header pin map


The 21 X 30 grid is sized to accommodate the popular 30 position (400 total connection points) solder-less breadboards, figure 6, with power buses along both sides which are 2 1/8" by 3 1/4". These breadboards come with adhesive backs that will stick the breadboard to the prototype adapter PC board.

This adapter board provides a place to connect external power sources such as a pair of 9 V batteries. A socket for a dual op-amp is included with the two amplifiers configured as non-inverting gain stages and are powered from the external power supplies. A pair of resistors for each amplifier sets the gain. Depending on the choice of amplifier it can be used, for example, to boost the voltage available from the analog outputs or for other purposes in the circuit being prototyped. The external power supplies along with the inputs and outputs of the two amplifiers fill out a 2X6 pin female header also placed along the side of the breadboard area.

The amplifiers can be easily configured as a two amplifier instrumentation amplifier as shown in figure 10. In addition to doing differential to single ended conversion this In-amp can add an offset to center the output voltage swing on the 0 to +5 V input range of the ALM1000.

.. image:: https://wiki.analog.com/_media/university/tools/m1k_adapter_f10.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 Instrumentation amplifier application using a dual op amp


Another possible use would be to generate complementary or differential signals from one of the analog outputs. By connecting one input to ground, with the other input connected to one of the analog outputs and adjusting the resistor values, the first amplifier acts as a non-inverting stage to generate the in phase or true output and the other amplifier acts as an inverting stage to generate the 180º phase or complement output. To make it easy to swap resistor values individual pin sockets could be installed rather than directly soldering the resistors to the board. Likewise using a socket for the op-amp would allow you to interchange different devices optimized for the intended application.

The ADALM1000 hardware itself is rather small and light weight and special care should be taken when using this adapter. It might be useful to add small stick on rubber feet to the underside of the adapter board to help prevent it from tipping or sliding around on the work surface.

Eagle CAD schematic and board files for both breadboard adapters are attached to this document below: `m1000_breadboard_adapters.zip <https://wiki.analog.com/_media/university/tools/m1000_breadboard_adapters.zip>`__
