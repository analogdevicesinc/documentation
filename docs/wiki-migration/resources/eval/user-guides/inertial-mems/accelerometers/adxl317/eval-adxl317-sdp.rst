EVAL-ADXL317-SDP User Guide
===========================

FEATURES
--------

-  Flexible inertial sensor evaluation platform
-  Controller board and interface board operate with interchangeable evaluation boards
-  Separates device under test (DUT) from controller for accurate environmental testing
-  Data capture at maximum BW (4kHz)
-  Continuous stream to file data recording
-  Standard USB cable for power and communications
-  PC-based graphical user interface (GUI)
-  Fast, easy installation

GENERAL DESCRIPTION
-------------------

This user guide describes the evaluation software that interfaces with the ADXL317 accelerometer. For more information on performance details, see the ADXL317 datasheet. The EVAL-SDP-CB1Z is the serial system demonstration platform controller board from Analog Devices, Inc. The SDP-B is part of the Analog Devices system demonstration platform (SDP). SDP controller boards provide a means of communicating with the sensor from the PC. The EVAL-SDP-INTER-317Z is an SDP interface board. This board serves as an interposer between the SDP controller board and the evaluation board. The interface board includes hardware that allows I2S to parallel output data conversion, compatible with Arduino UNO V3 pinout. Please visit the following wiki for more information: :doc:`Evaluating the ADXL317 </wiki-migration/resources/eval/user-guides/inertial-mems/accelerometers/adxl317>`. The EVAL-ADXL317-SDP is an evaluation board that is separate from the interface board to allow easier manipulation of the device for testing (that is, rotating the device around its sensitive axis). The evaluation board is connected to the interface board via a 10-pin cable connector. This user guide provides an overview of how to use the application software. The functionality of the software is described with examples provided where appropriate. Figure 1 shows the required hardware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl314/eval-adxl31x-sdp-hw-inbox.jpg
   :align: center

.. container:: center lo

   **Figure 1:** what is included in the kit? a) One EVAL-SDP-CB1Z, b) One EVAL-SDP-INTERZ board, c) One EVAL-ADXL317Z board, d) One Standard A to Mini B USB cable, e) Two 10-pin Harwin Datamate L-Tek cable to board connectors, f) One 10-pin Harwin Datamate L-Tek cable connector.


SETTING UP THE EVALUATION SYSTEM
--------------------------------

QUICK START
~~~~~~~~~~~

To configure the hardware, follow these steps:

-  Download and install the application software by copying the following FTP link into your system's file explorer: `EVAL-ADXLx-SDP Eval Platform <https://wiki.analog.com/ftp/ftp.analog.com/pub/imems_sensor_eval/eval-adxlx-sdp%20eval%20platform>`__.
-  Connect the EVAL-ADXL317Z to the interface board (EVAL-SDP-INTER-317Z) using the 10-pin cable connector provided.
-  Connect the SDP interface board to the SDP-B controller board by clipping the 120-pin connectors together (see Figure 2).
-  Connect the Mini B USB cable to the SDP-B controller board and plug the opposite end of the USB cable into the PC. At this point, the set up should look like the one in Figure 3.
-  Start the application software.

|image1|

.. container:: center lo

   **Figure 2:** Correctly Connected Controller Board and Interface Board: Underside of Controller Board (Left) to Top of Interface Board (Right).


   |image2|

.. container:: center lo

   **Figure 3:** Fully Assembled Evaluation System.


ADXL317 GRAPHICAL USER INTERFACE
--------------------------------

|image3|

.. container:: center lo

   **Figure 4:** ADXL317 Evaluation System Graphic User Interface.


GETTING STARTED
~~~~~~~~~~~~~~~

The ADXL317 Customer Evaluation System provide an easy start evaluating the sensor performance. The graphic user interface is divided into separate tabs, each of which specializes in commonly performed measurements for accelerometer devices. In this way, the evaluation system offers users an immediate ability to capture data for a wide variety of tests without the need to develop a customized hardware and software solution.

A brief description of the functionality contained within the evaluation environment is presented in Table 1.

