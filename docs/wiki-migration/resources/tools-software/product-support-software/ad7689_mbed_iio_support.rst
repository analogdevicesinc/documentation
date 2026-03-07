AD7689 IIO Application
======================

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware example with Analog Devices AD7689 Evaluation board(s) and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD7689 family devices (AD7689, AD7682, AD7699 and AD7949 -one at a time) by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :adi:`AD7689 <en/products/ad7689.html>`
-  :adi:`AD7682 <en/products/ad7682.html>`
-  :adi:`AD7699 <en/products/ad7699.html>`
-  :adi:`AD7949 <en/products/ad7949.html>`
-  :adi:`AD7689 Evaluation Kit <en/products/ad7689.html#product-evaluationkit>`

--------------

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_hw_interface.png
   :align: center
   :width: 600px

Jumper Settings
---------------

-  SDP-K1:
   Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V
-  EVAL-AD7689:
   Use default

AD7689 uses SPI communication for device parameter access and data capture.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
==================

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

--------------

Evaluating AD7689 Using IIO Ecosystem
-------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
---------------------------------

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD7689 device should pop-up in IIO devices list.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_iio_osc_connections.png
   :align: center
   :width: 600px

Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_iio_osc_windows.png
   :align: center
   :width: 600px

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

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_iio_osc_dmm_tab.png
   :align: center
   :width: 600px

Data Capture from IIO Device
----------------------------

To capture the data from AD7689 IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

<fc #ff0000>\ *\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.*\ </fc>

More info here: :doc:`Data Capture using IIO App </wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app>`

Time Domain Plot
----------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_time_domain_plot.png
   :align: center
   :width: 600px

Frequency Domain Plot
---------------------

<fc #ff0000>\ *\*Note: Max 4096 samples can be selected for plotting frequency domain response due to limited buffer size in the firmware.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_freq_domain_plot.png
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data capture can be achieved with python based IIO clients, using 'pyadi-iio' library. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The python scripts are provided along with firmware package.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter

--------------

AD7689 Firmware Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7689_fw_structure.png
   :align: center
   :width: 400px

app_config.h
------------

This file can be used to:

-  Select the active platform using macro “ACTIVE_PLATFORM_MBED” (Only Mbed is supported)
-  Select active device using one of the “DEV_AD7689” Or “DEV_AD7682” Or “DEV_AD7699” Or
-  “DEV_AD7949” macro (one at a time).
-  Select UART baud rate (for physical UART port) using “IIO_UART_BAUD_RATE” macro. Default is 230400.
-  Pin mapping of controller board (SDP-K1) w.r.t. target evaluation board (AD7689).

app_config_mbed.h
-----------------

This file can be used to:

-  Select Mbed compatible board pin mapping w.r.t. Arduino connector (e.g. SDP-K1).
-  Enabling VirtualCOM port (for SDP-K1) using macros “USE_VIRTUAL_COM_PORT” and “VIRTUAL_COM_PORT_ID”.
-  Define the possible sampling rate (ODR). Should never exceed than default ODR selected using macro
-  “SAMPLING_RATE” as this could impact data capture with device.

ad7689_user_config.c/.h
-----------------------

These files define the user configurations for the AD7689, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD7689 device (active device, input channel type, reference source, etc) These are the parameters loaded into device when device is powered-up or power-cycled.

ad7689_data_capture.c
---------------------

This file implements the data capturing logic for the AD7689 device. The adc_data_capture.c module present in platform drivers acts as an abstracted layer for common IIO application data capturing

ad7689_iio.c
------------

This file defines getter/setter functions for all the device and channel specific attributes (related to AD7689 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

No-OS Drivers for AD7689
------------------------

The no-os drivers provide the high level abstracted layer for digital interface of AD7689 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers. The functionality related with no-os drivers is covered in below 2 files:

-  ad7689.c
-  ad7689.h
