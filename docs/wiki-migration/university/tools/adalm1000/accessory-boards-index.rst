ADALM1000 (M1K) Accessory PC Boards
===================================

Objective
---------

This document serves as a User’s Guide for a series of accessory PC boards for use with the ADALM1000 active learning module hardware.

General background on the M1K accessory boards.
-----------------------------------------------

The idea is that the M1K analog input path is bare bones simple (for cost savings) and this ecosystem of accessory boards is a set of signal chain building blocks to daisy chain together more complex input and output signal chains. To that end there are generally pass through connections from one side of the boards to the other. Let's consider the 8 pin female analog connector on the M1K as connector "analog1". The connector pads on the accessory boards named ADALM1000 would be populated with matching male connectors. The connector pads on the accessory boards named analog2 would be populated with a female connector replicating the female connector on the M1K but with whatever signal processing a given board does inserted. The simple model is that various boards would be daisy chained in series (the ADALM1000 male connector plugged into the analog2 female connector etc.) building up a new signal chain. The order the boards are connected in series would of course matter and provides additional flexibility. Included is what we are calling a "riser" board which allows the signal chain to split vertically and have a second parallel path as it were.

List of PC Boards
~~~~~~~~~~~~~~~~~

+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Picture                      | Description                             | GitHub Link                                                                                                                                 |
+==============================+=========================================+=============================================================================================================================================+
| |input-divider-2.png|        | Input Resistor Voltage Divider          | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-input-divider>`        |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |input-buffer-d1-dip.png|    | Input buffer dual op-amp                | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-buffermod-d1>`         |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |input-buffer-s2.png|        | Input buffer 2 single op-amp            | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-buffermod-s2>`         |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |minus-5-generator-2.png|    | Negative 5 Volt supply generator        | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-minus-5-generator>`    |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |awg_buffer-1.png|           | Quad op-amp AWG Buffer Board            | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-awg-buffer>`           |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |bnc-adapter-3.png|          | BNC / Scope Adapter Board               | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-scope-probe>`          |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |analog-mux-2.png|           | Dual 4:1 Analog Input Multiplexer Board | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k_analog_mux-4052>`      |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |mili-ohm-amp-meter-1.png|   | Milli Ohm / Amp meter Board             | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-mili-ohmmeter>`        |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |test-points_dip-switch.png| | Test point extender board               | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-test-point-extender>`  |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| |right-angle-1.png|          | Right angle extender board              | :git-education_tools:`CAD Files <m1k-accessory-boards/m1k-right-angle-extender>` |
+------------------------------+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Detailed Descriptions
---------------------

Input Resistor Voltage Divider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Input Voltage Divider accessory board is used when :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`. There are two resistor dividers, R1,2 on the BIN pin and R3,4 on the AIN pin. Referring to the schematic figure, the 8 pin right angle male header named ALM1000 mates with the 8 pin female connector on M1K. The 8 pin right angle female header named ANALOG2 replicates the 8 pin female connector on M1K as a pass through port. The input side of the dividers R2 and R4 are connected to the equivalent “BIN” and “AIN” pins on the ANALOG2 connector. There are solder jumpers to connect the “low” side of the dividers R1, R3 to either of GND, +2.5V or +5V to introduce positive offset for measuring negative input voltages.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-divider-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   Input Resistor Voltage Divider Schematic


The values for the resistors are arbitrary and depend on the desired input voltage span and offset as well as the input impedance. Capacitors (C1,2 and C3,4) across the input resistors R2 and R4 are included to provide course frequency compensation. Fine tuning of the divider frequency response can be done using the software frequency compensation filters in the ALICE software.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-input-divider-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   Input Resistor Voltage Divider PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-divider-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Assembled Input Resistor Voltage Divider PC Board


A common request it to support -5V to +5V inputs. To have the input range most centered on 0V (GND) the offsetting resistors R1, R3, should be connected to the fixed +5V rail when using high value resistors close to the value of the grounded internal 1 MegOhm input resistor in m1k. To maintain an input impedance close to 1 MegOhm, and use standard resistor values, possible values for the resistors would be:

-  R2,4 = 1 MegOhm, R1, R3 = 1 MegOhm
-  R2,4 = 560K, R1, R3 = 560K
-  R2,4 = 680K, R1, R3 = 560K
-  R2,4 = 560K, R1, R3 = 680K
-  R2,4 = 680K, R1, R3 = 680K

Using these values will result in a divider ratio more than 2X so the actual range will be greater than -5V to +5V but not so much greater to waste much of the 16 bit dynamic range of the m1k. Using such large resistors values will greatly reduce the frequency response and adding capacitors (C1,2 and C3,4) across the input resistors R2 and R4 to provide course frequency compensation is suggested. Fine tuning of the divider frequency response can be done using the software frequency compensation filters in the ALICE software.

