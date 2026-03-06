ADAR1000EVAL1Z Data Set
=======================

Receive Mode
============

Gain, Return Loss
-----------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_rx_spars_maxgain.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 1: Gain and Return Loss vs. Frequency, at Maximum Gain, Receive Channel**\


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_rx_gain_gain.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **//Figure 2: Gain vs. Frequency for Gain Settings from 0 to 127, Single Receive Channel //**\


Noise Figure
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_rx_nf_over_gain.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 3: Noise Figure vs. Frequency over Gain, Receive Channel**\


Input P1dB
----------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_rx_ip1db_gain.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 4: Input P1dB vs. Frequency over Gain, Receive Channel**\


Input IP3
---------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_rx_iip3_gain.png
   :align: center
   :width: 600px

.. container:: centeralign

   \ **Figure 5: Input IP3 vs. Frequency over Gain, Receive Channel**\


Transmit Mode
=============

.. _gain-return-loss-1:

Gain, Return Loss
-----------------

|image1|

.. container:: centeralign

   \ **Figure 6: Gain and Return Loss vs. Frequency, at Maximum Gain, Transmit Channel**\


.. _noise-figure-1:

Noise Figure
------------

|image2|

.. container:: centeralign

   \ **Figure 7: Noise Figure vs. Frequency over Gain, Transmit Channel**\


Output IP3
----------

|image3|

.. container:: centeralign

   \ **Figure 8: Output IP3 vs. Frequency, Transmit Channel**\


Output P1dB
-----------

|image4|

.. container:: centeralign

   \ **Figure 9: Output P1dB vs. Frequency, Transmit Channel**\


Output Power vs Input Power
---------------------------

|image5|

.. container:: centeralign

   \ **Figure 10: Output Power vs Input Power, Transmit Channel at 10 GHz**\


Switching Speed
===============

This measurement was conducted using a single cell (1x ADAR1000, 4x ADTR1107) on the ADAR1000EVAL1Z board. All tests were conducted at 10 GHz RF Frequency. The Tx output was combined using a 4:1 combiner and feed into a :adi:`adl6010` envelope detector. The detector Vout was connected to the high impedance input of an oscilloscope. The oscilloscope trigger signal was the TR pin of the ADAR1000.

Pulse characteristics are a 1 kHz pulse repetition frequency with a 50 us pulse width (5% duty cycle).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_rxtx_m25dbm_input.png
   :align: center

.. container:: centeralign

   \ **Figure 11: Rx-Tx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -25 dBm Input Power**\


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_txrx_m25dbm_input.png
   :align: center

.. container:: centeralign

   \ **Figure 12: Tx-Rx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -25 dBm Input Power**\


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_rxtx_m7dbm_input_200nsdiv.png
   :align: center

.. container:: centeralign

   \ **Figure 13: Rx-Tx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -7 dBm Input Power**\


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_txrx_m7dbm_input_200nsdiv.png
   :align: center

.. container:: centeralign

   \ **Figure 14: Tx-Rx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -7 dBm Input Power**\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_tx_spars_maxgain.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_tx_nf_over_gain.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_tx_oip3_maxgain.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_tx_p1db_maxgain.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_tx_poutvspin_maxgain.png
   :width: 600px
