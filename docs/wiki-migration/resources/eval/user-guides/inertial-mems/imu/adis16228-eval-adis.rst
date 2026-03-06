ADIS16228 EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
--------

The :adi:`ADIS16228` iSensor® is a complete vibration sensing system that combines triaxial acceleration sensing with advanced time domain and frequency domain signal processing. Time domain signal processing includes a programmable decimation filter and selectable windowing function. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-hookup.png
   :width: 400px

ADIS16228/PCBZ BREAKOUT BOARD
-----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16228` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is the breakout board for the :adi:`ADIS16228` and may provide assistance in the process of hooking it up to an existing embedded processor system. For more information, click on the following link: :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`

For tips on interfacing to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` with a ribbon cable, check out the following Engineer Zone post:

:ez:`ADIS16228/PCBZ Breakout Board Cables (Engineer Zone FAQ) <mems/w/documents/4496/faq-adis16228-pcbz-breakout-board-cables>`

EVAL-ADIS: PC EVALUATION
------------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16228`, before developing their own embedded system, the :adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system.

PART LIST FOR ORDERING
----------------------

:adi:`EVAL-ADIS`

:adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16228/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the Vibration Evaluation Program.

PHYSICAL SETUP
--------------

The :adi:`ADIS16228/PCBZ <ADIS16228>` provides the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` on a small printed circuit board (PCB) that simplifies the connection to an existing processor system. This PCB includes a silkscreen, for proper placement, and four mounting holes that have threads for M2 × 0.4 mm machine screws. The second set of mounting holes on the interface boards are in the four corners of the PCB and provide clearance for 4-40 machine screws. The third set of mounting holes provides a pattern that matches the EVAL-ADIS evaluation system, using M2 × 0.4mm × 4 mm machine screws. These boards are made of IS410 material and are 0.063 inches thick. J1 is a 16-pin connector, in a dual row, 2 mm geometry that enables simple connection to a 1 mm ribbon cable system. For example, use Molex P/N 87568-1663 for the mating connector and 3M P/N 3625/16 for the ribbon cable. For direct connection to the :adi:`EVAL-ADIS` evaluation system, use these parts to make a 16-pin cable or remove pins 13, 14, 15 and 16. The LEDs (D1 and D2) are not populated, but the pads are available to install to provide a visual representation of the DIO1 and DIO2 signals. The pads accommodate Chicago Miniature Lighting Part No. CMD28-21VRC/TR8/T1, which works well when resistors R1 and R2 are approximately 400 Ω (0603 pad sizes).The mating connector for the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>`, J2, is AVX P/N 04-6288-015-000-846. The picture below provides a close-up view of this connector, which clamps down on the flex cable to press its metal pads onto the metal pads inside the mating connector. The schematic is for the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` board.

NOTE: Some of the illustrations show the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` instead of the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The package and setup process is identical for both of these products.

|image1| |image2| |image3| |image4|

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1 - Install ADIS16228CMLZ onto Interface Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slide the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part into the mating J2 connector on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Press the J2 clamp down onto the flex connector to complete the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part connection to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Then secure the part using the M2 × 0.4mm × 4 mm machine screws provided with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The following pictures provide a visual reference for correct connection but are actually :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` parts that share the same mechanical body.

|image5| |image6| |image7|

WARNING: Make sure that the connector cable going from J1 on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is properly aligned to the J1 connector on the :adi:`EVAL-ADIS`. The 16 pin cable is included with the :adi:`EVAL-ADIS`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-16pin-conn.png
   :width: 600px

Step #2 - Install ADIS16228/PCBZ onto EVAL-ADIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mounting to the system frame is accomplished using 4 M2 x.4 x 6mm machine screws included with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 4 holes to secure the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` to the :adi:`EVAL-ADIS`.

|image8| |image9| |image10| |image11|

Step #3 - Set Power Supply Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following picture shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`EVAL-ADIS` required for the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` operation.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-3.3v.png
   :width: 400px

VIBRATION EVALUATION PROGRAM OVERVIEW
-------------------------------------

The following sections provide a general description of the functions available in the Vibration Evaluation Program. For a set of :adi:`ADIS16288 <ADIS16228>`-specific instructions, please jump down to the section.

PROGRAM DOWNLOAD
----------------

EVAL-ADIS2 Vibration Evaluation Software User Guide
===================================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
-------------------------------------------------

The Vibration Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to a subset of iSensor products designed specifically for machine health and vibration monitoring applications. The platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition.

Due to the specialized nature of the machine health monitoring portfolio, only a subset of sensors is supported by this software. These devices are shown below.

+-------------------------------------------------------+


| SENSOR DEVICE NUMBER                                  |

+=======================================================+

| :adi:`ADIS16000AMLZ <ADIS16000>`  |

+-------------------------------------------------------+

| :adi:`ADIS16229AMLZ <ADIS16229>`  |

+-------------------------------------------------------+

| :adi:`ADIS16227/PCBZ <ADIS16227>` |

+-------------------------------------------------------+

| :adi:`ADIS16228/PCBZ <ADIS16228>` |

+-------------------------------------------------------+

.. important::

   The :adi:`ADIS16000AMLZ <ADIS16000>` manages wireless communication between several :adi:`ADIS16229AMLZ <ADIS16229>` devices.


.

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 Vibration Evaluation Software
--------------------------------------------------

Once the Vibration Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main.png
   :width: 700px

If an error similar to the image below pops up, click OK to proceed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-select-device.png
   :width: 400px

Device Selection
~~~~~~~~~~~~~~~~

Click on **Device**, located on the left side of the Menu bar, at the top of the **Main Screen**, and select the model number corresponding to your sensor. The :adi:`adis16228` was used for the following examples.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-device.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-main-select.png
   :width: 600px

.. important::

   Some menu options may appear "grayed out." This normal and indicates that some of the software features may not be available for the selected device type.

   
   For example, all of the **Network** options presently only apply :adi:`ADIS16229`.


