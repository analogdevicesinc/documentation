AD4130 IIO Application
======================

Introduction
============

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware example with Analog Devices AD4130 Evaluation board and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD4130 device by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :adi:`AD4130 Product Page <en/products/ad4130-8.html>`
-  :adi:`AD4130 Evaluation Kit <en/products/ad4130-8.html#product-evaluationkit>`

--------------

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130-eval_and_sdp-k1_hardware_connections.png
   :align: center
   :width: 600px

Jumper Settings
---------------

-  SDP-K1:
   Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V
-  EVAL-AD4130:
   `ad4130_evb_jumper_settings.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_evb_jumper_settings.xlsx>`_

.. note::

   Above jumper settings of AD4130 EVB are specific to sensor demo modes supported in the firmware. Change the jumper settings according to your requirements.


AD4130 uses SPI communication for device register access and data capture.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
==================

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

--------------

Evaluating AD4130 Using IIO Ecosystem
-------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
---------------------------------

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD4130 device should pop-up in IIO devices list.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_iio_osc_connection.png
   :align: center
   :width: 600px

Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_iio_osc_windows.png
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

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4130_iio_osc_dmm_tab.png
   :align: center
   :width: 600px

Data Capture from IIO Device
----------------------------

To capture the data from AD4130 IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

<fc #ff0000>\ *\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.*\ </fc>

More info here: :doc:`Data Capture using IIO App </wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app>`

Data capturing utilizes two modes:

-  Normal sequencer: In this mode, the channel for which data to be captured are enabled and automatically added into a sequencer. The sequencer operates in the continuous conversion mode. After each conversion, an interrupt signal attached to configured INT source is triggered and conversion result is read into a internal acquisition buffer.

-  FIFO mode: This mode uses the internal FIFO of device to store the ADC samples. The conversion happens in continuous conversion mode and an interrupt signal attached to configured INT source is triggered when internal FIFO becomes full (reached to watermark limit). The data from FIFO is read periodically when FIFO is made available by device. The FIFO is operated in ‘Oldest Save’ mode as there must be enough time provided to read the FIFO after it becomes full. If FIFO is operated into streaming mode, the previous data could get overwritten before it is being acquired by the firmware.

Time Domain Plot
----------------

<fc #ff0000>\ *\*Note: Due to low sampling rate (50SPS) for temperature sensor measurement, select 50 or less samples during data capturing for sensor demo mode channels.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_iio_osc_time_domain_plot.png
   :align: center
   :width: 800px

Frequency Domain Plot
---------------------

<fc #ff0000>\ *\*Note: Max 4096 samples can be selected for plotting frequency domain response due to limited buffer size in the firmware.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_iio_osc_freq_domain_plot.png
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data capture, sensor measurement, device calibration, etc. can be achieved with python based IIO clients, using 'pyadi-iio' library. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The python scripts are provided along with firmware package.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter

--------------

Sensor Demo Modes
~~~~~~~~~~~~~~~~~

AD4130 IIO firmware provides support for interfacing different sensors to analog inputs and perform the measurement on them. Below sensor demo modes are supported in the firmware.

-  User Default Config (All channels test)
-  2-wire/3-wire/4-wire RTD (Default is PT100)
-  Thermistor (Default is 10K NTC)
-  Thermocouple (Default is T type TC and PT1000 RTD as CJC)
-  Load Cell (4-wire bridge)
-  Noise Test (AIN0-AIN1 shorted)
-  ECG
-  Power Test (ADC internal channels voltage/current measurement)

<fc #ff0000>\ *\*Note: The selection of default sensor types can be changed from ‘ad4130_temperature_sensor.cpp’ file to large extent and from respective user config header files to some extent.*\ </fc>

Demo Mode Selection
-------------------

The sensor mode selection is done from “app_config.h” file using “ACTIVE_DEMO_MODE_CONFIG” macro. The selection is done at compilation time, that means only one sensor demo mode is active at a time. Whenever demo mode is changed from app_config.h file, the code must be compiled again to generate a new binary file for that.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_sensor_demo_selection.png
   :align: center
   :width: 600px

Demo Mode User Configuration
----------------------------

Firmware maintains the unique user configuration file for each sensor demo mode as per below table. The configurations can be updated by using .c and .h user config files.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_sensor_demo_configs.png
   :align: center
   :width: 600px

Sensor Measurement
------------------

Sensor measurement for RTD, Thermistor, Thermocouple, Noise Test, ECG, Power Test and User Default Config can be done using the IIO oscilloscope GUI client application or by executing python scripts from the ‘scripts’ folder. Temperature result for RTD, TC and Thermistor would be in degree Celsius. The result for other configs would in voltage/current.

Sensor measurement for Load Cell can be done by executing the python script available in the project “scripts” folder. IIO oscilloscope can only support measurement for voltage, current and temperature quantities and threfore python code is developed to support measurement for other sensor types.

The python script can be executed from ‘Visual Studio Code’ or any other preferred IDE/console prompt application using “python script_name.py” command as shown below. The demo config is fetched from the firmware by establishing serial (UART/VCOM) connection between host and MCU (sdp-k1). Refer next section to install necessary python tools and updating/executing the python scripts.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_sensor_demo_console.png
   :align: center
   :width: 600px

Sensor Channels Calibration
---------------------------

It is possible to calibrate the device channels which are connected to external sensors. The sensors calibration (gain and offset) is done by executing the python script “ad4130_calibration.py”.

--------------

AD4130 Firmware Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/ad4130_fw_structure.png
   :align: center
   :width: 400px

app_config.h
------------

-  Select the AD4130 device package (either LFCSP or WLCSP). Default is WLCSP. The corresponding hardware board must be used with software selected package type.
-  Select demo config mode (e.g. Thermistor, 2-wire RTD, etc).
-  Select data capture mode (Continuous, Burst, FIFO).
-  Select UART/VCOM (only for SDP-K1).

ad4130_user_config.c
--------------------

This file defines the user configurations for the AD4130, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD4130 device (e.g. required GPIOs, software/hardware mode, etc). These are the parameters loaded into device when device is powered-up or power-cycled.

ad4130_data_capture.c
---------------------

This file implements the data capturing logic for the AD4130 device. The data capturing can be done using normal ‘Sequencer’ Or using internal ‘FIFO’. Enable the macro ‘FIFO_ENABLED’ for enabling FIFO mode.

ad4130_iio.c
------------

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4130 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

No-OS Drivers for AD4130
------------------------

The no-os drivers provide the high level abstracted layer for digital interface of AD4130 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers. The functionality related with no-os drivers is covered in below 2 files:

-  ad413x.c
-  ad413x.h
