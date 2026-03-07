ADALM-PLUTO Transmit
====================

Transmit Architecture
---------------------

The AD9363 transmit chain is based on `Direct Conversion <https://en.wikipedia.org/wiki/Direct-conversion_receiver>`_ techniques. Although this block diagram is for the :adi:`AD9361`, it is also appropirate for the :adi:`AD9363` found inside the ADALM-PLUTO. The differences between the two units are the tuning range and minor missing features (DCXO, external LO are missing, and the RF channel bandwidth is reduced).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361.svg
   :width: 950px
   :height: 650px

Some things to think about:

-  The Tx LO is always the same amplitude, therefore, to get the best Signal to LO ratio, run the DACs as close to full scale as you can, and then turn up/down the output attenuation to vary the output signal strength. (Don't just decrease the input to the DAC). Full scale into the DAC is 12 bits, but to supply a full scale signal using HDL provided by ADI will actually require a 16 bit signal to be provided, where the lower 4 LSBs are removed. See the :doc:`AXI_AD9361 </wiki-migration/resources/fpga/docs/axi_ad9361>` documentation for more details on these interfaces.

Transmit Performance
--------------------

Details on the performance can be found in the `performance section <https://wiki.analog.com/../devs/performance>`_.

While there are many aspects of transmit performance, the two most common are:

-  Output Power (how far can it transmit)
-  Output fidelity (how accurate is the transmission)

For the ADALM-PLUTO, both the output power and output accuracy are frequency dependent.

Transmit Power
~~~~~~~~~~~~~~

Most modern spectrum analyzers allow measurement of power within a frequency range called the channel bandwidth. Such analyzers make many small power measurements :math:`p_i` across a frequency range. They average these power measurements to calculate a desired channel power over a desired frequency range using the following equation:

<m 16>P_CH = {(B_S/B_N)(1/N)sum{i=n_1}{n_2} 10^(p_i/10)}</m>

Where :math:`P_CH` is the power in the channel, :math:`B_S` is the specified bandwidth (also known as the channel bandwidth), :math:`B_N` is the equivalent noise bandwidth of the resolution bandwidth (RBW) used, :math:`N` is the number of data points in the summation, :math:`p_i` is the sample of the power in measurement :math:`i` in dB units (if p_i is in dBm, :math:`P_ch` is in milliwatts). :math:`n_1` and :math:`n_2` are the end-points for the index i within the channel bandwidth, thus :math:`N = (n_2 - n_1) + 1` . [1]_

For this test an LTE10 signal was transmitted at various LO frequencies, and the power in the 9 MHz channel was measured and recorded:

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/pluto_tx_pow.svg
   :alt: LTE10 Power in channel
   :align: center
   :width: 600px

This differs from the a continuous sine wave (CW) at various LOs, were the LO was swept from 70 MHz to 6 GHz. This is not measuring power in the channel, just peak transmit power (the spectrum analyzer was set up to do a peak hold). The two graphs show the difference between the Tx attenuation settings. The default setting of -10dB ensures that the analog output stages are running completely in the linear range, and will not saturate or come close to the 1PdB point. It is also safe at this setting to loop the Tx directly into the Rx with an SMA cable.

.. warning::

   Do not set the TX attenuation to anything less than -10dB and loop the Tx (output) signal into the Rx (input) connector.


However, using the AD9361 or any SDR should be calibrated before attempting any measurement in absolute units. This is necessary since data that is provided from the AD9361 is in reference to the full scale range of the ADC which is dependent on the gain stages of the transceiver. The values produced are therefore best described in dBFS or ADC codes, and not dBm or volts.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/txat0.png
   :alt: CW at 0dB attenuation
   :align: left
   :width: 420px

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/txat-10.png
   :alt: WC at -10dB attenuation
   :align: right
   :width: 420px

The random peaks in the -10 dB attenuation settings are (I think) random noise caused by the Tx calibrations when the LO changes by more than 100 MHz.

As expected, the wider LTE10 channel measurement has more *power* in it than a narrow CW signal.

Transmit Fidelity
~~~~~~~~~~~~~~~~~

This is a the output of the `Keysight 89600 VSA software <http://www.keysight.com/find/89600B>`_, which is used to measure signal demodulation and complete vector signal analysis. In this case, we generate an LTE 10 (10MHz wide channel), and transmit it out the Tx port of the ADALM-PLUTO, and capture it on the `PXA N9030A Signal Analyzer <http://www.keysight.com/find/N9030A>`_. We can measure the RF offset (frequency error = 50Hz), and how accurate the 64-QAM constellation is created (an EVM of -46dB, or less than 0.5% RMS error) - which is pretty good. We can also see the output power (average peak output for the 10MHz channel is -45dBm/Hz).

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/rev_b_tx_lte10.png
   :width: 800px

By changing the LO frequency, output power, output attenuation, these results will change.


|image1|

.. important::

   This is power out the SMA, not the antenna. Any antenna (including the one provided in the kit) may provide additional filtering (change the shape), as well as gain/attenuation


This test was done in an open lab setting and as a result we can observe degradation at certain common commercial frequencies like LTE and WiFi. To remove these outliers the tests should be run inside an RF chamber, to make sure there is no external noise, but since we meet datasheet specifications, we are unlikely to.

.. [1]
   https://literature.cdn.keysight.com/litweb/pdf/5966-4008E.pdf

.. |image1| image:: https://wiki.analog.com/_media/university/tools/pluto/users/pluto_tx2.svg
   :width: 800px
