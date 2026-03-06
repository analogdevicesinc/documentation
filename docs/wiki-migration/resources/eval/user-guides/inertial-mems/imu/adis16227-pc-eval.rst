ADIS16227 EVALUATION ON A PERSONAL COMPUTER
===========================================

The :doc:`Vibration Evaluation Program </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>` enables PC-based evaluation of the :adi:`ADIS16227CMLZ <ADIS16227>`, using the following hardware: :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` breakout board and :adi:`EVAL-ADIS` evaluation system. Please the following picture for an example of how to use these two devices together for this purpose.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-eval-adis-setup.png
   :align: left
   :width: 300px

PART NUMBERS TO ORDER
=====================

:adi:`Click here to start the online ordering process <en/mems-sensors/mems-accelerometers/adis16227/products/product.html#product-samples>` for the following two parts, or contact your ADI distributor to place the order.

:adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`

:adi:`EVAL-ADISZ <EVAL-ADIS>`

SOFTWARE TO DOWNLOAD
====================

EVAL-ADIS2 Vibration Evaluation Software User Guide
---------------------------------------------------

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
=================================================

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
==================================================

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
=========================



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
=============================================



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



PC SYSTEM REQUIREMENTS
======================

EVAL-ADIS2 Vibration Evaluation Software User Guide
---------------------------------------------------

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
=================================================

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
==================================================

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
=========================



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
=============================================



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



ADIS16227/PCBZ CONTENTS & SETUP
===============================

The :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` kit comes with the following materials: (1) ADIS16227CMLZ, (1) interface PCB, (10) M2x0.4x6mm machine screws and (1)10-32 x 3/8" flat socket head screw.

Installing the :adi:`ADIS16227CMLZ <ADIS16227>` onto the interface PCB requires two simple steps:

**Step #1**

Secure the :adi:`ADIS16227CMLZ <ADIS16227>` to the interface board, using the 10-32 x 3/8" flat socket head machine screw.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-mnt-with-10-32-screw.png
   :width: 300px

**Step #2**

Insert the :adi:`ADIS16227CMLZ's <ADIS16227>` flex connector into the mating connector on the interface board, then close the clasp to secure the connection. For more details on this process, please :ez:`click here to see a video demonstration <docs/DOC-2672>`

EVAL-ADISZ SETUP
================

Use the following two steps to configure the :adi:`EVAL-ADISZ <EVAL-ADIS>` for use with the :adi:`ADIS16227/PCBZ <ADIS16227>`:

**Step #1**

Connect J1 on the :adi:`EVAL-ADISZ <EVAL-ADIS>` to J1 on the :adi:`ADIS16227/PCBZ <ADIS16227>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-j1-cable.png
   :width: 300px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-eval-adis-setup.png
   :width: 300px

NOTE: The ribbon cable in this example is not included with the :adi:`EVAL-ADIS` or :adi:`ADIS16227/PCBZ <ADIS16227>`. For more information on where to acquire these types of cables, :ez:`Click here <mems/w/documents/4496/faq-adis16228-pcbz-breakout-board-cables>`.

**Step #2**

Set JP1 to +3.3V

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-jp1-setting-02.jpg
   :width: 300px

USB DRIVER INSTALLATION
=======================

EVAL-ADIS2 Vibration Evaluation Software User Guide
---------------------------------------------------

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
=================================================

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
==================================================

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
=========================



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
=============================================



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



VIBRATION EVALUATION PROGRAM OVERVIEW
=====================================

This section provides a basic description of the functions in the Vibration Evaluation Software package. For a list of `ADIS16227-specific tutorials <https://wiki.analog.com/>`__ that provided detailed, step-by-step instructions for the most common :adi:`ADIS16227` evaluation functions, please `click here <https://wiki.analog.com/>`__.

LAUNCH SOFTWARE
===============

EVAL-ADIS2 Vibration Evaluation Software User Guide
---------------------------------------------------

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
=================================================

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
==================================================

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
=========================



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
=============================================



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



Device Selection
~~~~~~~~~~~~~~~~

Click on **Device**, located on the left hand side of the Menu bar, at the top of the **Main Screen**, to select the appropriate DUT (Device Under Test). In this example, the :adi:`adis16227` is in use. Note that some of the Menu bar options appear in a lighter gray color, to indicate that they are not associated with a particular device. For example, all of the **Network** options presently only apply to the :adi:`adis16229` at this time, so they will appear in the lighter gray color when either :adi:`ADIS16227` or [adi>adsi16228|ADIS16228]] options are in use.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_deviceselection_01.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-select.png
   :align: left
   :width: 600px

Register Access
~~~~~~~~~~~~~~~

The **Register Access** option on the **Menu Bar** provides direct read and write access to all of the user-accessible registers in DUT.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_mainscreen_registeraccess_01.png
   :width: 600px

Register Access Window Appearance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example of the **Register Access** window that illustrates the :adi:`ADIS16228`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_registeraccesswindow_01.png
   :width: 600px

Reading Register Contents
^^^^^^^^^^^^^^^^^^^^^^^^^

Select a specific register to read the contents.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-registers.png
   :width: 600px

Writing Data to Registers
^^^^^^^^^^^^^^^^^^^^^^^^^

Use the following two steps to write a value to the register. 1. Enter the hex code for the register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-reg-new-hex-value.png
   :width: 600px

2. Click on **Write**

