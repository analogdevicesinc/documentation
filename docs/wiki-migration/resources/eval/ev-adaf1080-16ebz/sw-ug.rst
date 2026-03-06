AMR Current Sensing Software User Guide
=======================================

Features
========

-  Data Visualization
   \* Data Logging
   \* Real-Time Data Capture
   \* Peripheral Configuration
   \* System Calibration

Software Requirement
====================

-  `NI LabVIEW Runtime 2019 <https://www.ni.com/en-ph/support/downloads/software-products/download.labview-runtime.html#301740>`__
-  `NI-488.2 Runtime 19.0 <https://www.ni.com/en-ph/support/downloads/drivers/download.ni-488-2.html#305442>`__
-  `NI-Serial Runtime 19.0 <https://www.ni.com/en-ph/support/downloads/drivers/download.ni-serial.html#305457>`__
-  `NI-VISA Runtime 19.0 <https://www.ni.com/en-ph/support/downloads/drivers/download.ni-visa.html#305862>`__

Hardware Requirement
====================

| AMR Current Sensing System
| \* Castor Sensor Board

-  Gemini Acquisition Board
-  5V Wall Adapter

| Standard USB A to Micro-B USB cable
| PC running Windows 10
| ======General Description====== This is the user guide describing the installation and use of the AMR Array Based Contactless Current Sensing Evaluation Software shown in Figure 1. The Castor and Gemini boards together make up an AMR array based contactless current sensing system shown in Figure 2. Please refer to the AMR Current Sensing User Guide for more detailed information on the hardware and its configuration. To operate the board, plug in the wall adaptor and press and hold the ON/OFF button for more than 1 second. The LCD will turn on and display measurement results. Connect the USB cable and launch the software (after installation procedure) to get started.

.. container:: centeralign

   \ |image1|\ *Figure 1. User Interface*


.. container:: centeralign

   \ |image2|\ *Figure 2. Gemini and Castor System*


Software Overview
-----------------

The AMR Array Based Contactless Current Sensing System can be controlled using the AMR Current Sensing software. The user interface enables peripheral configuration, real-time capture, and data logging of the AMR array based contactless current clamp. Calibration of the contactless current system can also be performed. There are two windows in the user interface:

-  Welcome Page
-  Main Page

On launching the software, the welcome page is first displayed. The welcome page ensures a valid connection between the PC and the evaluation board prior to moving to the Main evaluation user page. Figure 3 shows there three main functions of the user interface. Those are:

-  Device Configuration
-  Continuous Capture Mode
-  Device Data Capture
-  Real-time Data Capture
-  Calibration Mode

A detailed explanation on installation, the two windows, and the modes of operation will be given in the next sections.

.. container:: centeralign

   \ |image3|\ *Figure 3. user Interface Overview*


Getting Started
---------------

The following sections provide steps for installing the supporting software and an overview for connecting the evaluation board to the PC.

Software Installation Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Installing the AMR Current Sensing Installer**
| To install the AMR current sensing software, adhere to the following steps.

-  Navigate to the provided installation folder and extract if necessary.
-  Run the installer by double clicking setup.exe.

.. container:: centeralign

   \ |image4|\ *Figure 4. Installation Folder*


-  The screen in Figure 5 will be shown, intializing the installation.

.. container:: centeralign

   \ |image5|\ *Figure 5. Installer - Initializing Screen*


-  After the setup installer is initialized, the screen will update showing the default installation directory as seen in Figure 6. Click next to accept default or select an alternative location using the Browse… button. It is not recommended to install the software outside of the default folder.

.. container:: centeralign

   \ |image6|\ *Figure 6. Installer - Installation Directory Scree*


-  Click Next to accept installation of the AMR Contact Current Sensing application.

.. container:: centeralign

   \ |image7|\ *Figure 7. Installer - Start Installation Screen*


-  Click Next once the installer completes installation.

.. container:: centeralign

   \ |image8|\ *Figure 8. Installer - Complete Screen*


-  If asked, restart the computer to apply the dependencies installed.

