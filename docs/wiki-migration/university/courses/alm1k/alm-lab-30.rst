Activity : CMOS Logic Circuits, Transmission Gate XOR
=====================================================

Objective:
----------

The objective of this lab activity is to reinforce the basic principles of CMOS logic from the previous lab activity titled "Build CMOS Logic Functions Using CD4007 Array"[1] and gain additional experience with complex CMOS gates. Specifically, learn how to combine CMOS transmission gates and CMOS inverters to build transmission gate exclusive OR (XOR) and XNOR logic functions.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

In this Lab you will be using both of the channels of the ALM1000 in the split Input / Output mode. CB-Out is used to denote the connection to the Output pin and CB-In is used to denote the Input pin on the (expanded) 8 pin connector.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

To construct the logic functions in this lab activity you will be using the CD4007 CMOS array and discrete NMOS and PMOS transistors (ZVN2110A NMOS and ZVP2110A PMOS or similar) from the Analog Parts Kit. The CD4007 consists of 3 pairs of complimentary MOSFETs, as shown in figure 1. Each pair shares a common gate (pins 6,3,10). The substrates of all PMOSFETs are common (positive supply pin 14), as well as those of the NMOSFETs (ground pin 7). For the left pair, the NMOS Source terminal is tied to the NMOS substrate (pin 7), and the PMOS Source terminal is tied to PMOS substrate (pin 14). The other two pairs are more general purpose. For the right pair, the Drain terminal of the NMOS is tied to the Drain terminal of the PMOS on pin 12.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1: CD4007 functional diagram.


The CD4007 is a very versatile IC with many uses as we saw in the previous lab activity[1]. For example, a single CD4007 can be used to make three inverters, an inverter plus two transmission gates, or other complex logic functions such as NAND and NOR gates. Inverters and transmission gates are particularly useful for building transmission gate exclusive OR (XOR) and XNOR logic functions. The schematic symbols for XOR and XNOR logic gates are shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-xor_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2 XOR and XNOR schematic symbols


Static Discharge
~~~~~~~~~~~~~~~~

The CD4007 like many CMOS integrated circuits, it is easily damaged by static discharge. The CD4007 includes diodes to protect it from static discharge, but it can still be damaged if it is not handled carefully. Normally one would use anti-static mats and wrist straps when working with static sensitive electronics. However, you may not have those when working at home outside a formal lab environment. A low budget way to avoid static discharge is to ground yourself before touching an IC. Discharging any built up static charge before handling a CD4007 will help ensure that you do not have a broken chip half way through the lab.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less Breadboard and jumper wire kit
| 1 CD4007 ( CMOS array)
| 2 ZVN2110A NMOS transistors
| 2 ZVP2110A PMOS transistors

Directions:
~~~~~~~~~~~

We will now combine the double pole single throw (SPDT) transmission gate switch and two CMOS inverters to build an XOR gate (and XNOR) as shown in Figure 3. The two transmission gates work in tandem to realize a selector operation. Depending on the state of the A input, either Input B or the inverted version of input B appears at the C (XOR) output. Another inverter, M\ :sub:`9,10`, inverts C to produce the Cbar (XNOR) output.

Build the XOR/XNOR circuit shown in figure 3 on your solder-less breadboard. Use the CD4007 CMOS array for devices M\ :sub:`1-6` and one ZVN2110A NMOS and ZVP2110A PMOS for each of the two inverter stages M\ :sub:`7,8` and M\ :sub:`9,10`. Use the fixed +5 V power supply from ALM1000 to power your circuit.

There are two logic inputs A, and B to the circuit. The non-inverting XOR output is at node C and an inverting version of the output is at node Cbar to form the XNOR function.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-xor_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3, Exclusive OR and XNOR gate


Hardware Setup:
~~~~~~~~~~~~~~~

Configure both analog I/O's in Hi-Z mode for the first steps of the lab. The scope input channels are to be used to monitor the C and Cbar outputs of the circuit as needed. The fixed +5 V power supply is to be used to power your circuit.

Procedure:
~~~~~~~~~~

Connect pins 2,5,12, which serves as the C output to Scope channel A input pin, CA-In. Connect the drain terminals of M9,10 which serves as the Cbar output to Scope channel B input pin CB-In. Be sure to connect the fixed +5 V power supply.

First apply logic Low to the A logic input (pin 6) by grounding it to 0 V DC. Apply logic low to the B input (pins 1,9) by grounding it to 0 V DC.

Observe the output C of the gate on scope Channel A. A steady DC voltage should appear on the scope screen. To apply logic Hi to the A logic input (pin 6) connect it to +5 V, similarly apply logic Hi to the B input (pins 1,9) by connecting it to +5 V. Enter your observations in the following table. Include the completed logic table in your lab report.

======= ======= ======== ===========
Input A Input B Output C Output Cbar
======= ======= ======== ===========
0       0                
1       0                
0       1                
1       1                
======= ======= ======== ===========

Table 1 XOR / XNOR truth table

