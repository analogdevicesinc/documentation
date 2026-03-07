Circuits I and Circuits II Based Lab Activity Material
======================================================

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

Lab Preparation
---------------

Circuit Simulation
~~~~~~~~~~~~~~~~~~

Basic information and material on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`, including tool links and usage information. :adi:`Get Up and Running with LTspice <media/en/analog-dialogue/volume-53/number-4/get-up-and-running-with-ltspice.pdf>`.

| Most of the labs are populated with :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic. A file containing the ADALM2000 connections for the schematics can be found here: :git-education_tools:`m2k/ltspice/m2k_conn_ltspice`.

+-------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Course      | ADALM1000 (M1K)                                                                                            | ADALM2000 (M2K)                                                                                                       |
+=============+============================================================================================================+=======================================================================================================================+
| Circuits I  | `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electronics-lab-i.zip>`_   | :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-i>`                                               |
+-------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Circuits II | `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electroincs-lab-ii.zip>`_  | :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-ii>`                                              |
+-------------+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

Lab Hardware and Software
~~~~~~~~~~~~~~~~~~~~~~~~~

These labs can be performed using the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) entry level Active Learning Module or the :doc:`ADALM2000 </wiki-migration/university/tools/m2k>` (M2K) more advanced level Active Learning Module. :doc:`This document </wiki-migration/university/courses/alm1k/m2k-convert-labs>` outlines how labs might be altered for use with either M1K or M2K.

+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+
|             | ADALM1000 (M1K)                                                                | ADALM2000 (M2K)                                           |
+=============+================================================================================+===========================================================+
| PC Software | :doc:`ALICE </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` | :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` |
+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+

The ALICE Windows executable installer, in addition to the main ALICE Desktop program, includes the following DC measurement tools:

-  DC Voltmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/voltmeter_lab-0.pdf>`_ (volt-meter-tool-1.2.exe)
-  DC Ohmmeter `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/ohmmeter_lab-0.pdf>`_ (ohm-meter-vdiv-1.2.exe)
-  DC Meter-Source `Quick Start Guide <https://wiki.analog.com/_media/university/tools/m1k/alice/meter-source-lab0.pdf>`_ (dc-meter-source-tool-1.3.exe)

:doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

The labs are generally written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI and our authorized distribution channels, however additional devices are sometimes needed.

General Lab materials
~~~~~~~~~~~~~~~~~~~~~

