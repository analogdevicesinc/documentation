.. _eval_ad9265 user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9265` board connects to the FPGA carrier via the FMC LPC
connector.

On the :xilinx:`ZC706`, configure the boot mode switch SW11 for SD card or
JTAG boot and ensure VADJ is set to **2.5 V**. Refer to the
:ref:`eval_ad9265 quickstart zc706` guide for more details.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9265` board is powered through the FMC LPC connector from
the FPGA carrier board. The carrier board itself (e.g., ZC706)
requires a **12 V** external power supply.

The required VADJ for the FMC LPC interface is **2.5 V**.

On-board connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - - Connector
     - Type
     - Description
   - - J100
     - SMA
     - Analog signal source input
   - - J201
     - SMA
     - External clock signal input for ADC sampling
   - - J202
     - SMA
     - External amplified signal input for ADC sampling
   - - J300
     - Jumper
     - Configuration for the optional clock path using the :adi:`AD9517 <ad9517>`
       (RESET, SYNC, PD and REF_SEL pins)
   - - P1
     - Jumper
     - :adi:`AD9265` Clock divider synchronization
   - - P2
     - Jumper
     - On-board oscillator enable (Pin 1–Pin 2 = on-board oscillator on; 
       Pin 2-Pin 3 = on-board oscillator off)
   - - P300
     - Jumper
     - Optional clock status pins (REFMON, LD and STATUS)
   - - FMC LPC
     - FMC
     - FPGA carrier board interface

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect a low-noise, low-distortion signal source to the analog input of the
:adi:`EVAL-AD9265` board via the **J100** SMA connector.

The full-scale differential input range is 2 V peak-to-peak (1 V peak on
each side). The common-mode input voltage (VCM) is provided by the on-board
reference and defaults to VREF/2 = 1.0 V.

Clock input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9265` board provides three possible clock paths (some board
modification may be necessary):

- **External passive clock (default)** — connect an external clock source to 
  the **J201** SMA connector after removing the P2 connector.
- **Optional active clock path** using the :adi:`AD9517 <ad9517>`.
- **Optional oscillator** — on-board oscillator selectable via P2 jumper.

Ensure the corresponding components are removed or inserted on the board to
select the desired clock path. For optimal performance, use a low-jitter,
low-phase-noise clock source.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files are available on the product page:

- :adi:`EVAL-AD9265`

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported through the :ref:`libiio` library, which
is cross-platform (Windows, Linux, Mac) with bindings for C, C#, Python,
MATLAB, and others. Applications that interface via libiio include:

- :ref:`iio-oscilloscope` — graphical waveform and spectrum analyzer
- :external+scopy:doc:`Scopy <index>` v2.0 or later (requires the IIO plugin)
- :external+pyadi-iio:doc:`index` — Python interface

For a step-by-step walkthrough of connecting and using these tools with the
:adi:`EVAL-AD9265`, see the :ref:`eval_ad9265 quickstart zc706` or
:ref:`eval_ad9265 quickstart zed` guides.

IIO device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the system is booted and the :adi:`EVAL-AD9265` is detected, the
following IIO devices should appear:

.. shell::

   $iio_info | grep iio:device
    iio:device0: ad7291
    iio:device1: xadc
    iio:device2: ad9265 (buffer capable)

The ``ad9265`` IIO device exposes the following channels:

- ``voltage0``: ADC input channel (buffer capable)

Channel attributes include:

- ``raw`` — raw ADC sample value
- ``scale`` — conversion factor from raw to millivolts
- ``sampling_frequency`` — current sample rate in Hz
- ``hardwaregain`` — input gain setting (if applicable)
