Evaluating the ADG1206L and ADG1207L, 16- and 8-Channel Multiplexers with 1.2 V and 1.8 V JEDEC Logic Compliance
================================================================================================================

Features
--------

-  Single inline headers provide flexibility for the field-programmable gate array (FPGA) or microcontroller 1.2 V or 1.8 V logic input signals
-  SMD pin resistor or capacitor sockets available for the addition of passive components
-  SMB connector sockets provide flexibility for the input and output signals

Evaluation Kit Contents
-----------------------

-  EVAL-ADG1206LEBZ Evaluation Board
-  EVAL-ADG1207LEBZ Evaluation Board

Documents Needed
----------------

-  ADG1206L/ADG1207L Datasheet
-  EVAL-ADG1206LEBZ/EVAL-ADG1207LEBZ User Guide

Equipment Needed
----------------

-  DC Voltage Source (V\ :sub:`DD`/V\ :sub:`SS`)

   -  ±15 V for Dual Supply

-  Optional Digital Logic Supply (V\ :sub:`L`)

   -  1.1 V to 1.3 V for 1.2 V Logic
   -  1.65 V to 1.95 V for 1.8 V Logic

-  Analog Signal Source
-  Method to measure voltage, such as digital multimeter (DMM)

General Description
-------------------

The EVAL-ADG1206LEBZ/EVAL-ADG1207LEBZ are the evaluation boards for the ADG1206L/ADG1207L. The ADG1206L/ADG1207L contains sixteen single channels and eight differential channels, respectively. The ADG1206L switches one of sixteen inputs to a common output, as determined by 4-bit binary address lines A0, A1, A2, and A3. The ADG1207L switches one of eight differential inputs to a common differential output, as determined by the 3-bit binary address lines, A0, A1, and A2. An EN on both devices is used to enable or disable the device. When disabled, all channels are switched off. When on, each channel conducts equally well in both directions and has an input signal range that extends to the supplies.

An external VL supply pin provides logic control flexibility for lower logic controls. The ADG1206L/ADG1207L is both 1.2 V and 1.8 V JEDEC standard compliant.

Figure 1 shows the EVAL-ADG1206LEBZ/EVAL-ADG1207LEBZ in a typical evaluation setup. The ADG1206L/ADG1207L is placed in the center of the evaluation board, and wire screw terminals are provided to connect to each source and drain pin. Three screw terminals are used to power the device and an external pin provides users with a defined digital logic supply voltage. Alternatively, the digital logic supply voltage can be supplied from 5- and 6-pin headers.

Full specifications on the ADG1206L/ADG1207L are available in the ADG1206L/ADG1207L data sheet available from Analog Devices, Inc., and should be consulted in conjunction with this user guide when using the EVAL-ADG1206LEBZ/EVAL-ADG1207LEBZ.

Revision History
----------------

-  12/2022—Revision 0: Initial Version

ADG1206L and ADG1207L Evaluation Board Layout
---------------------------------------------

|image1|

.. container:: centeralign

   *Figure 1. EVAL-ADG1206LEBZ*


   |image2|

.. container:: centeralign

   *Figure 2. EVAL-ADG1207LEBZ*


Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

Connector P6 provides access to the supply pins of the ADG1206L/ADG2107L. V\ :sub:`DD`, GND, and V\ :sub:`SS` on the P6 terminal block link to the appropriate pins on the ADG1206L/ADG2107L. For dual-supply voltages, the evaluation board can be powered at ±15 V. For single-supply voltages, the GND and V\ :sub:`SS` terminals must be connected and power the evaluation board with 12 V. Additionally, 1.1 V to 1.95 V is supplied to the V\ :sub:`L` pin of the ADG1206L/ADG2107L.

Input Signals
~~~~~~~~~~~~~

Provided are screw connectors, P1, P2, P3, P4, and P5 to connect to both the source and drain pins of the ADG1206L/ADG1207L. Additional subminiature Version B (SMB) connector pads are available if extra connections are required.

Each trace on the source and drain side includes two sets of 0603 pads, which can place a load on the signal path to the ground. A 0 Ω resistor is placed in the signal path and can be replaced with a user-defined value. The resistor combined with the 0603 pads can create a simple resistor-capacitor (RC) filter.

Link Options
~~~~~~~~~~~~

The EVAL-ADG1206LEBZ/EVAL-ADG1209LEBZ evaluation boards provide several link options that must be set at the required operating conditions before use.

Table 1 describes the positioning of the links necessary for controlling the evaluation board via link headers. The functions of these link options are described in detail in Table 2.

.. container:: column

   
   **Table 1. Link Options**
   
   ===================== ====== ===========
   Link Number           Option Description
   ===================== ====== ===========
   JP1 to JP5 (ADG1206L) A      V\ :sub:`L`
   JP1 to JP4 (ADG1207L) A      V\ :sub:`L`
   \                     B      GND
   ===================== ====== ===========
   


