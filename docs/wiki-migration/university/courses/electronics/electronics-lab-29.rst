Activity: CMOS Logic Circuits, D Type Latch
===========================================

Objective:
----------

The objective of this lab activity is to reinforce the basic principles of CMOS logic from the previous lab activity titled "Build CMOS Logic Functions Using CD4007 Array" and gain additional experience with complex CMOS gates. Specifically, learn how to combine CMOS transmission gates and CMOS inverters to build a D-type flip-flop or latch.

Background:
-----------

To construct the logic functions in this lab activity you will be using the CD4007 CMOS array and discrete NMOS and PMOS transistors (ZVN2110A NMOS and ZVP2110A PMOS) from the ADALP2000 Analog Parts Kit. The CD4007 consists of 3 pairs of complimentary MOSFETs, as shown in figure 1. Each pair shares a common gate (pins 6,3,10). The substrates of all PMOSFETs are common (positive supply pin 14), as well as those of the NMOSFETs (ground pin 7). For the left pair, the NMOS Source terminal is tied to the NMOS substrate (pin 7), and the PMOS Source terminal is tied to PMOS substrate (pin 14). The other two pairs are more general purpose. For the right pair, the Drain terminal of the NMOS is tied to the to the Drain terminal of the PMOS on pin 12.

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
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 CD4007 ( CMOS array)
| 2 ZVN2110A NMOS transistors
| 2 ZVP2110A PMOS transistors

Directions:
-----------

We will now combine the double transmission gate built with inverter chain of the previous exercise to build a D-latch as shown in Figure 2. The two transmission gates work in tandem to realize the D-latch. During the transparent phase of the latch, when CLK=0, the first transmission gate (left) is ON while the second (right) is OFF. D is transmitted to the output (Q) through the first transmission gate and the two series connected inverters. During the latched phase of the latch, when CLK=1, the first transmission gate is OFF but the second transmission gate is ON. As a result, any change in the input D is not reflected at the output Q. However, the second transmission gate, which is now turned ON ensures that the previous logic level at Q is retained through the closed positive feedback loop formed around the two inverters in series. Build the D-latch circuit shown in figure 2 on your solder-less breadboard. Use the CD4007 CMOS array for devices M\ :sub:`1-6` and one ZVN2110A NMOS and ZVP2110A PMOS for each the two inverter stages M\ :sub:`7,8` and M\ :sub:`9,10`. Use the fixed +5 V power supply from ADALM2000 to power your circuit.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f2.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 2 D Type Latch


Hardware Setup:
---------------

Configure both AWG outputs as DC sources for the first steps of the lab. The scope channels are to be used to monitor the inputs and outputs of the circuit as needed. The fixed +5 V power supply is to be used to power your circuit. The fixed -5V supply should be disabled during this Lab.


|image1|

.. container:: centeralign

   Figure 3 D Type Latch Breadboard connections


Procedure:
----------

Connect pins 1,9, which serve as the D input of the latch to the output of AWG1. Connect pins 4,11, which serves as Q output of the latch to Scope channel 2 . Connect pin 6, which serves as CLK to AWG2. Be sure to turn on the fixed +5 V power supply.

First apply logic Low to CLK by opening the AWG control screen and setting AWG2 to 0V DC. Apply logic High to the D input by setting AWG1 to +5 V DC.

Observe the output Q of the latch on scope Channel 2. A steady +5 V should appear on the scope screen. Capture a screen shot.


|image2|

.. container:: centeralign

   Figure 4 Scopy screenshot


Apply logic Low to the D input by setting AWG1 to 0 V DC. Observe the output on the scope. This is the transparent phase of the latch. You should see that scope channel 2 is also at 0 V DC. Now apply logic High to CLK by setting AWG2 to +5 V DC. Also apply logic High to the D input by setting AWG1 to +5 V DC.

Observe the Q output on the scope screen. A steady low should appear in spite of changing D to logic High since the previous value at D-input was low. Capture a screen shot. This is the latched phase of the circuit.