Additional Software Installation Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The AMR Current sensing software uses LabView from National Instruments. The following National Instruments packages are installed and required to run. Runtime engines will be installed in the C:\\Program Files (x86)\\National Instruments\\ directory during installation of the application.
| The default destinations of other installed files are shown below for reference.
| Application Directory:

-  “C:\\Program Files (x86)\\ADI\\Contactless AMR Current Measurement\\Contactless AMR Current Measurement.exe”

Configuration Files Directory:

-  “C:\\ProgramData\\ADI\\Contactless AMR Current Measurement\\Configuration Files\\

Evaluation Hardware Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The AMR Array based contactless current sensing system can be connected via USB and the supplied power adaptor.
| **Connecting the Evaluation Hardware to a PC**
| To connect the evaluation board to a PC and measure a current. Refer to the AMR Current Sensing User Guide for specific details on the hardware.

-  Separate the Castor board.
-  Connect the Castor board to the Gemini Board.
-  Place the wire to be measured in the Castor board and reconnect the removable jaw and plastic spacers.
-  Plug in the wall adapter completely so that it is flush with the connector.
-  Press and hold the ON/OFF button for more than 1 second to power on.
-  The LCD will turn on and will start displaying the measurement results.
-  Connect the USB Cable.

| **Verifying Hardware Connections**
| Once the evaluation board is connected and powered, proper connection can be verified by taking the following steps.

-  Navigate to This PC in Windows Explorer.
-  Verify that DAPLINK (D:) is displayed per Figure 9. The drive letter D: may differ for each PC.

.. container:: centeralign

   \ |image9|\ *Figure 9. Verifying PC to Evaluation Board Connection*


The evaluation hardware can also be checked in the DEVICE Manager window under Ports (COM & LPT) as mbed Serial Port (COMXX), where XX will be a two digit number

.. container:: centeralign

   \ |image10|\ *Figure 9. Board Status Device Manager*


.. important::

   If the evaluation hardware is not detected as an "mbed Serial Port", install the driver from this website https://os.mbed.com/handbook/Windows-serial-configuration


Software Operation
~~~~~~~~~~~~~~~~~~

The following section describes the user interface in detail. **Running the Evaluation Software** After installation and hardware connection, the evaluation software can be launched in several ways.

-  Navigate to the destination folder of the software directory selected during the installation procedure and run the Contactless AMR Current Measurement.exe file.
-  Click Start > **Contactless AMR Current Measurement.exe**

Overview of the Welcome Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the application is launched, the welcome page is shown. This page shows if a valid connection is available between the PC and the AMR Current Sensing user interface. Figure 11 shows the welcome window and a description of each feature is described.

.. container:: centeralign

   \ |image11|\ *Figure 11. Welcome Window - Board not Detected*


-  COM Port, (Figure 11, Label 1). Shows a list of valid connections available to connect. The connections are validated using the interface name. The expected interface name is “mbed Serial Port”. Any port with this interface name will be chosen automatically and is displayed, for example, COM11 in Figure 13
-  Connection Status, (Figure 11, Label 2). This is a status indicator showing the current connection status between PC and the system.
-  Proceed (Figure 11, Label 3). This is the Proceed button, click on this button to proceed to the main page after a valid connection has been established.
-  Exit, (Figure 11, Label 4). Click on this button to close the application.

When the board is successfully connected to the user interface, the connection status will change as shown in Figure 12. Click the proceed button to move to the user main page.

.. container:: centeralign

   \ |image12|\ *Figure 12. Welcome Window - Board Connected*


Overview of the Main Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure 13 shows the main page of the user interface. The highlighted and labelled sections in this figure are explained below:

