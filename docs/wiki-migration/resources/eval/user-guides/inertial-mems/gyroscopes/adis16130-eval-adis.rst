f===== ADIS16130 EVALUATION ON THE EVAL-ADIS =====

INTRODUCTION
============

The purpose of this Wiki Guide is to describe an approach to use for evaluating the :adi:`ADIS16130` on the :adi:`EVAL-ADIS` evaluation system. Although the :adi:`ADIS16130` package and electrical connector would support physical connection with the :adi:`EVAL-ADIS`, its pin assignment, SPI protocol, data format and operation prevent compatibility with the IMU Evaluation software package.

Since the :adi:`ADIS16130` is on a "Last time buy," new design projects should consider the :adi:`ADIS16133`, :adi:`ADIS16135` or :adi:`ADIS16136`, as they provide better performance/price trade-offs, in the same package as the :adi:`ADIS16130`. In addition, the :adi:`EVAL-ADIS` and IMU Evaluation Software package provide direct support for the :adi:`ADIS16135`, which will be more convenient than the process for evaluating the :adi:`ADIS16130` on the :adi:`EVAL-ADIS` evaluation system.

OVERVIEW
========

Connecting the :adi:`ADIS16130BMLZ <ADIS16130>` to the :adi:`EVAL-ADISZ <EVAL-ADIS>` evaluation system will require the use of J1, on the :adi:`EVAL-ADISZ <EVAL-ADIS>`, an interface board and a cable. The following pictures provide an example of what this type of system might look like. The remainder of this Wiki Guide will describe this system and provide tips for those who may want to develop their own interface system for evaluating the :adi:`ADIS16130BMLZ <ADIS16130>` ON the :adi:`EVAL-ADISZ <EVAL-ADIS>`.

|image1| |image2| |image3|

BASIC SETUP
===========

ADIS16130 Installation
----------------------

Step #1
~~~~~~~

Align the :adi:`ADIS16130BMLZ <ADIS16130>` connector with J1 on the interface board, as shown in the first two pictures below.

|image4| |image5|

After alignment, press the unit down on the board, as shown in the following picture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-insertion-02.jpg
   :width: 300px

Step #2
~~~~~~~

Secure the :adi:`ADIS16130BMLZ <ADIS16130>` to the interface board using (4) M2x0.4x16mm machine screws. If a torque-setting is available on the screwdriver, use a setting of 20 inch-ounces.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-screws.jpg
   :width: 300px

Step #3
~~~~~~~

Install the interface cable onto J2 of the interface board. In this particular example, ink was added to the location on the cable connector to identify pin #1.

|image6| |image7|

EVAL-ADIS Setup
---------------

.. _step-1-1:

Step #1
~~~~~~~

Set JP1 to use the EXT (external supply option) option.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-jp1-ext.jpg
   :width: 300px

.. _step-2-1:

Step #2
~~~~~~~

Hook an external power supply up to J3. Set the supply for +5V (verify with a meter at J3).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-j3.png
   :width: 500px

.. _step-3-1:

Step #3
~~~~~~~

Install the interface cable onto J1 and connect the shield (from cable) to a ground on the :adi:`EVAL-ADISZ <EVAL-ADIS>`.

|image8| |image9| |image10|

SOFTWARE INSTALLATION
=====================

USB Driver Download
-------------------

Visit the :adi:`EVAL-ADIS` evaluation tool page to download the USB driver file:

:adi:`EVAL-ADIS USB Driver Download Link <static/imported-files/eval_boards/USB_Driver_Installation.zip>`

Some users may need to visit the web site and download the file directly from the :adi:`EVAL-ADIS Home Page <EVAL-ADIS>`:

:adi:`EVAL-ADIS Software Tools <en/evaluation/EVAL-ADIS/eb.html#SOFTWARE_AND_TOOLS>`

USB Driver Installation
-----------------------

The SDPDrivers.exe file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. Double-click on the SDPDrivers.exe file and follow the prompts to install the USB driver files onto the PC. When the following window appears, click on **Next** and then click on **Install** to continue with the installation. Note that the following pictures do not match the latest USB driver revision, but the installation process will be the same. Do not be alarmed if the revision on the window is not "1.3.7.0."

|image11| |image12|

The following pictures show the progress bar and the final confirmation window. Click on **Finish** to complete the installation.

|image13| |image14|

ADIS16130/EVAL-ADIS Software Download
-------------------------------------

