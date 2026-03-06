Installation Procedure
======================

| 
| :doc:`Click here to return to the SigmaStudio and SigmaDSP Documentation top page. </wiki-migration/resources/tools-software/sigmastudio>`
| This page describes how to install the SigmaStudio on a computer running the Microsoft Windows operating system.

.. admonition:: Download
   :class: download

   Download the latest version of SigmaStudio at our :adi:`download site <sigmastudiodownload>`.


System Requirements
-------------------

Most modern Windows PCs will be able to run SigmaStudio. Expand the display below to view requirements. 

.. raw:: html

   <details><summary>Click to expand</summary>

-  Windows 7/ Windows 10
-  256 MB of RAM (1 GB recommended)
-  80 MB of available hard disk space
-  1024 x 768 screen resolution
-  USB 1.1/2.0 data port (Required for use with Evaluation hardware only)

   -  Note that USB 2.0 or higher is required for use with the USBi (EVAL-ADUSB2EBZ)

.. raw:: html

   </details>


   | 

Step 1: Before You Install
--------------------------

-  Quit any applications you are running. This is not strictly required for SigmaStudio, but is generally good practice while installing new software.

Step 2: Application Setup
-------------------------

-  Run the setup application (named similarly to ``ADI_SigmaStudio-Rel4.5-x64.exe``). On managed corporate machines, it's recommended to run the installer elevated.
-  Review the contents of the license agreement.
-  The installer will proceed through the rest of the installation.

Step 3: Driver Installation
---------------------------

In most cases, driver installation is performed alongside SigmaStudio. If your machine is the rare exception, please follow these steps: 

.. raw:: html

   <details><summary>Click to expand</summary>

-  Connect the USB cable between your evaluation hardware and a PC USB port.
-  If this is your first time connecting the USB device, the Windows "Found New Hardware Wizard" will launch.
-  If prompted, choose “Install from a list or a specific location” and click "Next".
-  Select “Search for the best driver in these locations” and check the box for “Include this location in the search.”
-  Press the "Browse" button and locate the appropriate driver file in the SigmaStudio application folder (default folder is C:\\Program Files\\Analog Devices Inc\\Sigma Studio X.Y\\USB drivers, where X.Y represents the release version of the software)

   -  For **USB serial converter** and Eval-Boards (FDTIxx.inf) select **ftd2xx.inf** file.

      -  Any evaluation board sold after 2007 uses the USBi interface, but the FTDI drivers are included for backwards-compatibility.

   -  For the **USBi** interface select **CyUSB.inf file**.

-  Click "Continue Anyway" if you're prompted with "This software has not passed Windows Logo testing."

.. raw:: html

   </details>


Step 4: Hardware Configuration
------------------------------

-  Setup the Evaluation hardware jumpers and I/O configurations, refer to Evaluation Board documentation available on the web at :adi:`SigmaDSP Evaluation Boards </en/content/sigmadsp_evaluation_boards/fca.html>`.
-  For additional help, see the Evaluation Board Setup Examples.
-  If you are using the USBi, there is a quick way to verify that the driver is installed properly. Make a new project and drag in a USBi object from the ToolBox. The "USBi" text is highlighted green when the USBi is detected, and red when disconnected.

|

| It is rare for users to have issues during installation. If something does come up, please create a new question in the :ez:`SigmaDSP EngineerZone <dsp/sigmadsp>` forum and describe what is happening.