Data Collection Mode
~~~~~~~~~~~~~~~~~~~~

The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic modes of data collection: Manual FFT, Automatic FFT, Manual Time (Time Domain) and Real-Time. Each of these modes can be configured using the **Register Access** window. For ease of use, the **Main Screen** offers a drop-down selection menu for these modes, along with a **Start** that kicks off a data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_modeselection_01b.png
   :width: 600px

Waveform Display
~~~~~~~~~~~~~~~~

The **Waveform Display** quickly displays the data read back from the sensor. The data format, units, etc. will automatically change based upon the selected data capture mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px

Enable Data Log
~~~~~~~~~~~~~~~

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-enable-datalog.png
   :width: 600px

RegisterAccess
~~~~~~~~~~~~~~

The **Register Access** option on the **Menu Bar** provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-reg-sel.png
   :width: 700px

The image below shows the **Register Access** window when an :adi:`ADIS16228` is connected.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_01.png
   :width: 600px

Reading Sensor Register
^^^^^^^^^^^^^^^^^^^^^^^

In order to read the contents of a sensor register, click on the register in the table and then click on "Read Selected Register." The :adi:`EVAL-ADIS2` will issue the correct commands to the sensor and update the GUI with the data the sensor responded with.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_01.png
   :width: 600px

Writing to Sensor Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following two steps to write a value to the register. 1. Enter the data to be written to the sensor in the text box shown below.

.. important::

   Register data must be written in hexadecimal format!


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_02.png
   :width: 600px

2. Click on **Write**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_03.png
   :width: 600px

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Single-Command Options
^^^^^^^^^^^^^^^^^^^^^^

The section on the right side of the window provides a means of easily calling subroutines within the connected sensor. Clicking on a "Write" button is equivalent to writing a single-bit command to the respective register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_01.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_02.png
   :width: 600px

Configuring Alarms
~~~~~~~~~~~~~~~~~~

The **Alarm > Alarm Settings** option on the **Menu Bar** provides a convenient means of configuring the Spectral Alarm functions. The interface makes configuring and tuning these functions much easier!

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-alrm.png
   :width: 600px

Selecting **Alarms > Alarm Settings** will cause the following window to open:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_01.png
   :width: 600px

Select boxes in the matrix and enter values that are associated with the magnitude of the output data and FFT bin numbers.

.. important::

   The same results can be achieved by issuing individual writes to the respective registers using the **Register Access** window.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_02.png
   :width: 600px

Click on **Write to DUT** to update all of the registers associated with these entries.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_03.png
   :width: 600px

In order to verify that the settings were written to the sensor, close and re-open the window. Doing so will reset the form. Click on **Read from DUT** to read back the configuration settings from the sensor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_04.png
   :width: 400px

The **Alarms > Alarm Status Form** provides a convenient way to monitor each of the different alarm conditions. The dashes in each cell will change to green (no alarm), yellow ("warning" alarm, associated with Level 1) or red ("critical" alarm, associated with Level 2), depending on the conditions, after a data capture event completes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_statusform_01.png
   :width: 400px

Data Capture
~~~~~~~~~~~~

The **Data Capture** window provides a means of configuring the file location, base file name, and file count for each data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_01.png
   :width: 600px

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-datalog-file.png
   :width: 600px

This counter is also shown in the **Data Capture Window**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_02.png
   :width: 500px

Tools
~~~~~

The **Tools** option in the **Menu Bar** offers two options: **USB** and **SPI**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-tools-menu.png
   :width: 600px

The **USB** option allows for manually connecting or disconnecting the active :adi:`EVAL-ADIS2`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_01.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_02.png
   :width: 400px

The **SPI** option allows for adjusting the SPI SCLK and stall time (time between each 16-bit transaction). The image below shows the default settings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-spi-utilities.png
   :width: 400px

Demo
~~~~

Visit the :doc:`ADIS16229 Vibration Demo Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationdemo>` for more details on this function.

About
~~~~~

This option offers the revision and some codes that might be useful when seeking technical support.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-version-1-2.png
   :width: 400px

SOFTWARE REVISION HISTORY
-------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                                                                                                                        |
+==========+==============+===========================================================================================================================================================================================================================+
| v1.3.0   | 2/17/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 1/25/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 12/22/2013   | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.8   | N/A          | Internal test version, never published online                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 12/10/2013   | Added partial support for the ADIS16227 (Manual FFT mode only)                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 11/1/2013    | Extended the wait time to 4 seconds, for each sensor in the Network Scan                                                                                                                                                  |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.5   | N/A          | This version corrects a sizing problem in the main waveforms, along with a couple of bugs in other windows.                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.4   | N/A          | Updates for internal use only                                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.3   | N/A          | Added delays to Periodic Mode Exit routine register writes.                                                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.2   | N/A          | Added a dialog box for a user to specify the Update Interval of the Network Periodic Mode.                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 10/11/2013   | Corrected the GUI to indicate "not busy" after a communication is canceled by the user.                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Added exception handling routines to prevent a program crash and to show the Reconnect Dialog if the USB is disconnected.                                                                                                 |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.0001g                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | N/A          | Added "Scan All Channels" option to find nodes that are on different frequency channels                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.001g                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.3   | 9/10/2013    | Set the plot scale to +-2g for the first switch to time domain data. This ensures that data is visible on the plot. Subsequent plot mode changes set the scale to the previous user selected value for a particular mode. |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Set the Mode combo-box to ‘Periodic’ or ‘Manual’ when a demonstration mode is selected. This ensures that the plot mode is appropriate for the data displayed during a demonstration loop.                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.2   | 8/21/2013    | Add sensor node selection tabs to Register Access and Alarm menus                                                                                                                                                         |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: First version posted online at www.analog.com/EVAL-ADIS                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 8/15/2013    | Updated register names to match the :adi:`adis16229` datasheet                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Increased period mode sleep cycle time to 10 seconds                                                                                                                                                                      |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 8/1/2013     | Initial Release                                                                                                                                                                                                           |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


