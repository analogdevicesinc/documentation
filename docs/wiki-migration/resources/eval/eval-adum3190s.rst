EVALUATING THE ADUM3190S iCOUPLER ISOLATED ERROR AMPLIFIER
==========================================================

Preface
-------

| The :adi:`EVAL-ADUM3190S <ADUM3190S>` supports the ADuM3190s isolated error amplifier based on Analog Devices, Inc., iCoupler® technology. The :adi:`adum3190S` is ideal for linear feedback power supplies with primary side controllers enabling improvements in transient response, power density, and stability as compared to commonly used optocoupler and shunt regulator solutions. Included in the :adi:`adum3190S` is a wideband operational amplifier that can be used to set up a variety of commonly used power supply loop compensation techniques. The :adi:`adum3190S` is fast enough to allow a feedback loop to react to fast transient conditions and over current conditions. Also included is a high accuracy 1.225 V reference to compare with the supply output set point.
| Complete specifications for the :adi:`adum3190S` are provided in the :adi:`adum3190S` data sheet available from Analog Devices, Inc., and should be consulted in conjunction with this Wiki user guide when using the evaluation board.
| ===== Overview ===== The :adi:`EVAL-ADUM3190S <ADUM3190S>` board, shown in Figure 1, can be used to evaluate the performance and data sheet specifications of the :adi:`adum3190S`. Figure 2 shows the schematic of the :adi:`EVAL-ADUM3190S <ADUM3190S>` circuit which can be used to test the accuracy of the :adi:`adum3190S` and perform other tests. The :adi:`EVAL-ADUM3190S <ADUM3190S>` is a 4-layer PC board, complete with ground and power layers as shown in the Evaluation Board Schematics and Artwork section.

Helpful Documents
-----------------

-  :adi:`AD9UM3190 <ADUM3190S>` military data sheet
-  :adi:`ADUM3190` data sheet
-  :adi:`AN-1316 Application Note <media/en/technical-documentation/application-notes/AN-1316.pdf>`, //Generating Multiple Isolated Bias Rails for IGBT Motor Drives with Flyback, SEPIC, and Ćuk Combination (Rev. 0) //
-  :adi:`CN-0342 Application Note <cn0342>`, *Flyback Power Supply Using a High Stability Isolated Error Amplifier*
-  :adi:`MS-2727 Technical Article <ms-2727>`, *Optimizing Multiple Output Power Converters*
-  :adi:`MS-2501 Technical Article <en/technical-articles/isolated-error-amplifier.html>`, *Isolated Error Amplifier Replaces Optocoupler and Shunt Regulator for AC/DC and DC/DC Power*

Evaluation Board Files
----------------------

The evaluation board layout, BOM, and schematic files for the :adi:`EVAL-ADUM3190S <ADUM3190S>` board can be downloaded from the links below.

| **DISCLAIMER: The footprint used for layout on the evaluation board is provided for general reference only. The exact footprint required for mounting this device onto a printed circuit board will depend on the device lead forming and may differ from what is provided herein. It is recommended to generate specific footprint information from the users lead forming specifications when placing this device on the application printed circuit board.**
| ==== Artwork: ==== `09-042413-01b.zip <https://wiki.analog.com/_media/resources/eval/09-042413-01b.zip>`__
| ==== BOM: ==== `05-042413-01-b.zip <https://wiki.analog.com/_media/resources/eval/05-042413-01-b.zip>`__
| ==== Schematic: ==== `02-042413-01-a-1.pdf <https://wiki.analog.com/_media/resources/eval/02-042413-01-a-1.pdf>`__

Evaluation Board
----------------

|image1|\

.. container:: centeralign

   \ *Figure 1. ADuM3190S Evaluation board—*\ :adi:`EVAL-ADUM3190S <ADUM3190S>`\


Evaluation Board Schematic
--------------------------

|image2|\

