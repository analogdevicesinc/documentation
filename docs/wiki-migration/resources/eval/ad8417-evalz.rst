Evaluation Board for the AD8417 Current Sense Amplifier
=======================================================

Features
--------

**Enables quick breadboarding/protoyping
Easily configurable for unidirectional or bidirectional operation
Includes provision for current sense resistor
Easy connection to test equipment**

General Description
-------------------

The AD8417RM-EVALZ and AD8417R-EVALZ are designed to aid in the evaluation of the :adi:`AD8417` current sense amplifiers. The board is designed for easy configuration of different modes of operation. It can readily be mounted with a current sense resistor having a maximum standard size of 2818, and allows for flexibility with loads.

The AD8417RM-EVALZ accommodates the :adi:`AD8417` in the MSOP package, while the AD8417R-EVALZ accommodates the :adi:`AD8417` in an SOIC package. The data sheet for this device should be consulted in conjunction with this evaluation board user guide.

AD8417 Evaluation Board
-----------------------

|image1|

.. container:: centeralign

   \ *Figure 1. Component Side*\


   |image2|

.. container:: centeralign

   \ *Figure 2. Circuit Side*\


Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

The :adi:`AD8417` operates with a single supply ranging from 2.7 V to 5.5 V. Power is applied to the V\ :sub:`S` pin. Decoupling capacitors of 10 µF and 0.1 µF come preinstalled on the board for ready operation.

Components
~~~~~~~~~~

The :adi:`AD8417` can be used for a variety of current monitoring applications. The board has a provision for a current shunt resistor with a maximum standard size of 2818. There are also provisions for capacitive and resistive loads at the output with 1206 footprints.

Setting the Reference Voltage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD8417` can be configured for unidirectional or bidirectional operation. The evaluation board can easily be set for these operations using Header P1 and Header P2. P1 sets the voltage at V\ :sub:`REF`\ 1, while P2 sets the voltage at V\ :sub:`REF`\ 2.

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

= ====== ========================== =========================
1 C1     C1206                      Capacitor, 0.1 μF
1 C3     C3528                      Capacitor, 10 μF
2 P1, P2 CNSAMTEC2X3H330LD36        6-pin header
1 U1     8-lead MSOP or 8-lead SOIC AD8417WBRMZ or AD8417WBRZ
= ====== ========================== =========================

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/AD8417RM-EVALZ component side of evaluation board.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/AD8417RM-EVALZ circuit side of evaluation board.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/AD8417RM-EVALZ evaluation board schematic.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/AD8417RM-EVALZ component side layout.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/AD8417RM-EVALZ circuit side layout.png
   :width: 400px
