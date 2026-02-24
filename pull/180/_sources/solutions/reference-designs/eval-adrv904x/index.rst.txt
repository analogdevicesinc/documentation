.. _adrv904x:

EVAL-ADRV904x
===============================================================================

Integrated 8T8R RF Transceiver with Digital Pre-Distortion and Crest Factor Reduction.

.. image:: ../images/adrv904x-evaluation-board.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV904x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv904x.html>`,
is an FMC radio card designed to showcase the :adi:`ADRV9040` and
:adi:`ADRV9044`, highly integrated, radio frequency (RF) agile transceivers
offering 8 independently controlled transmitters, 2 observation receiver inputs
for monitoring transmitter channels, 8 independently controlled receivers,
integrated local oscillator (LO) and clock synthesizers, digital front-end
(DFE) with crest factor reduction (CFR) and digital pre-distortion (DPD), and
digital signal processing functions providing a complete transceiver solution.

The device provides the high radio performance and low-power consumption
demanded by cellular infrastructure applications and massive MIMO base stations,
offering advanced DFE capabilities on an integrated ARM Cortex-A55 quad-core
processor.

Features:

- Both chips feature:

  - 8 differential transmitters & 8 differential receivers
  - 2 differential observation receivers
  - Support for TDD and FDD applications
  - LO tunable range: 450 MHz to 7100 MHz
  - RF frequency bands:

    - Low Band (LB): 600 MHz to 2800 MHz
    - Mid Band (MB): 1.8 GHz to 4.8 GHz
    - High Band (HB): 4.5 GHz to 6 GHz

  - Integrated Digital Front-End (DFE) with CFR and digital pre-distortion
  - ARM Cortex-A55 quad-core processor for DFE algorithms (DPD, CLGC, VSWR)
  - JESD204B and JESD204C digital interface with fixed and floating-point
    data format support
  - Zero-IF (ZIF) architecture

- Complete ADRV9040/ADRV9044 radio cards for evaluation

  - FMC connector for FPGA integration
  - Fully integrated fractional-N RF synthesizer
  - Fully integrated clock synthesizer

Applications:

- 3G/4G/5G TDD and FDD massive MIMO
- Macro and small cell base stations
- Software defined radios
- Wireless infrastructure

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADRV9040` / :adi:`ADRV9044`, we recommend to
use the :adi:`EVAL-ADRV904x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv904x.html>`
evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <adrv904x prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <adrv904x quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale+ MP SoC <adrv904x quickstart zcu102>`

   #. Configure an SD Card with :external+adi-kuiper-gen:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9040/ADRV9044

   - :ref:`adrv904x block-diagram`

     - :adi:`ADRV9040 product page <ADRV9040>`
     - :adi:`ADRV9044 product page <ADRV9044>`
     - :adi:`Full data sheet and chip design package <en/products/adrv9040.html>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom ADRV9040/ADRV9044-based platform software

     #. For Linux software:

        #. About the device driver:

           - :dokuwiki:`JESD204B Transmit Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           - :dokuwiki:`JESD204B Receive Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           - :dokuwiki:`JESD204B/C AXI_ADXCVR High-speed transceivers Linux driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           - :dokuwiki:`AXI ADC HDL Linux driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
           - :dokuwiki:`AXI DAC HDL Linux driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
           - :dokuwiki:`AD9528 Low Jitter Clock Generator Linux driver <resources/tools-software/linux-drivers/iio-pll/ad9528>`
           - :dokuwiki:`AXI-DMAC DMA Controller Linux driver <resources/tools-software/linux-drivers/axi-dmac>`
           - :dokuwiki:`ADRV904x Linux device driver <resources/tools-software/linux-drivers/iio-transceiver/adrv904x>`
             (not yet mainlined; source at
             :git-linux:`staging/koror_support:drivers/iio/adc/koror/adrv904x.c`)
             and :dokuwiki:`how to customize it <resources/tools-software/linux-drivers/iio-transceiver/adrv904x-customization>`

        #. About the device tree:

           - :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :dokuwiki:`JESD204 (FSM) interface Linux Kernel framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
           - :dokuwiki:`JESD204 status utility <resources/tools-software/linux-software/jesd_status>`
           - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`
           - :external+hdl:ref:`jesd204`

     #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
     #. :git-hdl:`HDL reference design <projects/adrv904x>` which you must use in your FPGA.

#. :dokuwiki:`Additional documentation about SDR Signal Chains - The math behind the RF <resources/eval/user-guides/ad-fmcomms1-ebz/math>`
#. :ref:`Help and Support <help-and-support>`

.. _adrv904x block-diagram:

Block diagram
-------------------------------------------------------------------------------

The ADRV9040/ADRV9044 features a zero-IF (ZIF) architecture that provides
wide bandwidth with dynamic range suitable for contiguous and non-contiguous
multicarrier applications. The transceiver includes:

- 8 transmitter channels with integrated DACs and DPD/CFR
- 8 receiver channels with integrated ADCs
- 2 observation receiver channels for transmitter monitoring
- Integrated RF and clock synthesizers
- Integrated ARM Cortex-A55 quad-core processor for DFE
- JESD204B/C digital interface
- SPI control interface
- General purpose I/O and interrupts

.. image:: ../images/adrv904x_block_diagram.png
   :align: center
   :width: 800

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI articles
-------------------------------------------------------------------------------

Four Quick Steps to Production: Using Model-Based Design for Software-Defined
Radio:

#. :adi:`Part 1 - The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
#. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
#. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
#. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

MathWorks webinars
-------------------------------------------------------------------------------

#. :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
