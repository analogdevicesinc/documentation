.. _eval-adxrs290-pmdz-software:

Software
========

This page provides software setup details for the :ref:`eval-adxrs290-pmdz`
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
device as well as the platform where the EVAL-ADXRS290-PMDZ is attached. Two
platforms are currently supported: Raspberry Pi using the ADI Kuiper Linux and
the ADICUP3029 running the ADXRS290 IIO demo project. The user needs to supply
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

Example -- To read the device ID (register = 0x02) of an ADXRS290 interfaced
via RPi from a Windows machine:

.. code-block:: bash

   iio_reg -u ip:<ip address> adxrs290 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

Make sure to download/update to the latest version of
`IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__.

1. Open the IIO Oscilloscope application. Supply the URI used in context
   creation (see previous section).
2. Press refresh to display available IIO Devices. Once adxrs290 appears, press
   connect.

.. figure:: iio_osc_connection.jpg
   :align: center
   :width: 200px

   IIO Oscilloscope Connection Dialog

**Debug Panel:**
The Debug panel allows you to directly access the attributes of the device.

.. figure:: adxrs290_debug.png
   :align: center
   :width: 400px

   ADXRS290 Debug Panel

**DMM Panel:**
Access the DMM panel to see the instantaneous reading of the X and Y angular
velocities.

.. figure:: adxrs290_dmm-2.png
   :align: center
   :width: 400px

   ADXRS290 DMM Panel

**Waveform Panel:**
The Waveform panel (Capture window) displays the real-time waveform of the
ADXRS290 response.

.. figure:: iio_osc_graph.jpg
   :align: center
   :width: 400px

   ADXRS290 Waveform Capture

.. note::

   The readings from the DMM panel will freeze upon activation of the real-time
   plot in the waveform panel. The two panels are designed to be used separately
   and not simultaneously.

PyADI-IIO
~~~~~~~~~~

`PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__ is a Python
abstraction module for ADI hardware with IIO drivers to make them easier to use.
This module provides device-specific APIs built on top of the current libIIO
Python bindings. These interfaces try to match the driver naming as much as
possible without the need to understand the complexities of libIIO and IIO.

Install PyADI-IIO using the standard installation method. The ADXRS290 example
requires a number of packages to be installed before it can be used. To ensure
that all required packages are present, install them in a virtual environment so
that other Python projects will not be affected. Make sure that
`virtualenv <https://pypi.org/project/virtualenv/>`__ has been installed before
proceeding.

Creating a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open a command prompt and navigate to the ``pyadi-iio`` directory.
2. Create a virtual environment by entering the following command:

   .. code-block:: bash

      D:\pyadi-iio>python -m venv adxrs290

   Note that the last argument ``adxrs290`` is just the name of the virtual
   environment to be created. It can be replaced by any other name. In case the
   code above does not work, try:

   .. code-block:: bash

      D:\pyadi-iio>virtualenv adxrs290

3. Input the following command to activate the virtual environment:

   .. code-block:: bash

      D:\pyadi-iio>adxrs290\Scripts\activate

Installing the Packages
^^^^^^^^^^^^^^^^^^^^^^^^

Upon activation of the virtual environment, enter the following commands:

.. code-block:: bash

   (adxrs290) D:\pyadi-iio>pip install -r requirements.txt
   (adxrs290) D:\pyadi-iio>pip install -r examples/requirements_adiplot.txt
   (adxrs290) D:\pyadi-iio>python setup.py install

.. important::

   One of the packages in ``requirements_adiplot.txt`` is PyQt5. If you already
   have a pre-installed PyQt5 prior to the installation of the packages, we
   suggest that you uninstall the said package in the virtual environment.
   Duplicate installations may sometimes cause errors that inhibit the system
   from displaying the real-time plot. This can easily be done by inputting the
   command: ``pip uninstall PyQt5`` while the virtual environment is active.

Running the Example
^^^^^^^^^^^^^^^^^^^^

1. Connect the ADXRS290 to the device platform you have chosen.
2. If interfaced via RPi, connect your laptop to the same network as the
   ADXRS290 and take note of its IP address. For ADICUP3029, take note of the
   serial port used.
3. On the source code, go to the ``examples`` folder and open ``adxrs290.py``.
   Provide the necessary context in order to detect the device. Make sure that
   only one context source is active and the other one is commented out
   depending on whether you are using the RPi board or the ADICUP3029.
4. Run the example by typing this line on the command prompt:

   .. code-block:: bash

      D:\pyadi-iio\examples>python adxrs290.py

   .. figure:: adxrs290_output.png
      :align: center
      :width: 700px

      Output on Terminal

5. You can opt to see a real-time plot of the ADXRS290 output. To do this, open
   ``adxrs290.py`` and set ``enable_plot`` to ``True``. A plot will pop up
   after running the code.

   .. figure:: adxrs290_enable-plot.png
      :align: center
      :width: 500px

      Enable Plot Setting

   .. figure:: adxrs290_plot.png
      :align: center
      :width: 500px

      ADXRS290 Real-Time Plot