More info on using voltage dividers can be found :ez:`Here <adieducation/university-program/b/blogs/posts/new-feature-in-alice-adds-input-divider-frequency-compensation>` and :ez:`Here <adieducation/university-program/b/blogs/posts/dc-voltage-divider-for-the-adalm1000>`.

Potentiometer Input Voltage Divider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The an adjustable voltage divider can be substituted for the fixed resistor voltage divider by using a potentiometer as we see in this board. All the same design procedures apply.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/pot-input-divider-sch.png
   :align: center
   :width: 600px

.. container:: centeralign

   Potentiometer Input Voltage Divider Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-pot-divider-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   Potentiometer Input Voltage Divider PCB top


The PCB has multiple holes to accommodate multiple potentiometer styles.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/pot-input-divider-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Assembled Potentiometer Input Voltage Divider examples


Input buffer dual op-amp
~~~~~~~~~~~~~~~~~~~~~~~~

The board layout provides both 8 DIP and 8 pin SOIC footprints (connected in parallel) so that a range of IC variations can be installed. The AD822 Single-Supply, Rail-to-Rail Low Power FET-Input Dual Op Amp is available I both PDIP and SOIC packages and is capable with single-supplies from 5 V to 30 V and dual-supplies from ±2.5 V to ±15. The AD8542 General-Purpose CMOS Dual Rail-to-Rail Amplifier is only available in an SOIC-8 package and can operate form +2.7 V to +5.5 V. Other dual amplifiers in the standard dual amplifier 8 pin pinout can of course be used as well.

Each amplifier is connected as a unity gain follower. With the + input connect to the input pins on the ANALOG2 connector. Provision is made to AC couple the inputs through capacitors C1 and C2. Resistors R1 and R2 provide a DC bias level referenced to the +2.5 V (mid-rail) supply. Solder jumpers SJ1 and SJ2 short the AC coupling capacitors for DC inputs.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-buffer-d1-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   Dual Op-amp Input Buffer Circuit Schematic


The amplifier negative supply pin is connected to the GND2 node which will be connected to GND if the board is connected directly to the M1K. If the board is plugged in to the minus 5 volt supply generator board (see section on that board) the GND2 node will be connected to -5 V.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-buffermod-d1-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   Dual Op-amp Input Buffer Circuit PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-buffer-d1-dip.png
   :align: center
   :width: 400px

.. container:: centeralign

   Assembled Dual Op-amp Input Buffer PC Board


Input buffer 2 single op-amps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The board layout provides 8 DIP footprints (for two single op-amps in standard 8 pin pinout) so that a range of IC variations can be installed.

Each amplifier is connected as a follower with gain setting resistors. Provision is made to AC couple the inputs through capacitors C1 and C2. Solder jumpers SJ1 and SJ2 short the AC coupling capacitors for DC inputs. Resistors R5 and R2 provide a DC bias level referenced through solder jumpers SJ3 and SJ5 to the +2.5 V (mid-rail) supply or GND.

Solder jumpers SJ4 and SJ6 are used to bias the feedback netork resistors to either he +2.5 V (mid-rail) supply or GND.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-buffer-s2-bw-sch.png
   :align: center
   :width: 400px

.. container:: centeralign

   Single Op-amp Input Buffer Circuit Schematic


The amplifier negative supply pins are connected to the GND2 node which will be connected to GND if the board is connected directly to the M1K. If the board is plugged in to the minus 5 volt supply generator board (see section on that board) the GND2 node will be connected to -5 V.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-buffermod-s2-top.png
   :align: center
   :width: 320px

.. container:: centeralign

   Single Op-amp Input Buffer Circuit PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/buffer-board-s2.png
   :align: center
   :width: 375px

.. container:: centeralign

   Assembled Single Op-amp Input Buffer PC Board


Even more info on input buffer circuits can be found :ez:`Here <adieducation/university-program/b/blogs/posts/low-capacitance-fet-input-buffers-for-the-adalm1000>`.

Negative 5 Volt supply generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice that the M1K 8 pin analog I/O connector has two ground pins. The -5 generator hijacks one of these pins for its -5 V rail. On all the other accessory boards these two "ground" pins are never shorted together. If a given board (other than the -5 generator) is plugged into the M1K directly, the two pins will be connected together inside the M1K.

The board layout provides both 8 DIP and 8 pin SOIC footprints (connected in parallel) so that a range of IC variations can be installed. The board is compatible with the ADM660 CMOS Switched-Capacitor Voltage Converter configured as a voltage inverter and the LT1054 Switched-Capacitor Voltage Converter with Regulator. Please refer to the appropriate datasheet for configuring solder jumpers SJ1 and SJ3.

