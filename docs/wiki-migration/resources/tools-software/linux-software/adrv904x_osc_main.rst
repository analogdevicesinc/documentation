IIO OSC ADRV904x Capture Window
===============================

Introduction
------------

Main receivers RX1, RX2, RX3, RX4, RX5, RX6, RX7 and RX8 are handled by the axi-adrv904x-rx-hpc IIO device.

Channels:

=================== ===================== === =====================
\                   Receiver Inputs           
=================== ===================== === =====================
IIO Device Channels voltage0_i voltage0_q ... voltage7_i voltage7_q
axi-adrv9009-rx-hpc RX1                   ... RX8
=================== ===================== === =====================

Screenshots
-----------

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/adrv904x_osc_time_domain.png
   :align: center
   :width: 600px

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/adrv904x_osc_freq_domain.png
   :align: center
   :width: 600px
