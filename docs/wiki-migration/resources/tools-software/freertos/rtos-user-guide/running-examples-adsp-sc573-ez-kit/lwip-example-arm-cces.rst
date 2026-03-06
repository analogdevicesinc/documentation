Running the LwIP Example for ARM on ADSP-SC573 EZ-Kit with CrossCore Embedded Studio
====================================================================================

Overview
--------

This page describes the steps to build and run the LwIP Example for ARM on ADSP-SC573 EZ-Kit with CrossCore Embedded Studio.

Environment Setup
-----------------

Before running the lwip example with CrossCore Embedded Studio, you should make some preparation for environment setup including software and hardware.

Software Requirement
--------------------

-  Analog Devices CrossCore Embedded Studio. For more information please refer to `Software environment set up for CrossCore Embedded Studio <https://wiki.analog.com/resources/tools-software/freertos/rtos-user-guide/software-enviroment-setup-cces>`__
-  FreeRTOS product and the Analog Devices FreeRTOS product. For more information please refer to :doc:`Get the source code ready </wiki-migration/resources/tools-software/freertos/rtos-user-guide/hardware-software-setup>`

Hardware Setup
--------------

-  An ADSCP-SC573 EZ-Kit board
-  An ICE1000 or ICE2000 emulator

Connect the ICE1000 or ICE2000 emulator to **DEBUG P1** port of EZ-Kit and the host PC using USB cable, connect the target board to the same LAN as PC using standard network cable and simultaneously connect the power supply with 5 volts as in the diagram below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/573-lwip-hw.jpg
   :width: 400px

--------------

Build the Example
-----------------

Before you run the FreeRTOS example in CrossCore Embedded Studio, follow below three steps to import and build it.

1.Import the FreeRTOS example into CrossCore Embedded Studio:

-  Select the **File** menu and then select the **Import** option from the menu and when the **Import** project window appears
-  Click on the **General** folder, then click on the **Existing Projects into Workspace** entry, and click **Next**
-  Click the **Select root directory** radio button and then click the **Browse** button
-  Browse the root folder where you previously installed the FreeRTOS product and then browse down into the \**FreeRTOSv10.0.0\\FreeRTOS\\Demo\\CORTEX_A5_ADSP_SC573_CCES_LwIP \*\* folder
-  Click **Finish** to close the file browser dialog
-  A single project should appear in the **Project Explorer**
-  Check the entry in the projects pane and click Import

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/lwip_import.png
   :width: 400px

2. Choose Debug/Release mode to build the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/t2_副本.jpg
   :width: 200px

3. Build the project in CrossCore Embedded Studio

-  In the **Project Explorer** right click on the **DnsClient_FreeRTOS_A5** project and select the **Build Project** option from the menu

--------------

Run the Example
---------------

Follow below four steps to do debug configuration, download and run the built binary on the target board

1. In the **Project Explorer** right click on the **DnsClient_FreeRTOS_A5** project and select the **Debug As** option from the menu 2. From the popup menu select **Debug Configurations** option to create a new debug configuration that matches your emulator and target board

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/573lwip_debug_cog.png
   :width: 1000px

3. Click the **Debug** button to close the **Debug Configuration** window

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/573lwip_debug_conf2.png
   :width: 1000px

4. Click the **Run/Resume** button to start running your application

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/573lwip_resume.png
   :width: 600px

--------------

Test Results
------------

Output from the application should be visible within the **Console** window in the CrossCore Embedded Studio IDE. You should see link is established, and **IP ADDRESS** assigned from DHCP server will be printed after you install the LwIP.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/rtos-user-guide/running-examples-adsp-sc573-ez-kit/lwip/573lwip.png
   :width: 1000px
