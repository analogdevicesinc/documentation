.. _eval-cn0579-ardz:

EVAL-CN0579-ARDZ
================

Quad-Channel IEPE Vibration Sensor Measurement System.

Overview
--------

Condition-based monitoring (CbM) enables early detection and diagnosis of
machine and system abnormalities. Identifying and isolating these issues creates
opportunities for optimizing replacement part inventories, scheduling downtime
for planned maintenance, and making run-time process adjustments that can extend
the life of equipment.

The :adi:`EVAL-CN0579-ARDZ <CN0579>` is a 4-channel, high resolution, wide
bandwidth, high dynamic range, IEPE-compatible interface data acquisition
(DAQ) system that interfaces with IC piezoelectric (ICP®)/IEPE sensors. While
most solutions that interface with piezoelectric sensors in the market are
AC-coupled and lack DC and subhertz measurement capabilities, this solution is
DC-coupled. By looking at the complete data set from an IEPE vibration sensor
in the frequency domain (DC to 50 kHz), the type and source of a machine fault
can be better predicted using the position, amplitude, and number of harmonics
found in the fast Fourier transform (FFT) spectrum.

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0579_simplified_block_diagram.png

Hardware Configuration
----------------------

Primary Side
~~~~~~~~~~~~

.. figure:: eval-cn0579-ardz_top-web.gif

Sensor Input
^^^^^^^^^^^^

The main input on the :adi:`EVAL-CN0579-ARDZ <CN0579>` are right-angle 
SMA connectors on the primary side of the board, as such it is
highly recommended to connect the sensor using an SMA cable. If this is not
possible, due to the type of sensor or otherwise, use the headers to connect
the board with other standard wires.

LED Indicators
^^^^^^^^^^^^^^

+-------------------------+-------------------------+-------------------------+
| LED                     | Location                | Function                |
+=========================+=========================+=========================+
| **PWR LEDs (DS1 to      | bottom-left corner      | indicates board power   |
| DS2)**                  |                         |                         |
+-------------------------+-------------------------+-------------------------+
| **FAULT LEDs (DS3 to    | near each SMA connector | indicates the status of |
| DS6)**                  |                         | switch’s fault flag     |
+-------------------------+-------------------------+-------------------------+
| **SHUTDOWN LED (DS7)**  | left side of U19        | indicates status of     |
|                         |                         | shutdown logic/buffer,  |
|                         |                         | FDA, SW disable         |
+-------------------------+-------------------------+-------------------------+

Secondary Side
~~~~~~~~~~~~~~

.. figure:: eval-cn0579-ardz_bottom-web.gif

