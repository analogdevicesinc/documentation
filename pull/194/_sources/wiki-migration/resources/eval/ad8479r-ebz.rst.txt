Evaluation Board for the AD8479 Precision Difference Amplifier
==============================================================

Features
--------

**Enables quick breadboarding/prototyping
User-defined circuit configuration
Edge-mounted SMA connector
Easy connection to test equipment
RoHS compliant
~~~~~~~~~~~~~~

General Description
-------------------

The AD8479R-EBZ is specifically designed to aid the evaluation of the AD8479, a very high common-mode voltage precision difference amplifier. The design of this board emphasizes simplicity and ease of use. This board comes with connection options for the input and output terminals (SMA and Vector pins) and a predefined configuration with the reference pins both tied to ground.

The AD8479 datasheet covers the details of the device’s operation. It also shows the basic connections for operating the device with a single or dual supply. It is recommended to consult the datasheet in conjunction with this evaluation board user guide especially when powering up for the first time.

AD8479 Evaluation Board Photograph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ *Figure 1. Component Side*\


.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ *Figure 2. Circuit Side*\


Quick Start
-----------

Overview
~~~~~~~~

This section outlines the most basic configuration of the AD8479 evaluation board to test for basic functionality.

Required Equipment
~~~~~~~~~~~~~~~~~~

Apart from the AD8479 evaluation board, there are a minimum of 9 other items required (see Figure 3):

-  A single or dual output power supply
-  A signal source such as an arbitrary waveform generator
-  An oscilloscope
-  A SMA termination
-  Two BNC-to-SMA or BNC-to-Grabber cables to connect the signal source and oscilloscope to the AD8479 evaluation board
-  Three Banana-to-Grabber cables to connect the power supply to the AD8479 evaluation board

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ *Figure 3. Minimal Requirements for Quick Start Operation*\


Initial Configuration
~~~~~~~~~~~~~~~~~~~~~

To start the initial board configuration, do the following steps:

1. Ensure that the power supply is off. Connect the supply leads to the vector pins labelled +Vs, Gnd1 and –Vs as shown in Figure 4.

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ *Figure 4. AD8479 Evaluation Board with the Basic Power Connections*\


2. For a single input signal source, connect the signal source to the +IN on the SMA connector (J3) using a BNC to SMA cable and put a SMA termination to the -IN on the SMA connector (J1) as shown on figure 5.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ *Figure 5. AD8479 Evaluation Board with Source Signal Connected*\


3. Connect the oscilloscope to the SMA connector (J4) using the BNC to SMA cable as shown on figure 6.

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ *Figure 6. Completed Connections for Quick Start Usage*\


Power Up
~~~~~~~~

After completing the initial configuration, power up the board as follows:

1. Set the power supply to ±15.0 V.

2. Turn on the power supply. Typical supply current of AD8479 is 550 µA. Current drawn from the power supply should not exceed 1 mA.

3. Configure the signal source to output a 1 kHz sine wave at 2 V p-p. (Note that if your signal source is relative to a 50 Ω impedance, set the amplitude to 1 V p-p.)

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   \ *Figure 7. The Completed Setup*\


4. Enable the signal source. Oscilloscope should be able to measure a 2 V p-p sine wave at the output of the AD8479.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   \ *Figure 8. Final Result, with 2 V p-p Signal Appearing on the Oscilloscope*\


Configuration Options
---------------------

Setting the Reference Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the output of the evaluation board is referenced to ground as shown on its schematic in Figure 9.

An external supply may also be used to set the reference voltage by removing the R7 and then applying a voltage to any of the REF pins. This configuration biases the output to the external supply.

Applying Common Mode Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common mode voltage may be applied to the SMA connector (J2) or to the vector pin labelled VCM after providing necessary parts to R3, R4 and R5.

Other Components
~~~~~~~~~~~~~~~~

There are provisions available on the AD8479 Evaluation boards for the following components:

-  Input termination resistor (R1, R2)
-  Resistive load (RL)
-  Capacitive load (CL)
-  Output series resistor (R9)
-  Output termination resistor (R10)

Evaluation Board Schematic
--------------------------

.. container:: centeralign

   \ |image9|\


.. container:: centeralign

   \ *Figure 9. Evaluation Board Schematic*\


Evaluation Board Layout
-----------------------

.. container:: centeralign

   \ |image10|\


.. container:: centeralign

   \ *Figure 10. Component Side Layout*\


.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   //Figure 11. Circuit Side Layout //


Ordering Information
--------------------

Bill of Materials
~~~~~~~~~~~~~~~~~

| **Table 1. Bill of Materials**
| ^Quantity^Reference Designator^Package^Description^

+----+----------------------------------------------------------+------------------------+------------------------+
| 2  | R1, R2                                                   | R1206                  | Resistor, 49.9 Ω       |
+----+----------------------------------------------------------+------------------------+------------------------+
| 4  | R3, R4, R5, RL                                           | R1206                  | User-defined resistor  |
+----+----------------------------------------------------------+------------------------+------------------------+
| 4  | R6, R7, R8, R9                                           | R1206                  | Resistor, 0 Ω          |
+----+----------------------------------------------------------+------------------------+------------------------+
| 1  | R10                                                      | R1206                  | Resistor, 10 k Ω       |
+----+----------------------------------------------------------+------------------------+------------------------+
| 2  | C1, C2                                                   | c1206                  | Capacitor, 0.1uF       |
+----+----------------------------------------------------------+------------------------+------------------------+
| 2  | C3, C4                                                   | C7343-31               | Capacitor, 10uF        |
+----+----------------------------------------------------------+------------------------+------------------------+
| 1  | CL                                                       | C1206                  | User-defined capacitor |
+----+----------------------------------------------------------+------------------------+------------------------+
| 13 | +IN,-IN,+VS,-VS,OUT, VCM,GND1-GND3, OUT1,REF+,REF-,STGND | CNLOOPTP_D45           | CONN-PCB pin vector    |
+----+----------------------------------------------------------+------------------------+------------------------+
| 4  | J1,J2,J3,J4                                              | CN JOHNSON142-0701-801 | SMA connector          |
+----+----------------------------------------------------------+------------------------+------------------------+
| 1  | U1                                                       | 8-lead SOIC            | AD8479ARZ              |
+----+----------------------------------------------------------+------------------------+------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad8479_component_side.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad8479_circuit_side.jpg
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ad8479_minimal_requirement_for_quick_start_operation.jpg
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ad8479_power_connections.jpg
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ad8479_with_source_signal.jpg
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad8479_completed_connections.jpg
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ad8479_the_completed_setup.jpg
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad8479_final_result.jpg
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ad8479_schematic.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/figure_6._component_side_layout.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/figure_7._circuit_side_layout.png
