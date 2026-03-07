:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

Two Step Discovery for AD2437 Platforms
=======================================

AD2437 Platforms support “Two step Discovery” to avoid enabling 24V biasing (High Power) without confirming that downstream device is the intended AD2437 based A2B device. During two step discovery, 5V biasing is enabled first using on board regulator to discover the device. Once discovery is done, EEPROM available on the sub node is read to confirm that it supports high power. Post that, rediscovery is initiated using 24V. Before initiating Two step discovery for downstream, it is required to confirm that 5V power supply on the upstream node is stable. GPIO7 is used to indicate that.

Flowchart for Two Step Discovery
--------------------------------

Below figure captures the Two Step Discovery flow for AD2437 platforms

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/rj45_twostepdisc.png
   :align: center

.. container:: centeralign

   \ **Figure:** Two Step Discovery flow for AD2437 platforms


EEPROM Content for Two Step Discovery
-------------------------------------

Below Table lists down the EEPROM data required for Two Step Discovery

+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| **EEPROM Address(0x51)** | **Field Details**         | **Size(Bytes)** | **Value**             | **Remarks**                      |
+==========================+===========================+=================+=======================+==================================+
| 0x0                      | Start Byte                | 1               | 0xAA                  |                                  |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x1                      | Vendor ID                 | 2               | 0xAD                  |                                  |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x3                      | Product ID                | 2               | 0x37                  |                                  |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x5                      | Version ID                | 2               | Si Version            | This is more for information     |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x23                     | Power configuration       | 1               | Sub nodes - 0x40      | **Bits 7:4:**                    |
|                          |                           |                 | Main as LPS - 0x41    | **0:-** CFG 0 (Standard Powered) |
|                          |                           |                 |                       | **4:-** CFG 4 (High Powered)     |
|                          |                           |                 |                       | **Bit 0:**                       |
|                          |                           |                 |                       | **0-** Bus Powered               |
|                          |                           |                 |                       | **1-** Local Powered             |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x24                     | Maximum Power Consumption | 2               | TBD for RJ45 platform |                                  |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x26                     | Minimum Power Consumption | 2               | TBD for RJ45 platform |                                  |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+
| 0x28                     | B-Side Cable Type         | 1               | 0x2                   | RJ45 on ADI RJ45 platforms       |
+--------------------------+---------------------------+-----------------+-----------------------+----------------------------------+

.. container:: centeralign

   \ **Table:** EEPROM Content for Two Step Discovery


.. note::

   Currently Software verifies only the Vendor ID, Product ID and High-Power configuration. Other checks would be added in the later release.


Two Step Discovery configuration using SigmaStudio+
---------------------------------------------------

User may decide to enable or disable the Two Step discovery for a given sub node using “Enable Two Step Discovery” checkbox. If this check box is unchecked, upstream node will directly enable 24V biasing without verifying the EEPROM content on sub node’s EEPROM.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/two_step_disovery.png
   :align: center

.. container:: centeralign

   \ **Figure:** Enable/Disable Two Step Discovery flow for RJ45 platforms

