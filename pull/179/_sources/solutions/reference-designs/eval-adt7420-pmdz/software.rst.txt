.. _eval-adt7420-pmdz-software:

Software
========

This page provides software setup details for the :ref:`eval-adt7420-pmdz`
evaluation board across all supported platforms.

Application Software (All Platforms)
------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio library is used for interfacing with IIO devices and is required to
be installed on your computer.

Download and install the latest
`Libiio package <https://github.com/analogdevicesinc/libiio/releases>`__
on your machine.

To be able to connect your device, the software must be able to create a
context. The context creation depends on the backend used to connect to the
device as well as the platform where the EVAL-ADT7420-PMDZ is attached. Two
platforms are currently supported: Raspberry Pi using the ADI Kuiper Linux and
the ADICUP3029 running the no-OS ADT7420 demo project. The user needs to supply
a **URI**, which will be used in the context creation.

The ``iio_info`` command is a part of the libIIO package that reports all IIO
attributes. Upon installation, simply enter the command on the terminal command
line to access it.

For RPi Direct Local Access:

.. code-block:: bash

   iio_info

For Windows machine connected to Raspberry Pi:

.. code-block:: bash

   iio_info -u ip:<ip address of your RPi>

Example: If your Raspberry Pi has the IP address **192.168.1.7**, use
``iio_info -u ip:192.168.1.7`` as your URI.

.. note::

   The Windows machine and the RPi board should be connected to the same network
   in order for the machine to detect the device.

For Windows machine connected to ADICUP3029:

.. code-block:: bash

   iio_info -u serial:<serial port>

Examples:

- In a Windows machine, check the port of your ADICUP3029 via Device Manager in
  the Ports (COM & LPT) section. If your device is in COM4, use
  ``iio_info -u serial:COM4`` as your URI.
- In a Unix-based machine, you will see it under the ``/dev/`` directory in this
  format ``ttyUSBn``, where n is a number depending on how many serial USB
  devices are attached. If your device is ttyUSB0, use
  ``serial:/dev/ttyUSB0`` as your URI.

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage and control the device.
The ``iio_attr`` command reads and writes IIO attributes.

.. code-block:: bash

   analog@analog:~$ iio_attr [OPTION]...

Example -- To look at the context attributes:

.. code-block:: bash

   analog@analog:~$ iio_attr -a -C

The ``iio_reg`` command reads or writes SPI or I2C registers in an IIO device.
This is generally not needed for end applications but can be useful in debugging
drivers. Note that you need to specify a context using the ``-u`` qualifier when
you are not directly accessing the device via RPi or when you are using the
ADICUP3029 platform.

.. code-block:: bash

   analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example -- To read the device ID (register = 0x02) of an ADT7420 interfaced
via RPi from a Windows machine:

.. code-block:: bash

   iio_reg -u ip:<ip address> adt7420 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

Make sure to download/update to the latest version of
`IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

1. Open the IIO Oscilloscope application. Supply the URI used in context
   creation (see previous section).
2. Press refresh to display available IIO Devices. Once ADT7420 appears, press
   connect.

.. figure:: adt7420_iio_osc.png
   :align: center
   :width: 300

   ADT7420 IIO Oscilloscope Configuration

**Debug Panel:**
The Debug panel allows you to directly access the device attributes.

.. figure:: adt7420_iio_debug_panel.png
   :align: center
   :width: 300

   ADT7420 IIO Oscilloscope Debug Panel

**DMM Panel:**
Access the DMM panel to see the instantaneous reading of the ADT7420
temperature reading.

.. figure:: adt7420_iio_dmm_panel.png
   :align: center
   :width: 300

   ADT7420 IIO Oscilloscope DMM Panel

PyADI-IIO
~~~~~~~~~~

`PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__ is a Python
abstraction module for ADI hardware with IIO drivers to make them easier to use.
This module provides device-specific APIs built on top of the current libIIO
Python bindings. These interfaces try to match the driver naming as much as
possible without the need to understand the complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set up
PyADI-IIO and install the necessary packages/modules.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PyADI-IIO on your machine, run the
``adt7420_example.py`` found in the examples folder.

For No-OS (MAX32655FTHR/MAX32650FTHR):