Click on the following link and save the file to a convenient location on the test PC. Then extract two files into the folder that the application will run out of.

`adis16130-eval-adis-datacaptureapp.zip <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-datacaptureapp.zip>`__

SOFTWARE GUIDE
==============

The ADIS16130 software package does not require installation. Double-click on the \*.exe file to launch this package and get started.

Main Menu/Initial View
----------------------

This is the first window that appear when starting the software:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-01.png
   :width: 800px

Main Menu/Connect
-----------------

Click on the **Connect** button to run the ADIS16130BMLZ through the initialization sequence that the :adi:`ADIS16130 Dataheet <ADIS16130>` offers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-02.png
   :width: 800px

The red **False** indicator will change to a green **True** indication when this process completes and is successful.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-03.png
   :width: 800px

Main Menu/Plot Scaling
----------------------

Move the mouse pointer over the waveform recorder screen and right-click to access to window scaling functions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-04.png
   :width: 800px

Note the changes to the the gyro scaling after completing these adjustments:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-05.png
   :width: 800px

Main Menu/Waveform Recorder
---------------------------

Click on the **Start** button to start the waveform scroll across the screen. Observe the :adi:`ADIS16130's <ADIS16130>` response to hand-waving.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-06.png
   :width: 800px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-07.png
   :width: 800px

Main Menu/Read Array
--------------------

The **Read Array** button provides a function that can capture a small amount of data in a dialog window, which can be copied an pasted into Excel.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-08.png
   :width: 800px

Here is an example of the resulting dialog box. The "unscaled" columns are 24-bit, offset binary numbers that are displayed in hexadecimal format. :adi:`See Table 7 and 8, on page 10 of the ADIS16130 datasheet <static/imported-files/data_sheets/ADIS16130.pdf#Page=10>`, for more information on the numerical format for the digital data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-datafile-01.png
   :width: 800px

Main Menu/Streaming Function
----------------------------

The **Start Streaming** button enables a larger data record.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-09.png
   :width: 800px

The following relationships help determine the two key input variables for the Streaming Mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-ds-01.png
   :width: 400px

The total samples and averaging factors are both inputs that the ADIS16130 software package provides:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-main-10.png
   :width: 800px

Here is an example that supports producing a 1 hour time record, which has a data sample rate of 100 samples per second.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-ds-02.png
   :width: 300px