Video Guides
~~~~~~~~~~~~

- `EVAL-ADXRS290-PMDZ Unboxing <https://www.youtube.com/watch?v=Z4bt3IdRFEQ>`__
- `EVAL-ADICUP3029 Demo <https://www.youtube.com/watch?v=LwD-MHoSlWk>`__

ADICUP3029 CLI Demo
-------------------

The **ADuCM3029_demo_adxrs290** is a dual-axis angular rate sensor (gyroscope)
demo project that provides a solution to control the EVAL-ADXRS290-PMDZ PMOD
using a minimal CLI and the no-OS drivers for the EVAL-ADICUP3029 platform.

The application senses and reads the **X-axis** and **Y-axis** rate (roll and
pitch). It produces a positive output for clockwise rotation about the x-axis
and y-axis. All outputs are printed from the UART to the USER USB port and can
be read on the PC using a serial terminal program, such as PuTTY or Tera Term.

The application builds upon the no-OS device and platform drivers and a minimal
CLI module to provide a robust command set.

Demo Requirements
~~~~~~~~~~~~~~~~~

Hardware:

- EVAL-ADICUP3029
- EVAL-ADXRS290-PMDZ
- Micro-USB to USB cable
- PC or laptop with USB port

Software:

- ADuCM3029_demo_adxrs290_pmdz software
- CrossCore Embedded Studio (2.7.0 or higher)
- ADuCM302x DFP (3.2.0 or higher)
- ADICUP3029 BSP (1.1.0 or higher)
- Serial terminal program (PuTTY or Tera Term)

Obtaining the Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~

There are two basic ways to program the ADICUP3029:

1. **Dragging and Dropping the .Hex to the DAPLINK drive** -- This is the
   easiest way to get started.
2. **Building, Compiling, and Debugging using CCES** -- Allows customization
   but requires downloading the CrossCore toolchain.

The software for the ADICUP3029_ADXRS290 demo can be found here:

- `Prebuilt ADXRS290 CLI Hex File <https://github.com/analogdevicesinc/no-OS/releases/download/Latest/adxrs290-pmdz.zip>`__
- `ADuCM3029_demo_adxrs290_pmdz Source Code <https://github.com/kister-jimenez/ADuCM3029_demo_adxrs290pmdz>`__

Project Structure
~~~~~~~~~~~~~~~~~

Beside the IDE generated sources the project structure is divided into high
level software modules and low level software modules.

The high level modules are in the **src** folder:

- ADXRS290 device driver
- CLI module
- ADXRS290_PMDZ module (application source)
- ADuCM3029_demo_adxrs290_pmdz.c (main file)

The low level modules are the platform drivers and are included in the
**platform_source** and **platform_include** folders.

Configuring the Software Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Gyroscope range setting** -- ``ADXRS290_RANGE`` parameter. 2, 4, or 8 are
  acceptable values to set the g range for the ADXRS290 (in ``ADXRS290.h``):

  .. code-block:: c

     #define ADXRS290_SENSE        2

- **Sensor activity and inactivity thresholds** -- ``ACT_VALUE`` and
  ``INACT_VALUE`` parameters used to determine at which acceleration values
  the sensor can react at sleep/wake-up commands (in ``ADXRS290.h``):

  .. code-block:: c

     #define ACT_VALUE          50
     #define INACT_VALUE        50

- **Sensor activity and inactivity time** -- ``ACT_TIMER`` and ``INACT_TIMER``
  parameters used to determine sleep/wake-up intervals (in ``ADXRS290.h``):

  .. code-block:: c

     #define ACT_TIMER          50
     #define INACT_TIMER        50

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

1. Flash the program to the EVAL-ADICUP3029.
2. Extract the zip file and drag and drop the provided hex file in the
   DAPLINK drive.
3. Once done, open a serial terminal program, such as PuTTY or Tera Term.
4. Follow the UART configuration below.

.. code-block:: none

   Select COM Port
   Baud rate: 115200
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

The user must press the reset button on ADICUP3029 each time they want to
display the results.

.. figure:: example_serial_output.png
   :align: center
   :width: 600px

   Example Serial Terminal Output

Digital Communications
~~~~~~~~~~~~~~~~~~~~~~

Digital communication on the EVAL-ADXRS290-PMDZ is accomplished using a
standard expanded SPI PMOD port.

.. list-table:: Connector P1 Pinout
   :header-rows: 1

   * - Description
     - Pin(s)
   * - SS
     - 1
   * - MOSI
     - 2
   * - MISO
     - 3
   * - SCLK
     - 4
   * - GND
     - 5, 11
   * - IOVDD
     - 6, 12
   * - SYNC
     - 7