The negative output supply voltage is available on pin 4 of the ANALOG2 8 pin female connector. Jumper SJ2 should be left open if the board (ALM1000 8 pin male connector) is to be connected directly to the ALM1000. Provision is made to have the circuit optionally produce a “doubled” +8.8 V output by installing diodes (preferably Schottky diodes) D1 and D2 and capacitor C3. Solder jumper SJ5 is used to connect the input side of diode D2 to either the +5 V supply rail to produce approximately 2 X +5V minus the two diode drops or to connect D2 to the +2.5 V supply to produce approximately 2.5V + 5V minus the two diode drops. When using the boost option solder jumper SJ4 should be left open. Otherwise to pass the +5 V input supply to the ANALOG2 connector SJ4 can be shorted.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-minus-5-generator-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   Negative 5 Volt supply generator Circuit Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-minus-5-generator-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   Negative 5 Volt supply generator Circuit PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/minus-5-generator-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Negative 5 Volt supply generator board assembled


Quad op-amp AWG Buffer board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AWG buffer board uses a quad op-amp (OP484) in a DIP package to produce larger output swings from the m1k AWG output channels. Output range is determined by the power supply voltages and the resistor values chosen. Two of the amplifiers buffer the AWG outputs. The other two amplifiers can be used to buffer the analog input channels and can be configured as difference amplifiers. Input range is also determined by the power supply voltages and the resistor values chosen.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/awg_buffer-schematic-1.png
   :align: center
   :width: 800px

.. container:: centeralign

   Quad op-amp AWG Buffer board schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/awg_buffer-1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Quad op-amp AWG Buffer board


The AWG buffer board, for example, can be soldered to the -5V generator board to provide nearly +/ 5V output swings from the board.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/awg-buffer-5v.png
   :align: center
   :width: 300px

.. container:: centeralign

   AWG Buffer board plus Negative 5 Volt supply generator


BNC / Scope Adapter Board
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-scope-probe-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   BNC / Scope Adapter Board Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-scope-probe-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   BNC / Scope Adapter Board PCB Top artwork


The following photo shows the BNC Scope Probe adapter soldered to a dual op-amp input buffer board to connect a pair of 10X passive probes to the m1k. With this combination the input range is extended to greater than +/- 20 V. Input impedance is 10 Meg ohms in parallel with the probe capacitance which is about 25 pF.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/scope-probe-adapter-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   10X Scope probes plus adapter board and buffer board


Extender Boards
~~~~~~~~~~~~~~~

There are three extender boards. The first is a simple test point / break-out board that provides a second header connector to be added on the input and output side of the board. There are solder jumpers that allow any of the output side pins to be disconnected / separated from the input side pins. The second board is like the first but the solder jumper are replaced by a 8 position DIP switch.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/test-points_dip-switch.png
   :align: center
   :width: 200px

.. container:: centeralign

   Test point and DIP switch extender boards


The third board is a right angle extender that has two output ports one on the right and left sides of the board. There are solder jumpers that allow each of the 8 input side pins to be optionally connected to the right and left output port pins. This allows, for example, the channel inputs (AIN,BIN) to be routed to the right port while the outputs (CHA,CHB) are routed to the left port. This can improve the input to output isolation.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/right-angle-1.png
   :align: center
   :width: 200px

.. container:: centeralign

   Right angle extender boards


The version on the bottom in the photo has the female output headers installed such that the board is inserted vertically rather then horizontally.

Dual 4:1 Analog Input Multiplexer Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This analog multiplexer input board is centered around a CD4052 (or 74HC4052) dual 4:1 multiplexer. In addition the PDIP versions of the MAX4618 and MAX4582 are pin compatible with the industry-standard 74HC4052.

Referring to the schematic figure, the 8 pin right angle male header named ALM1000 mates with the 8 pin female connector on M1K. The three pin header named CTRL (can be either male or female) is generally connected to three of the digital I/O connector pins on M1K (such as PIO 0-2). The 8 pin right angle female header named ANALOG2 replicates the 8 pin female connector on M1K as a pass through port. The AIN and BIN pins have optional series solder jumpers (SJ1,2) to interrupt those lines. The 8 pin right angle female header named MUXIN provides connection point for the 8 multiplexer inputs. When :doc:`Using Analog Mux in ALICE </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` BIN will be hard wired to the Y half of the Mux and solder jumper SJ1 left open. The X half will not be used and the X output of the Mux is not connected to AIN, solder jumper SJ3 left open and SJ2 shorted.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   CD4952 Analog Mux Circuit Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/m1k-analog-mux-4052-top.png
   :align: center
   :width: 350px

.. container:: centeralign

   CD4052 Analog Mux Circuit PCB Top artwork


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   CD4052 Analog Mux Circuit configured for use in ALICE