NOTE: Clicking on **Write** causes the Vibration Evaluation Program to write to both upper and lower bytes

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-reg-write.png
   :width: 600px

Single-Command Options
^^^^^^^^^^^^^^^^^^^^^^

The vibration sensor products often come with registers that support "Global Commands." While these commands are associated with specific bits, located in user-accessible registers, the right side of the **Register Access** Window provides access to them through a drop down menu that offers each related register and a series of **Write** buttons.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-glob-comm-button.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-glob-cmd-writes.png
   :width: 600px

Network
~~~~~~~

Coming soon.....

Alarms
~~~~~~

The **Alarm > Alarm Settings** option on the **Menu Bar** provides a more convenient method for configuring the Spectral Alarm functions. This provides a more convenient method for tuning this function, in comparison with the single-register access method associated with **Register Access** window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-start.png
   :width: 600px

Selecting **Alarms > Alarm Settings** will cause the following window to open:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_01.png
   :width: 600px

Select boxes in the matrix and enter values that are associated with the magnitude of the output data and FFT bin numbers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_02.png
   :width: 600px

Click on **Write to DUT** to update all registers that are associated with these entries.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_03.png
   :width: 600px

Close this window, then go back in. The values will not appear automatically. Click on **Read from DUT** to make sure the settings are still in place.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_settings_04.png
   :width: 600px

The **Alarms > Alarm Status Form** option provides a convenient monitor for the conditions. The dashes will change to green (no alarm), yellow ("warning" alarm, associated with Level 1) or red ("critical" alarm, associated with Level 2), depending on the conditions, after a data capture event completes.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_alarms_statusform_01.png
   :width: 400px

Data Capture
~~~~~~~~~~~~

The **Data Capture** window provides user inputs for file location, base file name and for resetting the file count.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-data-cap.png
   :width: 500px

When this function is active (See the :doc:`Enable Data Capture checkbox </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>`, located in the **Main Screen**), each trigger will cause the creation of a new file that contains the FFT result and FFT Header information. Notice the increments in the file count, after three clicks on the **Start** button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-datalog-file.png
   :width: 600px

This counter is also in the **Data Capture Window**

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-data-file-cnt.png
   :width: 500px

Tools
~~~~~

The **Tools** option in the **Menu Bar** offers two options: **USB** and **SPI**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-tools-menu.png
   :width: 600px

Use the **USB** option to manually connect or disconnect to the USB port on the :adi:`eval-adis`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_01.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/vep_wiki_tools_usb_02.png
   :width: 400px

Use the **SPI** option to adjust the timing in between the :adi:`EVAL-ADIS` and the DUT. this should not be required for normal operation but the "typical" settings are offered in the following picture:

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

Data Collection Mode
~~~~~~~~~~~~~~~~~~~~

The :adi:`ADIS16227`, :adi:`ADIS16228` and :adi:`ADIS16229` all have four basic modes of data collection: manual time domain, manual FFT, automatic FFT and automatic time domain. Inside of these products, these modes are typically related to the settings in the REC_CTRL1 register. The **Main Screen** offers a drop-down selection menu for these modes, along with a **Start** button to begin operation. At this time, only use the **Manual FFT** or **Manual Time Domain** modes in the **Main Screen**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-man-fft.png
   :width: 600px

Waveform Display
~~~~~~~~~~~~~~~~

The **Waveform Display** enables quick access to sensor data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-wavfrms.png
   :width: 600px

KEY PROGRAM FEATURES
====================

The follow sections provide a basic description of each function inside of the Vibration Evaluation Program.

`Click here to access a list of ADIS16228 Tutorials with the Vibration Evaluation Program <https://wiki.analog.com/[/resources/eval/user-guides/inertial-mems/imu/adis16228-pc-eval>`__

EVAL-ADIS2 Vibration Evaluation Software User Guide
---------------------------------------------------

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/Vibration_Evaluation.zip>` to download the latest version of the Vibration Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`__.


EVAL-ADIS2 Vibration Evaluation Software Overview
=================================================

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
==================================================

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
=========================



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
=============================================



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



ADIS16227 EVALUATION TUTORIALS
==============================

For specific, step-by-step instructions for evaluating the :adi:`ADIS16227`, click on the following tutorials. Please note that this is under construction. These tutorials will update often. For specific tutorial requests, please post them in the :ez:`MEMS Community, inside of the Engineer Zone <community/mems>`.

`ADIS16228 Register Configuration Tutorial <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-regaccess_01.pdf>`__

`ADIS16228 Manual FFT Tutorial, Single Sample Rate <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_singlesrx_01.pdf>`__

`ADIS16228 Manual FFT Tutorial, Four Sample Rate Scan <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_foursrx_01.pdf>`__

`ADIS16228 Manual FFT Tutorial, Single Sample Rate, with Alarms <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_singlesrx_alarms_01.pdf>`__

`ADIS16228 Manual FFT Mode, Four Sample Rate Scan, with Alarms <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16228-eval-tutor-manfft_multisrx_alarms.pdf>`__

**Future Tutorials**

ADIS16228 FFT Records Demo, using Data Capture

Manual FFT Mode, Single Sample Rate, with Alarms, with Data Capture

Manual FFT Mode, Four Sample Rate Scan, with Alarms, with Data Capture

Periodic FFT Mode, Single Sample Rate

Periodic FFT Mode, Single Sample Rate, with Alarms