.. container:: COLUMN

   **Table 2. Link Functions**

   
   +-----------------------+--------------------------------------------------------------------------+
   | Link Number           | Function                                                                 |
   +=======================+==========================================================================+
   | JP1 to JP5 (ADG1206L) | This link selects the source of the IN voltage supplied to the ADG1206L. |
   +-----------------------+--------------------------------------------------------------------------+
   | JP1 to JP4 (ADG1207L) | This link selects the source of the IN voltage supplied to the ADG1207L. |
   +-----------------------+--------------------------------------------------------------------------+
   |                       | Position A selects VL from P7.                                           |
   +-----------------------+--------------------------------------------------------------------------+
   |                       | Position B selects the 0 V or GND.                                       |
   +-----------------------+--------------------------------------------------------------------------+
   


SMB Connectors
~~~~~~~~~~~~~~

The parallel interface of the AD1206L/ADG1207L is controlled manually using the link headers of JP20 to JP24 (EVAL-ADG1206LEBZ), JP20 to JP23 (EVAL-ADG1207LEBZ), or it can be accessed using the SMB connectors, A0 to A3. To use the SMB connectors, remove the link headers of JP20 to JP24.

Evaluation Board Schematics and Artwork
---------------------------------------

|image3|

.. container:: centeralign

   *Figure 3. EVAL-ADG1206LEBZ Schematic 1*


   |image4|

.. container:: centeralign

   *Figure 4. EVAL-ADG1206LEBZ Schematic 2*


   |image5|

.. container:: centeralign

   *Figure 5. EVAL-ADG1206LEBZ Silkscreen*


   |image6|

.. container:: centeralign

   *Figure 6. EVAL-ADG1206LEBZ Top Layer*


   |image7|

.. container:: centeralign

   *Figure 7. EVAL-ADG1206LEBZ Layer 2*


   |image8|

.. container:: centeralign

   *Figure 8. EVAL-ADG1206LEBZ Layer 3*


   |image9|

.. container:: centeralign

   *Figure 9. EVAL-ADG1206LEBZ Bottom Layer*


   |image10|

.. container:: centeralign

   *Figure 10. EVAL-ADG1207LEBZ Schematic 1*


   |image11|

.. container:: centeralign

   *Figure 11. EVAL-ADG1207LEBZ Schematic 2*


   |image12|

.. container:: centeralign

   *Figure 12. EVAL-ADG1207LEBZ Silkscreen*


   |image13|

.. container:: centeralign

   *Figure 13. EVAL-ADG1207LEBZ Top Layer*


   |image14|

.. container:: centeralign

   *Figure 14. EVAL-ADG1207LEBZ Layer 2*


   |image15|

.. container:: centeralign

   *Figure 15. EVAL-ADG1207LEBZ Layer 3*


   |image16|

.. container:: centeralign

   *Figure 16. EVAL-ADG1207LEBZ Bottom Layer*


Ordering Information
--------------------

Bill of Materials
~~~~~~~~~~~~~~~~~

.. container:: column

   
   **Table 3.**
   
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | Reference Designator                                              | Description                                                                | Manufacturer         | Part Number         |
   +===================================================================+============================================================================+======================+=====================+
   | C21, C22, C27                                                     | 50 V tantalum capacitor, 10 µF, Size D                                     | KEMET                | T491D106K050AT      |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | C19, C20, C23 to C26                                              | 50 V, X7R multilayer ceramic capacitor, 0.1 µF, 0603                       | VISHAY               | VJ0603Y104KXAAC31X  |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | C1 to C18                                                         | Not placed                                                                 | -                    | -                   |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | R17 to R32, R35, R36                                              | Not placed                                                                 | -                    | -                   |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | R1 to R16, R33, R34                                               | Resistor 0 Ω 0603, 1%                                                      | VISHAY               | CRCW06030000Z0EA    |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | J1 to J24                                                         | 50 Ω, SMB socket, do not insert                                            | AMPHENOL             | SMB1251B1-3GT30G-50 |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | S1A to S8A, S1B to S8B, S1-S16, DA, DB, D, A0 to A3, VDD, VSS, VL | Red test point                                                             | VERO TECHNOLOGIES    | 20-313137           |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | AGND1-AGND5                                                       | Black test point                                                           | VERO TECHNOLOGIES    | 20-2137             |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | P1-P4                                                             | 4-pin terminal block, 5 mm                                                 | CAMDENBOSS LTD       | CTB5000/4           |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | P5                                                                | 2-pin terminal block, 5 mm                                                 | CAMDENBOSS LTD       | CTB5000/2           |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | P6                                                                | 3-pin terminal block, 5 mm                                                 | PHOENIX CONTACT      | 1803280             |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | P7                                                                | Header RA 3.81 mm                                                          | SAMTEC               | TSW-106-08-G-S      |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | JP1 to JP4                                                        | 3-pin SIL header and shorting link                                         | HARWIN               | M20-9990345         |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   | U1                                                                | 8- and 16-channel Multiplexers with 1.2 V and 1.8 V JEDEC Logic Compliance | ANALOG DEVICES, INC. | ADG1206L/ADG1207L   |
   +-------------------------------------------------------------------+----------------------------------------------------------------------------+----------------------+---------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/eval-adg1634lebz_top-web.gif
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/eval-adg1634lebz_top-web.gif
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_schematic_1.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_schematic_2.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_silkscreen.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_layer_1.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_layer_2.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_layer_3.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/adg1206l_layer_4.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_schematic_1.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_schematic_2.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_silkscreen.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_layer_1.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_layer_2.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_layer_3.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/adg1207l_layer_4.png
   :width: 600px
