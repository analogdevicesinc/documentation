Activity: A BJT Curve Tracer - ADALM2000
========================================

Objective:
----------

The purpose of this activity is to investigate the collector current, I\ :sub:`C` vs. collector voltage, V\ :sub:`CE` characteristics of the BJT. The kit of parts the student has will contain a number of transistors (ideally both NPN and PNP devices of various types). Many of the activities in this series make use of the matching or relative size of the devices in their operation. The student, after successfully configuring the curve tracer, should serialize and measure their devices and sort this inventory of transistors by various parameters such as gain (beta) , V\ :sub:`BE` etc.

Background:
-----------

The variable analog outputs supplied by the ADALM2000 hardware are voltages. The BJT collector current is controlled by the base current. The AWG output voltage must be converted into a suitable current to drive the base terminal of the device under investigation. A simple resistor can be used to convert a voltage into a current, as shown in figure 1. However, only if the voltage across the resistor is known or controlled in some way. In this simple circuit, the base current I\ :sub:`B` = (V\ :sub:`AWG1` - V\ :sub:`BE`)/100KΩ. We can set V\ :sub:`AWG1` to known values but we don’t know the exact value of V\ :sub:`BE`. We can of course remove an estimate of the V\ :sub:`BE` mathematically. This is still only an estimate.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Simple I\ :sub:`C` vs V\ :sub:`CE` circuit


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf1.png
   :align: right

.. container:: centeralign

   Figure 2, Simple I\ :sub:`C` vs V\ :sub:`CE` circuit breadboard connection


Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - 100KΩResistors
| 1 - 100ΩResistor
| 1 - small signal NPN transistor (2N3904 or SSM2212)

Directions and Setup:
---------------------

Build the simple curve tracer circuit shown in Figure 1. The green boxes indicate where to connect the ADALM2000. Using the Scopy Signal Generator tool, in Channel 2 Buffer tab import the csv file for the stairstep signal needed. Now at this point set the amplitude to 2 V peak-to-peak and the offset to 2.6 V. The waveform in the display should start at 0.6V and increase in 1 V increments to 4.6 V (0.6, 1.6, 2.6, 3.6, 4.6). For each step to be 5 mSec long for a total of 25 mSec, set the sampling rate to 200 sps. In Signal Generator Channel 1 configure a triangle wave with an amplitude of 5V peak-to-peak and an offset of 2.5V (wave should swing from 0 to 5V). Set the frequency to 200 Hz ( 5 times the 40 Hz of channel 2). Comparing the waveforms in Channel 1 and Channel 2, the triangle wave in Channel 1 should go through one cycle from 0 to 5 V and back to zero during the time of one step in the waveform in Channel 2. It will probably be necessary to set the phase of Channel 1 to 90 degrees to make them line up in this way.

Procedure:
----------

The 1 V steps in the voltage driving the 100KΩ base resistor will produce approximately 1 V/100KΩ or 10 uA steps in the base current. Using the scope in XY mode plot channel 1 on the horizontal axis (V\ :sub:`CE`) and channel 2 (I\ :sub:`C`) on the vertical axis. You should see a set of 5 curves of I\ :sub:`C` vs. V\ :sub:`CE`, one for each of the 5 different base current levels. These base current levels should be approximately 0, 10uA, 20uA, 30uA and 40uA. It may be necessary to slightly adjust the 0.6V level of the first step of AWG2 up or down slightly to insure it is right at the initial turn on value ( I\ :sub:`B`\ =0 and I\ :sub:`C`\ =0) of the transistor you are testing.

Questions:
----------

-  From the measured data calculate the current gain Beta ( I\ :sub:`C`/I\ :sub:`B` ) for each device.
-  Using the curve for the highest base current step, calculate the early voltage for each device.
-  Calculate the Beta Early voltage product ( b*VA) for each device.
-  Compare your results with manufacturer specifications for each device measured.

The Gummel Plot
---------------

