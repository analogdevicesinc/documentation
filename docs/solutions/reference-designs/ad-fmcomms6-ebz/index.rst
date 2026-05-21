.. _fmcomms6:

AD-FMCOMMS6-EBZ (Obsolete)
===============================================================================

400 MHz to 4.4 GHz Direct Conversion Receiver.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS6-EBZ` is an FMC evaluation board featuring a direct
conversion (zero IF) receiver based on the :adi:`AD9652` dual 16-bit ADC, the
:adi:`ADL5566` dual differential amplifier, and the :adi:`ADL5380` quadrature
demodulator. The board demonstrates a high performance receiver signal chain
aimed at military and commercial radar using COTS components. The overall
circuit has a bandwidth of 220 MHz with a pass band flatness of +/- 1.0 dB. The
SNR and SFDR measured at an IF of 145 MHz are 64 dB and 75 dBc, respectively.

Features:

- Direct conversion (zero IF) receiver architecture
- 400 MHz to 4.4 GHz RF input frequency range
- 220 MHz circuit bandwidth with +/- 1.0 dB pass band flatness
- :adi:`AD9652` dual 16-bit ADC with sampling speeds up to 310 MSPS
- :adi:`ADL5380` broadband quadrature I-Q demodulator (400 MHz to 6 GHz)
- :adi:`ADL5566` dual differential amplifier for IF and DC applications
- :adi:`AD9517-4` multi-output clock distribution with subpicosecond jitter
- :adi:`ADF4351` fractional-N/integer-N PLL frequency synthesizer
- On-board power solution (:adi:`ADP2370`, :adi:`ADM7150`)
- FMC (VITA57) form factor connector

Applications:

- Military and commercial radar
- Communications receivers
- General-purpose RF signal acquisition

.. figure:: images/top_view_main_page.png
   :width: 500

   AD-FMCOMMS6-EBZ

.. toctree::
   :hidden:

   ad-fmcomms6-ebz
   hardware

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our :ez:`EngineerZone
forums </>` but before that, please make sure you read our documentation
thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. :doc:`User guide <ad-fmcomms6-ebz>`
#. :doc:`Hardware <hardware>`

   #. Picture and main components
   #. Outline and dimensions
   #. Schematic, PCB Layout, Bill of Materials

#. :external+hdl:ref:`HDL Reference Design <fmcomms6>`

#. :ref:`Help and Support <fmcomms6 help-and-support>`

Reference Demos & Software
-------------------------------------------------------------------------------

- :ref:`iio-oscilloscope`
- :ref:`kuiper`
- :external+hdl:ref:`fmcomms6`

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD9652 Product Page <AD9652>`
- :adi:`ADL5380 Product Page <ADL5380>`
- :adi:`ADL5566 Product Page <ADL5566>`
- :adi:`AD9517-4 Product Page <AD9517-4>`
- :adi:`ADF4351 Product Page <ADF4351>`
- :adi:`ADP2370 Product Page <ADP2370>`
- :adi:`ADM7150 Product Page <ADM7150>`

HDL Reference design
-------------------------------------------------------------------------------

.. note::

   This project has been removed from the HDL repository. The last release that
   supports this project is :git-hdl:`hdl_2016_r1 <hdl_2016_r1:projects/fmcomms6/zc706>`.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _fmcomms6 help-and-support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
