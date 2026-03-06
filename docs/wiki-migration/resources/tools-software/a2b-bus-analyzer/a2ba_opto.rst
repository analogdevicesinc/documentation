Setting up the A2B Analyzer (as main node) for optoA2B
======================================================

The procedure to use optoA\ :sup:`2`\ B with A\ :sup:`2`\ B Bus Analyzer is as follows:

This section will guide the user to configure an OptoA\ :sup:`2`\ B branch network using ADI’s A\ :sup:`2`\ B Bus Analyzer as main node in the following configuration:

A\ :sup:`2`\ B Analyzer <--> Opto A\ :sup:`2`\ B Sub<--> Opto A\ :sup:`2`\ B Main <--> A\ :sup:`2`\ B Sub node DUT

+--------+-----------------------------+----------------+--------------------------------------------------------------------------------------------------------+
| SI No. | Software Component          | Version        | Comments                                                                                               |
+========+=============================+================+========================================================================================================+
| 1.     | SigmaStudio+                | 2.1.0 or later | :doc:`SS+ Guide </wiki-migration/resources/tools-software/sigmastudiov2>`                              |
+--------+-----------------------------+----------------+--------------------------------------------------------------------------------------------------------+
| 2.     | A\ :sup:`2`\ B              | 1.3.1 or later | :doc:`User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`                  |
+--------+-----------------------------+----------------+--------------------------------------------------------------------------------------------------------+
| 3.     | A\ :sup:`2`\ B Bus Analyzer | 3.4 or later   | :doc:`Quick Start Guide </wiki-migration/resources/tools-software/a2b-bus-analyzer/quick-start-guide>` |
+--------+-----------------------------+----------------+--------------------------------------------------------------------------------------------------------+

.. tip::

   Please contact A\ :sup:`2`\ B SW and A\ :sup:`2`\ B Analyzer support teams for latest updates


Example Project
---------------

A\ :sup:`2`\ B Analyzer <--> Opto A\ :sup:`2`\ B Sub <--> Opto A\ :sup:`2`\ B Main <--> A\ :sup:`2`\ B Sub node DUT

Project file: <Installation Path>\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\A2BBusAnalyzer\\adi_a2bbusanalyzer_243xStdPwrMain_242xOptoA2B.ssproj

Hardware Requirements
---------------------

+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| Sl. No | Name of Board                                       | Type of Board/ Node                                                                                        | Quantity |
+========+=====================================================+============================================================================================================+==========+
| 1      | A\ :sup:`2`\ B Bus Analyzer kit                     | Emulated as Main node                                                                                      | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 2      | Twisted Pair A\ :sup:`2`\ B Cable                   | DuraClik connector on one end to Analyzer and Rosenberger HSD connector on one end to OptoA2B Main         | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 3      | 12V Power Supply                                    | -                                                                                                          | 2        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 4      | USB cable from PC to A2B Bus Analyzer               | -                                                                                                          | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 5      | Audio source (non-grounded)                         | ­­­­­e.g., PC/Mobile phone                                                                                 | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 6      | Aux Cable                                           | -                                                                                                          | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 7      | Audio Sink Devices                                  | 3.5mm Jack Headphones                                                                                      | 1        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+
| 8      | AD2428WD1BZ (for emulating optoA\ :sup:`2`\ B only) | Primary chain-sub, Branch Main, Branch Sub - NOT required when actual optoA\ :sup:`2`\ B is available      | 3        |
+--------+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------+

System Block Diagram
--------------------

| |image1|
|

.. note::

   AD2428WD1BZ boards are used to emulate optoA\ :sup:`2`\ B sub and branch-main in the above figure.


OptoA2B Setup
-------------

| |image2|
| OptoA\ :sup:`2`\ B main and DUT are present inside the EMC chamber while A\ :sup:`2`\ B Bus Analyzer and optoA\ :sup:`2`\ B sub are outside the chamber.

A2B Analyzer Settings
---------------------