REPORTED ISSUES, UPGRADE REQUESTS & SOLUTIONS
---------------------------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | #  | DATE     | STATUS    | DEVICE                                           | DESCRIPTION & RELATED NOTES                                                                                                                                                                                                                                                     | SOLUTION                                                                                                                                                                                                                       |
+==========+====+==========+===========+==================================================+=================================================================================================================================================================================================================================================================================+================================================================================================================================================================================================================================+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.1   | 01 | 7/29/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time mode does not work after executing an **Auto-null** command in the **Register Access** menu. `Click here for more details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-v1_3_1-problemreport_adis16228.pdf>`__                     | After executing an **Auto-null** command, select Manual FFT mode first, then **Real-time** mode.                                                                                                                               |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | 01 | 2/24/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time only supports data collection at a rate of 1.26kSPS                                                                                                                                                                                                                   | v1.4.0 will address this. For now, use AVG_CNT settings that are *>* 4 (Sample rate = 1260 SPS)                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 04 | 2/12/14  | CLOSED    | :adi:`ADIS16000`                                 | Connection with :adi:`ADIS16229` is hard to establish                                                                                                                                                                                                                           | SPI Timing violation, click here for more details                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 03 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | **Time Domain** mode in this package seems to translate into **Manual Time Capture** in the :adi:`ADIS16228` datasheet. Can the software be consistent with the datasheet?                                                                                                      | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 02 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | The **Data Capture** function does not appear to work when using **Time Domain** mode                                                                                                                                                                                           | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 01 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | When using the **Data Capture** function, when in **Real-Time** mode, can this produce one continuous file for the data samples?                                                                                                                                                | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 01 | 1/9/14   | CLOSED    | :adi:`ADIS16228`                                 | Add all of the FFT Header registers to the Data Capture file                                                                                                                                                                                                                    | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 06 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16228` datasheet                                                                                                                        | v1.1.9 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 05 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Exiting **Periodic FFT** mode causes the program to jump into the **Main Screen > Tools > USB Menu**. When closing that Window, it engages in a 10 second countdown while allowing no user input.                                                                               | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 04 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Changes in the Mode Selection drop-down menu, located in the **Main Screen**, do not seem to track the related register settings in the **Register Access** menu                                                                                                                | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 03 | 12/13/13 | CLOSED    | :adi:`ADIS16228`                                 | **Manual FFT** only seems to support 20480 SPS sample rates. For more details, click on the following file: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-manualfftmultrecord.pdf>`__ | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 02 | 12/10/13 | CLOSED    | :adi:`ADIS16228`                                 | The **Alarm Status Form** does not correctly display alarm status. Click on this file for more details: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-alarmstatusform.pdf>`__         | No issue found. Open this file for more details: `Problem Resolution Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemresolutionreport-v1-1-7-adis16228-alarmstatusform.pdf>`__ |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 01 | 12/10/13 | CLOSED    | :adi:`ADIS16227`                                 | **Periodic FFT** appears to lock the software up and does not appear to produce FFT results                                                                                                                                                                                     | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 06 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16000` datasheet                                                                                                                        | v1.1.10, release date estimate = 1/10/2014                                                                                                                                                                                     |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 05 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Not able to add :adi:`adis16229` devices to pages 2-6 in the :adi:`ADIS16000`                                                                                                                                                                                                   | No issue found, but this will be closely scrutinized in the next two versions: v1.1.10 and v1.2.0                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: This function was verified in earlier versions of the software. Re-test of this function is in the test queue.                                                                                                                                                             |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 04 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There are a number of cases where the software becomes non-responsive, with particular sensitivity observed when using Periodic FFT.                                                                                                                                            | v1.2.0, release date estimate = 1/24/2014. For present revision, use **Manual FFT** mode only.                                                                                                                                 |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: Investigation has revealed that the present approach for simultaneous sensor monitoring and user input management is not stable. The solution to this will require substantial code changes, which are in progress.                                                        |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 03 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Sample rate settings in the **AVG_CNT** register do not seem to cause updates on the horizontal axis, of the x-axis data.                                                                                                                                                       | Use version v1.1.9 or later.                                                                                                                                                                                                   |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 02 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | Real-time data logging is not working                                                                                                                                                                                                                                           | This was not part of the original plan for this package, but is under consideration for v1.4.0 or later.                                                                                                                       |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 01 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Waveforms updates do not always respond to **Start** button presses, in any mode.                                                                                                                                                                                               | Use v1.2.0 or later                                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **STATUS CODE DEFINITIONS**                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **OPEN** means that the issue observation has been received, but has not been independently confirmed by ADI                                                                                                                                                                    |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CONFIRMED** means that the issue has been independently confirmed and ADI is working on a solution path.                                                                                                                                                                      |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CLOSED** means that the issue has been resolved                                                                                                                                                                                                                               |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



USB DRIVER INSTALLATION
-----------------------

EVAL-ADIS2 Vibration Evaluation Software User Guide
===================================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
-------------------------------------------------

The Vibration Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to a subset of iSensor products designed specifically for machine health and vibration monitoring applications. The platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition.

Due to the specialized nature of the machine health monitoring portfolio, only a subset of sensors is supported by this software. These devices are shown below.

+-------------------------------------------------------+


| SENSOR DEVICE NUMBER                                  |

+=======================================================+

| :adi:`ADIS16000AMLZ <ADIS16000>`  |

+-------------------------------------------------------+

| :adi:`ADIS16229AMLZ <ADIS16229>`  |

+-------------------------------------------------------+

| :adi:`ADIS16227/PCBZ <ADIS16227>` |

+-------------------------------------------------------+

