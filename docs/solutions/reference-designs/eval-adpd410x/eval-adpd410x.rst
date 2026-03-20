Quick Start Guide
==================

The :adi:`EVAL-ADPD410x-ARDZ` is a simple, Arduino form-factor breakout
board for developing :adi:`ADPD4100` and :adi:`ADPD4101` applications.
The :adi:`ADPD4101`, interfaced through I2C, and the :adi:`ADPD4100`,
interfaced through SPI, are highly versatile, multimodal sensor front
ends, stimulating up to eight light emitting diodes (LEDs) and measuring
the return signal on up to eight separate current inputs. There are a
number of other evaluation platforms for these devices, including the
:adi:`EVAL-ADPD4100Z-PPG`, optimized for photoplethysmograph
applications, and the reference design :adi:`CN0503`, optimized for
optical liquid analysis applications such as colorimetry, turbidity, and
fluorescence. The :adi:`EVAL-ADPD410x-ARDZ` board come in handy for
adapting these evaluation boards to meet specific application
requirements, as well as for "ground up" development of new
applications.

|image1|

Features
--------

-  8 LED excitation channels with high-voltage extension circuitry
-  8 Photodiode inputs

Device Driver and Support
-------------------------

A no-OS device driver and an example program are provided, targeting the
:adi:`EVAL-ADICUP3029` platform. The ADICUP3029 example application uses
the ADPD410x no-OS driver and emulates the Linux IIO framework through
the tinyiiod daemon library. The application communicates with the host
computer via the serial backend over a USB-UART physical connection.
This facilitates rapid application development on a host computer,
independent from embedded code development.

Similarly, utility software (such as iio_info, IIO Oscilloscope,
PyADI-IIO, etc.) typically associated with Linux systems can be used
with this no-OS implementation.

Materials Needed
----------------

-  :adi:`EVAL-ADICUP3029`
-  :adi:`EVAL-ADPD410x-ARDZ`
-  Micro USB to USB cable
-  PC or laptop with a USB port

Hardware Setup
--------------

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~

There are two shunt-configurable jumpers and three types of solder
jumpers on the :adi:`EVAL-ADPD410x-ARDZ` board.

I/O Logic Voltage (IOSEL) Shunt Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====================== ==============
Correct Shunt Position Layout Picture
====================== ==============
Shorted Pin 1 and 2    |image2|
====================== ==============

Onboard LED and Photodiode (P10) Shunt Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The onboard LED and photodiode are by default connected to LED1A and
PD1A, respectively. **When using external LEDs and sensors on this
channel, make sure to remove this connection using jumper header P10.**

=============================================================== ==============
 Correct Shunt Position                                         Layout Picture                    
=============================================================== ==============
Shorted Pin 1 and 2, Shorted Pin 3 and 4, Shorted Pin 5 and 6   |image3|
=============================================================== ==============

LED Supply Voltage (JP1) Solder Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====================== ==============
Correct Shunt Position Layout Picture
====================== ==============
Shorted Pin 2 and 3    |image5|

====================== ==============

LED Driver Connection P9, P11, P13, P15, P17, P19, P22, P24
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

====================== ==============
Correct Shunt Position Layout Picture
====================== ==============
Shorted                |image6|
====================== ==============

SPI or I2C Interface
^^^^^^^^^^^^^^^^^^^^

+--------------------------+-----------------------------------+
| Board                    | Shorted Resistors                 |
+==========================+===================================+
| EVAL-ADPD410x-ARDZ (SPI) | Shorted R8 and R9, Open R6 and R7 |
+--------------------------+-----------------------------------+

Below is a photo of the :adi:`ADPD4100` (SPI) board with all the
correct shunt and solder jumper connections.

|image9|

+------------------------------------------------------+
| Board                           | Shorted Resistors  |
+=================================+====================+
| :adi:`ADPD4101` (I2C)           | Shorted R6 and R7, |
|                                 | Open R8 and R9     |
+------------------------------------------------------+

