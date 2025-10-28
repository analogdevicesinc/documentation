.. _adrv902x:

ADRV902x
===============================================================================

.. image:: adrv9026-bc.webp
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`, are FMC radio cards
designed to showcase the :adi:`ADRV9026` and :adi:`ADRV9029`, highly
integrated, radio frequency (RF) agile transceivers offering 4 independently
controlled transmitters, dedicated observation receiver inputs for monitoring
each transmitter channel, 4 independently controlled receivers, integrated
synthesizers, and digital signal processing functions providing complete
transceiver solutions.

The devices provide the performance demanded by cellular infrastructure
applications, such as small cell base station radios, macro 3G/4G/5G systems,
and massive multiple in/multiple out (MIMO) base stations.

Features:

- Both chips feature:

  - 4 differential transmitters & 4 differential receivers
  - 2 observation receivers with 2 inputs each
  - Support for TDD and FDD applications
  - 24.33 Gbps JESD204B/JESD204C digital interface

- Complete ADRV9026 radio cards for evaluation

  - ADRV9026-HB/PCBZ for frequency band 2.8GHz to 6GHz
  - ADRV9026-MB/PCBZ for frequency band 650MHz to 2.8GHz
  - ADRV9026-LB/PCBZ for frequency band 75MHz to 1000MHz

- Complete ADRV9029 radio cards for evaluation

  - ADRV9029-HB/PCBZ (integrated DPD & CFR) for frequency band 2.8GHz to 6GHz
  - ADRV9029-MB/PCBZ (integrated DPD & CFR) for frequency band 650MHz to 2.8GHz

- A separate power daughter card provides reference design for high efficiency
  power supply solution
- FMC connector for FPGA

Applications:

- 3G/4G/5G TDD and FDD massive MIMO, macro and small cell base stations

.. image:: adrv9026-pcb.png
   :align: center

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADRV9026` / :adi:`ADRV9029`, we recommend to use
the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <adrv902x prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <adrv902x quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale MP SoC <adrv902x quickstart zynqmp>`
      #. Using the :ref:`VCK190/Versal <adrv902x quickstart versal>`

   #. Configure an SD Card with :external+adi-kuiper-gen:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9026/ADRV9029

   - :ref:`adrv902x blockdiagram`

     - :adi:`ADRV9026 product page <ADRV9026>`
     - :adi:`ADRV9029 product page <ADRV9029>`
     - :adi:`Full data sheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom ADRV9026/ADRV9029-based platform software

     #. For Linux software:

        #. About the device driver:

           - :dokuwiki:`JESD204B Transmit Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`
           - :dokuwiki:`JESD204B Receive Linux driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`
           - :dokuwiki:`JESD204B/C AXI_ADXCVR High-speed transceivers Linux driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
           - :dokuwiki:`AXI ADC HDL Linux driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
           - :dokuwiki:`AXI DAC HDL Linux driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
           - :dokuwiki:`AD9528 Low Jitter Clock Generator Linux driver <resources/tools-software/linux-drivers/iio-pll/ad9528>`
           - :dokuwiki:`AXI-DMAC DMA Controller Linux driver <resources/tools-software/linux-drivers/axi-dmac>`
           - :dokuwiki:`ADRV9026/ADRV9029 Linux device driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9025>`
             and :dokuwiki:`how to customize it <resources/tools-software/linux-drivers/iio-transceiver/adrv9025-customization>`

        #. About the device tree:

           - :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :dokuwiki:`JESD204 (FSM) interface Linux Kernel framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
           - :dokuwiki:`JESD204 status utility <resources/tools-software/linux-software/jesd_status>`
           - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`
           - :external+hdl:ref:`jesd204`

     #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
     #. :external+hdl:ref:`HDL reference design <adrv9026>` which you must use in your FPGA.

#. :dokuwiki:`Additional documentation about SDR Signal Chains - The math behind the RF <resources/eval/user-guides/ad-fmcomms1-ebz/math>`
#. :ref:`Help and Support <help-and-support>`

.. _adrv902x blockdiagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: blockdiagram.png

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

Additional information
-------------------------------------------------------------------------------

:dokuwiki:`Digital Pre-Distortion (DPD) User Guide <resources/eval/user-guides/adrv9029>`
with the :adi:`ADRV9029`:

- :dokuwiki:`ADRV9029 DPD Introduction <resources/eval/user-guides/adrv9029/dpd_principle_of_operation>`

  - :dokuwiki:`ADRV9029 Digital Front End System Overview <resources/eval/user-guides/adrv9029/dpd_system_overview>`
  - :dokuwiki:`ADRV9029 DPD System Overview <resources/eval/user-guides/adrv9029/dpd_system_overview2>`
  - :dokuwiki:`ADRV9029 DPD Specifications <resources/eval/user-guides/adrv9029/adrv9029_dpd_capabilities>`
  - :dokuwiki:`Typical High Level DPD development flow with the ADRV9029 transceiver <resources/eval/user-guides/adrv9029/dpd_development_flow>`

- :dokuwiki:`ADRV9029 DPD Prerequisites <resources/eval/user-guides/adrv9029/prerequisites>`
- `Unboxing ADRV902x Transceiver Eval Platform - Video <https://www.youtube.com/watch?v=Oq_9bl5f8fM>`__
- :dokuwiki:`Evaluating ADRV9029 through TES GUI <resources/eval/user-guides/adrv9029/evaluation_through_tes_gui>`
- :dokuwiki:`Evaluating ADRV9029 DPD through TES GUI <resources/eval/user-guides/adrv9029/evaluating_dpd_through_tes_gui>`
- :dokuwiki:`ADRV9029 DPD Error Troubleshooting <resources/eval/user-guides/adrv9029/dpd_error_troubleshooting>`
- :dokuwiki:`ADRV9029 Based DPD Development Flow <resources/eval/user-guides/adrv9029/dpd_development_flow_low_level>`
- :dokuwiki:`ADRV9029 DPD Model Generation <resources/eval/user-guides/adrv9029/dpd_model_optimization>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
