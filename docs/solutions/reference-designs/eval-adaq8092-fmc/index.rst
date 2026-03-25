.. _adaq8092:

EVAL-ADAQ8092-FMCZ
===============================================================================

Dual-Channel, 14-Bit, 105 MSPS, Data Acquisition uModule.

.. image:: images/adaq8092_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADAQ8092` evaluates the :adi:`ADAQ8092`, a 14-bit, 105 MSPS,
high-speed dual-channel data acquisition (DAQ) μModule solution. This device
uses System-in-Package (SiP) technology that integrates three common signal
processing and conditioning blocks: a dual high-speed ADC, a differential
amplifier/ADC driver, and a voltage reference buffer. This μModule solution
simplifies the development of high-speed data acquisition systems by
transferring the design burden of component selection, optimization, and layout
from the designer to the device, enabling a 6x footprint reduction.

The :adi:`EVAL-ADAQ8092` does not require an external power supply and requires
minimal jitter in the clock source. We recommend using the :adi:`DC1075B` clock
divider to improve the clock signal. For full details on the :adi:`ADAQ8092`,
see the :adi:`ADAQ8092` data sheet, which should be consulted in conjunction
with this user guide.

Features:

- Dual-channel simultaneously sampling ADC
- Integrated differential amplifier/ADC driver
- Single-ended to differential input configuration circuitry
- LVDS output capability
- Serial SPI port for configuration
- On-board power solution
- FMC-LPC system board connector

Applications:

- High-speed data acquisition systems
- Ultrasound imaging
- Test and measurement equipment
- Electro-optical targeting systems

.. figure:: images/eval-adaq8092-fmcz.jpg
   :width: 800

   EVAL-ADAQ8092

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our :ref:`EngineerZone
forums <help-and-support>`, but before that, please make sure you read our
documentation thoroughly.

To better understand the :adi:`ADAQ8092`, we recommend using the
:adi:`EVAL-ADAQ8092` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`Prerequisites <adaq8092 prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <adaq8092 quickstart>`:

      #. Using the :ref:`ZedBoard <adaq8092 quickstart zed>`
      #. Using the :ref:`ZedBoard with ACE <adaq8092 quickstart ace_zed>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADAQ8092

   - :ref:`adaq8092 block-diagram`

     - :adi:`ADAQ8092 product page <ADAQ8092>`

   - Resources for designing a custom ADAQ8092 based platform

     #. For Linux software:

        #. :external+linux:doc:`ADAQ8092 IIO ADC Linux Driver <drivers/iio-adc/adaq8092>`
        #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
        #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`

     #. For no-OS software:

        #. :git-no-os:`ADAQ8092-FMC no-OS project <projects/adaq8092_fmc>`
        #. :git-no-os:`ADAQ8092 Driver <drivers/adc/adaq8092>`

     #. :external+hdl:ref:`HDL reference design <adaq8092_fmc>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _adaq8092 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/eval-board-block.png
   :align: center
   :width: 800

   Block Diagram of the EVAL-ADAQ8092-FMCZ

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Technical support for the evaluation board hardware and software can be obtained
by posting a question to ADI's :ez:`EngineerZone <data_converters/precision_adcs>`
technical support community for precision ADCs.
