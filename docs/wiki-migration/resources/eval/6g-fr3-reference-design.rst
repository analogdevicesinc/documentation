6G FR3 Reference Design for Wireless Test
=========================================

The need for ubiquitous connectivity, high speed data, wide bandwidth streaming is driving newer wireless technologies like 6G, Wi-Fi 7 & 8 and UWB. As these newer standards emerge, the testing complexity is also increasing such as wider bandwidths, higher frequencies, complex modulations, higher dynamic range. Instrumentation customers are seeking solutions that tame their measurement challenges, shorten their development times, and provide the highest performance.

ADI’s 6G FR3 Radio Front End (RFFE) reference design aims to address these challenges for Test and Measurement customers. It supports frequencies from 6-18GHz and instantaneous bandwidths up to 4GHz. The FR3 RFFE includes TX and RX modes for signal generation and spectrum analysis applications respectively. Each TX & RX path have a dedicated LO inputs to support TDD and FDD operation.

The FR3 reference design uses ADI’s latest RF signal conditioning solutions such as the HMC8191 IQ Mixer, ADMV8818 Tunable Filter, wideband distributed driver amplifiers along with RF switching and attenuation. The design also includes other critical functions of clocking and power management to simply customer implementation.

The RFFE is agnostic to the data converter used; however, it is recommended to use ADI’s MxFE data converter solutions. The measurements shown in the ensuing section uses the Apollo MxFE ADC and DAC.

6-18 GHz RF Front-End Design includes complete TX and RX signal chains with 4 GHz of iBW. The design supports both 5G/6G signal generation and spectrum analyzer/demodulator. I/Q IF ports are provided for TX inputs and RX outputs, there's a common RF input/output interface connector. both TX and RX each have dedicated LO inputs to support FDD or TDD operation.

Evaluation Kit
--------------

-  6-18 GHz (FR3) RF Front-End Board
-  Universal AC power adapter, 12 VDC Output
-  Raspberry Pi board with SD card for FR3 board SPI/i2c programming.
-  GUI is preloaded on SD card.

Additional Equipment Required
-----------------------------

-  18 GHz Signal Source for LO
-  TX I/Q IF stimulus, DC to 2.8 GHz.
-  RF source for RX input
-  Spectrum Analyzer or demodulator at RX I/Q IF output

Product Overview
----------------

-  RF carriers 6 GHz to 18 GHz
-  Supports up to 4 GHz iBW
-  EVM < –50 dB
-  TX Gain: 28 dB
-  TX P1dB: 27 dBm
-  TX OIP3: 40 dBm
-  TX Attn control: 130 dB in 0.5 dB steps
-  Transmitter LO nulling capability
-  TX Directional Coupler for TX to RX Loopback
-  TX and RX digitally tunable filters for Image and spur rejection
-  RX Gain: 70 dB
-  RX Noise Figure: 4 dB
-  RX Attn control: 65 dB in 0.5 dB steps
-  Includes temperature sensors for calibration over temperature
-  Design is SPI/i2c programable
-  Includes power management

Key RF Components
~~~~~~~~~~~~~~~~~

-  RF Mixer: HMC8191
-  Tunable Filter: ADMV8818
-  LO Driver: ADL8105

Block Diagram
~~~~~~~~~~~~~

|image1| //

//

FR3 Board
~~~~~~~~~

TX Performance Data
-------------------

|image2| |image3| //

|image4| |image5| //

RX Performance Data with LNA Enabled
------------------------------------

|image6| |image7| //

|image8| |image9| //

RX Performance Data with LNA Bypassed
-------------------------------------

|image10| |image11| //

|image12| //

TX EVM Data
-----------

::

   -802.11ax 80MHz 1024QAM waveform
   -Output Power:  +5.0 dBm
   -EVM: < -50dB

.. image:: https://wiki.analog.com/_media/resources/eval/fr3_tx_evm.jpg
   :width: 800px

RX EVM Data
-----------

-  5G-NR 100 MHz 256QAM waveform
-  EVM: < -49dB

.. image:: https://wiki.analog.com/_media/resources/eval/fr3_rx_evm.jpg
   :width: 800px

//

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/fr3_block_diagram.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/tx_gain.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/tx_op1db-1.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/tx_oip3-1.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/tx_gain_vs_attn.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/rx_gain_with_lna.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/rx_ip1db_with_lna.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/rx_nf_with_lna_enabled.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/rx_attn_with_lna.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/rx_gain_with_lna_bypassed.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/rx_ip1db_with_lna.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/rx_attn_with_lna_bypassed.jpg
   :width: 400px
