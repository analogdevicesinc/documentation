Energy Harvesting- Eaton Board Demo
===================================

Energy Harvesting using Eaton Board is a system that is used to power up the MCU using PV cell.It is ultralow power wireless sensor node that is powered using Energy Harvesting

General Description
-------------------

1) ADF7030-1 - It is high performance low power Sub GHz radio transceiver. It has data rate of 0.1Kbps to 300 Kbps. The frequency range is 169Mhz to 960 Mhz.

2) ADuCM3029- It is an ultra low power ARM Cortex M3 MCU. 780nA in Hibernate mode with RTC enabled

3) ADP5091 - It is an intelligent, integrated energy harvesting, ultralow power management unit (PMU) solutions that convert dc power from PV cells or TEGs. These devices charge storage elements such as rechargeable Li-Ion batteries, thin film batteries, super capacitors.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adp.png
   :align: center
   :width: 400px

Demo Setup
----------

1) Transmitter node :

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eh.png
   :align: center
   :width: 400px

2) Receiver node :

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eh12.png
   :align: center
   :width: 600px

Demo Requirements
-----------------

Transmitter node:

-  ADF70301EHZ- Energy Harvesting Board
-  Photo voltaic cell

Receiver node:

-  ADuCM3029 EZ-Kit
-  LCD Screen
-  ADF7030 RF module with antenna on RX.

Setting Up the Hardware
-----------------------

ADP5091 converts the dc power of the PV cell and stores the charge in rechargeable battery like capacitor. The charge stored in the capacitor is used to provide required 3.3 V to power up the MCU.

-  Connect a super capacitor as shown in the diagram above. When the charge in capacitor is above 2.8V the MCU wakes up and transmits the temperature values
-  The Vin of the Energy harvesting board should be connected to the first pin of the PV cell.
-  The Gnd pin of Energy Harvesting board should be connected to the fourth pin of PV cell.
-  A constant power source is required to charge the super capacitor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/setup.png
   :align: center
   :width: 400px

Obtaining Source Code
---------------------

.. admonition:: Download
   :class: download

   
   The source code has to be inserted from the github
   
   |


| ===== Data Output=====

The temperature results on the receiver node is shown below:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/temp.png
   :align: center
   :width: 400px

-  The six rows in the display shows that 6 energy harvesting nodes are possible.
-  The node which is sending the temperature values is indicated by "\*".
-  In the above example, node 5 is sending the temperature values.
-  There are three columns of temperature values displayed.
-  Each time a new value arrives, it appears on the first column and previous value gets shifted.
