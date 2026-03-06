User Guide for the Dual SOIC Evaluation Board for Low Bias Current Amplifiers
=============================================================================

Features
--------

**Full featured evaluation board for dual low bias current
amplifiers in narrow-body SOIC
Enables quick prototyping
User defined circuit configuration
Edge mounted SMA connector provisions
Easy connection to test equipment and other circuits
Available provision for photodiode for quick evaluation
\* Connections available for photodiode bias
\* Guard trace available to minimize leakage** x

GENERAL DESCRIPTION
-------------------

This user guide describes the evaluation board, which allows users to test dual-channel, low bias current amplifiers that come in an 8 lead standard small outline package (SOIC_N). The design of this evaluation board emphasizes simplicity and ease of use. Provisions are available on the board to interface easily to test equipment.

The evaluation board uses a combination of surface-mount technology (SMT) in Case Size 0603, with the exception of bypass capacitors and termination resistors. It also features a variety of unpopulated resistor and capacitor pads that provide the user with multiple choices and extensive flexibility for different application circuits.

The evaluation board also has a provision for photodiode sensors, allowing easy configuration of a transimpedance amplifier (TIA). The layout is optimized with provisions for guarding to ensure low leakage and low parasitic capacitance for TIA applications.

The device specifications and operation, along with application circuit configurations and guidance are covered in the datasheets of the devices covered by this user guide. These datasheets should be consulted in conjunction with the user guide for a better understanding of the device operation.

Table 1. Compatible Low Bias Current Amplifiers

============ ============ ========= =======================
Part Number  Bias Current Bandwidth Broadband Noise (@1kHz)
============ ============ ========= =======================
ADA4510-2ARZ 5 pA         10 MHz    5 nV/√Hz
============ ============ ========= =======================

EVALUATION BOARD PHOTOGRAPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/dual_soic_low_ib_evb_photo.png
   :align: center
   :width: 400px

EVALUATION BOARD QUICK START OPERATION
--------------------------------------

OVERVIEW
~~~~~~~~

This section outlines the basic configuration of the evaluation board to test basic functionality of the device. Provisions are included on the board so that it is highly configurable for any application. The connectors available on the board provide an easy interface to various bench equipment.

Power Supply
~~~~~~~~~~~~

The evaluation board uses turret connectors for the power supply connections. The board comes installed with 0.1 µF and 10 µF decoupling capacitors on both supplies. Apply the positive supply to the VS+ connector and the negative supply to the VS− connector.

Amplifier Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Both channels on the evaluation board are configured in a noninverting configuration with a gain of 1 by default. Preinstalled resistors accommodate this configuration. Figure 2 shows the default connections on the board.


|image1|

POWER-UP PROCEDURE
~~~~~~~~~~~~~~~~~~

| To begin using the evaluation board, use the following procedure.
| 1. Set the power supplies to 15 V, −15 V, and ground, and connect to the VS+, VS−, and GND turrets, respectively.
| 2. Connect an oscilloscope to the OUTA and OUTB Subminiature Version A (SMA) connectors.
| 3. Connect an input signal source to INA+ and INB+. Set the signal source to the preferred amplitude and frequency. Keep the amplitude within the input voltage range of the device to ensure proper operation.
| 4. Turn on the power supplies, then turn on the input signal source.
| The oscilloscope now reads the same amplitude and frequency as the input signal

TRANSIMPEDANCE AMPLIFIER (TIA) CONFIGURATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The low input bias current and low input capacitance of these amplifiers make this device a good choice for transimpedance configurations. The evaluation board has an on-board provision for a photodiode (radial package) on both channels of the amplifier. The evaluation board is fabricated with a guard trace around the −IN x pin to ensure minimal leakage when evaluating in a transimpedance configuration. R1 for Channel A and R2 for Channel B provide quick connections of the guard trace to the noninverting pin of the amplifier in an inverting TIA configuration.
| When operating in a TIA configuration, a bias voltage can be applied to VPDA or VPDB. If no bias voltage needs to be applied, install a 0 Ω resistor at RPDA or RPDB to connect the anode of the photodiode to ground. For this TIA configuration, install the photodiode at either PDA or PDB, along with the feedback resistor at RFA and RFB, for Channel A and Channel B, respectively. A capacitor at C5 and C12 can be added for stability of the circuit.

