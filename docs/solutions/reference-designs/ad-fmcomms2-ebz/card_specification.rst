.. _ad-fmcomms2-ebz-specs:

RF Card Specifications
======================

The following characterization data was obtained using an Agilent Technology
MXA Signal Analyzer and the Rohde & Schwarz SMA 100A Signal Generator.

.. figure:: hardware/setup2.jpg
   :align: center
   :width: 400

   Test equipment setup

These specs are common to any of the boards which use a narrow band balun
(AD-FMCOMMS2-EBZ, AD-FMCOMMS4-EBZ).

Transmit Specifications
-----------------------

LO Bandwidth
~~~~~~~~~~~~~

.. figure:: hardware/tx_lo_sweep.png
   :align: center
   :width: 400

   LO linearity sweep with 1 MHz tone, -10 dB attenuation and scale of 0.25

Intermodulation Distortion
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.625scale.png
   :align: center
   :width: 400

   IMD3 at LO of 2.4 GHz and tone of 1 MHz with one-eighth power out

.. figure:: hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.125scale.png
   :align: center
   :width: 400

   IMD3 at LO of 2.4 GHz and tone of 1 MHz with quarter power out

.. figure:: hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.25scale.png
   :align: center
   :width: 400

   IMD3 at LO of 2.4 GHz and tone of 1 MHz with half power out

.. figure:: hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.5scale_0000.png
   :align: center
   :width: 400

   IMD3 at LO of 2.4 GHz and tone of 1 MHz with full power out

Phase Noise
~~~~~~~~~~~

.. figure:: hardware/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.5scale_.png
   :align: center
   :width: 400

   1 MHz tone, LO 2.4 GHz, scale of 0.5

.. figure:: hardware/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.25scale.png
   :align: center
   :width: 400

   1 MHz tone, LO 2.4 GHz, scale of 0.25

EVM
~~~

.. figure:: hardware/lte_10tx_0dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE10, with 0 dB attenuation and 2.4 GHz LO

.. figure:: hardware/lte_10tx_10dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE10, with -10 dB attenuation and 2.4 GHz LO

.. figure:: hardware/lte_10tx_20dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE10, with -20 dB attenuation and 2.4 GHz LO

.. figure:: hardware/lte_20tx_0dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE20, with 0 dB attenuation and 2.4 GHz LO

.. figure:: hardware/lte_20tx_10dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE20, with -10 dB attenuation and 2.4 GHz LO

.. figure:: hardware/lte_20tx_20dbatten_2_45ghz_fdd.png
   :align: center
   :width: 500

   EVM test result using LTE20, with -20 dB attenuation and 2.4 GHz LO

Receive Specifications
----------------------

LO Bandwidth
~~~~~~~~~~~~~

.. figure:: hardware/rx_lo_sweep.png
   :align: center
   :width: 400

   RX linearity LO sweep with 1 MHz tone, -10 dB input power and 10 dB
   hardware gain

EVM
~~~

.. figure:: hardware/lte_10_rx_slow_agc_2_45ghz_neg45dbm_input_tdd.png
   :align: center
   :width: 500

   EVM using LTE10 with 2.4 GHz LO and -45 dBm input

Bandwidth
~~~~~~~~~

.. figure:: hardware/bw_sweep_rx_lo2.4ghz_slowattack_gc.png
   :align: center
   :width: 400

   BW with 2.4 GHz LO and -10 dBm input and slow attack gain control

.. figure:: hardware/bw_sweep_rx_lo2.4ghz_manual_gc.png
   :align: center
   :width: 400

   BW with 2.4 GHz LO and -10 dBm input and manual gain control

Configuration Options
---------------------

By default, the AD-FMCOMMS2-EBZ includes the Johanson Technology
2450BL15B050E 2.45 GHz balun. This balun is rated for an operating frequency of
2400-2500 MHz. If you want to evaluate the part outside of this frequency range,
an alternative balun should be installed. A list of alternative baluns are below.

Receive Balun
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Manufacturer
     - Frequency (MHz)
     - Balun Number
     - Impedance
     - AC Coupling
   * - TDK
     - 350
     - HHM1591D1
     - 50/100
     - 100 pF
   * - TDK
     - 900
     - HHM1564A4
     - 50/200
     - 100 pF
   * - Johanson
     - 1450
     - 1450BL15A200E
     - 50/200
     - 20 pF
   * - Johanson
     - 1600
     - 1600BL15B050E
     - 50/50
     - 20 pF
   * - Anaren
     - 1631
     - BD1631J50100A00
     - 50/100
     - 18 pF
   * - Johanson
     - 2450
     - 2450BL15B200E
     - 50/200
     - 9 pF
   * - Johanson
     - 2450
     - 2450BL15B050E
     - 50/50
     - 18 pF
   * - Hitachi
     - 3000
     - ESLT-S370KBI
     - 50/50
     - 10 pF
   * - Johanson
     - 5400
     - 5400BL15K050E
     - 50/50
     - 10 pF
   * - Hitachi
     - 5000
     - ESLT_S540E
     - 50/50
     - 10 pF

Transmit Balun
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Manufacturer
     - Frequency (MHz)
     - Balun Number
     - Impedance
   * - TDK
     - 350
     - HHM1591D1
     - 50/100
   * - Johanson
     - 900
     - 0900BL15C050E
     - 50/50
   * - Johanson
     - 1600
     - 1600BL15B050E
     - 50/50
   * - Johanson
     - 1850
     - 1850BL15B050E
     - 50/50
   * - Johanson
     - 2450
     - 2450BL15B050E
     - 50/50
   * - Johanson
     - 3700
     - 3700BL15B050E
     - 50/50
   * - Johanson
     - 5400
     - 5400BL15K050E
     - 50/50
