Running the Basic Example for ADuCM302x EZ-Kit with Keil MDK
============================================================

Overview
--------

This page describes the steps required to build and run basic example on ADuCM3029 EZ-KIT board using Keil MDK.

Environment Setup
-----------------

Before running the basic example with Keil MDK, you should make some preparation for environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices Keil MDK. For more information please refer to `Software environment set up for Keil MDK <https://wiki.analog.com/resources/tools-software/freertos/rtos-user-guide/software-enviroment-setup-keil-mdk>`__
-  FreeRTOS product and the Analog Devices FreeRTOS product. For more information please refer to :doc:`Get the source code ready </wiki-migration/resources/tools-software/freertos/rtos-user-guide/hardware-software-setup>`
   ===== Hardware Setup =====
-  An ADuCM302x EZ-Kit board
-  A J-Link Lite

Connect **DEBUG P4** port of the EZ-Kit to the host PC using the J-Link connector, connect the **USB to UART** port on the EZ-Kit to the host PC using the USB cable provided and simultaneously connect the power supply with 5 volts as in the diagram below

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/3029-j-link.jpg
   :width: 400px

--------------

Build the Example
-----------------

Before you run the FreeRTOS example in Keil MDK, follow below four steps to import and build it.

1. Import the FreeRTOS example into Keil MDK

-  Select the **Open Project** option from the **Project** menu
-  In the file tree window browse to the **FreeRTOSv10.0.0\\FreeRTOS\\Demo\\CORTEX_M3_ADuCM302x_KEIL** folder in the **FreeRTOS product installation** and select the **RTOSDemo.uvprojx** file.
-  Click the **Open** button to import the project

2. Choose Debug/Release mode to build the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/keil/3029-debug-release-keil.png
   :width: 400px

3. Build the project in Keil MDK

-  Select the **Build Target/Rebuild All Target Files** option from the **Project** menu

4. Configure a serial console application of your choice to view the output from the **UART to USB connection** on the HOST PC

-  The Keil MDK is unable to output and text to the console within the MDK IDE.The output of the application is transmitted via UART to the serial console. The easiest way to determine the correct USB device is to view the **Ports** entry in the Windows Device Manager.From here identify the COM port.Configure your serial console application to connect to the port with a baud rate of 57600

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/keil/3029keil_com.png
   :width: 600px

--------------

Run the Example
---------------

Follow below two steps to do debug configuration, download and run the built binary on the target board

1. From the **Flash** menu select the **Download** sub-menu and then choose the **Start/Stop Debug Session** option from **Debug** menu.

2. Click the **Run** button to start running the application

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/keil/3029keil_run.png
   :alt: 3029keil_run.png
   :width: 400px

--------------

Test Results
------------

When the application runs it will blink three LEDs on the EZ-Kit, **The test is ok for <num> round(s)** will be printed constantly and **Test Passed** which means the test is successful will be printed after 25 rounds on the console.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm302x-ez-kit/keil/3029keil_output.jpg
   :width: 400px
