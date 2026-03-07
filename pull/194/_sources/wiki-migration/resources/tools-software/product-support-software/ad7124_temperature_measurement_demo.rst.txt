AD7124 Temperature Measurement Demo Example
===========================================

This page gives an overview of using the 'ARM Mbed' platform supported temperature measurement firmware example with Analog Devices AD7124 Evaluation board and SDP-K1 controller board (or any other Mbed supported target board). The firmware example is console based, which provides an user-interactive menu options for user to select and configure the multiple temperature sensors at different instances, such as 2/3/4-wire RTDs, NTC Thermistors and Thermocouples.

The connection block diagram is described below:


|image1|

.. important::

   This code has been developed and tested on SDP-K1 Controller Board using the on-board Arduino/SDP-120 Headers. However, same code can be used without or with little modifications on any other Mbed supported board which has Arduino Header Support on it, such as STM32-Discovery, STM32-Nucleo, etc.


--------------

Useful links
------------

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/useful_links#Useful Link&showfooter=nofooter

-  :doc:`AD7124 No-OS Software </wiki-migration/resources/tools-software/uc-drivers/ad7124>`
-  :adi:`AD7124-8 Product Page <AD7124-8>`
-  :adi:`AD7124-4 Product Page <AD7124-4>`
-  :adi:`AD7124-8 Evaluation Board <EVAL-AD7124-8>`
-  :adi:`AD7124-4 Evaluation Board <EVAL-AD7124-4>`

--------------

Hardware Connections
--------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_temperature_hw_connections.jpg
   :align: center
   :width: 650px

.. note::

   Connect the VIO_ADJUST jumper on the SDP-K1 board to 3.3V position to drive SDP-K1 GPIOs at 3.3V.

   
   For AD7124 evaluation board connections and jumper settings, refer the respective evaluation board manual. Arduino connector is used as default interface type for both the boards in the software.


SDP-K1 is powered through USB connection from the computer. SDP-K1 acts as a serial device when connected to PC, which creates a COM Port to connect to serial terminal (console based application) running on windows-os. The COM port assigned to a device can be seen through the device manager for windows based OS.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/com_port_sdp-k1.jpg
   :align: center
   :width: 350px

--------------

Software Downloads
------------------

AD7124 Temperature Measurement Mbed Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section briefs on the usage of MBED firmware. This also explains the steps to compile and build the application using mbed and *make* based build.

.. admonition:: Download
   :class: download

   Source code is hosted here:

   
   -  `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_
   
   Build Guide for Precision Converters MBED firmware (Use below link):
   
   -  :doc:`Precision Converters MBED Firmware </wiki-migration/resources/tools-software/product-support-software/pcg-fw-mbed-build-guide>`
   


Quick Start to use AD7124 Mbed Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are familiar with the Mbed platform, the following is a basic list of steps required to start running the code:

-  Connect the evaluation board to the SDP-K1 controller board, and power it appropriately, usually 3.3V to AVDD.
-  Connect the SDP-K1 controller board to your computer over USB.
-  Go to the link of the code provided above in the 'Source Code' section and import the code into the Mbed online compiler
-  Ensure the SDP-K1 controller board is selected as the target

   -  *If a different controller board is being used, then it should be selected, and the pin out in app_config.h may also need to be updated.*

-  In the Mbed Online IDE compile the code.
-  After a successful compile a binary file (.BIN) will be downloaded to your computer.
-  Drag and drop this binary to the USB drive corresponding to the SDP-K1 controller board.
-  Start up a serial terminal emulator (e.g. Tera Term)

   -  Find the com-port your controller board is connected on and select it.
   -  Set the baud-rate for 230400 baud, 8 data, no parity, 1 stop bit.
   -  Reset the controller board and connect.

-  The terminal windows should display the console menu providing access to the functionality.

Using the Firmware
------------------

Configure your serial terminal (`Tera Term <https://osdn.net/projects/ttssh2/releases/>`_) for below settings:

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_temp_example_teraterm_settings.jpg
   :align: center
   :width: 600px

The AD7124 temperature measurement example main menu looks like below (with Tera Term):


|image2|

.. tip::

   The firmware is designed to be intuitive to use, and requires little explanation, simply enter a number corresponding to the required command and follow the on-screen prompts.


Firmware allows user to perform the measurement for single or multiple (more than one) temperature sensors of same type. Below sensors are supported:

-  Single or Multiple 2/3/4-wire RTDs (default is PT100)
-  Single Or Multiple Thermocouple (default is T-type)
-  Single Or Multiple Thermistors (default is 10K NTC)

User must ensure all sensors are connected to AD7124 evaluation board as per configurations specific in the software and on this wiki page (see subsequent sections). If user intend to change these configurations in the software, the hardware connections must be modified as per new configurations. The details about altering the software modules for modifying the configurations are given in 'Modifying Firmware' section.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/bypassing_lk6_link_on_legacy_board.jpg
   :align: center
   :width: 600px

.. tip::

   In order to use analog inputs AIN4 and AIN5 on Legacy AD7124 Eval board (with SDP-120 interface only) in any of the demo mode, make sure to route the sensor connections directly through LK6 link, instead of physical screw-terminal connector. Make sure LK6 link is removed for the same purpose.


