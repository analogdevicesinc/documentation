.. _pulsar-lvds-adc:

PULSAR-LVDS-ADC
===============

16-Bit/18-Bit, 5 MSPS to 10 MSPS PulSAR LVDS Differential ADC Family

.. Chip photo doesn't exist in ContentHub, add after it's been added there.

Overview
--------

The :adi:`AD7625`, :adi:`AD7626`, :adi:`AD7960`, and :adi:`AD7961` are
high-performance successive approximation register (SAR) analog-to-digital
converters from the PulSAR LVDS family. They feature charge redistribution
SAR architecture with LVDS self-clocked or echoed-clock serial interfaces.

The :adi:`AD7625` is a 16-bit, 6 MSPS ADC and the :adi:`AD7626` is a 16-bit,
10 MSPS ADC. Both achieve 92 dB SNR with excellent linearity (±1 LSB INL for
AD7625, ±1.5 LSB INL for AD7626). They use an internal 4.096 V reference with
a 1.2 V REFIN input.

The :adi:`AD7960` is an 18-bit, 5 MSPS ADC and the :adi:`AD7961` is a 16-bit,
5 MSPS ADC. They provide 99 dB SNR (AD7960) and 95.5 dB SNR (AD7961) with
±1 LSB INL. They operate with an external 5 V reference and 2.048 V REFIN.

All devices feature internal reference buffers, low power dissipation, and LVDS
digital outputs suitable for high-speed data acquisition systems.

Features:

-  16-bit or 18-bit resolution, up to 10 MSPS throughput
-  92 dB to 99 dB SNR, ±1 LSB INL
-  LVDS self-clocked or echoed-clock serial interface
-  Internal reference buffer
-  Low power dissipation
-  Charge redistribution SAR architecture

Applications:

-  Digital imaging
-  High-speed data acquisition
-  Telecommunications
-  Spectrum analysis
-  Test and measurement equipment
-  Medical instrumentation

.. figure:: images/pulsar_lvds_adc_eval-ad7625-6.jpg
   :align: center
   :width: 400

   EVAL-AD7625/EVAL-AD7626 evaluation board

.. figure:: images/pulsar_lvds_adc_eval-ad7960.jpg
   :align: center
   :width: 400

   EVAL-AD7960/EVAL-AD7961 evaluation board

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand these devices, we recommend using one of the following
evaluation boards:

-  :adi:`EVAL-AD7625` for the AD7625
-  :adi:`EVAL-AD7626` for the AD7626
-  :adi:`EVAL-AD7960` for the AD7960
-  :adi:`EVAL-AD7961` for the AD7961

Table of contents
-----------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <pulsar-lvds-adc prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <pulsar-lvds-adc quickstart>`:

      #. Using the :ref:`ZedBoard / Zynq-7000 SoC
         <pulsar-lvds-adc quickstart zed>`

   #. Configure an SD Card with
      :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD7625/AD7626/AD7960/AD7961

   #. HDL reference design

      #. :external+hdl:ref:`pulsar_lvds_adc` which
         you must use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/functional_diagram_ad7625-6.jpg
   :align: center
   :width: 600

   AD7625/AD7626 functional block diagram

.. figure:: images/functional_diagram_ad7960.jpg
   :align: center
   :width: 600

   AD7960/AD7961 functional block diagram

.. toctree::
   :hidden:

   user-guide
   quickstart/index
   prerequisites

Additional Information and Useful Links
----------------------------------------

-  :adi:`AD7625 Product Page <AD7625>`
-  :adi:`AD7626 Product Page <AD7626>`
-  :adi:`AD7960 Product Page <AD7960>`
-  :adi:`AD7961 Product Page <AD7961>`
-  :adi:`EVAL-AD7625 Evaluation Board <EVAL-AD7625>`
-  :adi:`EVAL-AD7626 Evaluation Board <EVAL-AD7626>`
-  :adi:`EVAL-AD7960 Evaluation Board <EVAL-AD7960>`
-  :adi:`EVAL-AD7961 Evaluation Board <EVAL-AD7961>`
-  :adi:`AD7625 Data Sheet <media/en/technical-documentation/data-sheets/ad7625.pdf>`
-  :adi:`AD7626 Data Sheet <media/en/technical-documentation/data-sheets/ad7626.pdf>`
-  :adi:`AD7960 Data Sheet <media/en/technical-documentation/data-sheets/ad7960.pdf>`
-  :adi:`AD7961 Data Sheet <media/en/technical-documentation/data-sheets/ad7961.pdf>`
-  :adi:`UG-745: EVAL-AD7625/EVAL-AD7626 User Guide <media/en/technical-documentation/user-guides/eval-ad7625fmcz_7626fmcz_ug-745.pdf>`
-  :adi:`UG-490: EVAL-AD7960/EVAL-AD7961 User Guide <media/en/technical-documentation/user-guides/ug-490.pdf>`

Warning
--------

.. esd-warning::

Help and support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
