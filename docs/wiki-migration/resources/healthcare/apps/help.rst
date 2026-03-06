Help
====

`ADI Study Watch - User Guide <https://wiki.analog.com/_media/resources/healthcare/apps/adistudywatch_usersguide.pdf>`__

Introduction
------------

This document is a getting started guide for the users to know about the ADI Study Watch application. The document explains how to use the different views of the application. The application is used for validating the study watch.


|image1|

BLE Connection
--------------

The app needs Bluetooth support to connect to the watch. The communication between watch and the application is done through BLE connectivity. Steps to connect the watch to the application is explained below.

Connection
~~~~~~~~~~

-  Once the app is opened, the user could see the ble connection page. Press the Bluetooth button to scan for the available devices.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/2-connection.png
   :align: center
   :width: 200px

-  After pressing the button, the app will check if Bluetooth and Location is enabled in the device or not. If it is not enabled, it will alert the user to enable the Bluetooth and the location. If Bluetooth and location is already enabled, it will directly move to the scan page.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/3-connerrors.png
   :align: center
   :width: 400px

-  Once the Bluetooth is enabled, the app will start scanning for the devices. The devices found will be listed out in the screen. If devices are not found it will give the warning message to the user. The user can click on the refresh button to scan again.
-  After the devices are listed, the user can click on the connect button to connect with the watch.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/5-devfound.png
   :align: center
   :width: 200px

-  Once the device is connected, it will move to dashboard page by initializing the basic settings.

Disconnection
~~~~~~~~~~~~~

-  User can click on the disconnect button on the dashboard to get disconnected from the watch.
-  If user click on the disconnect button when stream is running ,the app will alert the user to stop streaming in dashboard.

Evaluating the Watch
--------------------

Dashboard
~~~~~~~~~

Dashboard is the page where the user can see the sensors that are supported by the device. In dashboard, the app will display the result of the sensors. Dashboard supports the following sensors PPG, ECG, EDA, Temperature, ADPD led Green/Red/IR/Blue. Dashboard also supports the user to connect to the reference watches.

Start Sensor
^^^^^^^^^^^^

-  Once the watch is connected, User can start the sensor by clicking on the switch to ON side
-  Once the sensor is started, it will display the result of the sensor on that dashboard
-  User can see the result of this sensor in chart page.
-  User can start only one sensor in the dashboard. If user try to start the second sensor, the app will alert the user that the sensor cannot be started.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/7-enstream.png
   :align: center
   :width: 200px

Stop Sensor
^^^^^^^^^^^

-  If the sensor is ON, then Click on the switch to Off side to stop it.
-  This would stop the streaming of data from the watch

Charts
~~~~~~

Chart page displays the result of each sensor in the graphical form. It also displays the current sample rate of the sensor.

-  Click on the chart icon at the bottom tab to move to the chart page.
-  If no VSM signal is selected, the chart will display that there is no data available.
-  If any of the VSM signal is selected, it will automatically displays the result of that application in the form of plots. Below you can see the example of PPG , ECG and ADPD chart.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/8-charts.png
   :align: center
   :width: 400px

-  User can change the graph settings in the settings page.

Logging
~~~~~~~

In Logging page user can log the sensor data. The logs that are selected will be stored inside the watch. The logs can be retrieved using the desktop tool *Applications Wavetool*. Logging helps in collecting and validating data of each sensor. The application allows two ways of logging.

Single View Logging
^^^^^^^^^^^^^^^^^^^

In single view logging, user can select the sensor of their own choice for logging.

-  Click on the log icon at the bottom tab to move to logging page.
-  Click on *SingleView* tab at top of the page.
-  Select the sensor that need to be logged

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/9-logging.png
   :align: center
   :width: 200px

-  Now click on the *Start Log* button to start logging. The app will check for the memory available device.
-  It will display the pop up to enter the participant id. Enter the id and click ok to continue logging.
-  Now the log will be automatically be saved into the watch device (NAND flash)
-  If the users wants to see the logging data, they can start the sensor in dashboard and can view real-time plots in chart page.
-  If user wants to stop the log, they can simply click on the stop log button.