\`1q====SOFTWARE TUTORIALS (EXAMPLES)====

EXAMPLE #1: Total Noise Measurement
-----------------------------------

The :adi:`ADIS16130` datasheet does not have a parameter for total noise, but it does offer typica specifications for both noise and bandwidth. The total noise is equal to the noise density, times the square root of the noise bandwidth. Since the ADIS16130 has a two pole filter (327, 1000Hz), we can approximate the noise bandwidth to be ~1.4 x the cut-off frequency (300Hz, :adi:`per Table 1 in the ADIS16130 datasheet) <static/imported-files/data_sheets/ADIS16130.pdf>`.

Therefore:

Total Noise = 0.0125 x sqrt(1.4 x 300) = ~0.255 deg/sec

Start this process by verifying basic function, using the waveform recorder mode. After verifying that the :adi:`ADIS16130` is functional, place it in a secure location, where it will not be moved during data collection. Then, update the main menu settings in the picture below (total samples, etc).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-noise-01.png
   :width: 800px

After verifying all of these settings, click on **Start Streaming**. When the following window opens, select the file name and location, then click on **Save** to start the datalog.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-noise-02.png
   :width: 600px

The data streaming progress shows up as a "Stream xx% complete," with 100% complete indicating that all of the data samples are in the target file.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-noise-03.png
   :width: 800px

Click on the following file to see the result of this test on a lab unit. In this test, the :adi:`adis16130` noise result was close to 0.2 deg/sec.

`adis16130-noisetest-01.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-noisetest-01.xlsx>`__

--------------

--------------

EXAMPLE #2: Sensitivity
-----------------------

This example exercise is based on the calibration method that the following article reference explains:

:adi:`A Simple Gyroscope Calibration by Mark Looney, EDN Europe, July 2010 <static/imported-files/tech_articles/GyroCalibration_EDN_EU_7_2010.pdf>`

Start this process by entering 114000 samples for the record size, which provides a data record of 20 seconds at the nominal sample rate of 5700SPS.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-sens-02.png
   :width: 800px

Click on **Start Streaming**, enter the file name/location in the window that pops up and then click on **Save** to start the streaming process. Then, gently rotate the :adi:`ADIS16130`/Interface PCB around, 180 degrees, using the PCB edge and the edge of a table as a guide. Allow the device to rest (zero motion) for a couple of seconds and then rotate it back. This entire process must be complete before the data streaming completes.

NOTE: Over-ranging the gyroscope will introduce errors. This might require iteration to achieve expected results.

Here is an example of a hand-turn, which was a bit choppy but still produced results that were within the expected error range for sensitivity on the :adi:`adis16130`. The 3% error is well within the datasheet specification of +/-10% for sensitivity error.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-sens-03.png
   :width: 600px

Here is the spreadsheet file which contains the data and analysis, which produced the rate and angle graphs:

`adis16130-senstest-01.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-senstest-01.xlsx>`__

:ez:`Click on this Engineer Zone post <docs/DOC-2181>` to see another example of this type of sensitivity (or scale factor) test on a gyroscope.

--------------

--------------

EXAMPLE #3: Bias vs Temperature
-------------------------------

The :adi:`adis16130` datasheet offers performance curves that project a "bias temperature coefficient" of approximately 0.04 deg/sec per degree Celsius. The purpose of this experiment is to illustrate the process of testing this on an actual :adi:`ADIS16130` unit, using the :adi:`EVAL-ADIS` and techniques covered in this Wiki Guide. For this experiment, place the :adi:`ADIS16130`/Interface PCB inside of an oven and use the twisted pair cable to route it to the :adi:`EVAL-ADIS`, which is located outside of the temperature chamber. See the picture below:

|image15| |image16|

Take note of the clamps that are on the interface board, but not on the :adi:`\|ADIS16130 <adis16130>`. In some cases, clamping the :adi:`adis16130` down to the board will be necessary, due to the vibration in the oven. This was not important for this exercise, but can be influential when developing fixtures for calibration systems.

The following table illustrates the thermal profile for the temperature chamber for this experiment. For those who are developing calibration systems, the dwell times and ramp rates are likely to be an area for application-specific optimization.

============ =============================== =======================
Temperature  Dwell Time/Ramp Rate            Time
============ =============================== =======================
+25C         5 min                           5 min
+25C to -40C ~2 degC/min                     32.5 min (37.5 min max)
-40C         30min                           30 min
-40C to +85C ~2 degC/min                     62.5 min (67.5 min max)
+85C         15 min                          15 min
+85C to +25C ~2 degC/min                     30 (35 min max)
Total Time = 180 min (typical) 195 min (max) 
============ =============================== =======================

In order to support the maximum profile time of 195 minutes, set the data capture process up to collect data for 210 minutes. This allows for 15 extra minutes, for any expected delays or handling. Of course, this is adjustable, once someone has enough experience to understand how these adjustments impact the overall characterization goals. For now, calculate the total samples by multiplying the record time and the sample rate together.

Total samples = 5700 SPS x 210 min x 60 sec/min = 71820000 samples

In order to keep the file size under control, set the averages to produce a sample rate of 5 SPS in the data record.

Averages = Sample rate/Record data rate = 5700 SPS/5 SPS = 1140

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-sens-05.png
   :width: 800px

The following figure provides the results of this process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-es-mm-sens-04.png
   :width: 600px

Note that the bias temperature coefficient was calculated on the rising edge of the thermal profile, using two points between -40 and +85C. The bias temperature coefficient was was within the expectations that the :adi:`ADIS16130` datasheet sets in its performance curves.

Click on the following file name to download the MS Excel file for this test run.

`adis16130-biastemp-1.xlsx <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-biastemp-1.xlsx>`__

--------------

--------------

SUPPORTING DETAILS (UNDER CONSTRUCTION)
=======================================

The purpose of this section is to provide supporting documentation, which might be useful for longer-term review of these techniques.

BASIC ELECTRICAL CONNECTIONS
----------------------------

This system establishes the following connections, between the :adi:`ADIS16130BMLZ's <ADIS16130>` connector and J1 on the :adi:`EVAL-ADISZ <EVAL-ADIS>`.

