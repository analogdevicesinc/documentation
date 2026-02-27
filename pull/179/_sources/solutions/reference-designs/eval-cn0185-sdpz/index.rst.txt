.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0185

.. _eval-cn0185-sdpz:

EVAL-CN0185-SDPZ
=================

Analog-to-Analog Isolator with 2500 V RMS Isolation.

Overview
--------

:adi:`CN0185` is a complete low-cost implementation of an analog-to-analog
isolator. The circuit provides isolation of 2500 V rms (1 minute per UL 1577).

The circuit is based on the :adi:`AD7400A`, a second-order sigma-delta
modulator with a digitally isolated 1-bit data stream output. The isolated
analog signal is recovered with a fourth-order active filter based on the dual,
low-noise, rail-to-rail :adi:`AD8646` op amp. With the :adi:`ADuM5000` as the
power supply for the isolated side, the two sides are completely isolated and
use only one power supply for the system. The circuit has 0.05% linearity and
benefits from the noise shaping provided by the modulator of the
:adi:`AD7400A` and the analog filter.

Applications include motor control and shunt current monitoring, and the
circuit is a good alternative to isolation systems based on optoisolators.

.. figure:: cn0185-hw-1024.jpg
   :align: center

   EVAL-CN0185-EB1Z evaluation board

Required Equipment
------------------

Equivalents can be substituted for the following:

- EVAL-CN0185-EB1Z evaluation board
- Multifunction calibrator (DC source), e.g., Fluke 5700A
- Digital multimeter, e.g., Agilent 3458A (8.5 digits)
- Spectrum analyzer, e.g., Agilent 4396B
- Function generator, e.g., Agilent 33250A
- Oscilloscope
- +6 V power supply

General Setup
-------------

- Connect the +6 V power supply to the CN0185 power terminal **J4**
- Connect DC source or function generator to **VIN+** and **VIN-**
- Connect digital multimeter, spectrum analyzer, or oscilloscope to the
  output terminal

Test Setup Functional Block Diagram
------------------------------------

DC Input Voltage Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: dc.png
   :align: center

   Test setup block diagram for DC input voltage measurements

Frequency Response Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: freqres.png
   :align: center

   Test setup block diagram for frequency response measurements

.. note::

   Signal generator settings for frequency response measurements:

   - Output Waveform: Sinewave
   - Amplitude: +/-20 mV (40 mV p-p)
   - DC Offset: 0

Connectors and Jumper Configurations
-------------------------------------

.. figure:: cn0185connectors.png
   :align: center

   EVAL-CN0185-EB1Z connector and jumper locations

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Ref
     - Description
   * - 1
     - Connect the +6 V power supply to this screw terminal (**J4**)
   * - 2
     - Connect the GND terminal of the +6 V power supply to this screw
       terminal (**J4**)
   * - 3
     - Connect the positive analog input signal to this SMB connector
       (**J1**)
   * - 4
     - Connect the negative analog input signal to this SMB connector
       (**J2**)
   * - 5
     - **LK2** jumper: Pins 1--2 connect the positive analog input signal to
       the AD7400A; Pins 2--3 ground the input
   * - 6
     - **LK1** jumper: Pins 1--2 connect the negative analog input signal to
       the AD7400A; Pins 2--3 ground the input
   * - 7
     - Connect the digital multimeter (for DC) or spectrum analyzer /
       oscilloscope (for frequency response) to this SMB connector (**J3**)

.. note::

   The output is available through the **J3** SMB connector or test point
   **OUT**.

Documents
---------

- :adi:`CN0185 Circuit Note <CN0185>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0185-EB1Z Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0185-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`AD7400A Product Page <AD7400A>`
- :adi:`AD8646 Product Page <AD8646>`
- :adi:`ADuM5000 Product Page <ADUM5000>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
