.. _eval-ad7134-fmcz:

EVAL-AD7134-FMCZ
=================

24-Bit, 4-Channel Simultaneous Sampling 1.5 MSPS Precision Alias Free ADC

.. image:: images/ad7134_chip.png
   :align: left
   :width: 100

Overview
--------

The :adi:`AD7134` is a 24-bit, 4-channel simultaneous sampling 1.5MSPS,
precision, alias free ADC. It contains a continuous time Σ-Δ modulation
technology that does not use sample-and-hold circuitry to alleviate the side
effects introduced by it, like charge kickback and signal aliasing. This
inherent alias rejection is up to 100dB.

The device has an asynchronous sample rate converter used to synchronize two
or more devices using only a signal line. To do this one of the devices will
generate the synchronization signal while the others will receive it. This
also allows for freely programmable data rates from 10SPS up to 1.496MSPS.

It has excellent AC and DC performance with 107dB dynamic for the FIR filter
at 374kSPS and 138dB dynamic range for the sinc3 filter at 10SPS. The offset
drift is 1.5uV/°C, gain drift of 2ppm/°C and INL of ±2.5ppm.

It can be powered from a 4.5V to 5.5V power supply and a 1.65V to 1.95V
digital power supply for 1.8V I/O level. It can have external voltage
reference of 2.5V, 4.096V and 5V and a crystal or CMOS external clock of
48MHz. The device can be configured and controlled by GPIOs or SPI. It has
temperature operating range between 0°C and 85°C.

Features:

-  24-bit, 4-channel simultaneous sampling ADC
-  Throughput of up to 1.496 MSPS
-  Alias-free continuous time Σ-Δ modulation (up to 100dB rejection)
-  Freely programmable data rates from 10SPS to 1.496MSPS
-  Asynchronous sample rate converter for multi-device synchronization
-  SPI or GPIO configuration and control

Applications:

-  Electrical test and measurement
-  Audio test
-  3-phase power quality analysis
-  Control and hardware in loop verification
-  Sonar
-  Condition and monitoring for predictive maintenance
-  Acoustic and material science research and development

   .. figure:: images/ad7134_eval.png
      :align: center
      :width: 400

      EVAL-AD7134FMCZ evaluation board

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD7134`, we recommend to use the
:adi:`EVAL-AD7134FMCZ` evaluation board.

Table of contents
-----------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad7134-fmcz prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-ad7134-fmcz quickstart>`:

      #. Using the :ref:`Zedboard/ Zynq-7000 SoC
         <eval-ad7134-fmcz quickstart zed>`

   #. Configure an SD Card with
      :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

   #. :ref:`AD7134 IIO Application
      <eval-ad7134-fmcz ad7134-iio-support>` (no-OS / MBED / STM32)

#. Design with the AD7134

   #. HDL reference design

      #. :external+hdl:ref:`ad7134_fmc` which
         you must use in your FPGA.

   #. More information

      #. :external+hdl:ref:`spi_engine`

#. :ref:`Help and Support <help-and-support>`

Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

   .. figure:: images/ad7134_block_diagram.png
      :width: 1000

      AD7134 functional block diagram

.. toctree::
   :hidden:

   user-guide
   quickstart/index
   prerequisites
   ad7134_iio_support

Additional Information and Useful Links
----------------------------------------

-  :adi:`AD7134 Product Page <AD7134>`
-  :adi:`EVAL-AD7134FMCZ Evaluation Board <EVAL-AD7134FMCZ>`
-  :adi:`AD7134 Data Sheet
   <media/en/technical-documentation/data-sheets/ad7134.pdf>`

Warning
--------

.. esd-warning::

Help and support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
