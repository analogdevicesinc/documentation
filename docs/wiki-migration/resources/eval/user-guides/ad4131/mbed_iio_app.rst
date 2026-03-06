Mbed IIO Application
====================

Introduction
------------

This page gives an overview of using the ARM Mbed platform supported firmware example with Analog Devices AD4131 Evaluation board and SDP-K1 controller board. This example code leverages the ADI developed IIO (Industrial Input Output) ecosystem to evaluate the AD4131 device by providing a device debug and data capture support. The overview of an entire system is shown below: |image1| IIO oscilloscope is used as client application running on windows-os, which is ADI developed GUI for ADC data visualization and device debug. The interface used for communicating client application with firmware application (IIO device) is UART. The firmware application communicates with IIO device (AD4131) using ADI No-OS drivers and platform drivers low level software layers. SDP-K1 is used as controller board, on which IIO firmware application runs and using above software libraries, the IIO firmware communicates with AD4131 IIO device. The AD4131 eval board is used for development and testing of this application.

Useful links
~~~~~~~~~~~~

-  `Mbed Online Compiler <https://ide.mbed.com/compiler/#nav:/;>`__
-  `SDP-K1 on Mbed <https://os.mbed.com/platforms/SDP_K1/>`__

Hardware Connections
--------------------

Jumper Settings
~~~~~~~~~~~~~~~

-  SDP-K1:
   Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V
-  EVAL-AD4131:

|image2|

Hardware Interface
~~~~~~~~~~~~~~~~~~

|image3| AD4131 uses SPI communication for device register access and data capture. SDP-K1 is powered through USB connection from the computer. SDP-K1 acts as a Serial device when connected to PC, which creates a COM Port to connect to IIO Oscilloscope GUI running on windows-os. The COM port assigned to a device can be seen through the device manager for windows based OS. |image4|

Software Downloads
------------------

Firmware
~~~~~~~~

Quick Start to Use Mbed IIO Firmware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have some familiarity with the Mbed platform, the following is a basic list of steps required to start running the code, see below for more detail:

-  Connect the AD4131 EVAL-board to the SDP-K1 controller board as specified in hardware connections section.
-  Connect the SDP-K1 controller board to your computer over USB provided along with SDP-K1 board.
-  Go to the link of the code provided above in the 'Downloads' section and import code into `Mbed Online Compiler <https://ide.mbed.com/compiler/#nav:/;>`__.

|image5|