Below is a photo of the EVAL-ADPD4101-ARDZ (I2C) board with all the
correct shunt and solder jumper connections.

|image12|

Prototyping Connectors
~~~~~~~~~~~~~~~~~~~~~~

The board has two parallel 18-pin, 100-mil pitch male connectors, which
give access to the LED driver channels, the photodiode inputs, custom
I/O pins from the AFE, and supply voltage for the LED. The user can use
this along with the break-away protoboard to implement a custom circuit
for testing. The pin assignment and functions are shown below.

|image13| |image14|

Pins labeled **XYC** (where X refers to LED 1, 2, 3, or 4, and Y refers
to channel A or B) denote connections to the LED cathode which are
voltage protected via transistors to the ADPD4100/1 LED inputs (denoted
by **LXY**). It is recommended to connect LED cathodes to these pins
instead of connecting directly to **LXY** pins. **PDXY** (X refers to
photodiode 1, 2, 3, or 4 and Y refers to channel A or B) pins denote
photodiode signal inputs to the AFE. **ACOM** and **BCOM** pins refer to
the common cathode bias output for photodiode sensors. These should be
connected to the cathodes of photodiodes in the matching channel (for
example, photodiodes connected to PD1A, PD2A, PD3A, and PD4A should
have their cathodes connected to ACOM).

A simple circuit for testing LED driver outputs and photodiode current
sensing using the break-away prototype board can easily be set up using
optocouplers, as shown below.

.. image:: images/testschematic.png
   :width: 600

General Connection
~~~~~~~~~~~~~~~~~~

-  Set the following EVAL-ADICUP3029 switches according to their
   configuration on the table.

      ========== =============
      Switch     Configuration
      ========== =============
      UART (S2)  USB
      POWER (S5) WALL/USB
      ========== =============

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the
   :adi:`EVAL-ADICUP3029` using the headers shown. See correct Jumper
   Configuration for both evaluation boards 
   :doc:`here </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.

      .. image:: images/arduinoconnection.jpg
         :width: 400 px

Driver/Firmware Setup
-----------------------

There are two basic ways to program the :adi:`EVAL-ADICUP3029` with the
software for both boards.

Dragging and Dropping the Hex File to the Daplink Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Ensure that the :adi:`EVAL-ADICUP3029` board switches are set to the
   correct configuration, as detailed in 
   :doc:`General Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Connect the :adi:`EVAL-ADICUP3029` board to the PC or laptop using
   the Micro USB to USB cable.
-  Drag and Drop the appropriate .hex file from the list below to the
   Daplink Drive.

      .. image:: images/daplink_windows_explorer.png
         :width: 550 px

-  The drive will unmount once the .hex file is dropped and wait for it
   to reappear. Once it does, press the reset button of the
   :adi:`EVAL-ADICUP3029` to ensure that the microcontroller is
   updated.

.. admonition:: Download
   :class: download

   Pre-built HEX files can be found here:

   -  `EVAL-ADPD4100-ARDZ HEX File
      (ADuCM3029_demo_adpd410x_spi.hex)
      <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/
      download/Latest/ADuCM3029_demo_adpd410x_spi.hex>`_
   -  `EVAL-ADPD4101-ARDZ HEX File
      (ADuCM3029_demo_adpd410x_i2c.hex)
      <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/
      download/Latest/ADuCM3029_demo_adpd410x_i2c.hex>`_

   The latest source code can be found here:

   -  :git-EVAL-ADICUP3029:`EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_adpd410x<projects/ADuCM3029_demo_adpd410x>`.

Using CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Acquire a copy of the project source files of the
   :adi:`EVAL-ADPD410x-ARDZ` by downloading the source files directly
   from the repository at :git-EVAL-ADICUP3029:`EVAL-ADICUP3029/tree/master/projects/ADuCM3029_demo_adpd410x<projects/ADuCM3029_demo_adpd410x>` 
   or you can clone the entire `EVAL-ADICUP3029 repository
   <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`_ and check
   the projects folder for ADuCM3029_demo_adpd410x.
