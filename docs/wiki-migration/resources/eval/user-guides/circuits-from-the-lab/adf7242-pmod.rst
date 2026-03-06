2.4 GHz Wireless Transceiver PMOD
=================================

:adi:`EVAL-ADF7242-PMDZ (Product Page) <EVAL-ADF7242-PMDZ>`

Overview
--------

The low cost and small profile RF solution 2.4 GHz, 802.15.4/Proprietary Wireless Transceiver PMOD board (:adi:`EVAL-ADF7242-PMDZ`) is designed to support RF to FPGA or processor applications system that utilizes PMOD-compatible expansion ports configurable for SPI communication (PACKET MODE). For applications that require data streaming, a synchronous bidirectional serial port (SPORT) interface is also available. The Wireless Transceiver PMOD board can be selectively configured to operate on the 2400 MHz to 2483.5 MHz ISM band. This uses single chip :adi:`ADF7242` 2.4Ghz transceiver, with most of the system blocks embedded on chip, and minimizing eternal RF components.

This wireless transceiver PMOD board uses mini 2.4 GHz chip antennas. In conjunction with the impedance-matched (complex differential impedance value) filter balun, reduces the RF front end count. This PMOD board supports polarization diversity that uses two chip antennas which can greatly improve performance under multipath fading conditions.

Refer to the :adi:`ADF7242` data sheet for detailed information regarding operation of the device.

Applications
~~~~~~~~~~~~

-  Zigbee
-  Home automation
-  Consumer electronics
-  Monitoring
-  Remote control
-  Wireless sensor networks

--------------

Specifications
--------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adf7242_pmod/table_2_n.png
   :width: 600px

--------------

| 

Interface Connector Signal Description
--------------------------------------

| |image1|

--------------

.. _interface-connector-signal-description-1:

Interface Connector Signal Description
--------------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adf7242_pmod/table_3.png
   :width: 400px

--------------

Functional Block Diagram
------------------------

| |image2|
| ===== Schematic, PCB Layout, Bill of Materials =====

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADF7242-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-adf7242-pmdz-designsupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   
   |


| ===== Additional Information and Useful Links =====

-  :adi:`ADF7242 Product Page <ADF7242>`
-  :doc:`ADF7242 Linux driver </wiki-migration/resources/tools-software/linux-drivers/networking-mac802154/adf7242>`
-  :doc:`Using ADF7242 with Contiki Operating System </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/contiki-os>`
-  :adi:`AN-1151 Using a Johanson 2450BM14E0007 Impedance-Matched, Integrated Filter Balun with the ADF7241 and ADF7242 <static/imported-files/application_notes/AN-1151.pdf>`

Registration
------------

|

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADF7242-PMDZ?&v=RevA>`__ to receive all these great benefits and more!


| // End of Document

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adf7242_pmod/table_1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adf7242_pmod/block.png
   :width: 900px
