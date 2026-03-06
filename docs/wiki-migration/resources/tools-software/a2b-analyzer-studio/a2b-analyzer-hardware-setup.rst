:doc:`Click here to return to A2B Analyzer Studio Homepage. </wiki-migration/resources/tools-software/a2b-analyzer-studio>`

A2B Bus Analyzer and A2B Analyzer HP Hardware Setup
===================================================

Introduction
============

The guidelines on these pages are intended to help A\ :sup:`2`\ B users configure and use the ADI A\ :sup:`2`\ B Analyzer Studio tool in Monitor or Emulator mode for A2B1.0 and A2B2.0 networks on A\ :sup:`2`\ B Bus Analyzer and A\ :sup:`2`\ B Analyzer HP respectively. 

Getting Started with A2B Analyzer HP
====================================

A2B Analyzer HP Setup
---------------------

| 1. Connect the A\ :sup:`2`\ B Analyzer HP to your PC using the supplied USB-C to USB-C cable. You may also use USB-C to USB-A cable with 24V power supply.
| |image1|

| 2. Connect 24V power supply to A\ :sup:`2`\ B Analyzer HP. A\ :sup:`2`\ B Analyzer HP supports both power and data over USB-C. USB-C power alone may not be sufficient to use the A\ :sup:`2`\ B Analyzer HP to its full capacity. When the power is not sufficient, an error message is displayed in the User Interface. To allow the connection a 24V power supply must be connected.
| |image2|

3. Ensure your A\ :sup:`2`\ B Analyzer Studio software is installed, and upgraded as explained in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` Section *"Installation and Upgrades"*.

| 4. Launch A\ :sup:`2`\ B Analyzer Studio. Connect to your A\ :sup:`2`\ B Analyzer HP device by selecting it from the device selection drop-down menu then clicking the Power button. Once connected, the Power button becomes green.
| |image3|

Hardware setup for using A2B Analyzer HP as Bus Monitor
-------------------------------------------------------

1. Complete steps in `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

2. For custom cabling, please use the below pinout details.


|image4|

-  P1 (towards main): 1 - AN, 2 - AP(left to right)
-  P2 (towards sub):   1 - BN, 2 - BP (left to right)

| 3. Connect A\ :sup:`2`\ B Analyzer HP unit between two nodes in an A\ :sup:`2`\ B network. **You must use personality module 2 for monitor functionality.**
| **Note:** It is recommended to place the A\ :sup:`2`\ B Analyzer HP between the Main and first Sub node (Sub node0) to allow capturing all events on the bus.
| |image5|

4. If ADI evaluation boards are used for main and sub-node, please refer the following path for documentation on how to set up a network using ADAA245x-EV-A1CA + ADAA24xx-EV-B2BX eval boards.

-  <Installation path of SigmaStudio+>\\docs\\root-qsg\\resources\\pages\\quick-start-guide\\gui\\examples\\adaa245x-ev-a1ca-rev-d_adaa24xx-ev-b2bx-rev-c_3-node.html
-  Also, please refer to the specific jumper settings for main node and sub-node.

5. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Analyzer HP as Bus Monitor" * for using A\ :sup:`2`\ B Analyzer Studio software.

Hardware setup for using A2B Analyzer HP as Node Emulator
---------------------------------------------------------

Main Node Emulator
~~~~~~~~~~~~~~~~~~

1. Complete steps in `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

2. For custom cabling, please use the below pinout details.


|image6|

-  P1 (towards main): 1 - AN, 2 - AP(left to right)
-  P2 (towards sub):   1 - BN, 2 - BP(left to right)

| 3. Connect Sub node or chain of Sub nodes to the node emulator port labelled “TOWARDS SUB”. **You must use personality module 1 for emulator functionality.**
| |image7|

4. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Analyzer HP as Node Emulator - Main Node Emulator" * for using A\ :sup:`2`\ B Analyzer Studio software.

Sub Node Emulator
~~~~~~~~~~~~~~~~~

1. Complete steps in `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

2. For custom cabling, please use the below pinout details.


|image8|

-  P1 (towards main): 1- AN, 2 - AP(left to right)
-  P2 (towards sub): 1 - BN, 2 - BP(left to right)