-  Open CrossCore Embedded Studio and import the project into your
   workspace, as detailed in the `cces_user_guide
   <https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/
   tools/cces_user_guide>`_. This allows you to edit the software to
   fit your requirements.

.. important::

   If this is your first time using CrossCore Embedded Studio, check the
   `user guide
   <https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/
   tools/cces_user_guide>`_ to get started.

-  Once ready, you can opt to generate your own .hex file and use the
   first method to program the :adi:`EVAL-ADICUP3029` or you can use a
   debug session by following the quickstart guide.

CrossCore Project Header File Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Select which board the project will support when built using
   :git-EVAL-ADICUP3029:`projects/ADuCM3029_demo_adpd410x/src/app_config.h`.

   -  For EVAL-ADPD4100-ARDZ

       |image15|

   -  For EVAL-ADPD4101-ARDZ

       |image16|

         You can configure the default timeslots and other settings of the
         :adi:`ADPD4100` or :adi:`ADPD4101` using 
         :git-EVAL-ADICUP3029:`projects/ADuCM3029_demo_adpd410x/src/adpd410x_app_config.h`.

-  You can set the default number of active timeslots and output data
   rate.

   |image17|

-  Initial timeslot settings are configured using the
   **adpd410x_timeslot_init** data structure, as shown below:

   |image18|

-  **Enabling ADC channel 2**

   Each timeslot can use the two ADC input channels of the ADPD4100/1.
   By default, the timeslot only uses channel 1. Setting this to true
   will enable channel 2.

-  **Timeslot Inputs**

   |image19|

   Each timeslot input can be set to use a pair of input pins of the
   ADPD4100/1. Below are possible pair options:

   |image20|

-  Each of the input pins can be disabled or routed to any or both of
   the channels. Below are the possible configurations of the input
   pins.

   |image21|

-  **Timeslot Input Preconditioning**

   Timeslot inputs have programmable connections, which precondition the
   sensor to set operating conditions before sampling. Below are the
   possible options:

   |image22|

-  **TIA Reference Voltage**

   The reference voltage of the Trans-Impedance Amplifier (TIA) is
   configurable. Below are the possible values:

   |image23|

-  **TIA Gain Resistor**

   The gain resistor used by the TIA is configurable for each input
   channel. Below are the possible values:

   |image24|

-  **Multiple Pulses and Integrator Chopping**

      The ADPD4100/1 is capable of improving SNR using multiple pulses per sample
      and integrator chopping, which have configurable settings.

   -  **4-Pulse Reverse Pattern**

      Each pulse from the LED in a set of 4 can be configured to either
      have an on-off or off-on integrator chopping sequence. This is a
      4-bit value, 1 bit for each pulse. Setting a bit reverses the
      integrator chopping sequence for that pulse.

   -  **4-Pulse Subtract Pattern**

      The mathematical operation performed on a digitized ADC sample can
      be set to addition or subtraction for each pulse in a set of 4.
      This is a 4-bit value, 1 bit for each pulse. Setting a bit negates
      the operation for that pulse.

-  **Byte Number**

   This sets the number of data bytes used in the timeslot.

-  **Decimation Factor**

   The decimation factor sets the number of time slot values used in the
   final sample.
   ``output data rate = sample rate / (decimation factor - 1)``

-  **LED Output**

   The 4 LED outputs have configurable output current and can be set to
   either channel A or channel B only. You can define the LED value
   directly or through fields. The first 7 bits are for the output
   current, which scale from 1.5 mA to 200 mA for 0x01 to 0x7F. The
   last bit is for the output channel. Setting this bit selects channel
   B while clearing selects channel A.

   |image25|

