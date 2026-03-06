.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9364-z7020

.. _adrv9364-z7020:

ADRV9364-Z7020 User Guide
==========================

Introduction
------------

The :adi:`ADRV9364-Z7020 <ADRV9364>` is a System-On-Module (SOM) based on the
Xilinx Zynq-7000 All Programmable SoC (XC7Z020) and the :adi:`AD9364` RF Agile
Transceiver. Operating over a wide tuning range (70 MHz to 6 GHz), it provides
an RF platform for prototyping, evaluation, and as a reference design for
production.

The ADRV9364-Z7020 is schematically and HDL-compatible with the
:ref:`AD-FMCOMMS4-EBZ <ad-fmcomms4-ebz>`. The :adi:`AD9364` is the 1Rx/1Tx
variant of the :adi:`AD9361`, supporting channel bandwidths from less than
200 kHz to 56 MHz.

.. image:: adrv9364-z7020.jpg
   :align: center
   :width: 400

Applications
~~~~~~~~~~~~

- Software-defined radio (SDR)
- Remote radio heads
- Satellite modems
- Test and measurement equipment
- Radar and advanced imaging
- General purpose data acquisition

Hardware Specifications
-----------------------

.. list-table::
   :header-rows: 1

   * - Parameter
     - Value
   * - FPGA
     - Xilinx Zynq XC7Z020 (dual-core ARM Cortex-A9 + PL)
   * - RF Transceiver
     - :adi:`AD9364` (70 MHz to 6 GHz, 200 kHz to 56 MHz channel bandwidth)
   * - Channels
     - 1 Rx x 1 Tx
   * - Data Interface
     - LVDS mode (DDR)
   * - PCB
     - 62 mm x 100 mm
   * - Connectors
     - 4x FCI 0.8 mm BergStak 100-position micro headers (JX1--JX4)

The micro headers are FCI 0.8 mm BergStak 100-position dual-row BTB vertical
receptacles (61082-101400LF) that mate with FCI 0.8 mm BergStak plugs
(61083-10x400LF) for variable stack heights of 5 mm to 8 mm.

Revision History
~~~~~~~~~~~~~~~~

**Revision D** (current shipping version):

- Enhanced power delivery (1 V current increased from 2 A to 4 A).
- RF traces modified to improve insertion loss, return loss, and EVM.

Supported Devices
-----------------

- :adi:`AD9364`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Carrier
     - Description
   * - ADRV1CRR-BOB (PZSDRCC-BRK)
     - Breakout/BOB Carrier (recommended)
   * - ADRV1CRR-FMC (PZSDRCC-FMC)
     - FMC Carrier
   * - PZSDRCC-PCIE
     - PCIe Carrier
   * - PZSDRCC-PackRF
     - PackRF Carrier

.. note::

   Due to the fewer available user I/Os on the Zynq XC7Z020, the
   :adi:`ADRV1CRR-BOB <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-BOB.html>`
   breakout carrier is recommended for the ADRV9364-Z7020.

HDL Reference Design
--------------------

The HDL reference design is based on the
:ref:`AD-FMCOMMS4-EBZ <ad-fmcomms4-ebz>` reference design using the
AD9364 (1Rx, 1Tx variant of AD9361). The LVDS interface is configured for
maximum data throughput and can be reconfigured to CMOS mode for alternate
prototyping.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv9364z7020`

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
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9364-z7020.dtsi`
   * - BOB carrier DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9364-z7020-bob.dts`
   * - BOB carrier (CMOS) DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9364-z7020-bob-cmos.dts`
   * - PackRF carrier DTS
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9364-z7020-packrf.dts`

The following software tools and frameworks are supported:

- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` with AD9361
  control plugins (basic and advanced)
- libiio streaming examples (MATLAB/Simulink)
- GNU Radio support
- AD9361 Filter Design Wizard (MATLAB)
- pyadi-iio (Python)
- No-OS bare-metal driver

More Information
----------------

- :ref:`AD-FMCOMMS4-EBZ User Guide <ad-fmcomms4-ebz>`
- :ref:`AD-FMCOMMS2-EBZ User Guide <ad-fmcomms2-ebz>`
- :ref:`ADRV9361-Z7035 User Guide <adrv9361-z7035>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
