AD5770R ADuCM410 IAR Example
============================

Supported Device
----------------

-  :adi:`AD5770R`

Introduction
------------

The :adi:`AD5770R` is a 6-channel, 14-bit resolution, low noise, programmable current output digital-to-analog converter (DAC) for photonics control applications. This chip incorporates a 1.25 V on-chip voltage reference, a 2.5 kΩ precision resistor for reference current generation, die temperature, output monitoring functions, fault alarm, and reset functions.

The :adi:`AD5770R` contains five 14-bit resolution current sourcing DAC channels and one 14-bit resolution current sourcing/ sinking DAC channel.

Channel 0 can be configured to sink up to 60 mA and source up to 300 mA. Channel 1 to Channel 5 have multiple, programmable output current sourcing ranges, set by register access. Each DAC can operate with a wide power supply rail from 0.8 V to AVDD − 0.4 V for optimizing power efficiency and thermal power dissipation.

This page describes the AD5770R firmware example running on the :adi:`ADuCM410 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-aducm410.html>` controller board, interfacing with the AD5770R evaluation board. The firmware example comprises 3 layers of software, built on top of the Mbed OS.

-  Console Application - uses the ADI console libraries to provide a basic terminal UI
-  AD5770R No-OS Driver - AD5770R device C API
-  Platform Drivers - Hardware Abstraction Layer (SPI, GPIO, ...) to adapt No-OS driver to ADuCM410 drivers

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r_m410_software_architecture.jpg
   :align: center
   :width: 400px

Useful links
============

-  :adi:`ADuCM410 Controller Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-aducm410.html>`
-  :adi:`SDP-120 Breakout Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-breakout-board.html#eb-overview>`
-  `IAR ARM Compiler Toolchain <https://www.iar.com/iar-embedded-workbench/#!?architecture=Arm>`__
-  :doc:`AD5770R No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/ad5770r>`
-  :doc:`AD5770R IIO DAC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dac/ad5770r>`
-  :adi:`AD5770R Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5770R.html>`

Hardware Setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r_m410_hardware_connection.jpg
   :align: center

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/aducm410_jumper_settings.jpg
   :align: center
   :width: 500px

The :adi:`AD5770R Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5770R.html>` is connected to ADuCM410 using the :adi:`SDP-120 Breakout Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-breakout-board.html#eb-overview>`. The evaluation board must be powered externally, typically using an external 3.3V DC supply connected to the AVDD input supply terminal, if using the default power supply jumper settings.

The default jumper configuration of the evaluation board selects a diode dummy load on all of the output channels. Refer to the evaluation board user guide for the jumper configuration necessary to route the output current to the screw terminal.

:adi:`ADuCM410 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-aducm410.html>` controller board is powered through USB connection from the computer. ADuCM410 controller board acts as a Serial device when connected to PC, which creates a COM Port to connect to serial console terminal using UART protocol. The COM port assigned to a device can be seen through the device manager for windows-based OS. Use 2nd port from list (Device B) for console terminal application communication.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/aducm410_com_port.jpg
   :align: center
   :width: 400px

AD5770R IAR Firmware
--------------------

Source Code
~~~~~~~~~~~

.. admonition:: Download
   :class: download

   The latest version of the example code is available here:

   
   -  `AD5770R ADuCM410 IAR Example <https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r_iar_m410example.zip>`__
   


.. admonition:: Download
   :class: download

   Code compilation and Debugging guide using IAR:

   
   -  `ADuCM410 Development Toolchain Guide <https://wiki.analog.com/_media/resources/tools-software/product-support-software/aducm410_development_toolchain_support.pdf>`__
   


Quick Start
===========

-  Connect the AD5770R EVAL-board to the ADuCM410 controller board as mentioned in the "Hardware Setup" section and apply external 3.3V DC supply to Eval board through AVDD terminal.
-  Connect the ADuCM410 controller board to your computer over USB cable (also acts as a power supply).
-  Download the code from the software download link provided on this page and compile it using IAR compiler.

The detailed guide to use IAR compiler and J-link mIDAS programmer is provided in 'ADuCM410 Development Toolchain Guide'.

Firmware in Detail
------------------

The example is menu driven, providing keyboard shortcuts to access/execute the menus items, and prompting for further inputs where necessary. When the example runs, it attempts to connect and initialize the AD5770R. The configuration used is defined in the ad5770r_user_config.h file, which can be modified as needs be to suit specific applications.

*Note: While much of the functionality of the AD5770R No-OS driver is made available through the console UI, not all function are available. The additional AD5770R functionality can only be configured the ad5770r_user_config.c file.*

Main Menu
~~~~~~~~~

The AD5770R Console App main menu provides basic initialization/reset type functions, and access to several sub-menus that provide more detailed configuration and control settings. Like most menus in the firmware, the menu options are framed by a header and footer that display status information related to the functions on the menu.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/main_menu.jpg
   :align: center
   :width: 400px

The value of the scratchpad register is displayed in both the header and the footer. After reading the scratchpad value for the header, the value is incremented and written back to the device, such that the scratchpad footer value should always be equal to the header value + 1. This can be useful a debug aid to confirm communications.

DAC Operations
~~~~~~~~~~~~~~

This menu provides the ability to set the Input and DAC register values, and control the update of the DAC using both the hardware and software LDAC functions. The ordering of menu items is intended to follow the order in which actions are typically performed by the user.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad5770r/dac_operations.jpg
   :align: center
   :width: 400px

There are three ways in which the DAC output may be controlled using this menu.

-  Write to Input Channel(s), set software LDAC shadow value, then write software LDAC to update DAC output
-  Write to Input Channel(s), toggle hardware LDAC
-  Write to DAC Channel to directly update DAC output

Toggling a channel in the software LDAC shadow sets a bit corresponding to that channel in a mask. This SW LDAC Channel shadow value can then be written in a single transaction, transferring the input to the DAC value for all of the channels which are set in the shadow mask.

The channels affected by the hardware LDAC pin toggling are set in the ad5770r_user_config.h file at compile time.

.. note::

   The toggling of the hardware LDAC is outside of the AD5770R No-OS driver, and as such the DAC values are not updated by this action.


.. tip::

   For support on this firmware example and No-OS drivers please go to :adi:`Engineer-Zone <engineerzone>`.