EVALUATION BOARD SCHEMATICS AND ARTWORK
---------------------------------------

|image2|

.. container:: centeralign

   \ *Figure 3. Channel A Circuit Connections*\


   |image3|

.. container:: centeralign

   \ *Figure 4. Channel B Circuit Connections*\


   |image4|

.. container:: centeralign

   \ *Figure 5. Power and Ground Connections*\


   |image5|

.. container:: centeralign

   \ *Figure 6. Assembly Drawing, Primary Side*\


   |image6|

.. container:: centeralign

   \ *Figure 7. Layout Pattern, Primary Side*\


   |image7|

.. container:: centeralign

   \ *Figure 8. Layout Pattern, Secondary Side*\


ORDERING INFORMATION
--------------------

BILL OF MATERIALS
~~~~~~~~~~~~~~~~~

| **Table 2. Bill of Materials**
| ^Quantity^Reference Designator^Description^Supplier^Part Number^

+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 1  | U1                                                                                                               | 8-lead SOIC                                | Analog Devices, Inc.         | ADA4510-2ARZ            |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 2  | C1, C3                                                                                                           | Ceramic capacitors, X7R, 0603, 0.1 µF, 50V | Vishay                       | VJ0603Y104KXAAC31X      |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 2  | C2, C6                                                                                                           | Ceramic capacitors, X5R, 0603, 10 µF, 50 V | TDK                          | C3216X5R1H106K160AB     |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 10 | C4, C5, C7, C11, C12, C13, CLA, CLB, CSA, CSB                                                                    | User defined capacitors, 0603              | Not applicable               | Not applicable          |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 12 | CFA, CFB, R4, R7, R8, R15, RFA, RFB, RO1, RO2, RO3, RO4                                                          | 0 Ω resistors, 0603                        | Panasonic                    | ERJ-3GEY0R00V           |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 16 | R1, R2, RPDA, RPDB, R3, R5, R6, R9, R10, R14, R16, R17, RLA, RLB, RSA, RSB                                       | User defined resistors, 0603               | Not applicable               | Not applicable          |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 4  | RT1, RT2, RT3, RT4                                                                                               | User defined resistors, 1206               | Not applicable               | Not applicable          |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 3  | GND, VS+, VS−                                                                                                    | Connectors, solder terminal turrets        | Mill-Max                     | 2501-2-00-80-00-00-07-0 |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 2  | GND1, GND2                                                                                                       | Test points, black                         | Components Corporation       | TP-104-01-00            |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 2  | PDA, PDB                                                                                                         | User defined photodiodes                   | Not applicable               | Not applicable          |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 6  | INA+, INA−, INB+, INB−, OUTA, OUTB                                                                               | Coaxial SMA end launches                   | Cinch Connectivity Solutions | 142-0701-801            |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+
| 16 | GND1, GND2, GND3, GND4, GND5, GND6, GRDA, GRDB, TP_INA+, TP_INA−, TP_INB+, TP_INB−, TP_OUTA, TP_OUTB, VPDA, VPDB | Connectors, PCB test points                | Keystone Electronics         | 5115                    |
+----+------------------------------------------------------------------------------------------------------------------+--------------------------------------------+------------------------------+-------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/figure_2._default_connection.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/figure_3._channel_a_circuit_connections.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/figure_4._channel_b_circuit_connections.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/figure_5._power_and_ground_connections.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/figure_6._assembly_drawing_primary_side.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/figure_7._layout_pattern_primary_side.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/figure_8._layout_pattern_secondary_side.png
   :width: 400px
