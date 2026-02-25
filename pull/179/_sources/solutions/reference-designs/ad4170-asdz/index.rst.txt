.. _ad4170-asdz:

AD4170-ASDZ User Guide
=======================

Introduction
------------

The :adi:`AD4170` is a multiplexed, 24-bit, sigma-delta analog-to-digital
converter (ADC) featuring a 5.5 nV/rtHz ultra-low-noise core (at gain = 128),
integrated programmable gain amplifier (PGA), and programmable digital filter.
The device includes an integrated 5 ppm/C reference, a programmable 12-bit
DAC, and comprehensive measurement diagnostics, making it suitable for
multi-sensor measurement applications.

The EVAL-AD4170-4ARDZ evaluation board provides all the necessary hardware to
interact with the device using an FPGA development board via an Arduino shield
connector. The HDL reference design supports continuous data capture at the
maximum sample rate.

Supported Devices
-----------------

- :adi:`AD4170`

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Carrier
     - Connector
   * - `Cora Z7S <https://digilent.com/reference/programmable-logic/cora-z7/start>`__
     - Arduino shield
   * - `DE10-Nano <https://www.terasic.com.tw/cgi-bin/page/archive.pl?No=1046>`__
     - Arduino shield

Hardware
--------

Evaluation Board
~~~~~~~~~~~~~~~~

- `EVAL-AD4170-4ARDZ <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4170-4.html>`__

The evaluation board supports multiple sensor types including 2/3/4-wire RTD,
thermocouple, thermistor, load cell (DC and AC excitation), and accelerometer
configurations. On-board power regulation, configurable reference sources
(internal, external via LTC6655/ADR4525, or user-supplied), and SPI
connectivity through the Arduino and PMOD connectors are all provided.

HDL Reference Design
--------------------

The HDL reference design uses the
`SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
to interface with the :adi:`AD4170` ADC. The design captures continuous
samples at the maximum sample rate.

Block Diagram
~~~~~~~~~~~~~

.. figure:: ad4170_asdz_block_diagram.svg
   :align: center

   AD4170-ASDZ HDL block diagram

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad4170_asdz`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD4170-ASDZ HDL project <https://analogdevicesinc.github.io/hdl/projects/ad4170_asdz/index.html>`__

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad4170_asdz/coraz7s
   make

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Software Support
----------------

No-OS Driver
~~~~~~~~~~~~~

The AD4170 No-OS driver provides a platform-independent software layer for
controlling the :adi:`AD4170` ADC from bare-metal applications.

Source code:

- :git-no-OS:`drivers/adc/ad4170`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
- :adi:`AD4170 Product Page <AD4170>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
