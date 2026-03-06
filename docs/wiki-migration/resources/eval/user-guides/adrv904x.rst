ADRV9040 Prototyping Platform User Guide
========================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv904x.jpeg

Overview
--------

The :adi:`ADRV9040 <en/products/adrv9040.html>` is a highly integrated, system on chip (SoC) radio frequency (RF) agile transceiver with integrated digital front end (DFE). The SoC contains eight transmitters, two observation receivers for monitoring transmitter channels, eight receivers, integrated LO and clock synthesizers, and digital signal processing functions. The SoC meets the high radio performance and low power consumption demanded by cellular infrastructure applications including small cell basestation radios, macro 3G/4G/5G systems, and massive MIMO base stations.

Supported carriers
------------------

-  :adi:`ADRV904x-MB/PCBZ <en/products/adrv9040.html>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv904x/adrv904x-zcu102-quickstart.jpeg
   :align: center
   :width: 600px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  Use the board to better understand the ADRV9040

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/adrv904x/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/adrv904x/quickstart>`

      -  :doc:`Linux on ZCU102 </wiki-migration/resources/eval/user-guides/adrv904x/quickstart/zynqmp>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/zynq_images>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

         -  :doc:`ADRV904x IIO Scope View </wiki-migration/resources/tools-software/linux-software/adrv904x_osc_main>`

-  Design with the ADRV904x

   -  :doc:`Understanding the ADRV9040 </wiki-migration/resources/eval/user-guides/adrv904x/adrv904x>`

      -  :adi:`ADRV9040 Product page <en/products/adrv9040.html>`
      -  :adi:`Full Datasheet and chip design package <en/products/adrv9040.html#product-documentation>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`Transceiver Toolbox </wiki-migration/resources/tools-software/transceiver-toolbox>`

   -  Design a custom ADRV904x based platform

      -  Linux software

         -  :doc:`ADRV904x Integrated Radio Frequency Transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv904x>`

            -   :doc:`ADRV904x Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv904x-customization>`
            -   :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         -  :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         -  :doc:`AD9528 Low Jitter Clock Generator Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9528>`
         -  :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
         -  :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            -  :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`

         -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      -  :doc:`Changing the VCXO frequency and updating the default RF Transceiver Profile </wiki-migration/resources/eval/user-guides/rf-trx-vcxo-and-profiles>`

-  :doc:`Additional Documentation about SDR Signal Chains - The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`
-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Software Defined Radio using the Linux IIO Framework
----------------------------------------------------

.. image:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4
   :alt: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

`Software Defined Radio using the Linux IIO Framework <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`__

ADI Articles
------------

-   Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
------------------

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`__
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`__

DPD
---

:doc:`ADRV904x DPD Wiki </wiki-migration/resources/eval/user-guides/adrv904x/dpd>`

Warning
-------

.. esd-warning::

