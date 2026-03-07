AD-BMSE2E3W-SL Software User Guide
==================================

| 
|

.. admonition:: Download
   :class: download

   A concise version of this document is available in portable document format. Click on the file below to download:


   | `AD-BMSE2E3W-SL QUICKSTART GUIDE (pdf) <https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl-ug-2245.pdf>`_
   
   |

| ==== Requirements ====

-   Host PC (Windows 10 or later) *with administrator and internet access*

   -  1920 by 1080 or greater screen resolution, recommended

| 
| The **AD-BMSE2E3W-SL GUI** also referred as the **Light EV BMS GUI** is a PC-based Graphical User Interface (GUI) tool designed to work in conjunction with the ADBMSE2E3W-SL board.
| **MyAnalog.com account is required to download the software**.

| 
| Follow the steps below to create a MyAnalog account:

| 1. Go to :adi:`MyAnalog <en/index.html>` and create an account using email. Select the "**Register with email**" option to get started. |image1|
| 2. Once you have a MyAnalog account, log in to :adi:`MyAnalog <en/index.html>` using your credentials. |image2|

| 
| ----

Request for Software Access
===========================

|

.. important::

   Send the following details to this email address: <fc #6495ed>\ **LEV_CSESupport@analog.com**\ </fc>


   | \* MyAnalog email address
   
   -  Company
   -  Country
   -  Purpose/Projects
   


|

--------------

Software Download
=================

| 1. Click this link: `AD-BMSE2E3W-SL Version 1.0.0 <https://wiki.analog.com/https/download.analog.com/secure/bms-cse-solutions/e2e3w-00/1-0-0/ad-bmse2e3w-sl-rel1.0.0.exe>`_.
| 2. You will be directed to the *Software Package Download* page. Tick the checkbox and click the **I Accept** button to indicate acceptance of the license agreement.
| |image3|
| 3. Click the **Download** button to download the installer.

.. tip::

   When software updates or new versions of the software are available, Analog Devices sends a notification to the email address associated with the MyAnalog account used to download the original software package.


--------------

GUI Installation
================

1. Double-click on <fc #6495ed>\ **ad-bmse2e3w-sl-rel1.0.0.exe**\ </fc> to install the program to your computer.


|image4|

2. Accept the license terms and click *Next* to proceed with the installation. The default installation directory is in **C:\\Analog Devices\\**


|image5|

| 3. Locate the <fc #6495ed>\ **light_ev_bmsv1.0.0.hex**\ </fc> file inside the AD-BMSE2E3W-SL installer files folder.
| **C:\\Analog Devices\\AD-BMSE2E3W-SL-Rel1.0.0\\Software\\Firmware**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/firmware_location.png
   :align: center
   :width: 600px

4. Drag and drop the .hex file into the DAPLink drive to flash the program on the MCU.

| |image6|
| 5. Find the <fc #6495ed>\ **Light_EV_BMS_GUI.exe**\ </fc> file inside the AD-BMSE2E3W-SL installer files folder.
| **C:\\Analog Devices\\AD-BMSE2E3W-SL-Rel1.0.0\\Software\\GUI\\Light_EV_BMS_GUI_v1.0.0**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/gui_executable_file_location.png
   :align: center
   :width: 1000px

| 6. Double-click the <fc #6495ed>\ **Light_EV_BMS_GUI.exe**\ </fc> file to open the program. You should see a script running in the background separately and the landing page running in the browser.
| |image7|

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/home_landing_page.png
   :align: center

| 
| ----

Interface Setup
===============

| |image8|
| \|\ **Details Available on the Landing Page** \||\|

+---+------------------------------+-------------------------------------------------------------------------------------------------+
|   | **Function**                 | **Definition**                                                                                  |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 1 | Connection Indicator         | Shows if UART or CAN is connected                                                               |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 2 | Communication Mode Drop Down | Allows selection of the communication mode                                                      |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 3 | Vehicle System Mode          | Contains a dropdown list for vehicle system states such as parked, driving, charging, and fault |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 4 | Refresh Button               | Updates the list of available communication ports                                               |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 5 | Battery Specifications       | Input boxes for battery specifications which are used for SoC and SoH                           |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 6 | Load Defaults Button         | Sets the battery specification values to the predefined default program entries                 |
+---+------------------------------+-------------------------------------------------------------------------------------------------+
| 7 | Start Button                 | Initiates battery monitoring and directs users to the Overview page                             |
+---+------------------------------+-------------------------------------------------------------------------------------------------+

| 
| 1. Set the jumper configuration based on the communication mode being used: UART or CAN.
| |image9|
| On the GUI landing page, hover to the *Communication Mode* dropdown menu. Select *UART COM* followed by the specific port number if using UART, or *CAN* if using CAN.
| |image10|
| Press the RESET button every time the hardware set up is changed. |image11|
| 2. Click the <fc #6495ed>\ **Load Defaults**\ </fc> button to set the initial entry values for the different parameters needed for the State of Charge (SoC) and State of Health (SoH) calculations.
| |image12|
| 3. Click the <fc #6495ed>\ **Start**\ </fc> button to begin the measurements. |image13|

--------------

Tabs
====

Overview
--------

| The Overview tab features plots for stack voltage, module current, max charge current, max discharge current, cell voltages, cell temperatures, and state of the battery. This tab also allows setting of the vehicle state, which by default is set to "PARKED".
| |image14|

| 
| === Graph === The Graph tab enables checking the progression of the readings for different parameters such as the cell voltage, temperature, SoC, SoH, and pack voltage and current.
| |image15|

| 
| === Console === Presents the actual numerical data being fetched by the UI in a tabular form. This tab allows the user to study or qualify the data, if needed.
| |image16|
| === Diagnostic === This tab enables the user to check any anomaly detected by the BMS devices. Some of these diagnostic functions are cell overvoltage and undervoltage, open wire detection, and others.

Indicators:

-  Green color = passed (or no issue detected)
-  Red color = failed

| 
| |image17|

| 

--------------

Further Help
============

For questions and more information about this product, connect with us through the Analog Devices Engineer Zone.

.. hint::

   :ez:`EngineerZone Support Community <reference-designs>`


   | 
|

.. container:: center round box

   :doc:`➤ Go back to AD-BMSE2E3W-SL Hardware User Guide </wiki-migration/resources/eval/user-guides/ad-bmse2e3w-sl>`


| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/creating_myanalog_account.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/myanalog_account_entries.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/software_license_terms.png
   :width: 1000px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/gui_executable_file.png
   :width: 650px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/gui_installation.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/hex_file_to_daplink.png
   :width: 1000px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/background_script.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/home_landing_details.png
   :width: 1000px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/communication_jumper_selection.png
   :width: 300px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/communication_mode.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/reset_button_hardware.png
   :width: 500px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/setting_defaults.png
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/start_button.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_overview_page.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_graph_page.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_console_page.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/update_diagnsotic_page.png
