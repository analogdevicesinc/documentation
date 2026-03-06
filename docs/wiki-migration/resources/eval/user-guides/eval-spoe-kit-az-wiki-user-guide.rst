EVAL-SPoE-KIT-AZ Evaluation Kit User Guide
==========================================

<WRAP group>

General Description
-------------------

The EVAL-SPoE-KIT-AZ is an IEEE 802.3cg single-pair, power over Ethernet (SPoE) evaluation kit. The kit features the LTC4296-1, 5-Port SPoE power sourcing equipment (PSE) controller, and the LTC9111, SPoE powered device (PD) for evaluation of IEEE 802.3cg Class 10 through 15 SPoE power. The ADIN1100, 10BASE-T1L PHY provides the Ethernet data in the system.

Power + Data Evaluation
~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-SPoE-KIT-AZ provides evaluation of 10BASE-T1L data and SPoE power over a single twisted pair Ethernet (SPE) cable. Connect the EVAL-LTC9111-AZ to the EVAL-LTC4296-1-KIT-AZ with the provided SPE cable. Connect a 10BASE-T compatible data source with a CATV Ethernet cable to the EVAL-LTC4296-1-KIT-AZ. Connect a 10BASE-T compatible end device with a CATV Ethernet cable to the EVAL-LTC9111-AZ. (Note the end device will need power from an auxiliary source.)


|image1|

.. container:: centeralign

   \ *<fc #4682b4>Figure 1. 10BASE-T1L data and SPoE power evaluation with the EVAL-SPoE-KIT-AZ.</fc>*\


Kit Contents
~~~~~~~~~~~~

-  (1) EVAL-LTC4296-1-KIT-AZ

   -  EVAL-LTC4296-1-AZ PSE Motherboard

      -  EVAL-LTC4296-1-RC-AZ Microcontroller Rider Card

         -  Micro B USB Cable

-  (1) EVAL-LTC9111-AZ PD Motherboard
-  (2) EVAL-10BT1L-MCS-AZ ADIN1100 Media Converter Class 10 through 14 SPoE Shield
-  (2) EVAL-10BT1L-MCS-BZ ADIN1100 Media Converter Class 15 SPoE Shield
-  (1) 12”, Single Twisted Pair, 18AWG, Cable
-  (1) Micro-B USB Cable (not shown)

|image2|

.. container:: centeralign

   \ *<fc #4682b4>Figure 2. EVAL-SPoE-KIT-AZ 802.3cg SPoE Class 10 through 15 and 10BASE-T1L SPE evaluation kit.</fc>*\


--------------

EVAL-LTC4296-1-KIT-AZ Setup
---------------------------

The EVAL-LTC4296-1-KIT-AZ is comprised of the EVAL-LTC4296-1-AZ PSE motherboard, EVAL-LTC4296-1-RC-AZ microcontroller rider card, and a micro-B USB cable. The LTC4296-1 GUI communicates with the EVAL-LTC4296-1-KIT-AZ for user interaction.


|image3|

.. container:: centeralign

   \ *<fc #4682b4>Figure 3. EVAL-LTC4296-1-AZ PSE motherboard.</fc>*\


   |image4|

.. container:: centeralign

   \ *<fc #4682b4>Figure 4. EVAL-LTC4296-1-RC-AZ microcontroller rider card.</fc>*\


Rider Card Installation
~~~~~~~~~~~~~~~~~~~~~~~

Align the EVAL-LTC4296-1-RC-AZ rider card male headers with the female headers on the EVAL-LTC4296-1-AZ motherboard labeled for the µC RIDER CARD. Insert the card to where the headers are flush. Before proceeding, verify no pins are sticking out indicating a misalignment. Powering the motherboard with a misaligned card can cause damage to the system.


|image5|

.. container:: centeralign

   \ *<fc #4682b4>Figure 5. EVAL-LTC4296-1-KIT-AZ (EVAL-LTC4296-1-AZ motherboard and installed EVAL-LTC4296-1-RC-AZ microcontroller rider card.</fc>*\


Shield Installation
~~~~~~~~~~~~~~~~~~~

