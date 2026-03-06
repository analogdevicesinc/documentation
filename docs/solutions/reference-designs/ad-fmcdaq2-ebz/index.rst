.. _ad-fmcdaq2-ebz:

AD-FMCDAQ2-EBZ
===============

High Speed ADC/DAC FMC Evaluation Board.

Overview
--------

The :adi:`AD-FMCDAQ2-EBZ` is an FMC board for the high
speed :adi:`AD9144` DAC and :adi:`AD9680` ADC.
While the complete chip level design package can be found on the ADI product
pages of these converters, information on the card, and how to use it, the
design package that surrounds it, and the software which can make it work, can
be found here.

The purpose of the :adi:`AD-FMCDAQ2-EBZ` is a data
acquisition platform that connects the analog world using FMC to the FPGA.

.. figure:: software/linux/ad-fmcdaq2-ebz_zc706.png
   :align: center
   :width: 500

   AD-FMCDAQ2-EBZ on a ZC706 carrier

.. esd-warning::

.. toctree::
   :hidden:

   introduction
   quickstart
   quickstart/zynq
   quickstart/zcu102
   quickstart/microblaze
   quickstart/a10soc
   quickstart/a10gx
   hardware
   hardware/functional_overview
   hardware/card_specification
   reference_hdl
   software
   software/baremetal
   software/linux
   software/linux/zynq
   software/linux/microblaze
   software/linux/applications
   software/linux/applications/iio_scope
   software/linux/applications/libiio
   software/linux/applications/fru_dump
   clocking
   testing
   help_and_support

Table of contents
-----------------

#. :doc:`Introduction <introduction>`
#. :doc:`Quick Start Guides <quickstart>`

   #. :doc:`Linux on ZC706 <quickstart/zynq>`
   #. :doc:`Linux on ZCU102 <quickstart/zcu102>`
   #. :doc:`Linux on KCU105, KC705, VC707 <quickstart/microblaze>`
   #. :doc:`Linux on Arria10 SoC Development Kit <quickstart/a10soc>`
   #. :doc:`Linux on Arria10 GX FPGA Development Kit <quickstart/a10gx>`

#. :doc:`Hardware <hardware>` (including schematics)

   #. :doc:`Functional Overview & Specifications <hardware/functional_overview>`
   #. :doc:`Characteristics & Performance <hardware/card_specification>`

#. :doc:`Reference HDL Design <reference_hdl>`
#. :doc:`Software <software>`

   #. :doc:`No-OS drivers <software/baremetal>`
   #. :doc:`Linux <software/linux>`

      #. :doc:`ZC706 <software/linux/zynq>`
      #. :doc:`KCU105, KC705, VC707 (Microblaze) <software/linux/microblaze>`
      #. :doc:`Applications <software/linux/applications>`

#. :doc:`Clocking Tree <clocking>` (including samplerate reconfiguration)
#. :doc:`Production Testing Process <testing>`
#. :doc:`Help and Support <help_and_support>`
