.. _ad57xx:

EVAL-AD57XXARDZ
===============

Family of Precision, Single-Channel output DACs

.. .. image:: images/ad57xx_chip.png
      :align: left
      :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5780ARDZ` facilitates fast prototyping of the
:adi:`AD5780` circuit, and can be substituted with either the
:adi:`AD5760` or :adi:`AD5790`, which must be ordered separately.
Similarly, the :adi:`EVAL-AD5781ARDZ` and :adi:`EVAL-AD5791ARDZ`
come with the :adi:`AD5781` and :adi:`AD5791` respectively.

The :adi:`AD5790`, :adi:`AD5791`, :adi:`AD5760`, :adi:`AD5780`
and :adi:`AD5781` are a family of precision, single-channel
voltage output DACs, with resolutions from 16-bits up to 20-bits.
They offer guaranteed monotonic operation, and low nonlinearity
(down to 0.5 LSB INL and DNL)

The evaluation boards provide an on-board -14 V and +14 V dual
power supply. These evaluation boards also utilize external
reference boards with an output voltage of +10 V and -10 V. The
eval boards are connected to the carrier board through the
Arduino Shield connector.

Features:

- Precision, single-channel voltage output DACs
- Resolution options from 16 bits to 20 bits
- Guaranteed monotonic operation
- Low integral and differential nonlinearity
  (down to 0.5 LSB INL and DNL, device dependent)
- Buffered voltage outputs
- Wide bipolar output voltage range support
- External precision reference input
- SPI-compatible serial interface
- Low noise and low glitch performance
- Industrial temperature range operation

Applications:

- Medical instrumentation
- Test and measurement equipment
- Industrial control systems
- Scientific instrumentation
- Aerospace and defense instrumentation
- Data acquisition systems
- Precision DC sources
- Digital gain and offset adjustment
- Power supply control and calibration

   .. grid::
      :widths: 50% 50%

      .. figure:: images/eval_ad5781ardz_angle.jpg
         :width: 300

         EVAL-AD5781ARDZ

      .. figure:: images/eval_ad5780ardz_top.jpg
         :width: 400

         EVAL-AD5780ARDZ

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better
experience with things. However, like many things, documentation
is never as complete as it should be. If you have any questions,
feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that,
please make sure you read our documentation thoroughly.

To better understand the :adi:`AD5790` /:adi:`AD5791`
/:adi:`AD5760` /:adi:`AD5780` /:adi:`AD5781`, we recommend to
use the :adi:`EVAL-AD5780ARDZ` /:adi:`EVAL-AD5781ARDZ`
/:adi:`EVAL-AD5791ARDZ` evaluation boards.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that
   we offer:

    #. :ref:`AD57xx user-guide <ad57xx user-guide>` - what you
        need to know about the evaluation board
    #. :ref:`Prerequisites <ad57xx prerequisites>` - what you
        need to get started
    #. :ref:`Quick start guides <ad57xx-ardz quickstart>`:

        #. Using the :ref:`AD57xx on Cora Z7S <ad57xx-ardz quickstart coraz7s>`
        #. Using the :ref:`AD57xx on DE10-Nano <ad57xx-ardz quickstart de10nano>`

    #. Configure an SD Card with
       :external+kuiper:doc:`Kuiper <index>`

    #. Linux Applications

        #. :ref:`iio-oscilloscope`

#. Design with the :adi:`AD5790` /:adi:`AD5791` /:adi:`AD5760`
   /:adi:`AD5780` /:adi:`AD5781`:

    - :ref:`ad57xx block-diagrams`
        #. :adi:`AD5780 product page <ad5780>`
        #. :adi:`AD5781 product page <ad5781>`
        #. :adi:`AD5790 product page <ad5790>`
        #. :adi:`AD5791 product page <ad5791>`
        #. :adi:`AD5760 product page <ad5760>`

    - Resources for designing a custom AD57xx-based platform

    #. For Linux software:

        - About the device driver:

            - :git-linux:`AD5791 IIO DAC Linux Driver <drivers/iio/dac/ad5791.c>`

    #. For no-OS software:

        - About the no-OS driver:

            - :git-no-os:`AD5791 no-OS driver source code <drivers/dac/ad5791/ad5791.c>`

.. _ad57xx block-diagrams:

Block diagrams
-------------------------------------------------------------------------------

The HDL block diagrams for this project are maintained in the
HDL repository:

- :external+hdl:ref:`ad57xx_ardz`

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`EVAL-AD5780ARDZ`
- :adi:`EVAL-AD5781ARDZ`
- :adi:`EVAL-AD5791ARDZ`
