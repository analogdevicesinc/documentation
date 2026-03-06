AD717x IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware application with Analog Devices AD717x/AD411x Evaluation board(s) and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD717x/AD411x family devices by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  `no-OS Drivers for AD717x-AD411x Family <https://github.com/analogdevicesinc/​no-OS>`__
-  :adi:`AD4111 <​en/​products/​ad4111.html>` :adi:`AD4112 <​en/​products/​ad4112.html>` :adi:`AD4114 <​en/​products/​ad4114.html>` :adi:`AD4115 <​en/​products/​ad4115.html>` :adi:`AD4116 <​en/​products/​ad4116.html>`
-  :adi:`AD7172-2 <​en/​products/​ad7172-2.html>` :adi:`AD7172-4 <​en/​products/​ad47172-4.html>`
-  :adi:`AD7173-8 <​en/​products/​ad7173-8.html>` :adi:`AD7175-2 <​en/​products/​ad7175-2.html>` :adi:`AD7175-8 <​en/​products/​ad7175-8.html>`
-  :adi:`AD7176-2 <​en/​products/​ad7176-2.html>`
-  :adi:`AD7177-2 <​en/​products/​ad7177-2.html>`

Hardware Connections
--------------------

SDP-K1:
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

EVAL-AD717x:
~~~~~~~~~~~~

-  Please refer to the :adi:`EVAL-AD4111SDZ User Manual <media/en/technical-documentation/user-guides/EVAL-AD4111SDZ-UG-1124.pdf>`

Please refer to the respective board user guide on the product page of the chosen device.

NOTE: In order to capture signals from the AD717x/AD411x board using continuous data capturing, there needs to be an external connection from the MISO pin on the board to the D8 of the arduino header. Example- in case of the AD4111, the J10-3 needs to be connected to D8 on the SDP-K1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_hardware_interface.png
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

Evaluating AD717x Using IIO Ecosystem
=====================================

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
---------------------------------

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD717x device should pop-up in IIO devices list.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_running_iio_oscilloscope.png
   :align: center
   :width: 600px

Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_iio_osc_windows.png
   :align: center
   :width: 600px

Select the device from ‘Device’ pop-up list on ‘Debug’ tab window. This will make available all device specific and channel specific attributes.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_iio_dev_selection.png
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

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_using_dmm_tab.png
   :align: center
   :width: 600px

Data Capture from IIO Device
----------------------------

To capture the data from AD717x IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

<fc #ff0000>\ *\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.*\ </fc>

More info here: :doc:`Data Capture using IIO App </wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app>`

-  Time Domain Plot

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_time_domain_plot.png
   :align: center
   :width: 800px

-  Frequency Domain Plot

<fc #ff0000>\ *\*Note: Max 4096 samples can be selected for plotting frequency domain response due to limited buffer size in the firmware.*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_freq_domain_plot.png
   :align: center
   :width: 600px

Access Register map of IIO Device
---------------------------------

This tab is used to access the device registers in byte mode.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_access_reg_map.png
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
------------------------------

Data capture can be achieved with clients other than the IIO Oscilloscope as well. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The *ad717x_data_capture.py* is capable of achieving the same.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter

--------------

AD717x Firmware Structure
=========================

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_firmware_structure.png
   :align: center
   :width: 600px

app_config.h
^^^^^^^^^^^^

This file can be used to:

-  Select the 'Active Device' to evaluate by changing '#define DEV_AD4111' macro. Default active device is AD4111.
-  Configure the pin mapping of AD4111 w.r.t SDP-120 Header on Controller Board.

ad717x_user_config.c
^^^^^^^^^^^^^^^^^^^^

This file defines the user configurations for the AD4111, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD4111 device (e.g. required GPIOs, software/hardware mode, etc). These are the parameters loaded into device when device is powered-up or power-cycled.

iio_ad717x.c
^^^^^^^^^^^^

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4111 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

iio_ad717x_data_capture.c
^^^^^^^^^^^^^^^^^^^^^^^^^

This file defines the data capture implementation of AD4111 for visualizing adc raw data on IIO oscilloscope.

No-OS Drivers for AD4111
^^^^^^^^^^^^^^^^^^^^^^^^

The no-os drivers provide the high level abstracted layer for digital interface of AD4111 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers.

The functionality related with no-os drivers is covered in below 2 files:

-  ad717x.c
-  ad717x.c
-  ad411x_regs.h
-  ad7172_2_regs.h
-  ad7172_4_regs.h
-  ad7713_8_regs.h
-  ad7175_2_regs.h
-  ad7175_8_regs.h
-  ad7176_2_regs.h
-  ad7177_2_regs.h

.. tip::

   It is hoped that the most common functions of the AD4111 family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.