| 3. Insert the A\ :sup:`2`\ B Analyzer HP unit in an A\ :sup:`2`\ B network at a desired Sub node position to be emulated. Connect the unit to an upstream node, using TOWARDS MAIN, and to a downstream node, using TOWARDS SUB (if it is not the last node). **You must use personality module 1 for emulator functionality.**
| |image9|

4. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Analyzer HP as Node Emulator - Sub Node Emulator" * for using A\ :sup:`2`\ B Analyzer Studio software.

Getting Started with A2B Bus Analyzer
=====================================

A2B Bus Analyzer Setup
----------------------

| 1. Connect the A\ :sup:`2`\ B Bus Analyzer to your PC using the supplied USB-A to Micro-B cable.
| |image10|

| 2. Connect 12V power supply to A\ :sup:`2`\ B Bus Analyzer.
| |image11|

3. Ensure your A\ :sup:`2`\ B Analyzer Studio software is installed, and upgraded as explained in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` Section *"Installation and Upgrades"*.

| 4. Launch A\ :sup:`2`\ B Analyzer Studio. Connect to your A\ :sup:`2`\ B Bus Analyzer device by selecting it from the device selection drop-down menu then clicking the Power button. Once connected, the Power button becomes green.
| > |image12|

Hardware setup for using A2B Bus Analyzer as Bus Monitor
--------------------------------------------------------

1. Complete steps in `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

2. For custom cabling, please use the below pinout details.


|image13|

-  P1 (towards main): 1 - NC, 2 - AN, 3 - AP, 4 – NC (left to right)
-  P2 (towards sub): 1 - NC, 2 - AP, 3 - AN, 4 – NC (left to right)

| 3. Connect A\ :sup:`2`\ B Bus Analyzer unit between two nodes in an A\ :sup:`2`\ B network.
| **Note:** It is recommended to place the analyzer between the Main and first Sub node (Sub node0) to allow capturing of all events on the bus.
| |image14|

4. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Analyzer HP as Bus Monitor" * for using A\ :sup:`2`\ B Analyzer Studio software.

Hardware setup for using A2B Bus Analyzer as Node Emulator
----------------------------------------------------------

For customer cabling, please use the below pinout details:

**High power connector:**

-  P7 (towards sub): 1 - GND, 2 - BP, 3 - BN, 4 – GND (left to right)
-  P8 (towards main): 1 - GND, 2 - AN, 3 - AP, 4 – GND (left to right)

**Standard power connector:**

-  P6 (towards sub): 1 - BP, 2 – BN (left to right)
-  P3 (towards main): 1- AN, 2- AP (left to right)

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_15.png
   :width: 400px

.. _main-node-emulator-1:

Main Node Emulator
~~~~~~~~~~~~~~~~~~

1. Complete the steps in `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

| 2. Connect Sub node or chain of Sub nodes to the node emulator port labelled “TOWARDS SUB” on STD or HIGH PWR depending on the power configuration of the node being emulated
| |image15|

3. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Bus Analyzer as Node Emulator - Main Node Emulator" * for using A\ :sup:`2`\ B Analyzer Studio software.

.. _sub-node-emulator-1:

Sub Node Emulator
~~~~~~~~~~~~~~~~~

1. Complete steps in Section `A2B Bus Analyzer and A2B Analyzer HP Hardware Setup <https://wiki.analog.com/>`__.

| 2. Insert the A\ :sup:`2`\ B Bus Analyzer unit in an A\ :sup:`2`\ B network at a desired Sub node position to be emulated. Connect the unit to an upstream node, using TOWARDS MAIN, and to a downstream node, using TOWARDS SUB (if it is not the last node), on STD or HIGH PWR node emulator ports depending on the power configuration of the node being emulated.   
| |image16|

3. Follow the instructions in :doc:`A2B Analyzer Studio Quick Start Guide. </wiki-migration/resources/tools-software/a2b-analyzer-studio/quick-start-guide>` section *"Using A2B Bus Analyzer as Node Emulator - Sub Node Emulator"  * for using A\ :sup:`2`\ B Analyzer Studio software.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_3.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_4.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_5.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_6.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_7.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_8.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_9.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_10.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_11.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_12.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_13.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_14.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_16.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-analyzer-studio/A2BASHW_17.png
   :width: 600px
