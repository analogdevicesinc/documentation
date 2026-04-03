.. _ad4170:

EVAL-AD4170-4ARDZ
===============================================================================

Customer Evaluation Board for the AD4170-4 Sigma-Delta ADC

.. image:: ./images/ad4170.webp
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4170-4ARDZ` is a comprehensive evaluation board for the
:adi:`AD4170-4`, a multiplexed sigma-delta analog-to-digital converter (ADC)
with ultra-low noise performance. The AD4170-4 features a 5.5 nV/√Hz noise floor
at 128x gain, integrated programmable gain amplifier (PGA), and programmable
digital filters offering output data rates from 500 kSPS to 5 SPS.

The AD4170-4 Family
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD4170-4 family of ADCs offers the highest integration and feature set
required for multi-sensor measurement applications. The platform combines
excellent AC and DC performance, enabling instrumentation and industrial
system designers to address multiple measurement requirements for both
isolated and non-isolated applications.

Features:

- Ultra-low noise sigma-delta ADC core (5.5 nV/√Hz)
- Integrated programmable gain amplifier (PGA) with gains from 0.5x to 128x
- Programmable digital filters
- Integrated low-drift 5 ppm/°C reference
- 12-bit programmable DAC for sensor biasing/excitation
- Multiple measurement diagnostic capabilities
- Optimal input path for AC performance
- Support for various sensor types (thermocouples, RTDs, load cells,
  accelerometers)

Applications:

- Industrial process control: PLC/DCS modules
- Temperature and pressure measurement
- High accuracy medical and scientific instrumentation
- Chromatography
- Seismic and energy exploration
- Electrical test and measurement
- Acoustic analysis
- Instrumentation
- Weigh scale

.. image:: ./images/eval-ad4170-4.webp
   :align: center
   :width: 600

Evaluation board Features

- Full featured evaluation board for the AD4170-4
- PC control in conjunction with SDP controller boards (SDP-K1, SDP-B)
- PC software for control and data analysis (time and frequency domain)
- Standalone capability

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

Following the recommended flow outlined in this documentation provides a much
better experience. However, documentation is never completely comprehensive.
If you have questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but please read the
documentation thoroughly first.

To better understand the :adi:`AD4170-4`, we recommend using the
:adi:`EVAL-AD4170-4ARDZ` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`ad4170 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`ad4170 prerequisites` - what you need to get started with the setup
   #. :ref:`ad4170 quickstart`:

      #. Using the :ref:`SDP-K1 Controller (EVAL-SDP-CK1Z) <ad4170 sdp_k1>`

#. Design with the AD4170-4

   - :ref:`ad4170 block-diagram`
   - :adi:`AD4170-4 product page <AD4170-4>`
   - :adi:`AD4170-4 Eval Guide Document <media/en/technical-documentation/user-guides/eval-ad4170-4-ug-2243.pdf>`

#. Software

   - `AD4170 Device Drivers <https://developer.analog.com/software/drivers/linux/ad4170>`_
   - `ACE Plugin <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software>`_
     for evaluation and testing

#. :ref:`Help and Support <help-and-support>`

.. _ad4170 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad4170_board_block_diagram.png
   :align: center
   :width: 600

Warning
-------------------------------------------------------------------------------

.. esd-warning::
