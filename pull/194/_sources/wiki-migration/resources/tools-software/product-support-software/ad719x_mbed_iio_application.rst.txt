AD719x IIO Application
======================

Introduction
============

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware example with Analog Devices AD719x Evaluation board and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD719x device by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :git-no-OS:`AD719x No-OS drivers <drivers/adc/ad719x>`
-  :adi:`AD7190 Product Page <en/products/ad7190.html>`
-  :adi:`AD7192 Product Page <en/products/ad7192.html>`
-  :adi:`AD7193 Product Page <en/products/ad7193.html>`
-  :adi:`AD7195 Product Page <en/products/ad7195.html>`

--------------

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

Jumper Settings: SDP-K1: Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD719X:

-  Stack the EVAL-AD719X-ASDZ on the Arduino connectors of the SDP-K1 board.
-  Connect a male-to-male jumper wire between D8 and D12 on Arduino connectors.
-  Set the LK7 and LK8 jumper headers to 3.3V.
-  Set LK12 jumper header to position

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_hardware_connection.png
   :width: 800px

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
==================

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

--------------

Evaluating AD719x Using IIO Ecosystem
-------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
---------------------------------

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD719X device should pop-up in IIO devices list.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_osc_new.png
   :width: 800px

Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_osc_windows.jpg
   :width: 800px

Configure/Access Device Attributes (Parameters)
-----------------------------------------------

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes“. There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters.
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters.

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, select attribute value in the 'value field' and press 'Write' button.

Using DMM Tab to Read DC Voltage on Input Channels
--------------------------------------------------

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button.

<fc #ff0000>\ *\*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, do not access/use the Data Capture or Debug tab as this could impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_osc_dmm.png
   :width: 600px

Data Capture from IIO Device
----------------------------

To capture the data from AD719x IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

<fc #ff0000>\ *\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.*\ </fc>

More info here: :doc:`Data Capture using IIO App </wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app>`

Time Domain Plot
----------------

<fc #ff0000>//\*Note: When enabling more than 4 channels, the number of samples should be decreased to 200 to avoid timeout in the IIO oscilloscope. //</fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_osc_plot.png

Frequency Domain Plot
---------------------

<fc #ff0000>\ *\*Note: Max 4096 samples can be selected for plotting frequency domain response due to limited buffer size in the firmware.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_osc_fft.png

--------------

Python Environment and Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data capture, device calibration, etc. can be achieved with python based IIO clients, using 'pyadi-iio' library. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The python scripts are provided along with firmware package.

Setting-up Python Environment

-  Please install python into your local machine. The python scripts are developed and executed using python 3.8.0 version, so recommend using version 3.8.0 or beyond. Download python
-  Once python is installed, make sure the environment path (on windows machine) is set properly. You can verify if python is installed properly by typing “python --version” command on command line tool such as gitbash, command prompt, power shell, etc.
-  Install the “pyadi-iio” python package by executing command “python -m pip install pyadi-iio”. Detailed guide on installing it is available in Python Interfaces for ADI Hardware

\* Make sure to install additional support packages by running requirements.txt file using command “python -m pip install -r requirements.txt” from “scripts/” directory.”

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_requirement.png

Modifying/running Python Scripts
--------------------------------

-  All python scripts specific to ad719x IIO firmware are stored into “scripts” folder present in the project directory.
-  Ensure that the firmware is compiled with the noise testing mode, using the macros in the app_config.h file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_config.png

-  Update the ‘uri’ interface in script according to COM port assigned to your device (sdp-k1). Default COM port is set to COM16 in all scripts.
-  Update the ‘device_name’ variable to match with the device name in the compiled firmware.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_com.png

-  Enable the channel and size of the sample block for noise analysis.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_samples.png

Output Obtained from the Python Script While executing the ad719x_rms_50hz_test.py, the command prompt requests for the number of samples to be entered by the user. This should be multiple of defined sample block size. On successful completion of capturing n samples, the noise data is displayed on the windows and the data points are stored in a csv as adc_data_capture.csv in the folder where the script is present.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_output.png
   :alt:

   |image1|

--------------

AD719x Firmware Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_firmware_structure.png

app_config.h
------------

This file can be used to:

-  Select the active platform using macro “ACTIVE_PLATFORM_MBED” (Only Mbed is supported)
-  Select UART baud rate (for physical UART port) using “IIO_UART_BAUD_RATE” macro. Default is 230400.
-  Select burst capture mode or continuous capture mode using “DATA_CAPTURE_MODE” macro.
-  Select the active device by defining as “DEV_AD7193”. Default is AD7193
-  Uncomment the “BIPOLAR_MODE” macro to enable bipolar mode. Default is Unipolar mode.
-  Uncomment the “DIFFERENTIAL_INPUT” macro to enable differential input. Default is Pseudo differential input.

ad719x_user_config.c/.h
-----------------------

These files define the user configurations for the AD719X, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD719X device (gain, data output rate, reference voltage etc).

ad719x_data_capture.c
---------------------

This file implements the data capturing logic for the AD719x device. The data capturing can be done using normal burst mode or continuous mode.

ad719x_iio.c
------------

This file defines getter/setter functions for all the device and channel specific attributes (related to AD719X devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

No-OS Drivers for AD719x
------------------------

The no-OS drivers provide the high level abstracted layer for digital interface of AD719x devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers. The functionality related with no-os drivers is covered in below 2 files:

-  ad719x.c
-  ad719x.h

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad719x_iio_python_2.png
