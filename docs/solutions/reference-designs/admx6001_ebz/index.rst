.. _admx6001_ebz:

EVAL-ADMX6001-EBZ
===============================================================================

DC-Coupled 10 GSPS Digitizer Evaluation Board.

.. image:: images/ADMX6001-EBZ_evaluation-board.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`ADMX6001-EBZ` is a dual-path digitizer evaluation board combining a
high-speed :adi:`AD9213` 12-bit ADC operating at 10 GSPS with a precision
:adi:`AD4080` 20-bit SAR ADC operating at 40 MSPS. This combination enables
low-noise signal acquisition from DC to 5 GHz.

The high-speed path uses the :adi:`ADL5580` differential amplifier driver for
the AD9213, while the :adi:`LTC2664` quad-channel DAC provides programmable DC
offset adjustment to maximize the AD9213 input dynamic range. The board
connects to an FPGA carrier via an FMC+ HSPC connector.

Features:

- High-speed path: :adi:`AD9213` 12-bit ADC at 10 GSPS with
  :adi:`ADL5580` driver
- Precision path: :adi:`AD4080` a 20-bit, 40MSPS, differential SAR ADC
  reduces 1/f noise
- Programmable DC offset: :adi:`LTC2664` DAC output adjusts DC offset
  to maximize AD9213 input dynamic range
- FMC+ HSPC connector for :xilinx:`VCU118` FPGA board connectivity
- Supports IIO Oscilloscope and Python (PyADI-IIO) software interfaces

Applications:

- Time-of-flight mass spectrometry
- Distributed fiber optic sensing
- Digital oscilloscopes
- Wideband signal capture and analysis

.. image:: images/eval_admx6001_ebz.png
   :align: center
   :width: 500

EVAL-ADMX6001-EBZ

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADMX6001-EBZ`, we recommend using the
evaluation board together with the :xilinx:`VCU118` FPGA carrier.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`admx6001 user-guide` — hardware guide for the evaluation board
   #. :ref:`Prerequisites <admx6001 prerequisites>` — what you need to get
      started
   #. :ref:`Quick start guides <admx6001 quickstart>`:

      #. Using the :ref:`VCU118/Virtex UltraScale+ <admx6001 quickstart vcu118>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+pyadi-iio:doc:`index`

#. Design with the ADMX6001

     - :adi:`AD9213 product page <AD9213>`
     - :adi:`AD4080 product page <AD4080>`
     - :adi:`LTC2664 product page <LTC2664>`
     - :adi:`ADL5580 product page <ADL5580>`

#. :ref:`Help and Support <help-and-support>`

ADI articles
-------------------------------------------------------------------------------

- :adi:`AD9213 Data Sheet <AD9213>`
- :adi:`AD4080 Data Sheet <AD4080>`
- :adi:`LTC2664 Data Sheet <LTC2664>`
- :adi:`ADL5580 Data Sheet <ADL5580>`

Videos
-------------------------------------------------------------------------------

- :adi:`ADMX6001: 10 GSPS Low-Noise Digitizer Evaluation Board
  <resources/media-center/videos/6387492087112.html>`
- :adi:`EVAL ADMX6001-EBZ DC-Coupled 10GSPS Digitizer Evaluation Board
  <resources/media-center/videos/6373904219112.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
