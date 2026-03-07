AD-FMCOMMS3-EBZ Specifications
==============================

Transmit and Receive Specs
--------------------------

LO BW
~~~~~

+---------------------------------------------+
| |image1|                                    |
+---------------------------------------------+

| LO BW over the full range or 70 MHz to 6GHz |

+---------------------------------------------+

EVM
~~~

The `error vector magnitude <https://en.wikipedia.org/wiki/Error_vector_magnitude>`_ or EVM (sometimes also called receive constellation error or RCE) is a measure used to quantify the performance of a digital radio transmitter or receiver.

A signal would normally be sent by an transmitter and then received by a receiver, and the resulting constellation would be precisely compared to the ideal constellation location. This is a interesting metric since any sort of imperfections in either the transmit or receive implementation (such as carrier leakage, image rejection, phase noise, group delay mismatch, any nonlinearity, jitter, timing recovery, equalization, etc) will cause the actual constellation points to deviate from the ideal locations.

Since EVM is a total system test, users must understand for testing a receiver, a transmitter with better performance that the receiver is required. For testing a transmitter, a receiver with better performance than then transmitter is required. Care must be taking to understand the "weakest" link, and where the performance limit is coming from. It can be any of:

-  transmitter
-  receiver
-  receive algorithm

In many cases `LTE <https://en.wikipedia.org/wiki/LTE_(telecommunication)>`_ is used for EVM testing, since it such as well defined, and understdood standard for high-speed wireless communication for mobile phones and data terminals. The the `European Telecommunications Standards Institute <http://www.etsi.org/>`_ (ETSI) has detailed  [1]_ standards which define the waveforms used for LTE EVM testing, including:

-  EVM of single 64QAM PRB (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, and 20 MHz channels) at max and min powers
-  EVM for 16QAM modulation (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, and 20 MHz channels)
-  EVM for QPSK modulation (for 1.4 MHz, 3 MHz, 5 MHz, 10 MHz, 15 MHz, and 20 MHz channels)

To create these vectors to play out either a bench instrument, or a SDR platform, most people (including ADI) use one of:

-  Keysight `Signal Studio <https://www.keysight.com/zz/en/software/application-sw/signal-studio-software.html>`_
-  MathWorks `LTE System Toolbox <https://www.mathworks.com/products/lte.html>`_

On the receive side (to actually decode the LTE signal, and measure EVM), we use one of:

-  Keysight `89600 VSA Software <https://www.keysight.com/zz/en/software/application-sw/89600-vsa-software.html>`_
-  MathWorks `LTE System Toolbox <https://www.mathworks.com/products/lte.html>`_

To complicate matters, EVM is a unit-less measurement. It's a ratio, which can be represented in both percent (%) or as a dB (converting to log scale). Since dB will show you in details where the differences are - it's easier to understand the difference between 2%, 1% and half a percent by discussing -34 dB, -40 dB, -46 dB (which are the same physical error). Typically EVM performance of less than -35 dB is required for many communications applications.

+-------------------------------------------+
| |image2|                                  |
+-------------------------------------------+

| EVM over the full range or 70 MHz to 6GHz |

+-------------------------------------------+

Transmit Specs
--------------

TX Output Power vs Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there is a large (2 orders of magnitude) tuning range of the device (70 MHz to 6000 MHz), it's good to understand how much power the AD9361 can output.

Tests were done both with CW (single tone 10 MHz offset from the LO), measuring output power, lo leakage, and image.

+---------------------------------------------+
| |image3|                                    |
+---------------------------------------------+

| TX Output Power vs Frequency 70 MHz to 6GHz |

+---------------------------------------------+

Tests should also be done with a wide band signal (LTE 10), measuring output power, and `ACPR <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`_).

Adjacent Channel Power
~~~~~~~~~~~~~~~~~~~~~~

`ACP <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`_

Phase Noise
~~~~~~~~~~~

`Phase noise <https://en.wikipedia.org/wiki/Phase noise>`_

Output power
~~~~~~~~~~~~

`Transmitter power output <https://en.wikipedia.org/wiki/Transmitter power output>`_

Intermodulation Distortion
~~~~~~~~~~~~~~~~~~~~~~~~~~

`IMD <https://en.wikipedia.org/wiki/Intermodulation>`_

Bandwidth
~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`_

Receive Specs
-------------

Signal to Noise
~~~~~~~~~~~~~~~

`SNR <https://en.wikipedia.org/wiki/Signal-to-noise_ratio>`_

Noise floor
~~~~~~~~~~~

`Noise floor <https://en.wikipedia.org/wiki/Noise floor>`_

Input sensitivity
~~~~~~~~~~~~~~~~~

`Input sensitivity <https://en.wikipedia.org/wiki/Sensitivity_(electronics)>`_

Dynamic range
~~~~~~~~~~~~~

`Dynamic range <https://en.wikipedia.org/wiki/Dynamic range>`_

.. _lo-bw-1:

LO BW
~~~~~

+---------------------------------------------+
| |image4|                                    |
+---------------------------------------------+

| LO BW over the full range or 70 MHz to 6GHz |

+---------------------------------------------+

.. _evm-1:

EVM
~~~

+------------------------------------------+
| |image5|                                 |
+------------------------------------------+

| LTE10, slow AGC, 2.4GHz LO, -38dBm input |

+------------------------------------------+
| |image6|                                 |
+------------------------------------------+

| LTE20, slow AGC, 2.4GHz LO, -38dBm input |

+------------------------------------------+

.. [1]
   `ETSI TS 136 141 Specification <http://www.etsi.org/deliver/etsi_ts/136100_136199/136141/12.05.00_60/ts_136141v120500p.pdf>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/fmcomms3_6ghz_lo_sweep.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/fmcomms3_evm.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/tx_wb_sweep.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/rx_sweep_track.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/lte_10_rx_slow_agc_2_45ghz_neg38dbm_input_fdd.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms3-ebz/hardware/lte_20_rx_slow_agc_2_45ghz_neg38dbm_input_fdd.png
   :width: 500px