The EVAL-LTC4296-1-AZ PSE motherboard can accept up to 5 media converter shields at locations Port 0 through 4. The sense resistors for each port have been pre-selected for evaluation of specific maximum classes with respect to the power supply voltage.

The EVAL-10BT1L-MCS-AZ is a 10BASE-TX to 10BASE-T1L media converter shield with a power coupling network suited for Class 10 through 14 power levels. On the default configured motherboard, the EVAL-10BT1L-MCS-AZ should be inserted at Port 0, Port 1, Port 2, or Port 4. These positions are shown in red in the picture below. See Table 1 and Figure 6.

The EVAL-10BT1L-MCS-BZ is a 10BASE-TX to 10BASE-T1L media converter shield with a power coupling network suited for the Class 15 power level. On the default configured motherboard, the EVAL-10BT1L-MCS-BZ should be inserted at Port 3 only. This position is shown in orange in the picture below. See Table 1 and Figure 6.

When inserting a shield on to the motherboard, align the shield’s two short male headers with the two short female headers at a port on the motherboard. The longer header will naturally align. Note, the last two pins of the longer header on the mother board are reserved for future use and will not have pins inserted in them. Insert the shield to where the headers are flush. Before proceeding, verify no pins are sticking out indicating a misalignment. Powering the motherboard with a misaligned shield can cause damage to the system.

**<fc #4682b4>Table 1. EVAL-LTC4296-1-AZ Board Default Port Class Configuration</fc>**

+------+-----------------+-------------+-------------+-------------------------------------+
| PORT | PORT CONFIGURED | MAX CLASS   | MAX CLASS   | SHIELD                              |
|      | CURRENT LIMIT   | (VIN = 24V) | (VIN = 52V) |                                     |
+======+=================+=============+=============+=====================================+
| 0    | 0.116A          | 10          | N/A         | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+------+-----------------+-------------+-------------+-------------------------------------+
| 1    | 0.300A          | 11          | 13          | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+------+-----------------+-------------+-------------+-------------------------------------+
| 2    | 0.775A          | 12          | 14          | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+------+-----------------+-------------+-------------+-------------------------------------+
| 3    | 1.860A          | N/A         | 15          | <fc #ffa500>EVAL-10BT1L-MCS-BZ</fc> |
+------+-----------------+-------------+-------------+-------------------------------------+
| 4    | 0.775A          | 12          | 14          | <fc #ff0000>EVAL-10BT1L-MCS-AZ</fc> |
+------+-----------------+-------------+-------------+-------------------------------------+

|image6|

.. container:: centeralign

   \ *<fc #4682b4>Figure 6. EVAL-LTC4296-1-KIT-AZ port shield placements.</fc>*\


Power Supply
~~~~~~~~~~~~

Note: Before turning on the power supply, verify all shields and rider card are properly aligned with their respective headers on the motherboard and the connector pins are fully inserted.

Connect a bench power supply across the VIN (+) and GND (-) banana terminals on the EVAL-LTC4296-1-AZ motherboard. The voltage of the power supply sets the SPoE voltage. For evaluation of Class 10 through 12, set the nominal voltage to 24V; for evaluation of Class 13 through 15 set the nominal voltage to 52V. Set the current limit of the power supply higher than the current limit of the port under test, or the sum of the current limits for multiple port evaluation.

The EVAL-LTC4296-1-AZ motherboard has an onboard stepdown DC/DC converter that generates 3.3V to power the rider card and the shield cards.


|image7|

.. container:: centeralign

   \ *<fc #4682b4>Figure 7. EVAL-LTC4296-1-KIT-AZ power supply connection and settings.</fc>*\


GUI Setup
~~~~~~~~~

The LTC4296-1 Graphical User Interface (GUI) provides the user with basic status and configuration of the PSE ports. Use the micro-B USB cable to connect a PC to the powered EVAL-LTC4296-1-KIT-AZ at the EVAL-LTC4296-1-RC-AZ rider card micro-USB female connector. Open the LTC4296-1 GUI and the condensed GUI display will open if successful. If an error occurs when opening the GUI, verify the EVAL-LTC4296-1-KIT-AZ is powered, push the reset button on the EVAL-LTC4296-1-RC-AZ rider card and re-launch the LTC4296-1 GUI.