.. container:: center lo

   **Table 1:** Evaluation Environment Overview.


   |image4|

On each tab, the **Start Data Capture** and **Stop Data Capture** buttons are the primary ways the user acquires data from the device. Click **QUIT** located in the lower right of the start-up window to exit the software at any time.

The device filters can be configured independently for each axes. Changes are applied when pressing **Update Filters Configurations** button. This interface also allows the user to decide if they want to save data to a file and the output data format, LSB or [g].


|image5|

.. container:: center lo

   **Figure 5:** GUI controls.


Memory Register Map
^^^^^^^^^^^^^^^^^^^

Provides the ability to read the memory register or to take a snapshot of the current memory register values. Click the **Read Register Map** button for a snapshot of the current memory register values (see Figure 6).


|image6|

.. container:: center lo

   **Figure 6:** Register Map.


The following sections describe the purpose of each tab of the software.

DEVICE OVERVIEW TAB
~~~~~~~~~~~~~~~~~~~

|image7|

.. container:: center lo

   **Figure 7:** OverView Tab.


The Device Overview tab is a good way to become familiar with how the device operates. The ADXL317 is a 3-axis accelerometer, meaning the device is sensitive to acceleration in any direction, whit a fixed range of +/- 16g and a resolution of 14 bits. Please refer to the ADXL317 data sheet for more details.



|image8|

.. container:: center lo

   **Figure 8:** Axes of Acceleration Sensitivity (Corresponding Output Increases When Accelerated Along the Sensitive Axis).


Press **Start Capture Data** button to initiate data capture. This tab is configure to read acceleration data directly from the register map, registers X_DATA_LO to Z_DATA_HI, via I2C serial communication protocol. The I2C interface supports standard data transfer mode at 100 kHz.

TDM4 DATA STREAMING TAB
~~~~~~~~~~~~~~~~~~~~~~~

|image9|

.. container:: center lo

   **Figure 9:** TDM4 data streaming tab.


The TDM4 data streaming tab allows the user to evaluate the ADXL317 performance at its highest bandwidth, using its I2S data streaming interface. In this case, the part is configured for TDM4, 16-bits at 3.072MHz clock frequency. TDM stands for Time Division Multiplexing, which is a synchronous serial data transmission protocol. TDM4 refers to the division of each data frame in four channels. Each frame contains 64 clock periods (four 16-bits channels). The ADXL317 features a 14-bits resolution and the word length per axis (X,Y,Z) is 16-bits. The data is left justified and the two LSB are zero allways.

Each frame follows this structure:


|image10|

.. container:: center lo

   **Figure 10:** Evaluation kit I2S package format: 3.072MHz 16-bits TDM4.


Press **Start Data Capture** to begin data streaming. 20000 frames are read in a single stream read. The data is then postprocessed and plotted. Press Stop Data Capture to stop data streaming. The user can also save the data to a file while streaming. To do so, check the **Save data?**, select **File Path** and **File Name**.

FFT ANALYSIS
~~~~~~~~~~~~

|image11|

.. container:: center lo

   **Figure 11:** FFT Analysis Tab.


This tab allows the user to quickly study the FFT response of a signal. Data is streamed from I2S interface. To control the number of frames per read, change the **FFT Read Length** field value. By default is set to 20000 frames. Press **Start Data Capture** to begin data streaming or refresh last read.

SELF TEST
~~~~~~~~~

|image12|

.. container:: center lo

   **Figure 12:** Self Test Tab.


This Tab allows the user to check the integrity of the part by performing a self-test. The self test results section shows the average positive and negative delta self test values for each axis. The self test passes if the positive and negative delta self test are within the datasheet specifications. The green button will turn red and show "Failed" if the self test is not successful.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl314/eval-adxl31x-sdp_assembly1.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl314/eval-adxl31x-sdp_assembly2.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/overview_tab.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/gui_tabs.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/gui_controls.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/registermap.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/overview_tab_2.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/eval-adxl31x-sdp_xlaxesorientation.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/tdm4_tab.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/tdm4-16bit3mhz.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/fft_analysis.jpg
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl317/self-test.jpg
