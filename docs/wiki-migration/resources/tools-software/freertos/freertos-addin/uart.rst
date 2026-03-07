Enabling UART
=============

Note: This section of the document applies to the ADSP-SC5xx (Cortex-A and SHARC+) and ADSPBF7xx processors. It does not apply to the ADuCM\* processor families. CrossCore Embedded Studio provides support for the on-chip peripherals and EZ-KIT hosted device drivers that are provided for its processors. In order to use these features with FreeRTOS the source based versions of the drivers must be used rather than the default pre-built libraries that are provided.

.. note::

   Use of the library based version of the System Services and Device Drivers is not compatible with FreeRTOS. Use of the pre-built libraries may result in run-time corruption and execution failure. All of the setup is done automatically by the Add-In when it is added to a project, you can view the setup list for :doc:`Using System Services and Device Drivers in your CCES project </wiki-migration/resources/tools-software/freertos/rtos-user-guide/using-cces-system-services-and-device-drivers-freertos>`


To get started using UART alongside the FreeRTOS Add-In, you must first make sure that you have added the **Pin Multiplexing** and **UART** Add-Ins to your project. This should be automatically done by the Add-In when it is added to your project.

--------------

Final Step
----------

Now you should have both **Pin Mulitplexing** and the **UART** Add-Ins installed into your project.

-  Click on the System.svc
-  Select the **Pin Mulitplexing** tab.
-  Enable UART Setting **-Suggested: UART0 All Options-**

--------------

Disabling UART
--------------

This section is for removing UART functionality from an existing project. To remove UART we follow the inverse of the adding UART steps which are as follows.

Remove the source based version of the required services and driver:

-  Double click the system.svc file in the Project Explorer
-  Select UART from the Add-In list
-  Click the Remove button in the System Configuration Overview
-  Accept
-  Select the **Pin Multiplexing** tab
-  Disable UART setting **-Default UART0 All Options-**
