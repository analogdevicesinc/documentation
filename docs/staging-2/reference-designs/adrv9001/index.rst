.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9001

.. _adrv9001:

ADRV9001/2 Prototyping Platform User Guide
==========================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/16658_50037.png
   :width: 200px

The :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` (low band, 30MHz – 3GHz) and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` (high band, 3GHz – 6GHz) are FMC radio
cards for the :adi:`ADRV9002` highly integrated RF transceiver, offering dual
channel transmitters and dual channel receivers, integrated synthesizers, and
digital signal processing functions. The IC delivers a versatile combination of
high performance and low power consumption required by battery powered radio
equipment and can operate in both FDD and TDD modes. The ADRV9002 operates from
30 MHz to 6000 MHz covering the VHF, licensed and unlicensed cellular bands, and
ISM bands. The IC is capable of supporting both narrowband and wideband
standards up to 40MHz bandwidth on both receive and transmit.

While the complete chip level design package can be found on
:adi:`the ADI web site <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/42975_50034.jpg
   :width: 600px

User Resources
--------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:dokuwiki:`ask <ad-fmcomms2-ebz/help_and_support>`.

- Gettings Started

  #. :dokuwiki:`What you need to get started <adrv9002/prerequisites>`
  #. :dokuwiki:`Quick Start Guides <adrv9002/quickstart>`

     #. :dokuwiki:`Linux on Zed Board <adrv9002/quickstart/zed>`
     #. :dokuwiki:`Linux on ZC706 <adrv9002/quickstart/zynq>`
     #. :dokuwiki:`Linux on ZCU102 <ADRV9002/quickstart/zynqmp>`
     #. :dokuwiki:`Linux on Arria 10 SoC <adrv9002/quickstart/a10soc>`
     #. :ref:`kuiper`
     #. :ref:`kuiper`

- Software Solutions

::

   - [[resources/tools-software/linux-software/iio_oscilloscope|IIO Scope]]
     - [[resources:tools-software:linux-software:adrv9002_osc_main| ADRV9001/2 IIO Scope View]]
     - [[resources:tools-software:linux-software:adrv9002_plugin|ADRV9001/2 Control IIO Scope Plugin]]
   - [[:resources/tools-software/transceiver-toolbox|Transceiver Toolbox for MATLAB and Simulink]]
   - [[/resources/tools-software/linux-software/gnuradio|GNU Radio]]
   - [[:resources/tools-software/linux-software/pyadi-iio|Python Interfaces]]
   - [[resources:tools-software:linux-software:libiio:cmd_line|IIO Command Line Tools]]
   - Generic language support
* Embedded Resources
   - [[resources:tools-software:linux-drivers:iio-transceiver:adrv9002|
     ADRV9001/2 Linux Device Driver]]
   -
     [[resources:tools-software:linux-drivers:iio-transceiver:adrv9002-customization|ADRV9001/2 Device Driver Customization]]
   - [[resources:tools-software:linux-drivers:axi-dmac| AXI-DMAC DMA Controller
     Linux Driver]]
   - [[resources:tools-software:linux-drivers:iio-adc:axi-adc-hdl|AXI ADC HDL
     Linux Driver]]
   - [[resources:tools-software:linux-drivers:iio-dds:axi-dac-dds-hdl|AXI DAC
     HDL Linux Driver]]
   - [[.:ad-fmcomms2-ebz:software:linux:zynq_tips_tricks|Customizing the
     devicetree on the target]]
   - [[/resources/eval/user-guides/ADRV9002/no-os-setup|ADRV9001/2 No-OS System
     Level Design Setup]]
   - [[resources:tools-software:linux-build:generic:zynqmp|Building the ZynqMP /
     MPSoC Linux kernel and devicetrees from source]]
* FPGA Resources
   - [[:resources/eval/user-guides/adrv9002/reference_hdl|HDL Reference Design]]
     which you must use in your FPGA.
   - [[:resources/eval/user-guides/adrv9002/axi_adrv9002|AXI_ADRV9002 Interface
     Core]]
   - [[resources:fpga:docs:hdl|ADI Reference Designs HDL User Guide]]
   - [[:resources/tools-software/transceiver-toolbox|HDL Targeting From MATLAB
     and Simulink]]
* Hardware Resources
   - [[adi>ADRV9002|ADRV9002 Product page]]
   -
     [[adi>en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html|Full Datasheet and chip design package]]

- :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`
- For Hardware technical support go to:

  -  :ez:`Design Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/design-support-adrv9001-adrv9007>`

- For Evaluation System Software support (TES GUI, ADRV9001 API driver, etc.) go
  to:

::

   * [[ez>wide-band-rf-transceivers/tes-gui-software-support-adrv9001-adrv9007 | TES GUI Software Support Community ADRV9001-ADRV9007 ]]
* For questions regarding the HDL reference design please use the
     * [[ez>community/fpga|FPGA Reference Designs]] sub-community.
* For questions regarding the the ADI Linux distribution, the Linux drivers, or
  the device trees for the ADRV9001/2 based platforms, please use the
   * [[ez>community/linux-device-drivers/linux-software-drivers|Linux Software
     Drivers]] sub-community.
* For questions regarding the no-OS drivers for ADRV9001/2, please use the
   *
     [[ez>community/linux-device-drivers/microcontroller-no-os-drivers|Microcontroller and No-OS Driver]] sub-community.
* [[.:ad-fmcomms1-ebz:math|Additional Documentation about SDR Signal Chains -
  The math behind the RF]]

Downloads
---------

Binaries:

Osc for windows can be downloaded directly from Github. Go to to the following
link and download the latest release.

- :git-iio-oscilloscope:`IIO-Scope <releases+>`

The latest boot files for adrv9002 (for all supported carriers) can be found in
the latest Kuiper Image release (note one can choose between downloading the
full image or just the boot partition):

::

   *[[:resources:tools-software:linux-software:adi-kuiper_images:release_notes#release_image|Kuiper Image]]

<hidden Older releases (Click to expand)>

- `ADRV9002_ZCU102_SDCARD_BOOT_FILES_JULY17.zip <http://swdownloads.analog.com/cse/tmp/ADRV9002_ZCU102_SDCARD_BOOT_FILES_JULY17.zip>`__
- `adrv9002_2019_r2_prerelease.zip <http://swdownloads.analog.com/cse/tmp/adrv9002_2019_r2_prerelease.zip>`__
- `adrv9002_B0_2019_r2_prerelease.zip <http://swdownloads.analog.com/cse/tmp/B0_2019_r2_pre_release_zcu102.zip>`__
- `adrv9002_B0_2019_r2_4_1_2021.zip <http://swdownloads.analog.com/cse/tmp/B0_2019_r2_4_1_2021_zcu102.zip>`__

</hidden> Source code have been posted on following branches on github, or has
been already merged into master:

- :git-linux:`drivers/iio/adc/navassa`
- :git-hdl:`adrv9001_zcu102:projects/adrv9001`
- :git-iio-oscilloscope:`plugins/adrv9002.c`
- :git-pyadi-iio:`examples/adrv9002_example.py`

Videos
------

- :adi:`ADRV9002: Narrow to Wide Band Integrated RF Transceiver <en/education/education-library/videos/6170462863001.html>`

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

-  Four Quick Steps to Production: Using Model-Based Design for Software-Defined
  Radio
- :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
- :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
- :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
- :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices" RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning
