
.. _adrv9002- eval:

EVAL-ADRV9002
===============================================================================

.. Add a picture here of the chip

.. image:: images/ADRV9002-SP-TAG-chip-illustration.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

.. important::

   The ADRV9001 is family designator assigned to the System Development User
   Guide (UG-1828) for new ADRV9002, ADRV9003, ADRV9004, and upcoming additional
   family members. Thus, throughout this document, ADRV9001 designator may be
   used to refer to either ADRV9002, ADRV9003 or ADRV9004.

The ADRV9002 is a highly integrated RF transceiver that has dual-channel
transmitters, dual-channel receivers, integrated synthesizers, and digital
signal processing functions.

The ADRV9002 is a high performance, highly linear, high dynamic range
transceiver designed for performance vs. power consumption system
optimization. The device is configurable and ideally suited to demanding,
low power, portable and battery powered equipment. The ADRV9002 operates
from 30 MHz to 6000 MHz and covers the UHF, VHF, industrial, scientific,
and medical (ISM) bands, and cellular frequency bands in narrow-band
(kHz) and wideband operation up to 40 MHz. The ADRV9002 is capable of
both TDD and FDD operation.

The transceiver consists of direct conversion signal paths with
state-of-the-art noise figure and linearity. Each complete receiver and
transmitter subsystem includes dc offset correction, quadrature error
correction (QEC), and programmable digital filters, which eliminate the
need for these functions in the digital baseband. In addition, several
auxiliary functions, such as auxiliary analog-to-digital converters
(ADCs), auxiliary digital-to-analog converters (DACs), and
general-purpose inputs/outputs (GPIOs), are integrated to provide
additional monitoring and control capability.


Features:

- 2 × 2 highly integrated transceiver
- Frequency range of 30 MHz to 6000 MHz
- Transmitter and receiver bandwidth from 12 kHz to 40 MHz
- Two fully integrated, fractional-N, RF synthesizers
- LVDS and CMOS synchronous serial data interface options
- Low power monitor and sleep modes
- Multichip synchronization capabilities
- Fast frequency hopping
- Dynamic profile switching for dynamic data rates and sample rates
- Fully integrated DPD for narrow-band and wideband waveforms
- Fully programmable via a 4-wire SPI
- 12 mm × 12 mm, 196-ball CSP_BGA

Applications:

- Mission critical communications
- Very high frequency (VHF), ultrahigh frequency (UHF), and cellular
  to 6 GHz
- Time division duplexing (TDD) and frequency division duplexing (FDD)
  applications

:adi:`EVAL-AD9002` looks like this, with 2x ADCs and 2x DACs. The evaluation
boards are available in two variants: ADRV9002NP/W1/PCBZ (narrowband) and
ADRV9002NP/W2/PCBZ (wideband).

.. image:: images/eval-adrv9002.gif
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   adrv9002_plugin

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADRV9002`, we recommend to use
the :adi:`EVAL-AD9002` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`adrv9002 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`adrv9002 prerequisites` - what you need to get started
   #. :ref:`adrv9002 quickstart`:

      #. Using the :ref:`ZedBoard <adrv9002-zed>`
      #. Using the :ref:`ZC706 <adrv9002-zc706>`
      #. Using the :ref:`ZCU102 <adrv9002-zcu102>`
      #. Using the :ref:`Arria 10 SoC <adrv9002-a10soc>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Software Solutions

      #. :ref:`iio-oscilloscope`
      #. :ref:`adrv9002-plugin`
      #. :external+scopy:doc:`Scopy <index>`
      #. :external+scopy:doc:`ADRV9002 Scopy Plugin <plugins/adrv9002/adrv9002>`
      #. `IIO Command Line Tools <https://analogdevicesinc.github.io/documentation/software/libiio/cli.html>`_
      #. `Python Interfaces <https://analogdevicesinc.github.io/documentation/software/pyadi-iio/index.html>`_

#. Design with the  ADRV9002

   #. :ref:`adrv9002 block-diagram`

      #. :adi:`ADRV9002 product page <ADRV9002>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
      #. `Transceiver Toolbox <https://analogdevicesinc.github.io/TransceiverToolbox/master/>`_

   #. Resources for designing a custom ADRV9002-based platform software

     #. For Linux software:

        #. About the device driver:

           #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
           #. :external+linux:doc:`AXI DAC HDL Linux driver <drivers/iio-dds/axi-dac-dds-hdl>`
           #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`
           #. :external+linux:doc:`ADRV9002 Linux device driver <drivers/iio-transceiver/adrv9002>`
           #. :external+linux:doc:`ADRV9002 Driver Customization <drivers/iio-transceiver/adrv9002-customization>`

        #. About the device tree:

           #. :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

     #. For no-OS software:

        #. :external+no-OS:doc:`ADRV9001 no-OS Example Project <projects/rf-transceiver/adrv9001>`
        #. :external+no-OS:doc:`ADRV9002 no-OS Driver <drivers/rf-transceiver/navassa>`
        #. :dokuwiki:`no-OS IIO </resources/tools-software/no-os-software/iio>`

     #. FPGA Resources:

        #. :external+hdl:ref:`HDL reference design <adrv9001>` which you must use in your FPGA.
        #. :external+hdl:doc:`AXI ADRV9001 HDL Library <library/axi_adrv9001/index>`
        #. :external+hdl:ref:`HDL User Guide <user_guide>`



.. _adrv9002 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/adrv9002-fbl.png
   :align: center
   :width: 800


Videos
-------------------------------------------------------------------------------

ADRV9002 RF Agile Transceiver Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: https://www.analog.com/en/resources/media-center/videos/6170462863001.html

ADRV9002 Dual, Narrow and Wideband Integrated Transceiver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: https://www.analog.com/en/resources/media-center/videos/6248890375001.html

ADI articles
-------------------------------------------------------------------------------

  MathWorks webinars
  -------------------------------------------------------------------------------

.
  #. :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
  #. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`


Additional information
-------------------------------------------------------------------------------

Four Quick Steps to Production - SDR Prototyping Platform Series:

#. :adi:`Part 1—The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
#. :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
#. :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
#. :adi:`Part 4—Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`


Help and support
-------------------------------------------------------------------------------

For Hardware technical support go to:

- :ez:`design-support/design-support-adrv9001-adrv9007`

For Evaluation System Software support (TES GUI, ADRV9001 API driver,
etc.) go to:

- :ez:`sw-interface-tools/tes-gui-software-support-adrv9001-adrv9007`

For questions regarding the HDL reference design please use the:

- :ez:`fpga`

For questions regarding the ADI Linux distribution, the Linux drivers, or
the device trees for the ADRV9001/2 based platforms, please use the:

- :ez:`linux-software-drivers`

For questions regarding the no-OS drivers for ADRV9001/2, please use
the:

- :ez:`microcontroller-no-os-drivers`

Additional Documentation about SDR Signal Chains - The math behind the
RF:

- :adi:`SDR Signal Chains Documentation <en/lp/001/sdr.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
