Filter response
===============

The following transmitter and receiver FIR filters were designed using the AD9361 Filter Design Wizard (for more information, consult the MATLAB Filter Design Wizard for AD9361 wiki page :doc:`/wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters`).

The response was measured on an AD-FMCOMMS3-EBZ using the bare-metal AD9361
software running in Linux user space, a spectrum analyzer and the ADI
VisualAnalog software.

Updated on October 20, 2015

+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Description                                                                                                                                                | Filter settings                                                                                                                 | TX Filter response | TX & RX Filter response |
+============================================================================================================================================================+=================================================================================================================================+====================+=========================+
| Sampl. Freq.: 232748 Hz LO Freq.: 70 MHz DDS Freq.: 70000 Hz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*   | `fir_232748.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_232748.zip>`_    | |image17|          | |image18|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 245760 Hz LO Freq.: 2415 MHz DDS Freq.: 70000 Hz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\* | `fir_245760.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_245760.zip>`_    | |image19|          | |image20|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 256000 Hz LO Freq.: 460 MHz DDS Freq.: 70000 Hz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*  | `fir_256e3.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_256e3.zip>`_      | |image21|          | |image22|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 15.360 MHz LO Freq.: 806 MHz DDS Freq.: 4 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*    | `fir_15.36e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_15.36e6.zip>`_  | |image23|          | |image24|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 15.360 MHz LO Freq.: 2450 MHz DDS Freq.: 4 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*   | `fir_15.36e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_15.36e6.zip>`_  | |image25|          | |image26|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 22 MHz LO Freq.: 2427 MHz DDS Freq.: 6 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*       | `fir_22e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_22e6.zip>`_        | |image27|          | |image28|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 50 MHz LO Freq.: 1000 MHz DDS Freq.: 12 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*      | `fir_50e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_50e6.zip>`_        | |image29|          | |image30|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 60 MHz LO Freq.: 4000 MHz DDS Freq.: 12 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*      | `fir_60e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_60e6.zip>`_        |                    | |image31|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+
| Sampl. Freq.: 61.44 MHz LO Freq.: 6000 MHz DDS Freq.: 12 MHz DDS Scale: 0.250 for each tone\* DDS Phase: 90 degrees for I tones, 0 degrees for Q tones\*   | `fir_61.44e6.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/fir_61.44e6.zip>`_  |                    | |image32|               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+--------------------+-------------------------+

\*Note: The DDS for a channel consists of two tones.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_232748_lo_70e6.png
   :width: 220
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_232748_lo_70e6.png
   :width: 200
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_245760_lo_2415e6.png
   :width: 220
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_245760_lo_2415e6.png
   :width: 200
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_256e3_lo_460e6.png
   :width: 220
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_256e3_lo_460e6.png
   :width: 200
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_15.36e6_lo_806e6.png
   :width: 220
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_15.36e6_lo_806e6.png
   :width: 200
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_15.36e6_lo_2450e6.png
   :width: 220
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_15.36e6_lo_2450e6.png
   :width: 200
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_22e6_lo_2427e6.png
   :width: 220
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_22e6_lo_2427e6.png
   :width: 200
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_50e6_lo_1000e6.png
   :width: 220
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_50e6_lo_1000e6.png
   :width: 200
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_60e6_lo_4000e6.png
   :width: 200
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_61.44e6_lo_6000e6.png
   :width: 200
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_232748_lo_70e6.png
   :width: 220
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_232748_lo_70e6.png
   :width: 200
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_245760_lo_2415e6.png
   :width: 220
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_245760_lo_2415e6.png
   :width: 200
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_256e3_lo_460e6.png
   :width: 220
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_256e3_lo_460e6.png
   :width: 200
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_15.36e6_lo_806e6.png
   :width: 220
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_15.36e6_lo_806e6.png
   :width: 200
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_15.36e6_lo_2450e6.png
   :width: 220
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_15.36e6_lo_2450e6.png
   :width: 200
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_22e6_lo_2427e6.png
   :width: 220
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_22e6_lo_2427e6.png
   :width: 200
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/tx_50e6_lo_1000e6.png
   :width: 220
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_50e6_lo_1000e6.png
   :width: 200
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_60e6_lo_4000e6.png
   :width: 200
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/filter/trx_61.44e6_lo_6000e6.png
   :width: 200
