.. imported from: https://wiki.analog.com/resources/tools-software/linux-software/FMCOMMS1_plugin

.. _fmcomms1-plugin:

FMCOMMS1 Plugin Description
===========================

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated, which
   means it is no longer maintained or actively updated, even though the devices
   themselves may be Recommended for New Designs or in Production. This page is
   here for historical/reference purposes only.

The FMCOMMS1 plugin works with the :ref:`iio-oscilloscope`. The FMCOMMS1 view is
divided into two sections:

- **Receive Chain**
- **Transmit Chain**

.. image:: ../images/fmcomms1_plugin.png
   :align: center

Clicking the **Save Settings** button will write changes which have been made to
the FMCOMMS1 settings to the hardware. Values round to the nearest
hardware-supported value upon saving.

Receive Chain
-------------

ADC Settings
~~~~~~~~~~~~

- **Sampling Frequency (MHz):** Configures the ADC sampling rate.

Gain Amplifier Settings
~~~~~~~~~~~~~~~~~~~~~~~

- **Lock Channels:** Forces matching gain values on both channels.
- **Gain (dB):** Adjustable I/Q channel gain, from 4.5 dB to 20.5 dB. See
  :adi:`AD8366` for more details.

RX LO Settings
~~~~~~~~~~~~~~~

Configures the receive PLL (:adi:`ADF4350`).

- **Enable:** Toggles the local oscillator on/off.
- **Frequency (MHz):** Sets the receive base frequency.
- **Spacing (Hz):** Selects the frequency spacing.

Transmit Chain
--------------

DDS Settings
~~~~~~~~~~~~

The DDS (Direct Digital Synthesizer) provides test tone generation. See
:external+linux:ref:`AXI DAC DDS HDL documentation <axi-dac-dds-hdl>` for more
details.

Available modes:

- **One CW Tone**
- **Two CW Tones**
- **Independent I/Q Control**
- **DAC Buffer Output**
- **Disabled**

Tone Parameters:

- **Frequency (MHz):** Tone frequency selection.
- **Scale:** Amplitude adjustment.
- **Phase (degrees):** Phase offset configuration.

DAC Frequency Settings
~~~~~~~~~~~~~~~~~~~~~~

- **Data (MHz):** DAC data clock.
- **Interpolation (Hz):** Selectable interpolation frequencies.
- **Center Shift (Hz):** Selectable center shift frequencies.

TX LO Settings
~~~~~~~~~~~~~~

Configures the transmit PLL (:adi:`ADF4350`).

- **Enable:** Toggles the local oscillator on/off.
- **Frequency (MHz):** Sets the transmit output frequency.
- **Spacing (Hz):** Selects the frequency spacing.