-  **ADC Cycles**

   This sets the number of integration cycles per ADC conversion. This
   value can range from 0x01 to 0xFF.

-  **Number of Repeats**

   This sets the number of repeat ADC conversions. This value can range
   from 0x01 to 0xFF. ``total number of pulses = ADC cycles X Number
   of Repeats``

Here is an example timeslot setting used in the pre-built hex files:

|image26|

Software Setup
--------------

Installation
~~~~~~~~~~~~

To communicate with the device from the PC or laptop using IIO commands,
install the Libiio package by following the guide in the repository:
`libiio/releases <https://github.com/analogdevicesinc/libiio/releases>`_. 
The method is different for Windows or Linux operating systems.

Connection
~~~~~~~~~~

The device must be able to create a context. Context creation in the
software depends on the backend used to connect the device. This guide
covers the device communication using the currently supported platform,
a serial backend through a USB-UART connection. A simple way of
checking, if the device is connected, is through the `iio_info
<https://wiki.analog.com/resources/tools-software/linux-software/
libiio/iio_info>`_ command. Specifically, it reports all IIO attributes
of a detected device and context. To do this, simply enter the below
command to a terminal or command line.

::

   iio_info -u serial:<serial port>

Examples:

-  In a Windows machine, you can check the port of your ADICUP3029 via
   Device Manager in the Ports (COM & LPT) section. If your device is
   in COM4, use **serial:COM4** as your URI (e.g., *iio_info -u
   serial:COM4*).
-  In a Unix-based machine, you will see it under the /dev/ directory
   in this format "ttyUSBn", where n is a number depending on how many
   serial USB devices are attached. If you see that your device is
   ttyUSB0, use **serial:/dev/ttyUSB0** as your URI. (e.g., *iio_info
   -u serial:/dev/ttyUSB0*).

An example output of this command should look like the one below:

|image27|

Reading and Configuring the Device from Command Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the `iio_attr
<https://wiki.analog.com/resources/tools-software/linux-software/
libiio/iio_attr>`_ command from the Libiio package, you can read and
configure the device.

Reading Raw Channel Outputs from the Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The -c option of the `iio_attr
<https://wiki.analog.com/resources/tools-software/linux-software/
libiio/iio_attr>`_ command allows reading of the individual raw channel
outputs. Specifically, this reads the raw attribute of the specified
channel of the specified device in the context of the specified URI. The
command follows the format shown below.

::

   iio_attr -u <URI> -c <DEVICENAME> <CHANNELNAME> <ATTRIBUTE>
   For example, for a Windows Machine
   iio_attr -u serial:COM4  -c adpd410x voltage0 raw

-  <URI> specifies the URI similar to the one used in :doc:`Connection
   </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  <DEVICENAME> specifies the device name, which is **adpd410x**.
-  <CHANNELNAME> specifies the channel name, which are formatted as
   voltageX where X can be from 0 to 7.
-  <ATTRIBUTE> specifies the name of the channel attribute, which is
   raw. This is a read-only attribute.

An example output of this command should look like the one below:

|image28|

Reading and Writing Device Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The -d option of the `iio_attr
<https://wiki.analog.com/resources/tools-software/linux-software/
libiio/iio_attr>`_ command allows reading or writing (only for specific
items) of device attributes. For example, the *sampling_frequency*
attribute is readable and writeable. The command to read and write to
this attribute is shown below:

::

   For reading, use iio_attr -u <URI> -d <DEVICENAME> <ATTRIBUTE>
   For writing, use iio_attr -u <URI> -d <DEVICENAME> <ATTRIBUTE>
   <VALUE>
   for example, for a Windows Machine
   iio_attr -u serial:COM4 -d adpd410x sampling_frequency 40

-  <URI> specifies the URI similar to the one used in :doc:`Connection
   </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  <DEVICENAME> specifies the device name which is **adpd410x**.
-  <ATTRIBUTE> specifies the name of the device attribute which is
   **sampling_frequency**.

