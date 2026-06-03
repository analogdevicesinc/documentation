.. _pulsar-adc pmods:

PulSAR ADC PMOD Boards
===============================================================================

Overview
-------------------------------------------------------------------------------

The PulSAR ADC PMOD boards are evaluation modules featuring low-power ADCs
offering 14 to 18-bit resolution with throughputs ranging from 100 kSPS to
1.33 MSPS. These boards are designed to demonstrate the ADC's performance and
to provide an easy to understand digital interface for a variety of system
applications. A full description of each product is available in their
respective data sheets and should be consulted when utilizing the evaluation
boards.

.. figure:: images/pulsar_pmod.jpg
   :align: center
   :width: 400

   PulSAR ADC PMOD evaluation board

.. list-table::
   :header-rows: 1
   :widths: 14 10 12 20 14 30

   * - Evaluation Board
     - Part
     - Resolution
     - Throughput (kSPS)
     - Input Type
     - Driver
   * - :adi:`EVAL-AD7942-PMDZ`
     - :adi:`AD7942`
     - 14-bit
     - 250
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7946-PMDZ`
     - :adi:`AD7946`
     - 14-bit
     - 500
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7988-1-PMDZ`
     - :adi:`AD7988-1`
     - 16-bit
     - 100
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7685-PMDZ`
     - :adi:`AD7685`
     - 16-bit
     - 250
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7687-PMDZ`
     - :adi:`AD7687`
     - 16-bit
     - 250
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7686-PMDZ`
     - :adi:`AD7686`
     - 16-bit
     - 500
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7688-PMDZ`
     - :adi:`AD7688`
     - 16-bit
     - 500
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7693-PMDZ`
     - :adi:`AD7693`
     - 16-bit
     - 500
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7988-5-PMDZ`
     - :adi:`AD7988-5`
     - 16-bit
     - 500
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7980-PMDZ`
     - :adi:`AD7980`
     - 16-bit
     - 1000
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7983-PMDZ`
     - :adi:`AD7983`
     - 16-bit
     - 1333
     - Unipolar, Single-Ended
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7690-PMDZ`
     - :adi:`AD7690`
     - 18-bit
     - 400
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7691-PMDZ`
     - :adi:`AD7691`
     - 18-bit
     - 250
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7982-PMDZ`
     - :adi:`AD7982`
     - 18-bit
     - 1000
     - Unipolar, Differential
     - :adi:`ADA4841-1`
   * - :adi:`EVAL-AD7984-PMDZ`
     - :adi:`AD7984`
     - 18-bit
     - 1333
     - Unipolar, Differential
     - :adi:`ADA4841-1`

.. note::

   The throughput of the PulSAR ADC will be limited to the SPI bus speed of
   the host platform (maximum 30 MHz on the SDP platform).

Hardware Setup
-------------------------------------------------------------------------------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PulSAR ADC PMOD boards are approximately 1 inch wide by 3 inches long.
While standard PMOD connectors typically supply up to 100 mA at 3.3V, the
successive approximation ADC architecture requires low-noise external power
supplies to achieve data sheet performance. The precision amplifiers require
supplies above and below the ADC input range to provide zero and full-scale
inputs.

External power supply connections (via terminal block):

- **-2.5V** — Amplifier negative rail
- **GND** — Ground reference
- **+7.5V** — Amplifier positive rail and on-board regulators

.. figure:: images/pmod_power_supplies.png
   :align: center
   :width: 400

   PMOD board power supply connections

.. warning::

   Connect external power supplies with the supplies turned **OFF**. Turn on
   the power supplies only after all connections are made.

Input Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two SMB connectors per board accommodate positive (Vin+) and negative (Vin-)
input signals. Using SMB connectors minimizes input noise at the input stage
and fully utilizes the converter's resolution and speed capabilities.

Each converter supports single-ended, differential, or pseudo-differential
inputs depending on the specific model. Consult the device data sheet for the
correct input configuration.

.. figure:: images/vin.png
   :align: center
   :width: 400

   PMOD board analog input connectors

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital interface uses the extended SPI protocol per the Digilent
specification. The boards operate in 3-wire mode without busy indication,
using three signals:

- **CNV** — Conversion trigger (similar to chip select)
- **SCLK** — Serial clock
- **MISO** — Serial data output (ADC data)

Since PulSAR ADCs contain no internal registers, no MOSI (input) line is
required. Data streams directly via the CNVST pin upon completion of each
conversion.

.. figure:: images/pmod_pinout.png
   :align: center
   :width: 400

   PMOD connector pinout

SDP Evaluation Setup
-------------------------------------------------------------------------------

Equipment Required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- PulSAR ADC PMOD board (EVAL-AD7xxx-PMDZ)
- :adi:`EVAL-SDP-CB1Z` evaluation board
- SDP-PMD-IB1Z PMOD interposer board
- EVAL-CFTL-6V-PWRZ power supply
- PC with Windows (.NET 3.5 or higher)
- Mini USB cable
- Low distortion signal source and appropriate cabling
- Bench-top power supply (-2.5V, GND, +7.5V)

Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the Mini USB cable from the PC to J1 of the :adi:`EVAL-SDP-CB1Z`.
   Verify that **ADI Development Tools** appears in Device Manager.

   .. figure:: images/sdp_usb.jpg
      :align: center
      :width: 400

      Mini USB connection to EVAL-SDP-CB1Z

   .. figure:: images/device_manager.png
      :align: center
      :width: 300

      ADI Development Tools in Device Manager

#. Remove the shunt at JP1 of the SDP-PMD-IB1Z interposer.

#. Connect the :adi:`EVAL-SDP-CB1Z` CON A to the SDP-PMD-IB1Z J4.

   .. figure:: images/sdp_usb_interposer.jpg
      :align: center
      :width: 400

      EVAL-SDP-CB1Z connected to SDP-PMD-IB1Z interposer

#. Connect the EVAL-CFTL-6V-PWRZ to the SDP-PMD-IB1Z J1 barrel jack. Wait
   10 seconds for power stabilization.

   .. figure:: images/sdp_usb_interposer_power.jpg
      :align: center
      :width: 400

      Power supply connected to SDP-PMD-IB1Z interposer

#. Insert the PulSAR ADC PMOD board into the SDP-PMD-IB1Z J3.

   .. figure:: images/sdp_evaluation_combo.jpg
      :align: center
      :width: 400

      Complete SDP evaluation setup

#. With external power supplies **OFF**, connect -2.5V, GND, and +7.5V to
   the terminal block on the EVAL-AD7xxx-PMDZ board.

#. Turn **ON** the external power supplies.

#. Place the shunt across JP1 of the SDP-PMD-IB1Z to enable 3.3V to the
   PMOD connector (see silkscreen for orientation).

   .. figure:: images/sdp_usb_interposer_power_jumper.jpg
      :align: center
      :width: 400

      JP1 shunt placement on SDP-PMD-IB1Z

#. Verify that **ADI Development Tools** is still visible in Device Manager.

#. Connect SMB cables from the signal source to the Vin+ and Vin- connectors
   of the EVAL-AD7xxx-PMDZ board.

Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A LabVIEW-based evaluation application provides the following controls:

.. figure:: images/software_panel_numbered.png
   :align: center
   :width: 500

   Evaluation software control panel

**Control Panel:**

#. **Select Supply Voltage** — Choose 5.0V or 2.5V corresponding to the
   ADC VDD supply.
#. **Select ADC** — Select the part number. Choices are filtered by voltage
   selection; parts incompatible with the selected voltage are grayed out.
#. **Sampling Frequency** — Enter the desired frequency in Hz (for example,
   250000 for 250 kHz). Do not exceed the converter's maximum sample rate.
#. **Number of Samples** — Select the number of samples for waveform,
   histogram, and FFT calculations.
#. **Acquire Data** — Click to gather data and calculate results.

**Data Display Tabs:**

- **Waveform** — Time-domain representation of captured data
- **Histogram** — Bin-based data distribution for noise analysis
- **FFT** — Frequency-domain analysis with SINAD, THD, and SNR calculations

.. figure:: images/software_fft_10khz.png
   :align: center
   :width: 500

   FFT analysis example using AD7980 with 10 kHz input sine wave

FPGA Carrier Setup
-------------------------------------------------------------------------------

The PulSAR ADC PMOD boards are also supported on FPGA carrier boards for use
with HDL reference designs and Linux/no-OS drivers. For FPGA-based evaluation,
see the :ref:`PulSAR ADC quick start guides <pulsar-adc quickstart>`.

Design & Integration Files
-------------------------------------------------------------------------------

Complete design support packages including schematics, PCB layout, bill of
materials, and Allegro project files are available for download from the
respective evaluation board product pages on analog.com:

- :adi:`EVAL-AD7685-PMDZ Product Page <EVAL-AD7685-PMDZ>`
- :adi:`EVAL-AD7686-PMDZ Product Page <EVAL-AD7686-PMDZ>`
- :adi:`EVAL-AD7687-PMDZ Product Page <EVAL-AD7687-PMDZ>`
- :adi:`EVAL-AD7688-PMDZ Product Page <EVAL-AD7688-PMDZ>`
- :adi:`EVAL-AD7690-PMDZ Product Page <EVAL-AD7690-PMDZ>`
- :adi:`EVAL-AD7691-PMDZ Product Page <EVAL-AD7691-PMDZ>`
- :adi:`EVAL-AD7693-PMDZ Product Page <EVAL-AD7693-PMDZ>`
- :adi:`EVAL-AD7942-PMDZ Product Page <EVAL-AD7942-PMDZ>`
- :adi:`EVAL-AD7946-PMDZ Product Page <EVAL-AD7946-PMDZ>`
- :adi:`EVAL-AD7980-PMDZ Product Page <EVAL-AD7980-PMDZ>`
- :adi:`EVAL-AD7982-PMDZ Product Page <EVAL-AD7982-PMDZ>`
- :adi:`EVAL-AD7983-PMDZ Product Page <EVAL-AD7983-PMDZ>`
- :adi:`EVAL-AD7984-PMDZ Product Page <EVAL-AD7984-PMDZ>`
- :adi:`EVAL-AD7988-1-PMDZ Product Page <EVAL-AD7988-1-PMDZ>`
- :adi:`EVAL-AD7988-5-PMDZ Product Page <EVAL-AD7988-5-PMDZ>`

Revision History
-------------------------------------------------------------------------------

Changes from Rev 0 to Rev A:

- Migrated from PADS to Allegro CAD tools (reference designators changed)
- Replaced capacitors C9 and C10 with resistors R5 and R7
- Added R16 and R17 for extended ADC operating modes (daisy-chain capability)
- Removed U5 (:adi:`ADG1401`) multiplexer; connected 5V reference directly to
  ADC
- Removed U8 (ADP7104-3.3) regulator; connected VIO pin to VCC
- Separated analog (AGND) and digital (DGND) ground planes
