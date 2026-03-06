EVAL-ADIS-FX3 Setup and Troubleshooting Guide
=============================================

Breakout Board Selection Table
------------------------------

Expand the table below to find the breakout board for your specific IMU.



.. raw:: html

   <details><summary>Click to expand</summary>

+--------------------------------------------------------------+--------------------------------------------------------------+
| MODEL NUMBER                                                 | BREAKOUT BOARD                                               |
+==============================================================+==============================================================+
| :adi:`ADIS16201CCCZ`                                         | :adi:`ADIS16201/PCBZ <EVAL-ADIS16201>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16203CCCZ`                                         | :adi:`ADIS16203/PCBZ <EVAL-ADIS16203>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16209CCCZ`                                         | :adi:`ADIS16209/PCBZ <EVAL-ADIS16209>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16210BMLZ <ADIS16210>`                             | :adi:`ADIS16210/PCBZ <EVAL-ADIS16210>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16223CMLZ`                                         | :adi:`ADIS16ACL2/PCBZ <EVAL-ADIS16ACL2>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16227CMLZ`                                         | :adi:`ADIS16ACL2/PCBZ <EVAL-ADIS16ACL2>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16228BMLZ <ADIS16228>`                             | :adi:`ADIS16ACL1/PCBZ <EVAL-ADIS16ACL1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16375BMLZ <ADIS16375>`                             | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16445BMLZ <ADIS16445>`                             | :adi:`ADIS16IMU2/PCBZ <EVAL-ADIS16IMU2>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16446BMLZ <ADIS16446>`                             | :adi:`ADIS16IMU2/PCBZ <EVAL-ADIS16IMU2>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16448BMLZ <ADIS16448>`                             | :adi:`ADIS16IMU2/PCBZ <EVAL-ADIS16IMU2>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16460AMLZ`                                         | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16465-1BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16465-2BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16465-3BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16467-1BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16467-2BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16467-3BMLZ`                                       | :adi:`ADIS16IMU4/PCBZ <EVAL-ADIS16IMU4>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16470AMLZ`                                         | :adi:`ADIS16470/PCBZ <EVAL-ADIS16470>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16475-1BMLZ`                                       | :adi:`ADIS16475-x/PCBZ <EVAL-ADIS16475>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16475-2BMLZ`                                       | :adi:`ADIS16475-x/PCBZ <EVAL-ADIS16475>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16475-3BMLZ`                                       | :adi:`ADIS16475-x/PCBZ <EVAL-ADIS16475>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16477-1BMLZ`                                       | :adi:`ADIS16477-x/PCBZ <EVAL-ADIS16477>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16477-2BMLZ`                                       | :adi:`ADIS16477-x/PCBZ <EVAL-ADIS16477>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16477-3BMLZ`                                       | :adi:`ADIS16477-x/PCBZ <EVAL-ADIS16477>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16480BMLZ`                                         | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16485BMLZ`                                         | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16488BMLZ`                                         | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16488CMLZ`                                         | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16490BMLZ`                                         | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16495-1BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16495-2BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16495-3BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16497-1BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16497-2BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16497-3BMLZ`                                       | :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16500AMLZ <ADIS16500>`                             | :adi:`ADIS16500/PCBZ <EVAL-ADIS16500>`                       |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16505-1AMLZ <ADIS16505>`                           | :adi:`ADIS16505-x/PCBZ <EVAL-ADIS16505>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16505-2AMLZ <ADIS16505>`                           | :adi:`ADIS16505-x/PCBZ <EVAL-ADIS16505>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16505-3AMLZ <ADIS16505>`                           | :adi:`ADIS16505-x/PCBZ <EVAL-ADIS16505>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16507-1AMLZ <ADIS16507>`                           | :adi:`ADIS16507-x/PCBZ <EVAL-ADIS16507>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16507-2AMLZ <ADIS16507>`                           | :adi:`ADIS16507-x/PCBZ <EVAL-ADIS16507>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+
| :adi:`ADIS16507-3AMLZ <ADIS16507>`                           | :adi:`ADIS16507-x/PCBZ <EVAL-ADIS16507>`                     |
+--------------------------------------------------------------+--------------------------------------------------------------+

.. raw:: html

   </details>


Downloading and Installing the FX3 Drivers and Software
-------------------------------------------------------

The :adi:`EVAL-ADIS-FX3` includes a laundry list of hardware and software features designed to enable in-depth test and characterization of iSensor IMUs. To get started, we suggest you first download the :git-iSensor-FX3-Eval:`latest Evaluation GUI <releases>` and FX3 :git-iSensor-FX3-Eval:`device drivers <drivers>` from our GitHub page.

Once downloaded, double click on ``FX3DriverSetup.exe`` and follow the install prompts. Once complete, the signed Analog Devices driver should be installed on your PC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/driver1.png
   :width: 420px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/driver2.png
   :width: 420px