==================== ======================= ===========================
ADIS16130 Pin Number EVAL-ADIS J1 Pin Number ADIS1630BMLZ Function
==================== ======================= ===========================
1                    No connection           Self-test
2                    No connection           Self-test
3                    No connection           Self-test
4                    No connection           Self-test
5                    No connection           Self-test
6                    No connection           Self-test
7                    No connection           Self-test
8                    3                       SPI Chip Select (~CS)
9                    No connection           Self-test
10                   13                      Data ready
11, 13, 15           10, 11, 12              Power Supply (VDD)
12                   4                       SPI Data Output (SDO)
14                   6                       SPI Data Input (SDI)
16                   2                       SPI Serial Clock (SCLK)
17, 19, 20, 21, 22   7, 8, 9                 Ground (GND)
18                   No connection           Input clock (SYNC)
23                   No connection           Analog Filter Node 1 (ROA1)
24                   No connection           Analog Filter Node 2 (ROA2)
==================== ======================= ===========================

INTERFACE CABLE
---------------

Although the :adi:`EVAL-ADISZ <EVAL-ADIS>` system was not designed to support remote device communication, using J1, experimentation has determined that this port can support up to 12 inches of ribbon cabling, while maintaining quality data communication. For lengths that are greater than 12 inches, use shielded, twisted pair cabling. The cable shown in the OVERVIEW section is 3 feet long.

\*\* Cable part number & supplier \*\*

INTERFACE BOARD
---------------

The interface boards in this Wiki Guide is an old design for an adapter board. While any new project would benefit from a new printed circuit board design, we wanted to illustrate the concept using an existing board. Note that J1 on this interface board only supports pins 1 through 12, so pin 13 was routed to the data-ready connection on the :adi:`ADIS16130BMLZ <ADIS16130>`, using a small piece of wire.

Click on the following link to access the electrical schematic for this interface PCB:

`gs09654rasch.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/gs09654rasch.pdf>`__

Click on the following document link to access the printed circuit board layout for this interface PCB:

`gs09655rapcb.pdf <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/gs09655rapcb.pdf>`__

ADIS16130 Pin Assignments
-------------------------

While the :adi:`ADIS16130BMLZ <ADIS16130>` uses the same package style and size as the :adi:`ADIS16136AMLZ <ADIS16136>`, it does not use the same pin assignments. This difference in pin assignments prevents it from plugging directly into J4 on the :adi:`EVAL-ADISZ <EVAL-ADIS>` evaluation system. The following table illustrates these differences.

========== =========================== =======================
Pin Number ADIS1630BMLZ Function       EVAL-ADIS Function
========== =========================== =======================
1          Self-test                   Digital I/O Line 3
2          Self-test                   Digital I/O Line 4
3          Self-test                   SPI Serial Clock (SCLK)
4          Self-test                   SPI Data Output (DOUT)
5          Self-test                   SPI Data Input (DIN)
6          Self-test                   SPI Chip Select (~CS)
7          Self-test                   Digital I/O Line 1
8          SPI Chip Select (~CS)       Reset (~RST)
9          Self-test                   Digital I/O Line 2
10         Data ready                  Power Supply (VDD)
11         Power Supply (VDD)          Power Supply (VDD)
12         SPI Data Output (SDO)       Power Supply (VDD)
13         Power Supply (VDD)          Ground (GND)
14         SPI Data Input (SDI)        Ground (GND)
15         Power Supply (VDD)          Ground (GND)
16         SPI Serial Clock (SCLK)     Do not connect (DNC)
17         Ground (GND)                Do not connect (DNC)
18         Input clock (SYNC)          Do not connect (DNC)
19         Ground (GND)                Do not connect (DNC)
20         Ground (GND)                Do not connect (DNC)
21         Ground (GND)                Do not connect (DNC)
22         Ground (GND)                Do not connect (DNC)
23         Analog Filter Node 1 (ROA1) Do not connect (DNC)
24         Analog Filter Node 2 (ROA2) Do not connect (DNC)
========== =========================== =======================

:adi:`ADIS16130BMLZ <ADIS16130>` Pin Assignments (NOTE: Pins are not visible from this view, but are shown to help illustrate their location)

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-f01.jpg
   :width: 250px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-f03.jpg
   :width: 250px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-f02.jpg
   :width: 250px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-insertion-01.jpg
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-insertion-01b.jpg
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-cable-insertion-01.jpg
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-cable-insertion-02.jpg
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-j1-insertion-01.jpg
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-j1-insertion-02.jpg
   :width: 300px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-j1-insertion-03.jpg
   :width: 300px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-usbdriverinstall-01.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-usbdriverinstall-02.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-usbdriverinstall-03.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-usbdriverinstall-04.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-inoven2.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16130-eval-adis-outofoven1.jpg
   :width: 400px
