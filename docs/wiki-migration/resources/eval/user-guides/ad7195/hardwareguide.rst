EVAL-AD7195ASDZ Hardware Guide
==============================

Set-up Procedures
=================

After following the instructions in the :doc:`Software Procedures </wiki-migration/resources/eval/user-guides/ad7195/softwareguide>` section, set up the evaluation and SDP boards as detailed in this section.

-  **Warning:** The evaluation software and drivers must be installed before connecting the EVAL-AD7195ASDZ evaluation board and EVAL-SDP-CB1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.
-  Connect the EVAL-AD7195ASDZ to the controller board

   -  **Option A:** Connect the EVAL-AD7195ASDZ to the EVAL-SDP-CK1Z

      -  Using the 120 pin connector

         -   Screw the two boards together using the plastic screw-washer set included in the evaluation board kit to ensure that the boards are connected firmly together.
         -  Using the Arduino Connectors

         |image1|

   -  **Option B:** Connect the EVAL-AD7195ASDZ to the EVAL-SDP-CB1Z

      -  Using the 120 pin connector

         -   Screw the two boards together using the plastic screw-washer set included in the evaluation board kit to ensure that the boards are connected firmly together.

Block Diagram
=============

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195_blockdiag.png
   :align: center
   :width: 600px

Hardware Link Options
=====================

+--------------+--------+------------------+------------------------------------------------------------------------------------+
| Link Numbers | Colour | Default Position | Descirption                                                                        |
+==============+========+==================+====================================================================================+
| JP1          | Black  | A                | Used for stacking of Eval boards. To select Eval board(CS_N):                      |
|              |        |                  | Pos A(1-2): selects eval board 1 (CS_ARD_1)                                        |
|              |        |                  | Pos B(2-3): selects eval board 2 (CS_ARD_2)                                        |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| JP2          | Black  | C                | AVDD voltage select:                                                               |
|              |        |                  | Pos A: sets AVDD to 3.3v LDO supply                                                |
|              |        |                  | Pos B: sets AVDD to external source                                                |
|              |        |                  | Pos C: sets AVDD to 5V LDO Supply                                                  |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| JP3          | Black  | A                | IOVDD voltage select:                                                              |
|              |        |                  | Pos A: sets IOVDD to 3.3v LDO supply                                               |
|              |        |                  | Pos B: sets IOVDD to external source                                               |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| JP4          | Black  | Uninserted       | This link shorts AIN1 to AIN2. This is useful to perform noise tests on the AD7195 |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| JP5          | Black  | A                | DVDD voltage select:                                                               |
|              |        |                  | Pos A: DVDD is connected to 3.3V                                                   |
|              |        |                  | Pos B: DVDD is connected to AVDD                                                   |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| P15          | Black  | Uninserted       | Used as external AVDD voltage connector for scp boards                             |
+--------------+--------+------------------+------------------------------------------------------------------------------------+
| P16          | Black  | Uninserted       | Used as external IOVDD voltage connector for scp boards                            |
+--------------+--------+------------------+------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/ad7195links.png
   :align: center
   :width: 400px

On Board Connections
====================

Bridge Connections
------------------

Connector P9: DC (Analog Input)
-------------------------------

**Functionality:**

-  **Bridge Connection**

========== =======================
Connection Function
========== =======================
1          Ground/Sheild
2          Excitation+
3          External Reference +
4          AIN 3 with DC filtering
5          AIN 4 with DC filtering
6          External Reference -
7          BPDSW
8          Excitation-
========== =======================

Link JP4: Low Noise Test Circuitry
----------------------------------

**Functionality:**

-  **Low Noise Test**

-ALL INSERTED

========== ========
Connection Function
========== ========
1-2        AVDD
3-4        AIN1
5-6        AIN2
7-8        AINCOM
========== ========

External Powers
---------------

=========== ========================================
Connector   Function
=========== ========================================
P14 Pin 1-2 External IOVDD connection
P14 Pin 3-4 External AVDD connection
P15         External AVDD connection for SCP Boards
P16         External IOVDD connection for SCP Boards
=========== ========================================

Digital Connectors
------------------