Multi-View Logging
^^^^^^^^^^^^^^^^^^

In Multiview logging, there are use cases in which each sensor is configured with different sample rate. The logging of each sensor will be saved with those configuration setting.

-  Click on the log icon at the bottom tab to move to logging page.
-  Click on Multiview tab at top of the page.
-  Click on the respective use case switch button that need to be logged.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/10-mvlogging.png
   :align: center
   :width: 200px

-  It will display the pop up to enter the participant id. Enter the id and click ok to continue logging.
-  Now the log will be automatically saved into the device.
-  User can click on the selected use case switch button to stop the log.
-  Once the Multiview logging is enabled, user is not allowed to enable stream in dashboard or log data in the *SingleView* tab.

Settings
~~~~~~~~

In settings page, user can change the sensor configuration, change the graph duration and can filter the sensor data.

Load Configuration
^^^^^^^^^^^^^^^^^^

-  By default no file will be selected, so the sensors are started with the default configuration.
-  If the user wants to load different configuration, they can click browse button to select the respective configuration file.
-  If they want to reset to default configuration, they can click on the reset config button

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/11-loadconfig.png
   :align: center
   :width: 200px

Filter Selection
^^^^^^^^^^^^^^^^

The application supports filtering option for PPG and ECG. It filters the raw data of the sensor.


|image2|

Plot Duration
^^^^^^^^^^^^^

This setting enables user to change the real time plot duration (x-axis)


|image3|

Firmware Upgrade
----------------

The application can upgrade the firmware of the watch. Follow the below steps to upgrade the firmware

-  Open the application and click on the firmware upgrade button.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/14-fwupgrade1.png
   :align: center
   :width: 200px

-  The application will display a message to set the device to bootloader mode.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/14-fwupgrade2.png
   :align: center
   :width: 200px

-  Once the watch is set to the bootloader mode, the device will be listed on the page for upgradation.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/14-fwupgrade3.png
   :align: center
   :width: 200px

-  Click on the upgrade button to start updating the firmware. It will move to the upgradation page.
-  User can see the default binary that comes with the application. Clicking on update button will update the watch with default firmware.
-  To load a different firmware click on browse button and the choose the firmware that needs to be loaded.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/14-fwupgrade4.png
   :align: center
   :width: 200px

-  It will now show the selected firmware name and its size. Clicking on update button will update the watch with the selected firmware
-  Once the upgradation is completed, it will display the completion process with OK button. Click OK button to move back to connection page.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/14-fwupgrade5.png
   :align: center
   :width: 400px

Reference Watch Connection
--------------------------

The application supports the connection of reference watch. It helps to compare the HeartRate of Study watch and the reference watch. Steps to connect the reference watch is listed below,

-  Click on connect button next to the Ref HR label.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/15-refdev1.png
   :align: center
   :width: 200px

-  The view will display all the reference watches that are able to send HearRate data.
-  Click on connect button to connect the reference watch.
-  Once the device is connected, it will display the connected status.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/15-refdev2.png
   :align: center
   :width: 200px

-  Click OK button to go to dashboard. User can see the reference HeartRate in the dashboard

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/15-refdev3.png
   :align: center
   :width: 200px

Miscellaneous
-------------

Device Information
~~~~~~~~~~~~~~~~~~

-  Click on the action button displayed on the dashboard.
-  Select the DeviceInfo option.
-  It will display the device information like Firmware info, File memory status and hardware id of the device.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/16-devinfo.png
   :align: center
   :width: 200px

About Page
~~~~~~~~~~

-  Click on the info button on connection page to see the information of the application.
-  In the *About* page, the basic information of the application like version number, license agreement file and help page are displayed.

.. image:: https://wiki.analog.com/_media/resources/healthcare/apps/17-about.png
   :align: center
   :width: 200px

.. |image1| image:: https://wiki.analog.com/_media/resources/healthcare/apps/1-intro.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/healthcare/apps/12-filtersett.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/healthcare/apps/13-plotduration.png
   :width: 200px
