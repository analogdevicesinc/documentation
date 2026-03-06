Jupiter SDR
===========

Overview
--------

Jupiter is a versatile software-defined platform based on Analog Devices :adi:`ADRV9002` and Xilinx `Zynq UltraScale+ MPSoC <https://www.xilinx.com//products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`__. ADRV9002 is a new generation RF transceiver that has dual-channel transmitters, dual-channel receivers covering 30 MHz to 6 GHz frequency range with very good RF linearity performance and a set of advanced features like fast profiles switching, flexible power vs performance configuration, fast frequency hopping, multi-chip synchronization and DPD for narrow and wide band waveform. The evaluation platform includes XCZU3EG processing device that has a wide range of interfaces making the system capable of local processing or streaming to a remote host. It comes integrated in a self-contained ruggedised aluminum case which gives flexibility in evaluating and prototyping across different environments.

|jupitersdr_back1.png| |jupitersdr_front1.png|

The platform comes with open-source software that includes:

-  Linux and no-OS
-  HDL reference design
-  IIO
-  MATLAB
-  GNU Radio
-  Python

--------------

Key Features
------------

-  RF/SDR

   -  ADRV9002 transceiver

      -  2 x RX, 2 x TX
      -  LO Frequency range 30 MHz to 6 GHz
      -  12 KHz to 40 MHz frequency bandwidth
      -  Sampling rate 12 KS/s to 61.44 MS/s

   -  External device clock input
   -  External MCS input
   -  RF Front-end

-  Processing system

   -  Zynq UltraScale+ MPSoC XCZU3EG

      -  ARM CORTEX-A53 1.5GHz
      -  ARM CORTEX-R5 500 MHz
      -  Mali-400 MP2 graphic processor
      -  Programmable logic 154k

   -  DDR4 – 2 GB (x32)
   -  Boot source

      -  SD CARD 3.0
      -  FLASH memory 128MB

-  User Interfaces

   -  USB 3.1 Gen 1 – Type C

      -  Upstream Facing Port (UFP)
      -  Downstream Facing Port (DFP)
      -  USB 2.0 compatible

   -  Ethernet 1000BASE-T RGMII
   -  Display Port v1.2 (2 lanes 5.4Gb/s)
   -  SATA 3
   -  USB (micro) debug interface
   -  16 GPIOs (3V3 LVCMOS)

-  Power Sources

   -  USB Type-C (power only)

      -  Power Sink 5V, 9V/3A

   -  USB Type-C (data)

      -  Power Sink 5V/3A
      -  Power Source 5V/0.9A

   -  802.3at POE compliant, 25.5W Type2 (POE+)

--------------

User Resources
--------------

People who follow the flow that is outlined, have a much better experience with things. However, like many things, documentation is never as complete as it should be. If you have any questions, feel free to :doc:`ask </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

-  Getting Started

   -  `What you need to get started <https://wiki.analog.com/.jupiter-sdr/quickstart>`__
   -  Quick Start Guides

      -  `Generate a custom device profile using TES <https://wiki.analog.com/.jupiter-sdr/profile_generation_using_tes>`__
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

-  Software Solutions

   -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

      -  :doc:`ADRV9001/2 IIO Scope View </wiki-migration/resources/tools-software/linux-software/adrv9002_osc_main>`

         -  :doc:`ADRV9001/2 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/adrv9002_plugin>`
         -  :doc:`ADRV9001/2 Profile Generator Plugin </wiki-migration/resources/tools-software/linux-software/adrv9002_profile_generator_plugin>`

      -  :doc:`Transceiver Toolbox for MATLAB and Simulink </wiki-migration/resources/tools-software/transceiver-toolbox>`
      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`Python Interfaces </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
      -  :doc:`IIO Command Line Tools </wiki-migration/resources/tools-software/linux-software/libiio/cmd_line>`

-  Embedded Resources

   -  :doc:`ADRV9001/2 Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`

      -  :doc:`ADRV9001/2 Device Driver Customization </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
      -  :doc:`AXI-DMAC DMA Controller Linux Driver </wiki-migration/resources/tools-software/linux-drivers/axi-dmac>`
      -  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
      -  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
      -  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`
      -  :doc:`ADRV9001/2 No-OS System Level Design Setup </wiki-migration/resources/eval/user-guides/adrv9002/no-os-setup>`
      -  :doc:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </wiki-migration/resources/tools-software/linux-build/generic/zynqmp>`

-  FPGA Resources

   -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/jupiter_sdr/reference_hdl>` which you must use in your FPGA.

      -  :doc:`AXI_ADRV9002 Interface Core </wiki-migration/resources/eval/user-guides/adrv9002/axi_adrv9002>`
      -  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
      -  :doc:`HDL Targeting From MATLAB and Simulink </wiki-migration/resources/tools-software/transceiver-toolbox>`

-  Hardware Resources

   -  `Jupiter SDR Hardware Overview <https://wiki.analog.com/.jupiter-sdr/hardware-overview>`__

      -  :adi:`ADRV9002 Product page <ADRV9002>`
      -  :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`

-  :doc:`Multi-chip synchronization support </wiki-migration/resources/eval/user-guides/jupiter_sdr/mcs>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

   -  `Known issues <https://wiki.analog.com/.jupiter-sdr/known-issues>`__
   -  For Hardware technical support go to:

      -   :ez:`Design Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/design-support-adrv9001-adrv9007>`

   -  For Evaluation System Software support (TES GUI, ADRV9001 API driver, etc.) go to:

      -  :ez:`TES GUI Software Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/tes-gui-software-support-adrv9001-adrv9007>`

   -  For questions regarding the HDL reference design please use the

      -  :ez:`FPGA Reference Designs <community/fpga>` sub-community.

   -  For questions regarding the the ADI Linux distribution, the Linux drivers, or the device trees for the ADRV9001/2 based platforms, please use the

      -  :ez:`Linux Software Drivers <community/linux-device-drivers/linux-software-drivers>` sub-community.

   -  For questions regarding the no-OS drivers for ADRV9001/2, please use the

      -  :ez:`Microcontroller and No-OS Driver <community/linux-device-drivers/microcontroller-no-os-drivers>` sub-community.

   -  :doc:`Additional Documentation about SDR Signal Chains - The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`

--------------

Downloads
---------

Binaries:

Osc for windows can be downloaded directly from Github. Go to to the following link and download the latest release.

-  :git-iio-oscilloscope:`IIO-Scope <releases>`

The latest boot files for adrv9002 (for all supported carriers) can be found in the latest Kuiper Image release (note one can choose between downloading the full image or just the boot partition):

::

   *[[/resources/tools-software/linux-software/adi-kuiper_images/release_notes#release_image|Kuiper Image]]

Below it's an **experimental** pre-release which enables DMA Coherency on the AXI DMA core. That means the IP core can snoop the caches and so samples can actually live in them. This gave some promising throughput improvements when using libiio IP and USB backends:

::

   *[[https://wiki.analog.com/_media/resources/tools-software/linux-software/adrv9001/jupiter-dma-coeherent.tar.gz|Jupiter DMA Coeherent]]

--------------

Reference Material
------------------

-  :adi:`ADRV9002: Narrow to Wide Band Integrated RF Transceiver <en/education/education-library/videos/6170462863001.html>`

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


.. |jupitersdr_back1.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/jupitersdr_back1.png
   :width: 550px
   :height: 300px
.. |jupitersdr_front1.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/jupiter-sdr/jupitersdr_front1.png
   :width: 550px
   :height: 300px
