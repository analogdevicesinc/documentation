IIO OSC AD9371 Capture Window
=============================

Introduction
------------

Main receivers RX1 and RX2 are handled by the axi-ad9371-rx-hpc IIO device,
while the observation is handled by the axi-ad9371-rx-obs-hpc device. Splitting
into two devices was necessary since RX and OBS may run at different baseband
rates.

Channels:

===================== ===================== =====================
\                     Receiver Inputs       
===================== ===================== =====================
IIO Device Channels   voltage0_i voltage0_q voltage1_i voltage1_q
axi-ad9371-rx-hpc     RX1                   RX2
axi-ad9371-rx-obs-hpc OBS RX1               
===================== ===================== =====================

Screenshots
-----------

.. image:: images/myk_cap_time.png
   :align: center
   :width: 600

.. image:: images/myk_cap_freq.png
   :align: center
   :width: 600