Multiple RTD (2/3/4-wire Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference: :adi:`CN0383.html <en/design-center/reference-designs/circuits-from-the-lab/CN0383.html>`

Multiple 2-wire RTD configurations:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_2_wire_rtd_configs.jpg
   :align: center

Multiple 3-wire RTD configurations:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_3_wire_rtd_configs.jpg
   :align: center

Multiple 4-wire RTD configurations:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_4_wire_rtd_configs.jpg
   :align: center

--------------

Multiple Thermocouple Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference: :adi:`CN0384.html <en/design-center/reference-designs/circuits-from-the-lab/CN0384.html>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_tc_configs.jpg
   :align: center

Cold Junction Compensation (CJC) configurations for TC measurement:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_cjc_configs.jpg
   :align: center
   :width: 700px

--------------

Multiple NTC Thermistor Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference: :adi:`cn0545.html <en/design-center/reference-designs/circuits-from-the-lab/cn0545.html>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_ntc10k_configs.jpg
   :align: center

--------------

Calibrating 3-wire RTDs
~~~~~~~~~~~~~~~~~~~~~~~

Firmware provides an option for user to perform calibrated measurement on 3-wire RTD sensors. There are two types of calibration options available in the firmware. User must modify sensor hardware connections according to configuration defined in the software. Based on selected calibration type, the sensors are first calibrated and then 3-wire RTD measurement is performed on them. For more information on the calibration scheme, refer the :adi:`design note <en/design-center/reference-designs/circuits-from-the-lab/CN0383.html>` on RTD measurement.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_3wire_rtd_calibration_menu.jpg
   :align: center
   :width: 700px

.. tip::

   Calibration is allowed to perform only on Multiple RTD sensors and not on a single RTD sensor.


--------------

Calibrating ADC (Internal and System Calibration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Firmware allows user to perform ADC calibration on the current sensor configuration (demo mode) selected through console menu. ADC calibration helps to remove any offset Or gain error present on the input channels. The updated device coefficients (gain and offset) post ADC calibration are used/applied during the sensor measurement. Therefore, once calibration is complete, user must go to the previous demo mode which was selected before ADC calibration and then perform the measurement on selected sensors. The calibration coefficients (gain and offset) are applied only on the analog input channels which were enabled prior to calibration. Also after calibration if any new demo mode is selected apart from the one which was enabled during calibration, the calibration coefficients are reset and doesn't applied on input channels. In this case, user must perform the calibration again.

Internal ADC calibration is straightforward but system calibration needs user inputs (typically after applying full-scale/zero-scale) voltages on selected analog inputs.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_calibration_menu.jpg
   :align: center
   :width: 700px

--------------

Modifying Firmware
------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_temp_sensor_file_structure.jpg
   :align: center
   :width: 700px

app_config.h
~~~~~~~~~~~~

This file can be used to:

-  Select the 'Active Device' as either AD7124-4 Or AD7124-8. Default active device is AD7124-4.
-  Select the SDP_K1 interface type as either Arduino Or SDP-120. Default is Arduino.

ad7124_regs_configs.h
~~~~~~~~~~~~~~~~~~~~~

This file defines the analog inputs, excitation sources, PGA, reference sources and power mode for all sensor demo mode configurations.

ad7124_regs_config_rtd.c, ad7124_regs_config_thermistor.c, ad7124_regs_config_thermocouple.c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These files define the AD7124 register configurations used for various sensor demo modes.

ad7124_user_config.c
~~~~~~~~~~~~~~~~~~~~

This file defines the user configurations for the AD7124, such as SPI parameters (frequency, mode, etc) and other init parameters used by No-OS drivers to initialize AD7124 device. These are the parameters loaded into device when device is powered-up or power-cycled.

ad7124_console_app.c
~~~~~~~~~~~~~~~~~~~~

This file defines the functionality for selecting and displaying sensor configurations (hardcoded in the software), perform ADC sampling on selected sensor channels and display temperature measurement result for selected sensors.

ad7124_temperature_sensor.cpp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file defines the functions which acts as wrapper for calling 'tempsensor' library functions to calculate the temperature based on resistance or voltages. The fixed sensors such as NTC 10K, T type thermocouple, PT100/PT1000 RTD are used.

No-OS Drivers for AD7124
~~~~~~~~~~~~~~~~~~~~~~~~

No-OS drivers provide the high level abstracted layer for digital interface of AD7124 device. The complete digital interface (to access memory map and perform data read) is done in integration with low level platform drivers.

The functionality related with No-OS drivers is covered in below 2 files:

-  ad7124.c
-  ad7124.h

.. tip::

   It is hoped that the most common functions of the AD7124 are coded, but it's likely that some special functionality is not implemented. Feel free to consult Analog Devices :adi:`Engineer-Zone <engineerzone>` for feature requests, feedback, bug-reports etc.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_multiple_sensor_interface_block.jpg
   :width: 650px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_temperature_measure_main_menu.jpg
   :width: 400px
