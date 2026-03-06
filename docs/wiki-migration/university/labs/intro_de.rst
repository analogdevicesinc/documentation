Introduction to Digital Electronics Based Lab Activity Material
===============================================================

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

Lab Preparation
---------------

Circuit Simulation
~~~~~~~~~~~~~~~~~~

Basic information and material on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`, including tool links and usage information. :adi:`Get Up and Running with LTspice <media/en/analog-dialogue/volume-53/number-4/get-up-and-running-with-ltspice.pdf>`.

| Most of the labs are populated with :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic. A file containing the ADALM2000 connections for the schematics can be found here: :git-education_tools:`m2k/ltspice/m2k_conn_ltspice`.

+---------------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Course                    | ADALM1000 (M1K)                                                                                           | ADALM2000 (M2K)                                                                                                      |
+===========================+===========================================================================================================+======================================================================================================================+
| Intro Digital Electronics | `schematic files <https://wiki.analog.com/_media/university/courses/electronics/electronics-lab-i.zip>`__ | :git-education_tools:`schematic files <m2k/adisimpe/electronics-lab-i>`                                              |
+---------------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Lab Hardware and Software
~~~~~~~~~~~~~~~~~~~~~~~~~

These labs can be performed using the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) entry level Active Learning Module or the :doc:`ADALM2000 </wiki-migration/university/tools/m2k>` (M2K) more advanced level Active Learning Module. :doc:`This document </wiki-migration/university/courses/alm1k/m2k-convert-labs>` outlines how labs might be altered for use with either M1K or M2K.

+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+
|             | ADALM1000 (M1K)                                                                | ADALM2000 (M2K)                                           |
+=============+================================================================================+===========================================================+
| PC Software | :doc:`ALICE </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` | :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` |
+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+

The labs are generally written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI and our authorized distribution channels, however additional devices are sometimes needed (additional information on component selection included below).

:doc:`Oscilloscope Terminology </wiki-migration/university/courses/alm1k/intro/oscilloscope-terminology>`

Lab Activities and Exercises
----------------------------

.. note::

   Course topics List to be filled in as new lab pages are generated:


+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Class | Activity Topic                    | ADALM1000 (M1K)                                                                                                | ADALM2000 (M2K)                                                                                                            |
+=======+===================================+================================================================================================================+============================================================================================================================+
| #1    | Concept:                          | :doc:`Basic Logic Gates </wiki-migration/university/courses/alm1k/intro/basic-logic-gates-1>`                  |                                                                                                                            |
|       | Introduction to Logic Design      |                                                                                                                |                                                                                                                            |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #2    | Concept:                          | :doc:`NPN </wiki-migration/university/courses/alm1k/alm-lab-24>`                                               | :doc:`NPN </wiki-migration/university/courses/electronics/electronics-lab-24>`                                             |
|       | Multivibrators                    | :doc:`NMOS </wiki-migration/university/courses/alm1k/alm-lab-24m>`                                             | :doc:`NMOS </wiki-migration/university/courses/electronics/electronics-lab-24m>`                                           |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #3    | Concept:                          | :doc:`TTL inverter and NAND gate </wiki-migration/university/courses/alm1k/alm-lab-27>`                        | :doc:`TTL inverter and NAND gate </wiki-migration/university/courses/electronics/electronics-lab-27>`                      |
|       | TTL Logic                         |                                                                                                                |                                                                                                                            |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #4    | Concept:                          | :doc:`CMOS Logic Functions Using CD4007 Array </wiki-migration/university/courses/alm1k/alm-lab-28>`           | :doc:`CMOS Logic Functions Using CD4007 Array </wiki-migration/university/courses/electronics/electronics-lab-28>`         |
|       | CMOS Logic                        | :doc:`Transmission Gate XOR </wiki-migration/university/courses/alm1k/alm-lab-30>`                             | :doc:`Transmission Gate XOR </wiki-migration/university/courses/electronics/electronics-lab-30>`                           |
|       |                                   | :doc:`D Type Latch </wiki-migration/university/courses/alm1k/alm-lab-29>`                                      | :doc:`D Type Latch </wiki-migration/university/courses/electronics/electronics-lab-29>`                                    |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #5    | Concept:                          | :doc:`Logic Voltage Level Shifting </wiki-migration/university/courses/alm1k/alm-lab-voltage-level-shifter>`   | :doc:`Logic Voltage Level Shifting </wiki-migration/university/courses/electronics/electronics-lab-voltage-level-shifter>` |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #6    | Concept:                          | :doc:`Linear Feedback Shift Register </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-lfsr-lab>` | :doc:`Linear Feedback Shift Register (LFSR) </wiki-migration/university/courses/electronics/comms-lab-lfsr>`               |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #7    | Concept:                          | :doc:`CMOS Ring Oscillator </wiki-migration/university/courses/alm1k/alm-lab-ring-osc>`                        |                                                                                                                            |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #8    | Concept:                          | :doc:`CMOS Ring Oscillator Frequency Multiplier </wiki-migration/university/courses/alm1k/alm-lab-ring-3x>`    |                                                                                                                            |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| #10   | Concept:                          | :doc:`Software Controlling LEDs </wiki-migration/university/tools/python-tutorial/tutorial1-toggle-led>`       |                                                                                                                            |
|       | Digital Electronics               | :doc:`Reading Push Button Switches </wiki-migration/university/tools/python-tutorial/tutorial2-read-buttons>`  |                                                                                                                            |
|       | Interfacing Hardware and Software | :doc:`Reading a Potentiometer </wiki-migration/university/tools/python-tutorial/tutorial3-potentiometer>`      |                                                                                                                            |
|       |                                   | :doc:`Stepper Motor Control </wiki-migration/university/courses/alm1k/intro/stepper-motor-drive-1>`            |                                                                                                                            |
+-------+-----------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

General background Information.
-------------------------------

The assumption is made that the reader has some familiarity with either the ADALM1000 Lab hardware and ALICE software system or the ADALM2000 Lab hardware and Scopy software system, before starting these lab activities depending on which set of labs are to be preformed.

Things to think about
---------------------

Learning to mathematically analyze circuits requires much study and practice. Typically, students practice by working through lots of sample problems and checking their answers against those provided by the textbook or the instructor. While this is good, there is a much better way. You will learn much more by actually building and analyzing real circuits, letting your test equipment provide the "answers" instead of a book or another person. For successful circuit-building exercises, follow these steps:

1. Draw the schematic diagram for the circuit to be analyzed. Or perhaps print out the schematics shown in these lab activities.

2. Carefully build this circuit on your breadboard.

3. Before applying power to your circuit check the accuracy of the circuit's construction, following each wire to each connection point, and verifying these elements one-by-one on the diagram.

4. Mathematically analyze the circuit. Circuit simulation software such as LTSpice can be very useful for automating this process.

5. Carefully measure all voltages to verify the accuracy of your analysis.

6. If there are any substantial differences, carefully check your circuit's construction against the diagram, then carefully re-calculate the values and re-measure.

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

Information on component selection
==================================

First, here are a few words about components that might be suitable for use in these lab experiments. The Labs generally use the 4 74HC series logic gates from the ADALP2000 parts kit. Logic gates and other more complex components from the 74HC series can be substitutes depending on availability. Other logic families such as LSTTL or CD4000 series CMOS are possible alternatives as well.

**Return to Introduction to Digital Electronics Course Material** :doc:`Table of Contents </wiki-migration/university/courses/intro_de>`
