ADALM2000 Marketing Collateral
==============================

Just click on any picture to see the full size image.

================================ ====== =========
Description                      Format Rev D
================================ ====== =========
Picture of ADALM2000             JPG

|image1|

Animation of all layers of Rev C GIF

|image2|

Layer 1 (SIG)                    png

|image3|

Layer 2 (GND)                    png

|image4|

Layer 3 (PWR)                    png

|image5|

Layer 4 (GND)                    png

|image6|

Layer 5 (SIG)                    png

|image7|

Layer 6 (SIG)                    png

|image8|

Layer 7 (GND)                    png

|image9|

Layer 8 (PWR)                    png

|image10|

Layer 9 (GND)                    png

|image11|

Layer 10 (SIG)                   png

|image12|

================================ ====== =========

Scripts
=======

because I need to look this up every time (since we do it so infrequent):

::

   $ for i in $(ls layer*.png) ; do echo $i ; convert $i -crop 2575x1600+128+252 +repage -transparent white  plutosdr_${i} ; done
   $ convert -delay 150 -loop 0 plutosdr_layer*.png animatedGIF.gif

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/devs/m2k_50034.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/final_m2k_gif.gif
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/layer1_m2k.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/layer2_m2k.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/layer3_m2k.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/layer4_m2k.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/layer5_m2k.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/m2k/layer6_m2k.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/m2k/layer7_m2k.png
   :width: 300px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/m2k/layer8_m2k.png
   :width: 300px
.. |image11| image:: https://wiki.analog.com/_media/university/tools/m2k/layer9_m2k.png
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/university/tools/m2k/layer10_m2k.png
   :width: 300px