-  Ensure SDP-K1 controller board is selected (top right of online-compiler page). (SDP-K1 platform pre-installed from `here <https://os.mbed.com/platforms/SDP_K1/>`__.
-  The original firmware program may require few configurations to suits the REV E board.

   -  Open the **app** folder and open the file **app_config.h**.
   -  Comment line 31 and uncomment line 32 to select WLCSP package type for AD4131.
   -  Go to line 49 and line 54, change source pin **D3** to **D2**.
   -  Go to line 51 to change SDP-120 source pin from **SDP_GPIO_1** to **SDP_GPIN_5**.

   |image6|

-  Compile the code.
-  After a successful compile a binary will be downloaded to your computer - store this on your drive.
-  Drag and drop this binary to the USB drive hosted by your controller board.

\*Note: For more details on importing code into Mbed online compiler, refer below link (Section: Importing from local machine): `here <https://os.mbed.com/handbook/Importing-code>`__.

Libiio: IIO Library
~~~~~~~~~~~~~~~~~~~

This library provides an abstracted library interface to communicate IIO device (AD4131) and IIO client application (IIO Oscilloscope) without worrying about the low level hardware details. Download and install below :doc:`libiio </wiki-migration/resources/tools-software/linux-software/libiio>` windows installer in your computer. Libiio installer for Windows (Use below link):

-  :git-libiio:`libiio windows installer (.exe) <releases>`

IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a GUI (Graphical User Interface) based IIO client application for data visualization and device configuration/debugging. The data from IIO devices (ADCs/DACs) is transmitted over Serial/Ethernet/USB link to IIO Oscilloscope client through the abstracted layer of “\ `libiio <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscopelibiio>`__\ ”. Download and install below IIO Oscilloscope windows installer in your computer. IIO Oscilloscope installer for Windows (Use below link):

-  :git-iio-oscilloscope:`IIO Oscilloscope windows installer (.exe) <releases>`

Evaluating AD4131 Using IIO Ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that hardware connection has been made properly in between Controller Board (SDP-K1) and AD4131 Eval board. Also ensure all software's (IIO firmware, Libiio windows installer and IIO Oscilloscope windows installer) are downloaded and installed in your computer before trying to communicate with AD4131 device.

Running IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the IIO Oscilloscope application from start menu and configure the serial (UART) settings as shown below. Click on refresh button and AD4131 device should pop-up in IIO devices list.


|image7|

Click 'Connect' and select the AD4131 device from the drop down menu list of 'Device Selection'. It should display below screen after selecting available device.

Configure/Access Device Attributes (Parameters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows user to access and configure different device parameters, called as 'Device Attributes“. There are 2 types of attributes:

-  Device Attributes (Global): Access/Configure common device parameters e.g. Vbias
-  Channel Attributes (Specific to channels): Access/Configure channel specific device parameters e.g. PGA, filter FS, setup, etc

How to read and write attribute:

-  To 'Read' an attribute, simply select the attribute from a list or press 'Read' button on left side.
-  To 'Write' an attribute, write attribute value in the 'value field' and press 'Write' button. The value to be written corresponds to expected bit-field for that parameter, specified in the datasheet.
-  Sample configuration:

   -  filter_FS write to 1.


   |image8|

Using DMM Tab to Read DC Voltage on Input Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DMM tab can be used read the instantaneous voltage applied on analog input channels. Simply select the device and channels to read and press start button. \*Note: The voltage is just instantaneous, so it is not possible to get RMS AC voltage or averaged DC voltage. Also, when using DMM tab, do not access/use the Data Capture or Debug tab as this could impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation.


|image9|

Data Capture from IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To capture the data from AD4131 IIO device, simply select the device and channels to read/capture data. The data is plotted as “ADC Raw Value” Vs “Number of Samples” and is just used for Visualization. The data is read as is from device without any processing. If user wants to process the data, it must be done externally by capturing data from the Serial link on controller board. \*Note: The DMM or Debug tab should not be accessed when capturing data as this would impact data capturing. Both DMM scan and data capture uses different methods of conversion. The DMM data is read using single conversion, while data capture uses continuous conversion mode of operation. More info `here <https://wiki.analog.com/resources/tools-software/product-support-software/data capture-using-iio-app>`__. Data capturing utilizes two modes:

-  Normal sequencer: In this mode, the channel for which data to be captured are enabled and automatically added into a sequencer. The sequencer operates in the continuous conversion mode. After each conversion, an interrupt signal attached to configured INT source is triggered and conversion result is read into a internal acquisition buffer.
-  FIFO mode: This mode uses the internal FIFO of device to store the ADC samples. The conversion happens in continuous conversion mode and an interrupt signal attached to configured INT source is triggered when internal FIFO becomes full (reached to watermark limit). The data from FIFO is read periodically when FIFO is made available by device. The FIFO is operated in ‘Oldest Save’ mode as there must be sufficient time provided to read the FIFO after it becomes full. If FIFO is operated into streaming mode, the previous data could get overwritten before it is being acquired by the firmware.

|image10|

Access Register map of IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_132152.png
   :align: center
   :width: 400px

AD4131 Firmware Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

app_config.h
^^^^^^^^^^^^

This file can be used to:

-  Select the AD4131 and SDP-K1 interface (Default is SDP-120, but it can be changed to Arduino by enabling ‘ARDUINO’ macro.
-  Select the AD4131 device package (either LFCSP or WLCSP). Default is LFCSP. The corresponding hardware board must be used with software selected package type.
-  Configure the pin mapping w.r.t SDP-120 or Arduino interface.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_132328.png
   :align: center
   :width: 500px

ad4130_user_config.c
^^^^^^^^^^^^^^^^^^^^

This file defines the user configurations for the AD4131, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD4131 device (e.g. required GPIOs, software/hardware mode, etc). These are the parameters loaded into device when device is powered-up or power-cycled.

.. _ad4130_user_config.c-1:

ad4130_user_config.c
^^^^^^^^^^^^^^^^^^^^

This file implements the data capturing logic for the AD4131 device. The data capturing can be done using normal ‘Sequencer’ Or using internal ‘FIFO’. Enable the macro ‘FIFO_ENABLED’ for enabling FIFO mode.

iio_ad4130.c
^^^^^^^^^^^^

This file defines getter/setter functions for all the device and channel specific attributes (related to AD4131 devices) to read/write the device parameters. The majority of device specific functionality is present in this module.

No-OS Drivers for AD4131
~~~~~~~~~~~~~~~~~~~~~~~~

The no-os drivers provide the high level abstracted layer for digital interface of AD4131 devices. The complete digital interface (to access memory map and perform data read) is done in integration with platform drivers. The functionality related with no-os drivers is covered in below 2 files:

-  ad7124.c
-  ad7124.h

\*The AD7124 legacy no-os drivers are used for evaluating the part; however, the drivers are updated to support the memory map and device APIs for accessing AD4131 device.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-15_161906.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-15_162938.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-15_163209.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-15_164837.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-16_103924.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_124239.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-16_131004.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_131350.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_131757.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-04-19_132042.png
   :width: 600px