On the condensed GUI, click on Expand Details in each column for the full GUI display. In the Global Column, select in the Demo Board drop down menu EVAL-LTC4296-1-AZ to automatically configure each port maximum Class and Type, R_hsns and R_lsns sense resistor values, and MFVS Threshold to match the default settings on the EVAL-LTC4296-1-AZ motherboard. The ports will start in a Disabled state. To enable a port, select Power Up in the port’s Classification (SCCP) section.


|image8|

.. container:: centeralign

   \ *<fc #4682b4>Figure 8. LTC4296-1 GUI.</fc>*\


--------------

EVAL-LTC9111-AZ Setup
---------------------

The EVAL-LTC9111-AZ is an 802.3cg PD motherboard use for evaluating the LTC9111.


|image9|

.. container:: centeralign

   \ *<fc #4682b4>Figure 9. EVAL-LTC9111-AZ.</fc>*\


.. _shield-installation-1:

Shield Installation
~~~~~~~~~~~~~~~~~~~

The EVAL-LTC9111-AZ PD motherboard can accept one media converter shield. For Class 10 through 14 evaluations, install the EVAL-10BT1L-MCS-AZ. For Class 15 evaluation, install the EVAL-10BT1L-MCS-BZ.

When inserting a shield on to the motherboard, align the shield’s two short male headers with the two short female headers at a port on the motherboard. The longer header will naturally align. Note, the last two pins of the longer header on the mother board are reserved for future use and will not have pins inserted in them. Insert the shield until the headers are flush with each other. Before proceeding, verify no pins are sticking out indicating a misalignment. Powering the motherboard with a misaligned shield can cause damage to the system.


|image10|

.. container:: centeralign

   \ *<fc #4682b4>Figure 10. EVAL-LTC9111-AZ shield placement.</fc>*\


Jumper Settings
~~~~~~~~~~~~~~~

Set the CLASSC and CLASSV jumpers to the class for evaluation according to the table shown on the silkscreen.


|image11|

.. container:: centeralign

   \ *<fc #4682b4>Figure 11. EVAL-LTC9111-AZ CLASSC and CLASSV jumpers.</fc>*\


The EVAL-LTC9111-AZ rev. 1 will have a P4 jumper; set this jumper to CONNECT for Class 10 to 14 or DISCONNECT for Class 15.



|image12|

.. container:: centeralign

   \ *<fc #4682b4>Figure 12. EVAL-LTC9111-AZ (rev 1) RC Snubber jumper.</fc>*\


SPoE Load Connection
~~~~~~~~~~~~~~~~~~~~

In a typical application a DC/DC converter is connected across OUT+ and GND and enabled by the LTC9111.


|image13|

.. container:: centeralign

   \ *<fc #4682b4>Figure 13. EVAL-LTC9111-AZ output connection to a DC/DC converter.</fc>*\


For bench test purposes, connect passive loads such as a resistor across OUT+ and LAB_OUT-.



|image14|

.. container:: centeralign

   \ *<fc #4682b4>Figure 14. EVAL-LTC9111-AZ lab test output connection to a resistive load.</fc>*\


Onboard 3.3V
~~~~~~~~~~~~

The EVAL-LTC9111-AZ PD motherboard has an onboard buck converter that steps the SPoE voltage down to 3.3V. This 3.3V is used to power up the media converter shield. Additional load may be connected to the 3.3V output.


|image15|

.. container:: centeralign

   \ *<fc #4682b4>Figure 15. EVAL-LTC9111-AZ on board 3.3V buck.</fc>*\


--------------

Notes
-----

**Legal Terms and Conditions**

By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed.

©2022 Analog Devices, Inc. All rights reserved. Trademarks and  registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-spoe-kit-az_top-data_and_power_setup.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-spoe-kit-az_angle.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-az_angle.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-rc-az_angle.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-kit-az_angle2.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-kit-az_top_shield_placement.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc4296-1-kit-az_top_power_supply_connect_and_setting.jpg
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ltc4296-1_gui.jpg
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_angle.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_top_shield_placement.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_classc_classv_jumpers.jpg
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_rc_snubber_jumper.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_dc_dc_connect.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_resistive_load.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltc9111-az_buck.jpg
