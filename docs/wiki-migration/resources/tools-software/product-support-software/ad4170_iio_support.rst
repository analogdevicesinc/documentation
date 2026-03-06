AD4170 IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM platforms supported (default is Mbed) firmware application with Analog Devices AD417x, AD4190 Evaluation board(s) and SDP-K1/Nucleo-L552ZEQ controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD417x, AD4190 family of devices by providing a device debug and data capture support. The code provides support to MBED and STM32 platforms.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/block_diagram.png
   :align: center
   :width: 600px

IIO oscilloscope is used as client application running on Windows-os, which is ADI developed GUI for ADC data visualization and device debug. The interface used for communicating client application with firmware application (IIO device) is UART (Note: SDP-K1 can also support high speed VirtualCOM port @1Mbps or higher speed for faster data transmission). The firmware application communicates with IIO device using ADI No-OS drivers and platform drivers low level software layers. SDP-K1 for MBED and Nucleo-L552ZEQ is used as controller board, on which IIO firmware application runs and using above software libraries, the IIO firmware communicates with IIO device.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/mbed_and_stm32_support_board_message#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/mbed_and_stm32_support_board_message#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :adi:`AD4170 <​en/​products/​ad4170.html>`
-  :adi:`AD4171 <​en/​products/​ad4171.html>`
-  :adi:`AD4172 <​en/​products/​ad4172.html>`
-  :adi:`AD4190 <​en/​products/​ad4190.html>`

Hardware Connections
--------------------

SDP-K1 for mbed platform:
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

Nucleo L552ZEQ for STM32 platform:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The Nucleo L552ZEQ board has been used to develop and test the STM32 firmware.Please refer to the board user guide `Nucleo-L552ZEQ User Manual <https://www.st.com/content/ccc/resource/technical/document/user_manual/group1/ad/a4/bd/5e/14/15/4e/e8/DM00615305/files/DM00615305.pdf/jcr:content/translations/en.DM00615305.pdf>`__

EVAL-AD417x and EVAL-AD4190:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Please refer to the respective board user guide on the product page of the chosen device.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

--------------

Software Downloads
------------------

MBED and STM32 Firmware
^^^^^^^^^^^^^^^^^^^^^^^

This section briefs on the usage of MBED and STM32 firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   
   Build Guide for Precision Converters STM32 firmware (Use below link):
   
   -  :doc:`Precision Converters STM32 Firmware Build Guide </wiki-migration/resources/tools-software/product-support-software/pcg-fw-stm32-build-guide>`
   


.. image:: https://wiki.analog.com/_media/section>/resources/tools-software/product-support-software/lib_iio_download#Getting Started&showfooter=nofooter
   :alt: section>/resources/tools-software/product-support-software/lib_iio_download#Getting Started&showfooter=nofooter

.. image:: https://wiki.analog.com/_media/section>/resources/tools-software/product-support-software/iio_osc_download#Getting Started&showfooter=nofooter
   :alt: section>/resources/tools-software/product-support-software/iio_osc_download#Getting Started&showfooter=nofooter

Evaluating AD417x/AD4190 Using IIO Ecosystem
============================================

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
---------------------------------

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD417x device should pop-up in IIO devices list.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_connect_option.png
   :align: center
   :width: 800px

Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_debug_and_dc_window.png
   :align: center
   :width: 600px

Select the device from ‘Device’ pop-up list on ‘Debug’ tab window. This will make available all device specific and channel specific attributes.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_debug_window.png
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

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_dmm_tab.png
   :align: center
   :width: 600px

Data Capture from IIO Device
----------------------------

To capture the data from AD4170 IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

.. warning::

   The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.More info here: :doc:`Data Capture using IIO App </wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app>`


-  Time Domain Plot

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_data_capture.png
   :align: center
   :width: 800px

Access Register map of IIO Device
---------------------------------

This tab is used to access the device registers in byte mode.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_register_read.png
   :align: center
   :width: 600px

--------------

Python Environment and Scripts
------------------------------

Data capture can be achieved with clients other than the IIO Oscilloscope as well. A possible option using ADI's pyadi-iio library in python has been demonstrated in the forthcoming sections. The *ad4170_data_capture.py* is capable of achieving the same.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_python_application#Python Application&showfooter=nofooter

