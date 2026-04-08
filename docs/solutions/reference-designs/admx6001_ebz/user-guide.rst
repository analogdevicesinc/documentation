.. _admx6001 user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADMX6001-EBZ` connects to the :xilinx:`VCU118` FPGA carrier via the
**FMC+ HSPC** connector. The board provides two digitization paths:

- **High-speed path**: :adi:`AD9213` 12-bit ADC at 10 GSPS, driven by the
  :adi:`ADL5580` differential amplifier
- **Precision path**: :adi:`AD4080` 20-bit SAR ADC (40 MSPS max,
  31.25 MSPS operational) reducing 1/f noise for low-frequency signals

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADMX6001-EBZ requires an external power supply — it is **not** powered
through the FMC+ connector. Two independent 12 V / 65 W supplies are required:
one for the ADMX6001-EBZ and one for the :xilinx:`VCU118`.

.. warning::

   Always power up the ADMX6001-EBZ **before** the VCU118. Power down in
   reverse order. Incorrect power sequencing may damage the boards.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect a benchtop function generator to the analog input of the
ADMX6001-EBZ:

- The **high-speed path** (AD9213) accepts signals up to 5 GHz. Use a
  low-noise, low-jitter source with appropriate band-pass filtering.
- The **precision path** (AD4080) accepts lower-frequency differential
  signals. The :adi:`ADL5580` driver conditions the input for the AD9213.

DC offset adjustment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LTC2664` quad DAC provides a programmable DC offset on the AD9213
input, allowing the operating point to be shifted for maximum dynamic range
utilization. The DAC output value is calculated as:

.. math::

   \text{DAC value} = 32768 \times \left(1 + \frac{x}{5000}\right)

where *x* is the desired DC offset in millivolts. The default value of 32768
corresponds to 0 V. The output range spans −5 V to +5 V.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design and integration files (schematic, PCB layout, BOM) are available from
the :adi:`ADMX6001-EBZ product page <ADMX6001>` under the Design Resources
tab.

Software guide
-------------------------------------------------------------------------------

The ADMX6001-EBZ is supported through the :ref:`libiio` library. Applications
that interface via libiio include:

- :ref:`iio-oscilloscope` — graphical waveform and spectrum analyzer,
  connect via manual URI ``ip:192.168.2.1``
- :external+pyadi-iio:doc:`index` — Python interface, using the
  ``admx6001_v1`` branch of the PyADI-IIO repository

For a step-by-step walkthrough, see the
:ref:`admx6001 quickstart vcu118` guide.
