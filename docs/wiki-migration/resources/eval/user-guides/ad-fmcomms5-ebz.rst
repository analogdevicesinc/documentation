AD-FMCOMMS5-EBZ User Guide
==========================

For many Broadband Wireless Access (BWA) systems, Multi Input – Multi Output (`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_) operation and RF beamforming are proven techniques for maximizing throughput and efficient spectrum utilization. Modern integrated devices with multi-channel RX and multi-channel TX capability such as the AD9361 make developing MIMO systems with high performance and linearity utilizing integrated receivers, transmitters, and synthesizers a simpler task.

Some systems may require more complex configurations that combine multiple devices. Operating multiple devices while trying to coordinate data for each channel of each device is not practical for devices that operate independently without any mechanism for aligning data timing. Data synchronization into and out of multiple devices is required to implement such configurations. The :adi:`AD-FMComms5-EBZ` is a FMC board for the :adi:`AD9361`, a highly integrated RF Agile Transceiver™, which demonstrates how to design a platform based on multiple devices.

For MIMO systems requiring more than two input or two output channels, multiple AD9361 devices and a common reference oscillator are required. The AD9361 provides the capability to accept an external reference clock and synchronize operation with other devices using simple control logic. Each AD9361 includes its own baseband PLL that generates sampling and data clocks from the reference clock input, so an additional control mechanism is required to synchronize multiple devices.

The complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found below in the Table of Contents.

The purpose of the AD-FMCOMMS5-EBZ is to provide a platform to which shows how to connect and synchronize (at the RF side) multiple AD9361s for `SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_ applications. To help with algorithm array processing development, there are a variety of things that can be done, from purchasing complete solutions:

-  `MIMO receiver <https://www.xilinx.com/products/intellectual-property/do-di-mimoenc-lte.html>`_
-  `MIMO transmitter <https://www.xilinx.com/products/intellectual-property/ef-di-mimodec-lte.html>`_

To creating your own with something like `Phased Array System Toolbox <https://www.mathworks.com/products/phased-array/>`_.

If you are just starting a design, or investigating the AD9361 for the first time, it's suggested to get familiar with the single AD9361 based platforms (:doc:`ad-fmcomms2-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>` or :doc:`ad-fmcomms3-ebz </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>`) first.

Note that the AD-FMCOMMS5-EBZ uses a dual FMC connector. This means the base board requires two adjacent FMC connectors. Suitable base boards for example are ZC702 and ZC706.

Table of Contents
=================

`ad-fmcomms5-ebz.ashx <https://wiki.analog.com/_media/http///www.analog.com/-/media/analog/en/evaluation-board-images/images/ad-fmcomms5-ebz.ashx>`_

-  :doc:`Introduction </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
-  :doc:`FMCOMMS5 Hardware </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/hardware>`: This provides a brief description of the AD-FMCOMMS5-EBZ board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/hardware>` (including :doc:`schematics </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/hardware>`)

      -  :doc:`Functional Overview & Specifications </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`
      -  :doc:`Characteristics & Performance </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/card_specification>`
      -  :doc:`Configuration options </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/hardware/configuration_options>`

   -   :doc:`Production Testing Process </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/testing>`

-  Use the AD-FMCOMMS5-EBZ Board to better understand the AD9361

   -  :doc:`What you need to get started </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`
   -  :doc:`Quick Start Guides </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      -  :doc:`Linux on ZC702, ZC706, ZED </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`
      -  :doc:`Linux on KC705, VC707 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/microblaze>`
      -  :doc:`Configure a pre-existing SD-Card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
      -  :doc:`Update the old card you received with your hardware </wiki-migration/resources/tools-software/linux-software/zynq_images>`

   -  Linux Applications

      -  :doc:`IIO Scope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
      -  :doc:`FMCOMMS5 Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms5_plugin>`
      -  :doc:`FMCOMMS2/3/4/5 Advanced Control IIO Scope Plugin </wiki-migration/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      -  :doc:`FMComms5 Phase Sync Procedure </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/phase-sync>`
      -  :doc:`Command Line/Shell scripts </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   -  Push custom data into/out of the AD-FMCOMMS5-EBZ

      -  :doc:`Basic Data files and formats </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      -  :doc:`Create and analyze data files in MATLAB </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      -  :doc:`AD9361 libiio streaming example </wiki-migration/resources/tools-software/linux-software/libiio>`

-  Design with the AD9361

   -  :doc:`Understanding the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :doc:`MATLAB Filter Design Wizard for AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   -  Designing with multiple AD9361s.

      -  :doc:`Multi-Chip Sync(MCS) </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz/multi-chip-sync>`, synchronization of multiple devices

   -  Simulation

      -  :doc:`MathWorks SimRF Models of the AD9361 </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :doc:`Stream data into/out of MATLAB </wiki-migration/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         -  :doc:`Beacon Frame Receiver Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         -  :doc:`QPSK Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         -  :doc:`LTE Transmit and Receive Example </wiki-migration/resources/tools-software/linux-software/libiio/clients/lte_example>`

      -  :doc:`GNU Radio </wiki-migration/resources/tools-software/linux-software/gnuradio>`
      -  :doc:`FM Radio/Tuner </wiki-migration/resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :doc:`C example </wiki-migration/resources/tools-software/linux-software/libiio>`

   -  Design a custom AD9361 based platform

      -  :doc:`Linux software </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         -  :doc:`Linux Device Driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         -  :doc:`Build the demo on ZC702, ZC706, or ZED from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         -  :doc:`Build the demo on KC705 or VC707 for Microblaze from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`
         -  :doc:`Build the 2014_R2 Release Linux kernel from source </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         -  :doc:`Customizing the devicetree on the target </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      -  :doc:`No-OS Driver </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`
      -  :doc:`HDL Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>` which you must use in your FPGA.

         -  :doc:`Digital Interface Timing Validation </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

-  Additional Documentation about SDR Signal Chains

   -  :doc:`The math behind the RF </wiki-migration/resources/eval/user-guides/ad-fmcomms1-ebz/math>`
   -  :doc:`IQ rotation, and phase sync </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/iq_rotation>`

-  :doc:`Help and Support </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Videos
======


.. note::

   See `ad-fmcomms2-ebz <https://wiki.analog.com/ad-fmcomms2-ebz#videos>`_


Presentations
=============

-  :adi:`Developing Multiple-Input Multiple-Output (MIMO) Systems with the AD9361 <en/education/education-library/webcasts/developing-multiple-input-multiple-output.html>` As Software Defined Radio (SDR) and Multiple-Input Multiple-Output (MIMO) become more prevalent there is a need for more channel diversity. This webcast will detail how to use multiple AD9361 devices to create an NxN MIMO system, as well as explore the available tradeoffs in the design. The AD9361 is a fully integrated 2x2 MIMO transceiver. Its programmability and wideband capability make it ideal for a broad range of transceiver applications.

Warning
-------


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_

