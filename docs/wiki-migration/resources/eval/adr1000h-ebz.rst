Evaluation Board for the ADR1000 Ultra Stable Shunt Voltage Reference in 8 Pin TO-99
====================================================================================

Features
--------

| Includes full application circuit, both of the Reference loop and the Heater loop
| Includes top and bottom covers for the ADR1000
| Includes top and bottom covers for the VPG Foil resistors
| Panel mounted banana plugs have standard 0.75" centers
| Standard 0.75" banana centers mate directly to HP3458 or to standard dual cables
| Includes Copper Telurride female banana jacks for low thermals
| RoHS compliant
| **EVALUATION KIT CONTENTS**
| ADR1000H-EBZ
| **EQUIPMENT NEEDED**
| Benchtop Lab Supply capable of 12V to 18V (15V nominal)
| Several Digit DMM (such as HP3458 or Keithley 2001)
| Two banana plug cables, or one dual cable
| One additional cable for meters with Guard, or use Pomona 1167-18
| **GENERAL DESCRIPTION**
| The ADR1000H-EBZ allows the evaluation of the ADR1000AHZ, ultra-stable 6.6V Shunt Voltage Reference in 8-Pin TO-99 package.

The DUT is centered in a fan shaped cutout of the PCB, designed to weaken mechanical coupling from the PCB to the DUT (effective for temperature and humidity, but not flexure). There are also thermal "baffles" (slots) in the PCB to keep heat from coupling from the heater transistor to the control circuit, and between the DUT and the resistors. The heater temperature is set by the standard 13k:1k divider as with the old LTZ1000. However, the ADR1000 runs about 5 degrees warmer (75C) than the LTZ1000 (70C), due to the slightly lower voltage of the ADR1000 applied to the divider.

| **EVALUATION BOARD PHOTOGRAPH**
| |image1|

Figure 1a. ADR1000H-EBZ, Primary Side

| **EVALUATION BOARD PHOTOGRAPH**
| |image2|

Figure 1b. ADR1000H-EBZ, Primary Side, covers removed, showing the cutouts

| **EVALUATION BOARD PHOTOGRAPH**
| |image3|

Figure 1c. ADR1000H-EBZ, Primary Side, thermal view

EVALUATION BOARD QUICK START PROCEDURES

| The following sections outline the basic prepopulated configuration of the ADR1000H-EBZ required to test the basic functionality of the ADR1000 and the application circuit.
| POWER SUPPLY CONSIDERATION
| The board is most easily powered through the small red and black turrets at TP4 (red) and TP7 (black) at the left hand side of the board. But ensure JP1 and JP2 are installed. Apply 15V typically.
| INITIAL BOARD CONFIGURATION
| The ADR1000H-EBZ comes pre-configured with jumpers on JP1 and JP2. These jumpers force the opamp and Zener circuit to use the same power (VANA and VHEATER) and ground (AGND and HGND/DGND). The simplest way to get started is to leave the jumpers in place and apply 15V to TP4 (red) and TP7 (black). If you wish to use different supplies for the heater and the Reference circuit, remove JP1. Then you can run the Zener un-heated using the VANA and AGND on T1 wiring block, or run heated by also driving TP4 (red) with an independent supply. Leaving JP2 installed keeps all grounds shorted (DGND/HGND and AGND). If you remove JP2, this disconnects DGND/HGND from AGND. **Caution: do not take DGND/HGND below AGND, as this will forward the substrate on ADR1000.**
| USING THE EVALUATION BOARD FOR TESTING
| The board was designed to mate to a standard 0.75" centered HP3458 or equivalent precision DMM. The banana plugs and jacks are not soldered to the board, so you can remove them and re-install them depending on how you wish to mate to the DMM. Figure 1d shows the board mated with HP3458, banana plugs installed on the secondary side so that the voltage measured is positive, and with Ref- connected to the HP3458 Guard.
| |ADR1399H|

| Figure 1d. ADR1000H-EBZ direct coupled to HP3458
| |image4|

| Figure 1d. ADR1000H-EBZ direct coupled to HP3458, side view
| The board is not isolated, so power it with a conventional floating output benchtop power supply. Just power the board using one of the methods discussed, and start measuring the output DC voltage.
| EVALUATION BOARD SCHEMATIC AND ARTWORK
| |image5|

| Figure 2. ADR1000H-EBZ Schematic. The schematic is largely identical to the classic "7V Positive Reference Circuit" shown in the LTZ1000 data sheet.

.. image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz bom.png
   :alt: ADR1399H
   :width: 400px

Table 1. ORDERING INFORMATION BILL OF MATERIALS

::

     ESD Caution 

ESD (electrostatic discharge) sensitive device. Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, proper ESD precautions should be taken to avoid performance degradation or loss of functionality. Legal Terms and Conditions By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed. ©2019 Analog Devices, Inc. All rights reserved. Trademarks and registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz entire.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz zoom.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebc therm.jpg
   :width: 400px
.. |ADR1399H| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz 3458a.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz 3458b.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/adr1000h-ebz sch.png
   :width: 400px
