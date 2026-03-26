.. _fmcomms2 hardware card-specification:

AD-FMCOMMS2-EBZ / AD-FMCOMMS4-EBZ / AD-FMCOMMS5-EBZ Specifications
===============================================================================

The following equipment was used to generate the characterization data below.
These specs are common to any of the boards which use a narrow band balun.

.. figure:: ../images/setup2.jpg
   :width: 400

   The Agilent Technology MXA Signal Analyzer and the Rohde & Schwarz SMA 100A
   Signal Generator.

Transmit Specs
-------------------------------------------------------------------------------

LO BW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/tx_lo_sweep.png
   :width: 400

   LO linearity sweep with 1 MHz tone, -10 dB attenuation and scale of 0.25.

Intermodulation Distortion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid::
   :widths: 50 50

   .. figure:: ../images/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.625scale.png

      Phase Noise at LO of 2.4 GHz and Tone of 1 MHz with 1/8 power out.

   .. figure:: ../images/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.125scale.png

      Phase Noise at LO of 2.4 GHz and Tone of 1 MHz with quarter power out.

.. grid::
   :widths: 50 50

   .. figure:: ../images/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.25scale.png

      Phase Noise at LO of 2.4 GHz and Tone of 1 MHz with half power out.

   .. figure:: ../images/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.5scale_0000.png

      Phase Noise at LO of 2.4 GHz and Tone of 1 MHz with full power out.

Phase Noise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid::
   :widths: 50 50

   .. figure:: ../images/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.5scale_.png

      1 MHz tone, LO 2.4 GHz, Scale of 0.5.

   .. figure:: ../images/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.25scale.png

      1 MHz tone, LO 2.4 GHz, Scale of 0.25.

EVM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/lte_10tx_0dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE10, with 0 dB attenuation and 2.4 GHz LO.

.. figure:: ../images/lte_10tx_10dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE10, with -10 dB attenuation and 2.4 GHz LO.

.. figure:: ../images/lte_10tx_20dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE10, with -20 dB attenuation and 2.4 GHz LO.

.. figure:: ../images/lte_20tx_0dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE20, with 0 dB attenuation and 2.4 GHz LO.

.. figure:: ../images/lte_20tx_10dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE20, with -10 dB attenuation and 2.4 GHz LO.

.. figure:: ../images/lte_20tx_20dbatten_2_45ghz_fdd.png
   :width: 500

   EVM test result using LTE20, with -20 dB attenuation and 2.4 GHz LO.

Receive Specs
-------------------------------------------------------------------------------

LO BW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/rx_lo_sweep.png
   :width: 400

   RX linearity LO sweep with 1 MHz tone, -10 dB input power and 10 dB hardware
   gain.

.. figure:: ../images/lte_10_rx_slow_agc_2_45ghz_neg45dbm_input_tdd.png
   :width: 500

   EVM using LTE10 with 2.4 GHz LO and -45 dBm input.

Bandwidth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`_

.. grid::
   :widths: 50 50

   .. figure:: ../images/bw_sweep_rx_lo2.4ghz_slowattack_gc.png

      BW with 2.4 GHz LO and -10 dBm input and Slow attack gain control.

   .. figure:: ../images/bw_sweep_rx_lo2.4ghz_manual_gc.png

      BW with 2.4 GHz LO and -10 dBm input and manual gain control.