.. container:: centeralign

   \ *Figure 2. ADuM3190S Evaluation Board Schematic—*\ :adi:`EVAL-ADUM3190S <ADUM3190S>`\


Figure 2 shows the :adi:`adum3190S` schematic of the :adi:`EVAL-ADUM3190S <ADUM3190S>` evaluation board. U1 is the :adi:`adum3190S` in the center of the board and Pin 1 is the top-left pad with respect to the notch in the silkscreen’s package outline. C1, C2, C3, and C4 are ceramic 0603 1 μF bypass capacitors provided for proper bypassing of the :adi:`adum3190S` internal 3 V regulators on both sides of part. Also added to the board are 10 μF 0805 ceramic capacitors to the VDD1 and VDD2 connections to provide additional bypassing in case long wires are used from power supplies to the evaluation board. Test point connectors are provided for most of the important connections to pins of the :adi:`adum3190S`. The following sections describe connections to make to power the :adi:`EVAL-ADUM3190S <ADUM3190S>` and make performance tests.

Left Side Power Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the left-side external power supply (3 V to 20 V) to TP1 (labeled VDD1) and return it to TP2 (labeled GND1).

Right Side Power Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect the right-side external power supply (3 V to 20 V) to TP9 (labeled VDD2) and return it to TP10 (labeled GND2).

Accuracy Test Connections
~~~~~~~~~~~~~~~~~~~~~~~~~

| In the :adi:`EVAL-ADUM3190S <ADUM3190S>` schematic (see Figure 2), a blue line outlines the EAOUT accuracy circuit. Capacitor C7 (2.2 nF) together with R8 (680 Ω) and R7 (0 Ω) resistors form an integrator circuit to close the loop from the −IN input to the EAOUT output. A ±1% accurate internal reference voltage of 1.225 V at REFOUT is connected to the noninverting op amp input +IN through a 0 Ω resistor, R9, providing the reference for the accuracy test circuit. See Figure 3, :adi:`adum3190S` Test Circuit 1, or the :adi:`adum3190S` data sheet for more information about the operation of the :adi:`adum3190S`.
| For accuracy tests, add a wire between GND1 and GND2 for EAOUT and EAOUT2 (see Figure 3). This connection is needed because the accuracy tests connect a 680 Ω resistor across the isolation barrier and creates a current path between the two isolated areas, so a ground return is needed for the accuracy tests. The accuracy of the EAOUT output will be within ±1% of the reference voltage specified value of 1.225 V. Next, the EAOUT2 accuracy in Figure 4 (Test Circuit 2) can be performed by removing the R7 (0 Ω) resistor and placing a 0 Ω resistor at R5, completing the EAOUT2 circuit. Because the EAOUT2 circuit has a high gain and uses the same internal reference voltage to connect to the −IN input of the op amp, the accuracy of the EAOUT2 output is also within ±1% of the reference voltage specified value of 1.225 V.
| For tests other than the accuracy tests, open the 680 Ω resistor connections by removing R5 and R7 (0 Ω), the C7 integrating capacitor, and the external wire connection made between GND1 and GND2. Once completed, other components may be added to the evaluation board per the schematic in Figure 2 to make circuits for other tests such as :adi:`adum3190S` data sheet specifications for the op amp, reference, UVLO, output characteristics, or power supply.
| ==== Test Circuit 1 ==== |image3|\

.. container:: centeralign

   \ *Figure 2. ADuM3190S Test Circuit 1—*\ :adi:`EVAL-ADUM3190S <ADUM3190S>`\


| ==== Test Circuit 2 ==== |image4|\

.. container:: centeralign

   \ *Figure 2. ADuM3190S Test Circuit 2—*\ :adi:`EVAL-ADUM3190S <ADUM3190S>`\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/adum3190s_eval_board.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adum3190s_eval_schematic.png
   :width: 1600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adum3190s_test_circuit1.png
   :width: 1600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adum3190s_test_circuit2.png
   :width: 1600px
