ADIS1636x EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16364` is a high-performance IMU that uses a serial peripheral interface for data communications. This interface enables direct connection with a large variety of embedded processor products. This electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-spi-conn.png
   :width: 400px

This Wiki will cover all members of the ADIS1636x family: :adi:`ADIS16360` :adi:`ADIS16362`, :adi:`ADIS16364`, :adi:`ADIS16365`, :adi:`ADIS16367`, :adi:`ADIS16400` :adi:`ADIS16405`,

ADIS16364/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16362` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16364/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16364/products/EVAL-ADIS16364/eb.html>` is the breakout board for the :adi:`ADIS16364` and may provide assistance in the process of hooking it up to an existing embedded processor system. Also see the following breakout board pages:

:adi:`ADIS16360/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16360/products/EVAL-ADIS16360/eb.html>`

:adi:`ADIS16362/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16362/products/EVAL-ADIS16362/eb.html>`

:adi:`ADIS16364/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16364/products/EVAL-ADIS16364/eb.html>`

:adi:`ADIS16365/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16365/products/EVAL-ADIS16365/eb.html>`

:adi:`ADIS16367/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16367/products/EVAL-ADIS16367/eb.html>`

:adi:`ADIS16400/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16400/products/EVAL-ADIS16400/eb.html>`

:adi:`ADIS16405/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16405/products/EVAL-ADIS16405/eb.html>`

:adi:`ADIS16407/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16407/products/EVAL-ADIS16407/eb.html>`

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16364` product family, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16364`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16364/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16364/products/EVAL-ADIS16364/eb.html>` includes one interface PCB, which requires two M2 or 2-56 machine screws to secure the baseplate to the system printed circuit board. The :adi:`ADIS16364` product family is approximately 22 mm × 32 mm × 24 mm and provides a flexible connector interface that enables multiple mounting orientation options. Set the interface PCB aside, as it is not used for connecting the :adi:`ADIS16364` to the :adi:`ADISUSB`.

|image1| |image2|

NOTE: Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The :adi:`ADIS16364` installs directly into the J4 connector of the :adi:`ADISUSB`. The following pictures provide a visual reference for correct connection. Mounting to the system frame is accomplished by using 2 M2 pre-drilled holes in the :adi:`ADISUSB`, marked in the picture below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-mnt-locations.png
   :width: 600px

WARNING: Make sure that the connector is in proper alignment before pressing it in. Misalignment can cause pin damage and exposure to harmful conditions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-36x-mounted-parts.png
   :align: left
   :width: 400px

Step #2
~~~~~~~

The :adi:`ADIS16364` installation, is a simple two-step process:

1. Secure the baseplate using 2 M2 x 0.4mm x 6mm machine screws using the pre-drilled holes on the :adi:`ADISUSB`.

2. Press the connector into its mate.

For removal, 1. Gently pry the connector from its mate using a small slotted

screwdriver. 2. Remove the screws and lift the part up.

**Never** attempt to unplug the connector by pulling on the plastic case or baseplate. Although the flexible connector is very reliable in normal operation, it can break when subjected to unreasonable handling. When broken, the flexible connector cannot be repaired.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-mounted.png
   :width: 600px

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). Change the JP1 jumper setting on the :adi:`ADISUSB` to the **+5V** position (shown on the right) required for the :adi:`ADIS16364`.

|image3| |image4|

NOTE: If JP1 is left on **+3.3V**, the gyroscope outputs will not respond and will appear to be saturated in one direction or the other. See the following picture for an example of this behavior.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-main-screen-voltage-error.png
   :width: 800px

IMU_6DOF Six Degrees of Freedom Demonstration SOFTWARE
------------------------------------------------------

:adi:`Click here to download the IMU-6DOF Six Degrees of Freedom Software <static/imported-files/eval_boards/IMU_6DOF_2.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16364` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (IMU_6DOF.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-software-zip.png
   :width: 800px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the IMU_6DOF software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image5| |image6|

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The IMU_6DOF.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image7| |image8|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image9| |image10|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


IMU_6DOF Six Degree of Freedom Demonstration SOFTWARE
-----------------------------------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the IMU_6DOF.exe file to launch the software application.

Main Window
~~~~~~~~~~~

Once the IMU_6DOF Six Degrees of Freedom Demonstration Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image11| |image12|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Devices** option provides a list of products for Evaluation, click on **Devices** and then select the specific sensor device **ADIS16364**. The green box shows the current device selection, which depends on the ADIS1636x product family in this case, the :adi:`ADIS16364` is the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16364` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the two waveform recorder windows. The top window contains the three gyroscope outputs. The bottom window contains the three accelerometer responses. Also, each waveform matches the color of its register (see register titles in the purple box).

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16364`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-reg.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-reg-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16364`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16364`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16364`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image13| |image14|

The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow boxes identify a number of configuration options for the data acquisition process. The **Samples per File** is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the **Record Length** box, the software calculates then displays the total **Capture Time**. The **Numeric Data Only..No File Header** option allows the user to add or remove the header in the data storage file. The **No Scale LSB's Only** causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **No Scale LSB's Only,** the gyroscope outputs will be in units of degrees/second.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16364`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-part-dimensions.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16364bmlz.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2programgroup.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2completed-install.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-main-screen.png
   :width: 800px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-main-screen-defined.png
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-datalog.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-datalog-defined.png
   :width: 400px
