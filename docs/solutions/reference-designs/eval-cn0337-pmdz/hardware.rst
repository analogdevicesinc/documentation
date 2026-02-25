.. _eval-cn0337-pmdz-hardware:

Hardware Guide
==============

The EVAL-CN0337-PMDZ PMOD board connects to the :adi:`EVAL-ADICUP360
<ADICUP360>` base board via the PMOD SPI port (P4).

Hardware Setup
--------------

The figure below shows how to properly connect EVAL-CN0337-PMDZ to the
EVAL-ADICUP360.

.. figure:: cn0337_hw_setup.png
   :align: center
   :width: 500

   EVAL-CN0337-PMDZ connected to EVAL-ADICUP360

Sensor Interface
----------------

CN0337 processes the output of a Pt100 RTD and includes an innovative circuit
for lead-wire compensation using a standard 3-wire connection. For other
temperature sensors such as Pt200, Pt500, Pt1000, or Pt2000, the calculation of
gain, output offset, and resistor values is described in the
:adi:`CN0337 Circuit Note <CN0337>`.

Pin 1 and Pin 2 of J2 terminal block must be connected to similar RTD
terminals. The label on the board can also be used as a guide.

.. figure:: cn0337_hw_sensor.jpg
   :align: center
   :width: 500

   RTD sensor connection on the EVAL-CN0337-PMDZ

Power Supply Requirements
--------------------------

When using the EVAL-CN0337-PMDZ PMOD board, the 3.3 V power for the PMOD comes
directly from the host board. The power from the host is generally capable of
providing up to 100 mA at 3.3 V. For complete PMOD power specifications, refer
to the `Digilent Pmod Interface Specification
<https://digilent.com/reference/pmod/start>`__.

The fastest way to confirm that the EVAL-CN0337-PMDZ board is powered is by
checking if diode D1 is illuminated.

.. figure:: cn0337_hw_power.jpg
   :align: center
   :width: 500

   Power indicator LED on the EVAL-CN0337-PMDZ

Digital Interface (PMOD)
------------------------

The PMOD interface is a series of standardized digital interfaces for various
digital communication protocols such as SPI, I2C, and UART. These interface
types were standardized by Digilent (now a division of National Instruments).

The specific interface used for the EVAL-CN0337-PMDZ board is the extended SPI.
ADI has adopted the extended SPI connector for all PMOD devices with an SPI
interface. It provides flexibility to add interrupts, general purpose I/O,
resets, and other digitally controlled functions.

.. list-table::
   :header-rows: 1
   :widths: 15 35 20

   * - Pin Number
     - Pin Function
     - Mnemonic
   * - J1.1
     - Chip Select
     - CS
   * - J1.2
     - No Connect
     - NC
   * - J1.3
     - Master In Slave Out
     - MISO
   * - J1.4
     - Serial Clock
     - SCLK
   * - J1.5
     - Digital Ground
     - DGND
   * - J1.6
     - Digital Power
     - VDD
   * - J1.7
     - No Connect
     - NC
   * - J1.8
     - Not Connected
     - NC
   * - J1.9
     - Convert Start
     - CONVST
   * - J1.10
     - No Connect
     - NC
   * - J1.11
     - Digital Ground
     - DGND
   * - J1.12
     - Digital Power
     - VDD
