.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035

.. _adrv9361-z7035:

ADRV9361-Z7035 User Guide
==========================

Introduction
------------

The :adi:`ADRV9361-Z7035` is a System-On-Module (SOM) based on the Xilinx
Zynq-7000 All Programmable SoC and the :adi:`AD9361` RF Agile Transceiver.
Operating over a wide tuning range (70 MHz to 6 GHz), it provides an RF
platform for prototype, evaluation, and reference design purposes.

The ADRV9361-Z7035 is schematically and HDL-compatible with the
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`.

The :adi:`AD9361` combines an RF front end with a flexible mixed-signal
baseband section and integrated frequency synthesizers, simplifying design-in
by providing a configurable digital interface to a processor or FPGA. It
supports channel bandwidths from less than 200 kHz to 56 MHz and is suitable
for applications including:

- Wireless communications and software-defined radio
- Remote radio heads
- Satellite modems
- Test and measurement equipment
- Radar and advanced imaging
- General purpose data acquisition

.. toctree::
   :hidden:

   hardware
   quickstart

Supported Devices
-----------------

- :adi:`AD9361`

HDL Reference Design
--------------------

The HDL reference design is the same as the
:ref:`AD-FMCOMMS2-EBZ/AD-FMCOMMS3-EBZ <ad-fmcomms2-ebz>` reference design.
The LVDS interface is configured for maximum data throughput and can be
reconfigured to CMOS mode for alternate prototyping.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv9361z7035`

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

- :git-linux:`drivers/iio/adc/ad9361.c`

Device Trees
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - SOM base DTSI
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035.dtsi`
   * - FMC carrier DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035-fmc.dts`
   * - BOB carrier DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035-bob.dts`
   * - PackRF carrier DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035-packrf.dts`

The following software tools and frameworks are supported:

- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` with AD9361
  control plugins (basic and advanced)
- libiio streaming examples (MATLAB/Simulink)
- GNU Radio support
- AD9361 Filter Design Wizard (MATLAB)
- MathWorks RF Blockset models
- No-OS bare-metal driver

More Information
----------------

- :ref:`AD-FMCOMMS2-EBZ User Guide <ad-fmcomms2-ebz>`
- :ref:`AD-FMCOMMS3-EBZ User Guide <ad-fmcomms3-ebz>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
