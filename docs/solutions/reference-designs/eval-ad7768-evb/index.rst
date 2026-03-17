.. _ad7768:

EVAL-AD7768FMCZ / EVAL-AD7768-4FMCZ
===============================================================================

8/4 Channel, 24-Bit, 256 kSPS Simultaneous Sampling Sigma-Delta ADC.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7768` and :adi:`EVAL-AD7768-4` are FMC evaluation boards for
the :adi:`AD7768` and :adi:`AD7768-4`, 8-channel and 4-channel simultaneous
sampling sigma-delta analog-to-digital converters (ADCs), respectively. Each
channel includes a sigma-delta modulator and digital filter, enabling
synchronized sampling of ac and dc signals. The devices achieve 108 dB dynamic
range at a maximum input bandwidth of 110.8 kHz, with typical performance of
+/-2 ppm INL, +/-50 uV offset error, and +/-30 ppm gain error.

Features:

- 8/4 simultaneous sampling channels with independent sigma-delta modulators
- 108 dB dynamic range, 110.8 kHz maximum input bandwidth
- Three power modes: fast (256 kSPS), median (128 kSPS), low power (32 kSPS)
- Wideband antialiasing filter with +/-0.005 dB pass-band ripple
- Sinc5 filter for low latency, low bandwidth measurements
- Configurable decimation rates: x32, x64, x128, x256, x512, x1024

Applications:

- Sound and vibration monitoring
- Electrical power quality analysis
- Condition-based monitoring
- Acoustic and material testing

.. figure:: images/eval-ad7768-fmcz.png
   :width: 800

   EVAL-AD7768

.. figure:: images/eval-ad7768-4fmcz.png
   :width: 800

   EVAL-AD7768-4

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

To better understand the :adi:`AD7768` / :adi:`AD7768-4`, we recommend to use
the :adi:`EVAL-AD7768` / :adi:`EVAL-AD7768-4` evaluation boards.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad7768 prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <ad7768 quickstart>`:

      #. Using the :ref:`ZedBoard <ad7768 quickstart zed>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD7768/AD7768-4

   - :ref:`ad7768 block-diagram`

     - :adi:`AD7768 product page <AD7768>`
     - :adi:`AD7768-4 product page <AD7768-4>`
     - :adi:`AD7768/AD7768-4 Datasheet <media/en/technical-documentation/data-sheets/ad7768-ad7768-4.pdf>`

   - Resources for designing a custom AD7768/AD7768-4 based platform

     #. For Linux software:

        #. :external+linux:doc:`AD7768 IIO Precision ADC Linux Driver <drivers/iio-adc/ad7768>`
        #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
        #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`

     #. For no-OS software:

        #. :git-no-os:`AD7768-EVB no-OS project <projects/ad7768-evb>`
        #. :git-no-os:`AD7768 Driver <drivers/adc/ad7768>`
        #. :dokuwiki:`no-OS IIO </resources/tools-software/no-os-software/iio>`

     #. :external+hdl:ref:`HDL reference design <ad7768evb>` which you must use
        in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _ad7768 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad7768_ad7768-4_block_diagram.png
   :align: center
   :width: 800

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