| :adi:`ADIS16228/PCBZ <ADIS16228>` |

+-------------------------------------------------------+

.. important::

   The :adi:`ADIS16000AMLZ <ADIS16000>` manages wireless communication between several :adi:`ADIS16229AMLZ <ADIS16229>` devices.


.

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 Vibration Evaluation Software
--------------------------------------------------

Once the Vibration Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main.png
   :width: 700px

If an error similar to the image below pops up, click OK to proceed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-select-device.png
   :width: 400px

Device Selection
~~~~~~~~~~~~~~~~

Click on **Device**, located on the left side of the Menu bar, at the top of the **Main Screen**, and select the model number corresponding to your sensor. The :adi:`adis16228` was used for the following examples.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-device.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-main-select.png
   :width: 600px

.. important::

   Some menu options may appear "grayed out." This normal and indicates that some of the software features may not be available for the selected device type.

   
   For example, all of the **Network** options presently only apply :adi:`ADIS16229`.


Data Collection Mode
~~~~~~~~~~~~~~~~~~~~

The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic modes of data collection: Manual FFT, Automatic FFT, Manual Time (Time Domain) and Real-Time. Each of these modes can be configured using the **Register Access** window. For ease of use, the **Main Screen** offers a drop-down selection menu for these modes, along with a **Start** that kicks off a data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_modeselection_01b.png
   :width: 600px

Waveform Display
~~~~~~~~~~~~~~~~

The **Waveform Display** quickly displays the data read back from the sensor. The data format, units, etc. will automatically change based upon the selected data capture mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px

Enable Data Log
~~~~~~~~~~~~~~~

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-enable-datalog.png
   :width: 600px

RegisterAccess
~~~~~~~~~~~~~~

The **Register Access** option on the **Menu Bar** provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-reg-sel.png
   :width: 700px

The image below shows the **Register Access** window when an :adi:`ADIS16228` is connected.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_01.png
   :width: 600px

Reading Sensor Register
^^^^^^^^^^^^^^^^^^^^^^^

In order to read the contents of a sensor register, click on the register in the table and then click on "Read Selected Register." The :adi:`EVAL-ADIS2` will issue the correct commands to the sensor and update the GUI with the data the sensor responded with.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_01.png
   :width: 600px

Writing to Sensor Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following two steps to write a value to the register. 1. Enter the data to be written to the sensor in the text box shown below.

.. important::

   Register data must be written in hexadecimal format!


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_02.png
   :width: 600px

2. Click on **Write**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_03.png
   :width: 600px

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Single-Command Options
^^^^^^^^^^^^^^^^^^^^^^

The section on the right side of the window provides a means of easily calling subroutines within the connected sensor. Clicking on a "Write" button is equivalent to writing a single-bit command to the respective register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_01.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_02.png
   :width: 600px

Configuring Alarms
~~~~~~~~~~~~~~~~~~

The **Alarm > Alarm Settings** option on the **Menu Bar** provides a convenient means of configuring the Spectral Alarm functions. The interface makes configuring and tuning these functions much easier!

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-alrm.png
   :width: 600px

Selecting **Alarms > Alarm Settings** will cause the following window to open:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_01.png
   :width: 600px

Select boxes in the matrix and enter values that are associated with the magnitude of the output data and FFT bin numbers.

.. important::

   The same results can be achieved by issuing individual writes to the respective registers using the **Register Access** window.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_02.png
   :width: 600px

Click on **Write to DUT** to update all of the registers associated with these entries.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_03.png
   :width: 600px

In order to verify that the settings were written to the sensor, close and re-open the window. Doing so will reset the form. Click on **Read from DUT** to read back the configuration settings from the sensor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_04.png
   :width: 400px

The **Alarms > Alarm Status Form** provides a convenient way to monitor each of the different alarm conditions. The dashes in each cell will change to green (no alarm), yellow ("warning" alarm, associated with Level 1) or red ("critical" alarm, associated with Level 2), depending on the conditions, after a data capture event completes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_statusform_01.png
   :width: 400px

Data Capture
~~~~~~~~~~~~

The **Data Capture** window provides a means of configuring the file location, base file name, and file count for each data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_01.png
   :width: 600px

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-datalog-file.png
   :width: 600px

This counter is also shown in the **Data Capture Window**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_02.png
   :width: 500px

Tools
~~~~~

The **Tools** option in the **Menu Bar** offers two options: **USB** and **SPI**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-tools-menu.png
   :width: 600px

The **USB** option allows for manually connecting or disconnecting the active :adi:`EVAL-ADIS2`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_01.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_02.png
   :width: 400px

The **SPI** option allows for adjusting the SPI SCLK and stall time (time between each 16-bit transaction). The image below shows the default settings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-spi-utilities.png
   :width: 400px

Demo
~~~~

Visit the :doc:`ADIS16229 Vibration Demo Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationdemo>` for more details on this function.

About
~~~~~

This option offers the revision and some codes that might be useful when seeking technical support.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-version-1-2.png
   :width: 400px

