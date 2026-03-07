IIO OSC AD9081 Capture Window
=============================

Introduction
------------

Main receivers are handled by the axi-ad9081-rx-hpc IIO device, The number of channels depend on the JESD mode (M) parameter and can vary from case to case. When using complex IQ, two channels index by \_i and \_q from a receiver.

Screenshots
-----------

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_osc_time.png
   :align: center
   :width: 400px

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

|image1| |image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_osc_fft.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_osc_tone_fft.png
   :width: 400px
