.. _iio-oscilloscope adrv9009:

ADRV9009
========

Capture Window
--------------

Main receivers RX1 and RX2 are handled by the axi-adrv9009-rx-hpc IIO device,
while the observation is handled by the axi-adrv9009-rx-obs-hpc device.
Splitting into two devices was necessary since RX and OBS may run at different
baseband rates.

Channels:

======================= ===================== =====================
\                       Receiver Inputs
======================= ===================== =====================
IIO Device Channels     voltage0_i voltage0_q voltage1_i voltage1_q
axi-adrv9009-rx-hpc     RX1                   RX2
axi-adrv9009-rx-obs-hpc OBS RX1               OBS RX2
======================= ===================== =====================

Screenshots
+++++++++++

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: adrv9009_td_main.png

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: adrv9009_fd_main.png

Plugin
------

There are two plugins available for the ADRV9009:

.. toctree::
   :titlesonly:

   plugin
   advanced-plugin
