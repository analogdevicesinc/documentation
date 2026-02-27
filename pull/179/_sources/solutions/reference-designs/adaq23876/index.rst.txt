.. imported from: https://wiki.analog.com/resources/eval/user-guide/adaq23876/adaq23878

.. _adaq23876:

ADAQ23876/ADAQ23878 User Guide
==============================

Introduction
------------

The :adi:`ADAQ23876` and :adi:`ADAQ23878` are high-speed, 16-bit and 18-bit,
15 MSPS data acquisition uModule systems that integrate a precision SAR ADC
(based on the :adi:`LTC2387-18` core), a precision reference, a reference
buffer, and a high-bandwidth ADC driver into a single system-in-package (SiP).
These devices are part of the Low Harmonic Interleaving (LHI) family of
high-speed SAR ADCs, which enables multi-channel interleaving while maintaining
low harmonic distortion.

The EVAL-ADAQ23876 and EVAL-ADAQ23878 evaluation boards provide an analog
front-end and an FMC digital interface for evaluating these devices using a
ZedBoard FPGA platform. The boards include on-board reference oscillators and
retiming circuits to minimize SNR degradation from FPGA clock jitter.

By integrating critical signal chain components into a compact package, the
ADAQ23876 and ADAQ23878 simplify board-level design, reduce overall solution
size, and provide optimized performance that would otherwise require extensive
design effort with discrete components.

Supported Devices
-----------------

- :adi:`ADAQ23876`
- :adi:`ADAQ23878`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Hardware
--------

Required Hardware
~~~~~~~~~~~~~~~~~

- EVAL-ADAQ23876 or EVAL-ADAQ23878 evaluation board
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
- 12 V power supply
- SD card (at least 16 GB) with :doc:`Kuiper Linux </linux/kuiper/index>`
- LAN cable for network connection to the ZedBoard
- SMA cables and XLR-to-SMA adapter for analog input
- Audio analyzer (Audio Precision APX525 recommended) for evaluation

.. important::

   The VADJ for the ZedBoard must be set to 2.5 V.

Power Supply Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board features multiple on-board regulators that generate the
required supply rails:

.. list-table::
   :header-rows: 1

   * - Rail
     - Voltage
     - Regulator
   * - VS+
     - +7 V
     - :adi:`LTM8049` + :adi:`ADP7118`
   * - VDD
     - +5 V
     - :adi:`ADP7118`
   * - VIO
     - +2.5 V
     - :adi:`LT3023`
   * - VS-
     - -2.0 V
     - :adi:`LTM8049` + :adi:`ADP7183`

A single ground plane is used on the board to minimize the effect of high
frequency noise interference.

Analog Input
~~~~~~~~~~~~

The SMA connectors (VIN+, VIN-) support three configuration paths:

- Direct input to the ADAQ23876/ADAQ23878
- Through optional :adi:`ADA4899-1` amplifiers in unity-gain mode
- Via :adi:`ADG774` switch matrix for signal routing

The board supports configurable input ranges through multiple gain
configurations (0.37 to 2.25) and a choice between the 4.096 V :adi:`LTC6655`
or 2.048 V :adi:`ADR4520` precision reference.

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Jumper
     - Position
     - Function
   * - P1 (PD_N)
     - Pins 1-2
     - Enabled (default)
   * - P1 (PD_N)
     - Pins 2-3
     - Powered down
   * - P2 (TESTPAT)
     - Pins 1-2
     - Test pattern active
   * - P2 (TESTPAT)
     - Pins 2-3
     - Test pattern inactive (default)
   * - P3 (TWOLANES)
     - Pins 1-2
     - Two-lane mode (default)
   * - P3 (TWOLANES)
     - Pins 2-3
     - One-lane mode

HDL Reference Design
--------------------

The ADAQ23876/ADAQ23878 share the same HDL reference design as the
:adi:`ADAQ23875`. The design implements the ``axi_ltc2387`` IP core, which
provides a parallel LVDS data interface to the ADC. The captured data is moved
from the IP core output to system memory via a DMA engine.

The ``ADC_RES`` build parameter selects the appropriate resolution:

- ``ADC_RES=16`` for the ADAQ23876 (16-bit)
- ``ADC_RES=18`` for the ADAQ23878 (18-bit, default)

HDL IP Core Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

- `AXI LTC2387 IP core documentation <https://analogdevicesinc.github.io/hdl/library/axi_ltc2387/index.html>`__

HDL Project Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

- `ADAQ23875 HDL project documentation <https://analogdevicesinc.github.io/hdl/projects/adaq23875/index.html>`__

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adaq23875`
- :git-hdl:`library/axi_ltc2387`

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

For the ADAQ23876 (16-bit):

.. code-block:: bash

   cd hdl/projects/adaq23875/zed
   make ADC_RES=16

For the ADAQ23878 (18-bit):

.. code-block:: bash

   cd hdl/projects/adaq23875/zed
   make ADC_RES=18

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Quick Start
-----------

1. Flash the :doc:`Kuiper Linux </linux/kuiper/index>` image onto the SD card.
2. Configure the boot files (BOOT.BIN, devicetree.dtb, uImage) for the
   ADAQ23876 or ADAQ23878 design.
3. Insert the SD card into the ZedBoard.
4. Attach the EVAL-ADAQ23876 or EVAL-ADAQ23878 evaluation board to the
   ZedBoard FMC connector.
5. Connect the analog signal source via the XLR-to-SMA adapter.
6. Power the board with the 12 V supply.
7. Connect to the board via LAN and use
   :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` for data
   capture and visualization.

Software Support
----------------

Linux Driver
~~~~~~~~~~~~

The ADAQ23876 and ADAQ23878 use the LTC2387 Linux IIO driver, which provides
buffered data capture and sampling frequency control through the IIO subsystem.

Driver and device tree source files:

- :git-linux:`drivers/iio/adc/ltc2387.c`
- :git-linux:`arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ltc2387.dts`

IIO Oscilloscope
~~~~~~~~~~~~~~~~

The :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application
provides a graphical interface for data capture and analysis. It supports:

- Time domain and frequency domain (FFT) plotting
- DMM tab for continuous voltage readings
- Data export in CSV, MAT, and PNG formats

For FFT analysis, Blackman-Harris windowing is recommended for optimal
performance evaluation.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`ADAQ23876 Product Page <ADAQ23876>`
- :adi:`ADAQ23878 Product Page <ADAQ23878>`
- :doc:`ADAQ23875 User Guide </solutions/reference-designs/adaq23875/index>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