SOFTWARE REVISION HISTORY
-------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                                                                                                                        |
+==========+==============+===========================================================================================================================================================================================================================+
| v1.3.0   | 2/17/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 1/25/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 12/22/2013   | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.8   | N/A          | Internal test version, never published online                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 12/10/2013   | Added partial support for the ADIS16227 (Manual FFT mode only)                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 11/1/2013    | Extended the wait time to 4 seconds, for each sensor in the Network Scan                                                                                                                                                  |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.5   | N/A          | This version corrects a sizing problem in the main waveforms, along with a couple of bugs in other windows.                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.4   | N/A          | Updates for internal use only                                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.3   | N/A          | Added delays to Periodic Mode Exit routine register writes.                                                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.2   | N/A          | Added a dialog box for a user to specify the Update Interval of the Network Periodic Mode.                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 10/11/2013   | Corrected the GUI to indicate "not busy" after a communication is canceled by the user.                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Added exception handling routines to prevent a program crash and to show the Reconnect Dialog if the USB is disconnected.                                                                                                 |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.0001g                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | N/A          | Added "Scan All Channels" option to find nodes that are on different frequency channels                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.001g                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.3   | 9/10/2013    | Set the plot scale to +-2g for the first switch to time domain data. This ensures that data is visible on the plot. Subsequent plot mode changes set the scale to the previous user selected value for a particular mode. |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Set the Mode combo-box to ‘Periodic’ or ‘Manual’ when a demonstration mode is selected. This ensures that the plot mode is appropriate for the data displayed during a demonstration loop.                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.2   | 8/21/2013    | Add sensor node selection tabs to Register Access and Alarm menus                                                                                                                                                         |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: First version posted online at www.analog.com/EVAL-ADIS                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 8/15/2013    | Updated register names to match the :adi:`adis16229` datasheet                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Increased period mode sleep cycle time to 10 seconds                                                                                                                                                                      |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 8/1/2013     | Initial Release                                                                                                                                                                                                           |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


REPORTED ISSUES, UPGRADE REQUESTS & SOLUTIONS
---------------------------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | #  | DATE     | STATUS    | DEVICE                                           | DESCRIPTION & RELATED NOTES                                                                                                                                                                                                                                                     | SOLUTION                                                                                                                                                                                                                       |
+==========+====+==========+===========+==================================================+=================================================================================================================================================================================================================================================================================+================================================================================================================================================================================================================================+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.1   | 01 | 7/29/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time mode does not work after executing an **Auto-null** command in the **Register Access** menu. `Click here for more details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-v1_3_1-problemreport_adis16228.pdf>`__                     | After executing an **Auto-null** command, select Manual FFT mode first, then **Real-time** mode.                                                                                                                               |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | 01 | 2/24/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time only supports data collection at a rate of 1.26kSPS                                                                                                                                                                                                                   | v1.4.0 will address this. For now, use AVG_CNT settings that are *>* 4 (Sample rate = 1260 SPS)                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 04 | 2/12/14  | CLOSED    | :adi:`ADIS16000`                                 | Connection with :adi:`ADIS16229` is hard to establish                                                                                                                                                                                                                           | SPI Timing violation, click here for more details                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 03 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | **Time Domain** mode in this package seems to translate into **Manual Time Capture** in the :adi:`ADIS16228` datasheet. Can the software be consistent with the datasheet?                                                                                                      | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 02 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | The **Data Capture** function does not appear to work when using **Time Domain** mode                                                                                                                                                                                           | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 01 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | When using the **Data Capture** function, when in **Real-Time** mode, can this produce one continuous file for the data samples?                                                                                                                                                | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 01 | 1/9/14   | CLOSED    | :adi:`ADIS16228`                                 | Add all of the FFT Header registers to the Data Capture file                                                                                                                                                                                                                    | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 06 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16228` datasheet                                                                                                                        | v1.1.9 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 05 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Exiting **Periodic FFT** mode causes the program to jump into the **Main Screen > Tools > USB Menu**. When closing that Window, it engages in a 10 second countdown while allowing no user input.                                                                               | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 04 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Changes in the Mode Selection drop-down menu, located in the **Main Screen**, do not seem to track the related register settings in the **Register Access** menu                                                                                                                | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 03 | 12/13/13 | CLOSED    | :adi:`ADIS16228`                                 | **Manual FFT** only seems to support 20480 SPS sample rates. For more details, click on the following file: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-manualfftmultrecord.pdf>`__ | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 02 | 12/10/13 | CLOSED    | :adi:`ADIS16228`                                 | The **Alarm Status Form** does not correctly display alarm status. Click on this file for more details: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-alarmstatusform.pdf>`__         | No issue found. Open this file for more details: `Problem Resolution Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemresolutionreport-v1-1-7-adis16228-alarmstatusform.pdf>`__ |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 01 | 12/10/13 | CLOSED    | :adi:`ADIS16227`                                 | **Periodic FFT** appears to lock the software up and does not appear to produce FFT results                                                                                                                                                                                     | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 06 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16000` datasheet                                                                                                                        | v1.1.10, release date estimate = 1/10/2014                                                                                                                                                                                     |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 05 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Not able to add :adi:`adis16229` devices to pages 2-6 in the :adi:`ADIS16000`                                                                                                                                                                                                   | No issue found, but this will be closely scrutinized in the next two versions: v1.1.10 and v1.2.0                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: This function was verified in earlier versions of the software. Re-test of this function is in the test queue.                                                                                                                                                             |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 04 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There are a number of cases where the software becomes non-responsive, with particular sensitivity observed when using Periodic FFT.                                                                                                                                            | v1.2.0, release date estimate = 1/24/2014. For present revision, use **Manual FFT** mode only.                                                                                                                                 |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: Investigation has revealed that the present approach for simultaneous sensor monitoring and user input management is not stable. The solution to this will require substantial code changes, which are in progress.                                                        |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 03 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Sample rate settings in the **AVG_CNT** register do not seem to cause updates on the horizontal axis, of the x-axis data.                                                                                                                                                       | Use version v1.1.9 or later.                                                                                                                                                                                                   |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 02 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | Real-time data logging is not working                                                                                                                                                                                                                                           | This was not part of the original plan for this package, but is under consideration for v1.4.0 or later.                                                                                                                       |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 01 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Waveforms updates do not always respond to **Start** button presses, in any mode.                                                                                                                                                                                               | Use v1.2.0 or later                                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **STATUS CODE DEFINITIONS**                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **OPEN** means that the issue observation has been received, but has not been independently confirmed by ADI                                                                                                                                                                    |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CONFIRMED** means that the issue has been independently confirmed and ADI is working on a solution path.                                                                                                                                                                      |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CLOSED** means that the issue has been resolved                                                                                                                                                                                                                               |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



