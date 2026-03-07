ADIS16265 EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
--------

The :adi:`ADIS16265` is a fully calibrated, digital gyroscope provides +/-320 degrees/second of measurement range. The standard supply voltage (+5V) and serial peripheral interface (SPI) enable simple integration into most industrial system designs. A simple internal register structure handles all output data and configuration features. This includes access to the following output data: calibrated rotation rate, power supply, internal temperature, auxiliary analog and digital input signals, diagnostic error flags, and programmable alarm conditions.

The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265logic-lines_.png
   :width: 500px

ADIS16265/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16265` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` is the breakout board for the :adi:`ADIS16265` and may provide assistance in the process of hooking it up to an existing embedded processor system.

EQUIPMENT LIST
--------------

:adi:`EVAL-ADIS`

:adi:`ADIS16265/PCBZ <EVAL-ADIS16265>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the IMU Evaluation software package.

PHYSICAL SETUP
--------------

The :adi:`ADIS16265` provides the :adi:`EVAL-ADIS16265 <ADIS16265>` function on a 1.2 inch × 1.3 inch printed circuit board (PCB), which simplifies the connection to an existing processor system. The four mounting holes accommodate either M2 (2mm) or Type 2-56 machine screws. These boards are made of IS410 material and are 0.063 inches thick. The second level assembly uses a SAC305-compatible solder composition (Pb-free), which has a pre-solder re-flow thickness of approximately 0.005 inches. The pad pattern on the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` matches that shown in below. J1 and J2 are dual-row, 2 mm (pitch) connectors that work with a number of ribbon cable systems, including 3M Part Number 152212-0100-GB (ribbon-crimp connector) and 3M Part Number 3625/12 (ribbon cable).

|image1| |image2|

.. container:: center round box

   **NOTE:** Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the setup. Wait until the software installation is complete.


Step #1
~~~~~~~

The connection to the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` is simple using J1 and a 16 pin cable included with the :adi:`EVAL-ADIS`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265pcbz.png
   :align: center
   :width: 600px

.. warning::

   **WARNING:** Make sure that the connector cable going from J1 on the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` is properly aligned to the J1 connector on the :adi:`EVAL-ADIS`. The 16 pin cable is included with the :adi:`EVAL-ADIS` and proper mating has the last 4 cable connections open. The Black wire from from J2-12 of the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` to the DIO1 test point on the :adi:`EVAL-ADIS` is only required for synchronous data.


|image3| |image4|

Step #2
~~~~~~~

Mounting to the system frame is accomplished using 4 M2x.4x4mm machine screws included with the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>`. The mounting location holes are marked as an example in the picture below. Use the 4 A-location holes to secure the :adi:`ADIS16265/PCBZ <EVAL-ADIS16265>` to the :adi:`EVAL-ADIS`.

|image5| |image6|

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). That is not the correct JP1 jumper setting on the :adi:`EVAL-ADIS`) required for the :adi:`ADIS16265CCCZ <EVAL-ADIS16265>`\ and should be moved to the **\*+5V**\ \* position (right side).

|image7| |image8|

.. container:: center round box

   **NOTE:** If JP1 is left on **+3.3v** position the software will look like the following picture. Move JP1 to the\ **+5V** setting to correct the problem.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265-main-low-voltage.png
   :width: 600px

IMU EVALUATION SOFTWARE OVERVIEW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

EVAL-ADIS2 Evaluation Software User Guide
=========================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
-------------------------------------------

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
--------------------------------------------

Main Window
~~~~~~~~~~~

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
~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~

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
-------------------------



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
~~~~~~~~~~~~~~~~~~~~~~~

EVAL-ADIS2 Evaluation Software User Guide
=========================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
-------------------------------------------

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
--------------------------------------------

Main Window
~~~~~~~~~~~

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
~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~

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
-------------------------



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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EVAL-ADIS2 Evaluation Software User Guide
=========================================

.. warning::

   The :adi:`EVAL-ADIS2` has been superseded by the :adi:`EVAL-ADIS-FX3` and is **no longer supported**.


.. warning::

   This guide assumes that you've connected your vibration sensor to the :adi:`EVAL-ADIS2`, drivers were successfully installed on your PC, and you've downloaded the correct software for your sensor. We recommend reviewing the :doc:`Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` before continuing.


Software Downloads
------------------

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/IMU_Evaluation.zip>` to download the latest version of the IMU Evaluation software.

Click :adi:`here <media/en/evaluation-boards-kits/evaluation-software/SDPDrivers.zip>` to download the latest drivers for the :adi:`EVAL-ADIS2`.

.. important::

   This application requires Microsoft .NET 3.5 to be installed and enabled on the host PCs running Windows 10. Additional information on enabling .NET 3.5 can be found `here <https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install-winpc/installingenabling-net-35-on-windows-10/fe7b4699-c096-4369-b06f-e1063da42e18>`_.


EVAL-ADIS2 IMU Evaluation Software Overview
-------------------------------------------

The IMU Evaluation Software is a Microsoft Windows (.NET) application that works in conjunction with the EVAL-ADIS2, in order to provide users with a PC-Based interface to most ADIS16xxx products. This platform enables observation of basic sensor functions, read/write access to all user-accessible registers, and full-rate data acquisition, which is synchronous with data production of each ADIS16xxx.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imues_mainwindow_04_Yaccel_pos_2_neg.png
   :width: 800px

.. important::

   This guide builds upon the :doc:`EVAL-ADIS2 Hardware User Guide </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis2-hardware-guide>` and assumes that you've installed the necessary drivers and software.


Using the EVAL-ADIS2 IMU Evaluation Software
--------------------------------------------

Main Window
~~~~~~~~~~~

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
~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~

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
-------------------------



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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



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



APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16265`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16265`, each command (16-bits) writes to one byte at a time.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16265`-specific content, but the :adi:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site <resources/eval/user-guides/inertial-mems/imu/adis16448?&#example_evaluation_exercises>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-pcbz-dimensions.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16220cccz-dimensions.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265mnt-on-eval-adis-j1conn.png
   :width: 420px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265eval-adis-data-ready.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265mnt-holes-on-eval-adis.png
   :width: 350px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/265-eval-adis-data-rdy.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-3.3v.png
   :width: 350px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/eval-adis-5v-setting.png
   :width: 500px