Current Source Jumper
^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-CN0579-ARDZ <CN0579>` includes solder jumpers (P17 to P20) to
control current source. The jumpers connect the current source to the circuit
and may be removed for testing without a current source.

Arduino Interface
^^^^^^^^^^^^^^^^^

All connector pinouts for the :adi:`EVAL-CN0579-ARDZ <CN0579>` are described in
the table below.

+----------------------+---------+-----------------+---------------------+
| Connector            | Pin No. | Pin Name        | CN0579 Pin Function |
+======================+=========+=================+=====================+
| Arduino DIO 1 (P12)  | 1       | SCL             | SCL                 |
|                      +---------+-----------------+---------------------+
|                      | 2       | SDA             | SDA                 |
|                      +---------+-----------------+---------------------+
|                      | 3       | AREF            | NC (Not connected)  |
|                      +---------+-----------------+---------------------+
|                      | 4       | GND             | GND                 |
|                      +---------+-----------------+---------------------+
|                      | 5       | 13 / SCLK       | SCLK                |
|                      +---------+-----------------+---------------------+
|                      | 6       | 12 / MISO       | MISO                |
|                      +---------+-----------------+---------------------+
|                      | 7       | 11 / PWM / MOSI | MOSI                |
|                      +---------+-----------------+---------------------+
|                      | 8       | 10 / PWM / CS   | CS_ADC              |
|                      +---------+-----------------+---------------------+
|                      | 9       | 9 / PWM         | DRDY_N              |
|                      +---------+-----------------+---------------------+
|                      | 10      | 8               | DCLK                |
+----------------------+---------+-----------------+---------------------+
| Arduino DIO 0 (P14)  | 1       | 7               | DOUT0               |
|                      +---------+-----------------+---------------------+
|                      | 2       | 6 / PWM         | DOUT1               |
|                      +---------+-----------------+---------------------+
|                      | 3       | 5 / PWM         | DOUT2               |
|                      +---------+-----------------+---------------------+
|                      | 4       | 4               | DOUT3               |
|                      +---------+-----------------+---------------------+
|                      | 5       | 3 / PWM         | SHUTDOWN_N          |
|                      +---------+-----------------+---------------------+
|                      | 6       | 2               | RESET_N             |
|                      +---------+-----------------+---------------------+
|                      | 7       | TX              | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 8       | RX              | NC                  |
+----------------------+---------+-----------------+---------------------+
| Arduino Analog (P13) | 1       | AIN0            | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 2       | AIN1            | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 3       | AIN2            | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 4       | AIN3            | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 5       | AIN4            | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 6       | AIN5            | NC                  |
+----------------------+---------+-----------------+---------------------+
| Arduino Power (P11)  | 1       | NC              | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 2       | IOREF           | IOREF               |
|                      +---------+-----------------+---------------------+
|                      | 3       | RESET           | NC                  |
|                      +---------+-----------------+---------------------+
|                      | 4       | 3.3 V           | 3V3                 |
|                      +---------+-----------------+---------------------+
|                      | 5       | 5V              | 5V                  |
|                      +---------+-----------------+---------------------+
|                      | 6       | GND             | GND                 |
|                      +---------+-----------------+---------------------+
|                      | 7       | GND             | GND                 |
|                      +---------+-----------------+---------------------+
|                      | 8       | Vin             | NC                  |
+----------------------+---------+-----------------+---------------------+

.. tip::

    To achieve reasonable noise measurements, the piezo
    vibration sensor must be stabilized using either an active shaker table, which
    cancels environmental vibrations; or anchored to a massive object, which makes
    sensor still. For noise measurements done on :adi:`EVAL-CN0579-ARDZ <CN0579>`,
    the piezo vibration sensor was anchored to a massive object, where it is also
    connected directly to the input of the signal chain.

Test Points
^^^^^^^^^^^

The board also has many test points, most of which are labeled and are fairly
self-explanatory. The table below describes some of the most significant test
points and their connections.

+---------------------------+-------------------------------------------------+
| Test Point                | Description                                     |
+===========================+=================================================+
| 26V8                      | Connects to the 26.8V rail before it’s reduced  |
|                           | to 26V.                                         |
+---------------------------+-------------------------------------------------+
| 26V0                      | Connects to the 26V rail.                       |
+---------------------------+-------------------------------------------------+
| 5V5                       | Connects to the 5.5V rail before it’s reduced   |
|                           | to 5V.                                          |
+---------------------------+-------------------------------------------------+
| 5V0                       | Connects to the 5V rail.                        |
+---------------------------+-------------------------------------------------+
| TP1                       | Connects to the voltage reference of the DAC    |
|                           | for IEPE sensor.                                |
+---------------------------+-------------------------------------------------+
| TP6 / TP11 / TP16 / TP21  | Connects to signal chain after passing through  |
|                           | the fault protection switch                     |
+---------------------------+-------------------------------------------------+
| TP7 / TP12 / TP17 / TP22  | Connects to VOCM.                               |
+---------------------------+-------------------------------------------------+
| TP8 / TP13 / TP18 / TP23  | Connects to signal chain that is level shifted. |
+---------------------------+-------------------------------------------------+
| TP9 / TP14 / TP19 / TP24  | Connects to FDA_OUT_N0 of the ADC driver.       |
+---------------------------+-------------------------------------------------+
| TP10 / TP15 / TP20 / TP25 | Connects to FDA_OUT_P0 of the ADC driver.       |
+---------------------------+-------------------------------------------------+
| TP27 / TP29 / TP31 / TP33 | Connects to output from the bias voltage        |
|                           | correction.                                     |
+---------------------------+-------------------------------------------------+
| TP34                      | Connects to ADC reference buffer.               |
+---------------------------+-------------------------------------------------+
| TP35                      | Connects to differential conversion reference   |
|                           | buffer output / VOCM.                           |
+---------------------------+-------------------------------------------------+
| TP36                      | Connects to 32.768 MEGHz clock output.          |
+---------------------------+-------------------------------------------------+
| TP37                      | Connects to VCM of ADC.                         |
+---------------------------+-------------------------------------------------+

System Setup
------------

General Setup Using DE10-Nano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demo Requirements
^^^^^^^^^^^^^^^^^

The following is the list of items needed in order to replicate this demo.

**Hardware**

-  :adi:`EVAL-CN0579-ARDZ <CN0579>`
-  `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__

      - 5V/2A wall power supply with barrel jack (comes with DE10-Nano)
      - mini USB to USB Type A (comes with DE10-Nano)

-  `Class 10 16GB SD Card <https://www.amazon.com/gp/product/B073K14CVB/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1>`__
   with boot files in :download:`cn0579_boot_files.zip`
