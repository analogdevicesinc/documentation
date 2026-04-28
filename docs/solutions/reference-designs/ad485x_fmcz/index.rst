.. _ad485x_fmcz:

AD485X-FMCZ
===================================

Buffered, 8-Channel Simultaneous Sampling, 20-Bit 1 MSPS DAS

.. image:: ./images/AD485x-chip-illustration.png
   :align: left
   :width: 150

.. image:: ./images/AD4858-chip-illustration.png
   :align: left
   :width: 150

Overview
------------

The :adi:`EVAL-AD4858` board contains the :adi:`AD4858` chip, which is a
20-bit, low noise 8-channel simultaneous sampling successive approximation
register (SAR) ADC, with buffered differential, wide common range picoamp
inputs.

More about simultaneous sampling A/D converters :adi:`here <en/products/analog-to-digital-converters/precision-ad-converters.html>`.

The :adi:`EVAL-AD4858` supports pin-selectable SPI CMOS and LVDS serial
interfaces. In CMOS mode, applications may employ between 1-8 lanes of serial
output data, allowing the user to optimize bus width and data throughput. In
LVDS mode, pins SDO+/-, SCKI+/- and SCKO+/- function as differential serial
data input, clock output and clock input pins respectively (from the FPGA's
point of view).

Features:

- Full featured evaluation board for the :adi:`AD4858`
- Eight input channels available through SMA connectors
- On-board reference circuit and power supplies
- Standalone capability through FMC connector and/or test points
- PC software for control and data analysis of the time and frequency domain
- :xilinx:`ZedBoard`-compatible
- Compatible with other FMC controller boards

Applications:

- Automatic test equipment
- Avionics and aerospace
- Instrumentation and control systems
- Semiconductor manufacturing
- Test and measurement

.. image:: ./images/EVAL-AD4858FMCZ_ANGLE-evaluation-board.JPG
   :align: center
   :width: 600px

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:ref:`ask <help-and-support>`.

Table of Contents
-----------------

#. Getting started with the EVAL_AD4858

   #. :ref:`What you need to get started <ad485x_fmcz prerequisites>`
   #. :ref:`EVAL-AD485X-FMCZ Quick Start Guide <ad485x_fmcz quickstart>`
      #. :dokuwiki:`Configure a pre-existing SD-Card <resources/tools-software/linux-software/kuiper-linux>`
      #. :dokuwiki:`Update the old card you received with your hardware <resources/tools-software/linux-software/kuiper-linux>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

   #. :dokuwiki:`FRU EEPROM Utility <resources/tools-software/linux-software/fru_dump>`

   #. Design with the AD485X

      #. Understanding the AD485X

         #. :adi:`AD4858` Product page
         #. `EVAL-AD485X-FMCZ User Guide <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad4858-ug-2142.pdf>`__

      #. Hardware in the Loop / How to design your own custom BaseBand

         #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
         #. :dokuwiki:`Board Support Package for MathWorks Tools <resources/tools-software/transceiver-toolbox>`

      #. Design with the EVAL-AD485X-FMCZ based platform

         #. Linux software

            .. #. :dokuwiki:`AD485X Linux Device Driver <TBD>`

            #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
            #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

         #. :external+hdl:ref:`HDL Reference Design <ad485x_fmc>`

Pre-requisites and quickstart
-------------------------------------------------------------------------------

.. toctree::
   :caption: The prerequisites and quickstart guides are provided at:
   :titlesonly:
   :maxdepth: 1

   prerequisites
   quickstart/index

.. _ad485x_fmcz block-diagram:

Functional Block Diagram
-------------------------------------------------------------------------------

.. image:: ./images/ad4858-fbl.png
   :width: 600

Warning
-------------------------------------------------------------------------------

.. esd-warning::