An example output of this command should look like the one below:

|image29|

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope
   found on this `link
   <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_.

-  Install and start IIO-Oscilloscope. There are two options you can
   use to select IIO contexts. First, you can use the Serial option and
   input the correct port settings of the board from the Device Manager.
   Another way is by manually entering the URI used in 
   :doc:`Connection</solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.

   |image30|

.. image:: images/iio-oscilloscopemanualcontext.png
   :width: 400

-  Press Refresh to display available IIO Devices, and once adpd410x is
   detected, press Connect. It may take several presses to Connect
   before the software proceeds and opens the Debug Panel and Waveform
   Panel.

.. image:: images/iio-oscilloscopedetecteddevice.png
   :width: 400

Debug Panel
^^^^^^^^^^^

In the Debug Panel, you can directly access the device/channel
attributes and even the device registers. Remember to select first the
adpd410x in the Device Selection section.

|image31|

Waveform Panel
^^^^^^^^^^^^^^

The Waveform panel, also known as the Capture window, displays the
real-time waveform of selected photodiode channels of the ADPD410x.
Select the desired channels to display in the upper left section. You
can also edit the plot settings in the left section.

.. important::

   You cannot use the Debug Panel and the Waveform Panel simultaneously.
   Using the Waveform Panel will freeze the Debug Panel.

   |image32| |image33|

.. important::

   For best device operation and waveform captured, it is recommended to
   use a time domain plot with 20 samples.

Python and PyADI-IIO
~~~~~~~~~~~~~~~~~~~~

`PyADI-IIO <https://wiki.analog.com/resources/tools-software/linux-
software/pyadi-iio>`_ is a python abstraction module for ADI hardware
with IIO drivers to make them easier to use. This module provides
device-specific APIs built on top of the current libIIO python bindings.
These interfaces try to match the driver naming as much as possible
without the need to understand the complexities of libIIO and IIO.

Installing the Packages
^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   PyADI-IIO requires a Python installed on your computer. It is
   recommended to install Python 3.7 or higher.

Install PyADI-IIO using one of the methods in `PyADI-IIO
<https://wiki.analog.com/resources/tools-software/linux-software/
pyadi-iio>`_.

There are two example scripts found in the examples folder in `PyADI-IIO
<https://wiki.analog.com/resources/tools-software/linux-software/
pyadi-iio>`_. To run both examples, the following packages are required:
`pyqtgraph <https://www.pyqtgraph.org>`_, `scipy <https://scipy.org>`_,
`PyQt5 <https://www.riverbankcomputing.com/software/pyqt>`_,
`matplotlib <https://matplotlib.org>`_.

If you are using `pip <https://pip.pypa.io/en/stable>`_, you can
install all of the PyADI-IIO, as well as the example script
dependencies, by following these steps:

-  Clone or download the pyadi-iio repository `pyadi-iio/
   <https://github.com/analogdevicesinc/pyadi-iio/>`_
-  Open command prompt or terminal and navigate to the *pyadi-iio*
   directory.
-  Enter the following commands: ``...\pyadi-iio\>pip install -r
   requirements.txt`` and ``...\pyadi-iio\>pip install -r
   examples/requirements_adiplot.txt`` and
   ``...\pyadi-iio\>python setup.py install``

.. important::

   One of the packages in *requirements_adiplot.txt* is the PyQt5. If you
   already have a pre-installed PyQt5 prior to the installation of the
   packages, it is suggested that you uninstall the said package in the
   virtual environment. Duplicate installations may sometimes cause
   errors that inhibit the system from displaying the real-time plot.
   This can easily be done by inputting the command: *pip uninstall
   PyQt5* while the virtual environment is active.

Running the Examples
^^^^^^^^^^^^^^^^^^^^