-  Ethernet cable
-  IEPE-compatible sensor

**Software**

- :ref:`kuiper`
- :ref:`iio-oscilloscope`

Hardware Setup
~~~~~~~~~~~~~~

.. figure:: 579_de10_setup.png

#. Mount the EVAL-CN0579-ARDZ onto the DE10-Nano.
#. Connect a monitor to the DE10-Nano using an HDMI cable.
#. Connect a USB OTG adapter to the DE10-Nano's USB OTG port. If additional USB ports
   are needed, attach a USB hub to the adapter.
#. Connect your keyboard and mouse to the USB OTG adapter or USB hub.
#. Plug in the DE10-Nano power supply.
#. Wait for the system to boot. The desktop will appear on your monitor once startup is complete.

.. figure:: kuiper.png

Software Setup
~~~~~~~~~~~~~~~

Preparing the SD Card
^^^^^^^^^^^^^^^^^^^^^

To prepare the SD card for the DE10-Nano board:

#. :dokuwiki:`Download ADI Kuiper Image </resources/tools-software/linux-software/kuiper-linux>`
#. Validate, format, and flash the SD Card

    - :dokuwiki:`Format and flash the SD Card using Windows </resources/tools-software/linux-software/zynq_images/windows_hosts>`
    - :dokuwiki:`Format and flash the SD Card using Linux </resources/tools-software/linux-software/zynq_images/linux_hosts>`

Download and Install IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the latest :ref:`iio-oscilloscope`
   from GitHub and install it on your PC. (You may need to right-click the
   installer and run as ``Elevated`` in order to get it to install.)
#. Once microSD card has been imaged, safely remove the hardware from the SD
   card writer, and insert the card directly into the microSD card slot on the
   DE10-Nano.

----

General Setup Using Cora Z7
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demo Requirements
^^^^^^^^^^^^^^^^^

The following is the list of items needed in order to replicate this demo.

**Hardware**

- :adi:`EVAL-CN0579-ARDZ <CN0579>`
- `CoraZ7-07s FPGA Board <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development>`__
- `Class 10 16 GB SD Card <https://www.amazon.com/gp/product/B073K14CVB/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1>`__
- Ethernet cable
- Micro USB to USB Type A cable
- IEPE-compatible sensor

**Software**

- `ADI Kuiper Image for CN0579 <https://swdownloads.analog.com/cse/kuiper/cn0540.tar.gz>`__
- :ref:`iio-oscilloscope`

Hardware Setup
~~~~~~~~~~~~~~

.. figure:: 579_coraz7_setup.png

#. Mount the EVAL-CN0579-ARDZ on the Cora Z7.
#. Connect the Ethernet cable on the Cora Z7 and on your PC.
#. Power up Cora Z7 by plugging its power supply or connecting microUSB.
#. Wait for the system to boot up. Upon boot up, open command terminal or any similar applications like PuTTy to communicate with the board.

Software Setup
~~~~~~~~~~~~~~~

Preparing the SD Card
^^^^^^^^^^^^^^^^^^^^^

To prepare the SD card for the DE10-Nano board:

#. :dokuwiki:`Download ADI Kuiper Image </resources/tools-software/linux-software/kuiper-linux>`
#. Validate, format, and flash the SD Card

   - :dokuwiki:`Format and flash the SD Card using Windows </resources/tools-software/linux-software/zynq_images/windows_hosts>`
   - :dokuwiki:`Format and flash the SD Card using Linux </resources/tools-software/linux-software/zynq_images/linux_hosts>`

Download and Install IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the latest :ref:`iio-oscilloscope`
   from Github, and install it on your PC. (You may need to right-click the
   installer, and run as ``Elevated`` in order to get it to install.)
#. Once the microSD card has been imaged, safely remove the hardware from the SD
   card writer, and insert the card directly into the microSD card slot on the
   DE10-Nano.

----

Application Software
--------------------

The :adi:`EVAL-CN0579-ARDZ <CN0579>` is supported by the Libiio library. This
library is cross-platform (Windows, Linux, Mac) with language bindings for C,
C#, Python, MATLAB, and others. Two easy examples that can be used with the
:adi:`EVAL-CN0579-ARDZ <CN0579>` are:

- :dokuwiki:`IIO Oscilloscope Installation Guide </resources/tools-software/linux-software/iio_oscilloscope>`
- :ref:`pyadi-iio`

Connection
~~~~~~~~~~

