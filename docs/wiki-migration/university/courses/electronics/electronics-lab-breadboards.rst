What Is a Solder-less Breadboard?
=================================

Objective:
----------

The purpose of this activity is to familiarize the reader with solder-less breadboards.

A breadboard is used to build and test circuits quickly before finalizing any circuit design. The breadboard has many holes into which circuit components like ICs and resistors can be inserted. The holes are most commonly spaced 0.1" apart to accommodate standard DIP components. A typical breadboard that includes top and bottom power distribution rails is shown below:

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abb_f1.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 1 Solder-less breadboard


The breadboard has strips of metal sockets which run underneath the board, yellow rectangles in figure 2, and connect the groups of five holes on the board. The metal strips are arranged as shown below. Note that the top and bottom rows of holes are connected horizontally while the holes in the center sections are connected vertically.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abb_f2.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 2 Arrangement of internal connections


To use the bread board, the leads of components are inserted into the holes. Each set of holes connected by a metal strip underneath forms a node. A node is a point in a circuit where two or more components are connected. Connections between different components are made by inserting their leads in a common node. The long top and bottom row of holes, indicated by the red and blue stripes are usually used for power supply connections. The rest of the circuit is built by inserting components and connecting them together with jumper wires. Solid rather than stranded wire is the best to use with breadboards like these.

ICs are placed in the middle of the board so that half of the leads are on one side of the middle line and half on the other.

A completed circuit might look like the following.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abb_f3.jpg
   :align: center
   :width: 420px

.. container:: centeralign

   Figure 3 Wired breadboard


It is very useful to have a few simple hand tools available as well. A pair of small wire cutters, often also called diagonal cutters to cut wires and component leads to length. A small pair of long nose pliers to bend and shape wires and leads. And of course a pair of wire strippers to strip the insulation from the ends of your jumper wires. A small screwdriver is also a handy item to adjust potentiometers and such.

Breadboarding tips:
-------------------

It is important to breadboard a circuit neatly and systematically, so that one can debug it and get it running easily and quickly. It also helps when someone else needs to understand and inspect the circuit. Here are some tips:

| 1. Always use the top and bottom bus rails for power supply connections. Power the integrated circuits and other devices from these bus rails and not directly from the power supply.
| 2. Color coding the jumper wires can help reduce confusion when building a circuit. For example, use green wires for ground connections (0V), red for +V and black for -V power connections.
| 3. Arrange the jumper wires to lay flat on the board, so that the board does not become cluttered.
| 4. Route jumper wires around the integrated circuits and not over the packages. This makes changing the chips easier as needed.
| 5. Trimming the leads of components like resistors, capacitors, transistors and LEDs, so that they fit closely to the board and do not get pulled out by accident is a good practice. While short wires and leads look neater, the clipped components will only fit into a limited “span” of breadboard socket holes, limiting the use of the component in other experiments. It is perfectly permissible to use components with longer leads while exploring different circuit possibilities.
| Be cautious when inserting components which have been removed from a tape reel used in automatic insertion equipment. Suppliers of surplus components often sell components in small batches cut from larger taped reels. Removing the tape from the components does not always remove the all the adhesive from the leads of the components. Placing a formerly taped component into a socket hole may result in a poor electrical connection and, even worse, may leave adhesive residue in the socket. To avoid this problem carefully clean the adhesive residue from component leads, clipping the taped portion of the lead off, or avoid using components that have been taped.

It is important to be especially careful when inserting integrated circuits into the breadboard holes. Unless the IC pins are straight, it is very easy to crush the pin into a zigzag shape or fold the pins underneath the body of the IC. Either way the result is a bad connection or no connection at all. Always use solid wire for breadboard connections. When stripping the wire ends, be careful not to strip more than about three-eighths of an inch of insulation from the wire. Too much bare wire may result in unintentional connections near the wire end. After you have built up a few circuits, you will have a good collection of pre-stripped jumper wires. Save them. By reusing these wires, you can save even more time and effort in assembling future circuits. Pre-formed wires of various lengths and colors are also available from many sources.

Using breadboards with the ADALM2000 Module:
--------------------------------------------

