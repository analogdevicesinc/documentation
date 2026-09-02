.. _ad9656_fmc:

EVAL-AD9656
===============================================================================

Quad, 16-Bit, 125 MSPS, Serial Output ADC with JESD204B Interface.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9656`, is a FMC evaluation board for the :adi:`AD9656`, a quad,
16-bit, 125 MSPS serial output analog-to-digital converter (ADC) with JESD204B
interface. The :adi:`AD9656` is designed for low power, small size, and ease of
use, and features a multistage, differential pipelined architecture with
integrated output error correction logic.

Features:

- SPI interface for setup and control
- External, on-board 125 MHz crystal oscillator
- On-board LDO regulator, needing a single external 6V, 2A dc supply
- ADC VREF configurable for ADC-internal reference, on-board reference,
  off-board reference
- JESD204B serial output interface
- VisualAnalog and SPIController software interfaces

Applications:

- Communications
- Instrumentation and measurement
- Medical imaging
- Phased array radar

.. image:: images/eval-ad9656.jpg
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the
:ref:`Help and Support <ad9656_fmc help_and_support>` section at the bottom of
the page.

To better understand the :adi:`AD9656`, we recommend to use the :adi:`EVAL-AD9656`
evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`Prerequisites <ad9656_fmc prerequisites>` — what you need to get
      started
   #. :ref:`Quick start guides <ad9656_fmc quickstart>`:

      #. Using the :ref:`ZCU102 <ad9656_fmc quickstart zcu102>` with no-OS
      #. Using the
         :ref:`HSC-ADC-EVALEZ <ad9656_fmc quickstart hsc-adc-evalez>` with
         VisualAnalog

   #. :ref:`User guide <ad9656_fmc user-guide>` — hardware and board details

#. Design with the AD9656

   #. :adi:`AD9656 product page <AD9656>`
   #. :external+hdl:ref:`HDL reference design <ad9656_fmc>` which you must use
      in your FPGA.

#. :ref:`Help and Support <ad9656_fmc help_and_support>`

ADI articles
-------------------------------------------------------------------------------

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`

Helpful documents
-------------------------------------------------------------------------------

- :adi:`AD9656` data sheet
- :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation
  Tool Version 1.0 User Manual*
- :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control
  Software*
- :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via
  SPI*
- :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and
  Evaluation*

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _ad9656_fmc help_and_support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
