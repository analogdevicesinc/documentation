AD4110 IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM Mbed platform supported firmware example with Analog Devices AD4110 Evaluation board(s) and SDP-K1 controller board. This example code leverage the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD4110 family devices by providing a device debug and data capture support.

The overview of an entire system is shown below:


|image1|

IIO oscilloscope is used as client application running on windows-os, which is ADI developed GUI for ADC data visualization and device debug. The interface used for communicating client application with firmware application (IIO device) is UART (Note: SDP-K1 can also support high speed VirtualCOM port @1Mbps or higher speed for faster data transmission). The firmware application communicates with IIO device (AD4110) using ADI No-OS drivers and platform drivers low level software layers. SDP-K1 is used as controller board, on which IIO firmware application runs and using above software libraries, the IIO firmware communicates with AD4110 IIO device. The AD4110-1 Eval board is used for development and testing of this application.

.. note::

   This code has been developed and tested on SDP-K1 Controller Board using the on-board Arduino Headers. However, same code can be used without or with little modifications on any Mbed enabled board which has Arduino Header Support on it, such as STM32-Discovery, STM32-Nucleo, etc.


--------------

Useful links
------------

-  `Kei Studio <https://studio.keil.arm.com/auth/login/>`_
-  `SDP-K1 on Mbed <https://os.mbed.com/platforms/SDP_K1/>`_
-  :git-no-OS:`AD4110 No-OS drivers <drivers/afe/ad4110>`
-  :adi:`AD4110-1 <en/products/ad4110-1.html>`

--------------

Hardware Connections
--------------------

SDP-K1:
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD4110-1SDZ:
~~~~~~~~~~~~~~~~~

Please refer to the :adi:`EVAL-AD4110-SDZ user guide <media/en/technical-documentation/user-guides/eval-ad4110-1sdz-ug-1203.pdf>`. to know the jumper connections to the EVAL board

SDP-K1 is powered through USB connection from the computer. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to IIO Oscilloscope GUI running on windows-os. The COM port assigned to a device can be seen through the device manager for windows based OS. |image2| SDP-K1 can also support high speed VirtualCOM port UART interface if “USE_VIRTUAL_COM_PORT” macro is defined in the firmware (in app_config.h file).


|image3|

Mbed Firmware
^^^^^^^^^^^^^

.. admonition:: Download
   :class: download

   Latest firmware (Use below link):

   
   -  `AD4110 IIO Firmware Application <https://os.mbed.com/teams/AnalogDevices/code/EVAL-AD4110/>`_
   


Quick Start to use Mbed IIO Firmware
""""""""""""""""""""""""""""""""""""

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail:

-  Connect the AD4110 EVAL-board to the SDP-K1 controller board as specified in hardware connections section.
-  Connect the SDP-K1 controller board to your computer over USB provided along with SDP-K1 board.
-  Go to the link of the code provided above in the 'Downloads' section and import code into Keil studio.
-  Ensure SDP-K1 controller board is selected.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/sdp_k1_target_keil.png
   :align: center
   :width: 600px

-  Set the imported project folder as active project (Right click on the ad717x_mbed_iio-application→ Set Active Project).
-  Make sure that all the dependent libraries are imported. This happens automatically when the active project has been configured.
-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this on your drive.
-  Drag and drop this binary to the USB drive hosted by your controller board.

Libiio: IIO Library
^^^^^^^^^^^^^^^^^^^

This library provides an abstracted library interface to communicate IIO device (AD4110) and IIO client application (IIO Oscilloscope) without worrying about the low level hardware details. Download and install below :doc:`Libiio </wiki-migration/resources/tools-software/linux-software/libiio>` windows installer in your computer.

.. admonition:: Download
   :class: download

   Libiio installer for Windows (Use below link):

   
   -  :git-libiio:`libiio windows installer (.exe) <releases>`
   


IIO Oscilloscope (Client)
^^^^^^^^^^^^^^^^^^^^^^^^^

