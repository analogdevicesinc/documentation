Activity: CMOS Logic Circuits, D Type Latch - ADALM1000
=======================================================

Objective:
----------

The objective of this lab activity is to reinforce the basic principles of CMOS logic from the previous lab activity titled "Build CMOS Logic Functions Using CD4007 Array" and gain additional experience with complex CMOS gates. Specifically, learn how to combine CMOS transmission gates and CMOS inverters to build a D-type flip-flop or latch.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current -V is added as in CA-V or when configured to force current / measure voltage -I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage -H is added as CA-H.

In this Lab you will be using both of the channels of the ALM1000 in the split Input / Output mode. CB-Out is used to denote the connection to the Output pin and CB-In is used to denote the Input pin on the (expanded) 8 pin connector.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V , CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

To construct the logic functions in this lab activity you will be using the CD4007 CMOS array and discrete NMOS and PMOS transistors (ZVN2110A NMOS and ZVP2110A PMOS) from the Analog Parts Kit. The CD4007 consists of 3 pairs of complimentary MOSFETs, as shown in figure 1. Each pair shares a common gate (pins 6,3,10). The substrates of all PMOSFETs are common (positive supply pin 14), as well as those of the NMOSFETs (ground pin 7). For the left pair, the NMOS Source terminal is tied to the NMOS substrate (pin 7), and the PMOS Source terminal is tied to PMOS substrate (pin 14). The other two pairs are more general purpose. For the right pair, the Drain terminal of the NMOS is tied to the Drain terminal of the PMOS on pin 12.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/cd4007_pinout.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1: CD4007 functional diagram.


The CD4007 is a very versatile IC with many uses as we saw in the previous lab activity. For example, a single CD4007 can be used to make a chain of 3 inverters, an inverter plus two transmission gates, or other complex logic functions such as NAND and NOR gates. Inverters and transmission gates are particularly useful for building D type latches or Master/Slave flip-flops.

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

We will now combine the double transmission gate built with inverter chain of the previous exercise to build a D-latch as shown in figure 2. The two transmission gates work in tandem to realize the D-latch. During the transparent phase of the latch, when CLK=0, the first transmission gate (left) is ON while the second (right) is OFF. D is transmitted to the output (Q) through the first transmission gate and the two series connected inverters. During the latched phase of the latch, when CLK=1, the first transmission gate is OFF but the second transmission gate is ON. As a result, any change in the input D is not reflected at the output Q. However, the second transmission gate, which is now turned ON ensures that the previous logic level at Q is retained through the closed positive feedback loop formed around the two inverters in series.

Build the D-latch circuit shown in figure 2 on your solder-less breadboard. Use the CD4007 CMOS array for devices M\ :sub:`1-6` and one ZVN2110A NMOS and ZVP2110A PMOS for each the two inverter stages M\ :sub:`7,8` and M\ :sub:`9,10`. Use the fixed +5 V power supply from the ALM1000 to power your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-d-type-ff_f2.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 2, D Type Latch


Hardware Setup:
~~~~~~~~~~~~~~~

Configure both analog I/O's in Split-I/O mode with the termination to GND for the first steps of the lab. The scope input channels are to be used to monitor the D and CLK inputs and the Q and Qbar outputs of the circuit as needed. The fixed +5 V power supply is to be used to power your circuit.

Procedure:
~~~~~~~~~~

Connect pins 1,9, which serve as the D input of the latch to output CA-Out. Connect pins 4,11, which serves as Q output of the latch to Scope channel CA-In . Connect pin 6, which serves as CLK to CB-Out. Be sure to connect the fixed +5 V power supply. First apply logic Low to CLK by setting CB-Out to shape DC and 0 mA Max value (0 V). Apply logic High to the D input by setting CA-Out to shape DC and 100 mA Max value (+5 V).

Observe the output Q of the latch on scope Channel CA-In. A steady +5 V should appear on the scope screen. Capture a screen shot.

