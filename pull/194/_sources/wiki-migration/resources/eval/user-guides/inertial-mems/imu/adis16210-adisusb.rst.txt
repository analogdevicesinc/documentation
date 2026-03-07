ADIS16210 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16210` iSensor® is a digital inclinometer system that provides precise measurements for both pitch and roll angles over a full orientation range of ±180°. It combines a MEMS tri-axial acceleration sensor with signal processing, addressable user registers for data collection/programming, and a SPI-compatible serial interface. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-elect-connection.png
   :width: 500px

ADIS16210/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16210` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` is the breakout board for the :adi:`ADIS16210` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB PC EVALUATION
---------------------

This Wiki Guide provides practical guidelines for PC-based evaluation of the :adi:`ADIS16210` on the :adi:`ADISUSB` system. Please note that the :adi:`EVAL-ADIS` evaluation system now provides this service and is the preferred system for new :adi:`ADIS16210` customers that want to start their evaluation on a PC system. The :adi:`EVAL-ADIS` provides a number of advantages that include support for 64-bit PCs, real-time data collection and software development options/examples.

:adi:`Click here to access the EVAL-ADIS home page. <EVAL-ADIS>`

:doc:`Click here to access the ADIS16210/EVAL-ADIS Wiki Guide. </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16210>`

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` provides the :adi:`ADIS16210 <en/mems-sensors/mems-accelerometers/adis16210/products/product.html>` on a small printed circuit board (PCB) that simplifies the connection to an existing processor system. This PCB includes a silkscreen, for proper placement, and four mounting holes that have threads for M2 × 0.4 mm machine screws. The second set of mounting holes on the interface boards are in the four corners of the PCB and provide clearance for 4-40 machine screws. The third set of mounting holes provides a pattern that matches the ADISUSBZ evaluation system, using M2 × 0.4mm × 4 mm machine screws. These boards are made of IS410 material and are 0.063 inches thick. J1 is a 16-pin connector, in a dual row, 2 mm geometry that enables simple connection to a 1 mm ribbon cable system. For example, use Molex P/N 87568-1663 for the mating connector and 3M P/N 3625/16 for the ribbon cable. For direct connection to the :adi:`ADISUSB` evaluation system, use these parts to make a 16-pin cable or remove pins 13, 14, 15 and 16. The LEDs (D1 and D2) are not populated, but the pads are available to install to provide a visual representation of the DIO1 and DIO2 signals. The pads accommodate Chicago Miniature Lighting Part No. CMD28-21VRC/TR8/T1, which works well when resistors R1 and R2 are approximately 400 Ω (0603 pad sizes).The mating connector for the :adi:`ADIS16210 <en/mems-sensors/mems-accelerometers/adis16210/products/product.html>`, J2, is AVX P/N 04-6288-015-000-846. The picture below provides a close-up view of this connector, which clamps down on the flex cable to press its metal pads onto the metal pads inside the mating connector. The schematic is for the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` board.

|image1| |image2| |image3| |image4|

NOTE: Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

Slide the :adi:`ADIS16210CMLZ <en/mems-sensors/mems-accelerometers/adis16210/products/product.html>` part into the mating J2 connector on the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>`. Press the J2 clamp down onto the flex connector to complete the :adi:`ADIS16210CMLZ <en/mems-sensors/mems-accelerometers/adis16210/products/product.html>` part connection to the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>`. Then secure the part using the M2 × 0.4mm × 4 mm machine screws provided with the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>`. The following pictures provide a visual reference for correct connection but are actually :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` parts that share the same mechanical body.

|image5| |image6| |image7|

WARNING: Make sure that the connector cable going from J1 on the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` is properly aligned to the J1 connector on the :adi:`ADISUSB`. The 12 pin cable is included with the :adi:`ADISUSB`. A 16 pin cable is also an option using the part numbers that are at the beginning of this section.

|image8| |image9| |image10|

Step #2
~~~~~~~

Mounting to the system frame is accomplished using 4 M2x.4x6mm machine screws included with the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 4 holes to secure the :adi:`ADIS16210/PCBZ <en/mems-sensors/mems-accelerometers/adis16210/products/EVAL-ADIS16210/eb.html>` to the :adi:`ADISUSB`.

|image11| |image12| |image13|

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`ADISUSB`) required for the :adi:`ADIS16210CMLZ <en/mems-sensors/mems-accelerometers/adis16210/products/product.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

NOTE: If JP1 is left on **+5v** the software will look like the following picture. Move JP1 to the\ **+3.3V** setting to correct the problem.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-main-screen-voltage-error.png
   :width: 800px

ADIS16210_Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16210 Evaluation Software <static/imported-files/eval_boards/ADIS16210_eval_Software.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16210` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16210_EVAL_Rev_2.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-zipfile.png
   :width: 800px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the :adi:`ADIS16210` software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image14| |image15|

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The ADIS16210_EVAL_Rev_2.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image16| |image17|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image18| |image19|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


ADIS16210 Evaluation SOFTWARE
-----------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the ADiS16210_Eval_Rev_2.exe file to launch the software application.

Main Window
~~~~~~~~~~~

Once the :adi:`ADIS16210` Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image20| |image21|

The orange box identifies the drop-down menus, which provide a number of useful features.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16210` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the two waveform recorder windows. The top window contains the three gyroscope outputs. The bottom window contains the three accelerometer responses. Also, each waveform matches the color of its register (see register titles in the purple box).

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16210`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-register.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-register-define.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16210`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16210`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16210`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image22| |image23|

The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow boxes identify a number of configuration options for the data acquisition process. The **Samples per File** is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the **Record Length** box, the software calculates the displays the total **Capture Time**. The **Numeric data only... No file header** option allows the user to add or remove the header in the data storage file. The **LSB Data only... No Scaling** causes the software to convert the decimal, twos complement number into its representative value. The default setting for **LSB Data only... No Scaling**, option the gyroscope outputs will be in units of degrees/second.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16210`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-mnt.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-part-dimensions.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-mating-connector.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-schematic.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-pcbz-parts.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-j2-insert1.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-pcbz-secure.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-j1-cable-option.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-j1-cable-option12pin.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-j1-cable-option16pin.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-adis16228pcbz-mount.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-mounted12pin-cable-zoom.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-secured-on-adisusb.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-prgm-group.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-finishedl.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-main-screen.png
   :width: 800px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-main-screen-defined.png
   :width: 800px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-datalog.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/210-adisusb-datalog-definition.png
   :width: 400px
