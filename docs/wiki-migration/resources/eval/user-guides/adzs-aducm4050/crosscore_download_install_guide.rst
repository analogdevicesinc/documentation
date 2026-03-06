CrossCore Embedded Studio Download and Installation Guide
=========================================================

This page provides all the necessary steps to get :adi:`CrossCore Embedded Studio’s <en/design-center/processors-and-dsp/evaluation-and-development-software/adswt-cces.html>` (CCES) software environment up and running on Windows or Linux. The CCES software development environment for the ADZS-ADuCM4050 EZ-KITs is based on open source tools, and is maintained by Analog Devices. CCES includes support for DSP (digital signal processing) and ARM Cortex-M and Cortex-A devices, and includes the following features and many more:

-  Eclipse based IDE
-  GNU ARM Embedded Toolchain for Cortex-M core based parts (5-2016-q2-update release)
-  OpenOCD with support for ADuCM4050 microcontroller (open source SWD)
-  CMSIS Pack files
-  Mbed CMSIS-DAP

.. important::

   CrossCore Embedded Studio is based on Eclipse, but because the MBED platform provides a CMSIS-DAP interface to connect to the board, the ADZS-ADuCM4050 can be used without problems with IAR Embedded Workbench IDE or Keil µVision IDE as well.


Pre-Requisites and Requirements List
====================================

The items listed below are required for the tools and software to work properly.

-  ADZS-ADuCM4050 hardware
-  PC or laptop computer
-  2 USB 2.0 Mini-B to A cables

.. important::

   The USB cables need to have ALL data lines connected, a charging only mini USB cable will not work.


-  Terminal Program to interface the PC with the ADZS-ADuCM4050

   -  Putty
   -  Tera Term
   -  Or other preferred Terminal program

CrossCore Embedded Studio Download
==================================

.. admonition:: Download
   :class: download

   
   The ADZS-ADuCM4050 **requires** the use of Crosscore Embedded Studio version **2.6.0 or higher**. Do not attempt to use earlier versions of the CrossCore tools, due to compatibility issues that will **damage** the ADZS-ADuCM4050.
   
   `CrossCore Embedded Studio 2.6.0 Windows Installer(Executable) <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.6.0/ADI_CrossCoreEmbeddedStudio-Rel2.6.0.exe>`__
   
   `CrossCore Embedded Studio 2.6.0 Ubuntu Linux Installer(Debian) <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.6.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.6.0.deb>`__


The following features are available and supported
--------------------------------------------------

-  Compilation using the GNU ARM Embedded toolchain for the ADuCM302x and ADuCM4x50 ARM Cortex-M cores
-  Debugging ADuCM302x and ADuCM4x50 via the IDE with GDB/OpenOCD
-  Development and debugging of bare-metal applications on the ADuCM302x and ADuCM4x50 ARM Cortex-M cores

The following features are only supported via the Windows version
-----------------------------------------------------------------

-  Use of CrossCore Embedded Studio Add-Ins other than the Linux Add-In

CrossCore Embedded Studio Installer Instructions
================================================

It is best to save all the files/folders to the default directories recommended by the CrossCore Embedded Studio installer. This way all the instructions and support provided will be standard.

Installing CrossCore Embedded Studio on Windows
-----------------------------------------------

-  To install CrossCore Embedded Studio, double-click ADI_CrossCoreEmbeddedStudio-Rel2.6.0.exe
-  The CrossCore Embedded Studio installer will install the mbed Windows serial driver.

   -  It is available separately, if required

      -  https://developer.mbed.org/handbook/Windows-serial-configuration

The executable installs all necessary components to the Analog Devices local directory structure which can be found below.

-  CrossCore Embedded Studio installs to **C:\\Analog Devices\\CrossCore Embedded Studio 2.6.0**
-  Eclipse IDE installs to **C:\\Analog Devices\\CrossCore Embedded Studio 2.6.0\\Eclipse**
-  GNU ARM Embedded Toolchain for Cortex-M installs to **C:\\Analog Devices\\CrossCore Embedded Studio 2.6.0\\ARM\\gcc-arm-embedded**
-  OpenOCD installs to **C:\\Analog Devices\\CrossCore Embedded Studio 2.6.0\\ARM\\openocd\\bin**

Installing CrossCore Embedded Studio on Linux
---------------------------------------------

-  To install CrossCore Embedded Studio, run the command:

   -  sudo dpkg -i adi-CrossCoreEmbeddedStudio-linux-x86-2.6.0.deb

The Ubuntu Linux Installer (Debian) installs all necessary components to the Analog Devices local directory structure which can be found below.

-  CrossCore Embedded Studio installs to **/opt/analog/cces/2.6.0**
-  Eclipse IDE installs to **/opt/analog/cces/2.6.0/Eclipse**

.. note::

   For full documentation of the software please refer to the :adi:`CrossCore Embedded Studio <en/design-center/processors-and-dsp/evaluation-and-development-software/adswt-cces.html>` web site.


Activating CrossCore Embedded Studio
====================================

The first time CrossCore Embedded Studio is launched, a prompt to input a serial number, name, and email address will be presented. The serial number is dependent upon the model being used:

.. important::

   **ADZS-ADuCM4050LF CrossCore Serial Number**

   
   EZK-CCES-QCQ9-692E-TSCV-M9N6-A2NB-ZW8M-H201
   
   **ADZS-ADuCM4050WL CrossCore Serial Number**
   
   EZK-CCES-YBS4-NX3P-EQR3-XEDE-9IN6-DJRJ-DW01


The New License Wizard will guide the process.

-  Select *Yes* to install a license at this time
-  Choose **I have a serial number that I would like to activate** and click *Next*
-  Determine the model being used and enter the appropriate serial number (above) and click *Next*
-  Choose **Install and activate a license on-line all in one step** and click *Next*
-  Complete the **Name** and **Address** entry boxes and click *Finish*
-  On success, a window stating “Your license has been successfully activated” will be presented. Click *OK*

Once the serial number has been activated, the CrossCore development tools will allow full and unlimited access to all the features when using the Analog Devices family of ARM Cortex Processors.

CrossCore Embedded Studio Support
=================================

For more details on CrossCore Embedded Studio, updated versions of the tools, release notes, tools documentation, or other support, please visit the CrossCore :adi:`webpage <cces>`, or email the CrossCore support team at processor.tools.support@analog.com.

*End of Document*
