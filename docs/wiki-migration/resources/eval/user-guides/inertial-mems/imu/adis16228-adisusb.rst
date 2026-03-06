ADIS16228 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16228` iSensor® is a complete vibration sensing system that combines triaxial acceleration sensing with advanced time domain and frequency domain signal processing. Time domain signal processing includes a programmable decimation filter and selectable windowing function. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-hookup.png
   :width: 400px

ADIS16228/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16228` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is the breakout board for the :adi:`ADIS16228` and may provide assistance in the process of hooking it up to an existing embedded processor system. For more information, click on the following link: :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`

For tips on interfacing to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` with a ribbon cable, check out the following Engineer Zone post:

:ez:`ADIS16228/PCBZ Breakout Board Cables (Engineer Zone FAQ) <docs/DOC-2523>`

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16228`, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` provides the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` on a small printed circuit board (PCB) that simplifies the connection to an existing processor system. This PCB includes a silkscreen, for proper placement, and four mounting holes that have threads for M2 × 0.4 mm machine screws. The second set of mounting holes on the interface boards are in the four corners of the PCB and provide clearance for 4-40 machine screws. The third set of mounting holes provides a pattern that matches the ADISUSBZ evaluation system, using M2 × 0.4mm × 4 mm machine screws. These boards are made of IS410 material and are 0.063 inches thick. J1 is a 16-pin connector, in a dual row, 2 mm geometry that enables simple connection to a 1 mm ribbon cable system. For example, use Molex P/N 87568-1663 for the mating connector and 3M P/N 3625/16 for the ribbon cable. For direct connection to the :adi:`ADISUSB` evaluation system, use these parts to make a 16-pin cable or remove pins 13, 14, 15 and 16. The LEDs (D1 and D2) are not populated, but the pads are available to install to provide a visual representation of the DIO1 and DIO2 signals. The pads accommodate Chicago Miniature Lighting Part No. CMD28-21VRC/TR8/T1, which works well when R1 and R2 are approximately 400 Ω (0603 pad sizes).The mating connector for the :adi:`ADIS16228 <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>`, J2, is AVX P/N 04-6288-015-000-846. The picture below provides a close-up view of this connector, which clamps down on the flex cable to press its metal pads onto the metal pads inside the mating connector. The schematic is for the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` board.

|image1| |image2| |image3| |image4|

NOTE: Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

Slide the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part into the mating J2 connector on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Press the J2 clamp down onto the flex connector to complete the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>` part connection to the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. Then secure the part using the M2 × 0.4mm × 4 mm machine screws provided with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The following pictures provide a visual reference for correct connection.

|image5| |image6| |image7|

WARNING: Make sure that the connector cable going from J1 on the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` is properly aligned to the J1 connector on the :adi:`ADISUSB`. The 12 pin cable is included with the :adi:`ADISUSB`. A 16 pin cable is also an option using the part numbers that are at the beginning of this section.

|image8| |image9| |image10|

Step #2
~~~~~~~

Mounting to the system frame is accomplished using 4 M2x.4x6mm machine screws included with the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 4 holes to secure the :adi:`ADIS16228/PCBZ <en/mems-sensors/mems-accelerometers/adis16228/products/EVAL-ADIS16228/eb.html>` to the :adi:`ADISUSB`.

|image11| |image12| |image13|

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`ADISUSB`) required for the :adi:`ADIS16228CMLZ <en/mems-sensors/mems-accelerometers/adis16228/products/product.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

NOTE: If JP1 is left on **+5v** the software will look like the following picture. Move JP1 to the\ **+3.3V** setting to correct the problem.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-wrong-voltage.png
   :width: 800px

ADIS16228_Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16228 Evaluation Software <static/imported-files/eval_boards/228ES1.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16228` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16228_EVAL_Rev_1.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-zip.png
   :width: 800px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the ADIS16228 software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-begininstall.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-prgm-group.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-done.png
   :width: 400px

USB Driver Installation
^^^^^^^^^^^^^^^^^^^^^^^

The ADIS16228_EVAL_Rev_1.cab file contains USB drivers that are compatible with 32-bit Windows systems. The software installation process unpacks these files and copies them into the appropriate directories, which enable a "guided driver installation process," after the :adi:`ADISUSB` board connects to the computer (using the included USB mini cable) for the first time. After connecting the :adi:`ADISUSB` to the computer, the **Hardware Wizard** will find and install the drivers by following the steps below.

|image14| |image15|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image16| |image17|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


ADIS16228 Evaluation SOFTWARE
-----------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the ADiS16228_Eval_Rev_1.exe file to launch the software application.

Main Window
^^^^^^^^^^^

Once the ADIS16228 Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image18| |image19|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Devices** option provides a list of products.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16228` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The **Start** option will start the selected mode capture process.

The yellow box identifies the waveform recorder window. The window contains the three accelerometer responses.

Register Access
^^^^^^^^^^^^^^^

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16228`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-adisusb-reg.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-adisusb-reg-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16228`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16228`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
^^^^^^^^^^^^^^^^^

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16228`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image20| |image21|

The Main screen upper right corner datalog option should be checked to enable the datalog function.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow box identifies a number of configuration options for the data acquisition process. The **Scaled Units** option causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **Use Scaled Data,** the accelerometer outputs will be in units of g's `g-force <https://en.wikipedia.org/wiki/G-force>`__.

EXAMPLE EXERCISES
^^^^^^^^^^^^^^^^^

Click on the following links to access example exercises for this evaluation tool and software package:

:ez:`A Simple Vibration Demonstration with the ADIS16228 and ADISUSB <docs/DOC-2420>`

:ez:`ADIS16228 Vibration Analysis Example, Compressor Case <docs/DOC-2526>`

:ez:`ADIS16228 Evaluation Tools, The Compressor Case, Revisited <docs/DOC-2543>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228pcbz-mnt.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-part-dimensions.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-mating-connector.png
   :width: 200px
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
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-main-screen.png
   :width: 800px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-228-main-screen-defined.png
   :width: 800px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-adisusb-datalog.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/228-adisusb-datalog-defined.png
   :width: 400px
