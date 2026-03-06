BOM Improvements
================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Transmit Path
-------------

+-----------------------------------------------------------------------------------------------------------------------------------------------+


| Changing the ADF4351 output filter by changing the values of L17 and L18 from 3.9nH to 10nH will remove the Notch at 450 MHz when sweeping LO |

+===+
| |image1|                                                                                                                                      |
+---+

| The location of these components on the board is highlighted in this figure                                                                   |

+---+
| |image2|                                                                                                                                      |
+---+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


| Changing the loop filter of the ADF4351 by changing the component values as shown in this figure, will improve the phase noise by about 20 dB up to 1MHz within the whole range except between 2.14GHz and 2.19GHz |

+===+
| |image3|                                                                                                                                                                                                           |
+---+

| The location of these components on the board is highlighted in this figure                                                                                                                                        |

+---+
| |image4|                                                                                                                                                                                                           |
+---+

| Here is the phase noise we get with these changes around 2.19GHz                                                                                                                                                   |

+---+
| |image5|                                                                                                                                                                                                           |
+---+

Receive Path
------------

+-----------------------------------------------------------------------------------------------------------------------------------------------+


| Changing the ADF4351 output filter by changing the values of L22 and L23 from 3.9nH to 10nH will remove the Notch at 650 MHz when sweeping LO |

+===+
| |image6|                                                                                                                                      |
+---+

| The location of these components on the board is highlighted in this figure                                                                   |

+---+
| |image7|                                                                                                                                      |
+---+

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Changing the loop filter of the ADF4351 by changing the component values as shown in this figure, will improve the phase noise throughout the whole range except between 2.11GHz and 2.19GHz |           |
+==============================================================================================================================================================================================+===========+
| |image12|                                                                                                                                                                                    |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| The location of these components on the board is highlighted in these two figure                                                                                                             |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| |image13|                                                                                                                                                                                    | |image14| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Here is the phase noise we get with these changes around 2.19GHz                                                                                                                             |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| |image15|                                                                                                                                                                                    |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

+----------------------------------------------------------------------------------------------------------------------------------+


| Removing the ADL5380 output filter by removing the capacitors C115, C116, C142 and C143 will increase the receive path bandwidth |

+===+
| |image16|                                                                                                                        |
+---+

| The location of these components on the board is highlighted in this figure                                                      |

+---+
| |image17|                                                                                                                        |
+---+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+


| Removing R56 and making R55 200 Ohms will set the output common mode voltage of the ADL5380 to 2.3V which is in the input common mode range of the AD8366 |

+===+
| |image18|                                                                                                                                                 |
+---+

| The location of these components on the board is highlighted in this figure                                                                               |

+---+
| |image19|                                                                                                                                                 |
+---+

+-------------------------------------------------------------------------------------------------------------+


| Replacing R51, R57, R66 and R70 with an 82.5 Ohms will set the input common mode voltage of the ADC to 0.9V |

+===+
| |image20|                                                                                                   |
+---+

| The location of these components on the board is highlighted in this figure                                 |

+---+
| |image21|                                                                                                   |
+---+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_tx_l17_18.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_l17_18_22_23.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_tx_R40_42_C81_86_92.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_R40_42_C81_86_92.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_2.19_ghz_tx_lo_40mhz_tone_1.png
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_l22_23.png
   :width: 200px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_l17_18_22_23.png
   :width: 200px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_R48_108_C110_113_263.png
   :width: 200px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_R48_C110_113.png
   :width: 200px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/top_r108_c263.png
   :width: 200px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/lo_instability_rx_lo_2.19ghz.png
   :width: 200px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_R48_108_C110_113_263.png
   :width: 200px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_R48_C110_113.png
   :width: 200px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/top_r108_c263.png
   :width: 200px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/lo_instability_rx_lo_2.19ghz.png
   :width: 200px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_c115_116_142_143.png
   :width: 200px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_c115_116_142_143.png
   :width: 200px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_r55_56.png
   :width: 200px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_r55_56.png
   :width: 200px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ppp_rx_r51_57_66_70.png
   :width: 200px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bottom_r51_57_66_70.png
   :width: 200px
