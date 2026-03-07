EVAL-ADXL35x-SDP User Guide
===========================

FEATURES
--------

-  Flexible inertial sensor evaluation platform
-  Controller board and interface board operate with interchangeable evaluation boards
-  Separates device under test (DUT) from controller for accurate environmental testing
-  Data capture at maximum device output data rate (ODR)
-  Standard USB cable for power and communications
-  PC-based graphical user interface (GUI)
-  Fast, easy installation

GENERAL DESCRIPTION
-------------------

This user guide describes the evaluation software that interfaces with the ADXL355 and ADXL357 accelerometer. For more information on performance details, see the ADXL355/7 datasheet. This user guide provides an overview of how to use the application software. The functionality of the software is described with examples provided where appropriate.

Table 1 shows the required hardware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/eval_board_table.png
   :align: center
   :width: 800px

SETTING UP THE EVALUATION SYSTEM
--------------------------------

The following steps describe the installation process for the ADXL357 evaluation system, as an example. Same steps apply for the ADXL355.

HARDWARE CONFIGURATION
~~~~~~~~~~~~~~~~~~~~~~

To configure the hardware, follow these steps:

-  Connect the bottom part of the SDP connector to the interface board using the 10-pin cable connector provided. Follow the images below to make sure that the connections are correct.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture1.1.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture2.png
   :align: center
   :width: 400px

.. container:: center lo

   **Figure 1:** Connecting controller board to interface board.


-  Connect the SDP interface board to the SDP-B controller board by clipping the 120-pin connectors together (see Figure 2).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture4.png
   :align: center
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture5.png
   :align: center
   :width: 400px

.. container:: center lo

   **Figure 2:** Connecting the SDP Interface to SDP-B Controller


-  Take two 10-pin Harwin Datamate L-Tek connectors and connect it to Pins P1 and P2 respectively. Make sure that the marking on the connector is in-line with the markings on the eval board as shown in the Figure 3 below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture6.png
   :align: center
   :width: 800px

.. container:: center lo

   **Figure 3**


-  Connect the Mini B USB cable to the SDP-B controller board and plug the opposite end of the USB cable into the PC.

SOFTWARE INSTALATION
~~~~~~~~~~~~~~~~~~~~

-  Download the software installer on your desktop:

::

     * Use this link for EVAL-ADXL355-SDP: 

::

     * Use this link for EVAL-ADXL357-SDP:

-  Extract the files to your local drive. Double-click on **EVAL-ADXL357-SDP_install**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/step1.png
   :align: center
   :width: 1000px

.. container:: center lo

   **Figure 4**


-  To begin with installation, save the file to your preferred location, then click **“Next”**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/a.png
   :align: center
   :width: 800px

.. container:: center lo

   **Figure 5**


-  The file will be saved as **ADXL357 Customer Evaluation System**
-  Follow the steps in the images below to finish the SDP Driver Installation.

|image1| |image2|

.. container:: center lo

   **Figure 6**


-  After the SDP Driver installation is completed, we can start the evaluation software.
-  Connect the evaluation setup to your PC using the USB cable provided.
-  Go to the installation directory and run the **EVAL-ADXL357-SDP.exe** executable, or type **EVAL-ADXL357-SDP** in the Windows search bar and press Enter.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/s5.png
   :align: center

.. container:: center lo

   **Figure 7**


SOFTWARE STARTUP
~~~~~~~~~~~~~~~~

When the software first starts, it will check which interface board is being used. If the software is not able to detect any system it will show the following window below. Make sure that the device is connected properly and there are no loose connections. If the board is not detected, you might need to close the GUI application and open it again,

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/1.png
   :align: center
   :width: 300px

.. container:: center lo

   **Figure 8**


When the software detects a device, it will ask the user to specify which interface board is being used. The image below shows SDP Interface Rev.4 being detected. The user can also look at the SDP Interface version identifier to determine which revision board you have.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture1.png
   :align: center
   :width: 600px

.. container:: center lo

   **Figure 9**


ADXL35x GRAPHICAL USER INTERFACE
--------------------------------

|image3|

.. container:: center lo

   **Figure 10:** ADXL35x Evaluation Software Startup.


GETTING STARTED
~~~~~~~~~~~~~~~

The ADXL357 Customer Evaluation System provide an easy start evaluating the sensor performance. The graphic user interface is divided into separate tabs, each of which specializes in commonly performed measurements for accelerometer devices. In this way, the evaluation system offers users an immediate ability to capture data for a wide variety of tests without the need to develop a customized hardware and software solution.

A brief description of the functionality contained within the evaluation environment is presented in Table 2.


|image4|

.. container:: center lo

   **Table 1:** Evaluation Environment Overview.


SHARED COMMANDS BETWEEN TABS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The basic configuration block below (yellow rectangle) is shared by all tabs, except for a fewer exceptions that vary from tab to tab. Details will be provided on each tab. Each section of the basic configuration block is explained next:

**1. Power Mode**


|image5|

.. container:: center lo

   **Figure 11:** Standby to Measurement Mode.


**2. Output Data Rate**



|image6|

.. container:: center lo

   **Figure 12:** Output Data Rate.


The image below shows how different ODR affects how the data is being sampled. Data being sampled at 3.096 Hz is seen to be rougher (zig-zag motion) as the sample rate is slower than the rate at which data is being received which may cause loss of some data. Whereas data being sampled at 500Hz is seen to be a lot faster and smooth.



