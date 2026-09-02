.. _dac-fmc-ebz user-guide:

User Guide
===============================================================================

TBA -- Board overview image

Hardware Guide
-------------------------------------------------------------------------------

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBA -- Board-specific configuration details (jumper settings, clock
configuration, power supply options)

Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DAC-FMC-EBZ evaluation boards can be powered in two ways:

- **Via DPG3 connector** -- when using the DPG3 data pattern generator, +5V is
  supplied through the DPG3 connector (P4).
- **Via FMC connector** -- when using an ADS7-V2 or FPGA carrier board, power
  is supplied through the FMC connector (+12V, +3.3V, VADJ).

TBA -- Power supply details per board variant

Clock Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All DAC-FMC-EBZ boards include an AD9516 clock distribution chip that provides:

- DACCLK -- the main DAC sampling clock
- REFCLK / SYSREF -- JESD204B reference and synchronization clocks
- DPG3/ADS7 interface clock

A low phase noise external clock source should be connected to the SMA
connector J1 (CLK_IN).

TBA -- Clock configuration details per board variant

Schematic, PCB Layout, and BOM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for each board variant are available in the respective evaluation
board pages:

- :ref:`eval-ad9136`
- :ref:`eval-ad9144`
- :ref:`eval-ad9152`
- :ref:`eval-ad9154`
- :ref:`eval-ad917x`

Software Guide
-------------------------------------------------------------------------------

ACE Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred evaluation software is
:dokuwiki:`ACE (Analysis | Control | Evaluation) <resources/tools-software/ace>`.
ACE provides a graphical interface for configuring the DAC and clock
distribution chip via SPI, and is used in conjunction with the DPG Downloader
for waveform generation.

TBA -- ACE software usage overview

DPG Downloader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :dokuwiki:`DPG Downloader <resources/eval/dpg/dpgdownloader>` is used
to generate and download test waveforms (single tone, multi-carrier, custom
vectors) into the DPG3 or ADS7 pattern generator.

TBA -- DPG Downloader usage overview

Linux Driver Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For FPGA-based evaluation using Linux, the following drivers are available:

TBA -- Linux driver details, IIO devices, channel mapping
