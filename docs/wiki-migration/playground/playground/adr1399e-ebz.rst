Evaluation Board for the ADR1399 Ultra Stable Shunt Voltage Reference in 8 Pin LCC
==================================================================================

Features
--------

| Enables efficient prototyping
| User defined circuit configuration
| Edge mounted SMA connector
| Simple connection to test equipment and other circuits
| RoHS compliant
| **EVALUATION KIT CONTENTS**
| ADR1399E-EBZ
| **EQUIPMENT NEEDED**
| USB-C Compatible charger / power supply, or
| Benchtop Lab Supply
| Several Digit DMM (such as HP3458 or Keithley 2001)
| Two banana plug cables, or
| One SMA to meter-compatible cable
| **GENERAL DESCRIPTION**
| The ADR1399E-EBZ allows the evaluation of the ADR1399KEZ, ultra-stable 7.05V Shunt Voltage Reference in 8-Pin LCC package.

The DUT is on a paddle shaped "island" area of PCB for less stress from board flexure and also for thermal isolation. It is inside a captive acrylic enclosure to reduce air flow and further improve thermal isolation. Ground planes are removed under the DUT except for a hatch ground on the bottom side, again to prevent excessive thermal conduction away from the oven-ized reference.

Isolated power means that the Reference output is effectively floated, removing the likelihood of ground loops. The isolation is bridged only by a 1Meg resistor. Power may be supplied via the USB-C cable, or 5V may be applied to “VUSB”, or power may be back driven onto the regulator outputs at “VPRE” or “V+”. The ultra-stable 7.05V is brought out to both banana jacks and to an edge mounted SMA connector.

| **EVALUATION BOARD PHOTOGRAPH**
| |image1|

Figure 1. ADR1399E-EBZ, Primary Side

EVALUATION BOARD QUICK START PROCEDURES

| The following sections outline the basic prepopulated configuration of the ADR1399E-EBZ required to test the basic functionality of the device.
| POWER SUPPLY CONSIDERATION
| Use a USB-C charger or other USB-C source to power the board. You should see a Green LED. Alternately, 5V can be applied between VUSB and DGND from a bench supply. This will power the isolating LMT8048 module, providing isolated power downstream. Alternately, the LTM8048 internal regulator can be back driven at VPRE/AGND (Max 20V). AGND is the Reference ground, so this approach is not isolated.
| INITIAL BOARD CONFIGURATION
| The ADR1399E-EBZ comes pre-configured. There are no jumpers or other settings. Just power the board using (only) one of the methods described above, and begin watching the 7.05V output at either the SMA output or the Banana jacks (or both). For the best investigation, you will need a 6-digit or higher meter, such as HP3458 or Keithley 2001/2 or equivalent.
| USING THE EVALUATION BOARD FOR TESTING
| The board was designed along the lines of a simple “pocket calibrator”, so alternate means of supplying the DUT were not thoroughly provided for. For example, the Heater- is directly grounded, so there is no means of providing a negative 15V supply to Heater- for an overall 30V heater supply.
| The board is very easy to use. Just power the board using one of the methods discussed, and start measuring the output DC voltage. If you measure the supply current, you should see an initial fairly high current as the heater brings the ADR1399 to temperature (approx. 95C). The ADR1399 has an internal current limit of about 100mA. After losses and transformer, this limits the 5V USB input current to about 300mA. Total current at the DUT can be easily measured by probing across the 1 Ohm resistor R1 (at TP3, TP1).
| EVALUATION BOARD SCHEMATIC AND ARTWORK
| |ADR1399H| Figure 2. ADR1399E-EBZ Schematic, DUT Section
| |image2| Figure 3. ADR1399E-EBZ Schematic, USB Conditioning, Isolated Power, and Regulator Sections
| |image3| Table 1. BILL OF MATERIALS

::

     ESD Caution 

ESD (electrostatic discharge) sensitive device. Charged devices and circuit boards can discharge without detection. Although this product features patented or proprietary protection circuitry, damage may occur on devices subjected to high energy ESD. Therefore, proper ESD precautions should be taken to avoid performance degradation or loss of functionality. Legal Terms and Conditions By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the “Evaluation Board”), you are agreeing to be bound by the terms and conditions set forth below (“Agreement”) unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (“Customer”) and Analog Devices, Inc. (“ADI”), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term “Third Party” includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED “AS IS” AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER’S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI’S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed. ©2019 Analog Devices, Inc. All rights reserved. Trademarks and registered trademarks are the property of their respective owners.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ADR1399E-EBZ_prophoto.jpg
   :width: 600px
.. |ADR1399H| image:: https://wiki.analog.com/_media/resources/eval/adr1399e_schem.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/adr1399e_schem_pwr.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/adr1399e_bom.jpg
   :width: 600px
