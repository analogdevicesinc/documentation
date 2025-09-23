.. _adrv9026:

ADRV9026 & ADRV9029
===============================================================================

.. image:: adrv9026-bc.webp
   :align: left
   :width: 150

The :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`, are FMC radio cards for the
:adi:`ADRV9026` and :adi:`ADRV9029`, highly integrated, radio frequency (RF)
agile transceivers offering four independently controlled transmitters,
dedicated observation receiver inputs for monitoring each transmitter channel,
four independently controlled receivers, integrated synthesizers, and digital
signal processing functions providing complete transceiver solutions. The
devices provide the performance demanded by cellular infrastructure
applications, such as small cell base station radios, macro 3G/4G/5G systems,
and massive multiple in/multiple out (MIMO) base stations.

.. image:: adrv9026-pcb.png
   :align: center

.. toctree::
   :hidden:

   prerequisites
   quickstart/index

Table of Contents
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:ref:`ask <ad-fmcomms2-ebz help-and-support>`.

#. Use the board to better understand the ADRV9026/ADRV9029

   #. :ref:`What you need to get started <adrv9026 prerequisites>`
   #. :ref:`Quick Start Guides <adrv9026 quickstart>`

      #. :ref:`Linux on ZCU102 <adrv9026 quickstart zynqmp>`
      #. :external+adi-kuiper-gen:doc:`Configure a pre-existing SD Card <use-kuiper-image>`
      #. :external+adi-kuiper-gen:doc:`Update the old card you received with your hardware <repositories>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9026/ADRV9029

   #. :ref:`adrv9026 blockdiagram`

      #. :adi:`ADRV9026 Product page <ADRV9026>`
      #. :adi:`ADRV9029 Product page <ADRV9029>`
      #. :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   #. Design a custom ADRV9026/ADRV9029 based platform

      #. Linux software

         #. :dokuwiki:`ADRV9026/ADRV9029 Linux Device Driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9025>`

            #. :dokuwiki:`ADRV9026/ADRV9029 Device Driver Customization <resources/tools-software/linux-drivers/iio-transceiver/adrv9025-customization>`
            #. :dokuwiki:`Customizing the devicetree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         #. :dokuwiki:`JESD204 (FSM) Interface Linux Kernel Framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         #. :dokuwiki:`AD9528 Low Jitter Clock Generator Linux Driver <resources/tools-software/linux-drivers/iio-pll/ad9528>`
         #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
         #. :dokuwiki:`JESD204B Transmit Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B Receive Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            #. :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

         #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
      #. :dokuwiki:`HDL Reference Design <resources/eval/user-guides/adrv9026/ad9026_hdl>` which you must use in your FPGA.

#. :dokuwiki:`Additional Documentation about SDR Signal Chains - The math behind the RF <resources/eval/user-guides/ad-fmcomms1-ebz/math>`
#. :ref:`Help and Support <ad-fmcomms2-ebz help-and-support>`

.. _adrv9026 blockdiagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: blockdiagram.png

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
-------------------------------------------------------------------------------

#. Four Quick Steps to Production: Using Model-Based Design for
Software-Defined Radio

   #. :adi:`Part 1 - The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   #. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   #. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   #. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
-------------------------------------------------------------------------------

#. :mw:`Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
