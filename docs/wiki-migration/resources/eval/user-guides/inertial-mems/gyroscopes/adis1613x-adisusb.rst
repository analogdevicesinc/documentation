ADIS16135 Evaluation Software
=============================

Click :adi:`here <static/imported-files/eval_boards/135ES4.zip>` to download the ADIS16133/5/6 Evaluation Software. The download file will contain three separate files: The CAB file (ADIS16135_Rev_4.cab), the setup file (setup.exe), and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-zipfile-download.png
   :width: 600px

Navigate to the folder where the files were saved and double click the setup.exe file. The **Welcome** screen will should appear. Click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-welcome.png
   :width: 500px

Choose a directory for the software application to extract the files or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-install.png
   :width: 500px

Choose a program group or use the default settings (recommended) and click **Continue**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-prgrm-group.png
   :width: 400px

USB Driver Installation
-----------------------

The ADIS16135_Rev_4.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware will be recognized and loaded. The Windows **Hardware Wizard** will find and install the drivers by following the steps below.

|image1| |image2|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image3| |image4|

.. important::

   For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the setup.exe file to launch the software application.

Main Window
-----------

Once the Analog Devices ADIS16135 Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image5| |image6|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Devices** option provides a list of products for :adi:`ADIS1613x <ADIS16136>` Evaluation, click on **Devices** and then select **ADIS16133/5/6**. The green box shows the current device selection, which in this case, identifies the :adi:`ADIS16133` as the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS1613x <ADIS16136>` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the waveform recorder window. The window contains the gyroscope output.

Register Access
---------------

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS1613x <ADIS16136>`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-registers.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-registers-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

.. tip::

   The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS1613x <ADIS16136>`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS1613x <ADIS16136>`, each command (16-bits) writes to one byte at a time.


Data Capture Menu
-----------------

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS1613x <ADIS16136>`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image7| |image8|

The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow box identifies a number of configuration options for the data acquisition process. The **Samples per File** is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the **Record Length** box, the software calculates then displays the total **Capture Time**. The **Numeric Data Only...No File Header** option allows the user to add or remove the header in the data storage file. The **No Scale LSB's Only** causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **No Scale LSB's Only,** the gyroscope outputs will be in units of degrees/second.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-main_screen.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-main_screen-defined.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-datalog.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-datalog-defined.png
   :width: 400px
