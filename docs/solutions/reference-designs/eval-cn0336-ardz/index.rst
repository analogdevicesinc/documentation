.. _eval-cn0336-ardz:

EVAL-CN0336-ARDZ
=================

Isolated 4 mA-to-20 mA Current to Digital Conversion System.

Overview
--------

:adi:`CN0336` provides a robust and complete solution for 4 mA-to-20 mA
current to digital conversion with isolation, for a wide variety of
measurements where sensors with standard 4-20 mA output are used. The design
solution is optimized for high precision and low cost measurement, using only
three active devices, and has a total unadjusted error of less than 0.1% of
full scale range.

The circuit incorporates the :adi:`AD8606` rail-to-rail op-amp,
:adi:`AD7091R` 12-bit successive approximation (SAR) ADC, and
:adi:`ADuM5401` quad-channel digital isolator to create a standard
4 mA-to-20 mA current measurement system. The circuit has a 12-pin PMOD
connector on board, which can be used for connection to a microprocessor or
FPGA.

.. figure:: cn0336_hw_375.jpg
   :align: center
   :width: 400

   EVAL-CN0336-PMDZ Evaluation Board

.. figure:: cn0336-hw-1024.jpg
   :align: center

   EVAL-CN0336-PMDZ Board Detail

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` Controller Board (SDP-B Board)
- :adi:`EVAL-CN0336-PMDZ <CN0336>` Evaluation Board
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V Power Supply or equivalent
- :adi:`SDP-PMD-IB1Z` SDP-to-PMOD Interposer Board
- Current calibrator
- Multimeter (to measure the input current)
- `CN0336 Evaluation Software
  <https://www.analog.com/CN0336>`__
- PC with USB type A port (Windows XP SP2 or later)
- USB type A to USB type mini-B cable

General Setup
-------------

- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) powers the
  EVAL-CN0336-PMDZ (CN0336 Board) via the DC barrel jack.
- The :adi:`SDP-PMD-IB1Z` (Interposer Board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B Board) via the 120-pin connector A.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB cable.
- The EVAL-CN0336-PMDZ connects to the Interposer Board via the 12-pin header
  PMOD connector (J1 and J3).
- The 4-20 mA current source (current calibrator) connects to the
  EVAL-CN0336-PMDZ via the terminal block J2.

Hardware Configuration
----------------------

Input Interface
~~~~~~~~~~~~~~~

The circuit consists of an input current-to-voltage converter, a level
shifting circuit, an ADC stage, and an output isolation stage. The system
processes 4 to 20 mA input signals by connecting the positive terminal to
Pin 1 and the ground terminal to Pin 2 of the J2 terminal block. A diode is
connected to provide protection against accidental reverse connection.

Power Supply
~~~~~~~~~~~~

The 3.3 V power for the PMOD board comes directly from the host board it is
connected to. The host is generally capable of providing up to 100 mA at
3.3 V.

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0336-PMDZ uses the extended SPI PMOD interface:

.. list-table::
   :header-rows: 1

   * - Pin
     - Function
     - Mnemonic
   * - J1.1
     - Chip Select
     - CS
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
   * - J1.9
     - Convert Start
     - CONVST
   * - J1.11
     - Digital Ground
     - DGND
   * - J1.12
     - Digital Power
     - VDD

Using the Evaluation Software
------------------------------

Software Controls
~~~~~~~~~~~~~~~~~

The CN0336 evaluation software provides the following controls and indicators:

- **Connect/Reconnect Button** -- establishes a USB connection between the
  SDP-B Board and the CN0336 Board.
- **Run Button** -- starts data collection, presenting acquisitions in the
  chart.
- **Stop Button** -- stops data collection.
- **Save Data Button** -- saves captured data to a tab-delimited ASCII
  spreadsheet file.
- **Clear Data Button** -- clears all collected data from the chart history.
- **Numerical Indicator** -- displays the current reading value.
- **Graph Units Radio Buttons** -- selects between mA, mV, and ADC Codes.
- **Calibrate System Controls** -- allows two-point calibration with current
  inputs in the 4-20 mA range.

Calibrating the Board
~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Click the **Calibrate System** tab.
#. Apply the first calibration current to J2 and enter its value in
   **Calibration Current 1**.
#. Press the **Calibrate 1** button.
#. Apply a second (different) calibration current to J2 and enter its value
   in **Calibration Current 2**.
#. Press the **Calibrate 2** button.

For best performance, use 4 mA and 20 mA as the two calibration points.

Capturing Data
~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Click the **Run** button to begin acquisition.
#. Click the **Stop** button when acquisition is complete.

Saving Data
~~~~~~~~~~~

#. Capture data as described above.
#. Click the **Save Data** button.
#. Choose a file location and name, then click **OK**.

The software saves the spreadsheet file as ASCII text with tab-separated
columns.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0336 Design & Integration Files <https://www.analog.com/CN0336>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD8606 Product Page <AD8606>`
- :adi:`AD7091R Product Page <AD7091R>`
- :adi:`ADuM5401 Product Page <ADUM5401>`
- :adi:`CN0336 Circuit Note <CN0336>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
