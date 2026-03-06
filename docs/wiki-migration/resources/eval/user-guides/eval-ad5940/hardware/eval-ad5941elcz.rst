AD5941 Electrochemical Shield User Guide
========================================

Introduction
------------

The EVAL-AD5941ELCZ shield was designed specifically for carrying out electrochemical measurements. These include:

-  Measurements on a dummy RC sensor
-  Electrochemical Gas Sensing
-  Water Quality

   -  Conductivity
   -  pH
   -  Oxidation Reduction

-  General electrochemical measurements through cables provided

The platform is an Arduino form factor that can be used with any Arduino form-factor base board. This section describes the features of the evaluation board and how to use it.


|image1|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/ad5941_elcz.jpg
   :align: center
   :width: 600px

Connectors and Jumpers
----------------------

All the connectors and their default configurations are described in the table below.

+------------------------+------------------------------------------+------------------------------------------------------+
| Connector              | Jmpr Position.                           | Description                                          |
+========================+==========================================+======================================================+
| JP1 (DVDD)             | A                                        | DVDD powered from 3.3V on Arduino Header (Default)   |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | DVDD powered from LDO                                |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | DVDD powered from external source connected to P11   |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP2 (AVDD)             | A                                        | AVDD powered from 3.3V on Arduino Header (Default)   |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | AVDD powered from LDO                                |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | AVDD powered from external source connected to P8    |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP3 (Reset)            | A                                        | Reset pin connected to ARST Button (Default)         |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | Reset pin connected to Arduino Header Reset pin      |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | Reset pin connected to Arduino header P1.3 (Default) |
+------------------------+------------------------------------------+------------------------------------------------------+
| P9 (LDO Enable)        | 1-2                                      | LDO Enabled                                          |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | 2-3                                      | LDO Disabled (Default)                               |
+------------------------+------------------------------------------+------------------------------------------------------+
| P10 (LDO Aux Enable)   | 1-2                                      | LDO Enabled                                          |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | 2-3                                      | LDO Disabled (Default)                               |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP6 (Dummy RC)         | A                                        | Connect network A to CE, RE and SE (Default)         |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | Connect network B to CE, RE and SE                   |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP9,JP10,JP11          | Note, A is 1-2, B is 3-4, C is 5-6 (USB) |                                                      |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP9 (DE0 Mux)          | A                                        | DE0 connected to Gas sensor connector                |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | DE0 connected to dummy network                       |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | DE0 connected to USB port                            |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP10 (RE0 Mux)         | A                                        | RE0 connected to gas sensor                          |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | RE0 connected to dummy network                       |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | RE0 connected to USB port                            |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP11 (SE0 Mux)         | A                                        | SE0 connected to gas sensor                          |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | SE0 connected to dummy network                       |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | SE0 connected to USB port                            |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP4 (Cable Shield Mux) | A                                        | Shield connected to CE0                              |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | Shield connected to Bead                             |
+------------------------+------------------------------------------+------------------------------------------------------+
| JP5 (BNC Mux)          | A                                        | Water conductivity                                   |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | B                                        | pH Measurement                                       |
+------------------------+------------------------------------------+------------------------------------------------------+
| :::                    | C                                        | Connected to AFE1                                    |
+------------------------+------------------------------------------+------------------------------------------------------+

USB Connector and Cable
-----------------------

The USB connector provides an interface to connected the provided USB to Crocodile cable to the AD5941. This USB connector is only intended to be used in conjunction with the provided USB to crocodile cable. No other USB cable should be ever be connected.

The following table shows which color lead corresponds to which input:

=============== ====================== ===================
Connector Color Description            Schematic Reference
=============== ====================== ===================
Red             Counter Electrode      USB_1
Blue            Reference Electrode    USB_2
Green           Working Electrode      USB_3
Black           Connected to DE0 input USB_4
=============== ====================== ===================

The image below shows the crocodile connected to the EVAL-AD5941ELCZ. A dummy sensor consisting of a Resistor in parallel with a capacitor is connected. The counter and reference connectors are connected to one end and the working electrode is connected to the other end.


|image2|

Note, the USB to crocodile cable is intended for rapid prototyping. There is a parasitic resistance and capacitance associated with it which may effect measurement accuracy. This is especially through for high frequency impedance measurements.

EC Gas Connector
----------------

M1 is an Electrochemical gas sensor socket. Standard EC gas sensors can be connected to perform gas sensor measurements. When measuring a Gas sensor ensure JP9, JP10 and JP11 are switched to position C.

BNC Connector
-------------

The BNC connector is connected to the AD5941 via LTC6078 amplifier. This amplifier can be used with high impedance sensor's such as pH sensors and for water conductivity measurements.

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   
   EVAL-AD5941ELCZ Rev A Design and Integration Files
   
   -  `Schematics (PDF) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/02-057011-01-a-1.pdf>`__
   -  `PCB Layout (PDF) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/08-057011-01-a-1.pdf>`__
   -  `Bill of Materials (Excel) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/05-057011-01-a.xlsx>`__
   -  `Fabrication Files (zip) <https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/09-057011-01a.zip>`__
   


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/eval_ad5941_elcz.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/elcz_cable.jpg
   :width: 600px
