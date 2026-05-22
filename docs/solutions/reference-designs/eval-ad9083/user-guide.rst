.. _eval-ad9083 user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9083` evaluation board can be configured for different
operating modes using onboard resistors. Refer to the schematic for component
placement details.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9083` is powered through the FMC connector. The FPGA carrier
must supply **VADJ = 1.8 V** to the FMC connector.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9083` provides differential SMA connectors for the 16 analog
input channels. Connect a low-noise signal source compatible with the configured
input bandwidth (up to 125 MHz per channel).

A reference clock input is also provided via SMA connector. The clock frequency
must be compatible with the configured ADC sample rate.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the :adi:`EVAL-AD9083` evaluation board are available on the
:adi:`EVAL-AD9083 product page <EVAL-AD9083>`.

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9083` is supported through the Linux IIO framework and the
no-OS driver. The following software tools can be used with the evaluation
board:

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`iio-oscilloscope` is a graphical tool for capturing and visualizing ADC
data in time domain, frequency domain, and constellation views. After booting
Linux on the ZCU102, connect IIO Oscilloscope to the board over Ethernet using
the board's IP address.

pyadi-iio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python scripts can acquire data from the :adi:`AD9083` using the
:external+pyadi-iio:doc:`pyadi-iio <index>` library, which provides a
high-level interface to the IIO device.

libiio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9083` is accessible through the
:ref:`libiio` library, which provides language
bindings for C, C#, Python, MATLAB, and others.
