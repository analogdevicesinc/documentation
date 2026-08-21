.. _eval-ad7124-x:

EVAL-AD7124-x
===============================================================================

Evaluation Boards for the AD7124 Family of Low Noise, Low Power, 24-Bit,
Sigma-Delta ADCs with PGA and Reference

.. image:: images/AD7124-4-chip_image.webp
   :width: 150
   :height: 132
   :align: left
.. image:: images/AD7124-8-chip_image.webp
   :width: 150
   :height: 132
   :align: left

Overview
-------------------------------------------------------------------------------

The :adi:`AD7124-4` / :adi:`AD7124-8` are low power, low noise, completely
integrated analog front ends for high precision measurement applications. They
contain a low noise, 24-bit sigma-delta (Σ-Δ) analog-to-digital converter (ADC)
with an on-chip programmable gain amplifier (PGA), allowing small amplitude
signals to be interfaced directly to the ADC.

The :adi:`AD7124-4` and :adi:`AD7124-8` establish a high degree of signal
chain integration.
Each device contains a precision, low noise, low drift internal band gap
reference and also accepts an external differential reference, which can be
internally buffered. Additional integrated features include programmable low
drift excitation current sources, burnout currents, and a bias voltage
generator that sets the common-mode voltage of a channel to AVDD/2. A low-side
power switch enables bridge sensors to be powered down between conversions,
minimizing system power consumption. The devices support both internal and
external clock operation and can achieve simultaneous 50 Hz and 60 Hz rejection
at an output data rate of 25 SPS (single cycle settling), with rejection in
excess of 80 dB at lower output data rates.

Features:

- Low power, low noise, 24-bit sigma-delta ADC
- On-chip programmable gain amplifier (PGA)
- Three integrated power modes for flexible power/noise tradeoff
- Multiple filter options (sinc4, sinc3, fast settling, post filter)
- Integrated precision low drift reference
- Programmable excitation current sources and burnout detection
- Channel sequencer with up to 16 channels
- Per-channel configuration (8 setups)
- CRC diagnostics, SFF > 90% per IEC 61508
- SPI-compatible serial interface

Applications:

- Temperature Measurement
- Pressure Measurement
- Industrial Process Control
- Weigh Scales
- PLC/DCS Analog Input Modules

.. toctree::
   :hidden:

   eval-ad7124-4-8asdz/index
   eval-ad7124-4-8sdz/index
   eval-ad7124-8-pmdz/index
   quickstart/index
   prerequisites

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Evaluation boards and user guides:

   #. :ref:`eval-ad7124-8-pmdz_index` - EVAL-AD7124-8-PMDZ user guide
   #. :ref:`eval-ad7124-4-8sdz_index` - EVAL-AD7124-4SDZ / EVAL-AD7124-8SDZ
      user guide
   #. :ref:`eval-ad7124-4-8asdz_index` - EVAL-AD7124-4ASDZ /
      EVAL-AD7124-8ASDZ user guide
   #. :ref:`eval-ad7124-x prerequisites` - what you need to get started
   #. :ref:`eval-ad7124-x quickstart`:

      #. Using the :ref:`EVAL-ADICUP3029 <eval-ad7124-x quickstart adicup3029>`
      #. Using the :ref:`SDP-B <eval-ad7124-x quickstart sdp_b>`
      #. Using the :ref:`Nucleo-L476RG <eval-ad7124-x quickstart nucleo>`
      #. Using the :ref:`SDP-K1 <eval-ad7124-x quickstart sdp_k1>`

#. Design with the AD7124-4/AD7124-8

   - :ref:`eval-ad7124-x block-diagram`

     - :adi:`AD7124-4 product page <AD7124-4>`
     - :adi:`AD7124-8 product page <AD7124-8>`

   - Resources for designing a custom AD7124-based platform

     - :git-no-OS:`No-OS driver <drivers/adc/ad7124>`
     - :external+linux:ref:`ad7124` (Linux driver)

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad7124-x block-diagram:

Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/ad7124-8_functional_block_diagram.png
   :align: center

More Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD7124-4 Product Page <AD7124-4>`
- :adi:`AD7124-8 Product Page <AD7124-8>`

Support
-------------------------------------------------------------------------------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`EngineerZone forums <fpga>`.
