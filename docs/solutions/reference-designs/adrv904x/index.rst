ADRV9040 Prototyping Platform User Guide
========================================

.. image:: images/adrv904x.jpeg

Overview
--------

The :adi:`ADRV9040 <en/products/adrv9040.html>` is a highly integrated, system on chip (SoC) radio frequency (RF) agile transceiver with integrated digital front end (DFE). The SoC contains eight transmitters, two observation receivers for monitoring transmitter channels, eight receivers, integrated LO and clock synthesizers, and digital signal processing functions. The SoC meets the high radio performance and low power consumption demanded by cellular infrastructure applications including small cell basestation radios, macro 3G/4G/5G systems, and massive MIMO base stations.

Supported carriers
------------------

-  :adi:`ADRV904x-MB/PCBZ <en/products/adrv9040.html>`

.. image:: images/adrv904x-zcu102-quickstart.jpeg
   :align: center
   :width: 600

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to `ask <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_.

-  Use the board to better understand the ADRV9040

   -  :doc:`What you need to get started </solutions/reference-designs/adrv904x/prerequisites>`
   -  :doc:`Quick Start Guides </solutions/reference-designs/adrv904x/quickstart>`

      -  :doc:`Linux on ZCU102 </solutions/reference-designs/adrv904x/quickstart/zynqmp>`
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

         -  `ADRV904x IIO Scope View <https://wiki.analog.com/resources/tools-software/linux-software/adrv904x_osc_main>`_

-  Design with the ADRV904x

   -  :doc:`Understanding the ADRV9040 </solutions/reference-designs/adrv904x/adrv904x>`

      -  :adi:`ADRV9040 Product page <en/products/adrv9040.html>`
      -  :adi:`Full Datasheet and chip design package <en/products/adrv9040.html#product-documentation>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `Transceiver Toolbox <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_

   -  Design a custom ADRV904x based platform

      -  Linux software

         -  `ADRV904x Integrated Radio Frequency Transceiver Linux device driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/adrv904x>`_

            -   `ADRV904x Device Driver Customization <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/adrv904x-customization>`_
            -   `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

         -  `JESD204 (FSM) Interface Linux Kernel Framework <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`_
         -  `AD9528 Low Jitter Clock Generator Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/ad9528>`_
         -  `AXI-DMAC DMA Controller Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/axi-dmac>`_
         -  `JESD204B Transmit Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`_

            -  `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_

         -  `JESD204B Receive Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`_

            -  `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_

         -  `JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`_

            -  `JESD204 Eye Scan <https://wiki.analog.com/resources/tools-software/linux-software/jesd_eye_scan>`_

         -  `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_
         -  `AXI DAC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`_

      -  `Changing the VCXO frequency and updating the default RF Transceiver Profile <https://wiki.analog.com/resources/eval/user-guides/rf-trx-vcxo-and-profiles>`_

-  `Additional Documentation about SDR Signal Chains - The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_
-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Software Defined Radio using the Linux IIO Framework
----------------------------------------------------

`iiosdr.mp4 <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`_

`Software Defined Radio using the Linux IIO Framework <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`_

ADI Articles
------------

-   Four Quick Steps to Production: Using Model-Based Design for
    Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
------------------

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

DPD
---

:doc:`ADRV904x DPD Wiki </solutions/reference-designs/adrv904x/dpd>`

Warning
-------

.. esd-warning::


.. toctree::
   :hidden:

   ad904x_hdl
   adrv904x
   dpd
   dpd/adrv904x_dpd_analysis_tool
   dpd/adrv904x_dpd_capabilities
   dpd/dfe_system_overview
   dpd/dpd_principle_of_operation
   dpd/error_troubleshooting
   dpd/evaluation_user_guide
   dpd/high_level_dev_flow
   dpd/high_level_development_flow
   dpd/pre-requisites
   dpd_principle_of_operation
   prerequisites
   quickstart
   quickstart/zynqmp
