Evaluating the ADG1634L 4.7 Ω On-resistance, Quad SPDT Switch with 1.2 V and 1.8 V JEDEC Logic Compliance
=========================================================================================================

Features
--------

-  Single inline headers provide flexibility for the field-programmable gate array (FPGA) or microcontroller 1.2 V or 1.8 V logic input signals
-  SMD pin resistor or capacitor sockets available for the addition of passive components
-  SMB connector sockets provide flexibility for the input and output signals

Evaluation Kit Contents
-----------------------

-  EVAL-ADG1634LEBZ Evaluation Board

Documents Needed
----------------

-  ADG1634L Datasheet
-  EVAL-ADG1634LEBZ User Guide

Equipment Needed
----------------

-  DC Voltage Source (V\ :sub:`DD`/V\ :sub:`SS`)

   -  ±5 V for Dual Supply

-  Optional Digital Logic Supply (V\ :sub:`L`)

   -  1.1 V to 1.3 V for 1.2 V Logic
   -  1.65 V to 1.95 V for 1.8 V Logic

-  Analog Signal Source
-  Method to measure voltage, such as digital multimeter (DMM)

General Description
-------------------

The EVAL-ADG1634LEBZ is the evaluation board for the ADG1634L. The ADG1634L contains four independent single-pole, double-throw (SPDT) switches. Each switch conducts equally well in both directions when on, and each switch has an input signal range that extends to the supplies. In the off condition, signal levels up to the supplies are blocked.

An external VL supply pin provides logic control flexibility for lower logic controls. The ADG1634L is both 1.2 V and 1.8 V JEDEC Standard compliant.

Figure 1 shows the EVAL-ADG1634LEBZ in a typical evaluation setup. The EVAL-ADG1634LEBZ is placed to the center of the evaluation board, and eight test points and SMB sockets are provided to connect to each of the sources and one test point and SMB socket for drain inputs. Three screw terminals are used to power the device. A 5-pin header is provided for user-defined digital voltage if required.

Full specifications on the ADG1634L are available in the ADG1634L data sheet available from Analog Devices, Inc., and should be consulted in conjunction with this user guide when using the evaluation board.

Revision History
----------------

-  3/2022—Revision 0: Initial Version

ADG1634L Evaluation Board Layout
--------------------------------

|image1|

.. container:: centeralign

   *Figure 1. EVAL-ADG1634LEBZ*


Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

Connector P1 provides access to the supply pins of the ADG1634L. V\ :sub:`DD`, GND, and V\ :sub:`SS` on P1 link to the appropriate pins on the ADG1634L. For dual-supply voltages, the evaluation board can be powered at ±5 V. For single-supply voltages, the GND and V\ :sub:`SS` terminals must be connected and power the evaluation board with 5 V or 12 V. Additionally, 1.1 V to 1.95 V is supplied to the V\ :sub:`L` pin of the ADG1634L.

Input Signals
~~~~~~~~~~~~~

Three screw connectors, P3, P4, P5, and P6 are provided to connect to both the source and drain pins of the ADG1634L. Additional subminiature Version B (SMB) connector pads are available if extra connections are required. Each trace on the source and drain side includes two sets of 0603 pads, which can place a load on the signal path to the ground. A 0 Ω resistor is placed in the signal path and can be replaced with a user-defined value. The resistor combined with the 0603 pads can create a simple resistor-capacitor (RC) filter.

Link Options
~~~~~~~~~~~~

A number of link options are provided on the EVAL-ADG1634LEBZ board that must be set for the required operating conditions before use. Table 1 shows the summary of the link headers and how they are used on the evaluation board. The functions of these link options are described in detail in Table 2.

.. container:: column

   
   **Table 1. Link Options**
   
   ============ ====== ===========
   Link Number  Option Description
   ============ ====== ===========
   JP13 to JP17 A      V\ :sub:`L`
   \            B      GND
   ============ ====== ===========
   


