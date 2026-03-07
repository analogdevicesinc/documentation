ADALM-PLUTO Marketing Collateral
================================

Just click on any picture to see the full size image.

+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Description                              | Format | Rev B                                        | Rev D                                        |
+==========================================+========+==============================================+==============================================+
| Selfie of ADALM-PLUTO, cable and antenna | JPG    | |./marketing/adalm-pluto-photo.jpg|          | |./marketing/adalm-pluto-photo.jpg|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Selfie of ADALM-PLUTO, cable and antenna | PNG    | |./marketing/adalm-pluto-photo.png|          | |./marketing/adalm-pluto-photo.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Animation of all layers of Rev B         | GIF    | |./marketing/adalm-pluto_revb_alllayers.gif| | |./marketing/adalm-pluto_revd_alllayers.gif| |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 1 (SIG)                            | png    | |./marketing/layer1.png|                     | |./marketing/plutosdr_layer1_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 2 (GND)                            | png    | |./marketing/layer2.png|                     | |./marketing/plutosdr_layer2_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 3 (PWR)                            | png    | |./marketing/layer3.png|                     | |./marketing/plutosdr_layer3_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 4 (GND)                            | png    | |./marketing/layer4.png|                     | |./marketing/plutosdr_layer4_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 5 (SIG)                            | png    | |./marketing/layer5.png|                     | |./marketing/plutosdr_layer5_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 6 (SIG)                            | png    | |./marketing/layer6.png|                     | |./marketing/plutosdr_layer6_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 7 (GND)                            | png    | |./marketing/layer7.png|                     | |./marketing/plutosdr_layer7_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 8 (PWR)                            | png    | |./marketing/layer8.png|                     | |./marketing/plutosdr_layer8_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 9 (GND)                            | png    | |./marketing/layer9.png|                     | |./marketing/plutosdr_layer9_D.png|          |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+
| Layer 10 (SIG)                           | png    | |./marketing/layer10.png|                    | |./marketing/plutosdr_layer10_D.png|         |
+------------------------------------------+--------+----------------------------------------------+----------------------------------------------+

Scripts
=======

because I need to look this up every time (since we do it so infrequent):

::

   $ for i in $(ls layer*.png) ; do echo $i ; convert $i -crop 2575x1600+128+252 +repage -transparent white  plutosdr_${i} ; done
   $ convert -delay 150 -loop 0 plutosdr_layer*.png animatedGIF.gif

.. |./marketing/adalm-pluto-photo.jpg| image:: https://wiki.analog.com/_media/marketing/adalm-pluto-photo.jpg
   :width: 300px
.. |./marketing/adalm-pluto-photo.png| image:: https://wiki.analog.com/_media/marketing/adalm-pluto-photo.png
   :width: 300px
.. |./marketing/adalm-pluto_revb_alllayers.gif| image:: https://wiki.analog.com/_media/marketing/adalm-pluto_revb_alllayers.gif
   :width: 300px
.. |./marketing/adalm-pluto_revd_alllayers.gif| image:: https://wiki.analog.com/_media/marketing/adalm-pluto_revd_alllayers.gif
   :width: 300px
.. |./marketing/layer1.png| image:: https://wiki.analog.com/_media/marketing/layer1.png
   :width: 300px
.. |./marketing/plutosdr_layer1_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer1_D.png
   :width: 300px
.. |./marketing/layer2.png| image:: https://wiki.analog.com/_media/marketing/layer2.png
   :width: 300px
.. |./marketing/plutosdr_layer2_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer2_D.png
   :width: 300px
.. |./marketing/layer3.png| image:: https://wiki.analog.com/_media/marketing/layer3.png
   :width: 300px
.. |./marketing/plutosdr_layer3_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer3_D.png
   :width: 300px
.. |./marketing/layer4.png| image:: https://wiki.analog.com/_media/marketing/layer4.png
   :width: 300px
.. |./marketing/plutosdr_layer4_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer4_D.png
   :width: 300px
.. |./marketing/layer5.png| image:: https://wiki.analog.com/_media/marketing/layer5.png
   :width: 300px
.. |./marketing/plutosdr_layer5_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer5_D.png
   :width: 300px
.. |./marketing/layer6.png| image:: https://wiki.analog.com/_media/marketing/layer6.png
   :width: 300px
.. |./marketing/plutosdr_layer6_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer6_D.png
   :width: 300px
.. |./marketing/layer7.png| image:: https://wiki.analog.com/_media/marketing/layer7.png
   :width: 300px
.. |./marketing/plutosdr_layer7_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer7_D.png
   :width: 300px
.. |./marketing/layer8.png| image:: https://wiki.analog.com/_media/marketing/layer8.png
   :width: 300px
.. |./marketing/plutosdr_layer8_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer8_D.png
   :width: 300px
.. |./marketing/layer9.png| image:: https://wiki.analog.com/_media/marketing/layer9.png
   :width: 300px
.. |./marketing/plutosdr_layer9_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer9_D.png
   :width: 300px
.. |./marketing/layer10.png| image:: https://wiki.analog.com/_media/marketing/layer10.png
   :width: 300px
.. |./marketing/plutosdr_layer10_D.png| image:: https://wiki.analog.com/_media/marketing/plutosdr_layer10_D.png
   :width: 300px
