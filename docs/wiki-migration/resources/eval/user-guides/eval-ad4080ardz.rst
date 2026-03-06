Fast Precision ADCs KWIK Lecture + Lab
======================================

General Description
-------------------

The Fast Precision ADCs Know-how with Integrated Knowledge (KWIK) Lecture and Lab is a training module regarding Precision Fast ADCs with integrated digital filters. It is a combination of a lecture and a hands-on activity to understand how to drive such fast precision ADC and how to take advantage of the digital filters for noise performance improvements and antialiasing filtering.

On one hand, it provides lecture materials around sampled data system, antialiasing, how to drive a SAR ADCs and how the challenges increase with speed, as well as how to use digital filters to help achieving optimal performance.

On the other hand, the hands-on activity allows the user to measure signals with the EVAL-AD4080ARDZ Arduino form factor eval board, using ADALM2000 to both generate signals and measure them in the oscilloscope, as well as capturing the data stream coming from the ADC and generate time domain and frequency domain visualizations. Using IIO it also allows to configure the 20-bit 40-MSPS SAR ADC (AD4080) in order to check the benefits of the different digital filter option available.

Objective
---------

The Fast Precision ADCs KIWIK Lecture and Lab aims to understand the easy drives features on fast precision ADCs, as well as the benefits of using the digital filtering options available on-chip in the AD4080. Beyond theory slides, the user get to practice and play around with some physical hardware to see live all this options as well the impact on noise and antialiasing does the on-chip digital filter have.

Lecture Materials
-----------------

Theory slides: `seminar\_-\_adc\_-\_part_deaux.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/seminar_-_adc_-_part_deaux.pdf>`__

Step-by-step Hands on slide deck:`ad4080_hands_on.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/ad4080_hands_on.pdf>`__

ADALM2000 Active Learning Module and Scopy
------------------------------------------

:adi:`ADALM2000 Active Learning Module <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html>`

:doc:`Scopy - A Graphical User Interface (GUI) for the ADALM2000. A multi-functional software toolset with strong capabilities for signal analysis </wiki-migration/university/tools/m2k/scopy>`

ADALM2000 Configuration Files
-----------------------------

`m2k_and_ad4080_scopy_ini.zip <https://wiki.analog.com/_media/resources/eval/user-guides/m2k_and_ad4080_scopy_ini.zip>`__

LTSpice Simulation Circuits
---------------------------

`ad4080-signal-chain.zip <https://wiki.analog.com/_media/resources/eval/user-guides/ad4080-signal-chain.zip>`__

EVAL-AD4080ARDZ Demo PCB Image
------------------------------

**EVAL-AD4080ARDZ Angle View**


|image1|

**EVAL-AD4080ARDZ Top View**


|image2|

**EVAL-AD4080ARDZ Bottom View**


|image3|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4080ardz_angle-evaluation-board.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4080ardz_top-evaluation-board.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4080ardz_bottom-evaluation-board.jpg
   :width: 400px
