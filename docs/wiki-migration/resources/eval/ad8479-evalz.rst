Evaluation Board for the AD8479 Precision Difference Amplifier
==============================================================

Features
--------

**Enables quick breadboarding/prototyping
User-defined circuit configuration
Edge-mounted SMA connector provisions
Easy connection to test equipment
RoHS compliant
~~~~~~~~~~~~~~

General Description
-------------------

The AD8479R-EBZ is specifically designed to aid in the evaluation of the AD8479, a very high common-mode voltage precision difference amplifier. The evaluation board is a bare board (that is, there are no components soldered to the board; these must be ordered separately). Figure 1 and Figure 2 show component side and circuit side of the bare evaluation board. Figure 3 shows the evaluation board schematic.

The evaluation board is fabricated in a 4-layer printed circuit board (PCB). It accepts edge-mounted Subminiature A (SMA) connectors on the inputs and outputs, which allows efficient connection to test equipment and other circuits. The evaluation board components are primarily SMT 1206 case size, with the exception of the tantalum bypass capacitors (C3, C4), which are D (C7343) size.

Figure 4 and Figure 5 show the component side and circuit side of the evaluation board assembly drawing. Figure 6 and Figure 7 show the metal layout pattern for connecting the board to the current sense amplifier and to the supporting circuitry.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ *Figure 1. Component side of Evaluation Board*\


.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ *Figure 2. Circuit Side of Evaluation Board*\


Evaluation Board Schematic
--------------------------

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ *Figure 3. Evaluation Board Schematic*\


Evaluation Board Layout
-----------------------

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ *Figure 4. Component Side Assembly Drawing*\


.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ *Figure 5. Circuit Side Assembly Drawing*\


.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ *Figure 6. Component Side Layout*\


.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   //Figure 7. Circuit Side Layout //


Ordering Information
--------------------

Bill of Materials
^^^^^^^^^^^^^^^^^

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

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/blank_image_2.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/blank_image_2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/schematic.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/figure_4._component_side_assembly_drawing.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/figure_5._circuit_side_assembly_drawing.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/figure_6._component_side_layout.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/figure_7._circuit_side_layout.png
