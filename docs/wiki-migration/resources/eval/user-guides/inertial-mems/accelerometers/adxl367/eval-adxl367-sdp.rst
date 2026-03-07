-- EVAL-ADXL367-SDP User Guide --
=================================

FEATURES
--------

-  Flexible inertial sensor evaluation platform
-  Controller board and interface board operate with interchangeable evaluation boards
-  Separates device under test (DUT) from controller for accurate environmental testing
-  Save data to file
-  Standard USB cable for power and communications
-  PC-based graphical user interface (GUI)
-  Fast, easy installation

GENERAL DESCRIPTION
-------------------

The EVAL-ADXL367-SDP hardware is shown in the below.


|image1|

The EVAL-ADXL367-SDP includes the following components:

-  **EVAL-SDP-CB1Z:** also called "SDP-B" is part of the Analog Devices system demonstration platform (SDP). SDP controller boards provide the means for communicating with the ADXL367 from the PC.
-  **EVAL-SDP-INTER4-Z:** is an SDP interface board. This board serves as an interposer between the SDP controller board and the evaluation board.
-  **EVAL-ADXL367Z:** is the board that contains the ADXL367 sensor. This a small PCB that consist on the sensor, the necessary decoupling capacitors and pin headers for easy connectivity.
-  **USB cable and other connectors.**

This user guide provides an overview of how to use the application software. The functionality of the software is described with examples provided where appropriate.

SETTING UP THE EVALUATION SYSTEM
--------------------------------

To install the LabView based EVAL-ADXL367-SDP GUI follow the steps below:

-  Open the `ADXL367 GitHub Repository <https://github.com/bbearssADI/ADXL367-Evaluation-Software>`_.
-  Either clone this GitHub repository on your computer or simply click “Code>Download ZIP”
-  Run the “ADXL367_Setup.exe” file and follow the prompts.
-  If you have Labview 2020 or later installed on your computer you are done. If not, download the `Labview 2020 Runtime Engine <https://www.ni.com/en-us/support/downloads/software-products/download.labview.html#369643>`_.

ADXL367 GRAPHICAL USER INTERFACE
--------------------------------

The ADXL367 evaluation environment is divided into separate tabs, each of which specializes in commonly performed measurements for accelerometer devices. In this way, the evaluation system offers users an immediate ability to capture data for a wide variety of tests without the need to develop a customized hardware and software solution.

On each tab, the Start Data Acquisition and Stop Data Acquisition buttons are the primary ways the user acquires data from the device.

Device OverView Tab
~~~~~~~~~~~~~~~~~~~

On this tab, the user can view acceleration data, read the device memory map, and adjust device settings. Additional functionality on this tab includes the ability to read the memory register or to take a snapshot of the current memory register values.

Clicking the Read Register Map button gives a snapshot of the current memory register values, and it updates the serial number, device ID, part ID, and Rev ID.

.. image:: https://wiki.analog.com/_media/resources/quick-start/device_overview_tab5.png
   :align: center

Data record Tab
~~~~~~~~~~~~~~~

On this tab, the user can measure and record acceleration sampled at the selected output data rate. Data results are saved to a text file with the date, time, device ID, and serial number recorded as a header.

The user can specify the file path by clicking the small folder icon under Directory to Save File and browsing to the desired folder. If an existing file is selected, data is appended to the end of the file. The user can choose a data rate from 12.5 Hz to 400 Hz with the Data Rate Select control.

.. image:: https://wiki.analog.com/_media/resources/quick-start/data_record_tab.png
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/quick-start/eval-adxl367-sdp_photo.jpg