.. container:: COLUMN

   **Table 2. Link Functions**

   
   +--------------+--------------------------------------------------------------------------+
   | Link Number  | Function                                                                 |
   +==============+==========================================================================+
   | JP13 to JP17 | This link selects the source of the IN voltage supplied to the ADG1634L. |
   +--------------+--------------------------------------------------------------------------+
   |              | Position A selects VL from P2.                                           |
   +--------------+--------------------------------------------------------------------------+
   |              | Position B selects the 0 V or GND.                                       |
   +--------------+--------------------------------------------------------------------------+
   


SMB Connectors
~~~~~~~~~~~~~~

The parallel interface of the AD1634L is controlled manually using the link headers of JP13 to JP17, or it can be accessed using the SMB connectors, IN1 to IN4. To use the SMB connectors, remove the link headers of JP13 to JP17.

Evaluation Board Schematics and Artwork
---------------------------------------

|image2|

.. container:: centeralign

   *Figure 2. EVAL-ADG1634LEBZ Schematic 1*


   |image3|

.. container:: centeralign

   *Figure 3. EVAL-ADG1634LEBZ Schematic 2*


   |image4|

.. container:: centeralign

   *Figure 4. EVAL-ADG1634LEBZ Silkscreen*


   |image5|

.. container:: centeralign

   *Figure 5. EVAL-ADG1634LEBZ Top Layer*


   |image6|

.. container:: centeralign

   *Figure 6. EVAL-ADG1634LEBZ Layer 2*


   |image7|

.. container:: centeralign

   *Figure 7. EVAL-ADG1634LEBZ Layer 3*


   |image8|

.. container:: centeralign

   *Figure 8. EVAL-ADG1634LEBZ Bottom Layer*


Ordering Information
--------------------

Bill of Materials
~~~~~~~~~~~~~~~~~

.. container:: column

   
   **Table 3.**
   
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | Reference Designator          | Description                                                                       | Manufacturer         | Part Number         |
   +===============================+===================================================================================+======================+=====================+
   | C1 to C3                      | 50 V tantalum capacitor, 10 µF, Size D                                            | KEMET                | T491D106K050AT      |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | C4 to C6, C15 to C17          | 50 V, X7R multilayer ceramic capacitor, 0.1 µF, 0603                              | VISHAY               | VJ0603Y104KXAAC31X  |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | C7 to C14, C18 to C21         | Not placed                                                                        | -                    | -                   |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | R1 to R12                     | Not placed                                                                        | -                    | -                   |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | R13 to R24                    | Resistor 0 Ω 0603, 1%                                                             | YAGEO                | RC0603JR-070RL      |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | J1 to J18                     | 50 Ω, SMB socket, do not insert                                                   | AMPHENOL             | SMB1251B1-3GT30G-50 |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | T1 to T12, TP14 to TP20, TP23 | Red test point                                                                    | VERO TECHNOLOGIES    | 20-313137           |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | TP13, TP21 to TP22            | Black test point                                                                  | VERO TECHNOLOGIES    | 20-2137             |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | P1                            | Header RA 3.81mm with plug                                                        | PHOENIX CONTACT      | 1803280             |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | P2                            | Through hole header, 6P                                                           | SAMTEC               | TSW-106-08-G-S      |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | P3 to P6                      | 3-pin terminal block, 5 mm                                                        | KEYSTONE ELECTRONICS | 8719                |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | JP13to JP17                   | 3-pin SIL header and shorting link                                                | HARWIN               | M20-9990345         |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   | U1                            | 4.7 Ω On-resistance, Quad SPDT Switch with 1.2 V and 1.8 V JEDEC Logic Compliance | ANALOG DEVICES, INC. | ADG1634L            |
   +-------------------------------+-----------------------------------------------------------------------------------+----------------------+---------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/eval-adg1634lebz_top-web.gif
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_input-output_schematic.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_supply_pins.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_silkscreen.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_l1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_l2.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_l3.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/adg1634l_l4.png
   :width: 600px
