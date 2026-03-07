Power Based Lab Activity Material
=================================

The laboratory activities provided on this wiki are considered open source and available for free use in non-commercial educational and academic settings. **The only requirement is that they continue to retain the attribution to Analog Devices Inc.** Supplying them on the ADI wiki allows registered users to contribute to the materials posted here improving the content and keeping them up to date.

Lab Preparation
---------------

Circuit Simulation
~~~~~~~~~~~~~~~~~~

| Basic information and material on :doc:`circuit simulation </wiki-migration/university/courses/electronics/circuitsimulationnotes>`, including tool links and usage information.
| Most of the labs are populated with :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>` resource files which contain the schematics of the circuits discussed at a specific topic. A zip file with all M1K-specific and M2K-specific LTspice files for all lab exercises can be downloaded here:

+----------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Course   | ADALM1000 (M1K)                                                                                     | ADALM2000 (M2K)                                                                                     |
+==========+=====================================================================================================+=====================================================================================================+
| All Labs | :git-education_tools:`M1K LTspice files <m1k/ltspice>`                                              | :git-education_tools:`M2K LTspice files <m2k/ltspice>`                                              |
+----------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

| An LTspice file containing the ADALM2000 connections for the schematics can be found here: :git-education_tools:`m2k/ltspice/m2k_conn_ltspice`.

Lab Hardware and Software
~~~~~~~~~~~~~~~~~~~~~~~~~

These labs can be performed using the :doc:`ADALM2000 </wiki-migration/university/tools/m2k>` (M2K) Active Learning Module , or the :doc:`ADALM1000 </wiki-migration/university/tools/m1k>` (M1K) entry level design instrumentation.

+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+
|             | ADALM1000 (M1K)                                                                | ADALM2000 (M2K)                                           |
+=============+================================================================================+===========================================================+
| PC Software | :doc:`ALICE </wiki-migration/university/tools/m1k/alice/desk-top-users-guide>` | :doc:`Scopy </wiki-migration/university/tools/m2k/scopy>` |
+-------------+--------------------------------------------------------------------------------+-----------------------------------------------------------+

The labs are generally written to be performed using just the components provided in the Analog Parts Kit, :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>`, supplied through ADI and our authorized distribution channels, however additional devices are sometimes needed.

General Lab materials
~~~~~~~~~~~~~~~~~~~~~

Many of the power electronics labs require some additional equipment beyond the M1K, M2K, and parts kit.

-  An adjustable bench top power supply with constant voltage / constant current / current limit operation.
-  An adjustable electronic load and / or various power resistors mounted to heat sinks.
-  Some of the labs can be performed with optional hardware, such as the :adi:`ADALM-BUCK-ARDZ`
-  :adi:`Inductor Current Measurement in Switched Power Supplies <en/analog-dialogue/raqs/raq-issue-170.html>`

