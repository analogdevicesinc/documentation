.. _fmcomms2 software baremetal-filter:

Filter response
===============================================================================

The following transmitter and receiver FIR filters were designed using the
AD9361 Filter Design Wizard (for more information, consult the
:ref:`MATLAB Filter Design Wizard for AD9361 wiki page <fmcomms2 software filters>`).

The response was measured on an AD-FMCOMMS3-EBZ using the bare-metal AD9361
software running in Linux user space, a spectrum analyzer and the ADI
VisualAnalog software.

Updated on October 20, 2015

.. list-table::
   :header-rows: 1
   :widths: 40 20 20 20

   * - Description
     - Filter settings
     - TX Filter response
     - TX & RX Filter response
   * - | Sampl. Freq.: 232748 Hz
       | LO Freq.: 70 MHz
       | DDS Freq.: 70000 Hz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_232748.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_232748.zip>`
     - |tx-232748-70|
     - |trx-232748-70|
   * - | Sampl. Freq.: 245760 Hz
       | LO Freq.: 2415 MHz
       | DDS Freq.: 70000 Hz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_245760.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_245760.zip>`
     - |tx-245760-2415|
     - |trx-245760-2415|
   * - | Sampl. Freq.: 256000 Hz
       | LO Freq.: 460 MHz
       | DDS Freq.: 70000 Hz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_256e3.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_256e3.zip>`
     - |tx-256e3-460|
     - |trx-256e3-460|
   * - | Sampl. Freq.: 15.360 MHz
       | LO Freq.: 806 MHz
       | DDS Freq.: 4 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_15.36e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_15.36e6.zip>`
     - |tx-15.36e6-806|
     - |trx-15.36e6-806|
   * - | Sampl. Freq.: 15.360 MHz
       | LO Freq.: 2450 MHz
       | DDS Freq.: 4 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_15.36e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_15.36e6.zip>`
     - |tx-15.36e6-2450|
     - |trx-15.36e6-2450|
   * - | Sampl. Freq.: 22 MHz
       | LO Freq.: 2427 MHz
       | DDS Freq.: 6 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_22e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_22e6.zip>`
     - |tx-22e6-2427|
     - |trx-22e6-2427|
   * - | Sampl. Freq.: 50 MHz
       | LO Freq.: 1000 MHz
       | DDS Freq.: 12 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_50e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_50e6.zip>`
     - |tx-50e6-1000|
     - |trx-50e6-1000|
   * - | Sampl. Freq.: 60 MHz
       | LO Freq.: 4000 MHz
       | DDS Freq.: 12 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_60e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_60e6.zip>`
     -
     - |trx-60e6-4000|
   * - | Sampl. Freq.: 61.44 MHz
       | LO Freq.: 6000 MHz
       | DDS Freq.: 12 MHz
       | DDS Scale: 0.250 for each tone\*
       | DDS Phase: 90° for I tones, 0° for Q tones\*
     - :dokuwiki:`fir_61.44e6.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_61.44e6.zip>`
     -
     - |trx-61.44e6-6000|

.. note::

   \* The DDS for a channel consists of two tones.

.. |tx-232748-70| image:: ../../images/tx_232748_lo_70e6.png
   :width: 220
.. |trx-232748-70| image:: ../../images/trx_232748_lo_70e6.png
   :width: 200
.. |tx-245760-2415| image:: ../../images/tx_245760_lo_2415e6.png
   :width: 220
.. |trx-245760-2415| image:: ../../images/trx_245760_lo_2415e6.png
   :width: 200
.. |tx-256e3-460| image:: ../../images/tx_256e3_lo_460e6.png
   :width: 220
.. |trx-256e3-460| image:: ../../images/trx_256e3_lo_460e6.png
   :width: 200
.. |tx-15.36e6-806| image:: ../../images/tx_15.36e6_lo_806e6.png
   :width: 220
.. |trx-15.36e6-806| image:: ../../images/trx_15.36e6_lo_806e6.png
   :width: 200
.. |tx-15.36e6-2450| image:: ../../images/tx_15.36e6_lo_2450e6.png
   :width: 220
.. |trx-15.36e6-2450| image:: ../../images/trx_15.36e6_lo_2450e6.png
   :width: 200
.. |tx-22e6-2427| image:: ../../images/tx_22e6_lo_2427e6.png
   :width: 220
.. |trx-22e6-2427| image:: ../../images/trx_22e6_lo_2427e6.png
   :width: 200
.. |tx-50e6-1000| image:: ../../images/tx_50e6_lo_1000e6.png
   :width: 220
.. |trx-50e6-1000| image:: ../../images/trx_50e6_lo_1000e6.png
   :width: 200
.. |trx-60e6-4000| image:: ../../images/trx_60e6_lo_4000e6.png
   :width: 200
.. |trx-61.44e6-6000| image:: ../../images/trx_61.44e6_lo_6000e6.png
   :width: 200
