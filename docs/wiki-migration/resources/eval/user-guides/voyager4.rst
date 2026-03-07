Voyager 4 - Wireless Motor Monitoring Development Platform
==========================================================

Version 1.2
-----------

============= ==========
Created       22/09/2023
Last Modified 13/08/2025
============= ==========

--------------

0. Available Resources
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                          | Details                                                                                                                                                              | Where can I find this?                                                                                                                                        |
+===============================+======================================================================================================================================================================+===============================================================================================================================================================+
| Voyager4 Wiki (this document) | Good overview webpage that describes the Voyager4 project and contains links to all available resources                                                              | -                                                                                                                                                             |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EV-CBM-VOYAGER4-1Z Web Page   | EV-CBM-VOYAGER4-1Z page on Analog website where Voyager4 kits can be purchased                                                                                       | :adi:`EV-CBM-VOYAGER4-1Z Evaluation Kit <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/voyager4.html#eb-overview>`                     |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Voyager4-Quick_Start_Guide    | Short document describing only the steps needed to quickly get set up and begin plotting data using the Voyager4                                                     | Software Distribution Package (contact Project contacts)                                                                                                      |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Voyager4-User_Guide           | In depth document with background on the Voyager project, including use of BLE, advanced project setup and instructions on developing the project for your own needs | Software Distribution Package                                                                                                                                 |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Voyager4-Developers_Guide     | In depth software and firmware discussion, including block diagrams of operation, for those looking to add to the project                                            | Software Distribution Package                                                                                                                                 |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Project Contacts              | Central Apps                                                                                                                                                         | For more information on Voyager, please contact your local ADI sales team                                                                                     |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

*Table 1. Available Resources*

--------------

Table of Contents
~~~~~~~~~~~~~~~~~

= ============================
0 Available Resources
1 Introduction
2 Powering Up
3 Using the BLE Adapter
4 Running the GUI
5 Using the GUI
6 Saving Data
7 Make your first AI Inference
= ============================

--------------

1. Introduction
~~~~~~~~~~~~~~~

This is a Quick Start guide containing simple instructions to quickly evaluate Voyager4 Motor Monitoring Platform (EV-CBM-VOYAGER4-1Z) by visualizing and exporting 3-axis accelerometer data to a .csv file.

Prerequisites
^^^^^^^^^^^^^

-  Voyager4 Module.
-  PC with Bluetooth Adapter (or External Bluetooth Adapter).
-  Graphical User Interface (GUI) python code.

| 
| |Voyager Module|
| *Fig 1. Voyager4 Module*
| |Voyager4 GUI|
| *Fig 2. Voyager4 Graphical User Interface (GUI)*

--------------

2. Powering Up
~~~~~~~~~~~~~~

| With the Voyager4 (EV-CBM-VOYAGER4-1Z) fully assembled in hand:
| \* Remove the top acrylic part (lid).
| |Remove the Lid|
| \* Remove the cylinder part (body).
| |Remove the Body|

-  Connect the battery to the power board.
   |Unconnected Battery| |Connected Battery|
-  Connect Voyager4 to the PC using the USB Cable
   |Unconnected Voyager| |Connected Voyager|
-  The leftmost LED should perform one long blink and 3 short blinks upon successful startup. The LED will then remain OFF when the Voyager is running.

|Powered on Voyager|

   Voyager4 is running. The USB cable must be disconnected.

.. note::

   The USB cable **must be connected** to the Voyager **when powering or restarting it**, even if you plan on using the Voyager in wireless mode using the battery. This connection to the PC enables the correct power paths in the device for use with the battery.


--------------

3. Using the BLE Adapter
~~~~~~~~~~~~~~~~~~~~~~~~

A BLE 5.3 Adapter with Antenna is included in every Voyager4 kit. Voyager4 uses BLE (Bluetooth Low Energy) which makes it compatible with any PC with a Bluetooth Radio, but to ensure optimal performance and range, using the adapter when communicating with Voyager4 is recommended. On Windows, the default BLE drivers must be disabled to enable the use of the adapter.

.. warning::

   Enabling the BLE Adapter will disable the default Bluetooth drivers on your PC. You will need to re-enable them to ensure your PC’s Bluetooth operates correctly when the adapter is removed.