A2B Analyzer to be kept in Standard power Emulator mode.

Procedure
---------

Procedure to run a Branch Network (Opto A2B) from ADI A\ :sup:`2`\ B Analyzer:

-  In SigmaStudio+, create a schematic with the A2BBusAnalyzer platform as the main node Emulator and the OptoA2B platform as a sub node, and connect a Device under test as a sub node for the optoA2B branching chain. Schematic should be designed to have upstream audio from branch to A2B analyzer main.

   -  Drag an analyzer platform from the toolbox and change into main node.


   |image3|

   -  Drag a OptoA2B platform from Toolbox.

::

     *{{:resources:tools-software:a2b-bus-analyzer:optoa2b_treetoolbox_.png|}}
   * Drag a A2B sub node as DUT & connect to branching chain and save the project. 
     *{{:resources:tools-software:a2b-bus-analyzer:a2b_platform.png  |}}
   * One-click procedure: Press Link-Compile-Download button in SigmaStudio+. SigmaStudio+ will launch the A2B Bus Analyzer automatically and discover the primary chain via .Dat file and secondary chain via command list.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/optoa2b_schematic_lcd.png
   :align: center

-  The audio streams from the DUT are now available on the main emulator for analysis and logging.

.. note::

   Post Discovery Branching chain register/peripheral read/write is not supported.


.. note::

   Once the primary chain is discovered, each secondary chain commands are taken as individual branch transactions with its own CHIP, NODEADR and PERI transactions as show below.


| |image4|
| ===== APPENDIX =====

Jumper Settings
~~~~~~~~~~~~~~~

Opto A2B Sub to Opto A2B main (in the current example AD2428WD1BZ is used for Opto Sub and Opto main)

=========== =====================
Jumper      Opto Sub to Opto Main
=========== =====================
JP5 (BCLK)  3 → 3
JP6 (SYNC)  3 → 3
DRX0 - DTX0 3(JP7) → 2(JP10)
DRX1 - DTX1 2(JP8) → 3(JP9)
DTX0 - DRX0 2(JP10) → 3(JP7)
DTX1 - DRX1 3(JP9) → 2(JP8)
P1(SCL)     1 → 1
P1(SDA)     3 → 3
P1(GND)     10 → 10
=========== =====================

A2B Sub node DUT (in the current example – AD2428WD1BZ is used as Sub node DUT)

+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| Jumper             | LPS       | Comments                                                                                        |
+====================+===========+=================================================================================================+
| JP1 (A2B power)    | Install   | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP2                | Uninstall | Install when phantom power or hybrid power support is required                                  |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP3                | Uninstall | Install when phantom power or hybrid power support is required                                  |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP4 (BOOT)         | Install   | Self-Boot option disabled.                                                                      |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP5 (BCLK)         | 1-3       | AD2428_BCLK -> ADAU1961_BCLK                                                                    |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP6 (SYNC)         | 1-3       | AD2428_SYNC -> ADAU1961_LRCLK                                                                   |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP7 (DRX0)         | 1-3       | ADAU1961_ADC -> AD2428_DRX0                                                                     |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP8 (DRX1)         | Uninstall | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP9 (DTX1)         | Uninstall | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP10 (DTX0)        | 2-3       | AD2428_DTX0 -> ADAU1961_DAC                                                                     |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP11 (ADMP621 CLK) | Uninstall | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP12 (NTC)         | Install   | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP13 (A2B_REG)     | Uninstall | -                                                                                               |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP14 (VOLTAGE)     | Uninstall | Install/ Uninstall depending on VIN requirement. Installed -> VIN = 7V, Uninstalled -> VIN = 8V |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+
| JP19 (1961 BCLK)   | 2-3       | ADAU1761 MCLK from AD2428_BCLK                                                                  |
+--------------------+-----------+-------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/optoa2b.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/actual_optoa2b.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/analyzer_platform.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2b-bus-analyzer/optoa2b_transaction.png
