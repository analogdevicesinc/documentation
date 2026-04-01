.. _ad9208 dual ebz:

AD9208-DUAL-EBZ
===============================================================================

Dual 14-Bit, 3 GSPS, JESD204B, Analog-to-Digital Converter Evaluation Board.

Overview
-------------------------------------------------------------------------------

The AD9208-DUAL-EBZ (see also :adi:`EVAL-AD9208`) is a dual-channel evaluation
platform for the :adi:`AD9208`, a 14-bit, 3 GSPS, JESD204B analog-to-digital
converter. The evaluation board design is shared between the following device
variants: :adi:`AD9208` / :adi:`AD9689` / :adi:`AD9699`.

The board provides all of the support circuitry required to operate the ADC
in its various modes and configurations, including full bandwidth capture,
DDC (Digital Down Converter) mode, and Fsx4 mode.

The AD9208-DUAL-EBZ interfaces with an FPGA carrier via an FMC connector,
using the AMD Xilinx :xilinx:`VCU118` as the main supported platform.
Two additional FPGA-based data capture boards can also be used for
single-chip evaluation: the :adi:`ADS7-V2EBZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADS7-V2>`
and the :adi:`ADS8-V1EBZ`.

Features:

- Full featured evaluation board for the :adi:`AD9208` / :adi:`AD9689` /
  :adi:`AD9699`
- JESD204B coded serial digital outputs with support for lane rates up to
  16 Gbps/lane
- Wide full power bandwidth supports IF sampling of signals up to 9 GHz
  (-3 dB point)
- Four integrated wide-band decimation filter and NCO blocks supporting
  multi-band receivers
- Fast NCO switching enabled through GPIO pins
- Flexible SPI interface controls various product features and functions
- Programmable fast over range detection and signal monitoring
- On-chip temperature diode for system thermal management

Applications:

- Wideband radar and electronic warfare (EW)
- Test and measurement instrumentation
- Wideband communications receivers
- Direct RF sampling systems

.. figure:: images/AD9208-DUAL-EBZangle-web.png
   :align: center
   :width: 600

   EVAL-AD9208 DUAL

.. toctree::
   :hidden:

   user-guide
   ad9208-3000ebz
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ez:`EngineerZone <community/data_converters>`, or send an email to
**highspeed.converters@analog.com**.

To better understand the :adi:`AD9208` / :adi:`AD9689` / :adi:`AD9699`,
we recommend using the AD9208-DUAL-EBZ evaluation board together with
the AMD Xilinx :xilinx:`VCU118` FPGA development kit.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`User guide <ad9208 dual ebz user-guide>` - what you need to know
      about the AD9208-DUAL-EBZ board
   #. :ref:`Evaluating the AD9208 / AD9689 / AD9699 <ad9208-3000ebz>` -
      standalone evaluation board guide with ACE software
   #. :ref:`Prerequisites <ad9208 dual ebz prerequisites>` - what you need
      to get started
   #. :ref:`Quick start guides <ad9208 dual ebz quickstart>`:

      #. Using the :ref:`VCU118/Virtex UltraScale+ <ad9208 dual ebz quickstart vcu118>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9208 / AD9689 / AD9699

   - :adi:`AD9208 product page <AD9208>`
   - :adi:`AD9689 product page <AD9689>`
   - :adi:`AD9699 product page <AD9699>`

   - Resources for designing a custom platform:

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AD9208 ADC Linux Driver <ad9208>`

     #. For no-OS software:

           - :external+no-OS:doc:`AD9208 no-OS Example Project <projects/adc/ad9208>`

     #. :external+hdl:ref:`HDL reference design <ad9208_dual_ebz>` which you
        must use in your FPGA.

        - :external+hdl:ref:`jesd204`

#. :adi:`High-Speed Converter Data Source/Capture Boards <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/high-speed-adc-data-capture-boards>`
#. :ref:`Help and Support <help-and-support>`

ADI articles
-------------------------------------------------------------------------------

About the JESD204 standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.

For additional information or questions, post a question on
:ez:`EngineerZone <community/data_converters>`, or send an email to
**highspeed.converters@analog.com**.