-  Background Lab Notes: :doc:`Solder-less Breadboards </wiki-migration/university/courses/electronics/electronics-lab-breadboards>`
-  Background Lab Activity: :doc:`Solder-less Breadboard Parasitic Capacitance </wiki-migration/university/courses/electronics/electronics-lab-breadboard-coupling>`
-  Background Lab Notes: :doc:`Resistors </wiki-migration/university/courses/electronics/electronics-lab-resistors>` (including color code)
-  Background Lab Notes: :doc:`Capacitors </wiki-migration/university/courses/electronics/electronics-lab-capacitors>` (including color code)
-  Review Activity: :doc:`Real Voltage Sources </wiki-migration/university/courses/alm1k/intro/real-voltage-sources>`
-  Review Activity: :doc:`Rechargeable Batteries </wiki-migration/university/courses/alm1k/alm-lab-e1>`
-  Basic Activity: :doc:`Energy Harvesting </wiki-migration/university/courses/electronics/electronics-lab-eh>`
-  :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`
-  :doc:`How to Generate External Signal Sources </wiki-migration/university/courses/alm1k/circuits1/alm-cir-signal-generators>`
-  :doc:`Battery Voltage "Rail-Splitter" </wiki-migration/university/courses/alm1k/circuits1/alm_cir_lab-rail-splitter>`
-  :doc:`Bipolar power supplies for active learning labs </wiki-migration/university/courses/alm1k/circuits1/alm-bipolar-step-up-dc-dc>`

Lab Activities and Exercises
----------------------------

Circuits I
~~~~~~~~~~

+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Section | ADALM1000 (M1K)                                                                                                              | ADALM2000 (M2K)                                                                                                           |
+=========+==============================================================================================================================+===========================================================================================================================+
| Lab #   | :doc:`Ohm's Law </wiki-migration/university/courses/alm1k/intro/ohm-law-1>`                                                  | :doc:`An Ohm's Law Experiment </wiki-migration/university/courses/electronics/ohm_law>`                                   |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Kirchhoff’s Voltage and Current Laws </wiki-migration/university/courses/alm1k/circuits1/alm-cir-1>`                   |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Voltage and Current Division </wiki-migration/university/courses/alm1k/circuits1/alm-cir-2>`                           |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Proportionality and Superposition </wiki-migration/university/courses/alm1k/circuits1/alm-cir-3>`                      |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`DC Power </wiki-migration/university/courses/alm1k/intro/power-part1-dc>`                                              |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Thévenin Equivalent Circuit and Maximum Power Transfer </wiki-migration/university/courses/alm1k/circuits1/alm-cir-4>` |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Introduction to Two-Port Networks </wiki-migration/university/courses/alm1k/circuits1/alm-cir-two-port-network>`       |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Transient Response of an RC Circuit </wiki-migration/university/courses/alm1k/circuits1/alm-cir-5>`                    | :doc:`Transient Response of an RC Circuit </wiki-migration/university/courses/electronics/rc_transient_response>`         |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Transient Response of an RL Circuit </wiki-migration/university/courses/alm1k/circuits1/alm-cir-6>`                    | :doc:`Transient Response of an RL Circuit </wiki-migration/university/courses/electronics/rl_transient_response>`         |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`What is Phase </wiki-migration/university/courses/alm1k/circuits1/alm-cir-phase1>`                                     |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Resonance in RLC Circuits </wiki-migration/university/courses/alm1k/circuits1/alm-cir-7>`                              | :doc:`Resonance in RLC Circuits </wiki-migration/university/courses/electronics/rlc_resonance>`                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Parallel LC Resonance and energy storage </wiki-migration/university/courses/alm1k/circuits1/alm-cir-lc-resonator>`    |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`AC Power and Power Factor </wiki-migration/university/courses/alm1k/circuits1/alm-cir-ac-power-factor>`                |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Low Pass and High Pass Filters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-8>`                         | :doc:`Low Pass and High Pass Filters </wiki-migration/university/courses/electronics/lp_hp_filters>`                      |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Frequency compensated voltage dividers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-voltage-divider>`   |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Band Pass Filters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-9>`                                      | :doc:`Band Pass Filters </wiki-migration/university/labs/band_pass_filters_adalm200>`                                     |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Band Stop or Reject Filters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-band-reject-filters>`          | :doc:`Band Stop Filters </wiki-migration/university/labs/band_stop_filters_adalm2000>`                                    |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Cascaded RC Low Pass Filters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-cascade-rc>`                  | :doc:`Cascaded RC low pass filters </wiki-migration/university/labs/cascaded_rc_adalm2000>`                               |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Impedance Measurement - Frequency Effects </wiki-migration/university/courses/alm1k/circuits1/alm-cir-10>`             |                                                                                                                           |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Measuring Loudspeaker Impedance Profile </wiki-migration/university/courses/alm1k/circuits1/alm-cir-11>`               | :doc:`Measuring a Loudspeaker Impedance Profile </wiki-migration/university/courses/electronics/electronics-lab-speaker>` |
+---------+------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

Circuits II
~~~~~~~~~~~

+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Section | ADALM1000 (M1K)                                                                                                                       | ADALM2000 (M2K)                                                                                               |
+=========+=======================================================================================================================================+===============================================================================================================+
| Lab #   | :doc:`Basic OP Amp Configurations </wiki-migration/university/courses/alm1k/alm-lab-1>`                                               | :doc:`Simple Op Amps </wiki-migration/university/courses/electronics/electronics-lab-1>`                      |
|         |                                                                                                                                       | :doc:`Op Amp Settling Time </wiki-migration/university/courses/electronics/electronics-lab-1st>`              |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Op-Amp Open-Loop Gain </wiki-migration/university/courses/alm1k/alm-lab-olg>`                                                   | :doc:`Measuring Loop Gain </wiki-migration/university/courses/electronics/electronics-lab-loop-gain>`         |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Op-Amp Gain Bandwidth Product </wiki-migration/university/courses/alm1k/alm-lab-gbw>`                                           |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Vector Summing Amplifier </wiki-migration/university/courses/alm1k/alm-lab-vectrosumamp>`                                       |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Difference Amplifier </wiki-migration/university/courses/alm1k/alm-lab-diffamp>`                                                |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Current Sensing, Difference Amplifier </wiki-migration/university/courses/alm1k/alm-lab-current-sense>`                         |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`The Voltage Comparator </wiki-migration/university/courses/alm1k/alm-lab-comp>`                                                 | :doc:`Op Amp as Comparator </wiki-migration/university/courses/electronics/electronics-lab-opamp-comparator>` |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`PN Diode I/V curves </wiki-migration/university/courses/alm1k/alm-lab-2>`                                                       | :doc:`PN Diode I/V curves </wiki-migration/university/courses/electronics/electronics-lab-2>`                 |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Diode Rectifiers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-diode-rectifier>`                                  |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Precision Rectifiers, Absolute value circuits </wiki-migration/university/courses/alm1k/circuits1/alm-cir-precision-rectifier>` |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`BJT as a diode </wiki-migration/university/courses/alm1k/alm-lab-3>`                                                            |                                                                                                               |
|         | :doc:`MOS as a diode </wiki-migration/university/courses/alm1k/alm-lab-3m>`                                                           |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | Device I/V curves, :doc:`BJT </wiki-migration/university/courses/alm1k/alm-lab-4>`                                                    |                                                                                                               |
|         | :doc:`MOS </wiki-migration/university/courses/alm1k/alm-lab-4m>`                                                                      |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | Transistor as a switch, :doc:`BJT </wiki-migration/university/courses/alm1k/alm-lab-4s>`                                              |                                                                                                               |
|         | :doc:`MOS </wiki-migration/university/courses/alm1k/alm-lab-4ms>`                                                                     |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Common Emitter Amplifier </wiki-migration/university/courses/alm1k/alm-lab-5>`                                                  |                                                                                                               |
|         | :doc:`Common Source Amplifier </wiki-migration/university/courses/alm1k/alm-lab-5m>`                                                  |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`DC-DC Boost Converters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-15a>` ( inductors )                          |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Lab #   | :doc:`Simple "Joule Thief" DC/DC Converter </wiki-migration/university/courses/alm1k/circuits1/alm-joule-thief>`                      |                                                                                                               |
+---------+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

General background Information.
-------------------------------

The assumption is made that the reader has some familiarity with either the ADALM1000 Lab hardware and ALICE software system or the ADALM2000 Lab hardware and Scopy software system, before starting these lab activities depending on which set of labs are to be preformed.

Things to think about
---------------------

Learning to mathematically analyze circuits requires much study and practice. Typically, students practice by working through lots of sample problems and checking their answers against those provided by the textbook or the instructor. While this is good, there is a much better way. You will learn much more by actually building and analyzing real circuits, letting your test equipment provide the "answers" instead of a book or another person. For successful circuit-building exercises, follow these steps:

1. Carefully measure and record all component values prior to circuit construction, choosing resistor values high enough to make damage to any active components unlikely.

2. Draw the schematic diagram for the circuit to be analyzed. Or perhaps print out the schematics shown in these lab activities.

3. Carefully build this circuit on your breadboard.

4. Before applying power to your circuit check the accuracy of the circuit's construction, following each wire to each connection point, and verifying these elements one-by-one on the diagram.

5. Mathematically analyze the circuit, solving for all voltage and current values. Circuit simulation software such as LTSpice can be very useful for automating this process.

6. Carefully measure all voltages and currents, to verify the accuracy of your analysis.

7. If there are any substantial errors (greater than a few percent), carefully check your circuit's construction against the diagram, then carefully re-calculate the values and re-measure.

One way you can save time and reduce the possibility of error is to begin with a very simple circuit and incrementally add components to increase its complexity after each analysis, rather than building a whole new circuit for each practice activity. Another time-saving technique is to re-use the same components in a variety of different circuit configurations. This way, you won't have to measure any component's value more than once.

The Good Lab Report
===================

When performing lab tests, whether in college or industry, the lab report is vital for communicating the results in a logically ordered, readable fashion to others. To ensure readability, the report should be done using a word processor that can do text formatting, as well as math equation editing and drawing simple diagrams and schematics. A spell checker is useful to avoid spelling mistakes. All sections of the lab should be organized in some logical fashion, for example in the order the steps were performed. Material in later sections should reference any related material in previous sections.

The following section describes the layout that should be used.

In order to write a successful lab report it should contain the following key elements: objectives, pre lab calculations, equipment used, methods, results discussion, and end with conclusions.

Objectives
----------

The objectives section should be a brief one paragraph summary of the objectives of the lab experiments. In other words, this section should contain a short list of the steps to be performed as well as the expected test results.

Pre lab
-------

Any preparation that was done prior to the lab should be presented here. This section should contain a short list of tests to be performed as well as the expected results. Expected pre-lab calculations or other work such as circuit simulations is often set out in the Lab worksheet.

Equipment and Materials
-----------------------

This section includes a list of equipment, hardware and material used to perform the experiments. This list should include the make and model of any equipment used and a complete list of parts. Expected components, hardware and equipment to be used is often set out in the Lab worksheet.

Methods
-------

The Methods section should include detailed descriptions of each of the experiments to be performed. This should include both a description of the circuit and the test setup used to acquire the measured data. The measured data should not be included in this section, but rather in the results section. When describing the circuits and test setups, all relevant descriptions should be illustrated with diagrams and/or schematics. Enough information should be provided so that the reader can repeat the experiment completely.

Results and Discussion
----------------------

All of the test results should be included here. The results from each experiment should be presented in the same order as it was in the above methods section. The data or each experiment should be presented in a logical, concise format such as a graph or a table. Graphs should be completely labeled and all the axis should be scaled correctly. Sketches should be to scale with all pertinent points measured and marked correctly. Spreadsheet programs are a good way to generate graphs of your data. Much of the tests are performed using computer software tools. These tools often provide a means to save data or screen images to a file for inclusion in your lab report. Finally, the data should be discussed. Any apparent errors or unexpected results should be discussed.

Conclusions
-----------

At the end sum up your results and lessons learned from problems and mistakes made along the way. A few comments on next steps or further work to examine the subject matter in more depth is also a good practice.

Measurement Errors
------------------

There is no such thing as a perfect or ideal measurement which provides the "true value" of the measured quantity. There are a number of reasons for this, from limitations of the measurement equipment used and those of the observer, to the variations in the components in the circuit for which the measurement is made. This does not mean that good, useful measurements are not possible. Obtaining them requires not only adequate instruments but also some attention and vigilance against common mistakes which seem to lurk in even the best of laboratory setups. Gross mistakes are such errors as connecting a voltmeter lead to a wrong point in a circuit or entering data incorrectly into a notebook or a computer. These can be avoided by following proper procedures, careful data recording etc. Here we are concerned with two other important concepts: accuracy and precision.

Accuracy can be defined as the difference between the value obtained from measurement and a real "true" value of a quantity. It can be expressed in absolute numbers, such as 10 mV, or in relative numbers, such as 0.5%. In the first case the measured voltage may be different from the actual voltage by no more than 10 mV, in the second by the given percentage. Accuracy is difficult to determine, because we never know what the real value of the measured quantity is, but it can be roughly estimated if we know the precision of instrument and the reliability of it's calibration.

Precision of a measurement is related to the smallest difference between the measured values that can be distinguished. For example, if a voltmeter precision is 0.1 V we could measure the difference between 10.2 V and 10.3 V but no better. A reading of 10.25 may be assigned to either of these values, we could not tell. Precision is often confused with the resolution of the instrument scale. Just because an instrument has a finely divided scale on which we can read numbers "precisely" (true for many digital instruments), it does not necessarily follow that the measurement is precise. It may happen that when you disconnect the meter and connect it again to the same source you get a different reading on the same "precise" scale. It is generally true, however, that more precise instruments are designed with finer scales or more digits in their numerical display.

To understand better the difference between accuracy and precision consider a voltmeter that measures voltage consistently and reliably with the precision of 1 mV. A measurement of the voltage of an accurate standard source used for calibration of instruments gives a voltage 5 mV too high. This last error is the measure of the voltmeter accuracy. Its measurements were quite precise but the instrument was not well calibrated and showed consistently higher values. Such an instrument is still quite useful since we are often interested in comparing different voltages and this meter is able to measure the ratio of two voltages much better than it measures their absolute values.

In considering the effect of precision of instruments on measurement errors we are usually concerned with relative rather than absolute numbers. An error of 0.1 V for measurement of power line voltage of 117 V is very acceptable, since it gives the relative error of 0.1/117 < 0.1 % The same absolute error in a measurement of an amplifier output of 1 V gives a large relative error of 10%.

Information on component selection
==================================

First, here are a few words about components that might be suitable for use in these lab experiments. Transistors that can be used are general purpose NPN types like the popular 2N3904 NPN and the 2N3906 PNP complement. Similar type devices can be used such as the common 2SC1815 and the 2SA1015 PNP devices which are also considered comparable complements of each other. A supply of various diodes, resistors, capacitors and inductors should also be available. Another potential source of transistors for use in these lab exercises are transistor arrays such as the LM3045 / LM3046 / LM3086 NPN Arrays from National Semiconductor. Similar NPN arrays from Intersil are, CA3045 / CA3046 / CA3083. Arrays of two or four 2N2222, 2N3904, 2N3906 and other types are available from some manufacturers like Fairchild and ON Semiconductor. A readily available enhancement mode NMOS transistor is the 2N7000. Advanced Linear Devices Inc. offers dual and quad N and P channel MOS arrays (ALD1106 and ALD1107) as well. The CD4007C CMOS logic package consists of three complementary pairs of N and P-channel enhancement mode MOS transistors. The N and P type pairs share either a common gate or common drain terminal which limits their use as six individual devices but these devices can still be useful for Lab experiments.

Remember, not all transistors share the same terminal designations, or pinouts, even if they share the same physical appearance. The order of some types is CBE (base is center lead) and BCE (collector is center lead) for others. This is very important when you connect the transistors together and to other components. Be careful to check the manufacturer's specifications (component datasheet). These can be easily found on various websites. Double-checking pin identities with a multi-meter's "diode check" function is highly recommended.

Note about diodes and bandgap conventions:
==========================================

The common convention is that a typical silicon BJT base–emitter diode drop, ``VBE``, is 0.65V and a standard general purpose silicon diode drop is 0.6V. Other conventions use 0.6V or 0.7V for one or both. These are highly dependent on the manufacturing process used and the physical size of the components. The results you measure in the laboratory will most likely be between these values. Diodes and BJTs implemented on the same integrated circuit (i.e., on the same silicon die) may have equivalent characteristics. That is, the diodes and transistors will be more closely matched. Matched components are convenient to use in many circuit designs. We use discrete elements in most of these activities, and so it is not possible to match components unless they are all fabricated on the same silicon die. In the laboratory, a diode-connected transistor, with its base shorted to its collector may match the base–emitter characteristics of another transistor of the same type better than a simple diode.

Diode drops are strongly temperature dependent. Room-temperature transistors (~27ºC or 300ºK) have base–emitter drops around 0.65V, but as the temperature of the transistors increases, ``VBE`` drops near 0.5V. So temperature matching is just as important as component matching. Internal temperature compensation in bandgap voltage references lets them provide a temperature-independent voltage reference. Their output reference of ∼1.22V is the extrapolated ``VBE`` at absolute zero (i.e., 0ºK or −273.15ºC). It is not a coincidence that the Silicon bandgap (i.e., the energy separating valence and conduction electron bands) is ∼1.22 eV.

Temperature dependence and manufacturing variations (and the Early effect) are always a concern.

**Return to Circuits I & Circuits II Course Material** :doc:`Table of Contents </wiki-migration/university/courses/circuits>`
