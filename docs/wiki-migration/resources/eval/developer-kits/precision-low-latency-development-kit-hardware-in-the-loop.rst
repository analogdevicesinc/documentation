Precision Low Latency Development Kit(Hardware in the Loop)
===========================================================

HiL simulation system provides high precision and low latency solutions to solve the challenge of testing and verifying complex real-time systems (e.g. electronic control units)

Features
========

Precision Low-Latency Reference Design state-of-the-art HW for low latency and settling

::

   *16-bits resolution
   *4x differential analog input, ±10V
     *70ns analog latency (acquisition + data transfer)
     *±60 V Analog protection
     *Customizable analog input filter
     *Fully buffered, ADA4898-1
     *Low drift VREF, LTC6655
   *4x single ended analog output, ±10V
     *130ns analog latency (data transfer + low signal settling time)
     *±60 V Analog protection
     *Fully buffered, AD8065
     *Customizable analog output filter with cable compensation
     *Low drift VREF, ADR4525

Performance
===========

+-------------------------+---------------------------------------+-------------------------------------+
| Specification           | Value                                 | Comment                             |
+=========================+=======================================+=====================================+
| Resolution              | 16-bits                               |                                     |
+-------------------------+---------------------------------------+-------------------------------------+
| Input range             | ±10V Differential input               | ±60V protection                     |
+-------------------------+---------------------------------------+-------------------------------------+
| Output range            | ±10V Single ended output              | ±60V protection                     |
+-------------------------+---------------------------------------+-------------------------------------+
| Analog Latency          | 220ns                                 | @15Msps sample ; @15Mups generation |
+-------------------------+---------------------------------------+-------------------------------------+
| Analog settling time    | 70ns small signal; 200ns large signal |                                     |
+-------------------------+---------------------------------------+-------------------------------------+
| Analog signal bandwidth | 7MHz                                  |                                     |
+-------------------------+---------------------------------------+-------------------------------------+

Benefits
========

-  Unordered List ItemIndustry leading accuracy, minimizing both latency and error
-  System evaluation in minutes with plug and play hardware

System Integration
==================

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/hil-1.png
   :width: 600px

Key Component Locations
-----------------------

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/hil-2.png
   :width: 600px

Related Documents
=================

Publications
------------

:adi:`Hardware in the Loop (HIL) <en/applications/markets/instrumentation-and-measurement-pavilion-home/automotive-testing-solutions/hardware-in-the-loop.html>`

:adi:`Physical Measurements to Actionable Data - Solutions for Inertial, Optical, Capacitance, Temperature, ADCs and more <en/education/education-library/videos/6296622444001.html>`

:adi:`The On-Chip Calibration Benefits of New Simultaneous SAR Analog-to-Digital Converters <en/technical-articles/new-simultaneous-sar-adcs.html>`

:adi:`Step-by-Step Noise Analysis Guide for Your Signal Chain <en/analog-dialogue/articles/step-by-step-noise-analysis-guide-for-your-signal-chain.html>`

Related part pages
------------------

:adi:`ADAQ23876 <en/products/adaq23876.html>` 16-Bit, 15 MSPS, μModule Data Acquisition Solution

:adi:`AD3552R <en/products/ad3552r.html>` Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI DAC

:adi:`ADG5421F <en/products/adg5421f.html>` ±60 V Fault Protection and Detection, 11 Ω RON, Dual SPST Switch

:adi:`ADA4898-1 <en/products/ada4898-1.html>` High Voltage, Low Noise, Low Distortion, Unity Gain Stable, High-Speed Op Amp

Questions
=========

For additional questions or support, please visit the Engineering Zone forum at
