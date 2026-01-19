.. _jupiter-sdr:

Jupiter SDR
===========

Overview
--------

Jupiter is a versatile software-defined platform based on Analog Devices
:adi:`ADRV9002` and  
:xilinx:`Xilinx Zynq UltraScale+ MPSoC. <products/adaptive-socs-and-fpgas/soc/zynq-ultrascale-plus-mpsoc.html>`
:adi:`ADRV9002` is a new generation RF transceiver that has dual-channel
transmitters, dual-channel receivers covering 30 MHz to 6 GHz frequency 
range with very good RF linearity performance and a set of advanced 
features like fast profiles switching, flexible power vs performance 
configuration, fast frequency hopping, multi-chip synchronization and 
DPD for narrow and wide band waveform. The evaluation platform includes
XCZU3EG processing device that has a wide range of interfaces making the
system capable of local processing or streaming to a remote host. It 
comes integrated in a self-contained ruggedised aluminum case which 
gives flexibility in evaluating and prototyping across different 
environments.

.. figure:: jupitersdr_back1.png
   :align: center

.. figure:: jupitersdr_front1.png
   :align: center

.. toctree::
   :hidden:

   quickstart/index
   hardwareoverview
   mcssetup
   knownissues
   refdesign
   profgen

The platform comes with open-source software that includes:

- Linux and no-OS
- HDL reference design
- IIO
- MATLAB
- GNU Radio
- Python

---------------------------------------------------------

Key Features
------------

- RF/SDR
     - ADRV9002 transceiver
         - 2 x RX, 2 x TX
         - LO Frequency range 30 MHz to 6 GHz
         - 12 KHz to 40 MHz frequency bandwidth
         - Sampling rate 12 KS/s to 61.44 MS/s
     - External device clock input
     - External MCS input
     - RF Front-end
- Processing system
     - Zynq UltraScale+ MPSoC XCZU3EG
         - ARM CORTEX-A53 1.5GHz
         - ARM CORTEX-R5 500 MHz
         - Mali-400 MP2 graphic processor
         - Programmable logic 154k
     - DDR4 – 2 GB (x32)
     - Boot source
         - SD CARD 3.0
         - FLASH memory 128MB
- User Interfaces
     - USB 3.1 Gen 1 – Type C
         - Upstream Facing Port (UFP)
         - Downstream Facing Port (DFP)
         - USB 2.0 compatible
     - Ethernet 1000BASE-T RGMII
     - Display Port v1.2 (2 lanes 5.4Gb/s)
     - SATA 3
     - USB (micro) debug interface
     - 16 GPIOs (3V3 LVCMOS)
- Power Sources
     - USB Type-C (power only)
         - Power Sink 5V, 9V/3A
     - USB Type-C (data)
         - Power Sink 5V/3A
         - Power Source 5V/0.9A
     - 802.3at POE compliant, 25.5W Type2 (POE+)

---------------------------------------------------------

User Resources
--------------

People who follow the flow that is outlined, have a much better 
experience with things. However, like many things, documentation is 
never as complete as it should be. If you have any questions, 
feel free to ask.

- Getting Started
     #. :dokuwiki:`What you need to get started <resources/eval/user-guides/jupiter-sdr/quickstart>`
     #. Quick Start Guides
         #. :dokuwiki:`Generate a custom device profile using TES <resources/eval/user-guides/jupiter-sdr/profile_generation_using_tes>`
         #. :dokuwiki:`Configure a pre-existing SD-Card <resources/tools-software/linux-software/kuiper-linux>`
         #. :dokuwiki:`Update the old card you received with your hardware <resources/tools-software/linux-software/kuiper-linux>`
- Software Solutions
     #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`
         #. :dokuwiki:`ADRV9001/2 IIO Scope View <resources/tools-software/linux-software/adrv9002_osc_main>`
         #. :dokuwiki:`ADRV9001/2 Control IIO Scope Plugin <resources/tools-software/linux-software/adrv9002_plugin>`
         #. :dokuwiki:`ADRV9001/2 Profile Generator Plugin <resources/tools-software/linux-software/adrv9002_profile_generator_plugin>`
     #. :dokuwiki:`Transceiver Toolbox for MATLAB and Simulink <resources/tools-software/transceiver-toolbox>`
     #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
     #. :dokuwiki:`Python Interfaces <resources/tools-software/linux-software/pyadi-iio>`
     #. :dokuwiki:`IIO Command Line Tools <resources/tools-software/linux-software/libiio/cmd_line>`
