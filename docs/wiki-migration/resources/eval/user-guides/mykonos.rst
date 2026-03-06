AD9371 & AD9375 Prototyping Platform User Guide
===============================================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9371-bc_196-adi_m.png
   :align: left
   :width: 300px

The :adi:`ADRV9371-W/PRBZ <EVAL-ADRV9371>`, :adi:`ADRV9371-N/PCBZ <EVAL-ADRV9371>` and :adi:`ADRV9375-N/PCBZ <ADRV9375>` are FMC radio cards for the :adi:`AD9371` respectively :adi:`AD9375`, a highly integrated RF Transceiver™. While the complete chip level design package can be found on the the :adi:`the ADI web site <en/license/licensing-agreement/ad9371.html>`, information on the card and how to use it, the design package that surrounds it, and the software which can make it work can be found here.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9371-n_pcbz_side.jpg
   :align: center
   :width: 600px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  Use the board to better understand the AD9371/AD9375

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/mykonos/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/mykonos/quickstart>`

      -  :doc:`Linux on ZC706 </wiki-migration/resources/eval/user-guides/mykonos/quickstart/zynq>`
      -  :doc:`Linux on Arria 10 SOC </wiki-migration/resources/eval/user-guides/adrv9371/quickstart/a10soc>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

         -  :doc:`AD9371/AD9375 IIO Scope View </wiki-migration/resources/tools-software/linux-software/ad9371_osc_main>`
         -  :doc:`AD9371/AD9375 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/ad9371_plugin>`
         -  :doc:`Advanced AD9371/AD9375 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/ad9371_advanced_plugin>`

      -  :doc:`FRU EEPROM Utility </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

   -  Push custom data into/out of the AD9371/AD9375

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/mykonos/software/basic_iq_datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/transceiver-toolbox>`
      -  :doc:`Python Interfaces </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`

-  Design with the AD9371/AD9375

   -  :doc:`Understanding the AD9371/AD9375 </wiki-migration/resources/eval/user-guides/mykonos/ad9371>`

      -  :adi:`AD9371 Product page <AD9371>`
      -  :adi:`AD9375 Product page <AD9375>`
      -  :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      -  :doc:`MATLAB Filter Wizard / Profile Generator for AD9371 </wiki-migration/resources/eval/user-guides/mykonos/software/filters>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`Transceiver Toolbox </wiki-migration/resources/tools-software/transceiver-toolbox>`

   -  Design a custom AD9371/AD9375 based platform

      -  Linux software

         -  :doc:`AD9371/AD9375 Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`

            -   :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         -  :doc:`AD9528 Low Jitter Clock Generator Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-pll/ad9528>`
         -  :doc:`AD7291 IIO ADC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad7291>`
         -  :doc:`JESD204B Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            -  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`

         -  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            -  :doc:`JESD204 Eye Scan </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`

         -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      -  :doc:`Changing the VCXO frequency and updating the default RF Transceiver Profile </wiki-migration/resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
      -  :doc:`AD9371/AD9375 No-OS System Level Design Setup </wiki-migration/resources/eval/user-guides/mykonos/no-os-setup>`
      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/mykonos/reference_hdl>` which you must use in your FPGA.
      -  :doc:`Transceiver Toolbox: HDL Targeting with MATLAB and Simulink </wiki-migration/resources/tools-software/transceiver-toolbox>`

-  :doc:`Additional Documentation about SDR Signal Chains - The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`
-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Videos
------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4
   :alt: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

-   Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

   -  :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   -  :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   -  :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   -  :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

-  `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`__
-  `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`__

Warning
-------

.. esd-warning::

