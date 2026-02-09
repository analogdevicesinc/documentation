.. _ad-fmcomms3-ebz card-specifications:

AD-FMCOMMS3-EBZ Specifications
==============================

Transmit and Receive Specs
--------------------------

LO BW
~~~~~

.. figure:: lo_sweep.png

   LO BW over the full range or 70 MHz to 6 GHz

EVM
~~~

The `error vector magnitude <https://en.wikipedia.org/wiki/Error_vector_magnitude>`__
or EVM (sometimes also called receive constellation error or RCE) is a
measure used to quantify the performance of a digital radio transmitter
or receiver.

A signal would normally be sent by an transmitter and then received by a
receiver, and the resulting constellation would be precisely compared to
the ideal constellation location. This is a interesting metric since any
sort of imperfections in either the transmit or receive implementation
(such as carrier leakage, image rejection, phase noise, group delay
mismatch, any nonlinearity, jitter, timing recovery, equalization, etc)
will cause the actual constellation points to deviate from the ideal
locations.

Since EVM is a total system test, users must understand for testing a
receiver, a transmitter with better performance that the receiver is
required. For testing a transmitter, a receiver with better performance
than then transmitter is required. Care must be taking to understand the
“weakest” link, and where the performance limit is coming from. It can
be any of:

 - transmitter

 - receiver

 - receive algorithm

In many cases
`LTE <https://en.wikipedia.org/wiki/LTE_%28telecommunication%29>`__ is
used for EVM testing, since it such as well defined, and understood
standard for high-speed wireless communication for mobile phones and
data terminals. The
`European Telecommunications Standards Institute <http://www.etsi.org/>`__
(ETSI) has :download:`detailed standards <ts_136141.pdf>`
which define the waveforms used for LTE EVM testing, including:

 - EVM of single 64QAM PRB (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz,
   and 20 MHz channels) at max and min powers

 - EVM for 16QAM modulation (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz,
   and 20 MHz channels)

 - EVM for QPSK modulation (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz,
   and 20 MHz channels)

To create these vectors to play out either a bench instrument, or a SDR
platform, most people (including ADI) use one of:

 - Keysight
   `SignalStudio <https://www.keysight.com/zz/en/software/application-sw/signal-studio-software.html>`__

 - MathWorks
   `LTE System Toolbox <https://www.mathworks.com/products/lte.html>`__

On the receive side (to actually decode the LTE signal, and measure
EVM), we use one of:

 - Keysight
   `89600 VSA Software <https://www.keysight.com/zz/en/software/application-sw/89600-vsa-software.html>`__

 - MathWorks
   `LTE System Toolbox <https://www.mathworks.com/products/lte.html>`__

To complicate matters, EVM is a unit-less measurement. It’s a ratio,
which can be represented in both percent (%) or as a dB (converting to
log scale). Since dB will show you in details where the differences are
- it’s easier to understand the difference between 2%, 1% and half a
percent by discussing -34 dB, -40 dB, -46 dB (which are the same
physical error). Typically EVM performance of less than -35 dB is
required for many communications applications.

.. figure:: fmcomms3_evm.png

   EVM over the full range or 70 MHz to 6 GHz

Transmit Specs
--------------

Tx Output Power vs Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there is a large (2 orders of magnitude) tuning range of the
device (70 MHz to 6000 MHz), it’s good to understand how much power the
AD9361 can output.

Tests were done both with CW (single tone 10 MHz offset from the LO),
measuring output power, lo leakage, and image.

.. figure:: tx_wb_sweep.png

   Tx Output Power vs Frequency 70 MHz to 6 GHz

Tests should also be done with a wide band signal (LTE 10), measuring
output power, and
`ACPR <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`__.

Adjacent Channel Power
~~~~~~~~~~~~~~~~~~~~~~

`ACP <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`__

Phase Noise
~~~~~~~~~~~

`Phase noise <https://en.wikipedia.org/wiki/Phase%20noise>`__

Output power
~~~~~~~~~~~~

`Transmitter power output <https://en.wikipedia.org/wiki/Transmitter%20power%20output>`__

Intermodulation Distortion
~~~~~~~~~~~~~~~~~~~~~~~~~~

`IMD <https://en.wikipedia.org/wiki/Intermodulation>`__

Bandwidth
~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_%28signal_processing%29>`__

Receive Specs
-------------

Signal to Noise
~~~~~~~~~~~~~~~

`SNR <https://en.wikipedia.org/wiki/Signal-to-noise_ratio>`__

Noise floor
~~~~~~~~~~~

`Noise floor <https://en.wikipedia.org/wiki/Noise%20floor>`__

Input sensitivity
~~~~~~~~~~~~~~~~~

`Input sensitivity <https://en.wikipedia.org/wiki/Sensitivity_%28electronics%29>`__

Dynamic range
~~~~~~~~~~~~~

`Dynamic range <https://en.wikipedia.org/wiki/Dynamic%20range>`__

LO BW
~~~~~

.. figure:: rx_sweep_track.png

   LO BW over the full range or 70 MHz to 6 GHz

EVM
~~~

.. figure:: lte_10_rx_slow.png
   :width: 800px

   LTE10, slow AGC, 2.4GHz LO, -38dBm input

.. figure:: lte_20_rx_slow.png
   :width: 800px

   LTE20, slow AGC, 2.4GHz LO, -38dBm input