There are three example scripts for the ADPD410x found in `pyadi-iio/
<https://github.com/analogdevicesinc/pyadi-iio/>`_. The first simply
reads from the photodiode channels, the second plots specified
photodiode channels, and the third tests the board separately, with its
onboard LED and photodiode and with a test setup built from the simple
example circuit from 
:doc:`Prototyping Connectors</solutions/reference-designs/eval-adpd410x/eval-adpd410x>`. For
example 1, follow these steps:

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the
   :adi:`EVAL-ADICUP3029`.
-  Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro-USB
   cable and note the serial port from the Device Manager as in
   :doc:`Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Open command prompt or terminal and navigate to the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example using the command: ``...\pyadi-iio\examples>python
   adpd410x_example.py``
-  Input the noted serial port and press *Connect*.
   |image34|
-  Once connected, press *Read*.
   |image35|

For example 2, follow these steps:

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the
   :adi:`EVAL-ADICUP3029`.
-  Connect the :adi:`EVAL-ADICUP3029` to the PC using the micro USB
   cable and note the serial port from the Device Manager as in
   :doc:`Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Open command prompt or terminal and navigate to the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example script using the command: ``...\pyadi-iio\examples>
   python adpd410x_plot.py``
-  The script will ask for a serial port. Input the noted serial port
   and press Enter. In cases when the board is not found, press the
   reset button (S1) on the :adi:`EVAL-ADPD410x-ARDZ` and input the
   noted serial port again.

   |image36|

-  When the board is detected, you will be asked to specify the number
   of channels (1 to 8) you want to read. Then, you need to specify the
   desired channel numbers (1 to 8).

   |image37|

-  A plot will appear showing the specified channels. You have the
   option to save a copy of the displayed waveform at any point in time
   using the matplotlib controls at the top.

   |image38|

For example 3, follow these steps:

-  Connect the :adi:`EVAL-ADPD410x-ARDZ` to the EVAL-ADICUP3029.
-  Connect the :adi:`EVAL-ADICUP3029` to the pc using the micro-USB
   cable and note the serial port from the Device Manager as in
   :doc:`Connection </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`.
-  Open command prompt or terminal and navigate to the examples folder
   inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example script using the command: ``...\pyadi-iio\examples>
   python adpd410x_test.py``
-  A GUI window will appear, as shown below. There are four buttons at
   the top right for each test namely, open onboard LED test, covered
   onboard LED test, no load test, and mounted jig test. **Before
   pressing a button to start the test, select the noted COM port on the
   dropdown list at the top left.**

   |image39|

-  **Open Onboard LED Test**

   The test samples raw ADC values from the onboard photodiode and
   checks whether it is consistent with the standard. Make sure that
   all shunts on jumper header P10 are present and connected. A sample
   passing result is shown below

   |image40|

-  **Covered Onboard LED Test**

   Place your finger above the onboard photodiode and LED.

   |image41|

   This test checks if the sampled raw ADC value has significantly
   increased from the standard uncovered value. A sample passing result
   is shown below.

   |image42|

-  **No Load Test**
   Remove all shunts on jumper header P10. This test checks the
   photodiode input when no external sensor is connected. A sample
   passing result is shown below.

   |image43|.

-  **Mounted Jig Test**

   Using the simple test schematic shown in :doc:`Connection
   </solutions/reference-designs/eval-adpd410x/eval-adpd410x>`, a test
   board was fabricated using `MOC207M
   <https://www.onsemi.com/pdf/datasheet/moc217m-d.pdf>`_ optocouplers.
   Remove all shunts on jumper header P10 and connect the test jig to
   the :adi:`EVAL-ADPD410x-ARDZ`, as shown below. **(The test jig shown
   below was fabricated with female headers for easy mounting)**

   |image44|

   A sample passing result is shown below.

   |image45|

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADPD410x-ARDZ Design & Integration Files<media/en/evaluation-documentation/evaluation-design-files/eval-adpd410x-ardz-designsupport.zip>`

   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project

Additional Information and Useful Links
---------------------------------------

-  :adi:`ADPD4100 Product Page <ADPD4100>`
-  :adi:`ADPD4101 Product Page <ADPD4101>`
-  :doc:`Fluorescence Measurement Demo </solutions/reference-designs/eval-adpd410x/fluorescence>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view
   the latest videos, and more when you register your hardware.
   `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADPD410X-
   ARDZ?&v=RevD>`_ to receive all these great benefits and more!

