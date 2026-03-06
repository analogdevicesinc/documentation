Evaluation Board for the AD8418A Current Sense Amplifier
========================================================

Features
--------

**Enables quick breadboarding/protoyping
Easily configurable for unidirectional or bidirectional operation
Includes provision for current sense resistor
Easy connection to test equipment**

General Description
-------------------

The AD8418ARM-EVALZ and AD8418AR-EVALZ are designed to aid in the evaluation of :adi:`AD8418A` current sense amplifiers. The boards are designed for easy configuration of different modes of operation. They can readily be mounted with a current sense resistor having a maximum standard size of 2818, and allow for flexibility with loads.

The AD8418ARM-EVALZ accommodates the :adi:`AD8418A` in the MSOP package, while the AD8418AR-EVALZ accommodates the :adi:`AD8418A` in an SOIC package. The data sheet for this device should be consulted in conjunction with this evaluation board user guide.

AD8418A Evaluation Board
------------------------

.. container:: centeralign

   \ |image1| *Figure 1. Component Side* |image2| *Figure 2. Circuit Side*\


Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

The :adi:`AD8418A` operates with a single supply ranging from 2.7 V to 5.5 V. Power is applied to the V\ :sub:`S` pin. Decoupling capacitors of 10 μF and 0.1 μF come preinstalled on the board for ready operation.

Components
~~~~~~~~~~

The :adi:`AD8418A` can be used for a variety of current monitoring applications. The board has a provision for a current shunt resistor with a maximum standard size of 2818. There are also provisions for capacitive and resistive loads at the output with 1206 footprints.

Setting the Reference Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD8418A` can be configured for unidirectional or bidirectional operation. The evaluation board can easily be set for these operations using Header P1 and Header P2. P1 sets the voltage at V\ :sub:`REF`\ 1, while P2 sets the voltage at V\ :sub:`REF`\ 2.

Unidirectional Operation
^^^^^^^^^^^^^^^^^^^^^^^^

For unidirectional operation, the output can be set at the negative rail (near ground) or at the positive rail (near V\ :sub:`S`) when the differential input is 0 V. To set the evaluation board for a ground referenced output, place the jumpers for Header P1 and Header P2 at GND. For a V\ :sub:`S` referenced output, place the jumpers for both headers at V\ :sub:`S`.

Bidirectional Operation
^^^^^^^^^^^^^^^^^^^^^^^

For bidirectional operation, the output is typically set at half scale for equal range in both directions. To configure this on the evaluation board, place the jumper for P1 at V\ :sub:`S` and place the jumper for P2 at GND. This configuration biases the output to V\ :sub:`S`/2.

External Referenced Output
^^^^^^^^^^^^^^^^^^^^^^^^^^

An external supply may also be used to set the reference voltage by placing the jumpers at EXT for both headers and applying a voltage to any one of the EXT pins. This configuration biases the output to the external supply.

The external supply can also be divided by 2. For this reference level, place the jumper for P1 at EXT, place the jumper for P2 at GND, and apply the external supply to the EXT pin near P1.

By default, the output of the evaluation board is biased at midsupply.

Evaluation Board Schematic
--------------------------

|image3|

.. container:: centeralign

   \ *Figure 3. Evaluation Board Schematic*\


Evaluation Board Layout
-----------------------

|image4|

.. container:: centeralign

   \ *Figure 4. Component Side Layout*\


   |image5|

.. container:: centeralign

   \ *Figure 5. Circuit Side Layout*\


Ordering Information
--------------------

Bill of Materials
~~~~~~~~~~~~~~~~~

| **Table 1. Bill of Materials**
| ^Quantity^Reference Designator^Package^Description^

= ====== ========================== ===========================
1 C1     C1206                      Capacitor, 0.1 μF
1 C3     C3528                      Capacitor, 10 μF
2 P1, P2 CNSAMTEC2X3H330LD36        6-pin header
1 U1     8-lead MSOP or 8-lead SOIC AD8418AWBRMZ or AD8418AWBRZ
= ====== ========================== ===========================

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/AD8418AR-EVAL_component_side_of_evaluation_board.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/AD8418AR-EVAL_circuit_side_of_evaluation_board.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/AD8418AR-EVAL_evaluation_board_schematic.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/AD8418AR-EVAL_component_side_layout.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/AD8418AR-EVAL_circuit_side_layout.png
   :width: 400px
