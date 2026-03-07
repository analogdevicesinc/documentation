ADIS16260/5 EVALUATION ON THE ADISUSB
=====================================

OVERVIEW
--------

The :adi:`ADIS16260` iSensor® is a product family of high performance, digital gyro-scope sensing systems that operate autonomously and requires no user configuration to produce accurate rate sensing data. It provides performance advantages with low noise density, wide bandwidth, and excellent in-run bias stability, which are enabling for applications such as platform control, navigation, robotics, and medical instrumentation. All :adi:`ADIS16260` product sensors use a serial peripheral interface for data communications. This interface enables direct connection with a large variety of embedded processor products. This electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-spi-connection.png
   :width: 400px

ADIS16260/5/6/PCB BREAKOUT BOARD
--------------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16260` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16260/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16260/products/EVAL-ADIS16260/eb.html>` is the breakout board for the :adi:`ADIS16260` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16260/5 <ADIS16260>` product family, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16260/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16260/products/EVAL-ADIS16260/eb.html>`

:adi:`ADIS16265/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16265/products/EVAL-ADIS16265/eb.html>`

:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16260/5/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16260/products/EVAL-ADIS16260/eb.html>` includes one interface PCB, and requires four M2 machine screws to secure the baseplate to the system printed circuit board. The :adi:`ADIS16260` product family is approximately 11.2 mm × 11.2 mm × 5.5 mm and is a drop in replacement for the :adi:`ADIS16250/5 <ADIS16250>` family.

|image1| |image2|

NOTE: Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The :adi:`ADIS16260` uses the 12 pin cable included with the :adi:`ADISUSB` connecting J1 on the :adi:`ADISUSB` to J1 on the :adi:`ADIS16260/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16260/products/EVAL-ADIS16260/eb.html>`. The following pictures provide a visual reference for correct connection. Mounting to the system frame is accomplished by using 4 M2 pre-drilled holes in the :adi:`ADISUSB`, marked in the picture below.]]

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-all-parts.png
   :width: 600px

WARNING: Make sure that the connector is in proper alignment before pressing it in. Misalignment can cause pin damage and exposure to harmful conditions.

Step #2
~~~~~~~

Secure the :adi:`ADIS16260/5 <ADIS16260>` using 4 M2x.4x4mm machine screws. J1 is a dual-row, 2 mm (pitch) connector that mates to a number of ribbon cable systems, including 3M Part Number 152212-0100-GB (ribbon crimp connector) and 3M Part Number 3625/12 (ribbon cable).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-pcbz.png
   :width: 600px

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). Change the JP1 jumper setting on the :adi:`ADISUSB` to the **+5V** position (shown on the right) required for the :adi:`ADIS16260/5 <ADIS16260>` product family.

|image3| |image4|

NOTE: If JP1 is left on **+3.3V**, the gyroscope outputs will not respond and will appear to be saturated in one direction or the other. See the following picture for an example of this behavior.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-main-screen-voltage-error.png
   :width: 800px

ADIS16260/5 Evaluation SOFTWARE
-------------------------------

:adi:`Click here to download the ADIS16260/5 Evaluation Software <static/imported-files/eval_boards/265ES(2).zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16260` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16265_Rev_2.cab), the setup file (setup.exe), and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-zipfile.png
   :width: 600px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the :adi:`ADIS16260` Evaluation Software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image5| |image6|

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The (ADIS16265_Rev_2.cab) file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image7| |image8|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image9| |image10|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


Analog Devices ADIS16260/5 Evaluation SOFTWARE
----------------------------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the setup.exe file to launch the software application.

Main Window
~~~~~~~~~~~

Once the Analog Devices :adi:`ADIS16265 <ADIS16260>` Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image11| |image12|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Devices** option provides a list of products for ADIS16260/5 Evaluation, click on **Devices** and then select **ADIS16260/5/6**. The green box shows the current device selection, which in this case, identifies the :adi:`ADIS16265 <ADIS16260>` as the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16265 <ADIS16260>` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the waveform recorder window. The window contains the gyroscope output.

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16265 <ADIS16260>`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-registers.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-registers-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16265 <ADIS16260>`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16265 <ADIS16260>`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16265 <ADIS16260>`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image13| |image14|

The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow boxes identify a number of configuration options for the data acquisition process. The Samples per File is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the Record Length box, the software calculates then displays the total Capture Time. The Numeric Data Only…No File Header option allows the user to add or remove the header in the data storage file. The Record as LSB's...No Scaling causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling No Scale LSB's Only, the gyroscope output will be in units of degrees/second.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16260/5 <ADIS16260>`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-pinout.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-pcbz-dimensions.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-prgrm-group.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-finished.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-main-screen.png
   :width: 800px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-main-screen-defined.png
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-data-capture.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/26x-adisusb-data-capture-defined.png
   :width: 400px
