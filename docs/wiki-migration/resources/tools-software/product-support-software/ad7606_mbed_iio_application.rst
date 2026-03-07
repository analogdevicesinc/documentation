AD7606 IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware application with Analog Devices AD7606 Evaluation board(s) and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD7606 family devices by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :git-no-OS:`AD7606 No-OS drivers <drivers/adc/ad7606>`
-  :adi:`AD7606B <en/products/ad7606b.html>` AD7606C :adi:`AD7605-4 <en/products/ad7605-4.html>` :adi:`AD7606-4 <en/products/ad7606-4.html>` :adi:`AD7606-6 <en/products/ad7606-6.html>` :adi:`AD7606-8 <en/products/ad7606.html>` :adi:`AD7608 <en/products/ad7608.html>` :adi:`AD7609 <en/products/ad7609.html>`

--------------

Hardware Connections
--------------------

SDP-K1:
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD7606B-FMCZ:
~~~~~~~~~~~~~~~~~~

-  Make below jumper settings on the board. Refer :adi:`EVAL-AD7606B-FMCZ User Manual <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7606B-FMCZ.html#eb-overview>` for more details.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606b_jumper_settings.jpg
   :align: center
   :width: 450px

Arduino Connections:
~~~~~~~~~~~~~~~~~~~~

-


|image1|

The AD7606 device is configured in "Serial Software" mode in the firmware. AD7606 uses SPI communication for device register access and data capture.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

--------------

Evaluating AD7606 Using IIO Ecosystem
-------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD7606 device should pop-up in IIO devices list. Click 'Connect' and select the AD7606 device from the drop down menu list of 'Device Selection'.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_oscilloscope_connection.gif
   :align: center

Configure/Access Device Attributes (Parameters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes". There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters e.g. oversampling rate, operating mode
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters e.g. channel range, offset, calibration, open circuit detection, etc.

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, write a attribute value in the 'value field' and press 'Write' button. The value to be written corresponds to expected bit-field for that parameter, specified in the datasheet. For example, below figure shows how to write a "Oversampling" value.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_oscilloscope_attribute_rw.gif
   :align: center

Using DMM Tab to Read DC Voltage on Input Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button.

*\*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, it is not encouraged to use Data Capture or Debug tab as this could impact data capturing.*

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_oscilloscope_dmm_tab.gif
   :align: center

Data Capture from IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To capture the data from AD7606 IIO device, simply select the device and channels to read/capture data. The data is plotted as "ADC Raw Value" Vs "Number of Samples" and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

*\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing.*

More info here: :doc:`/wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app`

.. important::

   The continuous time domain data capture can work correctly at ODR/Sampling Rate defined in the firmware code (32KSPS) and also at 0 Oversampling Rate. For plotting frequency domain response max 4096 samples can be selected due to limited buffer size in the firmware. These limitations are due to the firmware architecture and design choices and does not limit the actual device specifications provided in device datasheet


Time Domain:



|image2|

Frequency Domain:


|image3|

--------------

Calibrating AD7606B/C Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADC Gain Calibration:
^^^^^^^^^^^^^^^^^^^^^

ADC gain calibration can be done in 3 easy steps as mentioned below. The gain calibration needs to be done for selected gain filter register as specified in the datasheet (refer 'System Gain Calibration' section from the AD7606B/C datasheet). The gain calibration can be done for each channel depending upon the filter resistor placed in series with each channel analog input.

**Reference: File: iio_ad7606.c, Function: get_chn_calibrate_adc_gain()**

|image4| |image5|

ADC Offset Calibration:
^^^^^^^^^^^^^^^^^^^^^^^

ADC offset calibration should only be done when ADC input is 0V. The purpose is to reduce any offset error from the input when analog input is at 0V level. The ADC offset calibration can be done for each input channel.

To perform ADC offset calibration, select the 'calibrate_adc_offset' attribute. It should automatically perform the calibration. Also, if 'Read' button is pressed, the calibration should happen one more time.

**Reference: File: iio_ad7606.c, Function: get_chn_calibrate_adc_offset()**

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_offset_calibration.jpg
   :align: center
   :width: 600px

--------------

Open Circuit Detection on AD7606B Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AD7606B device provides an open circuit detection feature for detecting the open circuit on each analog input channel of ADC.

There are 2 modes to detect open circuit on analog inputs (Refer AD7606B datasheet for more details):

-  Manual Mode
-  Auto Mode

Manual Mode Open Circuit Detect:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The manual open circuit detection needs 'Rpd' to be placed at analog input as shown in figure below. The firmware is written to perform the open circuit detection @50Kohm of Rpd value. The common mode change threshold has been defined as 15 ADC count in the firmware at above specified configurations (as specified in the datasheet).

**Reference: File: iio_ad7606.c, Function: get_chn_open_circuit_detect_manual()**

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_manual_open_circuit.jpg
   :align: center

Auto Mode Open Circuit Detect:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The auto open circuit detection on each individual ADC channel can be done by performing 3 easy steps mentioned in below screenshot.

**Reference: File: iio_ad7606.c, Function: get_chn_open_circuit_detect_auto()**

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_auto_open_circuit.jpg
   :align: center

--------------

Diagnostic Multiplexer on AD7606B/C Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using diagnostic multiplexer on AD7606B/C devices, the internal analog inputs can be sampled to provide a diagnostic voltages and parameters on IIO client application such as reference voltage (vref), DLO voltage (ALDO/DLDO), temperature and drive voltage (vdrive).

**\*Note: The diagnostic mux control must operate when input range is +/-10V**

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_diagnostic_mux.jpg
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data capture can be achieved with python based IIO clients, using 'pyadi-iio' library. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The python scripts are provided along with firmware package.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter

--------------

Modifying Firmware
------------------

The below block diagram shows the AD7606 IIO firmware layer.


|image6|

app_config.h
~~~~~~~~~~~~

This file can be used to:

-  Select the 'Active Device' to evaluate by changing '#define DEV_AD7606B' macro. Default active device is AD7606B.
-  Configure the pin mapping of AD7606 w.r.t Arduino Header on Controller Board.

ad7606_user_config.c
~~~~~~~~~~~~~~~~~~~~

This file defines the user configurations for the AD7606, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD7606 device (e.g. required GPIOs, software/hardware mode, etc). These are the parameters loaded into device when device is powered-up or power-cycled.

iio_ad7606.c
~~~~~~~~~~~~

This file defines getter/setter functions for all the device and channel specific attributes (related to AD7606 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

iio_ad7606_data_capture.c
~~~~~~~~~~~~~~~~~~~~~~~~~

This file defines the data capture implementation of AD7606 for visualizing adc raw data on IIO oscilloscope.

No-OS Drivers for AD7606
~~~~~~~~~~~~~~~~~~~~~~~~

The no-os drivers provide the high level abstracted layer for digital interface of AD7606 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers.

The functionality related with no-os drivers is covered in below 2 files:

-  ad7606.c
-  ad7606.h

.. tip::

   It is hoped that the most common functions of the AD7606 family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_connection_diagram.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_oscilloscope_data_capture.gif
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_oscilloscope_data_capture_freq_domain.gif
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_gain_calibration_ckt.jpg
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_gain_calibration.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7606_iio_firmware_layer.jpg
   :width: 600px
