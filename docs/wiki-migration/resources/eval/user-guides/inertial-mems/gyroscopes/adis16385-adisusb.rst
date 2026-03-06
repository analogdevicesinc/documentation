ADIS16385 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16385` iSensor® is an autonomous system that requires no user initialization. When it has a valid power supply, it initializes itself and starts sampling, processing, and loading sensor data into the output registers at a sample rate of 1024 SPS. DIO1 pulses high after each sample cycle concludes. The SPI interface enables simple integration with many embedded processor platforms. The :adi:`ADIS16385` SPI interface supports full-duplex serial communication (simultaneous transmit and receive).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-spi-conn.png
   :width: 500px

ADIS16385/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16385` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>` is the breakout board for the :adi:`ADIS16385` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16385`, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>` includes one interface PCB, 4 M2x.4x18mm machine screws and one :adi:`ADIS16385BMLZ <ADIS16385>` unit. The :adi:`ADIS16385` is approximately 44 mm × 47 mm × 14 mm and provides a flexible connector interface that enables multiple mounting orientation options. Set the interface PCB aside, as it is not used for connecting the :adi:`ADIS16385BMLZ <ADIS16385>` to the :adi:`ADISUSB`.

**NOTE:** Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The :adi:`ADIS16385BMLZ <ADIS16385>` installs directly into the J4 connector of the :adi:`ADISUSB`. The following pictures provide a visual reference for correct connection. The :adi:`ADIS16385BMLZ <ADIS16385>` is secured using the M2x0.4x18mm machine screws included with the :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>`. The mounting location holes are shown in the picture below.

|image1| |image2| |image3| |image4|

**WARNING:** Make sure that the connector is in proper alignment before pressing it in. Misalignment can cause pin damage and exposure to harmful conditions.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-adisusb-j4-closeup.png
   :align: left
   :width: 300px

Step #2
~~~~~~~

The remote mounting option :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>` includes one :adi:`ADIS16385BMLZ <ADIS16385>`, one interface printed circuit board (PCB), and four M2 × 0.4 x 18mm machine screws. The interface PCB provides larger connectors than the :adi:`ADIS16385BMLZ <ADIS16385>` for simpler prototyping, four-tapped M2 holes for attachment of the :adi:`ADIS16385BMLZ <ADIS16385>`, and four holes (machine screw size M2.5 or #4) for mounting the :adi:`ADIS16385BMLZ <ADIS16385>` to a solid structure. J1 is a dual-row, 2 mm (pitch) connector that mates to a number of ribbon cable systems, including 3M Part Number 152212-0100-GB (ribbon crimp connector) and 3M Part Number 3625/12 (ribbon cable). Note that J1 has 16 pads; however, some legacy boards use only Pin 1 through Pin 12.

|image5| |image6|

Step #3
~~~~~~~

Secure the :adi:`ADIS16385BMLZ <ADIS16385>` body, to the :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>` using (4) M2x0.4x18mm machine screws (included with :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>`. The suggested torque setting for the attachment hardware is 40 inch-ounces, or 0.2825 N-m.

|image7| |image8|

Step #4
~~~~~~~

Connect J1 on the :adi:`ADISUSB` to J1 on the :adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>`. Note that J1 (:adi:`ADISUSB`) has 12 pins and J1 (:adi:`ADIS16385/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16385/products/EVAL-ADIS16385/eb.html>`) has 16 pins. The four DIO pins are left un-connected using the 12 pin connector which allows easy access and shown in the pictures below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-adisusb-to-pcbz3.png
   :width: 500px

Step #5
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). Change the JP1 jumper setting on the :adi:`ADISUSB` to the **+5V** position (shown on the right) required for the :adi:`ADIS16385BMLZ <ADIS16385>`.

|image9| |image10|

ADIS16385 Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16385 Evaluation Software <static/imported-files/eval_boards/ADIS16385_ES.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16385` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16385_Rev_2.cab), the setup file (setup.exe), and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-zip-download-file.png
   :width: 600px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the ADIS16375 Evaluation Software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image11| |image12|

USB Driver Installation
^^^^^^^^^^^^^^^^^^^^^^^

The ADIS16385_Rev_2.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image13| |image14|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image15| |image16|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


Main Window
^^^^^^^^^^^

Once the :adi:`ADIS16385` Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image17| |image18|

The orange box identifies the drop-down menus, which provide a number of useful features.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16385` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after pressing the **Read** button (see the red box for the location of the **Read** button).

The yellow box identifies the two waveform recorder windows. The top window contains the three gyroscope outputs. The bottom window contains the three accelerometer responses. Also, each waveform matches the color of its register (see register titles in the purple box).

Register Access
^^^^^^^^^^^^^^^

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16385`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-registers.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-registers-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16385`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16385`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
^^^^^^^^^^^^^^^^^

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16385`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image19| |image20|

The red box identifies all of the registers that are eligible for inclusion in the next acquisition process. Click on each box to include a register in the next data acquisition sequence. The box will have a check mark when it has been selected.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow boxes identify a number of configuration options for the data acquisition process. The **Samples per File** is a user input for the total number of samples in a data record. Note that all selected registers will have this number of samples in the data record file, after the acquisition process completes. After each update to the **Record Length** box, the software calculates and displays the total **Capture Time**. The **Numeric Data only..No File header** option allows the user to add or remove the header in the data storage file. The **No Scale LSB's Only** causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **No Scale LSB's Only,** the gyroscope outputs will be in units of degrees/second.

EXAMPLE EXERCISES
^^^^^^^^^^^^^^^^^

This section currently has no :adi:`ADIS16385`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-dimensions.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-topview-pinout.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-adisusb-mnt-location.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-mounted-on-adisusb.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/adis16385pcbz.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385pcbz.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-adisusb-to-pcbz.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-adisusb-to-pcbz2.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-prgrm-group.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-finish.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-main-screen.png
   :width: 800px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-main-screen-defined.png
   :width: 800px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-datalog.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/385-datalog-defined.png
   :width: 400px
