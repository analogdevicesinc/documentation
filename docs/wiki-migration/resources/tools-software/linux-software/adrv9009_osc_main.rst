IIO OSC ADRV9009 Capture Window
===============================

Introduction
------------

Main receivers RX1 and RX2 are handled by the axi-adrv9009-rx-hpc IIO device, while the observation is handled by the axi-adrv9009-rx-obs-hpc device. Splitting into two devices was necessary since RX and OBS may run at different baseband rates.

Channels:

======================= ===================== =====================
\                       Receiver Inputs       
======================= ===================== =====================
IIO Device Channels     voltage0_i voltage0_q voltage1_i voltage1_q
axi-adrv9009-rx-hpc     RX1                   RX2
axi-adrv9009-rx-obs-hpc OBS RX1               OBS RX2
======================= ===================== =====================

Screenshots
-----------

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_TD_MAIN.png
   :align: center
   :width: 600px

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/ADRV9009_FD_MAIN.png
   :align: center
   :width: 600px