-  Connection Status, (Figure 13, Label 1), The connection status between PC and evaluation board is displayed as well as the COM port details. It also shows the current firmware version of the evaluation board connected. For example, CACM v3.1.0.0
-  Device Configuration, (Figure 13, Label 2), The device and peripheral configurations are listed under this section.
-  Device Data \| Real-Time Data Tabs, (Figure 13, Label 3). The device data tab (shown) presents the data from the evaluation board. In the Real-Time Data tab, the user will be able to see the instantaneous current plotted vs. time and the FFT of the most recent data capture.
-  Calibration Tab, (Figure 13, Label 4). This tab is used to view the system calibration factors, which include gain, null, offset, and gain factor. It allows the user to calibrate the gain factor as well.
-  Software Name & Version, (Figure 13, Label 5). The software name and version information are displayed here. E.g. 3.1 is the version of the user interface software in Figure 13.
-  Logging, (Figure 13, Label 6). All the data transferred from the hardware system can be logged to an external file (.csv). The file location and size/capture duration can be controlled and triggered from this section. See the Data Logging section for more information.
-  Capture, (Figure 13, label 7). The capture button can be used to start or pause data transfer to the user interface from the system hardware.

.. container:: centeralign

   \ |image13|\ *Figure 13. Main Window Overview*


Software Modes
--------------

There are three main types of operations in the user interface. Those are:

-  Continuous Capture Modes
-  Calibration Mode
-  Device Configuration

Continuous Capture Modes
~~~~~~~~~~~~~~~~~~~~~~~~

The user interface is capable of continuously capturing the device data as well as the raw data. There are multiple features available to analyze the data captured. There are two modes of capture available. They are:

-  Device Data Mode
-  Real-Time Data Mode

Device Data Mode
^^^^^^^^^^^^^^^^

In device data mode, the application will capture the calculated current and frequency values from the MCU.

-  DC Amps, (Figure 14, Label 1). The latest DC current(A) sent by the evaluation board is displayed here. There is also a graph to the right of the display which gives the graphical representation of the current value captured from the board over time.
-  AC Amps, (Figure 14, Label 2). The latest AC current (Arms) sent by the evaluation board is displayed here. There is also a graph to the right of the display which gives the graphical representation of the current value captured from the board over time.
-  AC Freq, (Figure 14, Label 3). The latest AC frequency (Hz) sent by the evaluation board is displayed. AC Freq also has a graphical display.
-  Temperature (Figure 14, Label 4) The current temperature (Celsius) from the ADT7420 is displayed here for reference.
-  Read Raw Data, (Figure 14, Label 5). This option enables transfer of the raw ADC sample data to the user interface. The data is not displayed, however, the “Log data” option can be used to export the captured raw data. See the Data Logging section for more information on this feature.
-  Autoscale, ( Figure 14, Label 6). Enabling this option forces all the graphs to auto scale based on the values captured.
-  Capture, (Figure 14 Label 7). This button is used to pause/restart the continuous capture. The graphs no longer update once the capture is paused, which makes it possible to analyze the data already present within the window.
-  Sampling Frequency (Hz), (Figure 14, Label 8). This configures the sampling rate of the ADC capturing the sensor array output. The default is 10kHz.
-  Graph Controls, (Figure 14, Label 9). Options to move the graph scale, zoom in/out of a section of the graph, and move the X and Y cursor to see the value at any specific point. The cursor current positions are also displayed.

Real-Time Data Mode
^^^^^^^^^^^^^^^^^^^

In real time data mode, the application will capture and display the raw data from the evaluation board, calculate the instantaneous current and display it. The ADAF1080 flipping control is disabled in this mode. Refer to ADAF1080 datasheet or the AMR Current Sensing User Guide for details on flipping.

-  Instantaneous Current, (Figure 15, Label 1) – Calculated current from raw ADC samples. Unlike the device tab, this data is calculated by the user interface based on the samples captured and the calibration settings. 1000samples are captured at 10kHz every 200ms.
-  FFT, (Figure 15, Label 2). The FFT of the raw data is calculated for the last set of captured data and displayed for analysis.
-  Autoscale, (Figure 15, Label 3). Enabling this option makes all the graphs auto scale based on the values captured.
-  Capture, (Figure 15, Label 4). This option is used to pause/restart the continuous capture. The graphs no longer update once the capture is paused, which makes it possible to analyze the data already present within the window.
-  Sampling Frequency (Hz), (Figure 15, Label 5). This configures the sampling rate of the ADC capturing the sensor array output. The default is 10kHz.
-  Graph Controls, (Figure 15, Label 6). Options to move the graph scale, zoom in/out of a section of the graph, and move the X and Y cursor to see the value at any specific point. The cursor current positions are also displayed.
-  Calculated Frequency, (Figure 15, Label 7) The frequency is calculated from the FFT for the last set of samples captured and displayed.