========================= ========= =============================
SDP 120 Pin Connector P1  Function  Arduino connector P2,P3,P5,P6
========================= ========= =============================
3,4                       GND       P3-6,P3-7
5                         V_USB     P3-5
6,11,17,23,28,36,40,46,52 GND       P5-7
56                        EEPROM_A0 -
58,63,69,75               GND       -
78                        SYNC_IN   P6-5
79                        SCL       P6-10
80                        SDA       P6-9
81                        GND       -
82                        SCLK      P6-6
83                        SDO/MSIO  P6-5
84                        SDI/MOSI  P6-4
85                        CS_N      P5-3,P5-2
86,93,98,109,115          GND       -
116                       VIO       P3-2
117,118                   GND       -
========================= ========= =============================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/ad7195arduinoheader.png
   :align: center
   :width: 400px

PMOD Connector P8
~~~~~~~~~~~~~~~~~

========== ======== ========== ========
Connection Function Connection Function
========== ======== ========== ========
1          CS_N     7          -
2          DIN      8          -
3          DOUT     9          -
4          SCLK     10         -
5          GND      11         GND
6          IOVDD    12         IOVDD
========== ======== ========== ========

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/ad7195pmod.png
   :align: center
   :width: 400px

SMB Connections
---------------

There are 3 SMB connections on the board. To allow clock signals and reference into the board.

-  J1 Provides option for External Reference+
-  J2 Provides option for External Reference-
-  J3 Brings external MCLK to the AD7195

Power Supplies
==============

The evaluation board receives power through the controller board when connected to the PC via USB. Linear regulators generate the required power supply levels from the applied USB voltage.

AVDD (JP2) selection
--------------------

-  **5V supply (DEFAULT)**

   -  5V regulator supplies AVDD :adi:`ADP7142 <en/products/adp7142.html>`

-  \**3.3V supply \*\*

   -  3.3V regulator supplies AVDD :adi:`ADP150 <en/products/adp150.html>`

-  **External AVDD**

   -  Connections on Connector P14

DVDD (JP5) selection
--------------------

-  **3.3V supply (DEFAULT)**

   -  3.3V supplies DVDD

-  **AVDD**

   -  AVDD connected to DVDD

IOVDD (JP3) selection
---------------------

-  **3.3V supply (DEFAULT)**

   -  3.3V regulator supplies IOVDD :adi:`ADP150 <en/products/adp150.html>`

-  **External IOVDD**

   -  Connections on Connector P14

-  **V_IO from SDP**

   -  R38 to be mounted

Serial Interface
================

There are four primary signals: CS, SCLK, SDI, and SDO/RDY (all are inputs, except for SDO/RDY, which is an output).

Serial communication options
----------------------------

-  SDP-B board and the respective 120 pin SDP connector.

::

     *When using the SDP-B connection (120 pin) The evaluation board connects via the serial peripheral interface (SPI) to the Blackfin® [[:adi:`en/products/adsp-bf527`.html|ADSP-BF527]] on the SDP-B board. 
   * Arduino connection SDP-K1 
   * PMOD connector
   * Standalone mode
      

For an introduction to the Serial Peripheral Interface (SPI), click :adi:`here <en/analog-dialogue/articles/introduction-to-spi-interface.html>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/spi_pic.png
   :align: center
   :width: 400px

Reference Options
=================

-  **DEFAULT** :adi:`ADR4525 <en/products/adr4525.html>` On Board external reference on REFIN1+
-   :adi:`LTC6655LN-2.5/LTC6655LN-4.096 <en/products/ltc6655.html>` On Board external reference on REFIN+

   -  Option to use ultra low noise reference

-  External Reference on REFIN1+ Connector J1
-  AVDD as Reference via R25

Schematics
==========

`AD7195 Schematic pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/02-068126-01-b.pdf>`_

Bill of Materials
=================

`AD7195 Evaluation board Bill of materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/ad7195bom.pdf>`_

:doc:`Next Page: Software Procedures </wiki-migration/resources/eval/user-guides/ad7195/softwareguide>`

:doc:`Return to Homepage </wiki-migration/resources/eval/user-guides/ad7195>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7190/sdp_connect.png
   :width: 400px