|image7|

.. container:: center lo

   **Figure 13:** Output Data Rate Example.


**3. High Pass Filter**

Below are the available, user selectable high pass filter values.


|image8|

.. container:: center lo

   **Figure 14:** High Pass Filter.


**4. Range**

3 user selectable range available. See example image below, for the ADXL357 evaluation system.


|image9|

.. container:: center lo

   **Figure 15:** Range Options.


**5. Offset Trim**



|image10|

.. container:: center lo

   **Figure 16:** Offset Trim.


**6. Saving File Path**



|image11|

.. container:: center lo

   **Figure 17**


**7. Memory Register Map**

Click the Read Register Map button for a snapshot of the current memory register values (see Figure 18).


|image12|

.. container:: center lo

   **Figure 18: ADXL35x Register Map**


**8. Start/Stop Capture and Quit**

These commands are also shared by all tabs. Start Capture initiates the data collection on the current tab. After Start Capture is pressed, it is automatically grayed out and disabled until Stop Capture is pressed. Quit exits the GUI.

DEVICE OVERVIEW TAB
~~~~~~~~~~~~~~~~~~~

|image13|

.. container:: center lo

   **Figure 19:** Device Overview Tab.


The Device Overview tab is a good way to become familiar with how the device operates. This tab contains all the controls to configure the part. For example, when the part first turns on, it powers up in standby mode. The ADXL35x powers up in standby mode to minimize power consumption. To exit standby mode, look at the Power Settings control. Change the mode from standby to measurement mode (see Figure. 11).

ACTIVITY/INACTIVITY DETECTION TAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The activity tab allows you set threshold for activity detection. In the example below the activity box is checked for x-axis and it shows ACT_EN register is enabled for X-axis. The next setting is for activity threshold, which allows the user to set the max threshold for it to start measuring acceleration. For this example, the Activity threshold is set to 3g, if there’s any activity more than 3g, the measurement starts for X-axis. Activity counter sets the number of consecutive events needed above the set threshold to detect activity.

|image14|}}

.. container:: center lo

   **Figure 21:** Activity Detection for X-Axis.


   |image15|

.. container:: center lo

   **Figure 22:** Activity Detection for all axes.


FFT
~~~

This tab runs a continuous loop that captures 1024 samples at the selected ODR and plots the FFT. The FFT is configured for 4 samples RMS averaging and rectangular windowing. The figure below shows the FFT plot for a 1g peak, 200Hz sinewave excitation.


|image16|

.. container:: center lo

   **Figure 23:** FFT Tab.


SELF-TEST TAB
~~~~~~~~~~~~~

The ADXL35X incorporates a self-test feature that effectively tests its mechanical and electronic systems simultaneously. When the self-test function is enabled, an electrostatic force is exerted on the mechanical sensor. This electrostatic force moves the mechanical sensing element in the same manner as acceleration, and it is additive to the acceleration experienced by the device. This added electrostatic force results in an output change in the x-, y-, and z-axes.


|image17|

.. container:: center lo

   **Figure 24:** Self-test event.


The Self-Test tab demonstrates how this function operates for each axis. Once the Start Data Acquisition button is clicked, the software acquires one second of data from the ADXL35X at the user specified data rate.

-  For the first 109 samples, the self-test feature is disabled (default state).
-  At 109th sample the self-test bit is asserted, and the self-test function begins. An electrostatic force is applied to the beam. This causes the output to shift as shown in Figure 25.
-  The self-test bit is asserted for the next sample.
-  At 210th sample the self-test bit is de-asserted and the device output return to normal.

|image18|

.. container:: center lo

   **Figure 25**


TILT MEASUREMENT TAB
~~~~~~~~~~~~~~~~~~~~

This tab enables the user to quicky evaluate the performance of the ADXL35x sensor as an inclinometer. To obtain accurate results, the software allows a pre-calibration step by leveraging the acceleration of gravity. Click the Calibrate XL button to begin. Following this, a series of 6 pop-up dialog boxes will appear. Follow the instructions in these dialog boxes. They will instruct you to hold the evaluation board in specific orientations such that each axis is exposed to a ±1g field (see Figure 26).


|image19|

.. container:: center lo

   **Figure 26:** Tilt Measurement Tab.


Use the circular marking on the top right corner of Eval board as the reference point for calibration.



|image20|

.. container:: center lo

   **Figure 27**


Place the x-axis in a +1g field. Hold the evaluation board vertically on a flat surface as shown in Figure 27.Hold part for 1 second and click OK



|image21|

.. container:: center lo

   **Figure 28:** +1g calibration.


Reorient the part as shown in the next dialog box. Repeat until all 6 measurements have been completed. The offset and sensitivity calibration coefficient are then calculated for each axis in g’s (see Figure 29).



|image22|

.. container:: center lo

   **Figure 29:** Calibration Result


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/s3.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/b.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture2.1.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/table2.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture4.1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture5.1.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture10.png
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture6.1.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture8.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture19.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture7.png
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture21.png
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture3.png
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture11.png
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture12.png
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture20.png
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture22.png
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture13.png
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture17.png
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture23.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture15.png
   :width: 500px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/picture18.png
