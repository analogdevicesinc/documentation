EVAL-ADBMS6822 User Guide
=========================

Overview
--------

| The :adi:`EVAL-ADBMS6822` is a dual SPI to 2-wire isolated serial port interface (isoSPI) adapter featuring the :adi:`ADBMS6822`. This board allows multiple ADBMS68xx battery monitors through daisy-chain connections. The EVAL-ADBMS6822 evaluation board also features reversible isoSPI, which enables a redundant path to the peripheral units. The PCB components and DuraClik connectors are optimized for low electromagnetic interference (EMI) susceptibility and emissions.
| The :adi:`EVAL-ADBMS6822` evaluation board can communicate to PC by connecting together with EVAL-SDP-CK1Z. The EVAL-ADBMS6822 evaluation board provides a standard SPI, which can be translated to isoSPI and then onward to a peripheral device or daisy chain as applicable.
| The :adi:`EVAL-ADBMS6822` evaluation board can also be used to evaluate the ADBMS6821. Note that for the ADBMS6821, there is only one SPI port; therefore, ignore the second SPI port and auxiliary isoSPI when using the ADBMS6821.
| Full specifications on the ADBMS6822 dual isoSPI adapter are available in the ADBMS6821/ADBMS6822 data sheet available from Analog Devices, Inc. and must be consulted with this user guide when using the EVAL-ADBMS6822 evaluation board.

| 
| ==== Features ====

-  Full-featured evaluation board for the ADBMS6822
-  Demonstrates SPI to isoSPI 2-wire datalinks
-  Includes two isoSPi ports for reversible isoSPI support
-  Configurable powering options for LPCM support isoSPI connections through simple DuraClik connectors
-  Compatible with the EVAL-ADBMS68xx boards, battery monitor boards, EVAL-SDP-CK1Z controller board
-  With PC-based software for control and data analysis using Broad Market Browser BMS GUI

| 
| ==== Applications ====

-  Electric and hybrid electric vehicles
-  Backup battery systems
-  Industrial networking
-  Remote sensors
-  Mobile Robot System
-  E-scooter/E-bikes/Light Electric Vehicle
-  Agricultural Gateway Hubs
-  Industrial Equipment Battery Monitoring
-  Metering Technology
-  Power Tools

| 
| ===== System Architecture =====
| |image1|
| |image2|

| 

Specifications
--------------

.. container:: center

   
   ============================ ================= =================
   **Parameter**                **Min**           **Max**
   V\ :sub:`DD` Supply Voltage  3 V               5.5 V
   V\ :sub:`DDS` Supply Voltage 1.7 V             5.5 V
   V+ Supply Voltage            3 V               30 V
   V+ Supply Voltage (LPCM)     6 V               30 V
   V\ :sub:`IH` Input Range     0.7 V\ :sub:`DDS` -
   V\ :sub:`IL` Input Range     -                 0.7 V\ :sub:`DDS`
   ============================ ================= =================
   


| 
| ----

Hardware Connections
--------------------

| 
|

.. container:: indent

   
   Shield-Mount Board Connection
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   | The primary connection for the EVAL-ADBMS6822 is by plugging it into a microcontroller board (for example, the SDP-K1 or the AD-APARD32690-SL). The pins on the backside of the EVAL-ADBMS6822 connect directly with the sockets of the MCU board. The shield connections provide all the default data and power connections.
   | Note that the microcontroller board's interface voltage must be set to 3.3 V through Pin P4.
   
   | 
   | ==== isoSPI Connections ==== J1 is the main isoSPI port. The applications that only use one port use this connection to make daisy-chain connections to peripheral isoSPI devices. J2 is an auxiliary port that is used as a redundant controller in a reversible isoSPI daisy-chain network, and as another indpendent isoSPI interface.
   
   | 
   | ==== Optional Connections ====
   
   SPI AUX Optional Header (J7)
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   This double row of through-holes (hole field) can be used to connect a fully independent AUX SPI channel. A connector or discrete wires can be soldered to this array.
   
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP1 to JP4** | These are set as a group to either configure the AUX SPI traffic as being common (COM) with the MAIN SPI, or the POCI, PICO, SCK from the SDP-K1 controller, along with dedicated CSB lines to provide multiplexing. The separate setting (SEP) connects the AUX SPI signals to J7 exclusively. |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP5**        | Sets the SPI mode for both channels of the ADBMS6822. Mode 0 is used in most applications.                                                                                                                                                                                                      |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP6**        | Two settings are provided for setting the low power cell monitoring (LPCM) response interval of the AUX channel: either 1.5 seconds or 48 seconds. Other intervals can be achieved with resistor value changes to the board.                                                                    |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP7, JP11**  | Configures the operating modes of the AUX and MAIN channels, respectively. Positions of the jumper correspond to the following options:                                                                                                                                                         |
   |                | **2 MB**: 2 MB peripheral with 1-bit latency                                                                                                                                                                                                                                                    |
   |                | **STD**: Standard bidirectional isoSPI                                                                                                                                                                                                                                                          |
   |                | **LPC**: Standard bidirectional isoSPI with LPCM timeout monitor support                                                                                                                                                                                                                        |
   |                | **4 MB**: 4 Mbps unidirectional                                                                                                                                                                                                                                                                 |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP8**        | Two options are provided for setting the LPCM response interval of the MAIN channel: either 1.5 seconds or 48 seconds. Other intervals can be achieved with resistor value changes to the board.                                                                                                |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP9**        | Configures the VDDS supply pins to either the VDD potential or an externally furnished voltage at turret VDDS EXT.                                                                                                                                                                              |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **JP10**       | Configures the V+ supply pins to either the VDD potential or an externally furnished voltage at turret V+ EXT.                                                                                                                                                                                  |
   +----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   | 
   |

   .. container:: center

         
         ================================================= ===========
         **Pin Designations for the J7 SPI AUX Connector** 
         **Number**                                        \*\* Pin*\*
         1                                                 POCI2
         2                                                 VDDS
         3                                                 SCLK2
         4                                                 PICO2
         5                                                 CSB2
         6                                                 GND
         ================================================= ===========
         

   


| 
| ----

Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


| 

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adbms6822_block_diagram.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adbms6822_system_setup.png
   :width: 600px
