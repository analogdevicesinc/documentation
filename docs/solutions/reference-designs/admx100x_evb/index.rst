.. _admx100x:

ADMX1001 & ADMX1002
===================

Ultra-low distortion, low noise signal generator and acquisition evaluation
modules.

.. grid::
   :widths: 50% 50%

   .. figure:: images/eval-admx1001.png
      :width: 500

      ADMX1001

   .. figure:: images/eval-admx1002.png
      :width: 500

      ADMX1002

Overview
--------

The :adi:`EVAL-ADMX100X-FMCZ` is an evaluation board for the :adi:`ADMX1001` and
:adi:`ADMX1002` ultra-low distortion, low-noise signal generator modules from
Analog Devices. The **EVAL-ADMX100X-FMCZ** evaluation board provides the
necessary interface circuitry to connect the ADMX100X module to a host PC via
the SDP-H1 controller board, or alternatively via the SDP-S or SDP-B controller
boards with the SDP-I-PMOD interposer.

The **ADMX1001** and **ADMX1002** modules are high-performance signal generators
designed for applications requiring ultra-low harmonic distortion. The DPD
algorithm exploits a patented differential temporal and amplitude sensing method
that requires no external reference inputs, enabling exceptional signal purity
through self-sensing correction. The ADMX1001 and ADMX1002 are capable of
generating signals up to 40 kHz without Digital Pre-Distortion (DPD), or up to
20 kHz with DPD enabled, achieving −130 dBc typical Total Harmonic Distortion
(THD) at 1 kHz.

The **ADMX1001** uniquely includes a differential input acquisition channel to
measure a signal of choice, while the **ADMX1002** focuses solely on signal
generation.

Features:

- SPI and ATE communication interface
- On-board power supply regulation
- External common-mode voltage option
- Sync In and Sync Out for coherent sampling
- External output clamp voltage option
- Differential to single-ended conversion

Applications:

- Audio test and measurement
- Automated test equipment (ATE)
- Coherent sampling and ADC evaluation
- Ultra-low distortion signal generation
- Laboratory signal source

.. figure:: images/EVAL-ADMX100X-FMCZ.png
   :align: center
   :width: 500

   EVAL-ADMX100X-FMCZ

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that,
please make sure you read our documentation thoroughly.

To better understand the :adi:`ADMX1001` / :adi:`ADMX1002`, we recommend to use
the :adi:`EVAL-ADMX100X-FMCZ` evaluation board.

Table of contents
-----------------

#. Using the :adi:`EVAL-ADMX100X-FMCZ` full stack reference design that we
   offer:

   #. :ref:`admx100x-evb user-guide` — what you need to know about the
      evaluation board
   #. :ref:`Prerequisites <admx100x prerequisites>` — what you need to get
      started
   #. :ref:`Quick start guides <admx100x-evb quickstart>`:

      #. Using the :ref:`SDP-H1 <admx100x-evb quickstart sdp-h1>`
      #. Using the :ref:`ZedBoard <admx100x-evb quickstart zed>`

#. Use the board to better understand the ADMX100X

   #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the :adi:`ADMX1001` / :adi:`ADMX1002`

   #. Design a custom ADMX100X-based platform

      #. HDL software

         #. :external+hdl:ref:`HDL reference design <admx100x_evb>`

      #. More information

         #. :external+hdl:ref:`SPI Engine Framework <spi_engine>`

#. :ref:`Help and Support <help-and-support>`

Block diagram
-------------

.. figure:: images/admx100x_simplified_block_diagram.png
   :align: center
   :width: 800

   ADMX100X Simplified Block Diagram

ADI article
-----------

- :adi:`High Performance Source for ADC and Audio Test with Novel Digital Predistortion <resources/technical-articles/high-performance-source-for-adc.html>`

Videos
------

- :adi:`Precision Narrow Bandwidth Signal Chain Solutions <resources/media-center/videos/6301584622001.html>`
- :adi:`Ultra-Low Distortion Waveform Generator and Acquisition Module <resources/media-center/videos/6355673963112.html>`

Warning
-------

.. esd-warning::

Help and support
----------------

For questions and more information, please visit the :ez:`EngineerZone <>` technical support
community.
