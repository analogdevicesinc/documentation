ADIS1613x EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
========

The ADIS1613x MEMS gyroscope family the following products: :adi:`ADIS16133BMLZ <ADIS16133>`, :adi:`ADIS16135 <ADIS16135BMLZ>`, :adi:`ADIS16136AMLZ <ADIS16136>` and :adi:`ADIS16137BMLZ <ADIS16137>`. All of these products provide low-profile, high-peformance MEMS gyroscopes that use a serial peripheral interface for data communications. This interface enables direct connection with a large variety of embedded processor products. The pin assignments for the :adi:`ADIS16133` and :adi:`ADIS16135` are identical. The :adi:`ADIS16136` and :adi:`ADIS16137 <ADIS16136>` provides four configurable I/O lines, while the other two products only provide one configurable I/O line, along with a dedidated clock input line (optional). Since these products use a serial peripheral interface (SPI) for it data communications interface, it connects directly to many embedded procoesor platforms, such as the :adi:`Blackfin DSP <blackfin>` series. For a generic example of this type of connection, click on the following reference:

-  :adi:`ADIS16136 Datasheet, Figure 10 <static/imported-files/data_sheets/ADIS16136.pdf#Page=08>`

ADIS16IMU1/PCBZ BREAKOUT BOARD
==============================

The ADIS16IMU1/PCBZ provides a simple method for connecting an existing processor system to the :adi:`ADIS16133BMLZ <ADIS16133>`, :adi:`ADIS16135BMLZ <ADIS16135>` :adi:`ADIS16136AMLZ <ADIS16136>` or :adi:`ADIS16137BMLZ <ADIS16137>`, using 1mm ribbon cables. Click on one of the following link for more information on this breakout boards.

:doc:`ADIS16IMU1/PCB Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb>`

NOTE: :adi:`ADIS16133BMLZ <ADIS16133>`, :adi:`ADIS16135BMLZ <ADIS16135>`, :adi:`ADIS16136AMLZ <ADIS16136>` and :adi:`ADIS16137BMLZ <ADIS16137>` are sold separately.

EVAL-ADIS: PC EVALUATION
========================

For those who would prefer to perform PC-based evaluation of the ADIS1613x products, before developing their own embedded system, the :adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system. Here is a list of equipment required for this:

:adi:`EVAL-ADISZ <EVAL-ADIS>`

:adi:`ADIS16136AMLZ <adis16136>`

NOTE: Substitute :adi:`ADIS16133BMLZ <adis16133>`, :adi:`ADIS16135BMLZ <adis16135>` or :adi:`ADIS16137BMLZ <ADIS16137>` for the :adi:`ADIS16136AMLZ <adis16136>`, as needed for specific application requirements.

SYSTEM REQUIREMENTS
===================

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the IMU Evaluation software package.

PHYSICAL SETUP
==============

The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm machine screws, which include 4 pieces that are in lengths of 16mm and 20mm. Using the 16mm version will only allow for 2mm of penetration into the EVAL-ADIS mouting holes, while the 20mm screws will result in the screws sticking out of the bottom side of the EVAL-ADIS, when fully-secured.

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the setup. Wait until the software installation is complete.

NOTE: The following pictures show the ADIS16488, not the ADIS1613x. The procedure will be the same, but when properly seated in the mating connector, the ADIS1613x devices will line up with different mounting holes.

Step #1
-------

Place the ADIS1613x device over the "C" mounting holes and align its connector with J4 on the :adi:`EVAL-ADIS`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-01.jpg
   :width: 400px

Step #2
-------

Once the alignment with J4 is correct, gently press the top of the ADIS1613xxMLZ unit down, so that its connector presses into J4. When the connector is fully seated, the ADIS1613xxMLZ will rest on the EVAL-ADIS surface. The following pictures provide a reference of how this setup will look when the ADIS1613xxMLZ has correct alignment with the mating connector on the :adi:`EVAL-ADIS`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02.jpg
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02b.jpg
   :width: 400px

This picture provides an example of the an incorrect connector alignment. Take care to avoid this type of connection error, because it can cause the the ADIS1613xxMLZ to experience harmful conditions. Notice the entire row of gold pins that are outside of the mating connector.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-03.jpg
   :width: 400px

Step #3
-------