Even more info on input multiplexer circuits can be found :ez:`Here <adieducation/university-program/b/blogs/posts/two-input-channels-not-enough-for-ya>`.

LTC1043 Analog Input Multiplexer Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The wiring connections to the LTC1043 quad switch block are relatively simple and can be often built on the Solder-less breadboard along with the rest of the experiment circuitry. However, this might not always be a workable solution so a small PCB adapter has been designed.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-ltc1043-analog-mux-fig8.png
   :align: center
   :width: 275px

.. container:: centeralign

   LTC1043 multiplexer PCB top


On the right there are 8 pins where a right angle male header is installed to connect to the female 8 pin analog connector on the M1k. The 8 analog connector pins of the M1k including the +5 volt and +2.5 volt power supplies are available on a vertical female connector labeled ANLOG2, just to the left of the right angle male header and can be used to power experiments and other circuitry, up to the current limits of the power supplies. The four Mux input channels are available on the four header pins, labeled MUX-IN, on the left side of the board.

There is a solder jumper, SJ1, in series with the CH-A AWG output pin between the right angle connector to the M1k and the female header. Leave this jumper open and connect the second from the top pin on the female header to digital I/O pin 0 when using the board in the Alternate Sweep configurations. To use the board in the Chop Sweep configuration, short the jumper.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-ltc1043-analog-mux-fig10.png
   :align: center
   :width: 375px

.. container:: centeralign

   LTC1043 multiplexer PCB connected to M1k


Milli Ohm / Amp Meter Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This board is built around the AD8210 High Voltage, Bidirectional Current Shunt Monitor IC. A Jumper, JP4, to select unipolar or bipolar current measurements is provided. The VRef2 pin on the AD8210 is connected to ground (GND) and the VRef1 pin can be alternately connected to either GND for a ground referenced output or V+ (5V) for bidirectional operation with the output splitting the supply (V+/2).

Jumper JP3 connects the FORCE- pin to either GND or the +2.5V fixed rail. A 10 Ohm resistor connects the CHA source output to the FORCE+ pin.

More information on measuring very small resistances :ez:`Part I <adieducation/university-program/b/blogs/posts/measure-very-small-resistances-by-building-your-own-milliohm-meter>` and :ez:`Part II <adieducation/university-program/b/blogs/posts/measuring-very-small-resistances-with-adalm1000-part-2>` can further explain how this board can be used.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/miliohmmeter-bw-sch.png
   :align: center
   :width: 550px

.. container:: centeralign

   Milli Ohm / Amp Meter Circuit Schematic


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/miliohmmeter-top.png
   :align: center
   :width: 300px

.. container:: centeralign

   Milli Ohm / Amp Meter PCB Top artwork


The board in the top of the photo below the board can be used as a four wire milli ohm meter or as an amp meter with an external shunt. The board on the bottom of the photo has had a low value (0.5 ohm in this case) surface mount shunt resistor soldered on the board across the S+ and S- pins.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/mili-ohm-amp-meter-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Board Configurations


.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/external-shunt-1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Board Connected to external shunt


Chaining Boards Together
~~~~~~~~~~~~~~~~~~~~~~~~

The accessory boards can be chained or combined together to form many different configurations to suit various needs and applications. In the example shown here the Right Angle Extender is used to send the inputs to a port on the right and the outputs to a port on the left.

On the input port side the dual op-amp input buffer board (using an SMD AD8542) is soldered to the BNC/Scope probe adapter board. Two 10X probes are connected to the inputs.

On the output port side the -5V supply generator with an LT1054 is soldered to the quad op-amp AWG buffer board using a OP484. The outputs are scaled and offset to produce +/- 5V signal swings on the outputs.

.. image:: https://wiki.analog.com/_media/university/tools/adalm1000/chain-exp-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Multiple Boards used in combination


.. |input-divider-2.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-divider-2.png
   :width: 150px
.. |input-buffer-d1-dip.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-buffer-d1-dip.png
   :width: 150px
.. |input-buffer-s2.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/input-buffer-s2.png
   :width: 150px
.. |minus-5-generator-2.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/minus-5-generator-2.png
   :width: 150px
.. |awg_buffer-1.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/awg_buffer-1.png
   :width: 150px
.. |bnc-adapter-3.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/bnc-adapter-3.png
   :width: 150px
.. |analog-mux-2.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/analog-mux-2.png
   :width: 150px
.. |mili-ohm-amp-meter-1.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/mili-ohm-amp-meter-1.png
   :width: 150px
.. |test-points_dip-switch.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/test-points_dip-switch.png
   :width: 120px
.. |right-angle-1.png| image:: https://wiki.analog.com/_media/university/tools/adalm1000/right-angle-1.png
   :width: 120px
