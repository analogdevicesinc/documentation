Running the Basic Example for ADuCM4x50 EZ-Kit with CrossCore Embedded Studio
=============================================================================

Overview
--------

This page describes the steps required to build and run basic example on ADuCM4x50 EZ-KIT board using CrossCore Embedded Studio.

Environment Setup
-----------------

Before running the basic example with CrossCore Embedded Studio, you should make some preparation for environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices CrossCore Embedded Studio. For more information please refer to `Software environment set up for CrossCore Embedded Studio <https://wiki.analog.com/resources/tools-software/freertos/rtos-user-guide/software-enviroment-setup-cces>`__
-  FreeRTOS product and the Analog Devices FreeRTOS product. For more information please refer to :doc:`Get the source code ready </wiki-migration/resources/tools-software/freertos/rtos-user-guide/hardware-software-setup>`

Hardware Setup
--------------

-  An ADuCM4x50 EZ-Kit board
-  An ICE1000 or ICE2000 emulator

Connect the ICE1000 or ICE2000 emulator to **DEBUG P5** port of EZ-Kit and the host PC using USB cable and simultaneously connect the power supply with 5 volts as in the diagram below

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050ice.jpg
   :width: 400px

--------------

Build the Example
-----------------

Before you run the FreeRTOS example in CrossCore Embedded Studio, follow below three steps to import and build it.

1. Select the **File** menu and then select the **Import** option from the menu and when the **Import** project window appears

-  Click on the **General** folder, then click on the **Existing Projects into Workspace** entry, and click **Next**
-  Click the **Select root directory** radio button and then click the **Browse** button
-  Browse the root folder where you previously installed the FreeRTOS product and then browse down into the \**FreeRTOSv10.0.0\\FreeRTOS\\Demo\\CORTEX_M4_ADuCM4x50_CCES \*\* folder
-  Click **OK** to close the file browser dialog
-  A single project should appear in the **projects** pane of the **Import** window
-  Check the entry in the **projects** pane and click **Finish** to close the file browser dialog

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050-import.png
   :width: 400px

2. Choose Debug/Release mode to build the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050-cces-debug-release.png
   :width: 400px

3. Build the project in CrossCore Embedded Studio

-  In the **Project Explorer** right click on the **RTOSDemo_CCES** project and select the **Build Project** option from the menu

--------------

Run the Example
---------------

Follow below four steps to do debug configuration, download and run the built binary on the target board.

1. In the **Project Explorer** right click on the **RTOSDemo_CCES** project and select the **Debug As** option from the menu 2. From the popup menu select **Debug Configurations** option to create a new debug configuration that matches your emulator and target board

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050-debug-configuration.png
   :width: 400px

3. Click the **Debug** button to close the **Debug Configuration** window

4. Click the **Run/Resume** button to start running your application

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050-run-resume.png
   :width: 400px

--------------

Test Results
------------

Output from the application should be visible within the **Console** window in the CrossCore Embedded Studio IDE. You should see three LEDs on the EZ-Kit are blinking. The test is ok for <num> round(s) will be printed constantly and **Test Passed** which means the test is successful will be printed after 25 rounds in the console.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-aducm4x50-ez-kit/cces/4050-cces-output.png
   :width: 400px
