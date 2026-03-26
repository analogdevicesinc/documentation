.. _adrv9002 user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:download:`ADRV9001/ADRV9002 System Development User Guide (UG-1828) <files/adrv9001-ug1828.pdf>`.

.. image:: images/ADRV9002TOP-evaluation-board.jpg
   :align: center
   :width: 600

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA carrier
board.

The ADRV9002 evaluation board uses the ADP5056 power management IC to
generate the required internal power domains. The board requires **1.8V**
on the VADJ supply for the transmitter/receiver DACs/ADCs and GPIO signals.

The VADJ configuration for each FPGA carrier board can be found in the
README.md file at: :git-hdl:`projects/adrv9002`.

Clock configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9002 evaluation board supports multiple clock configuration
options:

Clock source selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the FMC card, set the "DEV_CLK Source Sel." switch to select clock
source between:

#. **Internal** (default): On-board 38.4 MHz VCTCXO

   - Low phase noise crystal oscillator
   - Suitable for most applications
   - No external clock generator required

#. **External**: Via J501 connector

   - Frequency range: 10 MHz to 1000 MHz
   - Input power level: +13 dBm
   - Allows use of high-quality external reference clock for optimal
     performance

.. note::

   The quality of the clock source used to generate the DEV_CLK directly
   impacts the overall system performance. Use a high-quality, stable, and
   low-phase noise clock source.

Internal synthesizers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADRV9002 employs four PLL synthesizers for flexible clock
generation:

- **Clock PLL**: Generates digital clocks for ADC/DAC and LVDS interface
- **RF PLL 1**: Generates LO1 for transmitter/receiver channel 1
- **RF PLL 2**: Generates LO2 for transmitter/receiver channel 2
- **Auxiliary PLL**: Generates auxiliary LO for calibration

Each PLL features:

- Fractional-N architecture for flexible frequency synthesis
- Integrated VCO with tuning range of 6.5 GHz to 13 GHz
- RF LO frequency range: 30 MHz to 6000 MHz
- Programmable loop filter bandwidth for phase noise optimization

External LO mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADRV9002 supports external LO input for advanced applications:

- **Differential external LO**: 60 MHz to 12 GHz with 100 Ω differential
  impedance
- **Single-ended external LO**: 500 MHz to 1 GHz with 50 Ω impedance
- Programmable signal level: ±6 dBm typical
- Can be configured independently for each RF channel

RF and data interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board provides:

- **RF ports**: SMA connectors for:

  - Dual receiver channels: RX1A±, RX1B±, RX2A±, RX2B±
  - Dual transmitter channels: TX1±, TX2±

- **Frequency range**: 30 MHz to 6000 MHz covering VHF, UHF, ISM, and
  cellular bands
- **Bandwidth**: 12 kHz to 40 MHz (configurable via profile)
- **Data interface**: CMOS or LVDS synchronous-serial interface to FPGA
- **Control interface**: 4-wire SPI for device configuration

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect RF signals to the SMA connectors on the evaluation board:

- Use appropriate RF signal generators or antennas for the receiver
  inputs
- Ensure signal levels are within the specified input range
- For transmitter testing, connect to spectrum analyzers or RF power
  meters
- Maintain proper impedance matching (typically 50 Ω) for optimal
  performance

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the ADRV9002 evaluation board including schematics, PCB
layout, bill of materials, and reference designs are available at:

`ADRV9002 Integrated RF Agile Transceiver Design Resources <https://www.analog.com/en/lp/001/integrated-rf-agile-transceiver-design-resources.html>`_

Software guide
-------------------------------------------------------------------------------

The ADRV9002 evaluation board is supported with the
:git-libiio:`libiio library </>`. This library is cross-platform
(Windows, Linux, Mac) with language bindings for C, C#, Python, MATLAB,
and others.

ADI IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9002 has a dedicated plugin for :ref:`iio-oscilloscope`.

.. seealso::
   :ref:`adrv9002-plugin`

Scopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9002 is supported in :external+scopy:doc:`Scopy <index>`.

.. seealso::
   :external+scopy:doc:`ADRV9002 Plugin <plugins/adrv9002/adrv9002>`

PyADI-IIO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:git-pyadi-iio:`PyADI-IIO </>` is a Python abstraction module for ADI
hardware with IIO drivers. An ADRV9002 example can be found
:git-pyadi-iio:`here </examples/adrv9002_example.py>`.

MATLAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADRV9002 support through `Transceiver Toolbox <https://analogdevicesinc.github.io/TransceiverToolbox/master/>`_

GNU Radio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADRV9002 integration with :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`

Linux Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV9002 Linux kernel driver provides device initialization, profile
configuration, dynamic profile switching, tracking calibrations, ENSM control,
GPIO/AuxDAC/AuxADC access, and power management.

.. seealso::
   :external+linux:doc:`ADRV9002 Linux Driver <drivers/iio-transceiver/adrv9002>`

No-OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADRV9002 bare-metal driver for embedded applications.

.. seealso::
   :external+no-OS:doc:`ADRV9002 no-OS Project <projects/rf-transceiver/adrv9001>`