.. important::

   The root cause of most FX3 driver issues is user permissions. The driver installer **must** be executed using native Windows administrator privileges. Running the installer using privilege elevation tools such as BeyondTrust (`link <https://beyondtrust.com>`__) will likely cause issues once the Windows Kernel attempts to load the driver.


   |image1|

Every FX3 Evaluation GUI release is packaged inside of a .zip archive. We recommend extracting the archive somewhere convenient on your PC (like your desktop), where it can easily be accessed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/files.png
   :width: 180px

Connecting to the FX3 Board
---------------------------

Once extracted, double click on ``iSensorFX3Eval.exe`` to launch the GUI. Before the main GUI launches, the software will ask you to select a device configuration to load.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/select_dut.png
   :width: 250px

Select the product ID/model number of the sensor you're connecting to and click on "Apply Device Settings."

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/select_dut_dropdown.png
   :width: 250px

.. important::

   If you have several FX3 boards connected to the same PC, another dialog box asking you to select a target FX3 board should pop up after clicking "Apply Device Settings." The drop-down menu will list the unique serial number of each :adi:`EVAL-ADIS-FX3`. The "activity" LED corresponding to the selected serial number will blink, indicating the target board. Once you've made a selection, click "OK."

   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/select_fx3.png
      :align: center
   


Once you've selected the correct FX3 board, the main screen should like the image below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/main_screen_disconnected.jpg
   :alt: main_screen_disconnected.jpg

.. warning::

   The :adi:`EVAL-ADIS-FX3` supplies a 3.3V supply by default when connecting to an IMU but can also be configured to supply 5V by selecting a device profile for a sensor that requires it. You can always find the onboard sensor supply voltage and status on the main window shown here:

   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/supply_status.png
      :width: 500px
   


Once at the main window, click on “Connect to FX3” to enable all GUI features. If the connection to the :adi:`EVAL-ADIS-FX3` was successful, all of the Evaluation GUI utilities would activate. The iSensor FX3 Eval software assesses IMU Status by writing a randomly-generated number to the sensor module and reading it back.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/main_screen_connected.jpg
   :alt: main_screen_connected.jpg

Finished!
---------

Congratulations! If the Eval GUI looks similar to the image shown above, then you're ready to interact with the IMU and stream sensor data. Click :doc:`HERE </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3-eval-user-guide>` to go to the Eval GUI user guide!

If the Eval GUI shows a connection error, the section below should help debug many common connection issues.

Troubleshooting Connection Errors
---------------------------------

The FX3 Evaluation GUI attempts to read and write a random number to a scratch register upon startup or when the user clicks on "Check DUT Connection." This read and write operation does **not** commit any changes to the sensor's onboard flash memory and will not overwrite the register's contents. The FX3 Evaluation software will display an error if the verification operation fails. We've listed many common debugging steps to try if you encounter any errors while using our software or hardware.

"ERROR: FX3 Connection Lost" or "ERROR: No FX3 Board Connected"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These errors occur when the FX3 Evaluation GUI cannot detect or somehow loses connection with an active :adi:`EVAL-ADIS-FX3` board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/connection_lost.png
   :alt: connection_lost.png

Is the USB cable plugged in?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADIS-FX3` must be plugged into a USB Type-A port capable of at least USB 2.0 speeds. USB hubs should be avoided since the USB protocol imposes artificial power limits when connecting through one.

Is the USB cable capable of transmitting data?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many USB cables that ship with mobile phones are **not** capable of transferring USB data and are designed for high-speed charging. We suggest using a high-quality USB C cable (like the one included with the :adi:`EVAL-ADIS-FX3`) to ensure reliable, robust communication.

Does Windows detect the EVAL-ADIS-FX3?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Analog Devices FX3 bootloader is flashed to the onboard EEPROM as part of the :adi:`EVAL-ADIS-FX3` manufacturing process. It can be verified by looking for a USB device named “Analog Devices FX3 Bootloader” in the Windows Device Manager.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/device_manager.jpg
   :alt: device_manager.jpg

If you’re unable to find the device, try resetting the FX3 by either unplugging the USB cable or pressing the reset button on the :adi:`EVAL-ADIS-FX3`. If this still doesn’t solve the issue, try pressing and holding the “RECOVERY” button while plugging the board into your PC. This will force the board to connect in recovery mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/reset_bootloader.jpg
   :alt: reset_bootloader.jpg

Is the ribbon cable orientation correct? Are the ribbon cable or sensor connections shifted or offset?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADIS-FX3` includes short-circuit protection on the sensor supply pins when using the onboard (USB) supply. Even so, it is still possible to exceed the USB current limits and force the :adi:`EVAL-ADIS-FX3` to brownout. A connection issue like this can be harmful to both the :adi:`EVAL-ADIS-FX3` and the host PC and may permanently damage either if not corrected immediately.

