.. _ad_fmcomms1_ebz hardware card-specification:

AD-FMCOMMS1-EBZ Specifications
==============================

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

Transmit Specs
--------------

There are many specifications on the Transmit side of a RF system

- :adi:`Evaluating High Speed DAC Performance <MT-013>`

Theoretical specs
~~~~~~~~~~~~~~~~~

Bandwidth
^^^^^^^^^

Determining overall channel bandwidth is a little complex, since many devices
don't have a meaningful (in this aspect) bandwidth number.

|AD9122 Spurs| |ADL5375 Bandwidth|\ |ADL5602 Gain Flatness over frequency|

- In the AD9122, the above figure shows an fDATA of 400MHz, creating a waveform
  over 350MHz.
- The ADL5375 does include a baseband bandwidth specification - depending on the
  flatness you require, could be 200MHz (+/- 0.1dB) or 500MHz (+/- 0.5dB).
- the ADL5602 has different gain, depending on the RF frequency (but over
  250MHz, you will still notice).

So, transmit bandwidth can be as high as 250 MHz, depending on if the flatness
of the ADL5602 and ADL5375 works for your application.

LO BW (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~

+------------------------------+
| |image1|                     |
+------------------------------+

| LO BW with full output power |

+------------------------------+

Adjacent Channel Power (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`ACP <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`__

+--------------------------------------------------------------+--------------------------------------------------------------+
| |image4|                                                     | |image5|                                                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| ACP with LO of 1.2GHZ and Tone of 40MHz with full power out. | ACP with LO of 1.2GHZ and Tone of 40MHz with half power out. |
+--------------------------------------------------------------+--------------------------------------------------------------+

+--------------------------------------------------------------+--------------------------------------------------------------+
| |image8|                                                     | |image9|                                                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| ACP with LO of 2.4GHZ and Tone of 40MHz with full power out. | ACP with LO of 2.4GHZ and Tone of 40MHz with half power out. |
+--------------------------------------------------------------+--------------------------------------------------------------+

+--------------------------------------------------------------+--------------------------------------------------------------+
| |image12|                                                    | |image13|                                                    |
+--------------------------------------------------------------+--------------------------------------------------------------+
| ACP with LO of 3.6GHZ and Tone of 40MHz with full power out. | ACP with LO of 3.6GHZ and Tone of 40MHz with half power out. |
+--------------------------------------------------------------+--------------------------------------------------------------+

Phase Noise (RevB unmodified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Phase noise <https://en.wikipedia.org/wiki/Phase_noise>`__

+--------------------------------------------------------------------+--------------------------------------------------------------------+
| |image16|                                                          | |image17|                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------+
| Phase Noise at LO of 400MHz and Tone of 40MHz with full power out. | Phase Noise at LO of 900MHz and Tone of 40MHz with full power out. |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

+--------------------------------------------------------------------+--------------------------------------------------------------------+
| |image20|                                                          | |image21|                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------+
| Phase Noise at LO of 1.8GHz and Tone of 40MHz with full power out. | Phase Noise at LO of 2.4GHz and Tone of 40MHz with full power out. |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

+--------------------------------------------------------------------+
| |image22|                                                          |
+--------------------------------------------------------------------+

| Phase Noise at LO of 3.5GHz and Tone of 40MHz with full power out. |

+--------------------------------------------------------------------+

Phase Noise (RevB Modified Board & RevC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------+
| |image25|                                                          | |image26|                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------+
| Phase Noise at LO of 1.2GHz and Tone of 40MHz with full power out. | Phase Noise at LO of 1.2GHz and Tone of 40MHz with half power out. |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

+--------------------------------------------------------------------+--------------------------------------------------------------------+
| |image29|                                                          | |image30|                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------+
| Phase Noise at LO of 2.4GHz and Tone of 40MHz with full power out. | Phase Noise at LO of 2.4GHz and Tone of 40MHz with half power out. |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

+--------------------------------------------------------------------+--------------------------------------------------------------------+
| |image33|                                                          | |image34|                                                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------+
| Phase Noise at LO of 3.6GHz and Tone of 40MHz with full power out. | Phase Noise at LO of 3.6GHz and Tone of 40MHz with half power out. |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

Output power (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Transmitter power output <https://en.wikipedia.org/wiki/Transmitter_power_output>`__

+-------------------------------------------------------------+
| |image35|                                                   |
+-------------------------------------------------------------+

| CP with LO of 1.2GHZ and Tone of 40MHz with full power out. |

+-------------------------------------------------------------+
| |image36|                                                   |
+-------------------------------------------------------------+

| CP with LO of 2.4GHZ and Tone of 40MHz with full power out. |

+-------------------------------------------------------------+
| |image37|                                                   |
+-------------------------------------------------------------+

| CP with LO of 3.6GHZ and Tone of 40MHz with full power out. |

+-------------------------------------------------------------+

Intermodulation Distortion (Old Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Intermodulation_Distortion <https://en.wikipedia.org/wiki/Intermodulation#Measurement>`__ or IMD

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| |image40|                                                                                  | |image41|                                                                                  |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Intermodulation Distortion showing 3rd and 5th order products at 450MHz for 3 power levels | Intermodulation Distortion showing 3rd and 5th order products at 950MHz for 3 power levels |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| |image44|                                                                                   | |image45|                                                                                   |
+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Intermodulation Distortion showing 3rd and 5th order products at 1.85GHz for 3 power levels | Intermodulation Distortion showing 3rd and 5th order products at 2.45GHz for 3 power levels |
+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

Intermodulation Distortion (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+---------------------------------------+----------------------------------------+
| |image55|                            | |image56|                             | |image57|                              |
+--------------------------------------+---------------------------------------+----------------------------------------+
| 1MHz Offset, LO 1.2GHz, Scale of 0.5 | 1MHz Offset, LO 1.2GHz, Scale of 0.25 | 1MHz Offset, LO 1.2GHz, Scale of 0.125 |
+--------------------------------------+---------------------------------------+----------------------------------------+
| |image58|                            | |image59|                             | |image60|                              |
+--------------------------------------+---------------------------------------+----------------------------------------+
| 1MHz Offset, LO 2.4GHz, Scale of 0.5 | 1MHz Offset, LO 2.4GHz, Scale of 0.25 | 1MHz Offset, LO 2.4GHz, Scale of 0.125 |
+--------------------------------------+---------------------------------------+----------------------------------------+
| |image61|                            | |image62|                             | |image63|                              |
+--------------------------------------+---------------------------------------+----------------------------------------+
| 1MHz Offset, LO 3.6GHz, Scale of 0.5 | 1MHz Offset, LO 3.6GHz, Scale of 0.25 | 1MHz Offset, LO 3.6GHz, Scale of 0.125 |
+--------------------------------------+---------------------------------------+----------------------------------------+

bandwidth (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`_

+-----------------------------------------------------------------------+
| |image64|                                                             |
+-----------------------------------------------------------------------+

| BW with LO of 1.2GHZ with full power out. (20dB external attenuation) |

+-----------------------------------------------------------------------+
| |image65|                                                             |
+-----------------------------------------------------------------------+

| BW with LO of 2.4GHZ with full power out. (20dB external attenuation) |

+-----------------------------------------------------------------------+
| |image66|                                                             |
+-----------------------------------------------------------------------+

| BW with LO of 3.6GHZ with full power out. (20dB external attenuation) |

+-----------------------------------------------------------------------+

Receive Specs
-------------

Response to a "chirp"
~~~~~~~~~~~~~~~~~~~~~

Although this doesn't have a specific number associated with it, many RF systems
are "chirpy" - and linear response to these RF pulses is very important.

Here is a 2.4GHz waveform, input at -60dbB, with the VGA gain turned up to
+20dB. Although this does have some DC offset (the card was not calibrated), the
response is very linear over time, even when zoomed in. (Clicking on either
picture will open it up in a larger window)

|image67| |image68|

And with a larger input - it looks similar. This is with an input of +6.0dBm,
with the VGA set to 4.5dB.|

|image69| |image70|

The results are similar at different frequencies.|

Signal to Noise
~~~~~~~~~~~~~~~

`SNR <https://en.wikipedia.org/wiki/Signal-to-noise_ratio>`_

Noise floor
~~~~~~~~~~~

`Noise floor <https://en.wikipedia.org/wiki/Noise_floor>`__

Input sensitivity
~~~~~~~~~~~~~~~~~

`Input sensitivity <https://en.wikipedia.org/wiki/Sensitivity_(electronics)>`_

Dynamic range
~~~~~~~~~~~~~

`Dynamic range <https://en.wikipedia.org/wiki/Dynamic_range>`__

LO BW (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------+
| |image71|                                                                                                   |
+-------------------------------------------------------------------------------------------------------------+

| LO Sweep from 400 MHz to 4GHz, with 0dBm input signal (Low frequency roll-off is due to Balun 3600BL14M050) |

+-------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------+
| |image72|                                                                        |
+----------------------------------------------------------------------------------+

| LO Sweep from 400 MHz to 4GHz, with 0dBm input signal (With new Balun TC1-1-43A) |

+----------------------------------------------------------------------------------+

Intermodulation Distortion (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+-------------------------------------+--------------------------------------+
| |image82|                          | |image83|                           | |image84|                            |
+------------------------------------+-------------------------------------+--------------------------------------+
| 1MHz Offset, LO 1.2GHz, 0dBm input | 1MHz Offset, LO 1.2GHz, -6dBm input | 1MHz Offset, LO 1.2GHz, -12dBm input |
+------------------------------------+-------------------------------------+--------------------------------------+
| |image85|                          | |image86|                           | |image87|                            |
+------------------------------------+-------------------------------------+--------------------------------------+
| 1MHz Offset, LO 2.4GHz, 0dBm input | 1MHz Offset, LO 2.4GHz, -6dBm input | 1MHz Offset, LO 2.4GHz, -12dBm input |
+------------------------------------+-------------------------------------+--------------------------------------+
| |image88|                          | |image89|                           | |image90|                            |
+------------------------------------+-------------------------------------+--------------------------------------+
| 1MHz Offset, LO 3.6GHz, 0dBm input | 1MHz Offset, LO 3.6GHz, -6dBm input | 1MHz Offset, LO 3.6GHz, -12dBm input |
+------------------------------------+-------------------------------------+--------------------------------------+

Bandwidth (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`_

+-----------------------------------------+-----------------------------------------+
| |image93|                               | |image94|                               |
+-----------------------------------------+-----------------------------------------+
| BW with 1.2GHz LO and 0dBm input (Ch1). | BW with 1.2GHz LO and 0dBm input (Ch2). |
+-----------------------------------------+-----------------------------------------+

+-----------------------------------------+-----------------------------------------+
| |image97|                               | |image98|                               |
+-----------------------------------------+-----------------------------------------+
| BW with 2.4GHz LO and 0dBm input (Ch1). | BW with 2.4GHz LO and 0dBm input (Ch2). |
+-----------------------------------------+-----------------------------------------+

+-----------------------------------------+-----------------------------------------+
| |image101|                              | |image102|                              |
+-----------------------------------------+-----------------------------------------+
| BW with 3.6GHz LO and 0dBm input (Ch1). | BW with 3.6GHz LO and 0dBm input (Ch2). |
+-----------------------------------------+-----------------------------------------+

.. |AD9122 Spurs| image:: ../images/ad9122_fig10.png
   :width: 250

.. |ADL5375 Bandwidth| image:: ../images/adl5375-05_fig63.png
   :width: 250

.. |ADL5602 Gain Flatness over frequency| image:: ../images/adl5602.png
   :width: 250

.. |image1| image:: ../images/tx_bw_0.4to4ghz_scale_0.5.png
   :width: 200

.. |image2| image:: ../images/acp_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image3| image:: ../images/acp_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image4| image:: ../images/acp_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image5| image:: ../images/acp_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image6| image:: ../images/acp_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image7| image:: ../images/acp_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image8| image:: ../images/acp_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image9| image:: ../images/acp_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image10| image:: ../images/acp_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image11| image:: ../images/acp_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image12| image:: ../images/acp_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image13| image:: ../images/acp_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image14| image:: ../images/phase_noise_at_440mhz_rx_lo_off.png
   :width: 200

.. |image15| image:: ../images/phase_noise_at_940mhz_rx_lo_off.png
   :width: 200

.. |image16| image:: ../images/phase_noise_at_440mhz_rx_lo_off.png
   :width: 200

.. |image17| image:: ../images/phase_noise_at_940mhz_rx_lo_off.png
   :width: 200

.. |image18| image:: ../images/phase_noise_at_1.84ghz_rx_lo_off.png
   :width: 200

.. |image19| image:: ../images/phase_noise_at_2.44ghz_rx_lo_off.png
   :width: 200

.. |image20| image:: ../images/phase_noise_at_1.84ghz_rx_lo_off.png
   :width: 200

.. |image21| image:: ../images/phase_noise_at_2.44ghz_rx_lo_off.png
   :width: 200

.. |image22| image:: ../images/phase_noise_at_3.54ghz_rx_lo_off.png
   :width: 200

.. |image23| image:: ../images/phase_noise_1.24ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image24| image:: ../images/phase_noise_1.24ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image25| image:: ../images/phase_noise_1.24ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image26| image:: ../images/phase_noise_1.24ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image27| image:: ../images/phase_noise_2.44ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image28| image:: ../images/phase_noise_2.44ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image29| image:: ../images/phase_noise_2.44ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image30| image:: ../images/phase_noise_2.44ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image31| image:: ../images/phase_noise_3.64ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image32| image:: ../images/phase_noise_3.64ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image33| image:: ../images/phase_noise_3.64ghz_rx_lo_off_scale0.5_new.png
   :width: 200

.. |image34| image:: ../images/phase_noise_3.64ghz_rx_lo_off_scale0.25_new.png
   :width: 200

.. |image35| image:: ../images/cp_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image36| image:: ../images/cp_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image37| image:: ../images/cp_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image38| image:: ../images/imd_450mhz_vs_output_power.png
   :width: 200

.. |image39| image:: ../images/imd_950mhz_vs_output_power.png
   :width: 200

.. |image40| image:: ../images/imd_450mhz_vs_output_power.png
   :width: 200

.. |image41| image:: ../images/imd_950mhz_vs_output_power.png
   :width: 200

.. |image42| image:: ../images/imd_1.85ghz_vs_output_power.png
   :width: 200

.. |image43| image:: ../images/imd_2.45ghz_vs_output_power.png
   :width: 200

.. |image44| image:: ../images/imd_1.85ghz_vs_output_power.png
   :width: 200

.. |image45| image:: ../images/imd_2.45ghz_vs_output_power.png
   :width: 200

.. |image46| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image47| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image48| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image49| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image50| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image51| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image52| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image53| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image54| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image55| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image56| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image57| image:: ../images/imd3_1.24ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image58| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image59| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image60| image:: ../images/imd3_2.44ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image61| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200

.. |image62| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200

.. |image63| image:: ../images/imd3_3.64ghz_rx_lo_off_scale0.125.png
   :width: 200

.. |image64| image:: ../images/bw_rx_lo_off_scale0.5_tx_lo_1.2ghz.png
   :width: 200

.. |image65| image:: ../images/bw_rx_lo_off_scale0.5_tx_lo_2.4ghz.png
   :width: 200

.. |image66| image:: ../images/bw_rx_lo_off_scale0.5_tx_lo_3.6ghz.png
   :width: 200

.. |image67| image:: ../images/chirp_2.4ghz.png
   :width: 200

.. |image68| image:: ../images/chirp_zoom_2.4ghz.png
   :width: 200

.. |image69| image:: ../images/chirp_2.4ghz_6dbm.png
   :width: 200

.. |image70| image:: ../images/chirp_2.4ghz_6dbm_zoom.png
   :width: 200

.. |image71| image:: ../images/rx_lo_bw_0.4to4ghz.png
   :width: 200

.. |image72| image:: ../images/with_new_balun_tc1-1-43a.png
   :width: 200

.. |image73| image:: ../images/imd3_rx_0dbm_1.2ghzlo.png
   :width: 200

.. |image74| image:: ../images/imd3_rx_-6dbm_1.2ghzlo.png
   :width: 200

.. |image75| image:: ../images/imd3_rx_-12dbm_1.2ghzlo.png
   :width: 200

.. |image76| image:: ../images/imd3_rx_0dbm_2.4ghzlo.png
   :width: 200

.. |image77| image:: ../images/imd3_rx_-6dbm_2.4ghzlo.png
   :width: 200

.. |image78| image:: ../images/imd3_rx_-12dbm_2.4ghzlo.png
   :width: 200

.. |image79| image:: ../images/imd3_rx_0dbm_3.6ghzlo.png
   :width: 200

.. |image80| image:: ../images/imd3_rx_-6dbm_3.6ghzlo.png
   :width: 200

.. |image81| image:: ../images/imd3_rx_-12dbm_3.6ghzlo.png
   :width: 200

.. |image82| image:: ../images/imd3_rx_0dbm_1.2ghzlo.png
   :width: 200

.. |image83| image:: ../images/imd3_rx_-6dbm_1.2ghzlo.png
   :width: 200

.. |image84| image:: ../images/imd3_rx_-12dbm_1.2ghzlo.png
   :width: 200

.. |image85| image:: ../images/imd3_rx_0dbm_2.4ghzlo.png
   :width: 200

.. |image86| image:: ../images/imd3_rx_-6dbm_2.4ghzlo.png
   :width: 200

.. |image87| image:: ../images/imd3_rx_-12dbm_2.4ghzlo.png
   :width: 200

.. |image88| image:: ../images/imd3_rx_0dbm_3.6ghzlo.png
   :width: 200

.. |image89| image:: ../images/imd3_rx_-6dbm_3.6ghzlo.png
   :width: 200

.. |image90| image:: ../images/imd3_rx_-12dbm_3.6ghzlo.png
   :width: 200

.. |image91| image:: ../images/rx_bw_lo_1.2ghz_0dbm_input.png
   :width: 200

.. |image92| image:: ../images/rx_bw_lo_1.2ghz_0dbm_input_ch2.png
   :width: 200

.. |image93| image:: ../images/rx_bw_lo_1.2ghz_0dbm_input.png
   :width: 200

.. |image94| image:: ../images/rx_bw_lo_1.2ghz_0dbm_input_ch2.png
   :width: 200

.. |image95| image:: ../images/rx_bw_lo_2.4ghz_0dbm_input.png
   :width: 200

.. |image96| image:: ../images/rx_bw_lo_2.4ghz_0dbm_input_ch2.png
   :width: 200

.. |image97| image:: ../images/rx_bw_lo_2.4ghz_0dbm_input.png
   :width: 200

.. |image98| image:: ../images/rx_bw_lo_2.4ghz_0dbm_input_ch2.png
   :width: 200

.. |image99| image:: ../images/rx_bw_lo_3.6chz_0dbm_input.png
   :width: 200

.. |image100| image:: ../images/rx_bw_lo_3.6ghz_0dbm_input_ch2.png
   :width: 200

.. |image101| image:: ../images/rx_bw_lo_3.6chz_0dbm_input.png
   :width: 200

.. |image102| image:: ../images/rx_bw_lo_3.6ghz_0dbm_input_ch2.png
   :width: 200
