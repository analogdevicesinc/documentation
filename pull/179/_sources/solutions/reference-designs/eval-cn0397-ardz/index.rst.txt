.. _eval-cn0397-ardz:

EVAL-CN0397-ARDZ
================

Smart Agriculture Visible Light Detection System.

The :adi:`EVAL-CN0397-ARDZ <CN0397>` is an Arduino-compatible shield optimized
for smart agriculture utilizing wavelength-specific photodiodes.
Photosynthetic response of plants varies due to the wavelength and intensity of
light received. The photodiodes used in this circuit have peak sensitivities
over the red and blue wavelength regions and over the green region which is
mainly rejected by the leaves of the plant.

.. figure:: cn0397_v1.png
   :align: center
   :width: 500

   EVAL-CN0397-ARDZ evaluation board

.. toctree::
   :hidden:

   hardware
   software

Table of Contents
-----------------

#. :doc:`Hardware Guide <hardware>`
#. :doc:`Software Demos <software>`

Overview
--------

The circuit uses the :adi:`AD8500`, a low power, precision CMOS op amp with a
low input bias current of a typical 1 pA, configured in a transimpedance
amplifier configuration to convert the current output of the photodiodes into
voltage. It also features the :adi:`AD7798`, a 3-channel, low noise, low power
16-bit ADC that converts the analog voltage into digital data for processing
into light intensity. Gain resistor for each channel has been calculated to
maximize the full scale of the ADC, with additional filtering to remove
unwanted signals.

The circuit utilizes RGB photodiodes from Everlight with their peak
sensitivities at 620 nm (Red), 550 nm (Green), and 470 nm (Blue).

Supported Devices
-----------------

- :adi:`AD7798` -- 3-Channel, Low Noise, Low Power 16-bit Sigma-Delta ADC
- :adi:`AD8500` -- Low Power Precision CMOS Op Amp

Documents
---------

- :adi:`CN0397 Circuit Note <CN0397>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0397-ARDZ Design & Integration Files
   <https://www.analog.com/cn0397-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
