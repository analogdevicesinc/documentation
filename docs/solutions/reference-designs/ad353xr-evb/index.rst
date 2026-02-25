.. _ad353xr-evb:

AD353xR-EVB User Guide
======================

Introduction
------------

The :adi:`AD3530R` is a high-density, low-voltage supply, 8-channel
digital-to-analog converter (DAC) targeted at but not limited to optical
communications applications. The device features ultra-low headroom power
dissipation and WLCSP packaging for minimal board footprint, making it ideal
for compact optical modules such as QSFP-DD and OSFP form factors.

The AD353xR evaluation board provides all the interfaces necessary to interact
with the device family using an FPGA development board. The HDL reference
design supports SPI communication with the DAC using the SPI Engine Framework.

Supported Devices
-----------------

- :adi:`AD3530` (8-channel)
- :adi:`AD3530R` (8-channel, internal reference)
- :adi:`AD3531` (4-channel)
- :adi:`AD3531R` (4-channel, internal reference)

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Carrier
     - Connector
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC
   * - `Cora Z7S <https://digilent.com/reference/programmable-logic/cora-z7/start>`__
     - GPIO
   * - `DE10-Nano <https://www.terasic.com.tw/cgi-bin/page/archive.pl?No=1046>`__
     - GPIO

Hardware
--------

Evaluation Board
~~~~~~~~~~~~~~~~

- AD353xR Eval Board

Hardware Setup
~~~~~~~~~~~~~~

Required hardware:

- AD353xR evaluation board
- FPGA carrier board (one of the above)
- SDP-I-FMC or equivalent connection board
- Micro USB-to-Type-A cable for UART
- 16 GB or larger SD card

.. note::

   When using the ZedBoard, VADJ must be set to 2.5 V.

SPI Connection Table
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Signal
     - Function
     - ZedBoard (FMC)
     - Cora Z7S (GPIO)
     - DE10-Nano (GPIO)
   * - CSB
     - Chip Select
     - M19 / FMC-LA00_P
     - F16
     - AE19
   * - SCK
     - Serial Clock
     - D18 / FMC-CLK1_P
     - H15
     - AG18
   * - SDO
     - MOSI
     - N19 / FMC-LA01_P
     - T12
     - AG15
   * - SDI
     - MISO
     - N20 / FMC-LA01_N
     - W15
     - AF18
   * - RESETB
     - Reset
     - T19 / FMC-LA10_N
     - V13
     - AE20
   * - LDACB
     - Load DAC
     - J18 / FMC-LA05_P
     - T14
     - AE17

HDL Reference Design
--------------------

The HDL reference design uses the
`SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
to interface with the :adi:`AD3530R` DAC family. The design is built upon ADI's
generic HDL reference design framework.

Block Diagram
~~~~~~~~~~~~~

.. figure:: ad353xr_block_diagram.svg
   :align: center

   AD353xR HDL block diagram

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad353xr`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD353xR HDL project <https://analogdevicesinc.github.io/hdl/projects/ad353xr/index.html>`__

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad353xr/coraz7s
   make

A comprehensive build guide is available in the
`HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__.

Software Support
----------------

No-OS Driver
~~~~~~~~~~~~~

The AD3530R No-OS driver provides a platform-independent software layer for
controlling the :adi:`AD3530R` DAC from bare-metal applications.

Source code:

- :git-no-OS:`drivers/dac/ad3530r`

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `SPI Engine Framework <https://analogdevicesinc.github.io/hdl/library/spi_engine/index.html>`__
- :adi:`AD3530R Product Page <AD3530R>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
