.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms6-ebz

.. _ad-fmcomms6-ebz:

AD-FMCOMMS6-EBZ
================

.. warning::

   The :adi:`AD-FMCOMMS6-EBZ
   <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCOMMS6-EBZ.html>`
   board has been retired and is no longer available for sale. Support has been
   discontinued. The HDL project has been removed from the main branch but is
   still available in the
   :git-hdl:`hdl_2015_r2 <hdl_2015_r2:projects/fmcomms6>` release branch.

The :adi:`AD-FMCOMMS6-EBZ
<en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCOMMS6-EBZ.html>`
eval board is a 400 MHz to 4.4 GHz receiver based on the :adi:`AD9652` dual
16-bit ADC, the :adi:`ADL5566` high dynamic range RF/IF dual differential
amplifier, and the :adi:`ADL5380` quadrature demodulator.

.. figure:: top_view_main_page.png
   :align: center
   :width: 500

   AD-FMCOMMS6-EBZ evaluation board

Introduction
------------

This is an I and Q demodulation approach to direct conversion (also known as
homodyne or zero IF) receiver architecture. Direct conversion radios perform
just one frequency translation compared to a super-heterodyne receiver that can
perform several frequency translations. One frequency translation is
advantageous because it:

- Reduces receiver complexity and the number of stages needed, increasing
  performance and reducing power consumption
- Avoids image rejection issues and unwanted mixing

This topology provides image rejection and early implementation of the
differential signal environment. There is an amplification stage to maintain the
full-scale input to the ADC. The local oscillator and ADC clock are on-board and
share the same reference signal to prevent smearing. The form factor is VITA57
compliant and all of the DC power is routed from the data capture board through
an FMC connector. This evaluation board demonstrates a high performance receiver
signal chain aimed at military and commercial radar using "commercial off the
shelf" (COTS) components.

The overall circuit has a bandwidth of 220 MHz with a passband flatness of
+/- 1.0 dB. The SNR and SFDR measured at an IF of 145 MHz are 64 dB and
75 dBc, respectively.

Contains
~~~~~~~~

- :adi:`AD9652` two 16-bit ADCs with sampling speeds of up to 310 MSPS
- :adi:`ADL5380` broadband quadrature I-Q demodulator, 400 MHz to 6 GHz
- :adi:`ADL5566` high performance, dual differential amplifier for IF and DC
  applications
- :adi:`ADP2370` high efficiency, 800 mA buck DC-to-DC converter
- :adi:`AD9517-4` multi-output clock distribution with on-chip PLL and VCO
- :adi:`ADF4351` fractional-N/integer-N PLL frequency synthesizer
- :adi:`ADM7150` low dropout linear regulator, 4.5 V to 16 V, up to 800 mA

Hardware
--------

Main Components
~~~~~~~~~~~~~~~

.. figure:: main_components.jpg
   :align: center
   :width: 600

   AD-FMCOMMS6-EBZ main components

Component Placement
~~~~~~~~~~~~~~~~~~~

For those that don't want to load up the Allegro viewer, here is a basic
outline/component placement of the board.

.. figure:: fmcomms6_top.jpg
   :align: center
   :width: 400

   AD-FMCOMMS6-EBZ component placement outline

Board Dimensions
~~~~~~~~~~~~~~~~

The size of the board (not including the SMA connectors, which project beyond
the edge of the board) is 3.42 inches by 2.72 inches (or about 89 mm x 69 mm).
This exceeds the FMC specifications of 84 mm x 69 mm.

.. figure:: fmcomms6_dim.jpg
   :align: center
   :width: 400

   AD-FMCOMMS6-EBZ board dimensions

HDL Reference Design
--------------------

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`hdl_2015_r2:projects/fmcomms6`

Support
-------

If you have any questions regarding the AD-FMCOMMS6-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