.. container:: centeralign

   \ |image14|\ *Figure 15. Real-time Data Capture*


Sampling Frequency
^^^^^^^^^^^^^^^^^^

The system timing is based on a division of the MCU clock. The sensor array is sampled at 10kHz. For input signals where a frequency is not detected or below the system threshold a warning indicator is shown to the right AC Freq text as can be seen in Figure 16.

.. container:: centeralign

   \ |image15|\ *Figure 16. AC Frequency & Warning Indicator*


Calibration Mode
~~~~~~~~~~~~~~~~

In the calibration tab, the AC Null, DC Null, offset, gain, and gain factor are displayed. It also contains a gain factor calibration wizard to calibration the system based on a known input current.

-  Calibration Refresh, (Figure 17, Label 1). While the data in this tab is refreshed each time it is opened, pressing this will also refresh the calibration values from the Gemini system. This feature is helpful after the NULL button is pressed while this tab is open.
-  AC Null, (Figure 17, Label 2). This value shows the AC Null value for the sensor array.
-  DC Null, (Figure 17, Label 3). This value shows the DC Null value for the sensor array.
-  Offset, (Figure 17, Label 4). This is the offset in LSB of the sensor array output.
-  Gain, (Figure 17, Label 5). The temperature compensation gain value is displayed here.
-  Gain Factor, (Figure 17, Label 6). The overall system Gain factor is shown here.
-  Calibration Type, (Figure 17, Label 7). The calibration type denotes the type of current which we are going to calibrate against. It is either AC or DC.
-  Calibration Current, (Figure 17, Label 8). Applied calibration current for calibration algorithm. This value is used in the calibration sequence to set the current gain factor.
-  Calibrate, (Figure 17, Label 9). Clicking the calibrate button will calibrate the board for the calibration current value provided. After calibration, the gain factor value will be updated with the new calculated one

.. container:: centeralign

   \ |image16|\ *Figure 17. Calibration Mode Tab*


Device Configuration
~~~~~~~~~~~~~~~~~~~~

There are several configuration settings available in the Gemini user interface to enable or disable certain peripherals and controls. Figure 18 shows the device configuration options.

-  Use LCD, (Figure 18, Label 1). Used to enable/disable the LCD display. By default, this is enabled.
-  Enable LED Blacklight, (Figure 18, Label 2). Used to enable/disable the LCD backlight. This option will be available only when the LCD is enabled and is on by default.
-  Use Bluetooth, (Figure 18, Label 3). This feature is currently not supported in software. It used to enable/disable the Bluetooth communication.
-  Enable Temperature, (Figure 18, Label 4). Used to enable/disable the temperature sensor.
-  Enable Cloud Sync, (Figure 18, Label 5). This feature is available at request. It enables data synchronization to a cloud logging and display service. Contact ADI for further details.

.. container:: centeralign

   \ |image17|\ *Figure 18. Device Configuration Details*


Data Logging
~~~~~~~~~~~~

The logging feature is available to log the captured data (both device and real-time data) from the evaluation board to an external file at a location selected by the user. Figure 19 shows details of the data logging page. The following is a description of the feature at each labeled point:

-  Log Data, (Figure 19, Label 1). Starts logging of data.
-  Logging Options, (Figure 19, Label 2). Opens a window to configure the settings for logging and start if needed.
-  Save Directory, (Figure 19, Label 3). The save directory location for logging. The default save directory is shown. C:\\ProgramData\\ADI\\Orion\\Data Log.
-  Finite Check Box, (Figure 19, Label 4). The logging can be done for a finite interval of time(seconds) or will be file size limited. The default file size is 1MB.
-  Time \| File Size, (Figure 19, Label 5). This input is taken as seconds for finite logging or file size limit for infinite logging
-  Start Logging, (Figure 19, Label 6). Applies the configurations, starts the logging, and closes the window.
-  Apply, (Figure 19, Label 7). Applies the configurations and closes the window.
-  Cancel, (Figure 19, Label 8). Discards any changes not applied and closes the window.