LAUNCH SOFTWARE
---------------

EVAL-ADIS2 Vibration Evaluation Software User Guide
===================================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
-------------------------------------------------

The Vibration Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to a subset of iSensor products designed specifically for machine health and vibration monitoring applications. The platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition.

Due to the specialized nature of the machine health monitoring portfolio, only a subset of sensors is supported by this software. These devices are shown below.

+-------------------------------------------------------+


| SENSOR DEVICE NUMBER                                  |

+=======================================================+

| :adi:`ADIS16000AMLZ <ADIS16000>`  |

+-------------------------------------------------------+

| :adi:`ADIS16229AMLZ <ADIS16229>`  |

+-------------------------------------------------------+

| :adi:`ADIS16227/PCBZ <ADIS16227>` |

+-------------------------------------------------------+

| :adi:`ADIS16228/PCBZ <ADIS16228>` |

+-------------------------------------------------------+

.. important::

   The :adi:`ADIS16000AMLZ <ADIS16000>` manages wireless communication between several :adi:`ADIS16229AMLZ <ADIS16229>` devices.


.

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 Vibration Evaluation Software
--------------------------------------------------

Once the Vibration Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main.png
   :width: 700px

If an error similar to the image below pops up, click OK to proceed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-select-device.png
   :width: 400px

Device Selection
~~~~~~~~~~~~~~~~

Click on **Device**, located on the left side of the Menu bar, at the top of the **Main Screen**, and select the model number corresponding to your sensor. The :adi:`adis16228` was used for the following examples.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-device.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-main-select.png
   :width: 600px

.. important::

   Some menu options may appear "grayed out." This normal and indicates that some of the software features may not be available for the selected device type.

   
   For example, all of the **Network** options presently only apply :adi:`ADIS16229`.


Data Collection Mode
~~~~~~~~~~~~~~~~~~~~

The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic modes of data collection: Manual FFT, Automatic FFT, Manual Time (Time Domain) and Real-Time. Each of these modes can be configured using the **Register Access** window. For ease of use, the **Main Screen** offers a drop-down selection menu for these modes, along with a **Start** that kicks off a data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_modeselection_01b.png
   :width: 600px

Waveform Display
~~~~~~~~~~~~~~~~

The **Waveform Display** quickly displays the data read back from the sensor. The data format, units, etc. will automatically change based upon the selected data capture mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px

Enable Data Log
~~~~~~~~~~~~~~~

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-enable-datalog.png
   :width: 600px

RegisterAccess
~~~~~~~~~~~~~~

The **Register Access** option on the **Menu Bar** provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-reg-sel.png
   :width: 700px

The image below shows the **Register Access** window when an :adi:`ADIS16228` is connected.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_01.png
   :width: 600px

Reading Sensor Register
^^^^^^^^^^^^^^^^^^^^^^^

In order to read the contents of a sensor register, click on the register in the table and then click on "Read Selected Register." The :adi:`EVAL-ADIS2` will issue the correct commands to the sensor and update the GUI with the data the sensor responded with.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_01.png
   :width: 600px

Writing to Sensor Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following two steps to write a value to the register. 1. Enter the data to be written to the sensor in the text box shown below.

.. important::

   Register data must be written in hexadecimal format!


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_02.png
   :width: 600px

2. Click on **Write**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_regselect_03.png
   :width: 600px

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Single-Command Options
^^^^^^^^^^^^^^^^^^^^^^

The section on the right side of the window provides a means of easily calling subroutines within the connected sensor. Clicking on a "Write" button is equivalent to writing a single-bit command to the respective register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_01.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_singlecommand_02.png
   :width: 600px

Configuring Alarms
~~~~~~~~~~~~~~~~~~

The **Alarm > Alarm Settings** option on the **Menu Bar** provides a convenient means of configuring the Spectral Alarm functions. The interface makes configuring and tuning these functions much easier!

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-alrm.png
   :width: 600px

Selecting **Alarms > Alarm Settings** will cause the following window to open:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_01.png
   :width: 600px

Select boxes in the matrix and enter values that are associated with the magnitude of the output data and FFT bin numbers.

.. important::

   The same results can be achieved by issuing individual writes to the respective registers using the **Register Access** window.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_02.png
   :width: 600px

Click on **Write to DUT** to update all of the registers associated with these entries.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_03.png
   :width: 600px

In order to verify that the settings were written to the sensor, close and re-open the window. Doing so will reset the form. Click on **Read from DUT** to read back the configuration settings from the sensor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_04.png
   :width: 400px

The **Alarms > Alarm Status Form** provides a convenient way to monitor each of the different alarm conditions. The dashes in each cell will change to green (no alarm), yellow ("warning" alarm, associated with Level 1) or red ("critical" alarm, associated with Level 2), depending on the conditions, after a data capture event completes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_statusform_01.png
   :width: 400px

Data Capture
~~~~~~~~~~~~

The **Data Capture** window provides a means of configuring the file location, base file name, and file count for each data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_01.png
   :width: 600px

When the "Enable Data Log" check box in the main form is set, a data capture file will be saved every time a new FFT or time-domain capture is executed. The number located beside the "Enable Data Log" check box will also increment indicating that a new file was written to the host PC disk.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-datalog-file.png
   :width: 600px

This counter is also shown in the **Data Capture Window**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_datacapturewindow_02.png
   :width: 500px

Tools
~~~~~

The **Tools** option in the **Menu Bar** offers two options: **USB** and **SPI**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-tools-menu.png
   :width: 600px

The **USB** option allows for manually connecting or disconnecting the active :adi:`EVAL-ADIS2`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_01.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_02.png
   :width: 400px

The **SPI** option allows for adjusting the SPI SCLK and stall time (time between each 16-bit transaction). The image below shows the default settings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-spi-utilities.png
   :width: 400px

