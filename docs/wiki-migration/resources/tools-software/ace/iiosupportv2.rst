ACE - IIO Support
=================

IIO Support will be added to ACE as of version 1.19

This WIKI site will give a brief description of the available support for IIO devices in ACE, while also stepping through an example ACE plug-in which has been updated to support IIO devices.

You can return to the ACE WIKI Homepage here: :doc:`ACE Homepage </wiki-migration/resources/tools-software/ace>`

What is IIO
-----------

IIO (Industrial I/O) is a subsystem for Analog to Digital Converters (ADCs), Digital to Analog Converters (DACs) and various types of sensors. It can be used on high speed, high data rates industrial devices. Until recently, it was mostly focused on user-space abstraction. It also includes in-kernel API for other drivers.

For more information on IIO visit one of the links provided below:

-  :doc:`Linux Industrial I/O Subsystem </wiki-migration/software/linux/docs/iio/iio>`
-  :doc:`What is libiio? </wiki-migration/resources/tools-software/linux-software/libiio>`

Getting Started
~~~~~~~~~~~~~~~

In order to demonstrate ACE's IIO support there are several hardware and software requirements.

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

Download and install both ACE and LibIIOWCFProcessWrapper from the links attached below. The ADGenericIIO plug-in can be installed from inside ACE's plug-in manager.(:doc:`ACE Quickstart - Using ACE and Installing Plug-ins </wiki-migration/resources/tools-software/ace/userguide/quickstart>`)

-  ACE :adi:`ACE Landing Page <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
-  LibIIOWCFProcessWrapper `LibIIO Wrapper Download <https://swdownloads.analog.com/ACE/LibIIOProcessWrapper/LibIIO_Wrapper_1.1.0.167.exe>`__
-  ADGenericIIO ACE Plugin (Available From ACE's Plug-in Manager)

What is LIbIIOWCFProcessWrapper
-------------------------------

LIbIIOWCFProcessWrapper is a process which is used to interface between IIO devices using LibIIO and ACE. For more information on LibIIO visit the links attached below.

-  :git-libiio>`__
-  `API Documentation <http::`Github </analogdevicesinc.github.io/libiio>`

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

For this example a ZedBoard running IIO acts as a controller board, the SD card contains the appropriate files (E.x Device Tree) for the AD40XX. The ZedBoard is then connected to the PC over an Ethernet connection.

-  AD40XX
-  Controller Board Running IIO (ZedBoard)
-  SD Card (8GB) with the appropriate driver (:doc:`SD Card Set-up </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`)

Validating Hardware Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the hardware has been configured, verifying that IIO is running as expected on the device is the next step. This can be done using IIO Oscilloscope or using a serial communications tool such as putty.

.. tip::

   \ :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` can be used as a means of verifying the set up. If it is possible to detect the device and capture data with IIO oscilloscope, then the hardware is set up as expected and you can skip on to validating the software.


-  Using the available UART connection on the board, connect the ZedBoard to the PC.
-  Download and install a serial communication tool such as putty.
-  Power on the ZedBoard with the AD40XX attached. A blue LED should appear once the FPGA has loaded.
-  Attempt to open a serial connection with the attached board.(Baud Rate 115200) Once a connection has been established send the following command "iio_info".
-  This should respond with information on the attached board such as: number of devices, number of channels and attribute information. This confirms the hardware is operating as expected.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio_info.png
   :align: right

For more information on IIO commands

-  :doc:`IIO Command Line Tools </wiki-migration/resources/tools-software/linux-software/libiio/cmd_line>`
-  :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>`

Validating Software Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Verify ACE and LibIIOWCFProcessWrapper have been installed by navigating to the Analog Devices directory under program files. (E.x C:\\Program Files\\Analog Devices)
-  Two sub directories should be present called LibIIO Wrapper and ACE. Verify both directories are not empty.
-  Open ACE and select the plug-in manager from the side bar menu.
-  From available packages search for Board.ADGenericIIO and Board.ADIIOController install both plug-ins. (:doc:`ACE and Installing Plug-ins </wiki-migration/resources/tools-software/ace/userguide/quickstart>`)
-  Restart ACE.
-  When ACE is starting up, another window should appear with the heading "LibIIO WCF Server Process Started".

Acquiring an IIO Device in ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on the type of device that is running IIO it is possible to create a connection with ACE either using a serial connection or over Ethernet. For the ZedBoard and the AD40XX this example will demonstrate a connection over Ethernet.

-   Select the Manually Add Subsystem button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/selectmanuallyaddsubsystem.png
   :align: center

-  Select Ethernet Boards from the settings tab.
-  Enter the IP which matches the IP on the attached board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iiosettings.png
   :align: center
   :width: 600px

-  Enter in port value "1234"
-  Change the Protocol to IIO.
-  Ensure Ethernet settings are enabled as well as the individual port.

Once the the board settings have been updated ACE will attempt to create a connection with the board at the specified address. If a board has been located it will appear next to the **Manually Add Subsystem** button.

Communicating With An Acquired Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ACE contains a generic IIO plug-in for interfacing with IIO devices. This plug-in allows a user to capture data, modify registers and change attribute values.

.. important::

   IIO must expose the various operations in order to be able to perform them using the generic plug-in


Interfacing with a board using the Generic IIO ACE Plug-in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-manuallyaddsusystem.png
   :align: center

-  Once the generic IIO plug-in appears double click the subsystem. This should navigate to Generic IIO Board view

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboardview.png
   :align: center

-  Press the "Get info" button located in the board view. This will prompt the board to check which IIO device is connected, once a board has been detected the text "NoneDetected" will change to that of the detected board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboardviewfoundboard.png
   :align: center

-  Select the go to chip button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboardviewattributes.png
   :align: center

-  The various exposed attributes are displayed in a Initialization wizard called Initial Configuration. These attributes can be modified in this wizard **ONLY IF THE BOARD ALLOWS ATTRIBUTES TO BE MODIFIED**.
-  Select the register control navigation button

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboardregistercontrol.png
   :align: center

-  The AD40XX contains a register at address 0x00 which it is possible to read from. First specify the address in the address input block and press the read register button.
-  Return back to the chip view. This can be done using the tabs displayed above the register view. The chip tab is labelled "ADGenericIIO"
-  Select the data capture tab.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboarddatacapture.png
   :align: center

-  Update the capture settings to match that of the part connected. For the AD4003, set the resolution to 18 and the encoding as two's compliment.
-  Press run once to perform data capture.

.. tip::

   (Note: in some cases there may some disruption to the signal captured by ACE. To remedy this, turbo mode should be set to true. This can be done by writting the value 0xE3 to register 0x00. Once completed attempt to capture data again)


.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/iio-genericboarddatacapture.png
   :align: center

-  Once data has been returned from the part it is possible to use the various analyzers exposed in ACE. (Waveform, FFT and Histogram)

Supported Hardware Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As ACE IIO support is relatively new, currently there is only a small number of controller boards and plug-ins that have been tested with ACE. A list of supported controller boards and plug-ins have been attached below

Supported IIO Controller Board
------------------------------

-  ZedBoard
-  SDP-K1 (tinyiio)

Supported Plug-ins
------------------

-  AD40XX