Select the mounting screws. The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm machine screws, which include 4 pieces that are in lengths of 16mm and 20mm. Using the 16mm version will only allow for 2mm of penetration into the EVAL-ADIS mouting holes, while the 20mm screws will result in the screws sticking out of the bottom side of the EVAL-ADIS, when fully-secured.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-04.jpg
   :width: 400px

Step #4
-------

Use a screwdriver to secure all four screws into the appropriate mouting holes. Note that difficulty in getting the screws to penetrate the pre-tapped holes can be an indicator of connector misalignment.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-05.jpg
   :width: 400px

Step #5
-------

Set JP1 (:adi:`EVAL-ADIS`) to "+5V."

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-eval-adis-jp1.png
   :width: 400px

IMU EVALUATION SOFTWARE OVERVIEW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EVAL-ADIS2 Evaluation Software User Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
===========================================

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
============================================

Main Window
-----------

Once the IMU Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-01.png
   :width: 800px

The image below has been color-coded to illustrate the different parts of the IMU Evaluation Software. These colored sections will be referred to in the following sections.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-02.png
   :width: 800px

The drop-down menus highlighted in orange list additional features and utilities that make up the core functionality of the evaluation software.

- The **Devices** menu provides a list of supported products. Selecting a product from this list will configure the IMU evaluation software register map. Each device has a unique register map that must be selected to ensure proper sensor operation. The green box shows the active device. In this example, the :adi:`ADIS16448` is selected.

- The **Register Access** option calls a sub-menu that lists all user-configurable registers available from the part number selected in the "Devices" drop-down menu. It also provides read/write access to each register.

- The **Data Capture** option calls a sub-menu designed to enable synchronous data logging from the selected device.

- The **Demos** option calls a 3-D visualization tool. This feature is only supported for the :adi:`ADIS16480` and :adi:`ADIS16448` devices.

- The **Tools** option calls a sub-menu that displays USB diagnostic information.

- The **About** option provides more detailed software revision information.

The purple box shows the primary, inertial output registers for the selected device. These values are updated in real-time after pressing the **Read** button (identified by a red box).

The yellow box shows three waveform recorder windows. Each window allows for plotting the three primary sensor types (gyroscopes, accelerometers, and magnetometers [if supported]). The top subplot displays gyroscope data, the middle plot displays accelerometer data and the bottom plot displays magnetometer data. Each plot color corresponds to the colors displayed in the "Output Registers" window (highlighted in purple).

Register Access
---------------

The **Register Access** window provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-01.png
   :width: 800px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-02.png
   :width: 800px

The purple box sorts each set of registers into a standard category. The available categories are:

- **Control/Status** - General sensor configuration, alarm, and metadata registers

- **Output** - Inertial sensor output registers

- **Calibration** - User offset and misc. calibration registers

.. important::

   The calibration register section mentioned above **is separate from the factory calibration registers and procedures!**\


The section highlighted by the red box lists all of the registers in the selected category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection.

.. important::

   Registers must be written in hexadecimal format!


The **Update Registers in Category** button (shown in an orange box above) automatically reads all of the registers shown in the selected category (red box) and updates their contents in the GUI.

The section highlighted in yellow identifies provides a means of easily calling subroutines within the connected sensor. Clicking on a button is equivalent to writing a single-bit command to the respective register.

The **Save Reg Settings to File** programmatically reads and saves the contents of all of the registers in the current category into a \*.csv (common-delimited) file. The **Load Reg Settings from File** button reads a target .csv file and attempts to write the saved values back into the sensor.

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Data Capture
------------

The **Data Capture** window **only** supports synchronous data acquisition and logging to a file on the host PC. Data samples are only read from the sensor when the data ready pin toggles, indicating that data is valid.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-01.png
   :width: 500px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-02.png
   :width: 500px

The section highlighted in red lists all of the registers that are eligible for data capture. Checking the box next to each register indicates that the specified register values should be recorded once the data stream begins.

The section highlighted in green allows for customizing the file name and location of the resultant .csv files.

The section highlighted in yellow identifies the data stream configuration options.

- **Record Length** - The total number of samples to be captured. A sample is defined as a single "data valid" period as signaled by the data ready pin on the sensor

- **Sample Rate** - The instantaneous data ready rate as measured by the evaluation board

- **Capture Time** - The estimated data capture time in DD:HH:MM:SS format calculated based upon the instantaneous sample rate

