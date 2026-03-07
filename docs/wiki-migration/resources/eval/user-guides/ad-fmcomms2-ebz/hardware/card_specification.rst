AD-FMCOMMS2-EBZ / AD-FMCOMMS4-EBZ / AD-FMCOMMS5-EBZ Specifications
==================================================================

+---------------------------------------------------------------------------------------------+


| The following equipments were used to generate the following characterization data:         |

+---------------------------------------------------------------------------------------------+
| |image1|                                                                                    |
+---------------------------------------------------------------------------------------------+

| The Agilent Technology MXA Signal Analyzer and the Rohde&Schwarz SMA 100A Signal Generator. |

+---------------------------------------------------------------------------------------------+

These specs are common to any of the boards which use a narrow band balun.

Transmit Specs
--------------

LO BW
~~~~~

+------------------------------------------------------------------------+
| |image2|                                                               |
+------------------------------------------------------------------------+

| LO linearity sweep with 1MHz tone, -10dB attenuation and scale of 0.25 |

+------------------------------------------------------------------------+

Intermodulation Distortion
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------------------+
| |image5|                                                            | |image6|                                                             |
+---------------------------------------------------------------------+----------------------------------------------------------------------+
| Phase Noise at LO of 2.4GHz and Tone of 1MHz with eights power out. | Phase Noise at LO of 2.4GHz and Tone of 1MHz with quarter power out. |
+---------------------------------------------------------------------+----------------------------------------------------------------------+

+-------------------------------------------------------------------+-------------------------------------------------------------------+
| |image9|                                                          | |image10|                                                         |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
| Phase Noise at LO of 2.4GHz and Tone of 1MHz with half power out. | Phase Noise at LO of 2.4GHz and Tone of 1MHz with full power out. |
+-------------------------------------------------------------------+-------------------------------------------------------------------+

Phase Noise
~~~~~~~~~~~

================================== ===================================
|image11|                          |image12|
1MHz tone, LO 2.4GHz, Scale of 0.5 1MHz tone, LO 2.4GHz, Scale of 0.25
================================== ===================================

EVM
~~~

+-------------------------------------------------------------------+
| |image13|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE10, with 0dB attenuation and 2.4GHz LO   |

+-------------------------------------------------------------------+
| |image14|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE10, with -10dB attenuation and 2.4GHz LO |

+-------------------------------------------------------------------+
| |image15|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE10, with -20dB attenuation and 2.4GHz LO |

+-------------------------------------------------------------------+
| |image16|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE20, with 0dB attenuation and 2.4GHz LO   |

+-------------------------------------------------------------------+
| |image17|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE20, with -10dB attenuation and 2.4GHz LO |

+-------------------------------------------------------------------+
| |image18|                                                         |
+-------------------------------------------------------------------+

| EVM test result using LTE20, with -20dB attenuation and 2.4GHz LO |

+-------------------------------------------------------------------+

Receive Specs
-------------

.. _lo-bw-1:

LO BW
~~~~~

+--------------------------------------------------------------------------------+
| |image19|                                                                      |
+--------------------------------------------------------------------------------+

| RX linearity LO sweep with 1MHz tone, -10dB input power and 10dB hardware gain |

+--------------------------------------------------------------------------------+

+-------------------------------------------------+
| |image20|                                       |
+-------------------------------------------------+

| EVM using LTE10 with 2.4GHz LO and -45dBm input |

+-------------------------------------------------+

Bandwidth
~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`_

+-----------------------------------------------------------------+------------------------------------------------------------+
| |image23|                                                       | |image24|                                                  |
+-----------------------------------------------------------------+------------------------------------------------------------+
| BW with 2.4GHz LO and -10dBm input and Slow attack gain control | BW with 2.4GHz LO and -10dBm input and manual gain control |
+-----------------------------------------------------------------+------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/setup2.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tx_lo_sweep.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.625scale.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.125scale.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.625scale.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.125scale.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.25scale.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.5scale_0000.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.25scale.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/imd3_tx_lo2.4ghz_1mhzspacing_-4dbattenuation_0.5scale_0000.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.5scale_.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/phase_noise_tx_lo2.4ghz_1mhztone_-10dbattenuation_0.25scale.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_10tx_0dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_10tx_10dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_10tx_20dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_20tx_0dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_20tx_10dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_20tx_20dbatten_2_45ghz_fdd.png
   :width: 500px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/rx_lo_sweep.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/lte_10_rx_slow_agc_2_45ghz_neg45dbm_input_tdd.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/bw_sweep_rx_lo2.4ghz_slowattack_gc.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/bw_sweep_rx_lo2.4ghz_manual_gc.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/bw_sweep_rx_lo2.4ghz_slowattack_gc.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/bw_sweep_rx_lo2.4ghz_manual_gc.png
   :width: 400px
