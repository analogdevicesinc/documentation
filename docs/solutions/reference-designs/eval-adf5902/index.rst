.. _eval-adf5902:

EVAL-ADF5902
=========================================================================

24 GHz, ISM Band, Multichannel FMCW Radar Transmitter

.. image:: eval-adf5902.png
   :align: center
   :width: 500

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADF5902` evaluation board allows the user to evaluate the
performance of the :adi:`ADF5902`, a 24 GHz transmitter (Tx) monolithic
microwave integrated circuit (MMIC) with an on-chip, 24 GHz voltage controlled
oscillator (VCO). The VCO features a fractional-N frequency synthesizer with
waveform generation capability, programmable grid array (PGA), and dual
transmitter channels for radar systems. The on-chip 24 GHz VCO generates the
24 GHz signal for the two transmitter channels and the local oscillator (LO)
output. Each transmitter channel contains a power control circuit. There is also
an on-chip temperature sensor.

Features:

- 24 GHz to 24.25 GHz VCO (ISM band)
- 2-channel 24 GHz power amplifier with 8 dBm output
- Single-ended outputs with mux and mute function
- Programmable output power
- LO output buffer
- High and low speed FMCW ramp generation
- 25-bit fixed modulus allows subhertz frequency resolution
- Auxiliary 8-bit ADC
- Power control detector
- ±5°C temperature sensor

Applications:

- Automotive radars
- Industrial radars
- Microwave radar sensors

Software
-------------------------------------------------------------------------------

- :doc:`no-OS Setup <software/no-os-setup>`

.. toctree::
   :hidden:

   software/no-os-setup

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