--------------

AD4170 Firmware Structure
=========================

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4170_fw_structure.png
   :align: center
   :width: 600px

app_config.h
^^^^^^^^^^^^

This file can be used to:

-  Select the 'Active Device' to evaluate by changing '#define DEV_AD4170' macro. Default active device is AD4170.
-  Select the platform in which the firmware needs to be used. MBED and STM32 platforms are supported now. Select the active platform by modifying the '#define ACTIVE_PLATFORM' to 'MBED_PLATFORM' or 'STM32_PLATFORM' depending on the requirement.
-  Select the DATA_CAPTURE_MODE to set the data capturing to CONTINUOUS_DATA_CAPTURE or BURST_DATA_CAPTURE
-  Switch between two modes- SPI_MODE and TDM_MODE which can be chosen accordingly via the INTERFACE_MODE macro.
-  Select the preferred demo mode - ACTIVE_DEMO_MODE_CONFIG macro can be modified according to the intended mode of operation. The default mode is voltage mode, which is configured as USER_DEFAULT_CONFIG. The other configurations are- RTD_2WIRE_CONFIG, RTD_3WIRE_CONFIG, RTD_4WIRE_CONFIG, THERMISTOR_CONFIG, THERMOCOUPLE_CONFIG, ACCELEROMETER_CONFIG, LOADCELL_CONFIG.

.. important::

   Note that the maximum Output Data Rate of the device can be leveraged by selecting the TDM_MODE in the STM32 platform. There is a limit in the maximum achievable ODR while in SPI_MODE.


ad4170_user_config.c
^^^^^^^^^^^^^^^^^^^^

This file defines the user configurations for the Ad4170 in voltage mode, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD4170 device (e.g. required GPIOs, software/hardware mode, etc). These are the parameters loaded into device when device is powered-up or power-cycled. The part supports single ended/ differential mode. Default configuration in the FW is differential mode. It can be changed to single-ended by commenting the #define DIFFERENTIAL_CHN_CFG macro in the ad4170_user_config.h

ad4170_accelerometer_config.c
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This file defines the configurations for using the accelerometer configuration when the ACTIVE_DEMO_MODE_CONFIG is set as ACCELEROMETER_CONFIG

ad4170_loadcell_config.c
^^^^^^^^^^^^^^^^^^^^^^^^

This file defines the configurations for using the loadcell configuration when the ACTIVE_DEMO_MODE_CONFIG is set as LOADCELL_CONFIG

ad4170_rtd_config.c
^^^^^^^^^^^^^^^^^^^

This file defines the configurations for using the RTD configuration when the ACTIVE_DEMO_MODE_CONFIG is set as RTD_2WIRE_CONFIG/ RTD_3WIRE_CONFIG/ RTD_4WIRE_CONFIG.

ad4170_thermistor_config.c
^^^^^^^^^^^^^^^^^^^^^^^^^^

This file defines the configurations for using the loadcell configuration when the ACTIVE_DEMO_MODE_CONFIG is set as THERMISTOR_CONFIG

ad4170_thermocouple_config.c
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This file defines the configurations for using the loadcell configuration when the ACTIVE_DEMO_MODE_CONFIG is set as THERMOCOUPLE_CONFIG

ad4170_iio.c
^^^^^^^^^^^^

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4170 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

ad4170_support.c
^^^^^^^^^^^^^^^^

This file contains all the support functions utilized in the firmware

app_config_mbed.c
^^^^^^^^^^^^^^^^^

This file contains all the extra parameters specific to mbed platform

app_config_stm32.c
^^^^^^^^^^^^^^^^^^

This file contains all the extra parameters specific to STM32 platform. There might be a need to change certain parameters if any board other than the Nucleo-L552ZEQ is chosen.

No-OS Drivers for AD4170
^^^^^^^^^^^^^^^^^^^^^^^^

The no-os drivers provide the high level abstracted layer for digital interface of AD4170 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers.

The functionality related with no-os drivers is covered in below 2 files:

-  ad4170.c
-  ad4170.h

.. tip::

   It is hoped that the most common functions of the AD4170 family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.

