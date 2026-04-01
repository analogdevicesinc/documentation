.. _ad9208 dual ebz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. :adi:`AD9208-DUAL-EBZ <EVAL-AD9208>` FMC evaluation board
#. An FPGA carrier platform: AMD Xilinx :xilinx:`VCU118` (Virtex UltraScale+)
#. 2x Micro-USB cable
#. Ethernet cable
#. Signal generator
#. Low phase noise analog input source and antialiasing filter
#. 4-way splitter (optional)

.. note::

   For standalone single-chip evaluation using ACE software on :adi:`ADS7-V2EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADS7-V2>` or
   :adi:`ADS8-V1EBZ`, see the
   :ref:`AD9208-3000EBZ evaluation guide <ad9208-3000ebz>` for specific
   equipment requirements.

Software prerequisites
-------------------------------------------------------------------------------

#. A Linux OS on a PC
#. Xilinx Vivado 2019.1 or later
#. UART terminal (e.g. TeraTerm, PuTTY, Minicom)
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`

Helpful documents
-------------------------------------------------------------------------------

#. :adi:`AD9208 Datasheet <AD9208>`
#. :adi:`AD9689 Datasheet <AD9689>`
#. :adi:`AD9699 Datasheet <AD9699>`
#. :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter
   Evaluation Tool Version 1.0 User Manual*
#. :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing
   and Evaluation*
#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