At line 38 of the example python script, the COM port indicated should be
updated based on your device. In a Windows machine, check the port of your
MAX32655FTHR/MAX32650FTHR via Device Manager in the Ports (COM & LPT) section.
If your device is in COM18, line 38 should be:

.. code-block:: python

   temp_sensor = adi.adt7420(uri="serial:COM18,57600,8N1")

To run the example python script, the IIO example hex should be loaded on the
maxim platform before running:

.. code-block:: bash

   D:\pyadi-iio\examples>python adt7420_example.py

Press enter and you will get readings similar to the output below.

.. figure:: adt7420_pyadiio_example_max32650.png
   :align: center
   :width: 600

   PyADI-IIO ADT7420 Example Output

Python example script on GitHub:
`adt7420_example.py <https://github.com/analogdevicesinc/pyadi-iio/blob/master/examples/adt7420_example.py>`__

ADICUP3029 Bluetooth Demo
--------------------------

The ADICUP3029_ADT7420 demo project supports Bluetooth data output via the
IoTNode Android application. In the ``adt7420_app.h`` header file you can
configure:

- **ADI_APP_DISPATCH_TIMEOUT** -- Defines how often data is sent over
  Bluetooth.
- **ADI_APP_USE_BLUETOOTH** -- Enables or disables Bluetooth. When disabled,
  output is directed to the console window (debug mode) or serial terminal
  (release mode).

Output Modes
~~~~~~~~~~~~

There are three different ways to visualize the data:

- CrossCore Embedded Studio Console Window (through semihosting)
- Serial Terminal Program (such as PuTTY or Tera Term)
- IoTNode Smart Device App

.. list-table:: Launch Configuration
   :header-rows: 1

   * - Data Output Destination
     - Connected to Debugger
     - Configuration File
   * - CCES Console Window
     - Yes
     - ADICUP3029_Debug.launch
   * - PC/Laptop Serial Terminal
     - No
     - ADICUP3029_Release.launch
   * - IoTNode Smart App
     - Yes
     - ADICUP3029_Debug.launch
   * - IoTNode Smart App
     - No
     - ADICUP3029_Release.launch

UART configuration for release mode:

.. code-block:: none

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

ADICUP360 Demo (Deprecated)
----------------------------

The original software example for the EVAL-ADT7420-PMDZ was developed on the
ADICUP360 platform and is a simple, terminal-based command line interface. This
type of example program has been deprecated in favor of tinyiiod-based servers
for embedded platforms.

The ADuCM360_demo_adt7420_pmdz project reads temperature data from the ADT7420
and displays the temperature in [codes] and [C] on a serial terminal. The
temperature data can be changed between 16-bit (0.0078 C/LSB) and 13-bit
(0.0625 C/LSB) accuracy depending on the resolution needed. The application
also prints out the device ID register, which is a quick check to ensure reads
are working properly.

Configure the ADT7420 I2C address in the ``ADT7420.h`` file to match the
hardware:

.. code-block:: c

   /* ADT7420 I2C Address */
   #define ADT7420_ADDRESS    0x48      /* Default I2C Address of EVAL-ADT7420-PMDZ */

Configure the ADT7420 operating mode in the ``ADT7420.c`` file:

.. code-block:: c

   uint8_t ui8configAdt7420 = (FAULT_TRIGGER_4 | CT_PIN_POLARITY |
       INT_PIN_POLARITY | INT_CT_MODE | CONTINUOUS_CONVERSION_MODE |
       RESOLUTION_13_BITS);

Assign temperature setpoints and alarms/interrupts in the ``ADT7420.h`` file:

.. code-block:: c

   /* Temperature monitoring parameters */
   #define TEMP_HIGH_SETPOINT             75          /* Value in Degree C */
   #define TEMP_LOW_SETPOINT              0           /* Value in Degree C */
   #define TEMP_CRITICAL_SETPOINT         100         /* Value in Degree C */
   #define TEMP_HYSTERSIS_SETPOINT        5           /* Value in Degree C */

UART configuration for ADICUP360:

.. code-block:: none

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

.. note::

   The libiio, IIO Oscilloscope, and PyADI-IIO sections do NOT apply to the
   deprecated ADICUP360 example.
