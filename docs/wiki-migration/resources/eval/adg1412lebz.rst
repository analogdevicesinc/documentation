Evaluating the ADG1412L 1.5 Ω On-resistance, Quad SPST Switch with 1.2 V and 1.8 V JEDEC Logic Compliance
=========================================================================================================

Features
--------

-  Single inline headers provide flexibility for the field-programmable gate array (FPGA) or microcontroller 1.2 V or 1.8 V logic input signals 0.3 Ω on-resistance flatness
-  SMD pin resistor or capacitor sockets available for the addition of passive components
-  SMB connector sockets provide flexibility for the input and output signals

Evaluation Kit Contents
-----------------------

-  EVAL-ADG1412LEBZ Evaluation Board

Document Needed
---------------

-  :adi:`adg1412L` Datasheet
-  EVAL-ADG1412LEBZ User Guide

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

The EVAL-ADG1412LEBZ is the evaluation board for the :adi:`adg1412L`. The :adi:`adg1412L` contains four independent single-pole, single-throw (SPDT) switches that can be turned on with Logic 1. Each switch conducts equally well in both directions when on, and each switch has an input signal range that extends to the supplies. In the off condition, signal levels up to the supplies are blocked.

An external VL supply pin provides logic control flexibility for lower logic controls. The :adi:`adg1412L` is both 1.2 V and 1.8 V JEDEC Standard compliant.

Figure 1 shows the EVAL-ADG1412LEBZ in a typical evaluation setup. The EVAL-ADG1412LEBZ is placed in the center of the evaluation board, and four test points and SMB sockets are provided to connect to each of the sources and drain inputs. Three screw terminals are used to power the device. A 5-pin header is provided for user-defined digital voltage if required.

Full specifications on the :adi:`adg1412L` are available in the :adi:`adg1412L` data sheet available from Analog Devices, Inc., and should be consulted in conjunction with this user guide when using the evaluation board.

Revision History
----------------

-  8/2022—Revision 0: Initial Version

ADG1412L Evaluation Board Layout
--------------------------------

|image1|

.. container:: centeralign

   *Figure 1. EVAL-ADG1412LEBZ*


Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

Connector P1 provides access to the supply pins of the :adi:`adg1412L`. V\ :sub:`DD`, GND, and V\ :sub:`SS` on P1 link to the appropriate pins on the :adi:`adg1412L`. For dual-supply voltages, the evaluation board can be powered at ±5 V or ±15 V. For single-supply voltages, the GND and V\ :sub:`SS` terminals must be connected and power the evaluation board with 12 V. Additionally, 1.1 V to 1.95 V is supplied to the V\ :sub:`L` pin of the :adi:`adg1412L`.

Input Signals
~~~~~~~~~~~~~

Two-screw connectors, P3, P4, P5, and P6 are provided to connect to both the source and drain pins of the :adi:`adg1412L`. Additional subminiature Version B (SMB) connector pads are available if extra connections are required.

Each trace on the source and drain side includes two sets of 0603 pads, which can place a load on the signal path to the ground. A 0 Ω resistor is placed in the signal path and can be replaced with a user-defined value. The resistor combined with the 0603 pads can create a simple resistor-capacitor (RC) filter.

Link Options
~~~~~~~~~~~~

A number of link options are provided on the EVAL-ADG1412LEBZ board that must be set for the required operating conditions before use. Table 1 shows the summary of the link headers and how they are used on the evaluation board. The functions of these link options are described in detail in Table 2.

.. container:: column

   
   **Table 1. Link Options**
   
   =========== ====== ===========
   Link Number Option Description
   =========== ====== ===========
   JP9 to JP12 A      V\ :sub:`L`
   \           B      GND
   =========== ====== ===========
   


.. container:: COLUMN

   **Table 2. Link Functions**

   
   +-------------+----------------------------------------------------------------------------------------------------------------+
   | Link Number | Function                                                                                                       |
   +=============+================================================================================================================+
   | JP9 to JP12 | This link selects the source of the IN voltage supplied to the :adi:`adg1412L`.                                |
   +-------------+----------------------------------------------------------------------------------------------------------------+
   |             | Position A selects VL from P2.                                                                                 |
   +-------------+----------------------------------------------------------------------------------------------------------------+
   |             | Position B selects the 0 V or GND.                                                                             |
   +-------------+----------------------------------------------------------------------------------------------------------------+
   


SMB Connectors
~~~~~~~~~~~~~~

The parallel interface of the :adi:`adg1412L` is controlled manually using the link headers of JP9 to JP12, or it can be accessed using the SMB connectors, IN1 to IN4. To use the SMB connectors, remove the link headers of JP9 to JP12.

Evaluation Board Schematics and Artwork
---------------------------------------

|image2|

.. container:: centeralign

   *Figure 2. EVAL-ADG1412LEBZ Schematic 1*


   |image3|

.. container:: centeralign

   *Figure 3. EVAL-ADG1412LEBZ Silkscreen*


   |image4|

.. container:: centeralign

   *Figure 4. EVAL-ADG1412LEBZ Top Layer*


   |image5|

.. container:: centeralign

   *Figure 5. EVAL-ADG1412LEBZ Layer 2*


   |image6|

.. container:: centeralign

   *Figure 6. EVAL-ADG1412LEBZ Layer 3*


   |image7|

.. container:: centeralign

   *Figure 7. EVAL-ADG1412LEBZ Bottom Layer*


Ordering Information
--------------------

Bill of Materials
~~~~~~~~~~~~~~~~~

.. container:: column

   
   **Table 3.**
   
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | Reference Designator | Description                                                                       | Manufacturer         | Part Number                                    |
   +======================+===================================================================================+======================+================================================+
   | C1 to C3, C7 to C9   | 50 V, X7R Multilayer Ceramic Capacitor, 0.1 µF, 0603                              | TDK                  | CGA3E2X7R1H104K080AA                           |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | C4 to C6             | 50 V, Tantalum Capacitor, 10 µF, Size D                                           | KEMET                | T491D106K050AT                                 |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | C10 to C17           | Not placed                                                                        | -                    | -                                              |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | R1 to R8             | Not placed                                                                        | -                    | -                                              |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | R9 to R16            | Resistor, 0 Ω, 0603, 1%                                                           | YAGEO                | RC0603JR-070RL                                 |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | J1 to J13            | 50 Ω, SMB socket, do not insert                                                   | AMPHENOL             | SMB1251B1-3GT30G-50                            |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | T1 to T15            | Red test point                                                                    | KEYSTONE ELECTRONICS | 5000                                           |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | TP16 to TP20         | Black test point                                                                  | KEYSTONE ELECTRONICS | 5001                                           |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | P1                   | Header RA 3.81mm with plug                                                        | PHOENIX CONTACT      | 1803280                                        |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | P2                   | Through hole header, 5P                                                           | SAMTEC               | TSW-105-08-G-S                                 |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | P3 to P6             | 2-Position Terminal Block, 5 mm                                                   | PHOENIX CONTACT      | 1935161                                        |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | JP9 to JP12          | 3-pin SIL header and shorting link                                                | HARWIN               | M20-9990345                                    |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   | U1                   | 1.5 Ω On-resistance, Quad SPDT Switch with 1.2 V and 1.8 V JEDEC Logic Compliance | ANALOG DEVICES, INC. | :adi:`adg1412L`                                |
   +----------------------+-----------------------------------------------------------------------------------+----------------------+------------------------------------------------+
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_eval_board.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_schematic.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_silkscreen.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_l1.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_l2.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_l3.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/adg1412l_l4.png
   :width: 600px
