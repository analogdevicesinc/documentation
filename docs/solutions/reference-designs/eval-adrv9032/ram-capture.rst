.. _adrv9032 ram-capture:

RAM Capture
===============================================================================

Introduction
-------------------------------------------------------------------------------

The ADRV903x provides a RAM capture feature for capturing raw RX/ORX ADC
samples at various points in the signal chain. This is useful for debugging,
signal analysis, and calibration verification.

The ``adrv903x-ramc`` IIO device exposes this feature with standard IIO buffer
support, allowing data capture using IIO Oscilloscope or command-line tools
like ``iio_readdev``.

.. note::

   RAM capture is a **single-shot snapshot** mechanism. Each buffer enable
   triggers one capture that fills the buffer, then stops. For continuous
   RX data streaming, use the JESD interface (``axi-adrv903x-rx-hpc``).

.. note::

   The capture hardware can only sample one RX/ORX channel at a time. Only one
   I/Q channel pair can be enabled simultaneously.

IIO Device
-------------------------------------------------------------------------------

The RAM capture interface appears as a separate IIO device named
``adrv903x-ramc``. It provides 10 channel pairs (RX0-RX7 and ORX0-ORX1), each
with I and Q components.

Channel Mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - - IIO Channel
     - Signal
   - - ``voltage0_i``, ``voltage0_q``
     - RX0
   - - ``voltage1_i``, ``voltage1_q``
     - RX1
   - - ``voltage2_i``, ``voltage2_q``
     - RX2
   - - ``voltage3_i``, ``voltage3_q``
     - RX3
   - - ``voltage4_i``, ``voltage4_q``
     - RX4
   - - ``voltage5_i``, ``voltage5_q``
     - RX5
   - - ``voltage6_i``, ``voltage6_q``
     - RX6
   - - ``voltage7_i``, ``voltage7_q``
     - RX7
   - - ``voltage8_i``, ``voltage8_q``
     - ORX0
   - - ``voltage9_i``, ``voltage9_q``
     - ORX1

Device Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - - Attribute
     - Access
     - Description
   - - ``sample_count``
     - Read/Write
     - Number of samples to capture. Valid values: 32, 64, 128, 256, 512,
       1024, 2048, 4096, 8192, 12288, 16384, 32768. ORX channels are limited
       to 12288 maximum.
   - - ``sampling_frequency``
     - Read only
     - Sample rate in Hz (matches RX IQ rate).

Using IIO Oscilloscope
-------------------------------------------------------------------------------

1. Connect to the board using IIO Oscilloscope.

2. In the **Plot Channels** panel, expand ``adrv903x-ramc``.

3. Enable one I/Q channel pair (e.g., ``voltage0_i`` and ``voltage0_q`` for
   RX0).

4. Click **Capture** to trigger a single-shot capture and display the data.

5. To capture from a different channel, disable the current pair and enable
   another.

.. note::

   Attempting to enable channels from different RX/ORX pairs simultaneously
   will result in an error due to hardware constraints.

Using iio_readdev
-------------------------------------------------------------------------------

Capture 1024 samples from RX0:

.. code-block:: bash

   iio_readdev -u <uri> -s 1024 adrv903x-ramc voltage0_i voltage0_q > capture.bin

Capture from RX2:

.. code-block:: bash

   iio_readdev -u <uri> -s 1024 adrv903x-ramc voltage2_i voltage2_q > capture.bin

Replace ``<uri>`` with the appropriate connection URI (e.g., ``ip:192.168.1.1``
or ``local:``).

The output file contains interleaved 32-bit signed I and Q samples in
little-endian format.

Setting Capture Parameters
-------------------------------------------------------------------------------

The ``sample_count`` attribute controls how many samples are captured:

.. code-block:: bash

   # Check current value
   cat /sys/bus/iio/devices/iio:device3/sample_count

   # Set to 4096 samples
   echo 4096 > /sys/bus/iio/devices/iio:device3/sample_count

.. note::

   The device number (``iio:device3``) may vary depending on the system
   configuration. Use ``iio_info`` or check ``/sys/bus/iio/devices/*/name``
   to identify the ``adrv903x-ramc`` device.

debugfs Interface
-------------------------------------------------------------------------------

A simplified debugfs interface is also available for quick single-shot
captures without IIO buffer setup under the ``adrv903x-phy`` device.

Usage:

.. code-block:: bash

   # Trigger capture: channel 0 (RX0), 256 samples
   echo "0 256" > /sys/kernel/debug/iio/iio:device1/rx_data_capture

   # Read captured data
   cat /sys/kernel/debug/iio/iio:device1/rx_data_capture

Channel numbers for debugfs:

- ``0``-``7``: RX0-RX7
- ``8``-``9``: ORX0-ORX1

The output is raw 32-bit values in hardware format (interleaved I/Q with bank
layout). The IIO device interface is recommended for most use cases as it
handles the data format conversion automatically.
