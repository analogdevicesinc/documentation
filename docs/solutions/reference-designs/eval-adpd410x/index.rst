.. _eval_adpd410x eval:

EVAL-ADPD410X-ARDZ
==================

ADPD4100/ADPD4101 Arduino Shields

.. figure:: EVAL-ADPD4100-ARDZ_ANGLE-evaluation-board.jpg
   :align: center
   :width: 600 px
   :alt: EVAL-ADPD410x-ARDZ

Overview
--------

:adi:`EVAL-ADPD4100-ARDZ <EVAL-ADPD410x-ARDZ>` and :adi:`EVAL-ADPD4101-ARDZ <EVAL-ADPD410x-ARDZ>` 
are simple, Arduino form-factor breakout board for developing :adi:`ADPD4100` and :adi:`ADPD4101` 
applications, respectively. The ADPD4101, interfaced through I2C, and the ADPD4100, 
interfaced through SPI, are highly versatile, multimodal sensor front ends, 
stimulating up to eight light emitting diodes (LEDs) and measuring 
the return signal on up to eight separate current inputs. 

There are a number of other evaluation platforms for these devices, 
including the :adi:`EVAL-ADPD4100Z-PPG`, optimized for photoplethysmograph applications, 
and the reference design :adi:`CN0503`, optimized for optical liquid analysis applications 
(colorimetry, turbidity, fluorescence). The :adi:`EVAL-ADPD410X-ARDZ` boards come in handy 
for adapting these evaluation boards to meet specific application requirements, 
as well as for "ground up" development of new applications.

Features
--------

- On-board LED for quick and easy bring up
- Breakaway Prototyping Board for customized application needs 
- 8-Channels of LEDs and photodiodes connections
- Standard 0.1 inch headers 

Applications
------------

- Wearable health and fitness monitors: heart rate monitors (HRMs),
  heart rate variability (HRV), stress, blood pressure 
  estimation, SpO2, hydration, body composition 
- Industrial monitoring: CO, CO2, smoke, and aerosol detection 
- Home patient monitoring 

.. admonition:: Getting Started

   The :adi:`EVAL-ADPD410x-ARDZ` can be used for a wide range of applications, 
   and the following demos are meant to show examples of the flexibility of the board. 
   To get started with setup, configuration, and example use cases, 
   please proceed to the Quick Start Guide and follow the provided demo pages.

   - :doc:`Quick Start Guide </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`
   - :ref:`Fluorescence Demo <eval_adpd410x fluorescence_demo>`
   - :ref:`Turbidity Demo <eval_adpd410x turbidity_demo>`

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ez:`Analog Devices EngineerZone <Reference Designs>` forum, but before that, 
please make sure you read our documentation thoroughly.

Warning
-------

.. esd-warning::

Help and support
----------------

Please go to :ez:`Analog Devices EngineerZone <Reference Designs>` page.

.. toctree::
   :hidden:

   eval-adpd410x
   fluorescence
   turbidity
