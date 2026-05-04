.. _eval-ad4110:

EVAL-AD4110-1
===============================================================================

Universal Input Analog Front End with 24-Bit ADC for Industrial
Process Control Systems.

.. image:: ./images/ad4110_chip.jpeg
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4110-1SDZ` is the evaluation board for the :adi:`AD4110-1`,
a complete, single-channel, universal input analog-to-digital front end for
industrial process control systems where sensor type flexibility is required.

The high voltage input is fully software configurable for current or voltage
ranges and allows direct interface to all standard industrial analog signal
sources such as ±20 mA, ±4 mA to ±20 mA, ±10 V, and all thermocouple types.
Field power can be supplied for loop powered current output sensors. The high
voltage input can be programmed to power up in either voltage or current mode.

The :adi:`AD4110-1` provides internal front-end diagnostic functions to
indicate overvoltage, undervoltage, open wire, overcurrent, and overtemperature
conditions. The high voltage input is overcurrent limited and overvoltage
protected up to ±30 V.

The :adi:`AD4110-1` incorporates a precision 24-bit, Σ-Δ ADC offering
conversion rates from 5 SPS to 125 kSPS with simultaneous 50 Hz and 60 Hz
noise rejection.

Features:

- 2 software programmable input terminals

  - Current: up to ±20 mA
  - Voltage: up to ±10 V
  - Thermocouple
  - RTD

- Field power supply for loop powered current output sensors
- HV input overvoltage protected up to ±30 V
- Internal current sense resistor; option to use external resistor
- Diagnostic functions: overvoltage, undervoltage, open wire,
  overcurrent, overtemperature
- Fast and flexible output data rates: 5 SPS to 125 kSPS
- Simultaneous 50 Hz and 60 Hz noise rejection
- 4-wire SPI compatible interface (SPI, QSPI, MICROWIRE, DSP)
- Power supply: ±12 V to ±20 V, +5 V

Applications:

- Industrial process control (PLC, DCS)
- Remote and distributed control systems
- Data acquisition
- Instrumentation and measurement
- Sensor interface

.. figure:: ./images/eval-ad4110_board.jpeg
   :alt: Photo of the EVAL-AD4110-1SDZ evaluation board
   :align: center
   :width: 600

   EVAL-AD4110-1SDZ Evaluation Board

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   mbed-iio

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience.
However, documentation is never as complete as it should be. If you have any
questions, feel free to ask on our :ez:`/`, but please read our documentation
thoroughly first.

To better understand the :adi:`AD4110-1`, we recommend using the
:adi:`EVAL-AD4110-1SDZ` evaluation board with the :adi:`SDP-B` controller
board and the AD4110-1 evaluation software on Windows, or the Digilent
ZedBoard with the ADI HDL reference design and No-OS evaluation.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design:

   #. :ref:`eval-ad4110 user-guide` - hardware and software user guide
   #. :ref:`Prerequisites <eval-ad4110 prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-ad4110 quickstart>`:

      #. :ref:`SDP-B and Evaluation Software
         <eval-ad4110 quickstart sdp-b>`
      #. :ref:`ZedBoard HDL Reference Design
         <eval-ad4110 quickstart zedboard>`

#. Software and firmware:

   - :ref:`eval-ad4110 mbed-iio` - Mbed IIO firmware application
     for the :adi:`SDP-K1`

#. Design with the AD4110-1:

   - :ref:`eval-ad4110 block-diagram`

     - :adi:`AD4110-1 product page <AD4110-1>`

   - Resources for building a custom AD4110-1-based design:

     #. :external+hdl:ref:`ad4110`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad4110 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: ./images/ad4110_schematic.jpeg
   :alt: Functional block diagram of the EVAL-AD4110-1SDZ showing
         the signal path from field sensors through the AFE and ADC
         to the digital serial interface
   :align: center
   :width: 1000

   EVAL-AD4110-1SDZ Functional Block Diagram

Warning
-------------------------------------------------------------------------------

.. esd-warning::