Was the EVAL-ADIS-FX3 exposed to extreme environments?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADIS-FX3` was designed for bench evaluation, data capture, and characterization. Even though most iSensor portfolio devices are designed and validated to operate in extreme environments, the :adi:`EVAL-ADIS-FX3` was not. Exposing the :adi:`EVAL-ADIS-FX3` to environments outside of typical lab use may cause it to behave unreliably.

Did you try to send the FX3 several commands during a long execution process?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Certain FX3 API functions can take a very long time to execute and may look like the FX3 has "locked up." The Eval GUI has timeouts implemented during many of these function calls to prevent this behavior, but developers may occasionally run into these issues when writing their own applications.

If the board becomes unresponsive, pressing the reset button on the FX3 or unplugging/plugging the USB cable should return the FX3 to its default bootloader state.

"ERROR: DUT Read/Write Failed"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error occurs when the register read-back operation fails to return the number that should've been written to the first scratch register listed in the selected register map.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/read-write_failed.png
   :alt: read-write_failed.png

Is the power selection jumper correctly set?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADIS-FX3` can either supply power to the sensor using an onboard linear regulator or bypass the onboard regulator and use an external power source. The jumper must be set to "USB" when using the onboard regulator, as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/image_from_ios_11_.jpg
   :align: center
   :width: 450px

Is the ribbon cable orientation correct?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's common to invert (flip) the ribbon cable orientation when connecting the :adi:`EVAL-ADIS-FX3` to a sensor coupon or breakout board. The correct cable orientation is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/image_from_ios_9_.jpg
   :align: center
   :width: 450px

Is the sensor or ribbon cable connection shifted or offset?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's possible to shift the sensor or ribbon cable connection by one position or row. An example of a shifted connection is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/image_from_ios_10_.jpg
   :align: center
   :width: 450px

Was the correct profile for the sensor connected to the EVAL-ADIS-FX3 loaded? Was the correct register map loaded?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The name of the active profile and register map can always be found on the main form, as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/profile_regmap.png
   :alt: profile_regmap.png

If the incorrect profile was accidentally loaded, a new one could be selected by connecting to the FX3 and clicking on the "Select DUT Type" button on the main window.

Is the active SPI configuration valid for the sensor connected to the EVAL-ADIS-FX3?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It's possible to change the :adi:`EVAL-ADIS-FX3` configuration such that it exceeds the SPI specifications listed on the sensor's datasheet. Reloading the device configuration by clicking "Select DUT Type" in the main window will always restore the SPI settings to a known-good configuration.

Are the SPI pins on the EVAL-ADIS-FX3 forced high/low?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some logic analyzers and in-circuit debuggers will hold GPIO lines at specific states such that either the :adi:`EVAL-ADIS-FX3` or the sensor cannot source/sink enough current to force a transition.

Is the ribbon cable connected to the FX3 too long?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADIS-FX3` was not designed to drive long cable lengths without adding additional driver circuitry. As cable length increases, the SPI signal integrity will quickly deteriorate. Variables such as SPI SCLK rate and stall time will also influence the overall cable length. A long cable will usually result in zeros intermittently inserted in random registers and incomplete register writes.

Reporting Errors and Generating Crash Reports
---------------------------------------------

Generating a firmware error log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-ADIS-FX3` firmware includes an error logging feature that stores any exceptions generated during operation into the onboard EEPROM. When reporting an issue, it’s helpful to provide this file since it will help us recreate and diagnose the issue's root cause. The firmware log is unique to each :adi:`EVAL-ADIS-FX3` and is only transmitted to the PC when requested by the user.

To extract the firmware log, connector to the :adi:`EVAL-ADIS-FX3` in question, navigate to the "Advanced" tab and click on the "Check FX3 Error Log" button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/firmware_error_log.gif

This window will list the number of errors logged in the :adi:`EVAL-ADIS-FX3` EEPROM and allow you to extract a log file. This file contains firmware metadata and the exact line in the FX3 firmware where the error was generated. Providing this information greatly speeds up the debug process and plays a crucial role in determining the error's root cause.

Locating the Eval GUI error log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the Eval GUI ever encounters an exception, an error log will be generated and stored in: ``C:\ProgramData\Analog Devices\FX3ExampleGUI\ERROR_LOG.csv`` When reporting an issue on GitHub, please be sure to attach this error log to help us further understand the root cause of the exception.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/unhandled_exception_fx3.jpg
   :width: 600px

Click :doc:`HERE </wiki-migration/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3>` to go back to the :adi:`EVAL-ADIS-FX3` landing page.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/runasadmin.jpg