+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Topic                              | ADALM1000 (M1K)                                                                                                       | ADALM2000 (M2K)                                                                                                              |
+====================================+=======================================================================================================================+==============================================================================================================================+
| Diodes                             | :doc:`PN Diode I/V curves </wiki-migration/university/courses/alm1k/alm-lab-2>`                                       | :doc:`PN Diode I/V curves </wiki-migration/university/courses/electronics/electronics-lab-2>`                                |
|                                    | :doc:`Zener Diode I/V curves </wiki-migration/university/courses/alm1k/alm-lab-zener-diode>`                          | :doc:`Zener diode regulator </wiki-migration/university/courses/electronics/electronics-lab-26>`                             |
|                                    | :doc:`Diode Rectifiers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-diode-rectifier>`                  | :doc:`BJT as a diode </wiki-migration/university/courses/electronics/electronics-lab-3>`                                     |
|                                    | :doc:`BJT as a diode </wiki-migration/university/courses/alm1k/alm-lab-3>`                                            | :doc:`MOS as a diode </wiki-migration/university/courses/electronics/electronics-lab-3m>`                                    |
|                                    | :doc:`MOS as a diode </wiki-migration/university/courses/alm1k/alm-lab-3m>`                                           |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Active Rectifiers                  | :doc:`Active Rectifiers </wiki-migration/university/courses/alm1k/alm-active-rectifiers>`                             |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Bipolar Junction Transistors (BJT) | :doc:`BJT Device I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4>`                                     | :doc:`BJT Device I/V curves </wiki-migration/university/courses/electronics/electronics-lab-4>`                              |
|                                    | :doc:`BJT as a switch </wiki-migration/university/courses/alm1k/alm-lab-4s>`                                          |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Metal Oxide Transistors (MOS)      | :doc:`MOS Device I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4m>`                                    | :doc:`MOS Device I/V curves </wiki-migration/university/courses/electronics/electronics-lab-4m>`                             |
|                                    | :doc:`MOS as a switch </wiki-migration/university/courses/alm1k/alm-lab-4ms>`                                         |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Voltage Reference                  | :doc:`Regulated Voltage Reference </wiki-migration/university/courses/alm1k/alm-lab-9>`                               | :doc:`Regulated Voltage Reference </wiki-migration/university/courses/electronics/electronics-lab-9>`                        |
|                                    | :doc:`Shunt Voltage Regulator </wiki-migration/university/courses/alm1k/alm-lab-10>`                                  | :doc:`Shunt voltage regulator </wiki-migration/university/courses/electronics/electronics-lab-10>`                           |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Power Basics                       | :doc:`Efficiency, Power Loss, and Thermal Management </wiki-migration/university/courses/alm1k/alm-power-efficiency>` | :doc:`Efficiency, Power Loss, and Thermal Management </wiki-migration/university/courses/electronics/efficiency_power_loss>` |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Current Sensing                    | :doc:`The Current Transformer </wiki-migration/university/courses/alm1k/alm-current-transformer>`                     |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Switched Capacitor Design          |                                                                                                                       | :doc:`Switched Capacitor circuits </wiki-migration/university/courses/electronics/electronics-lab-19>`                       |
|                                    |                                                                                                                       | :doc:`Switched Capacitor Power Supplies </wiki-migration/university/courses/electronics/switched-cap-power-supplies>`        |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| DC-DC Converters                   | :doc:`DC-DC Converters I </wiki-migration/university/courses/alm1k/alm-lab-15>` (inductors)                           | :doc:`DC-DC Converters I </wiki-migration/university/courses/electronics/electronics-lab-15>` (inductors)                    |
|                                    | :doc:`DC-DC Converters II </wiki-migration/university/courses/alm1k/alm-lab-16>` (capacitors)                         | :doc:`DC-DC Converters II </wiki-migration/university/courses/electronics/electronics-lab-16>` (capacitors)                  |
|                                    | :doc:`Simple "Joule Thief" DC/DC Converter </wiki-migration/university/courses/alm1k/circuits1/alm-joule-thief>`      |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Regulators                         | :doc:`Low Drop out Linear Voltage Regulators </wiki-migration/university/courses/alm1k/alm-ldo-lab>`                  |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Buck & Boost Converters            | :doc:`DC-DC Boost Converters </wiki-migration/university/courses/alm1k/circuits1/alm-cir-15a>`                        | :doc:`Buck Converter Basics </wiki-migration/university/courses/electronics/buck_converter_basics>`                          |
|                                    | :doc:`Forward DC-DC Converters </wiki-migration/university/courses/alm1k/circuits1/alm-bipolar-step-up-dc-dc>`        | :doc:`Boost and Buck converter open-loop operation </wiki-migration/university/labs/open_loop_boost_and_buck_adalm2000>`     |
|                                    |                                                                                                                       | :doc:`Buck converter closed-loop operation </wiki-migration/university/labs/closed_loop_buck_adalm2000>`                     |
|                                    |                                                                                                                       | :doc:`Boost converter closed-loop operation </wiki-migration/university/labs/closed_loop_boost_adalm2000>`                   |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Electronic Circuit Breakers        | :doc:`Electronic Circuit Breakers </wiki-migration/university/courses/alm1k/alm-circuit-breaker>`                     |                                                                                                                              |
+------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+


General background Information.
===============================

Refer to :doc:`Introduction to Electrical Engineering Based Lab Activity Material </wiki-migration/university/labs/intro_ee>` for general information on test equipment, breadboards, components, etc.

**Return to Power Course Material** :doc:`Table of Contents </wiki-migration/university/courses/power>`