- **Add File Header** - Selects whether a header displaying the contents of each column should be appended to the beginning of the .csv file

- **Use Scaled Data** - Signals to the software to convert the 16-bit values read from the sensor into a sign-adjusted (two's complement) scaled number. For example, when this option is enabled, be in units of degrees/second

Software Revision History
=========================



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                          |
+==========+==============+=============================================================================================================================+
| v1.14.3  | 8/5/15       | Adjust ADIS16210 registers to match recent datasheet updates                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.2  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.1  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.0  | 3/2/15       | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.13.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.12.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.11.1  | 4/9/14       | Updated Magnetometer recorder in the **Main Menu** for consistency across the ADIS16405, ADIS16407, ADIS16448 and ADIS16488 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.1  | 12/9/13      | Address reported issue with SYS_E_FLAG register missing from ADIS16485 and ADIS16488 Register Access Menu                   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.0  | 11/1/13      | Add support for the ADIS16137                                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Fix register access (GPIO_CTRL) in ADIS16209                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.8   | 8/27/2013    | Corrected a number of register definition issues on the ADIS16480                                                           |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.7   | 8/21/2013    | Corrected scale factors associated with GYRO_OUT/GYRO_OUT2 registers in the ADIS16133/5                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.6   | N/A          | Extended Precision Auto Null Wait time to 30 seconds on ADIS1636x/40x                                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.5   | N/A          | Corrected scale factors and offset factors associated with xTEMP_OUT on the ADIS16445                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors and offset factors associated with xTEMP_OUT and xMAGN_OUT registers in the ADIS16448               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.4   | N/A          | Enabled support for using an external clock on the ADIS16405                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.3   | 3/18/2013    | Added support for the ADIS16400 and ADIS16405                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.2   | 2/18/2013    | Changed the separation "de-limit" in the data captures file from a comma to a semicolon                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.0   | 1/16/2013    | Added support for the ADIS16209 and ADIS16210                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors associated with the xDELTVEL_xxx registers in the ADIS16480/5                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.1   | 12/18/2013   | Corrected a data capture error, which was observed in the ADIS16448, but could have impacted other products                 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.0   | 11/8/2013    | Added support for external clock use                                                                                        |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added support for the ADIS16266                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.7.0   | 10/1/12      | Added support for the ADIS16360, ADIS16362, ADIS16364, ADIS16365, and ADIS16367                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected a scaling issue for those who use "Turkey" as their regional setting.                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: Some sensitivity was still observed; some users in Turkey may need to change the regional setting to fully address.   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.6.0   | 9/3/12       | Added support for the ADIS16300 and ADIS16305                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.5.0   | 8/22/12      | Added support for the ADIS16445                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.4.0   | 7/18/12      | Added support for the ADIS1613, ADIS16135, ADIS16136 and ADIS16334                                                          |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | N/A          | Internal updates                                                                                                            |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 5/28/2012    | Added support for the ADIS16480                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added 3-D viewer for ADIS16480 demonstration                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 5/4/2012     | Updated register names for ADIS16448/ADIS16485 to match datasheet names                                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Data Capture: changed "Cancel" button to "Stop"                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | 4/6/2012     | Added support for the ADIS16485                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Improvements to Waveform Recorder appearance                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 3/27/2012    | Addressed issue to enable correct register values in the Register Access menu                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 3/24/2012    | Initial Release                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



USB Driver Installation
-----------------------

EVAL-ADIS2 Evaluation Software User Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
===========================================

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
============================================

Main Window
-----------

Once the IMU Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-01.png
   :width: 800px

The image below has been color-coded to illustrate the different parts of the IMU Evaluation Software. These colored sections will be referred to in the following sections.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-02.png
   :width: 800px

The drop-down menus highlighted in orange list additional features and utilities that make up the core functionality of the evaluation software.

- The **Devices** menu provides a list of supported products. Selecting a product from this list will configure the IMU evaluation software register map. Each device has a unique register map that must be selected to ensure proper sensor operation. The green box shows the active device. In this example, the :adi:`ADIS16448` is selected.

- The **Register Access** option calls a sub-menu that lists all user-configurable registers available from the part number selected in the "Devices" drop-down menu. It also provides read/write access to each register.

- The **Data Capture** option calls a sub-menu designed to enable synchronous data logging from the selected device.

- The **Demos** option calls a 3-D visualization tool. This feature is only supported for the :adi:`ADIS16480` and :adi:`ADIS16448` devices.

- The **Tools** option calls a sub-menu that displays USB diagnostic information.

- The **About** option provides more detailed software revision information.

The purple box shows the primary, inertial output registers for the selected device. These values are updated in real-time after pressing the **Read** button (identified by a red box).

The yellow box shows three waveform recorder windows. Each window allows for plotting the three primary sensor types (gyroscopes, accelerometers, and magnetometers [if supported]). The top subplot displays gyroscope data, the middle plot displays accelerometer data and the bottom plot displays magnetometer data. Each plot color corresponds to the colors displayed in the "Output Registers" window (highlighted in purple).

Register Access
---------------

The **Register Access** window provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-01.png
   :width: 800px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-02.png
   :width: 800px

The purple box sorts each set of registers into a standard category. The available categories are:

- **Control/Status** - General sensor configuration, alarm, and metadata registers

- **Output** - Inertial sensor output registers

- **Calibration** - User offset and misc. calibration registers

.. important::

   The calibration register section mentioned above **is separate from the factory calibration registers and procedures!**\


The section highlighted by the red box lists all of the registers in the selected category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection.

.. important::

   Registers must be written in hexadecimal format!


The **Update Registers in Category** button (shown in an orange box above) automatically reads all of the registers shown in the selected category (red box) and updates their contents in the GUI.

The section highlighted in yellow identifies provides a means of easily calling subroutines within the connected sensor. Clicking on a button is equivalent to writing a single-bit command to the respective register.

The **Save Reg Settings to File** programmatically reads and saves the contents of all of the registers in the current category into a \*.csv (common-delimited) file. The **Load Reg Settings from File** button reads a target .csv file and attempts to write the saved values back into the sensor.

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Data Capture
------------

The **Data Capture** window **only** supports synchronous data acquisition and logging to a file on the host PC. Data samples are only read from the sensor when the data ready pin toggles, indicating that data is valid.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-01.png
   :width: 500px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-02.png
   :width: 500px

The section highlighted in red lists all of the registers that are eligible for data capture. Checking the box next to each register indicates that the specified register values should be recorded once the data stream begins.

The section highlighted in green allows for customizing the file name and location of the resultant .csv files.

The section highlighted in yellow identifies the data stream configuration options.

- **Record Length** - The total number of samples to be captured. A sample is defined as a single "data valid" period as signaled by the data ready pin on the sensor

- **Sample Rate** - The instantaneous data ready rate as measured by the evaluation board

- **Capture Time** - The estimated data capture time in DD:HH:MM:SS format calculated based upon the instantaneous sample rate

- **Add File Header** - Selects whether a header displaying the contents of each column should be appended to the beginning of the .csv file

- **Use Scaled Data** - Signals to the software to convert the 16-bit values read from the sensor into a sign-adjusted (two's complement) scaled number. For example, when this option is enabled, be in units of degrees/second

Software Revision History
=========================



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                          |
+==========+==============+=============================================================================================================================+
| v1.14.3  | 8/5/15       | Adjust ADIS16210 registers to match recent datasheet updates                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.2  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.1  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.0  | 3/2/15       | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.13.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.12.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.11.1  | 4/9/14       | Updated Magnetometer recorder in the **Main Menu** for consistency across the ADIS16405, ADIS16407, ADIS16448 and ADIS16488 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.1  | 12/9/13      | Address reported issue with SYS_E_FLAG register missing from ADIS16485 and ADIS16488 Register Access Menu                   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.0  | 11/1/13      | Add support for the ADIS16137                                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Fix register access (GPIO_CTRL) in ADIS16209                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.8   | 8/27/2013    | Corrected a number of register definition issues on the ADIS16480                                                           |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.7   | 8/21/2013    | Corrected scale factors associated with GYRO_OUT/GYRO_OUT2 registers in the ADIS16133/5                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.6   | N/A          | Extended Precision Auto Null Wait time to 30 seconds on ADIS1636x/40x                                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.5   | N/A          | Corrected scale factors and offset factors associated with xTEMP_OUT on the ADIS16445                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors and offset factors associated with xTEMP_OUT and xMAGN_OUT registers in the ADIS16448               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.4   | N/A          | Enabled support for using an external clock on the ADIS16405                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.3   | 3/18/2013    | Added support for the ADIS16400 and ADIS16405                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.2   | 2/18/2013    | Changed the separation "de-limit" in the data captures file from a comma to a semicolon                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.0   | 1/16/2013    | Added support for the ADIS16209 and ADIS16210                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors associated with the xDELTVEL_xxx registers in the ADIS16480/5                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.1   | 12/18/2013   | Corrected a data capture error, which was observed in the ADIS16448, but could have impacted other products                 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.0   | 11/8/2013    | Added support for external clock use                                                                                        |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added support for the ADIS16266                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.7.0   | 10/1/12      | Added support for the ADIS16360, ADIS16362, ADIS16364, ADIS16365, and ADIS16367                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected a scaling issue for those who use "Turkey" as their regional setting.                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: Some sensitivity was still observed; some users in Turkey may need to change the regional setting to fully address.   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.6.0   | 9/3/12       | Added support for the ADIS16300 and ADIS16305                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.5.0   | 8/22/12      | Added support for the ADIS16445                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.4.0   | 7/18/12      | Added support for the ADIS1613, ADIS16135, ADIS16136 and ADIS16334                                                          |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | N/A          | Internal updates                                                                                                            |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 5/28/2012    | Added support for the ADIS16480                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added 3-D viewer for ADIS16480 demonstration                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 5/4/2012     | Updated register names for ADIS16448/ADIS16485 to match datasheet names                                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Data Capture: changed "Cancel" button to "Stop"                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | 4/6/2012     | Added support for the ADIS16485                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Improvements to Waveform Recorder appearance                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 3/27/2012    | Addressed issue to enable correct register values in the Register Access menu                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 3/24/2012    | Initial Release                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



IMU EVALUATION SOFTWARE GETTING STARTED
---------------------------------------

EVAL-ADIS2 Evaluation Software User Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
==================

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
===========================================

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
============================================

Main Window
-----------

Once the IMU Evaluation software loads, you should be presented with a window similar to the image shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-01.png
   :width: 800px

The image below has been color-coded to illustrate the different parts of the IMU Evaluation Software. These colored sections will be referred to in the following sections.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-imueval-softguide-02.png
   :width: 800px

The drop-down menus highlighted in orange list additional features and utilities that make up the core functionality of the evaluation software.

- The **Devices** menu provides a list of supported products. Selecting a product from this list will configure the IMU evaluation software register map. Each device has a unique register map that must be selected to ensure proper sensor operation. The green box shows the active device. In this example, the :adi:`ADIS16448` is selected.

- The **Register Access** option calls a sub-menu that lists all user-configurable registers available from the part number selected in the "Devices" drop-down menu. It also provides read/write access to each register.

- The **Data Capture** option calls a sub-menu designed to enable synchronous data logging from the selected device.

- The **Demos** option calls a 3-D visualization tool. This feature is only supported for the :adi:`ADIS16480` and :adi:`ADIS16448` devices.

- The **Tools** option calls a sub-menu that displays USB diagnostic information.

- The **About** option provides more detailed software revision information.

The purple box shows the primary, inertial output registers for the selected device. These values are updated in real-time after pressing the **Read** button (identified by a red box).

The yellow box shows three waveform recorder windows. Each window allows for plotting the three primary sensor types (gyroscopes, accelerometers, and magnetometers [if supported]). The top subplot displays gyroscope data, the middle plot displays accelerometer data and the bottom plot displays magnetometer data. Each plot color corresponds to the colors displayed in the "Output Registers" window (highlighted in purple).

Register Access
---------------

The **Register Access** window provides read and write access to all user-accessible registers listed in the selected device's datasheet. The image below shows a screenshot of the window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-01.png
   :width: 800px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-registeraccess-02.png
   :width: 800px

The purple box sorts each set of registers into a standard category. The available categories are:

- **Control/Status** - General sensor configuration, alarm, and metadata registers

- **Output** - Inertial sensor output registers

- **Calibration** - User offset and misc. calibration registers

.. important::

   The calibration register section mentioned above **is separate from the factory calibration registers and procedures!**\


The section highlighted by the red box lists all of the registers in the selected category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection.

.. important::

   Registers must be written in hexadecimal format!


The **Update Registers in Category** button (shown in an orange box above) automatically reads all of the registers shown in the selected category (red box) and updates their contents in the GUI.

The section highlighted in yellow identifies provides a means of easily calling subroutines within the connected sensor. Clicking on a button is equivalent to writing a single-bit command to the respective register.

The **Save Reg Settings to File** programmatically reads and saves the contents of all of the registers in the current category into a \*.csv (common-delimited) file. The **Load Reg Settings from File** button reads a target .csv file and attempts to write the saved values back into the sensor.

.. important::

   The **Register Access** form **always** writes to both the upper and lower bytes of a given register. When writing to a register, make sure to include the desired 16-bit value in hexadecimal format **before** clicking the **Write Register** button.


Data Capture
------------

The **Data Capture** window **only** supports synchronous data acquisition and logging to a file on the host PC. Data samples are only read from the sensor when the data ready pin toggles, indicating that data is valid.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-01.png
   :width: 500px

The color-coded image below is referenced in the following section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x-imu-eval-datacapture-02.png
   :width: 500px

The section highlighted in red lists all of the registers that are eligible for data capture. Checking the box next to each register indicates that the specified register values should be recorded once the data stream begins.

The section highlighted in green allows for customizing the file name and location of the resultant .csv files.

The section highlighted in yellow identifies the data stream configuration options.

- **Record Length** - The total number of samples to be captured. A sample is defined as a single "data valid" period as signaled by the data ready pin on the sensor

- **Sample Rate** - The instantaneous data ready rate as measured by the evaluation board

- **Capture Time** - The estimated data capture time in DD:HH:MM:SS format calculated based upon the instantaneous sample rate

- **Add File Header** - Selects whether a header displaying the contents of each column should be appended to the beginning of the .csv file

- **Use Scaled Data** - Signals to the software to convert the 16-bit values read from the sensor into a sign-adjusted (two's complement) scaled number. For example, when this option is enabled, be in units of degrees/second

Software Revision History
=========================



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                          |
+==========+==============+=============================================================================================================================+
| v1.14.3  | 8/5/15       | Adjust ADIS16210 registers to match recent datasheet updates                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.2  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.1  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.0  | 3/2/15       | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.13.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.12.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.11.1  | 4/9/14       | Updated Magnetometer recorder in the **Main Menu** for consistency across the ADIS16405, ADIS16407, ADIS16448 and ADIS16488 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.1  | 12/9/13      | Address reported issue with SYS_E_FLAG register missing from ADIS16485 and ADIS16488 Register Access Menu                   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.0  | 11/1/13      | Add support for the ADIS16137                                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Fix register access (GPIO_CTRL) in ADIS16209                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.8   | 8/27/2013    | Corrected a number of register definition issues on the ADIS16480                                                           |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.7   | 8/21/2013    | Corrected scale factors associated with GYRO_OUT/GYRO_OUT2 registers in the ADIS16133/5                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.6   | N/A          | Extended Precision Auto Null Wait time to 30 seconds on ADIS1636x/40x                                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.5   | N/A          | Corrected scale factors and offset factors associated with xTEMP_OUT on the ADIS16445                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors and offset factors associated with xTEMP_OUT and xMAGN_OUT registers in the ADIS16448               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.4   | N/A          | Enabled support for using an external clock on the ADIS16405                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.3   | 3/18/2013    | Added support for the ADIS16400 and ADIS16405                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.2   | 2/18/2013    | Changed the separation "de-limit" in the data captures file from a comma to a semicolon                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.0   | 1/16/2013    | Added support for the ADIS16209 and ADIS16210                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors associated with the xDELTVEL_xxx registers in the ADIS16480/5                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.1   | 12/18/2013   | Corrected a data capture error, which was observed in the ADIS16448, but could have impacted other products                 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.0   | 11/8/2013    | Added support for external clock use                                                                                        |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added support for the ADIS16266                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.7.0   | 10/1/12      | Added support for the ADIS16360, ADIS16362, ADIS16364, ADIS16365, and ADIS16367                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected a scaling issue for those who use "Turkey" as their regional setting.                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: Some sensitivity was still observed; some users in Turkey may need to change the regional setting to fully address.   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.6.0   | 9/3/12       | Added support for the ADIS16300 and ADIS16305                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.5.0   | 8/22/12      | Added support for the ADIS16445                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.4.0   | 7/18/12      | Added support for the ADIS1613, ADIS16135, ADIS16136 and ADIS16334                                                          |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | N/A          | Internal updates                                                                                                            |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 5/28/2012    | Added support for the ADIS16480                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added 3-D viewer for ADIS16480 demonstration                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 5/4/2012     | Updated register names for ADIS16448/ADIS16485 to match datasheet names                                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Data Capture: changed "Cancel" button to "Stop"                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | 4/6/2012     | Added support for the ADIS16485                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Improvements to Waveform Recorder appearance                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 3/27/2012    | Addressed issue to enable correct register values in the Register Access menu                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 3/24/2012    | Initial Release                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



IMU EVALUATION SOFTWARE REVISION HISTORY
----------------------------------------



.. raw:: html

   <details><summary>Click to expand</summary>

+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| REVISION | RELEASE DATE | SUMMARY OF UPDATES                                                                                                          |
+==========+==============+=============================================================================================================================+
| v1.14.3  | 8/5/15       | Adjust ADIS16210 registers to match recent datasheet updates                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.2  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.1  | TBD          | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.14.0  | 3/2/15       | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.13.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.12.0  |              | Internal update                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.11.1  | 4/9/14       | Updated Magnetometer recorder in the **Main Menu** for consistency across the ADIS16405, ADIS16407, ADIS16448 and ADIS16488 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.1  | 12/9/13      | Address reported issue with SYS_E_FLAG register missing from ADIS16485 and ADIS16488 Register Access Menu                   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.10.0  | 11/1/13      | Add support for the ADIS16137                                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Fix register access (GPIO_CTRL) in ADIS16209                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.8   | 8/27/2013    | Corrected a number of register definition issues on the ADIS16480                                                           |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.7   | 8/21/2013    | Corrected scale factors associated with GYRO_OUT/GYRO_OUT2 registers in the ADIS16133/5                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.6   | N/A          | Extended Precision Auto Null Wait time to 30 seconds on ADIS1636x/40x                                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.5   | N/A          | Corrected scale factors and offset factors associated with xTEMP_OUT on the ADIS16445                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors and offset factors associated with xTEMP_OUT and xMAGN_OUT registers in the ADIS16448               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.4   | N/A          | Enabled support for using an external clock on the ADIS16405                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.3   | 3/18/2013    | Added support for the ADIS16400 and ADIS16405                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.2   | 2/18/2013    | Changed the separation "de-limit" in the data captures file from a comma to a semicolon                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.9.0   | 1/16/2013    | Added support for the ADIS16209 and ADIS16210                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected scale factors associated with the xDELTVEL_xxx registers in the ADIS16480/5                                       |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.1   | 12/18/2013   | Corrected a data capture error, which was observed in the ADIS16448, but could have impacted other products                 |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.8.0   | 11/8/2013    | Added support for external clock use                                                                                        |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added support for the ADIS16266                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.7.0   | 10/1/12      | Added support for the ADIS16360, ADIS16362, ADIS16364, ADIS16365, and ADIS16367                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Corrected a scaling issue for those who use "Turkey" as their regional setting.                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: Some sensitivity was still observed; some users in Turkey may need to change the regional setting to fully address.   |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.6.0   | 9/3/12       | Added support for the ADIS16300 and ADIS16305                                                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.5.0   | 8/22/12      | Added support for the ADIS16445                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.4.0   | 7/18/12      | Added support for the ADIS1613, ADIS16135, ADIS16136 and ADIS16334                                                          |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.3.0   | N/A          | Internal updates                                                                                                            |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | NOTE: This version was not posted online, but these updates are in current versions                                         |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.2.0   | 5/28/2012    | Added support for the ADIS16480                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Added 3-D viewer for ADIS16480 demonstration                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.1   | 5/4/2012     | Updated register names for ADIS16448/ADIS16485 to match datasheet names                                                     |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Data Capture: changed "Cancel" button to "Stop"                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.1.0   | 4/6/2012     | Added support for the ADIS16485                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
|          |              | Improvements to Waveform Recorder appearance                                                                                |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.1   | 3/27/2012    | Addressed issue to enable correct register values in the Register Access menu                                               |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+
| v1.0.0   | 3/24/2012    | Initial Release                                                                                                             |
+----------+--------------+-----------------------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </details>



APPLICATION TIP: The **Register Acess** screen writes to user control registers, inside of the ADIS1613x devices, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the ADIS1613x devices, each command (16-bits) writes to one byte at a time.