Demo
~~~~

Visit the :doc:`ADIS16229 Vibration Demo Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationdemo>` for more details on this function.

About
~~~~~

This option offers the revision and some codes that might be useful when seeking technical support.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-version-1-2.png
   :width: 400px

SOFTWARE REVISION HISTORY
-------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                                                                                                                        |
+==========+==============+===========================================================================================================================================================================================================================+
| v1.3.0   | 2/17/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 1/25/2014    | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 12/22/2013   | See the :doc:`Reported Issues & Solutions Table </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` for list of issues being addressed                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.8   | N/A          | Internal test version, never published online                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 12/10/2013   | Added partial support for the ADIS16227 (Manual FFT mode only)                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 11/1/2013    | Extended the wait time to 4 seconds, for each sensor in the Network Scan                                                                                                                                                  |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.5   | N/A          | This version corrects a sizing problem in the main waveforms, along with a couple of bugs in other windows.                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.4   | N/A          | Updates for internal use only                                                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.3   | N/A          | Added delays to Periodic Mode Exit routine register writes.                                                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.2   | N/A          | Added a dialog box for a user to specify the Update Interval of the Network Periodic Mode.                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 10/11/2013   | Corrected the GUI to indicate "not busy" after a communication is canceled by the user.                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Added exception handling routines to prevent a program crash and to show the Reconnect Dialog if the USB is disconnected.                                                                                                 |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.0001g                                                                                                                               |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | N/A          | Added "Scan All Channels" option to find nodes that are on different frequency channels                                                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Expanded the vertical axis range options on the FFT plots (Main Menu) to go down to 0.001g                                                                                                                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.3   | 9/10/2013    | Set the plot scale to +-2g for the first switch to time domain data. This ensures that data is visible on the plot. Subsequent plot mode changes set the scale to the previous user selected value for a particular mode. |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Set the Mode combo-box to ‘Periodic’ or ‘Manual’ when a demonstration mode is selected. This ensures that the plot mode is appropriate for the data displayed during a demonstration loop.                                |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.2   | 8/21/2013    | Add sensor node selection tabs to Register Access and Alarm menus                                                                                                                                                         |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: First version posted online at www.analog.com/EVAL-ADIS                                                                                                                                                             |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 8/15/2013    | Updated register names to match the :adi:`adis16229` datasheet                                                                                                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |              | Increased period mode sleep cycle time to 10 seconds                                                                                                                                                                      |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 8/1/2013     | Initial Release                                                                                                                                                                                                           |
+----------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>


REPORTED ISSUES, UPGRADE REQUESTS & SOLUTIONS
---------------------------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REVISION | #  | DATE     | STATUS    | DEVICE                                           | DESCRIPTION & RELATED NOTES                                                                                                                                                                                                                                                     | SOLUTION                                                                                                                                                                                                                       |
+==========+====+==========+===========+==================================================+=================================================================================================================================================================================================================================================================================+================================================================================================================================================================================================================================+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.1   | 01 | 7/29/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time mode does not work after executing an **Auto-null** command in the **Register Access** menu. `Click here for more details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-v1_3_1-problemreport_adis16228.pdf>`__                     | After executing an **Auto-null** command, select Manual FFT mode first, then **Real-time** mode.                                                                                                                               |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | 01 | 2/24/14  | CONFIRMED | :adi:`ADIS16228`                                 | Real-time only supports data collection at a rate of 1.26kSPS                                                                                                                                                                                                                   | v1.4.0 will address this. For now, use AVG_CNT settings that are *>* 4 (Sample rate = 1260 SPS)                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 04 | 2/12/14  | CLOSED    | :adi:`ADIS16000`                                 | Connection with :adi:`ADIS16229` is hard to establish                                                                                                                                                                                                                           | SPI Timing violation, click here for more details                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 03 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | **Time Domain** mode in this package seems to translate into **Manual Time Capture** in the :adi:`ADIS16228` datasheet. Can the software be consistent with the datasheet?                                                                                                      | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 02 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | The **Data Capture** function does not appear to work when using **Time Domain** mode                                                                                                                                                                                           | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 01 | 1/27/14  | CONFIRMED | :adi:`ADIS16228`                                 | When using the **Data Capture** function, when in **Real-Time** mode, can this produce one continuous file for the data samples?                                                                                                                                                | v1.3.0 (or later), Not released yet                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.9   | 01 | 1/9/14   | CLOSED    | :adi:`ADIS16228`                                 | Add all of the FFT Header registers to the Data Capture file                                                                                                                                                                                                                    | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 06 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16228` datasheet                                                                                                                        | v1.1.9 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 05 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Exiting **Periodic FFT** mode causes the program to jump into the **Main Screen > Tools > USB Menu**. When closing that Window, it engages in a 10 second countdown while allowing no user input.                                                                               | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 04 | 12/17/13 | CLOSED    | :adi:`ADIS16228`                                 | Changes in the Mode Selection drop-down menu, located in the **Main Screen**, do not seem to track the related register settings in the **Register Access** menu                                                                                                                | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 03 | 12/13/13 | CLOSED    | :adi:`ADIS16228`                                 | **Manual FFT** only seems to support 20480 SPS sample rates. For more details, click on the following file: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-manualfftmultrecord.pdf>`__ | v1.1.9 (or later).                                                                                                                                                                                                             |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 02 | 12/10/13 | CLOSED    | :adi:`ADIS16228`                                 | The **Alarm Status Form** does not correctly display alarm status. Click on this file for more details: `Problem Report Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemreport-v1-1-7-adis16228-alarmstatusform.pdf>`__         | No issue found. Open this file for more details: `Problem Resolution Details <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep-problemresolutionreport-v1-1-7-adis16228-alarmstatusform.pdf>`__ |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.7   | 01 | 12/10/13 | CLOSED    | :adi:`ADIS16227`                                 | **Periodic FFT** appears to lock the software up and does not appear to produce FFT results                                                                                                                                                                                     | v1.2.0 (or later)                                                                                                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 06 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There appear to be a few typos in the register names in **Register Access** menu, as they do not match the names given in the :adi:`ADIS16000` datasheet                                                                                                                        | v1.1.10, release date estimate = 1/10/2014                                                                                                                                                                                     |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 05 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Not able to add :adi:`adis16229` devices to pages 2-6 in the :adi:`ADIS16000`                                                                                                                                                                                                   | No issue found, but this will be closely scrutinized in the next two versions: v1.1.10 and v1.2.0                                                                                                                              |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: This function was verified in earlier versions of the software. Re-test of this function is in the test queue.                                                                                                                                                             |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 04 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | There are a number of cases where the software becomes non-responsive, with particular sensitivity observed when using Periodic FFT.                                                                                                                                            | v1.2.0, release date estimate = 1/24/2014. For present revision, use **Manual FFT** mode only.                                                                                                                                 |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | ADI: Investigation has revealed that the present approach for simultaneous sensor monitoring and user input management is not stable. The solution to this will require substantial code changes, which are in progress.                                                        |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 03 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Sample rate settings in the **AVG_CNT** register do not seem to cause updates on the horizontal axis, of the x-axis data.                                                                                                                                                       | Use version v1.1.9 or later.                                                                                                                                                                                                   |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 02 | 12/9/13  | CONFIRMED | :adi:`ADIS16000`                                 | Real-time data logging is not working                                                                                                                                                                                                                                           | This was not part of the original plan for this package, but is under consideration for v1.4.0 or later.                                                                                                                       |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v1.1.6   | 01 | 12/9/13  | CLOSED    | :adi:`ADIS16000`                                 | Waveforms updates do not always respond to **Start** button presses, in any mode.                                                                                                                                                                                               | Use v1.2.0 or later                                                                                                                                                                                                            |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **STATUS CODE DEFINITIONS**                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **OPEN** means that the issue observation has been received, but has not been independently confirmed by ADI                                                                                                                                                                    |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CONFIRMED** means that the issue has been independently confirmed and ADI is working on a solution path.                                                                                                                                                                      |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  | **CLOSED** means that the issue has been resolved                                                                                                                                                                                                                               |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          |    |          |           |                                                  |                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
+----------+----+----------+-----------+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