All the connections to the ADALM2000 design kit are made though the 30 pin male header (0.1" centers) connector on the side of the module. This is a very common, generic style connector and is simple to attach wires to as with the various female to female cables supplied in the kit. Double length square male pins are included to change the female end of the wires into male pins that can be easily inserted into the solder-less breadboards used in the lab for building example circuits. These fly-wires are several inches long and can be awkward to use at times given the relatively light weight of the ADALM2000 box and a small solder-less breadboard.

Adapters such as those shown below are workable alternatives. They adapt the square male pins of the ADALM2000 connector to two rows of male pins on 300 mil spacing (like DIP packages) that will plug nicely into a solder-less breadboard.

|image1| |dual_row_receptical-14.jpg| |image2|

These adapters can be easily constructed from dual row female receptacles, a small section of protoboard with rows of holes on 0.1" centers and single row male headers. They can also be purchased in 10, 14, 16, and 20 pin versions from: `Technological Arts <http://www.technologicalarts.ca/shop/store/category/54/adapters/receptacle.html>`__

A 12 pin (dual row of six) version is also available from:`Digilent PmodDIP <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,401,1081&Prod=PMOD-DIP>`__

The smaller adapters can be used individually or combined to fill out the entire 30 pins of the ADALM2000 connector, 10+20 or 14+16.

Another more convenient arrangement would be an adapter PC board that connects to the 30 pin male header of ADALM2000 and brings all the connections to a female header positioned right alongside the breadboard area. By using a female header simple 22 gage solid wire jumpers can be used to connect to the breadboard rather than the long female to female fly-wires supplied with the kit. An example 3.1" by 3.4" adapter PC board layout is shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abb_f4.jpg
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 4 Breadboard adapter layout


The board consists of a grid of 21 by 30 plated through holes on 0.1" centers which can be used to solder test circuits. Three of the columns of holes on the left side of the grid are shorted together and tied to the +5V, -5V and ground connections on the 30 pin right angle female connector that mates with ADALM2000. Three of the columns of holes on the right side of the grid are shorted together and tied to the +9V, -9V and ground connections for use with external batteries or other sources of power. The 30 ADALM2000 connections are brought to a breakout space for a 40 pin vertical female header positioned alongside the breadboard area. The 21 X 30 grid is sized to accommodate the popular 30 position (400 total connection points) solder-less breadboards with power busses along both sides which are 2 1/8" by 3 1/4". These breadboards come with adhesive backs that will stick the breadboard to the adapter PC board. The schematic of the adapter board is shown in figure 5. The signals and power supplies that ADALM2000 can generate are limited by the USB power available from the computer. The analog inputs can measure much larger +/- 20 volt signals. This board provides a place to connect external power sources such as a pair of 9 V batteries. A socket for a dual op-amp is included with the two amplifiers configured as non-inverting gain stages and are powered from the external power supplies. A pair of resistors for each amplifier sets the gain. Depending on the choice of amplifier it can be used, for example, to boost the voltage and/or current available from the AWGs or for other purposes in the circuit being breadboarded. The external power supplies along with the inputs and outputs of the two amplifiers fill out the extra 10 pins on the 40 pin header.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/abb_f5.jpg
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 5 Breadboard adapter schematic


The layout of the resistors around the dual op-amp are arranged such that rather than two independent amplifiers, a single resistor can be inserted between the two inverting inputs, in place of the two resistors (R1,R4) to ground. Configured this way the two op-amps form the input section of an instrumentation amplifier. The amplified differential signal at the outputs of the two amplifiers can then be connected to the differential scope inputs on ADALM2000. Another possible use would be to generate complementary or differential signals from one of the AWGs. By connecting one input to ground, with the other input connected to one of the AWG outputs and adjusting the resistor values the first amplifier acts as a non-inverting stage to generate the in phase or true output and the other amplifier acts as an inverting stage to generate the 180º phase or complement output. To make it easy to swap resistor values individual pin sockets could be installed rather than directly soldering the resistors to the board. Likewise using a socket for the op-amp would allow you to interchange different devices optimized for the intended application. The ADALM2000 hardware itself is rather small and light weight and special care should be taken when using an adapter like this. It might be useful to add small stick on rubber feet to the underside of the adapter board to help prevent it from tipping or sliding around on the work surface.

Eagle CAD schematic and PCB layout files can be down loaded here `ad_breadboard.zip <https://wiki.analog.com/_media/university/courses/electronics/ad_breadboard.zip>`__.

For more on building advanced breadboards see:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| http://www.analog.com/static/imported-files/tutorials/MT-100.pdf
| http://en.wikipedia.org/wiki/Breadboard

**Return to Labs** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_row_receptical-10.jpg
   :width: 300px
.. |dual_row_receptical-14.jpg| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_row_receptical-14.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_row_receptical-20.jpg
   :width: 300px
