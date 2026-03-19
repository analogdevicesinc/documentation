AD9371 & AD9375 Prototyping Platform User Guide
===============================================

.. image:: images/ad9371-bc_196-adi_m.png
   :align: left
   :width: 300

The :adi:`ADRV9371-W/PRBZ <EVAL-ADRV9371>`, :adi:`ADRV9371-N/PCBZ <EVAL-ADRV9371>` and :adi:`ADRV9375-N/PCBZ <ADRV9375>` are FMC radio cards for the :adi:`AD9371` respectively :adi:`AD9375`, a highly integrated RF Transceiver™. While the complete chip level design package can be found on the the :adi:`the ADI web site <en/license/licensing-agreement/ad9371.html>`, information on the card and how to use it, the design package that surrounds it, and the software which can make it work can be found here.

.. image:: images/adrv9371-n_pcbz_side.jpg
   :align: center
   :width: 600

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to `ask <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_.

-  Use the board to better understand the AD9371/AD9375

   -  :doc:`What you need to get started </solutions/reference-designs/adrv9371x/prerequisites>`
   -  :doc:`Quick Start Guides </solutions/reference-designs/adrv9371x/quickstart>`

      -  :doc:`Linux on ZC706 </solutions/reference-designs/adrv9371x/quickstart/zynq>`
      -  `Linux on Arria 10 SOC <https://wiki.analog.com/resources/eval/user-guides/adrv9371/quickstart/a10soc>`_
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

         -  `AD9371/AD9375 IIO Scope View <https://wiki.analog.com/resources/tools-software/linux-software/ad9371_osc_main>`_
         -  `AD9371/AD9375 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/ad9371_plugin>`_
         -  `Advanced AD9371/AD9375 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/ad9371_advanced_plugin>`_

      -  `FRU EEPROM Utility <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`_

   -  Push custom data into/out of the AD9371/AD9375

      -  :doc:`Basic Data files and formats </solutions/reference-designs/adrv9371x/software/basic_iq_datafiles>`
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
      -  `Python Interfaces <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_

-  Design with the AD9371/AD9375

   -  :doc:`Understanding the AD9371/AD9375 </solutions/reference-designs/adrv9371x/ad9371>`

      -  :adi:`AD9371 Product page <AD9371>`
      -  :adi:`AD9375 Product page <AD9375>`
      -  :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      -  :doc:`MATLAB Filter Wizard / Profile Generator for AD9371 </solutions/reference-designs/adrv9371x/software/filters>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `Transceiver Toolbox <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_

   -  Design a custom AD9371/AD9375 based platform

      -  Linux software

         -  `AD9371/AD9375 Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`_

            -   `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

         -  `AD9528 Low Jitter Clock Generator Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/ad9528>`_
         -  `AD7291 IIO ADC Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/ad7291>`_
         -  `JESD204B Transmit Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`_

            -  `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_

         -  `JESD204B Receive Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`_

            -  `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_

         -  `JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`_

            -  `JESD204 Eye Scan <https://wiki.analog.com/resources/tools-software/linux-software/jesd_eye_scan>`_

         -  `AXI ADC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_
         -  `AXI DAC HDL Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`_

      -  `Changing the VCXO frequency and updating the default RF Transceiver Profile <https://wiki.analog.com/resources/eval/user-guides/rf-trx-vcxo-and-profiles>`_
      -  :doc:`AD9371/AD9375 No-OS System Level Design Setup </solutions/reference-designs/adrv9371x/no-os-setup>`
      -  :doc:`HDL Reference Design </solutions/reference-designs/adrv9371x/reference_hdl>` which you must use in your FPGA.
      -  `Transceiver Toolbox: HDL Targeting with MATLAB and Simulink <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_

-  `Additional Documentation about SDR Signal Chains - The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_
-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Videos
------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`iiosdr.mp4 <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`_

ADI Articles
~~~~~~~~~~~~

-   Four Quick Steps to Production: Using Model-Based Design for
    Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

Warning
-------

.. esd-warning::
