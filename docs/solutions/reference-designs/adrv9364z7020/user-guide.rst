.. _adrv9364z7020 user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADRV9364-Z7020` SOM supports two digital interface modes when used
with the :adi:`ADRV1CRR-BOB` carrier board:

- **CMOS mode** - single-ended interface, lower speed
- **LVDS mode** - differential interface, higher throughput

The interface mode is selected via jumper settings on the ADRV1CRR-BOB carrier.
Refer to the
:dokuwiki:`RF SOM Hardware guide <resources/eval/user-guides/adrv936x_rfsom/hardware>`
for the complete jumper configuration.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADRV9364-Z7020` SOM is powered through the carrier board connector.
The :adi:`ADRV1CRR-BOB` carrier accepts an external power supply via its
dedicated power input connector. Refer to the carrier board documentation for
the required voltage and current specifications.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RF connections to the :adi:`ADRV9364-Z7020` are made via IPEX connectors
on the SOM. The AD9364 supports a single Tx and single Rx channel with a tuning
range of 70 MHz to 6 GHz.

For RF test and evaluation, connect a calibrated signal source (spectrum
analyzer, signal generator) using appropriate IPEX-to-SMA adapters.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the ADRV9364-Z7020 SOM and associated carrier boards can be
found on the
:dokuwiki:`RF SOM Hardware page <resources/eval/user-guides/adrv936x_rfsom/hardware>`.

Software guide
-------------------------------------------------------------------------------

The :adi:`ADRV9364-Z7020` is supported by the Libiio library, a cross-platform
library (Windows, Linux, macOS) with language bindings for C, C#, Python,
MATLAB, and others. The following tools can be used with it:

- :ref:`iio-oscilloscope` - graphical tool for real-time data capture and
  control, using the
  :ref:`AD9361 Control IIO Scope Plugin <fmcomms2 software ad9361-plugin>`
  and the
  :ref:`AD9361 Advanced Control IIO Scope Plugin <fmcomms2 software ad9361-advanced-plugin>`
- :external+pyadi-iio:doc:`pyadi-iio <index>` - Python interface for the AD9364
- :ref:`Analog Devices Transceiver Toolbox <matlab transceiver-toolbox>` - MATLAB and Simulink support

For the Linux device driver, see:
:external+linux:doc:`AD9361 Linux Device Driver <drivers/iio-transceiver/ad9361>`.

For the no-OS driver, see:
:external+no-OS:doc:`No-OS AD9361 project <projects/rf-transceiver/ad9361>`.

For the HDL reference design, see:
:external+hdl:ref:`adrv9364z7020`.
