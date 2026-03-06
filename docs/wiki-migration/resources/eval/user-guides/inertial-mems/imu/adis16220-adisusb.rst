ADIS16220 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16220` iSensor® is a complete vibration sensing system that combines triaxial acceleration sensing with advanced time domain and frequency domain signal processing. Time domain signal processing includes a programmable decimation filter and selectable windowing function. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-spi-conn.png
   :width: 400px

ADIS16220/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16220` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` is the breakout board for the :adi:`ADIS16220` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16220`, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16228/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

**NOTE:** All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` provides the :adi:`ADIS16220 <en/mems-sensors/mems-accelerometers/adis16220/products/product.html>` function on a 1.2 inch × 1.3 inch printed circuit board (PCB), which simplifies the connection to an existing processor system. The four mounting holes accommodate either M2 (2mm) or Type 2-56 machine screws. These boards are made of IS410 material and are 0.063 inches thick. The second level assembly uses a SAC305-compatible solder composition (Pb-free), which has a pre-solder reflow thickness of approximately 0.005 inches. The pad pattern on the :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` matches that shown in below. J1 and J2 are dual-row, 2 mm (pitch) connectors that work with a number of ribbon cable systems, including 3M Part Number 152212-0100-GB (ribbon-crimp connector) and 3M Part Number 3625/12 (ribbon cable).

|image1| |image2| |image3|

**NOTE:** Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The connection to the :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` is simple using J1 and a 12 pin cable included with the :adi:`ADISUSB`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-pcbz-brd.png
   :width: 400px

**WARNING:** Make sure that the connector cable going from J1 on the :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` is properly aligned to the J1 connector on the :adi:`ADISUSB`. The 12 pin cable is included with the :adi:`ADISUSB`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb.png
   :width: 400px

Step #2
~~~~~~~

Mounting to the system frame is accomplished using 4 M2x.4x4mm machine screws included with the :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 4 holes to secure the :adi:`ADIS16220/PCBZ <en/mems-sensors/mems-accelerometers/adis16220/products/EVAL-ADIS16220/eb.html>` to the :adi:`ADISUSB`.

|image4| |image5|

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`ADISUSB`) required for the :adi:`ADIS16220CMLZ <en/mems-sensors/mems-accelerometers/adis16220/products/product.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

**NOTE:** If JP1 is left on **+5v** the software will look like the following picture. Move JP1 to the\ **+3.3V** setting to correct the problem.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-main-screen-voltage-error.png
   :width: 800px

ADIS16220_Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16220 Evaluation Software <static/imported-files/eval_boards/ADIS1622x_eval_software.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16223` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16220_EVAL_Rev_5.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-download.png
   :width: 800px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the ADIS16223 software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image6| |image7|

USB Driver Installation
^^^^^^^^^^^^^^^^^^^^^^^

The ADIS16220_EVAL_Rev_5.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image8| |image9|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image10| |image11|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


ADIS16220 Evaluation SOFTWARE
-----------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the ADiS16220_Eval_Rev_5.exe file to launch the software application.

Main Window
^^^^^^^^^^^

Once the ADIS16220 Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image12| |image13|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Product** option provides a list of products for :adi:`ADIS16220` Evaluation, click on **Product** and then select :adi:`ADIS16220`. The green box shows the current device selection, which in this case, identifies the :adi:`ADIS16220` as the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16220` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, after pressing the **Read** button.

The red box identifies the Trigger button for different capture modes.

The yellow box identifies the waveform recorder window. The window contains the three accelerometer responses. Also, each waveform matches the color of its register.

Register Access
^^^^^^^^^^^^^^^

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16220`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-registers.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-registers-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16220`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16220`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
^^^^^^^^^^^^^^^^^

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16220`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image14| |image15|

**Note:** The Main screen datalog option should be checked to enable the datalog function.

The green box identifies the configuration box for the name and location of the data storage file.

The yellow box identifies a number of configuration options for the data acquisition process. The **Scaled Units** option causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **Use Scaled Data,** the accelerometer outputs will be in units of g's `g-force <https://en.wikipedia.org/wiki/G-force>`__.

EXAMPLE EXERCISES
^^^^^^^^^^^^^^^^^

This section currently has no :adi:`ADIS16220`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-pcbz-dimensions.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-pcbz-schematic.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16220cccz-dimensions.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-all-parts.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-mnt-adisusb.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-prgm-group.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-finished.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-main-screen.png
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/220-main-screen-defined.png
   :width: 800px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-datalog.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-datalog-defined.png
   :width: 400px
