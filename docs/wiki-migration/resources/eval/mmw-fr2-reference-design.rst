mmW FR2 Reference Design for Wireless Test
==========================================

The need for ubiquitous connectivity, high speed data, wide bandwidth streaming is driving newer wireless technologies like 5G, 6G, Wi-Fi 7 & 8 and UWB. As these newer standards emerge, the testing complexity is also increasing such as wider bandwidths, higher frequencies, complex modulations, higher dynamic range. Instrumentation customers are seeking solutions that tame their measurement challenges, shorten their development times, and provide the highest performance.

ADI’s mmW FR2 Radio Front End (RFFE) reference design aims to address these challenges for Test and Measurement customers. It supports frequencies from 18-55GHz and instantaneous bandwidths up to 8GHz. The FR2 RFFE includes TX and RX modes for signal generation and spectrum analysis applications respectively. Each TX & RX path have a dedicated LO inputs to support TDD and FDD operation.

The FR3 reference design uses ADI’s latest RF signal conditioning solutions such as the ADMV1355 Intergrated Up-Converter, ADMV1455 Integrated Down-Converter, ADL8106 LNA, ADPA7009 Power Amplifier and ADRF5740 Digital Attenuators. The design also includes other critical functions of clocking and power management to simply customer implementation.

The RFFE is agnostic to the data converter used; however, it is recommended to use ADI’s MxFE data converter solutions. The measurements shown in the ensuing section uses the Apollo MxFE ADC and DAC.

18-55 GHz RF Front-End Design includes complete TX and RX signal chains with 4 GHz of iBW. The design supports both 5G/6G signal generation and spectrum analyzer/demodulator. I/Q IF ports are provided for TX inputs and RX has a single IF output. TX and RX each have their own output/input 1.85mm interface connector. both TX and RX each have dedicated LO inputs to support FDD or TDD operation.

Evaluation Kit
--------------

-  18-55 GHz (FR2) mmW Front-End Board
-  Universal AC power adapter, 12 VDC Output
-  Raspberry Pi board with SD card for FR2 board SPI/i2c programming.
-  GUI is preloaded on SD card.

Additional Equipment Required
-----------------------------

-  26 GHz Signal Source for LO
-  TX I/Q IF stimulus, DC to 2.8 GHz.
-  RF source for RX input
-  Spectrum Analyzer or demodulator at RX IF output

Product Overview
----------------

-  RF carriers 18 GHz to 55 GHz
-  Supports up to 4 GHz iBW
-  2x LO multiplier with harmonic reject filter
-  EVM < –45 dB
-  TX Gain:

   -  Low Band (18-34 GHz): 47 dB
   -  High Band (30-55 GHz): 41 dB

-  TX OP1dB:

   -  Low Band (18-34 GHz): 23 dB
   -  High Band (30-55 GHz): 19 dB

-  TX OIP3:

   -  Low Band (18-34 GHz): 32 dB
   -  High Band (30-55 GHz): 28 dB

-  TX Attn control: 44 dB
-  TX and RX digitally tunable filters for Image and spur rejection
-  RX Gain:

   -  Low Band (18-34 GHz): 67 dB
   -  High Band (30-55 GHz): 55 dB

-  RX Noise Figure:

   -  Low Band (18-34 GHz): 5 dB
   -  High Band (30-55 GHz): 8 dB

-  RX Attn control: 22 dB
-  Includes temperature sensors for calibration over temperature
-  Design is SPI/i2c programable
-  Includes power management

Key RF Components
~~~~~~~~~~~~~~~~~

-  ADMV1355 Integrated mmW Up-Converter
-  ADMV1455 Integrated mmW Down-Converter
-  ADL8106 LNA/Driver Amplifier
-  ADPA7009 0.5W Power Amplifier
-  ADRF5740 Digital Attenuator

Block Diagram
~~~~~~~~~~~~~

|image1| //

*====FR2 Board==== *

//

TX Performance Data
~~~~~~~~~~~~~~~~~~~

|image2| |image3|

//

//

RX Performance Data
~~~~~~~~~~~~~~~~~~~

|image4| |image5|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/fr2_diagram_for_wiki.jpg
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/fr2_TX_Gain.jpg
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/fr2_TX_p1db.jpg
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/fr2_RX_Gain.jpg
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/fr2_RX_NF.jpg
   :width: 500px
