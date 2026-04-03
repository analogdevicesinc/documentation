.. _eval-ad4134-fmcz:

EVAL-AD4134FMCZ
===============

24-Bit, 4-Channel Simultaneous Sampling 1.5 MSPS Precision Alias Free ADC

.. image:: images/ad4134_chip.png
   :align: left
   :width: 100

Overview
--------

The :adi:`AD4134` is a quad channel, low noise, simultaneous sampling, precision
analog-to-digital converter (ADC), based on the continuous time sigma-delta
(CTSD) modulation scheme. This technology does not use sample-and-hold circuitry
to alleviate the side effects introduced by it, like charge kickback and signal
aliasing. This inherent alias rejection is up to 100 dB.

The device provides four independent converter channels with freely programmable
data rates from 0.01 kSPS up to 1496 kSPS and maximum input bandwidth of
391.5 kHz. An asynchronous sample rate converter is used to synchronize two
or more devices using only a signal line.

It has excellent AC and DC performance with 107.5 dB dynamic range for the FIR
filter and 111 dB SNR. The offset drift is 1.5 uV/C, gain drift of 2 ppm/C
and INL of +/-2.5 ppm.

It can be powered from a 4.5 V to 5.5 V power supply and a 1.65 V to 1.95 V
digital power supply for 1.8 V I/O level. It can have external voltage
reference of 2.5 V, 4.096 V and 5 V and a crystal or CMOS external clock of
48 MHz. The device can be configured and controlled by GPIOs or SPI. It has
temperature operating range between -40 C and +125 C.

Features:

-  24-bit, 4-channel simultaneous sampling ADC
-  Throughput of up to 1496 kSPS per channel
-  Alias-free continuous time sigma-delta modulation (up to 100 dB rejection)
-  Freely programmable data rates from 0.01 kSPS to 1496 kSPS
-  Maximum input bandwidth of 391.5 kHz
-  Asynchronous sample rate converter for multi-device synchronization
-  SPI or GPIO configuration and control

Applications:

-  Electrical test and measurement
-  Audio test
-  3-phase power quality analysis
-  Control and hardware in loop verification
-  Sonar
-  Condition monitoring for predictive maintenance
-  Acoustic and material science research and development

.. figure:: images/ad4134_eval_board.png
   :align: center
   :width: 400

   EVAL-AD4134FMCZ evaluation board

.. toctree::
   :hidden:

   user-guide
   quickstart/index
   prerequisites

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD4134`, we recommend to use the
:adi:`EVAL-AD4134FMCZ` evaluation board.

Table of contents
-----------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad4134-fmcz prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-ad4134-fmcz quickstart>`:

      #. Using the :ref:`Zedboard / Zynq-7000 SoC
         <eval-ad4134-fmcz quickstart zed>`

   #. Configure an SD Card with
      :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD4134

   #. HDL reference design

      #. :external+hdl:ref:`HDL reference design <ad4134_fmc>` which
         you must use in your FPGA.
      #. :git-hdl:`AD4134 HDL Reference Design
         <projects/ad4134_fmc>` which you must use in your FPGA.

   #. More information

      #. :external+hdl:ref:`SPI Engine Framework <spi_engine>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad4134-fmcz block-diagram:

Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/ad4134_block_diagram.png
   :width: 1000

   AD4134 functional block diagram

Additional Information and Useful Links
---------------------------------------

-  :adi:`AD4134 Product Page <AD4134>`
-  :adi:`EVAL-AD4134FMCZ Evaluation Board <EVAL-AD4134FMCZ>`
-  :adi:`AD4134 Data Sheet
   <media/en/technical-documentation/data-sheets/ad4134.pdf>`

Warning
--------

.. esd-warning::

Help and support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
