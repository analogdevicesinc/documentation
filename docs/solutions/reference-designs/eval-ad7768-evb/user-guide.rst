.. _ad7768 user-guide:

User guide
===============================================================================

The complete user guides of the evaluation boards can be found at:

- :adi:`EVAL-AD7768FMCZ User Guide (UG-917) <media/en/technical-documentation/user-guides/EVAL-AD7768FMCZ_UG-917.pdf>`
- :adi:`EVAL-AD7768-4FMCZ User Guide (UG-921) <media/en/technical-documentation/user-guides/EVAL-AD7768-4FMCZ-UG-921.pdf>`

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD7768` and :adi:`EVAL-AD7768-4` boards connect to the FPGA
carrier via the FMC LPC connector.
On the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__,
configure the BOOT switches (JP7-JP11) and the MIO0 jumper (JP6) for the desired
boot mode, and set VADJ to **3.3 V** as required by the HDL project.
Refer to the :ref:`ad7768 quickstart zed` guide for the specific jumper positions
for SD card and JTAG boot modes.

For detailed jumper and connector configurations on the evaluation boards,
refer to the user guides:
:adi:`UG-917 <media/en/technical-documentation/user-guides/EVAL-AD7768FMCZ_UG-917.pdf>`
(EVAL-AD7768FMCZ) and
:adi:`UG-921 <media/en/technical-documentation/user-guides/EVAL-AD7768-4FMCZ-UG-921.pdf>`
(EVAL-AD7768-4FMCZ).

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD7768` / :adi:`EVAL-AD7768-4` evaluation boards require an
external 7 V to 9 V power supply connected to the J1 barrel connector on the
evaluation board. The on-board regulators generate the required supply rails:

- **AVDD1A, AVDD1B**: 5 V (analog supply)
- **AVDD2A, AVDD2B**: 2.25 V to 5.0 V (analog supply)
- **IOVDD**: 2.5 V to 3.3 V or 1.8 V (digital I/O supply)

The FPGA carrier board (ZedBoard) is powered separately through its own 12 V
power input connector (J20). The VADJ voltage provided from the carrier through
the FMC connector must be set to **3.3 V**.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD7768` provides 8 differential analog input channels (AIN0 through
AIN7), while the :adi:`AD7768-4` provides 4 differential channels (AIN0
through AIN3). The differential input signals should be connected to the
corresponding AINx+/AINx- pins on the evaluation board.

The absolute input voltage range is determined by the external reference
voltage, with a range of 1 V to AVDD1 - AVSS. A precharge buffer on each
analog input reduces input current requirements.

For testing purposes, a signal generator can be connected to the analog inputs
using jumper wires or SMB connectors. For optimal performance, use a low noise,
low distortion signal source.

Schematic, PCB layout, bill of materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design and layout files for the evaluation boards can be found on the
respective product pages:

- :adi:`EVAL-AD7768FMCZ design files <EVAL-AD7768>`
- :adi:`EVAL-AD7768-4FMCZ design files <EVAL-AD7768-4>`

Software guide
-------------------------------------------------------------------------------

The evaluation boards are supported both with Linux (using the Libiio library)
and with no-OS (bare metal). The Libiio library is cross-platform (Windows,
Linux, Mac) with language bindings for C, C#, Python, and others. Two
applications that can be used with it are:

- :git-iio-oscilloscope:`IIO Oscilloscope <releases>`
- :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
  plugin)

For no-OS (bare metal), the evaluation board runs an embedded IIOD server over
the serial (UART) connection and can be accessed using IIO Oscilloscope with
the serial backend. Refer to the
:ref:`no-OS quick start section <ad7768 quickstart zed>` for details.
