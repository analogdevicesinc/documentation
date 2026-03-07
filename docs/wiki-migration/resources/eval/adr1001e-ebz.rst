Evaluation Board for the ADR1001 Ultra Stable Buried Zener Voltage Reference in LCC-20
======================================================================================

Features
--------

| Easy to Carry and Power Up "Pocket Calibrator" Style
| Edge mounted SMA connector
| Simple connection to test equipment and other circuits
| RoHS compliant
| **EVALUATION KIT CONTENTS**
| ADR1001E-EBZ
| **EQUIPMENT NEEDED**
| USB-C Compatible charger / power supply, or
| Benchtop Lab Supply
| Several Digit DMM (such as HP3458 or Keithley 2001)
| Two banana plug cables, or
| One SMA to meter-compatible cable
| **GENERAL DESCRIPTION**
| The ADR1001E-EBZ allows the evaluation of the ADR1001AHZ, ultra-stable 6.6V Shunt Voltage Reference with Resistor Divider in LCC-20 package.

Isolated power means that the Reference output is effectively floated, removing the likelihood of ground loops. The isolation is bridged only by a 1Meg resistor. Power may be supplied via the USB-C cable, or 5V may be applied to “VUSB”, or power may be back driven onto the regulator outputs at “VPRE” or V+”. The ultra-stable 6.5V is divided down to a precision trimmed 5V which is brought out to both banana jacks and to an edge mounted SMA connector. .

| **EVALUATION BOARD PHOTOGRAPH**
| |image1|

Figure 1. ADR1001E-EBZ, Primary Side

EVALUATION BOARD QUICK START PROCEDURES

| The following sections outline the basic prepopulated configuration of the ADR1399H-EBZ required to test the basic functionality of the device.
| POWER SUPPLY CONSIDERATION
| Use a USB-C charger or other USB-C source to power the board. You should see a Green LED. Alternately, 5V can be applied between VUSB and DGND from a bench supply. This will power the isolating LMT8048 module, providing isolated power downstream. Alternately, the downstream regulators can be back driven at VPRE/AGND (Max 20V) or at V+/AGND (Max 16V). AGND is the Reference ground, so this approach is not isolated.
| INITIAL BOARD CONFIGURATION
| The ADR1001E-EBZ comes pre-configured. There are no jumpers or other settings. Just power the board using (only) one of the methods described above, and begin watching the 5V output at either the SMA output or the Banana jacks (or both). For the best investigation, you will need a 6-digit or higher meter, such as HP3458 or Keithley 2001/2 or equivalent.
| When the board is powered, a green and a red LED should illuminate. When the chip reaches temperature, the red LED should turn off.
| USING THE EVALUATION BOARD FOR TESTING
| The board was designed along the lines of a simple “pocket calibrator”, so alternate means of supplying the DUT were not thoroughly provided for. For example, the Heater- is directly grounded, so there is no means of providing a negative 15V supply to Heater- for an overall 30V heater supply.
| The board is very easy to use. Just power the board using one of the methods discussed, and start measuring the output DC voltage. If you measure the supply current, you should see an initial fairly high current as the heater brings the ADR1001 to temperature (approx. 70C). The ADR1001 has an internal current limit of about 100mA, but the on board LT3045’s have been configured to limit available current to 75mA. After losses and transformer, this limits the 5V USB input current to about 250mA.
| The TSET pin is brought out to resistors R14 and R15 to allow for adjustment of the chip temperature. The INV1 and INV2 pins are brought out to TP7 and TP8 allowing access to the on-chip matched resistor pair, but no simple means of using them in circuit has been provided, as we sought to optimize the 5V reference and not introduce more thermocouples.

| EVALUATION BOARD SCHEMATIC AND ARTWORK
| Figure 2. ADR1001E-EBZ Schematic, DUT Section
| |ADR1399H|

| Figure 3. ADR1001E-EBZ Schematic, USB Conditioning, Isolated Power, and Regulator Sections
| |image2|

| Table 1 ORDERING INFORMATION BILL OF MATERIALS
| |image3|

::

     ESD Caution 

ESD (electrostatic discharge) sensitive device. Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, proper ESD precautions should be taken to avoid performance degradation or loss of functionality. Legal Terms and Conditions By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed. ©2019 Analog Devices, Inc. All rights reserved. Trademarks and registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/0056732_2.jpg
   :width: 400px
.. |ADR1399H| image:: https://wiki.analog.com/_media/resources/eval/adr1001_analog_sch.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adr1001 power sch.PNG
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adr1001_bom.PNG
   :width: 400px
