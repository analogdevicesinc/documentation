ADIS16334 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16334` is a low-profile, high-performance IMU that uses a serial peripheral interface for data communications. This interface enables direct connection with a large variety of embedded processor products. This electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16334-uc-hook-up.png
   :width: 400px

ADIS16334/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16334` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16334/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16334/products/EVAL-ADIS16334/eb.html>` is the breakout board for the :adi:`ADIS16334` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16334`, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16334/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16334/products/EVAL-ADIS16334/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16334/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16334/products/EVAL-ADIS16334/eb.html>` includes one interface PCB, one flexible cable/connector and one :adi:`ADIS16334AMLZ <ADIS16334>` unit. Use the flexible cable/connector to install the :adi:`ADIS16334` onto the :adi:`ADISUSB`, using the following five steps. Set interface PCB aside, as it is not used for connecting the :adi:`ADIS16334AMLZ <ADIS16334>` to the :adi:`ADISUSB`.

**NOTE:** Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

**NOTE:** Some of the pictures in this section represent the :adi:`ADIS16448`, not the :adi:`ADIS16334`. The packages associated with these two products are close enough to illustrate the key points associated with installing the :adi:`ADIS16334`.

Step #1
~~~~~~~

Install the flexible cable onto the :adi:`ADIS16334AMLZ <ADIS16334>`. The following pictures provide a visual reference for correct connection.

|image1| |image2| |image3|

**WARNING:** Make sure that the connector is in proper alignment before pressing it in. Misalignment can cause pin damage and exposure to harmful conditions. The following pictures provide visual examples of INCORRECT PIN ALIGNMENT. The most common alignment issues will cause the top view to look different than the third picture, shown directly above this paragraph.

|image4| |image5|

Step #2
~~~~~~~

Mounting to the system frame is accomplished by Drilling and tapping for M2 (drill size #52 1.6mm) or 2-56 (drill size #50 .070) holes in the :adi:`ADISUSB`, according to the locations in the physical mounting diagram. The tap is the best way but an M2x0.4x10mm machine screw can be used for tapping the PCB material. The distance between these components is flexible but make sure that the hole-to-hole distance is within the 15 mm to 45 mm range shown in the diagram. The mounting location holes are marked as an example in the picture below (right). These locate holes position the :adi:`ADIS16334AMLZ <ADIS16334>` at the edge of the :adi:`ADISUSB` giving the interface flex more room.

|image6| |image7| |image8|

Step #3
~~~~~~~

The :adi:`ADIS16334AMLZ <ADIS16334>` and interface flex can now be connected to the :adi:`ADISUSB`. Make sure that Pin 1 on J2 (interface-flex) connects to Pin 20 on the :adi:`ADISUSB` J4 connector which, has 24 pins (leaving 4 empty holes at the top of the J4 connector opposite the J4 pin1 ★ designator). J4 has a Pin 1 indicator to help guide this connection. Making the J4 connection first then sliding the :adi:`ADIS16334AMLZ <ADIS16334>` body forward allowing the flex ribbon to fold under until the mounting holes line up.

|image9| |image10| |image11|

Step #4
~~~~~~~

Secure the :adi:`ADIS16334AMLZ <ADIS16334>` body, to a system frame using (4) M2x0.4x10mm machine screws (included with :adi:`ADISUSB`). Use a mounting torque of 25 inch-ounces for the M2 machine screws.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-secured.png
   :align: left
   :width: 400px

Step #5
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). Change the JP1 jumper setting on the :adi:`ADISUSB`) to the **+5V** position (shown on the right) required for the :adi:`ADIS16334AMLZ <ADIS16334>`.

|image12| |image13|

**NOTE:** If JP1 is left on **+3.3V**, the gyroscope outputs will not respond and will appear to be saturated in one direction or the other. See the following picture for an example of this behavior.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-error.png
   :width: 800px

IMU_6DOF Six Degrees of Freedom Demonstration SOFTWARE
------------------------------------------------------

:adi:`Click here to download the IMU-6DOF Six Degrees of Freedom Software <static/imported-files/eval_boards/IMU_6DOF_2.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16334` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (IMU_6DOF.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-software-zip.png
   :width: 800px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the IMU_6DOF software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image14| |image15|

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The IMU_6DOF.cab file contains USB drivers that are compatible with both only 32-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image16| |image17|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image18| |image19|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


IMU_6DOF Six Degree of Freedom Demonstration SOFTWARE
-----------------------------------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the IMU_6DOF.exe file to launch the software application.

Main Window
~~~~~~~~~~~

Once the IMU_6DOF Six Degrees of Freedom Demonstration Software starts-up, the Main Window will appear and look like the following picture (which has highlights to support additional descriptions, see below the graphic).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-main-defined.png
   :width: 800px

The orange box identifies the drop-down menus, which provide a number of useful features. The **Devices** option provides a list of products for :adi:`ADIS16334` Evaluation, click on **Devices** and then select :adi:`ADIS16334`. The green box shows the current device selection, which in this case, identifies the :adi:`ADIS16334` as the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16334` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the two waveform recorder windows. The top window contains the three gyroscope outputs. The bottom window contains the three accelerometer responses. Also, each waveform matches the color of its register (see register titles in the purple box).

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16334`. The following picture shows the appearance of this window.

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

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16334`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16334`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

``The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the ADIS16334. The following picture represents the Data Capture window, right after opening it from the Main Window and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.``

|image20| |image21|

''The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected. ''

``The green box identifies the configuration box for the name and location of the data storage file.``

``The yellow boxes identify a number of configuration options for the data acquisition process. The Samples per File is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the Record Length box, the software calculates then displays the total Capture Time. The Numeric Data Only..No File Header option allows the user to add or remove the header in the data storage file. The No Scale LSB's Only causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling No Scale LSB's Only, the gyroscope outputs will be in units of degrees/second.``

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

``This section currently has no ADIS16334-specific content, but the ADIS16448 Evaluation on the EVAL-ADIS Wiki Site has some good examples to start with.``

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step1-01.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step1-03.jpg
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step1-02.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step1-04.jpg
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step1-05.jpg
   :width: 200px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-parts.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334_mnt-holes.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-physicalmnt.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-j4-connection.png
   :width: 300px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-flex-screws.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-334-sliding-to-locateholes.png
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2programgroup.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-v2completed-install.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-datalog.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-datalog-defined.png
   :width: 400px
