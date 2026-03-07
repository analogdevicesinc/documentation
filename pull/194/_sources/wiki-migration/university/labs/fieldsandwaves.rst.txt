Active Learning Module Lab Activities for Electromagnetic Fields and Waves
==========================================================================

Analog Devices is as passionate about educating the next generation of young electrical engineers as it is about pioneering the next technological breakthrough. The Active Learning Program is a platform where Analog Devices, working with leading educational institutions has created and deployed new hands on learning tools for the next generation of analog circuit design engineers. This University Program brings the analog signal processing technology the company has developed to the academic community in a way that is open and accessible to faculty and students in the form of analog design kits and analog component kits, online and downloadable software and teaching materials, online support, textbooks, reference designs and lab projects to enrich students’ education in electrical engineering and the application to core engineering and physical science curricula.

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

Electromagnetic Fields and Waves Lab
------------------------------------

The purpose of this lab class is to give the student a practical sense of what electromagnetics is. This very fundamental area has been an essential part of electrical engineering since it became a separate discipline in the overall Engineering profession in the late 1800s.

For nearly all of these lab activities, you will be connecting a signal source to the input of some circuit or network and observing both the input and output voltage waveforms. Be sure that you always observe both Vin and Vout on the oscilloscope channels. If you only observe what is happening at the output of the circuit, you will have learned little or nothing about how the circuit operates.

Circuit Simulation
~~~~~~~~~~~~~~~~~~

| Basic information and material on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`, including tool links and usage information.
| Many of the labs are populated with :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic.

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

The labs are generally written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI and our authorized distribution channels, however additional devices are sometimes needed (additional information on component selection included below).

Lab Activities and Exercises
----------------------------

+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Class | Activity Topic                     | ADALM1000 (M1K)                                                                                                             | ADALM2000 (M2K)                                                                                                |
+=======+====================================+=============================================================================================================================+================================================================================================================+
| #1    | Concept:                           | :doc:`Capacitive Coupling </wiki-migration/university/courses/fieldsandwaves/m1k-capacitive-coupling-lab>`                  |                                                                                                                |
|       | Capacitive Coupling                |                                                                                                                             |                                                                                                                |
+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| #2    | Concept:                           | :doc:`Magnetic Coupling </wiki-migration/university/courses/fieldsandwaves/m1k-magnetic-coupling-lab>`                      |                                                                                                                |
|       | Magnetic Coupling                  |                                                                                                                             |                                                                                                                |
+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| #3    | Concept:                           | :doc:`EMI radiation and electromagnetic signal propagation </wiki-migration/university/courses/fieldsandwaves/m1k-emi-lab>` |                                                                                                                |
|       | EMI radiation and wave propagation |                                                                                                                             |                                                                                                                |
+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| #4    | Concept:                           | :doc:`Magnetic Proximity Sensor </wiki-migration/university/courses/engineering_discovery/lab_6>`                           |                                                                                                                |
|       | Magnetic sensors                   |                                                                                                                             |                                                                                                                |
+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| #5    | Concept:                           | :doc:`Artificial Transmission Lines I </wiki-migration/university/courses/alm1k/alm-lc-atline>`                             | :doc:`Transmission Lines and Standing Waves </wiki-migration/university/labs/tlines_standing_waves_adalm2000>` |
|       | Transmission lines                 | :doc:`Artificial Transmission Lines II </wiki-migration/university/courses/fieldsandwaves/m1k-alt-notch-filter-lab>`        |                                                                                                                |
+-------+------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

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

**Return to Fields and Waves Course Material Table of Contents**