This is a GUI (Graphical User Interface) based IIO client application for data visualization and device configuration/debugging. The data from IIO devices (ADCs/DACs) is transmitted over Serial/Ethernet/USB link to IIO Oscilloscope client through the abstracted layer of "libiio". Download and install below :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` windows installer in your computer.

.. admonition:: Download
   :class: download

   IIO Oscilloscope installer for Windows (Use below link):

   
   -  :git-iio-oscilloscope:`IIO Oscilloscope windows installer (.exe) <releases>`
   


--------------

Evaluating AD4110 Using IIO Ecosystem
-------------------------------------

.. note::

   Ensure that hardware connection has been made properly in between Mbed Controller Board (SDP-K1) and AD4110 Eval board. Also ensure all software's (IIO firmware, Libiio windows installer and IIO Oscilloscope windows installer) are downloaded and installed in your computer before trying to communicate with AD4110 device.


Running IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on 'Refresh' button and AD4110 device should pop-up in IIO devices list. Click 'Connect'.


|image4|

Configure/Access Device Attributes (Parameters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes". There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters e.g. oversampling rate, operating mode
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters e.g. Scale, Raw, Offset.

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, write a attribute value in the 'Value' field and press 'Write' button. The value to be written corresponds to expected bit-field for that parameter, specified in the datasheet.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/iio_oscilloscope_step-1.png
   :align: center
   :width: 600px

Using DMM Tab to Read DC Voltage on Input Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button.

*\*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, it is not encouraged to use Data Capture or Debug tab as this could impact data capturing.*


|image5|

There firmware supports various demo modes- Voltage, Current, RTD, Field Power Supply and Thermocouple modes. The expected output quantity for each mode is as follows:

-  Voltage Mode - Voltage in V
-  Current Mode - Current in mA
-  RTD Mode - Temperature in degree C
-  Thermocouple Mode - Temperature in degree C
-  Field Instrument Mode - Current in mA

The demo modes shall be invoked by re-defining the *ACTIVE_DEMO_MODE_CONFIG* macro seen in the app_config.h. The list of permissible demo modes have been defined in the same file.

Data Capture from IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To capture the data from AD4110 IIO device, simply select the device and channels to read/capture data. The data is plotted as "ADC Raw Value" Vs "Number of Samples" and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

*\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing.*

More info here: :doc:`/wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app`

Time Domain: |image6| Frequency Domain:


|image7|

Accessing the Register Map of the Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tab is used to access the device registers in byte mode. Enter the register address in the 'Address' field and click on the 'Read' button to read the contents of the register, or 'Write' button in case of write to the chosen register.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/reg_map.png
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
------------------------------

Data capture can be achieved with clients other than the IIO Oscilloscope as well. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The *ad4110_data_capture.py* is capable of achieving the same.

Setting-up Python Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Please install python into your local machine. The python scripts are developed and executed using python 3.9.0 version, so recommend using version 3.9.0 or beyond. `Download python <https://www.python.org/downloads/>`_
-  Once python is installed, make sure the environment path (on windows machine) is set properly. You can verify if python is installed properly by typing “python --version” command on command line tool such as gitbash, command prompt, power shell, etc.

|image8| |image9|

-  Install the “pyadi-iio” python package by executing command “python -m pip install pyadi-iio”. Detailed guide on installing it is available in `Python Interfaces for ADI Hardware <https://github.com/analogdevicesinc/pyadi-iio>`_

<fc #008000>\ *\*Make sure to install additional support packages by running requirements.txt file using command “python -m pip install -r requirements.txt from “scripts/” directory”*\ </fc>

Modifying/running Python Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  All python scripts specific to ad4110 IIO firmware are stored into “scripts” folder present in the project directory. So, any script must be executed from this folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/requirements_capture.png
   :align: center
   :width: 600px

-  Update the ‘uri’ interface in script according to COM port assigned to your device (sdp-k1). Default COM port is set to COM16 in all scripts.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4110_uri_update.png
   :align: center
   :width: 600px

Output Obtained from the Python Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While executing the *ad4110_data_capture.py*, the command prompt requests for the number of samples to be entered by the user.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4110_num_samples.png
   :align: center
   :width: 600px

On Entering the number of samples *n*, on successful completion of capturing *n* samples, the data points are stored in a csv as *adc_data_capture.csv* in the folder where the script is present.

|image10| |image11|

--------------

Modifying Firmware
------------------

The below block diagram shows the AD4110 IIO firmware layer. The firmware and the device together supports five different modes of operations - Voltage, Current, Field Power Supply, RTD and the Thermocouple mode.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/firmware_file_structure.png
   :align: center
   :width: 600px

app_config.h
~~~~~~~~~~~~

This file can be used to:

-  Select the desired Demo mode configuration by re-defining the ACTIVE_DEMO_MODE_CONFIG macro
-  Select the required mode of data capture via the DATA_CAPTURE_MODE macro
-  Choose the required method of UART connection using the USE_PHY_COM_PORT macro.
-  Select the Output Data Rate at which the device is expected to operate.

app_config_mbed.h
~~~~~~~~~~~~~~~~~

This file defines the pin mappings for the peripherals for any mbed based board. The 'Arduino' connector has been enabled as the default. The macro definition 'ARDUINO' in the file header needs to be commented out in case the SDP-120 header on the SDP-K1 is to be used.

ad4110_user_config.h
~~~~~~~~~~~~~~~~~~~~

This file is included on selecting the Voltage Mode, which has been defined as the default mode.

ad4110_current_mode_config.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is included on selecting the Current Mode configuration.

ad4110_field_power_supply_config.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is included on selecting the Field Power Supply Mode configuration.

ad4110_rtd_mode_config.h
~~~~~~~~~~~~~~~~~~~~~~~~

This file is included on selecting the RTD Mode configuration.

ad4110_thermocouple_mode_config.h
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file is included on selecting the RTD Mode configuration.

ad4110_iio.c
~~~~~~~~~~~~

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4110 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

ad4110_data_capture.h
~~~~~~~~~~~~~~~~~~~~~

This file defines the data capture implementation of AD4110 for visualizing ADC raw data on IIO oscilloscope.

No-OS Drivers for AD4110
~~~~~~~~~~~~~~~~~~~~~~~~

The no-os drivers provide the high level abstracted layer for digital interface of AD4110 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers.

The functionality related with no-os drivers is covered in below 2 files:

-  ad4110.c
-  ad4110.h

.. tip::

   It is hoped that the most common functions of the AD4110 family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/application_interfaces.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/phy_com_port.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/virtual_com_port.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/step_1_step_2.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/dmm_tab_working.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/data_capturing.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/fft_plot.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_py_env_variable.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_py_version_check.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4110_data_capture_finishd.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4110_python_output.png
   :width: 600px
