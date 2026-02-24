.. _ad-fmcdaq2-ebz card_specification:

AD-FMCDAQ2-EBZ Specifications
==============================

Transmit Specs
--------------

120 MHz FFT
~~~~~~~~~~~

.. list-table::
   :header-rows: 0

   * - .. image:: cha_120mhz_fft.png
     - .. image:: chb_120mhz_fft.png
   * - Channel A 120 MHz tone, full scale, FFT
     - Channel B 120 MHz tone, full scale, FFT

Phase Noise
~~~~~~~~~~~

.. list-table::
   :header-rows: 0

   * - .. image:: cha_40mhz_pn.png
     - .. image:: chb_40mhz_pn.png
   * - Channel A 40 MHz tone, full scale, phase noise
     - Channel B 40 MHz tone, full scale, phase noise
   * - .. image:: cha_120mhz_pn.png
     - .. image:: chb_120mhz_pn.png
   * - Channel A 120 MHz tone, full scale, phase noise
     - Channel B 120 MHz tone, full scale, phase noise

Receive Specs
-------------

SNR
~~~

.. figure:: snrfs.png

   SNR sweep from 60 MHz to 550 MHz with full scale input.

SFDR
~~~~

.. list-table::
   :header-rows: 0

   * - .. image:: sfdr.png
     - .. image:: sfdr_eval_brd.png
   * - SFDR sweep from 60 MHz to 550 MHz with full power input.
     - SFDR sweep compared to Eval board with AD9523-1 reference clock