-  Plug the provided BLE Adapter into your PC



|Attached BLE Adapter|

   \* Open Device Manager (on Windows, Control Panel -> Hardware and Sound -> Device Manager. You may need administrator privileges to access this.

   |Devices and Printers|

   \* Confirm that the driver for the BLE Adapter was successfully installed automatically (Generic Bluetooth Adapter).

   |Generic Bluetooth Adapter Driver|

| 
| \* Right Click and disable the default Bluetooth Driver -> Intel® Wireless Bluetooth. You may need to turn off your PC’s Bluetooth first.
| |Disable Intel Wireless Bluetooth|
| \* Restart your PC. The driver has been successfully installed, and the adapter has replaced the default Bluetooth functionality of your PC.

.. warning::

   Remember to reenable the default Bluetooth driver for your PC when the BLE Adapter is removed.


--------------

4. Running the GUI
~~~~~~~~~~~~~~~~~~

For details on the software download of the project, please reach out to contacts in Section 0. Available Resources.

-  If you are an experienced Python user, you can simply run main.py after installing python ≥3.7 and installing the required packages using requirements.txt. Use of a virtual environment is recommended.
-  If you do not have python experience, the most reliable way to run the source code is via command prompt, so the recommendation is to use Miniconda.
-  Install python’s latest package (3.7 or later).
-  Download and install the latest miniconda.
-  Search for Anaconda Prompt (Miniconda) and open it.

|Launch Anaconda Environment|

   \* Type in ``conda create --name voy4_env python=3.7``.
-  This will create a virtual environment to run the GUI. Please note the double dash (- -) ahead of name.
-  Type in ``activate voy4_env``.

|Create and Start Anaconda Environment|

   \* cd into the directory where main.py is.
-  Example: ``cd C:\voy4\GUI\voyager4-gui``.
-  Type in ``pip install -r requirements.txt``. This will install all necessary packages.
-  Type in ``python main.py``. This should run the main.py script, prompting the GUI

|Default GUI, Unconnected|

.. note::

   Miniconda was chosen here as it allows us to specify not just the packages being installed but also the version of Python to be used, to eliminate confusion in Python versioning.


--------------

5. Using the GUI
~~~~~~~~~~~~~~~~

-  Click scan to search for nearby devices.


|GUI Scan to Connect|

   \* A Voyager device should appear under Available Devices.

   |GUI Available Devices|

-  **Double-click** the listed device to highlight its text.

|GUI Selected Device Entry|

   \* Click **"Connect"**.
-  The device Connected status changes to **“Connected: True”**. This may take several minutes depending on the strength of connection.

|GUI Connected to Device|

   \* Under **BLE Operations**, click the drop-down menu.

   -  Select **“setphy”**.
   -  Click **“Send”** to send the default value of **2**.

   |Issue Setphy 2 Command|

      \* Device Status displays “Return Value: OK”.

      |GUI Device Status OK|

| 
| \* Under BLE Operations, click **"Start"**
| |GUI Start Command|
| \* You should see data for 3-axis vibration data being plotted on the Canvas Frame.
| |GUI with accel data|

--------------

6. Saving Data
~~~~~~~~~~~~~~

-  To save data, simply click “Enable Save”.


|GUI Saving Data disabled|

   \* The label changes to “Saving Enabled”.

   |GUI Saving Data Enabled|

   \* Any data that is plotted will now also be saved as a CSV.

   |GUI Data Saving|

.. note::

   Plotting and saving occur simultaneously. Each plot is saved to its own CSV file. The name includes the timestamp and data on which the data was saved, along with information about the accelerometer mode. Saved data appears in the same folder as the GUI.


| 
| \* Press Start to begin the flow of data and save your first CSV.

--------------

7. Make your first AI Inference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Voyager4 comes packaged with a second microcontroller, the MAX78000, which can make low power AI inferences with an edge AI model. For more information on developing / deploying your own model, please consult the other documents mentioned in Available Resources. Voyager4 comes preloaded with a motor fault model that was trained on an example ADI motor. This is not adaptable to new motor types but can be used to showcase the basic operation of the MAX78000.

-  By default, the MAX78000 is unpowered. Enter the command “wake78000” with default value 1 to wake the MAX78000 and automatically begin an inference.


|GUI Wake78000|

   \* A reconstruction error is displayed in the device status.

   |GUI Reconstruction Error|

.. note::

   The reconstruction error is a percentage indicating how similar current data is to training data. If the Voyager is below a vibration threshold, the MAX78000 instead returns all zeros to indicate that the Voyager is not moving.


-  Click “Auto Detect” to move to the Fault Detection tab.



|GUI Auto Detect Tab|

   \* If the returned fault detection value is above the threshold, a “Motor Fault” status is displayed.

   |GUI Default Motor Detect|

   \* If the returned fault detection value is above the threshold, a “No motor fault detected” is displayed.

   |GUI Motor Fault Detected|

   \* The Reconstruction Threshold can be adjusted by entering a new value in the textbox or by adjusting the slider.
-  7. You can also press “Start Inference” which will automatically send a “wake78000 1” command and issue an inference.
-  8. If the Repeat Inference is enabled, it periodically runs an inference, goes to sleep, disconnects, wakes up after the defined period, reconnects, and repeats this sequence until the Repeat Inference checkbox is unchecked.

| 
| |GUI Motor Off|

.. |Voyager Module| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_1_voyager_module.svg
.. |Voyager4 GUI| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_2_voyager4_graphical_user_interface_gui_.svg
.. |Remove the Lid| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_3_remove_the_lid.svg
.. |Remove the Body| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_4_remove_the_body.svg
.. |Unconnected Battery| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_5_unconnected_battery.svg
   :width: 200px
   :height: 200px
.. |Connected Battery| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_6_connected_battery.svg
   :width: 200px
   :height: 200px
.. |Unconnected Voyager| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_7_voyager_not_connected_to_pc.svg
   :width: 200px
   :height: 200px
.. |Connected Voyager| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_8_voyager_connected_to_pc.svg
   :width: 200px
   :height: 200px
.. |Powered on Voyager| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_9_powered_on_voyager.svg
   :width: 200px
   :height: 200px
.. |Attached BLE Adapter| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_10_attached_ble_adapter.svg
   :width: 300px
   :height: 300px
.. |Devices and Printers| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_11_devices_and_printers.svg
.. |Generic Bluetooth Adapter Driver| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_12_generic_bluetooth_adapter_driver.svg
.. |Disable Intel Wireless Bluetooth| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_13_disable_intel_wireless_bluetooth.svg
.. |Launch Anaconda Environment| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_14_launch_anaconda_prompt.svg
.. |Create and Start Anaconda Environment| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_15_create_and_start_anaconda_environment.svg
.. |Default GUI, Unconnected| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_16_default_gui_unconnected.svg
.. |GUI Scan to Connect| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_17_gui_scan_to_connect.svg
.. |GUI Available Devices| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_18_gui_available_devices.svg
.. |GUI Selected Device Entry| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_19_gui_selected_device_entry.svg
.. |GUI Connected to Device| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_20_gui_connected_to_device.svg
.. |Issue Setphy 2 Command| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_21_issue_setphy_2_command.svg
.. |GUI Device Status OK| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_22_gui_device_status_ok.svg
.. |GUI Start Command| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_23_gui_start_command.svg
.. |GUI with accel data| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_24_gui_with_accel_data.svg
.. |GUI Saving Data disabled| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_25_gui_saving_data_disabled.svg
.. |GUI Saving Data Enabled| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_26_gui_saving_data_enabled.svg
.. |GUI Data Saving| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_27_gui_Data_saving.svg
.. |GUI Wake78000| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_32_gui_wake78000.svg
.. |GUI Reconstruction Error| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_28_gui_reconstruction_error.svg
.. |GUI Auto Detect Tab| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_29_gui_auto_detect_tab.svg
.. |GUI Default Motor Detect| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_30_gui_default_motor_detect.svg
.. |GUI Motor Fault Detected| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_31_gui_motor_fault_detected.svg
.. |GUI Motor Off| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fig_33_gui_motor_off.svg