The Gummel plot is the combined plot of the collector and base currents (I\ :sub:`C` and I\ :sub:`B`) of a transistor vs. the base-emitter voltage, V\ :sub:`BE`, on a semi-logarithmic scale. This plot is very useful in device characterization because it reflects on the quality of the emitter-base junction while the base-collector bias, V\ :sub:`BC`, is kept at a constant. A number of other device parameters can be garnered either quantitatively or qualitatively directly from the Gummel plot: the DC gain, Beta, base and collector ideality factors, nIb and nIc; series resistances and leakage currents. (http://en.wikipedia.org/wiki/Gummel_plot)

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Circuit to generate a Gummel Plot


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf2.png
   :align: right

|

.. container:: centeralign

   Figure 4, Circuit to generate a Gummel Plot breadboard connection


| |image1|

.. container:: centeralign

   Figure 5, Example Gummel Plot


(From: http://www.synopsys.com/Tools/TCAD/Pages/hbtprocessing.aspx)

A more accurate approach to create IB
=====================================

.. _objective-1:

Objective:
----------

We need to somehow remove V\ :sub:`BE` from the equation in figure 1 which sets I\ :sub:`B`. The circuits shown in figures 6 and 8 perform the function to force V\ :sub:`AWG1` across the 10KΩ resistor independent of the value of V\ :sub:`BE`.

.. _materials-1:

Materials:
----------

| ADALM2000 Active Learning Module
| Solder-less Breadboard
| 1 - Dual Op AMP (such as ADTL082)
| 4 - 10KΩ Resistors
| 1 - 1KΩ Resistor
| 1 - 100Ω Resistor
| 1 - small signal NPN transistor / PNP transistor (2N3904, 2N3906, SSM2212, SSM2220)
| 2 - 4.7 uF decoupling capacitors
| 1 - 1 uF filter capacitor

.. _directions-and-setup-1:

Directions and Setup:
---------------------

Below are schematics for both a common emitter and a common base BJT curve tracer test circuit for use with the ADALM2000. It uses one dual opamp (ADTL082) powered from the +/- 5 Volt board supplies. In the common emitter configuration, one opamp serves as a virtual ground at the base terminal to convert the voltage steps from waveform generator W2 into base current steps through a 10KΩ resistor. The collector voltage is swept using a ramp from generator W1. V\ :sub:`CE` is measured differentially by scope inputs 1+, 1-. The collector current, I\ :sub:`C` is measured by scope inputs 2+, 2- differentially across a 100Ω resistor. A ratio of 100 for the base and collector resistors is used because beta, the collector current to base current gain, is often approximately 100. The voltage on the base terminal can be offset to either +2.5V or -2.5V (or 0V) to increase the possible V\ :sub:`CE` swing (by -2.5 for NPN or +2.5 for PNP). The +2.5V is generated by a voltage divider from the +5V supply and the -2.5V is generated by inverting the +2.5V with the second opamp in the dual op-amp (ADTL082). The base and emitter connection can be interchanged to configure the device under test (DUT) in the common base mode. The resistor values are changed to 1KΩ for both in this configuration. This ratio of one is appropriate given that alpha, the ratio of emitter current to collector current, is very close to one. The voltage from W2 now sets the emitter current and the ramp on W1 sweeps the V\ :sub:`CB` and is measured differentially with 1+, 1-. The collector current I\ :sub:`C` is measured differentially across the 1KΩ resistor with 2+, 2-.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, Common Emitter configuration


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf4.png
   :align: right

.. container:: centeralign

   Figure 7, Common Emitter configuration breadboard connection


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8, Common Base configuration


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf5.png
   :align: right

.. container:: centeralign

   Figure 9, Common Base configuration breadboard connection


The following characteristic curves where taken using various NPN and PNP transistors in the common emitter configuration. A 10KΩ base resistor and 100Ω collector resistor was used in both cases.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 10, NPN I\ :sub:`C` vs. V\ :sub:`CE`


NPN, beta is approximately 166.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 11, PNP I\ :sub:`C` vs. V\ :sub:`CE`


PNP, beta is approximately 200.

The following characteristic curves where taken using the same NPN and PNP transistors in the common base configuration. A 1KΩ emitter resistor and 1KΩ collector resistor was used in both cases

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 12, NPN I\ :sub:`C` vs. V\ :sub:`CB`


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 13, PNP I\ :sub:`C` vs. V\ :sub:`CB`


Further reading: http://en.wikipedia.org/wiki/Transistor_curve_tracer

Measuring Transistor VBE
========================

.. _objective-2:

Objective:
----------

The purpose of this activity is to characterize the base emitter voltage of a BJT. The V\ :sub:`BE` vs. Collector current characteristic of the transistor is a key factor in circuits. Often transistors are used in pairs where the matching of the V\ :sub:`BE` is important to proper circuit operation. In other cases the difference between the V\ :sub:`BE` of two or more transistors is exploited in the operation of the circuit. Size matters, V\ :sub:`BE` is a strong function of the size of the transistor, the emitter region at least.

.. _materials-2:

Materials:
----------

| Various -- small signal transistors (NPN and PNP)
| 1 - Dual Op AMP (such as ADTL082)
| 1 - 1KΩResistor
| 2 - 4.7 uF decoupling capacitors

Directions:
-----------

The circuit below, figure 14, can be used in conjunction with the ADALM2000 to accurately measure the V\ :sub:`BE` vs. emitter current of an NPN transistor. Emitter current is used in this measurement rather than collector current but I\ :sub:`E` and I\ :sub:`C` are essentially the same given a high beta transistor. The op-amp supplies the base current and any bias current that might flow in the 2+ scope input while forcing the emitter of the transistor to the (virtual) ground potential. Negative voltages applied by waveform generator W1 set the emitter current through the 1KΩ resistor. The same circuit can be used to measure PNP transistors by connecting the collector to Vn rather than Vp. Positive voltages applied by generator W1 set the emitter current through the 1KΩresistor.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f10_1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 14, Circuit to measure V\ :sub:`BE`


Hardware Setup:
---------------

| 
| |image2|

.. container:: centeralign

   Figure 15, Circuit to measure V\ :sub:`BE` breadboard connection


The generator output W1 should be configured for a 100 Hz triangle wave with 2 volt amplitude peak-to-peak and -2 volt offset (for an NPN device). The single ended input of scope channel 2+ is used to measure the voltage at the base of the transistor (optionally connect 2- to the emitter to remove any input offset of the op-amp). The setup should be configured with channel 1 connected to display the output of W1 and channel 2 connected to display the base voltage. The emitter current is calculated as the voltage of W1 / 1KΩ.

.. _procedure-1:

Procedure:
----------

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_e1.png
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_e2.png
   :align: center
   :width: 100px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_e3.png
   :align: center
   :width: 100px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_e4.png
   :align: center
   :width: 300px

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_e5.png
   :align: center
   :width: 300px

where:

| V\ :sub:`T` is the Thermal Voltage
| I\ :sub:`C` is the collector current
| V\ :sub:`BE` is the base-emitter voltage
| ∆V\ :sub:`BE` is the base-emitter offset voltage
| k is Boltzmann's constant
| q is the electron charge
| T is the absolute temperature
| ln is the natural log
| I\ :sub:`S` is the collector-emitter saturation current

| When the collector-emitter saturation currents (emitter area) are equal, they cancel each other out, and Equation 4 reduces to Equation 5.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf16.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 16, I\ :sub:`E` vs V\ :sub:`BE` Scopy Plot


The I\ :sub:`E` vs. V\ :sub:`BE` data for two different size transistors is plotted in the next two graphs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f11.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 17, I\ :sub:`E` vs. V\ :sub:`BE`


.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f12.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 18, I\ :sub:`E` vs. V\ :sub:`BE`


The difference between these two curves, or delta V\ :sub:`BE`, is plotted here. It can be seen that this difference is relatively constant over a wide range of current and is about 66 mV. From our V\ :sub:`BE` equations this calculates to an effective emitter area difference of 12.7 between the two devices.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f13.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 19, DV\ :sub:`BE` 2S1815 / 2D438


.. _questions-1:

Questions:
----------

-  From the measured data calculate the current gain Beta ( I\ :sub:`C`/I\ :sub:`B` ) for each device.
-  Using the curve for the highest base current step, calculate the early voltage for each device.
-  Calculate the Beta Early voltage product ( b*VA) for each device.
-  Compare your results with manufacturer specifications for each device measured.

Alternative Method
==================

The circuits used earlier to make these measurements use the differential nature of the scope input channels of the ADALM2000 hardware. This was done, in part, to facilitate the conversion of the AWG’s voltage output into a current suitable to drive the transistor’s base. You may not always have access to instruments with differential input capability, such as standard bench top Oscilloscopes or the Analog Explorer student lab system. The following configuration, shown in figure 10, allows both the collector emitter voltage V\ :sub:`CE` and the collector current I\ :sub:`C` to be measured with ground referenced, singled ended, scope inputs while still converting the AWG voltage output into a suitable base current.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f14.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 20, Alternate curve tracer circuit


The circuit is built from one dual op-amp (ADTL082 for example or two single amplifiers) and a handful of resistors. Amplifier A1 is configured as a current to voltage converter such that the collector of the device under test (DUT) is forced to (virtual) ground and the voltage seen at its output represents I\ :sub:`C` = V\ :sub:`Scope2`/100. The second amplifier, A2, is configured as what is known as the “improved” Howland current source. The staircase voltage from AWG2 is converted into a current and applied to the base of the DUT. The emitter of the DUT, and thus the V\ :sub:`CE` is swept by the voltage of AWG1. The Howland current source will supply a fixed current independent of the emitter (and base) voltage. Since the collector of the DUT is at ground, the voltage ramp supplied by AWG1 must be negative, i.e. from -5V (or whatever the maximum negative voltage from the source is) to 0V. This is the minor concession that must be made to accommodate the single ended signal measurements. The V\ :sub:`CE` as measured by Scope1 will need to be inverted to display a positive V\ :sub:`CE` on the horizontal axis.

This same circuit can be used to measure PNP devices by simply configuring the ramp signal to be positive, i.e. from 0V to the maximum positive swing of the source.

.. admonition:: Download
   :class: download

   \*\* Lab Resources:\*\*

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/bjt_curve_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/bjt_curve_ltspice`
   -  Stairstep signal: :git-education_tools:`stairstep <m2k/import_waveforms/waveforms_sg/stairstep.csv>`
   


For further reading on the Howland current source:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`http://www.analog.com/static/imported-files/application_notes/236037846AN_843.pdf <static/imported-files/application_notes/236037846AN_843.pdf>`

http://michaelgellis.tripod.com/howland.html

http://falstad.com/circuit/e-howland.html

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/a4_f3.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/a4_nf10.png
