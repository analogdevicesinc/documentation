Software User Guide
===================

Requirements
------------

*  Host PC (Windows 10 or later)

   * with administrator and internet access
   * 1920 by 1080 or greater screen resolution, recommended

The **AD-BMSE2E3W-SL GUI** also referred as the **Light EV BMS GUI** is a PC-based Graphical User Interface (GUI) tool designed to work in conjunction with the AD-BMSE2E3W-SL board.

**MyAnalog.com account is required to download the software**.

Follow the steps below to create a MyAnalog account:

#. Go to :adi:`MyAnalog </>`  and create an account using email. Select the **Register with email** option to get started.

#. Once you have a MyAnalog account, log in to :adi:`MyAnalog </>` using your credentials.

Request for Software Access
---------------------------

.. note:: Send the following details to this email address to request for software access:

   **LEV_CSESupport@analog.com**

   * MyAnalog email address
   * Company
   * Country
   * Purpose/Projects

Software Download
-----------------

#. Download from: `AD-BMSE2E3W-SL Version 1.0.0 <https://download.analog.com/secure/bms-cse-solutions/e2e3w-00/1-0-0/ad-bmse2e3w-sl-rel1.0.0.exe>`_

#. You will be directed to the *Software Package Download* page. Tick the checkbox and click the **I Accept** button to indicate acceptance of the license agreement.

#. Click the ``Download`` button to download the installer.

.. note::

   When software updates or new versions of the software are available, Analog Devices sends a notification to the email address associated with the MyAnalog account used to download the original software package.

GUI Installation
----------------

#. Double-click on **ad-bmse2e3w-sl-rel1.0.0.exe** to install the program to your computer.

   .. figure:: gui_executable_file.png

      AD-BMSE2E3W-SL-Rel1.0.0 Installer File

#. Accept the license terms and click *Next* to proceed with the installation. The default installation directory is in ``C:\Analog Devices\``

  .. figure:: gui_installation.png

      License Terms and Agreement

#. Locate the **light_ev_bmsv1.0.0.hex** file inside the AD-BMSE2E3W-SL installer files folder.

   ``C:\Analog Devices\AD-BMSE2E3W-SL-Rel1.0.0\Software\Firmware``

   .. figure:: firmware_location.png

      Firmware Location inside the Installer Files Folder


#. Drag and drop the .hex file into the DAPLink drive to flash the program on the MCU.

   .. figure:: hex_file_to_daplink.png

      Drag-and-drop HEX to DAPLink Drive


#. Find the **Light_EV_BMS_GUI.exe** file inside the AD-BMSE2E3W-SL installer files folder.

   ``C:\Analog Devices\AD-BMSE2E3W-SL-Rel1.0.0\Software\GUI\Light_EV_BMS_GUI_v1.0.0``

   .. figure:: gui_executable_file_location.png

      Installer File Location

#. Double-click the **Light_EV_BMS_GUI.exe** file to open the program. You should see a script running in the background separately and the landing page running in the browser.

   .. figure:: background_script.png

      Background Script

   .. figure:: home_landing_page.png

      GUI Landing Page

Interface Setup
---------------

.. figure:: home_landing_details.png

   Landing Page Menu

.. csv-table:: Details Available on the Landing Page
  :file: landing-page.csv
  :widths: 10, 20, 70
  :header-rows: 1

#. Set the jumper configuration based on the communication mode being used: UART or CAN.

   .. figure:: communication_jumper_selection.png

      Selecting the Communication Mode

   On the GUI landing page, hover to the *Communication Mode* dropdown menu. Select **UART COM** followed by the specific port number if using UART, or **CAN** if using CAN.

   .. figure:: communication_mode.png

      Communication Mode Menu


   Press the ``RESET`` button every time the hardware set up is changed.

   .. figure:: reset_button_hardware.png

      RESET Button


#. Click the ``Load Defaults`` button to set the initial entry values for the different parameters needed for the State of Charge (SoC) and State of Health (SoH) calculations.

   .. figure:: setting_defaults.png

      Loading Default Settings


#. Click the ``Start`` button to begin the measurements.

   .. figure:: start_button.png

      Start Button

Tabs
----

Overview
^^^^^^^^

The Overview tab features plots for stack voltage, module current, max charge current, max discharge current, cell voltages, cell temperatures, and state of the battery. This tab also allows setting of the vehicle state, which by default is set to "PARKED".

.. figure:: update_overview_page.png

   Overview Tab

Graph
^^^^^

The Graph tab enables checking the progression of the readings for different parameters such as the cell voltage, temperature, SoC, SoH, and pack voltage and current.

.. figure:: update_graph_page.png

   Graph Tab

Console
^^^^^^^

Presents the actual numerical data being fetched by the UI in a tabular form. This tab allows the user to study or qualify the data, if needed.

.. figure:: update_console_page.png

   Console Tab

Diagnostic
^^^^^^^^^^

This tab enables the user to check any anomaly detected by the BMS devices. Some of these diagnostic functions are cell overvoltage and undervoltage, open wire detection, and others.

Indicators:

* Green color = passed (or no issue detected)
* Red color = failed

 .. figure:: update_diagnsotic_page.png

   Diagnostics Tab