*End of Document*

.. |image1| image:: images/20220105_094532.jpg
   :width: 600
.. |image2| image:: images/iosel_shunt.png
   :width: 200
.. |image3| image:: images/p10_shunt.png
   :width: 100
.. |image4| image:: images/p10_shunt.png
   :width: 100
.. |image5| image:: images/jp1_5v.png
   :width: 100
.. |image6| image:: images/p9_p13_p17_p22_p11_p15_p19_p24.png
   :width: 400
.. |image7| image:: images/adpd4100_r8_r9.png
   :width: 100
.. |image8| image:: images/adpd4100_r8_r9.png
   :width: 100
.. |image9| image:: images/spi.jpg
   :width: 600
.. |image10| image:: images/adpd4101_r6_r7.png
   :width: 100
.. |image11| image:: images/adpd4101_r6_r7.png
   :width: 100
.. |image12| image:: images/i2c.jpg
   :width: 600
.. |image13| image:: images/pinassignment.jpg
   :width: 400
.. |image14| image:: images/pinassignmentdiagram.png
   :width: 400
.. |image15| image:: images/adpd4100_support.png
   :width: 400
.. |image16| image:: images/adpd4101_support.png
   :width: 400
.. |image17| image:: images/activetimeslots_odr.png
   :width: 400
.. |image18| image:: images/timeslot_datastructure.png
   :width: 400
.. |image19| image:: images/timeslot_inputs.png
   :width: 400
.. |image20| image:: images/timeslot_pairoptions.png
   :width: 400
.. |image21| image:: images/timeslot_inputoptions.png
   :width: 400
.. |image22| image:: images/timeslot_precond.png
   :width: 400
.. |image23| image:: images/timeslot_tiavref.png
   :width: 400
.. |image24| image:: images/timeslot_tiares.png
   :width: 400
.. |image25| image:: images/timeslot_led.png
   :width: 400
.. |image26| image:: images/timeslot_example.png
   :width: 400
.. |image27| image:: images/iio_info_-_output.png
   :width: 600
.. |image28| image:: images/rawchanneliio.png
   :width: 600
.. |image29| image:: images/sampling_frequency_iio.png
   :width: 600
.. |image30| image:: images/iio-oscilloscopeserialcontext.png
   :width: 400
.. |image31| image:: images/iio-oscilloscopedebugwindow.png
   :width: 400
.. |image32| image:: images/iio-oscilloscopeplotinstructions.png
   :width: 400
.. |image33| image:: images/iio-oscilloscopeplot.png
   :width: 400
.. |image34| image:: images/pyadiiio_example1_comport.png
   :width: 400
.. |image35| image:: images/pyadiiio_example1_read.png
   :width: 400
.. |image36| image:: images/pyadiiio_example2_comport.png
   :width: 400
.. |image37| image:: images/pyadiiio_example2_inputchannels.png
   :width: 400
.. |image38| image:: images/pyadiiio_example2_plot.png
   :width: 400
.. |image39| image:: images/softwarewindow.png
   :width: 600
.. |image40| image:: images/openledresult.png
   :width: 600
.. |image41| image:: images/coveredled.jpg
   :width: 400
.. |image42| image:: images/coveredledresult.png
   :width: 600
.. |image43| image:: images/noloadtestresult.png
   :width: 600
.. |image44| image:: images/testjig_connection.jpg
   :width: 600
.. |image45| image:: images/mountedjigtestresult.png
   :width: 600