|image3|

.. container:: centeralign

   Figure 5 Scopy screenshot


Now configure both AWG channels as square waves with 5 V amplitudes peak-to-peak. Set AWG1 to a frequency of 1 KHz and AWG2 to a frequency of 2 KHz or twice AWG1. Set the phase of AWG2 to 0 degrees. Be sure to set the AWGs to run synchronously.

Observe the Q output on the scope screen with respect to the signals seen at the CLK and D inputs. Capture the various waveforms and save a screen shot for inclusion in your lab report.


|image4|

.. container:: centeralign

   Figure 6 Scopy screenshot


Now set the phase of AWG2 to 90 degrees. Again observe the Q output on the scope screen with respect to the signals seen at the CLK and D inputs. How have they changed compared to when the phase of AWG2 was 0 degrees and explain why? Capture the various waveforms and save a screen shot for inclusion in your lab report.



|image5|

.. container:: centeralign

   Figure 8 Scopy screenshot


Questions:
----------

The single D-Latch will delay the input signal by 1/2 of the clock cycle. Show how two D-Latches connected in series with opposite phase clocks will then make a master-slave D Flip Flop which will delay the input signal by a full clock cycle.

Building a master/slave D flip flop is left as a bonus exercise if additional CD4007 arrays are available.

Alternative Form:
-----------------

The D-Type latch shown in figure 2 uses complementary pass gates with both NMOS and PMOS transistors. Individual NMOS or PMOS cannot pass both high and low logic levels with equal strength (i.e. on resistance). A single NMOS device can pass a strong logic 0 but will pass a weak logic 1. Conversely, a single PMOS device can pass a strong logic 1 but will pass a weak logic 0.

For many design cases in integrated circuits where internal signals just pass between internal circuit blocks, the asymmetric drive of a single NMOS or PMOS transistor pass is not a significant issue. The positive feedback inherent in a latch can help in this case. In those cases a simplified D-Type latch that uses just 6 devices rather than the 10 used in figure 2 is shown in figures 9 ( latches on rising edge ) and 10 ( latches on falling edge ).

.. image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9 6 transistor rising edge D-Type latch


.. image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10 6 transistor falling edge D-Type latch


.. _hardware-setup-1:

Hardware Setup:
---------------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f9bb.png
   :align: center

.. container:: centeralign

   Figure 11 6 transistor rising edge D-Type latch Breadboard connections


.. image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f10bb.png
   :align: center

.. container:: centeralign

   Figure 12 6 transistor falling edge D Type Latch Breadboard connections


.. _directions-1:

Directions:
-----------

Be sure to turn off the fixed +5 V power supply before making any changes to your breadboard. Reconfigure the circuit from figure 2 on your solder-less breadboard to first look like figure 3. Be sure to turn on the fixed +5 V power supply. Repeat the same procedure with AWG1 connected to the D input and AWG2 to the CLK input. Verify the operation as a latch and that it will latch both logic 0 and 1 inputs on the proper edge of the input clock.

Finally, reconfigure the circuit from on your solder-less breadboard to look like figure 4. Be sure to turn on the fixed +5 V power supply. Repeat the same procedure with AWG1 connected to the D input and AWG2 to the CLK input. Verify the operation as a latch and that it will latch both logic 0 and 1 inputs on the proper edge of the input clock.

Alternate component choices:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The pair of inverters made using the four individual NMOS and PMOS transistors (ZVN2110A and ZVP2110A) could also be constructed from a second CD4007 IC or could be CMOS inverters from a Hex Inverter IC such as a 74HC04 or CD4049.

.. admonition:: Download
   :class: download

   **Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/cmos_dtype_latch_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/cmos_dtype_latch_ltspice`
   


**For Further Reading:**

Electronic Latches `Flip-flop\_(electronics) <https://en.wikipedia.org/wiki/Flip-flop_(electronics)>`_

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/adff_f2bb.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/adff_ss1.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/adff_ss2.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/adff_ss3.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/adff_ss4.png
   :width: 600px
