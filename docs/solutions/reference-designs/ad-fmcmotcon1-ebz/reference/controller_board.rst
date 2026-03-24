.. _ad_fmcmotcon1_ebz controller-board:

AD-FMCMOTCON1-EBZ Controller Board
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

Features and Block Diagram
-------------------------------------------------------------------------------

-  Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors
-  2x Gbit Ethernet PHYs for high-speed industrial communication
-  Hall, Differential Hall, Encoder, and Resolver interfaces
-  Current and voltage measurement using isolated ADCs
-  Xilinx XADC interface
-  Fully isolated control and feedback signals

.. figure:: ../images/controller_block_diagram_simplified.jpg
   :alt: AD-FMCMOTCON1-EBZ simplified block diagram
   :align: center
   :width: 350

   Simplified block diagram

.. figure:: ../images/controller_block_diagram.jpg
   :alt: AD-FMCMOTCON1-EBZ detailed block diagram
   :align: center
   :width: 500

   Detailed block diagram

Picture and Main Components
-------------------------------------------------------------------------------

.. figure:: ../images/ad-fmcmotcon1-ebz_top_parts.jpg
   :alt: AD-FMCMOTCON1-EBZ top view with main components labeled
   :align: center
   :width: 600

   AD-FMCMOTCON1-EBZ top view

.. figure:: ../images/ad-fmcmotcon1-ebz_bottom_parts.jpg
   :alt: AD-FMCMOTCON1-EBZ bottom view with main components labeled
   :align: center
   :width: 600

   AD-FMCMOTCON1-EBZ bottom view

Key Parts
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Part
     - Description
   * - **Measurement**
     -
   * - :adi:`AD7401A`
     - 5 kV rms, isolated 2nd order Sigma-Delta modulator
   * - :adi:`ADA4084-2`
     - 30 V, low noise, rail-to-rail I/O, low power operational amplifier
   * - :adi:`AD8646`
     - 24 MHz rail-to-rail dual op amp
   * - :adi:`AD2S1210`
     - Variable resolution, 10-bit to 16-bit R/D converter with reference
       oscillator
   * - **Power**
     -
   * - :adi:`ADuM5000`
     - isoPower® integrated isolated dc-to-dc converter
   * - :adi:`ADP1614`
     - 1000 mA, 2.5 MHz buck-boost dc-to-dc converter
   * - :adi:`ADM660`
     - CMOS switched-capacitor voltage converter
   * - **Isolation**
     -
   * - :adi:`ADuM7640`
     - Triple channel digital isolator
   * - **Voltage Translation**
     -
   * - :adi:`ADG3308`
     - 8-channel bidirectional level translator
   * - **Multiplexers**
     -
   * - :adi:`ADG704`
     - CMOS, low voltage 2.5 Ω 4-channel multiplexer
   * - :adi:`ADG759`
     - CMOS low voltage, 3 Ω 4-channel multiplexer
   * - **High Speed Communication**
     -
   * - 88E1512
     - Marvell integrated 10/100/1000 Mbps energy efficient Ethernet
       transceiver

Jumper Settings
-------------------------------------------------------------------------------

.. figure:: ../images/controller_jumpers.jpg
   :alt: AD-FMCMOTCON1-EBZ jumper locations
   :align: center
   :width: 600

   AD-FMCMOTCON1-EBZ jumper locations

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Setting
     - Jumper / Position 1
     - Jumper / Position 2
   * - **Sensor Selection**
     -
     -
   * - Back EMF
     - P9 - position 0
     - P20 - position 0
   * - Single ended Hall
     - P9 - position 1
     - P20 - position 0
   * - Differential Hall
     - P9 - position 0
     - P20 - position 1
   * - Reserved
     - P9 - position 1
     - P20 - position 1
   * - **Resolver Configuration Mode**
     -
     -
   * - Normal Mode - Position input
     - P3 - Not inserted
     - P5 - Not inserted
   * - Normal Mode - Velocity input
     - P3 - Not inserted
     - P5 - Inserted
   * - Reserved
     - P3 - Inserted
     - P5 - Not inserted
   * - Configuration Mode
     - P3 - Inserted
     - P5 - Inserted
   * - **Resolver Resolution Settings**
     -
     -
   * - 10 Bits
     - P4 - Not inserted
     - P6 - Not inserted
   * - 12 Bits
     - P4 - Not inserted
     - P6 - Inserted
   * - 14 Bits
     - P4 - Inserted
     - P6 - Not inserted
   * - 16 Bits
     - P4 - Inserted
     - P6 - Inserted
   * - **PHYs Configuration**
     -
     -
   * - 2.5V VDDO, different PHY addresses
     - P11 & P12 - Position 0
     - P9 - Inserted

LEDs
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - LED
     - Description
   * - DS1
     - FMC 3.3V Power Good
   * - DS2
     - Vadj Power Good
   * - DS3
     - 5V Power Good
   * - DS7
     - 12V Power Good

Power Map
-------------------------------------------------------------------------------

.. figure:: ../images/controller_power_map.jpg
   :alt: AD-FMCMOTCON1-EBZ power map
   :align: center
   :width: 400

   AD-FMCMOTCON1-EBZ power map

ADC FPGA Interface
-------------------------------------------------------------------------------

The :adi:`AD7401` isolated Sigma-Delta modulators present on the controller
board have a 2-wire signal interface with the FPGA:

-  10 / 20 MHz clock input
-  1-bit digital data stream output

The reconstruction of the data provided by the AD7401 modulator can be done
using a SINC3 filter. A filter model and HDL implementation are provided in
the AD7401 datasheet. Typical filter output characteristics:

-  Output code: 16-bit
-  Sampling rate: 78 kHz

The output code resolution and sampling rate can be controlled by changing the
filter's model and decimation. Polyphase interpolation filters are utilized to
increase the sampling rate of the system.

Position & Speed Sensors FPGA Interface
-------------------------------------------------------------------------------

**Single digital interface for multiple position sensors**

-  Single Ended HALL
-  Differential HALL
-  BEMF
-  Encoder

**3 digital signals between hardware and the FPGA**

-  HALL A / BEMF A / Encoder Channel A
-  HALL B / BEMF B / Encoder Channel B
-  HALL C / BEMF C / Encoder Index

Sensor selection is done with jumpers on the controller board. The hardware
conditions the analog signals and sends clean digital signals to the FPGA.