- Embedded Resources
     #. :dokuwiki:`ADRV9001/2 Linux Device Driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9002>`
     #. :dokuwiki:`ADRV9001/2 Device Driver Customization <resources/tools-software/linux-drivers/iio-transceiver/adrv9002-customization>`
     #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
     #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
     #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`
     #. :dokuwiki:`Customizing the devicetree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`
     #. :dokuwiki:`ADRV9001/2 No-OS System Level Design Setup <resources/eval/user-guides/adrv9002/no-os-setup>`
     #. :dokuwiki:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source <resources/tools-software/linux-build/generic/zynqmp>`
- FPGA Resources
     #. :dokuwiki:`HDL Reference Design <resources/eval/user-guides/jupiter_sdr/reference_hdl>` which you must use in your FPGA.
     #. :dokuwiki:`AXI_ADRV9002 Interface Core <resources/eval/user-guides/adrv9002/axi_adrv9002>`
     #. :dokuwiki:`ADI Reference Designs HDL User Guide <resources/fpga/docs/hdl>`
     #. :dokuwiki:`HDL Targeting From MATLAB and Simulink <resources/tools-software/transceiver-toolbox>`
- Hardware Resources
     #. :dokuwiki:`Jupiter SDR Hardware Overview <resources/eval/user-guides/jupiter-sdr/hardware-overview>`
     #. :adi:`ADRV9002 Product page <ADRV9002>`
     #. :adi:`Full Datasheet and chip design package <design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
- :dokuwiki:`Multi-chip synchronization support <resources/eval/user-guides/jupiter_sdr/mcs>`
- :dokuwiki:`Help and Support <resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`
     - Known issues <resources/eval/user-guides/jupiter-sdr/known-issues>`
     - For Hardware technical support go to:
         - :ez:`Design Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/design-support-adrv9001-adrv9007>`
     - For Evaluation System Software support (TES GUI, ADRV9001 API driver, etc.) go to:
         - :ez:`TES GUI Software Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/tes-gui-software-support-adrv9001-adrv9007>`
     - For questions regarding the HDL reference design please use the
         - :ez:`FPGA Reference Designs <community/fpga>` sub-community.
     - For questions regarding the the ADI Linux distribution, the Linux drivers, or the device trees for the ADRV9001/2 based platforms, please use the
         - :ez:`Linux Software Drivers <community/linux-device-drivers/linux-software-drivers>` sub-community.
     - For questions regarding the no-OS drivers for ADRV9001/2, please use the
         - :ez:`Microcontroller and No-OS Driver <community/linux-device-drivers/microcontroller-no-os-drivers>` sub-community.
     - Additional Documentation about SDR Signal Chains - The math behind the RF <>`

---------------------------------------------------------

Downloads
---------

Binaries:

Osc for windows can be downloaded directly from Github. Go to to the following link and download the latest release.

 - :git-iio-oscilloscope:`IIO-Scope <releases+>`

The latest boot files for adrv9002 (for all supported carriers) can be found in the latest Kuiper Image release (note one can choose between downloading the full image or just the boot partition):

 - :dokuwiki:`Kuiper Image <resources/tools-software/linux-software/adi-kuiper_images/release_notes#release_image>`

Below it's an experimental pre-release which enables DMA Coherency on the AXI DMA core. That means the IP core can snoop the caches and so samples can actually live in them. This gave some promising throughput improvements when using libiio IP and USB backends:

 - :download:`Jupiter DMA Coeherent <jupiter-dma-coeherent.tar.gz>`

---------------------------------------------------------

Reference Material
------------------

- :adi:`ADRV9002: Narrow to Wide Band Integrated RF Transceiver <education/education-library/videos/6170462863001.html>`

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

- Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio
     - :adi:`Part 1 - the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
     - :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
     - :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
     - :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

.. esd-warning::