.. container:: centeralign

   \ |image18|\ *Figure 19. Data Logging Window*


Device Data Logging Format
^^^^^^^^^^^^^^^^^^^^^^^^^^

Logged data will be stored in a comma separated format. Once logging is enabled the following files and results will be created:

-  File Names, (Figure 21, Label 1). A new file will be created with format “DeviceData <Date> <Time>.csv” in the location specified in the logging configurations window. If read raw data option was enabled during the logging, then a folder with format “RawData <Date> <Time>.csv” will also be created.
-  Device Data, (Figure 21, Label 2). The device data is logged with the time in the .csv file. Device data files include a time stamp, DC/AC Amps data, the calculated frequency and temperature
-  Raw Data File Location, (Figure 21, Label 3). If the read raw data option was selected, the raw data file location is also logged in the device data for reference.
-  Raw Data File Name, (Figure 21, Label 4).The format of the raw data file logging is “Raw_Data\_<Time in device data file>.csv”

Raw Data Logging Format
^^^^^^^^^^^^^^^^^^^^^^^

The raw data file format is shows in Figure 20. The raw data log includes the parameters seen in the calibration tab as well as details on firmware version and the sampling rate selected. Each file contains one ADC acquisition sequence with a total of 1000 sampled points each for the positive and negative flip phases, as well as a time stamp for each data point. Each raw data file corresponds to a results row in the device data .csv results.

.. container:: centeralign

   \ |image19|\ *Figure 20. Raw Data File & Format*


.. container:: centeralign

   \ |image20|\ *Figure 21. Device Data Log*


Real-Time Data Logging Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If data logging is performed in the real-rime data tab, a new file will be created. It has a similar format to the raw data of the device data options. Note that flipping is disabled in real-time data mode so only one set of raw ADC samples is shown. The instantaneous current is calculated by the GUI based on the sample set and the calibration parameters stored on the MCU. Figure 22 shows a sample file format and sample real-time data set. When the Log Data button is pressed, or Start Logging is pressed from the Log Configurations window the following occurs:

-  Real-Time Data file creation, (Figure 22, Label 1). A new file will be created with format “RealTimeData <Date> <Time>.csv” in the location specified in the logging configurations window.
-  Real-Time data file format, (Figure 22, Label 2). A .csv file including calibration parameters are logged for reference as well as the sampling rate. The raw ADC samples and the calculated instantaneous current are logged and time stamped.

.. container:: centeralign

   \ |image21|\ *Figure 22. Real-Time Data File & Format*


Troubleshooting
---------------

**Cannot connect to board in the welcome screen:**

-  Ensure board is powered and appears as:

   -  DAPLINK in Windows Explorer.
   -  mbed Serial Port (COMXX) in device manager.

-  Try alternative USB cable or port.
-  Confirm jumper connections on Gemini board & Castor board are in correct positions.

**Performance, error >1% over full range:**

-  Are plastic spacers installed?
-  Recalibrate at 50A, Gain Factor should be ~0.38-0.39.
-  Check for stray field – Note, 40dB rejection at clamp edge.
-  Was the Null performed with a current present or a coil within the clamp.

   -  AC Null should be zero.
   -  DC null is typically <10

**Calibration Failed in GUI** Default is 50A but it may need to retyped on first attempt to initialize the variable. Retype variable into Current(A) and retry

Other Information
-----------------

-  `Main Page <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz`>`__
-  `Quick Start Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/quick-start`>`__
-  `Hardware User Guide <:doc:`/wiki-migration/resources/eval/ev-adaf1080-16ebz/hw-ug`>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/ev-adaf1080-16ebz_kit_top2a.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw3.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw4.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw5.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw6.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw7.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw8.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw9.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw10.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw11.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw12.png
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw13.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw15.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw16.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw17.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw18.png
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw19.png
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw20.png
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw21.png
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/sw22.png
