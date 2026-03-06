AD-FMCMOTCON1-EBZ Controller Board
==================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Features and Block Diagram
--------------------------

-  Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors
-  2 x Gbit Ethernet PHYs for high speed industrial communication
-  Hall + Differential Hall + Encoder + Resolver interfaces
-  Current and voltage measurement using isolated ADCs
-  Xilinx XADC interface
-  Fully isolated control and feedback signals

============================ ==========================
**Simplified Block Diagram** **Detailed Block Diagram**
============================ ==========================
============================ ==========================

|Simplified Block Diagram| |Detailed Block Diagram|

+---+
+---+

Picture and Main Components
---------------------------

|AD-FMC-MOTCON1-EBZ Top| |AD-FMC-MOTCON1-EBZ Bottom|

+---+
+---+

Key Parts
---------

+--------------------------------------------------+-------------------------------------------------------------------------------+
| Measurement                                      |                                                                               |
+==================================================+===============================================================================+
| :adi:`AD7401A`                                   | 5 kV rms, isolated 2nd order Sigma-Delta modulator                            |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADA4084-2`                                 | 30 V, Low noise, rail-to-rail I/O, low power operational amplifier            |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`AD8646`                                    | 24 MHz rail-to-rail dual op amp                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`AD2S1210`                                  | Variable resolution, 10-bit to 16-bit R/D converter with reference oscillator |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| Power                                            |                                                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADuM5000`                                  | isoPower® integrated isolated dc-to-dc converter                              |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADP1614`                                   | 1000 mA, 2.5 MHz buck-boost dc-to-dc converter                                |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADM660`                                    | CMOS switched-capacitor voltage converter                                     |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| Isolation                                        |                                                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADuM7640`                                  | Triple channel digital isolator                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| Voltage Translation                              |                                                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADG3308`                                   | 8-channel bidirectional level translator                                      |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| Multiplexers                                     |                                                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADG704`                                    | CMOS, low voltage 2.5 Ω 4-channel multiplexer                                 |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| :adi:`ADG759`                                    | CMOS low voltage, 3 ohms 4-channel multiplexer                                |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| High Speed Communication                         |                                                                               |
+--------------------------------------------------+-------------------------------------------------------------------------------+
| **88E1512**                                      | Marvell Integrated 10/100/1000 Mbps Energy Efficient Ethernet Transceiver     |
+--------------------------------------------------+-------------------------------------------------------------------------------+

+---+
+---+

Jumper settings
---------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_jumpers.jpg
   :alt: AD-FMC-MOTCON1-EBZ Jumpers
   :width: 600px

+----------------------------------------+------------------------+-------------------+
| Sensor Selection                       |                        |                   |
+========================================+========================+===================+
| **Back EMF**                           | P9 - position 0        | P20 - position 0  |
+----------------------------------------+------------------------+-------------------+
| **Single ended Hall**                  | P9 - position 1        | P20 - position 0  |
+----------------------------------------+------------------------+-------------------+
| **Differential Hall**                  | P9 - position 0        | P20 - position 1  |
+----------------------------------------+------------------------+-------------------+
| **Reserved**                           | P9 - position 1        | P20 - position 1  |
+----------------------------------------+------------------------+-------------------+
| Resolver Configuration Mode            |                        |                   |
+----------------------------------------+------------------------+-------------------+
| **Normal Mode - Position input**       | P3 - Not inserted      | P5 - Not inserted |
+----------------------------------------+------------------------+-------------------+
| **Normal Mode - Velocity input**       | P3 - Not inserted      | P5 - Inserted     |
+----------------------------------------+------------------------+-------------------+
| **Reserved**                           | P3 - Inserted          | P5 - Not inserted |
+----------------------------------------+------------------------+-------------------+
| **Configuration Mode**                 | P3 - Inserted          | P5 - Inserted     |
+----------------------------------------+------------------------+-------------------+
| Resolver Resolution Settings           |                        |                   |
+----------------------------------------+------------------------+-------------------+
| **10 Bits**                            | P4 - Not inserted      | P6 - Not inserted |
+----------------------------------------+------------------------+-------------------+
| **12 Bits**                            | P4 - Not inserted      | P6 - Inserted     |
+----------------------------------------+------------------------+-------------------+
| **14 Bits**                            | P4 - Inserted          | P6 - Not inserted |
+----------------------------------------+------------------------+-------------------+
| **16 Bits**                            | P4 - Inserted          | P6 - Inserted     |
+----------------------------------------+------------------------+-------------------+
| PHYs Configuration                     |                        |                   |
+----------------------------------------+------------------------+-------------------+
| **2.5V VDDO, different PHY addresses** | P11 & P12 - Position 0 | P9 - Inserted     |
+----------------------------------------+------------------------+-------------------+

+---+
+---+

LEDs
----

=== ===================
LED Description
=== ===================
DS1 FMC 3.3V Power Good
DS2 Vadj Power Good
DS3 5V Power Good
DS7 12V Power Good
=== ===================

+---+
+---+

Power Map
---------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_power_map.png
   :width: 400px

+---+
+---+

ADC FPGA Interface
------------------

|image1| The AD7401 Isolated Sigma-Delta Modulators present on the controller board have a 2 wires signal interface with the FPGA:

-  10 / 20 MHz clock input
-  1 bit digital data stream output

The reconstruction of the data provided by the AD7401 modulator can be done using a SINC3 filter. A filter model and HDL implementation are provided in the AD7401 datasheet. Typical filter output characteristics:

-  Output code: 16 bit
-  Sampling rate: 78kHz

The output code resolution and sampling rate can be controlled by changing the filter’s model and decimation. Polyphase interpolation filters are utilized to increase the sampling rate of the system.

+---+
+---+

Position & Speed Sensors FPGA Interface
---------------------------------------

**Single digital interface for multiple position sensors**

-  Single Ended HALL
-  Differential HALL
-  BEMF
-  Encoder

**3 digital signals between HW and the FPGA**

-  HALL A / BEMF A / Encoder Channel A
-  HALL B / BEMF B / Encoder Channel B
-  HALL C / BEMF C / Encoder Index

Sensor selection is done with jumpers on the controller board. The hardware conditions the analog signals and sends clean digital signals to the FPGA.

+---+
+---+

Downloads
---------

.. admonition:: Download
   :class: download

   **AD-FMCMOTCON1-EBZ**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_schematics.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_bom.pdf>`__
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_layout.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.5 or higher).
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#../
   :alt: Overview#lv_board|Low Voltage Drive Board

.. |Simplified Block Diagram| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_block_diagram_simplified.png
   :width: 350px
.. |Detailed Block Diagram| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_block_diagram.png
   :width: 500px
.. |AD-FMC-MOTCON1-EBZ Top| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-fmcmotcon1-ebz_top_parts.jpg
   :width: 600px
.. |AD-FMC-MOTCON1-EBZ Bottom| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-fmcmotcon1-ebz_bottom_parts.jpg
   :width: 600px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad7401_logo.png
   :width: 100px
