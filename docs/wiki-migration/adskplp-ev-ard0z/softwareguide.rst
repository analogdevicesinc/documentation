ADSKPLP-EV-ARD0Z Software Guide
===============================

Introduction
------------

This page gives an overview of using the ARM Mbed platform supported firmware example with Analog Devices ADSKPLP01-EV-ARDZ Evaluation board and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the ECO0001 signal chain by providing a device debug and data capture support.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/iio_app_block.png
   :align: center
   :width: 600px

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :git-no-OS:`ad4696 No-OS drivers <drivers/adc/ad469x>`
-  :adi:`AD4696 <en/products/ad4696.html>`
-  :adi:`MAX7320 <en/products/max7320.html>`

Hardware Connections
--------------------

SDP-K1:
~~~~~~~

-  Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V

Arduino Connections
~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/arduino_interface.png
   :align: center
   :width: 800px

ADSKPLP01-EV-ARDZ uses SPI communication for device register access and data capture. For data transmission to IIO client, VirtualCOM or UART serial communication is used. SDP-K1 by default uses the VCOM serial interface for higher speed data transmission. The other port is used for printing log or debug messages from the firmware.

SDP-K1 is powered through USB connections from the computer. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to IIO Oscilloscope GUI running on Windows-OS. The COM port assigned to a device can be seen through the device manager for windows-based OS.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/port_device_manager.png
   :align: center
   :width: 400px

SDP-K1 can support high speed VirtualCOM port USB interface, so by default VCOM is configured as default interface for data transmission the firmware and UART is configure for printing debug messages on console. The data transmission port can be set to UART by assigning “USE_PHY_UART_PORT” to the “DATA_TRANSFER_PORT” macro in the app_config.h file.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/port_vcom.png
   :align: center
   :width: 600px

Software Downloads
------------------

Quick Start to use Mbed IIO Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail:

-  Connect the ADSKPLP01-EV-ARDZ EVAL-board to the SDP-K1 controller board as specified in hardware connections section.
-  Connect the SDP-K1 controller board to your computer over USB provided along with SDP-K1 board.

Using Keil Studio
^^^^^^^^^^^^^^^^^

-  Clone the `plp0001_iio-application <https://analog.sharepoint.com/:f:/r/sites/PTP_Collaboration/Shared%20Documents/Signal%20chain%20HW%20standardization/SW/ECO_eval_plus_API/ECO_0001_Code/API_with_code_examples?csf=1&web=1&e=bWXAoV>`__ repository on to Analog Devices onto your local machine.
-  Import the code into `Keil Studio IDE <https://studio.keil.arm.com/>`__ (web compiler) by drag and drop this folder into web IDE. This shall create a new project with same name as folder name onto web IDE.
-  Right click on the project name and select ‘Set Active Project’ option.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/keil_set_active_project.png
   :align: center
   :width: 600px

-  Fix libraries import issues by selecting ‘Mbed Libraries’ tab at the bottom side of IDE and then clicking on the ‘Fix all problems’ option. Allow some time to check out all library dependency.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/keil_fix_libraries.png
   :align: center
   :width: 600px

-  Compile the code as shown below

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/keil_compile.png
   :align: center
   :width: 400px

Libiio: IIO Library
^^^^^^^^^^^^^^^^^^^

This library provides an abstracted library interface to communicate IIO device and IIO client application (IIO Oscilloscope) without worrying about the low level hardware details. Download and install below :doc:`Libiio </wiki-migration/resources/tools-software/linux-software/libiio>` windows installer in your computer.

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
   


.. important::

   The current application supports IIO oscilloscope versions up to 0.14


--------------

Evaluating ADSKPLP01-EV-ARDZ Using IIO Ecosystem
------------------------------------------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/note_hardware_connections#Note in Hardware Connections&showfooter=nofooter

Running IIO Oscilloscope (Client)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD4696 device should pop-up in IIO devices list.

|image1| Click 'Connect' and it should by default open the data ‘Capture’ window. You can drag aside or close this window to see the main ‘Debug and DMM’ tab window.

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/iio_datacapture_debug_tab.png
   :align: center
   :width: 800px

Configure/Access Device Attributes (Parameters)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes”. There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters.
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters.

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, select attribute value in the 'value field' and press 'Write' button.

.. note::

   Note: IIO firmware expose only few (important) attributes and there is no option to modify (write) them. They are listed below: 1) “raw” – ADC raw value corresponding to selected channel. 2) “scale” – This attribute is used to convert ADC raw value into ‘voltage’ in DMM tab. 3) "offset" - This attribute is used to convert ADC raw value into ‘voltage’ in DMM tab.


Using DMM Tab to Read DC Voltage on Input Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button.

//\*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, it is not encouraged to use Data Capture or Debug tab as this could impact data capturing. //

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/iio_dmm_tab.png
   :align: center
   :width: 600px

Data Capture from IIO Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To capture the data from ad4696 IIO device, simply select the device and channels to read/capture data. The data is plotted as "ADC Raw Value" Vs "Number of Samples" and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board.

*\*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing.*

More info here: :doc:`/wiki-migration/resources/tools-software/product-support-software/data-capture-using-iio-app`

.. important::

   For plotting frequency domain response max 4096 samples can be selected due to limited buffer size in the firmware. These limitations are due to the firmware architecture and design choices and does not limit the actual device specifications provided in device datasheet


Time Domain
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/time_domain.png
   :align: center
   :width: 600px

Frequency Domain
~~~~~~~~~~~~~~~~

Firmware Structure
------------------

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/firmware_structure.png
   :align: center
   :width: 800px

Embedded Development using the EVAL APIs
----------------------------------------

.. _introduction-1:

Introduction
^^^^^^^^^^^^

This section gives an overview of using the ARM Mbed platform supported code examples and APIs with Analog Devices ADSKPLP01-EV-ARDZ Evaluation board and SDP-K1 controller board. These example codes leverage the ECO-APIs developed using the No-OS drivers to enable prototyping solutions for the ECO0001 signal chain and facilitate embedded development.


|image2|

Software Download
^^^^^^^^^^^^^^^^^

-  Clone the `plp0001_api <https://analog.sharepoint.com/:f:/r/sites/PTP_Collaboration/Shared%20Documents/Signal%20chain%20HW%20standardization/SW/ECO_eval_plus_API/ECO_0001_Code/API_with_code_examples?csf=1&web=1&e=s1bX1b>`__ repository on to Analog Devices onto your local machine.
-  Follow the steps as mentioned above in the IIO Application section.

Application Structure
^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/application_structure_apis.png
   :align: center
   :width: 600px

app_config.c
~~~~~~~~~~~~

This file defines the user configurations for the ADSKPLP01-EV-ARDZ, such as init parameters for driver initializations, data transfer port.

app_config_mbed.c
~~~~~~~~~~~~~~~~~

This file contains the mbed layer specific init parameters, pin mapping.

ECOevp_API_code_examples.c
~~~~~~~~~~~~~~~~~~~~~~~~~~

This file contains the code examples that facilitate the use of the underlying APIs for device configuration and data capture.

eco0001_api.c
~~~~~~~~~~~~~

This file acts as an abstraction layer that contains various API functions using the No-OS drivers to enable a simple means of prototyping and embedded development.

database.h
~~~~~~~~~~

This file contains the database for the current differential pressure expansion board. Any data on other expansion boards planned in future can be included here.

API Functions
^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/api_functions.png
   :align: center
   :width: 600px

.. |image1| image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/running_the_iio_client.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/adskplp-ev-ard0z/interface_overview.png
   :width: 600px
