.. _eval-ad4062-ardz tools:

Libraries and GUI Tools
=======================

Many language bindings and GUI tools are able to discover and interface IIO
devices, below is a summary.

Python interface
----------------

The :external+pyadi-iio:doc:`pyadi-iio <index>` library provides high-level
Python bindings for ADI IIO devices.

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install pyadi-iio

Basic usage
~~~~~~~~~~~

.. code-block:: python

   import adi

   # For serial connection (no-OS TinyIIO, Linux)
   dev = adi.ad405x("serial:/dev/ttyACM0,115200")

   # For network connection (Linux)
   # dev = adi.ad405x("ip:192.168.2.1")

   # Configure the device
   dev.rx_buffer_size = 1024

   # Capture data
   data = dev.rx()
   print(f"Captured {len(data)} samples")
   print(f"First 10 samples: {data[:10]}")

See :git-pyadi-iio:`examples/ad4052_example.py` for a complete example (the
AD4052 and AD4062 share the same driver and Python class).

Scopy
-----

:external+scopy:doc:`Scopy <index>`
is ADI's advanced signal analysis software with support for IIO devices.

Scopy provides additional features:

* Advanced signal analysis
* Spectrum analyzer
* Data logging
* Export to various formats

Then connect using one of the backends available.

IIO Oscilloscope
----------------

:ref:`iio-oscilloscope` is a GTK-based GUI application for visualizing IIO
device data.

Launch IIO Oscilloscope:

.. shell::

   $osc

Connect to the device using the same backends as Scopy.

Once connected, you can:

* View real-time waveforms
* Configure device attributes (sample rate, oversampling, etc.)
* Capture and export data
* Perform FFT analysis