To be able to connect your device, the software must be
able to create a context. The context creation in the software depends on the
backend used to connect to the device, as well as the platform where the
EVAL-CN0579-ARDZ is attached. The platforms currently supported for the
:adi:`EVAL-CN0579-ARDZ <CN0579>` are Cora Z7 and DE10-Nano using the ADI
Kuiper Linux. The user needs to supply a URI, which will be used in the
context creation. The Libiio is a library for interfacing with IIO devices.

.. admonition:: Download

   Install the `Libiio package <https://github.com/analogdevicesinc/libiio/releases>`__
   on your machine.

The :ref:`libiio iio_info` command is a part of the libIIO package that reports
all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For Windows machine connected to ZedBoard via Ethernet cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using SSH Terminal Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open SSH Terminal Software (PuTTY, TeraTerm, or similar). The user should now
start the PuTTY application and enter certain values in the configuration
window. In the terminal, run:

.. shell::

   $ iio_info -u ip:<ip_address>

Using Command Terminal
^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   $ iio_info -s

Prompting this on the command terminal in your Windows PC will give you the 
IP address to access the EVAL-CN0579-ARDZ.

.. code-block:: console

   ssh analog@<ip_address>

.. shell::

   $ iio_info -u ip:<ip_address>

IIO Commands
^^^^^^^^^^^^

There are different commands that can be used to manage the device being used.
The :ref:`libiio iio_attr` command reads and writes IIO attributes.

.. shell::

   $ iio_attr [OPTION]...

**Example:**

- To look at the context attributes, enter this code on the terminal:

.. shell::

   $ iio_attr -a -C

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. admonition:: Download

   Make sure to download/update to the latest version of IIO Oscilloscope
   :git-iio-oscilloscope:`release <releases+>`.

#. Once done with the installation or an update of the latest IIO Oscilloscope,
   open the application. The user needs to supply a URI, which will be used in
   the context creation of the IIO Oscilloscope and the instructions can be seen
   in the previous section.
#. Press refresh to display available IIO Devices. Once cn0579 appeared, press
   ``Connect``.

   .. figure:: 579_osc.png

Debug Panel
^^^^^^^^^^^

Below is the Debug panel wherein you can directly access
the attributes of the device.

.. figure:: 579_debug0.png

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the ADC voltages.

.. figure:: 579_dmm.png

Pyadi-IIO
~~~~~~~~~~

:ref:`pyadi-iio` is a Python abstraction module for ADI hardware
with IIO drivers to make them easier to use. This module provides device-specific APIs
built on top of the current libIIO Python bindings. These interfaces try to match
the driver naming as much as possible without the need to understand the complexities
of libIIO and IIO.

Running the Example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO on your
machine, you are now ready to run Python script examples. In our case, run the
:git-pyadi-iio:`PyADI-IIO CN0579 example <examples/cn0579/cn0579_example.py>`.

#. Connect the :adi:`EVAL-CN0579-ARDZ <CN0579>` to the DE10-Nano or Cora Z7.
#. Open command prompt or terminal and navigate through the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
#. Run the example script using the command.

   .. shell::

      /pyadi-iio/examples
      $ python3 cn0579_example.py

The expected output should look like this:

**Without input signal:**

.. figure:: 579_ex_no_input.png

**With input from ADALM2000 (1Vp-p, 1 kHz) on Channel 0:**

.. figure:: 579_ex_ch0_input.png

GitHub link for the Python sample script:
:git-pyadi-iio:`PyADI-IIO CN0579 example <examples/cn0579/cn0579_example.py>`

Reference Demos & Software
--------------------------

- :ref:`PyADI-IIO Installation Guide <pyadi-iio>`
- :dokuwiki:`IIO Oscilloscope Installation Guide </resources/tools-software/linux-software/iio_oscilloscope>`
- :ref:`Kuiper Images <kuiper>`
- :git-hdl:`CN0579 HDL Reference Design </projects/cn0579>`

More Information and Useful Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`CN0579 Circuit Note Page <CN0579>`
- :adi:`AD7768-4 Product Page <AD7768-4>`
- :adi:`AD5696R Product Page <AD5696R>`
- :adi:`ADA4807-2 Product Page <ADA4807-2>`
- :adi:`AD8605 Product Page <AD8605>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADR4540 Product Page <ADR4540>`
- :adi:`ADP1613 Product Page <ADP1613>`
- :adi:`ADP7142 Product Page <ADP7142>`
- :adi:`ADG5421F Product Page <ADG5421F>`
- :adi:`ADP7118 Product Page <ADP7118>`
- :adi:`LT3092 Product Page <LT3092>`
- :adi:`LT8333 Product Page <LT8333>`

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`EVAL-CN0579-ARDZ Design & Integration Files <cn0579-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information about this product, connect with us through
the Analog Devices :ez:`ez/reference-designs`.
