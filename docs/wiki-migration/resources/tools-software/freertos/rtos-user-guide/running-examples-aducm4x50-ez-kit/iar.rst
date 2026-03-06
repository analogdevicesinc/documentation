Running the Basic Example for ADuCM4x50 EZ-Kit with IAR Embedded Workbench
==========================================================================

Overview
--------

This page describes the steps required to build and run basic example on ADuCM4x50 EZ-KIT board using IAR Embedded Workbench.

Environment Setup
-----------------

Before running the basic example with IAR Embedded Workbench, you should make some preparation for environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices IAR Embedded Workbench. For more information please refer to `Software environment set up for IAR <https://wiki.analog.com/resources/tools-software/freertos/rtos-user-guide/software-enviroment-setup-iar>`__
-  FreeRTOS product and the Analog Devices FreeRTOS product. For more information please refer to :doc:`Get the source code ready </wiki-migration/resources/tools-software/freertos/rtos-user-guide/hardware-software-setup>`
   ===== Hardware Setup =====
-  An ADuCM4x50 EZ-Kit board
-  A J-Link Lite

Connect DEBUG P4 port of the EZ-KIT board to a PC running IAR Embedded Workbench using the J-Link and simultaneously connect the power supply with 5 volts as in the diagram below

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/iar/4050-j-link.jpg
   :width: 400px

--------------

Build the Example
-----------------

Before you run the FreeRTOS example in IAR Embedded Workbench, follow below three steps to import and build it.

1. Select the **Add Existing Project** from the **Project Menu** and browse to the **FreeRTOSv10.0.0\\FreeRTOS\\Demo\\CORTEX_M4_ADuCM4x50_IAR\\iar** folder within the FreeRTOS product directory and import the project

2. Choose Debug/Release mode to build the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/iar/3029-iar-debug-release.png
   :width: 400px

3. Build the project in the IAR workbench

-  From the **Project** menu select the **Make** option and enter the file name

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/iar/2_1.png
   :width: 600px

--------------

Run the Example
---------------

Follow below four steps to do debug configuration, download and run the built binary on the target board.

1. From the **Project menu** select the **Download and Debug** option

You may meet the Device Selection window, please select Coretex-M4 device.

2. The application should load and halt at main. Continue the application to see it run.

Test Results
------------

Output from the application should be visible within the **Terminal I/O** window which can be found in View menu in the IAR Embedded Workbench IDE. You should see three LEDs on the EZ-Kit are blinking. **The test is ok for <num> round(s)** will be printed constantly and **Test Passed** which means the test is successful will be printed after 25 rounds in the console.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/iar/3029iar_output_2_.png
   :width: 400px