:doc:`Click here for an overview of Main Screen Features </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>`

ADIS16228 FUNCTION TUTORIALS
----------------------------

This section provides specific, "how-to" steps for exercising the many functions and user-configurable parameters available in the :adi:`ADIS16228`.

Fastest Path to Data
~~~~~~~~~~~~~~~~~~~~

For starters, here the quickest and easiest way to get a response from the :adi:`ADIS16228` is through the **Main Screen**, using the **Manual FFT** data collection mode.

After selecting the :adi:`ADIS16228` as the **Device** in the **Main Screen**, click on the **Start** button to trigger a set of FFT results on each axis.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_228_mainscreen_quickplot.png
   :width: 600px

Generating and Displaying Spectral Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Vibration Evaluation Program provides a large area for displaying both time and frequency domain data from the :adi:`ADIS16228`

The **Waveform Display** quickly displays the data read back from the sensor. The data format, units, etc. will automatically change based upon the selected data capture mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px


The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic modes of data collection: Manual FFT, Automatic FFT, Manual Time (Time Domain) and Real-Time. Each of these modes can be configured using the **Register Access** window. For ease of use, the **Main Screen** offers a drop-down selection menu for these modes, along with a **Start** that kicks off a data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_modeselection_01b.png
   :width: 600px


MANUAL FFT MODE
---------------

When using **Manual FFT** mode, the :adi:`ADIS16228` will collect and analyze data when prompted through a software or hardware "start" command. The **Start** button in the **Main Screen** causes the Vibration Evaluation Program (VEP) to send a software "start" command (set GLOB_CMD[11] = 1) to the :adi:`ADIS16228`. Through the **REC_CTRL** and **AVG_CNT** registers, the :adi:`ADIS16228` can support data record production on four different sample rates: SR0, SR1, SR2 and SR3. **REC_CTRL[11:8]]** provides on/off bits for each of these sample rates, while each nibble in the **AVG_CNT** provides a control entry for configuring these sample rates. In **Manual FFT** mode, each "trigger" will cause data production at one of the enabled rates, start with the lowest "" value (SRx), incrementing with each trigger/data production event.

Example #1 - Manual Mode FFT, One Sample Rate Example #2 - Manual Mode FFT, Four sample Rates

Data Capture
------------

Click on the following file links for examples on how to use the Data Capture function.

`ADIS16228 Data Capture Tutorial <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_adis16228_datacaptureexample.pdf>`__

Coming soon = Example with Alarms

VIBRATION EVALUATION PROGRAM TUTORIALS
--------------------------------------

Manual FFT Mode, Single Sample Rate

Manual FFT Mode, Single Sample Rate, with Alarms

Manual FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Manual FFT Mode, Four Sample Rate Scan

Manual FFT Mode, Four Sample Rate Scan, with Alarms

Manual FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

Periodic FFT Mode, Single Sample Rate

Periodic FFT Mode, Single Sample Rate, with Alarms

Periodic FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Periodic FFT Mode, Four Sample Rate Scan

Periodic FFT Mode, Four Sample Rate Scan, with Alarms

Periodic FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-mnt.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-part-dimensions.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-mating-connector.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-schematic.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-pcbz-parts.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-pcbz-j2-slide1.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-pcbz-j2-slide2.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-210mnt-holes.png
   :width: 500px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-eval-adis-unplugged-conn.png
   :width: 500px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-mounted-to-eval-adis.png
   :width: 500px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-on-eval-adis-closeup.png
   :width: 500px