Apply logic Low to the D input by setting CA-Out to 0 mA Max value (0V). Observe the output on the scope. This is the transparent phase of the latch. You should see that scope channel CA-In is also at 0 V DC.

Now apply logic High to CLK by setting CB-Out to 100 mA Max value (+5 V). Next apply logic High to the D input by setting CA-Out to 100 mA Max value (+5 V). Observe the Q output on the scope screen. A steady low should appear in spite of changing D to logic High since the previous value at D-input was low. Capture a screen shot. This is the latched phase of the circuit.

Now configure both analog output channels as square waves (Shape) with 0 mA Min values and 100 mA Max value (0 to 5 V swings). Set CA-Out to a frequency of 1 KHz and CB-Out to a frequency of 2 KHz or twice CA. Set the phase of CB-Out to 270 degrees. Be sure to set the AWGs to run synchronously.

Observe the Q output on the scope screen with respect to the signals seen at the CLK and D inputs. Capture the various waveforms and save a screen shot for inclusion in your lab report.

Now set the phase of CB-Out to 90 degrees. Again observe the Q output on the scope screen with respect to the signals seen at the CLK and D inputs. How have they changed compared to when the phase of CB-Out was 270 degrees and explain why? Try setting the phase of CB-Out to 90 degrees and 180 degrees, how has the Q output changed with respect to the CLK and D inputs? Capture the various waveforms and save a screen shot for inclusion in your lab report.

Questions:
~~~~~~~~~~

The single D-Latch will delay the input signal by 1/2 of the clock cycle. Show how two D-Latches connected in series with opposite phase clocks will then make a master-slave D Flip Flop which will delay the input signal by a full clock cycle.

Building a master/slave D flip flop is left as a bonus exercise if additional CD4007 arrays are available.

Alternative Form:
-----------------

The D-Type latch shown in figure 2 uses complementary pass gates with both NMOS and PMOS transistors. Individual NMOS or PMOS cannot pass both high and low logic levels with equal strength (i.e. on resistance). A single NMOS device can pass a strong logic 0 but will pass a weak logic 1. Conversely, a single PMOS device can pass a strong logic 1 but will pass a weak logic 0.

For many design cases in integrated circuits where internal signals just pass between internal circuit blocks, the asymmetric drive of a single NMOS or PMOS transistor pass is not a significant issue. The positive feedback inherent in a latch can help in this case. In those cases a simplified D-Type latch that uses just 6 devices rather than the 10 used in figure 2 is shown in figures 3 ( latches on rising edge ) and 4 ( latches on falling edge ).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-d-type-ff_f3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3 6 transistor rising edge D-Type latch


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-lab-d-type-ff_f4.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 4 6 transistor falling edge D-Type latch


.. _directions-1:

Directions:
~~~~~~~~~~~

Be sure to disconnect the fixed +5 V power supply before making any changes to your breadboard. Reconfigure the circuit from figure 2 on your solder-less breadboard to first look like figure 3. Be sure to reconnect the fixed +5 V power supply. Repeat the same procedure with CA-Out connected to the D input and CB-Out to the CLK input. Verify the operation as a latch and that it will latch both logic 0 and 1 inputs on the proper edge of the input clock.

Finally, reconfigure the circuit on your solder-less breadboard to look like figure 4. Be sure to reconnect the fixed +5 V power supply after you complete the changes. Repeat the same procedure with CA-Out connected to the D input and CB-Out to the CLK input. Verify the operation as a latch and that it will latch both logic 0 and 1 inputs on the proper edge of the input clock.

Alternate component choices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pair of inverters made using the four individual NMOS and PMOS transistors (ZVN2110A and ZVP2110A) could also be constructed from a second CD4007 IC or could be CMOS inverters from a Hex Inverter IC such as a 74HC04.

**For Further Reading:**

`Electronic Latches <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>`__

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-labs-list>`\ **.**
