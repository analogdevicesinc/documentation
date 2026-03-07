AD4696 IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM Mbed platform supported firmware example with Analog Devices AD4696 Evaluation board(s) and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD4696 family devices by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_introduction#Introduction&showfooter=nofooter

--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :git-no-OS:`ad4696 No-OS drivers <drivers/adc/ad469x>`
-  :adi:`AD4696 <en/products/ad4696.html>` :adi:`AD4695 <en/products/ad4695.html>`

--------------

Hardware Connections
--------------------

Power Connections:
~~~~~~~~~~~~~~~~~~

-  Connect a 12V (1A max) DC power supply to board through VPWR and GND4 pin.
-  Connect the VCC_HOST pin of the AD4696 to the 3.3V supply.

.. note::

   Note: Make sure to connect the 12V DC power supply to VPWR before supplying 3.3v to the VCC_HOST pin to adhere to the power-supply-sequence requirement


SDP-K1:
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 1.8V position to drive SDP-K1 GPIOs at 1.8V

EVAL-AD4696-FMCZ:
~~~~~~~~~~~~~~~~~

-  Make below jumper settings on the board. Refer :adi:`EVAL-AD4696-FMCZ User Manual <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4696.html#eb-overview>` for more details.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_jumper_connection.jpg
   :align: center

Arduino Connections:
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_connection_diagram.jpg
   :align: center

.. note::

   Note: To achieve reliable high speed data transfer between the SDP-K1 and AD4696 Eval board, make sure to use good quality jumper wires with length not more than 10cm


The SDP-K1 generates PWM signals to manually trigger conversion on the AD4696. The digital pin and the sampling rate for PWM signal can be configured in the app_config_mbed.h file. By default, it is generated at 62.5 KSPS on D6 Arduino pin. The D6 (CNV) Arduino pin is used to generate trigger signals and the falling edge on the BSY pin triggers SPI read transaction to sampled data.

The firmware supports both unipolar and pseudo bipolar modes. By default, the firmware is configured in unipolar mode. To switch to pseudo bipolar mode, by defining "PSEUDO_BIPOLAR_MODE" macro in app_config.h file. Make sure to change the JP6 jumper to position A on the Eval board to use the PSEUDO_BIPOLAR_MODE. Since the pin pairing option is same for all the channels in standard sequencer mode, therefore polarity mode for all the channels is also kept same to avoid stale ADC output codes.

The AD4696 device is configured in "Serial Software" mode in the firmware. AD4696 uses SPI communication for device register access and data capture.

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/hardware_connections_uart#UART Connections&showfooter=nofooter

Software Downloads
------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/iio_support_software_downloads#Software Downloads&showfooter=nofooter

Evaluating AD4696 Using IIO Ecosystem
-------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD4696 device should pop-up in IIO devices list. Click 'Connect' and select the AD4696 device from the drop-down menu list of 'Device Selection'.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_connection.gif
   :align: center

Configure/Access Device Attributes (Parameters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes”. There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters.
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters.

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, select attribute value in the 'value field' and press 'Write' button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_attributes.jpg
   :align: center
   :width: 600px

.. note::

   Note: AD4696 IIO firmware expose only few (important) attributes and there is no option to modify (write) them. They are listed below: 1) “sampling-rate” – Defines the actual sampling rate (ODR) used in the firmware for data capturing. 2) “raw” – ADC raw value corresponding to selected channel. 3) “scale” – This attribute is used to convert ADC raw value into ‘voltage’ in DMM tab.


.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_oscilloscope_attribute_rw.gif
   :align: center

Using DMM Tab to Read DC Voltage on Input Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button.

//\*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, it is not encouraged to use Data Capture or Debug tab as this could impact data capturing. //

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_dmm_tab.gif
   :align: center

Data Capture from IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To capture the data from ad4696 IIO device, simply select the device and channels to read/capture data. The data is plotted as "ADC Raw Value" Vs "Number of Samples" and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

*\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing.*

More info here: :doc:`/wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app`

.. important::

   The continuous time domain data capture can work correctly at ODR/Sampling Rate defined in the firmware code (32KSPS) and also at 0 Oversampling Rate. For plotting frequency domain response max 4096 samples can be selected due to limited buffer size in the firmware. These limitations are due to the firmware architecture and design choices and does not limit the actual device specifications provided in device datasheet


Time Domain
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_data_capture.gif
   :align: center

Frequency Domain
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_iio_frequency.gif
   :align: center

Modifying Firmware
------------------

The below block diagram shows the ad4696 IIO firmware layer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad4696_firmware_structure.jpg
   :align: center

app_config.h
~~~~~~~~~~~~

This file can be used to:

-  Select the active platform using macro “ACTIVE_PLATFORM_MBED” (Only Mbed is supported)
-  Select between physical or virtual COM Port using "USE_VIRTUAL_COM_PORT" macro. Default is physical UART interface
-  Select between polarity mode of AD4696 (unipolar/pseudo bipolar) using "PSEUDO_BIPOLAR_MODE". Default is unipolar mode.
-  Select the 'Active Device' to evaluate by changing '#define DEV_AD4696' macro. Default active device is AD4696.

app_config_mbed.h
~~~~~~~~~~~~~~~~~

This file can be used to:

-  Select Mbed compatible board pin mapping w.r.t. Arduino connector (e.g. SDP-K1).
-  Define the possible sampling rate (ODR). Should never exceed than the default ODR selected using macro “SAMPLING_RATE” as this could impact data capture with device.

ad4696_user_config.c
~~~~~~~~~~~~~~~~~~~~

These files define the user configurations for the AD4696, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD4696 device (active device, data format, etc). These are the parameters loaded into device when device is powered-up or power-cycled.

ad4696_data_capture.c
~~~~~~~~~~~~~~~~~~~~~

This file implements the data capturing logic for the AD4696 device. The adc_data_capture.c module present in platform drivers acts as an abstracted layer for common IIO application data capturing.

iio_ad4696.c
~~~~~~~~~~~~

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4696 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

No-OS Drivers for AD4696
~~~~~~~~~~~~~~~~~~~~~~~~

The no-os drivers provide the high-level abstracted layer for digital interface of AD4696 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers. The functionality related with no-os drivers is covered in below 2 files: 1. ad469x.c 2. ad469x.h The drivers are can use SPI engine framework or Standard SPI framework to communicate with the board. By default, the drivers use the Standard SPI framework. The SPI engine framework can be enabled defining the “ENABLE_SPI_ENGINE” macro in the ad469x.h file.

.. tip::

   It is hoped that the most common functions of the AD4696 family are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.

