ADE9430 Energy and Power Quality Measurement Evaluation Board
=============================================================

| 
| ===== FEATURES =====

-  Energy and Class S power quality measurement evaluation board with ADE9430 multiphase energy and power quality monitoring IC
-  3-Phase 4-Wire, 3-Phase 3-Wire, or 3-wire single phase measurements
-  Direct interface with current output current transformers
-  Up to 240 V RMS nominal line neutral voltage measurement
-  For use with the ADSW-PQ-CLS Power Quality Library

| 

PROVIDED IN THE KIT
-------------------

-  STM32 NUCLEO-F413ZH
-  EVAL-ADE9430ARDZ Evaluation Board
-  Current transformers

|

NOT INCLUDED IN THE KIT
-----------------------

-  Micro USB cable
-  Voltage channel interconnects

| 

DOCUMENTS NEEDED
----------------

-  ADE9430 data sheet
-  ADSW-PQ-CLS Power Quality Library User's Guide

|

SOFTWARE NEEDED
---------------

| Refer to the ADSW-PQ-CLS Power Quality Library User's Guide for software information
| ===== GENERAL DESCRIPTION ===== The EVAL-ADE9430ARDZ Eval Board is for use with the STM32 NUCLEOF413ZH. The Evaluation board can be directly interfaced with current transformers and voltage leads. It enables quick evaluation and prototyping of energy and class S power quality measurement systems with the ADE9430. The power Quality library and application examples are provided to simplify implementation of larger systems.
| ===== HAZARDOUS HIGH VOLTAGE ===== This equipment is connected to hazardous line voltages. Exercise proper caution when connecting the sensors and voltage leads. Ensure that the system is enclosed in a protective casing.

CONNECTION DIAGRAM
------------------

|

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure 1. EVAL-ADE9430ARDZ Connection Diagram**\


| ===== MODULE HARDWARE =====

CURRENT SENSORS
~~~~~~~~~~~~~~~

| The EVAL-ADE9430ARDZ Evaluation Board is designed to work directly with the provided current output current transformers (CTs). Connect the CT leads to the SL1, SL2, SL3, and SL4 terminal blocks.
| === Current Output CTs === The EVAL-ADE9430ARDZ evaluation board has on-board burden resistors in differential configuration to allow direct connection with current output CTs. With a typical 2500:1 CT, the maximum recommended current is 86 A rms. Refer to the ADE9430 datasheet to modify burden resistors for different current ranges.
| === Voltage Output CTs=== To use voltage output CTs, remove burden Resistors R1, R2, R3, R4, R10, R11, R19, and R20. The maximum recommended CT output voltage is ±0.353 V rms.
| ====VOLTAGE SENSORS==== The EVAL-ADE9430ARDZ evaluation board has on-board resistor dividers to attenuate the incoming input voltage. The attenuation factor is 801. Do not exceed the 240 V rms nominal line to neutral voltage in the 3-phase, 4-wire (3P4W) wye configuration. In 3‑wire delta configuration, when Phase B is used as the reference, do not exceed 250 V rms line to line voltage. There are 4 mm banana jacks on board to connect the voltage inputs. Use TPI A079 or equivalent leads with alligator clips to connect the voltage inputs.
| ====POWERING THE ADE9430 EVALUATION BOARD ====

The EVAL-ADE9430ARDZ evaluation board can get power from one of two sources, the barrel power jack or power from the USB cable coming from the NUCLEO.

-  Remove the EVAL-ADE9430ARDZ evaluation board and NUCLEO from packaging
-  Plug the NUCLEO into the EVAL-ADE9430ARDZ evaluation board using the Arduno Uno headers on the evaluation board
-  To power the board there are 2 options

   -  Power it through the J15 5.1mm barrel connector, do not apply more than 12VDC. Place a jumper on J2 to the middle position

      -  Power from the NUCLEO, place a Jumper on J2 on the position next to D7

-  Securely screw the leads of the provided Current Transformers to the Current inputs (SL1..SL4)
-  Connect the voltage terminals to the J5..J8 connectors
-  After setting the power jumper, plug the NUCLEO to the PC via the USB port
-  Program the example from the PQlib software. Refer to the ADSW-PQ-CLS Power Quality Library User's Guide for software information
-  Configure the Serial port to talk to the PQlib via the CLI (if applicable)

| 
| |image2|

.. container:: centeralign

   \ **Figure 2. EVAL-ADE9430ARDZ to NUCLEO pin alignment. U10 header should align with row farthest from the ST Micro**\


| |image3|

.. container:: centeralign

   \ **Figure 3. EVAL-ADE9430ARDZ to NUCLEO pin alignment. U10 header should align with the connectors on each side**\


| |image4|

.. container:: centeralign

   \ **Figure 4. The EVAL-ADE9430ARDZ evaluation board and NUCLEO mated completely**\


| |image5|

.. container:: centeralign

   \ **Figure 5. Jumper position for external power jack**\


| |image6|

.. container:: centeralign

   \ **Figure 6. Jumer position for NUCLEO power**\


LINE VOLTAGE CONNECTIONS
------------------------

The EVAL-ADE9430ARDZ evaluation board is connected to hazardous line voltages. Exercise proper caution when connecting the sensors and voltage leads. Ensure that the system is enclosed in a protective casing.

3-PHASE, 4-WIRE (3P4W) WYE
~~~~~~~~~~~~~~~~~~~~~~~~~~

The 3P4W wye connection is shown in Figure 7. Do not exceed the nominal voltage of a 240 V rms line to neutral in wye configuration.

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   \ **Figure 7. 3P4W Wye Connection**\


3-PHASE, 3-WIRE (3P3W) DELTA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 3P3W delta connection is shown in Figure 8. Phase B is used as the reference; therefore, the neutral channel on the board is connected to Phase B. Do not exceed the 250 V RMS line to line voltage in the delta configuration.

-  Set VCONSEL to 001 so that VB = VA – VC.
-  Set ICONSEL to 1 so that IB = −IA – IC.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   \ **Figure 8. 3P3W Delta Connection**\


EVALUATION BOARD SCHEMATICS
---------------------------

`ade9430_eval_board_schematic.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/ade9430_eval_board_schematic.pdf>`__

PCB GERBERS
-----------

`ade9430_gerber_pdf.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/ade9430_gerber_pdf.pdf>`__

COMPONENTS
----------

Table 1 list required voltage leads, and clips. Equivalent components can also be used.

============ ========
Manufacturer Part No.
============ ========
Leads-TPI    A079
Clips-TPI    A079
Leads-TPI    A079
============ ========

Bill of Materials
-----------------

`bom.xls <https://wiki.analog.com/_media/undefined/bom.xls>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/connection_diagram.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/ade9430_userguide_fig2.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/ade9430_userguide_fig3_sideview.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/ade9430_user_guide_fig4_bottom.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/option_a_power2.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/option_b_power2.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/3ph_wye.jpg
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ade9430_eval_guide/3ph_delta.jpg