Now configure both output channels in the Split I/O mode with the termination set to +2.5V. Connect the A logic input (pin 6) to the channel A output pin CA-Out, and connect the B logic input (pins 1,9) to the channel B output pin CB-Out. Set the shape as square waves with -50 mA Min value and +50 mA Max value ( 0 to 5 V swing). Set channel A to a frequency of 1 KHz and channel B to a frequency of 2 KHz or twice CA. Be sure to set the AWGs to run synchronously.

Observe both the C output and the Cbar output on the scope screen with respect to the signals at the A and B inputs. Capture the various waveforms and save a screen shot for inclusion in your lab report.

Next set channel B to the same 1 KHz frequency as channel A but set the phase of CB to 90°. Observe both the C output and the Cbar output on the scope screen with respect to the signals at the A and B inputs. Capture the various waveforms and save a screen shot for inclusion in your lab report.

Questions:
~~~~~~~~~~

How could you configure ( i.e. add to ) an XOR gate to produce an output frequency that is twice ( double ) the frequency of a single input source?

XOR Gate as phase detector:
---------------------------

A phase detector or phase comparator is a logic circuit that generates an analog output voltage signal which represents the difference in phase between two logic signal inputs. It is a central element of a phase-locked loop (PLL). Detecting the phase relationship between signals is an important functional block in many systems, such as motor control, radar, telecommunication, demodulators, and servo mechanisms.

A phase detector for square wave signals can be made from an exclusive-OR (XOR) logic gate. When the two signals being compared are completely in-phase, i.e. phase difference is 0 degrees, the XOR gate's output will have a constant level of zero. When the two signals differ in phase by 10° for example, the XOR gate's output will be high for 10/180\ :sup:`th` or 1/18\ :sup:`th` of a cycle, the fraction of a cycle during which the two signals differ in value. When the signals differ by 180°, that is, one signal is high when the other is low, and vice versa the XOR gate's output remains high throughout each cycle.

When an XOR gate phase detector is used in a phase locked loop ( PLL ) system it generally locks near a 90° phase difference in the middle of the phase detection range. At 90° the XOR has a 50% duty cycle square-wave output at twice the frequency of the input. The square-wave changes duty-cycle in proportion to the phase difference of the two input signals. Passing the output of the XOR gate through a low-pass filter results in an analog voltage that is proportional to the phase difference between the two signals. It requires inputs that are symmetrical square waves. If the duty cycle of one input is slightly different than the duty cycle of the other, the low pass filtered output will have an offset from the ideal middle of the range at 90° of phase difference.

.. _directions-1:

Directions:
~~~~~~~~~~~

Add the RC low pass filter shown in figure 4 to your XOR breadboard circuit. Connect scope channel CA-In to the output of the RC filter.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-xor_f4.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4, XOR Gate phase detector


.. _hardware-setup-1:

Hardware Setup:
~~~~~~~~~~~~~~~

Configure both output channels in the Split I/O mode with the termination set to +2.5V. Connect the A logic input (pin 6) to the channel A output pin CA-Out, and connect the B logic input (pins 1,9) to the channel B output pin CB-Out. Set the shape as square waves with -50 mA Min value and +50 mA Max value (0 to 5 V swing). Set channel A to a frequency of 1 KHz and channel B to a frequency of 1 KHz. Also be sure to start with the phase of both CA and CB set to 0°.

.. _procedure-1:

Procedure:
~~~~~~~~~~

Connect scope channel CA-In to the output of the RC filter at C\ :sub:`1` to observe the filtered (DC) output of the phase detector. Connect scope channel CB-In to output C of the XOR gate to observe the pulse width of the output of the logic gate. Record the DC output voltage in the table below. Set the phase of channel B to the values listed in the table and record the DC voltage you observe at the output of the phase detector.

======== ======== ==============
CA Phase CB Phase Output Voltage
======== ======== ==============
0        0        
0        45       
0        90       
0        135      
0        180      
0        225      
0        270      
0        360      
======== ======== ==============

Table 2 Phase detector output vs phase

.. _questions-1:

Questions:
~~~~~~~~~~

Move the RC low pass filter to the XNOR output at Cbar and repeat your phase sweep measurements. How is the output response of the phase detector different?

Alternate component choices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pair of inverters made using the four individual NMOS and PMOS transistors (ZVN2110A and ZVP2110A) could also be constructed from a second CD4007 IC or could be CMOS inverters from a Hex Inverter IC such as a 74HC04 or CD4049. The CD4066 quad SPST switch could also serve as an alternative to the switches built from the CD4007.

**For Further Reading:**

| [1] Build :doc:`CMOS Logic Functions Using CD4007 Array </wiki-migration/university/courses/alm1k/alm-lab-28>`
| `Exclusive OR logic gate <https://en.wikipedia.org/wiki/XOR_gate>`__
| `Exclusive NOR logic gate <https://en.wikipedia.org/wiki/XNOR_gate>`__
| `Phase detector <https://en.wikipedia.org/wiki/Phase_detector>`__

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
