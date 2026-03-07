ADIS16227 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16227` iSensor® is a triaxial, wide bandwidth, vibration-sensing system. It combines a triaxial MEMS accelerometer with a sampling and advanced signal processing system. The SPI-compatible port and user register structure provide convenient access to frequency domain vibration data and many user controls. The electrical connection typically only requires 5 I/O lines for synchronous data collection, as shown in the following figure:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-spi-elect-conn.png
   :width: 400px

ADIS16227/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16227` to an embedded controller will provide the most flexibility in developing application firmware and will more closely reflect the final system design. The :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` is the breakout board for the :adi:`ADIS16227` and may provide assistance in the process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the :adi:`ADIS16227`, before developing their own embedded system, the :adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during software package install.

PHYSICAL SETUP
--------------

The :adi:`ADIS16227 <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` is available in a 15 mm × 15 mm × 15 mm module with a threaded hole for stud mounting with a 10-32 UNF screw. The dual-row, 1 mm, 14-pin, flexible connector enables simple user interface and installation. The :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` provides the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` on a small printed circuit board (PCB) that simplifies the connection to an existing processor system. A single 10-32 machine screw secures the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` to the interface board. The first set of mounting holes on the interface boards are in the four corners of the PCB and provide clearance for 4-40 machine screws. The second set of mounting holes provides a pattern that matches the :adi:`ADISUSB` evaluation system, using M2 × 0.4 mm machine screws. These boards are made of IS410 material and are 0.063 inches thick. The J1 connector uses Pin 1 through Pin 12 in this pattern. Pin 13 and Pin 14 are for future expansion, but they also provide convenient probe points for the DIO1 and DIO2 signals. The connector is a dual row, 2 mm (pitch) connector that work with a number of ribbon cable systems, including 3M Part Number 152212-0100-GB (ribbon-crimp connector) and 3M Part Number 3625/12 (ribbon cable). The LEDs (D1 and D2) provide visual indication on the DIO1 and DIO2 signals. The pads accommodate Chicago Miniature Lighting Part No. CMD28-21VRC/TR8/T1, which works well when resistors R1 and R2 are approximately 400 Ω (0603 pad sizes). The schematic is for the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` board.

|image1| |image2| |image3|

**NOTE:** Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The single 10-32 machine screw from the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` kit will secure the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` part on the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`. Once the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` part is secured plug the flexible connector into the U1 connector on the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`. The following pictures provide a visual reference for correct connection but, are pictures of the :adi:`ADIS16223CMLZ <en/mems-sensors/mems-accelerometers/adis16223/products/product.html>` that has the same physical dimensions.

|image4| |image5|

**WARNING:** Make sure that the connector cable going from J1 on the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>` is properly aligned to the J1 connector on the :adi:`ADISUSB`. The 12 pin cable is included with the :adi:`ADISUSB`.

Step #2
~~~~~~~

Mounting to the system frame is accomplished using 6 M2x.4x6mm machine screws included with the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>`. The mounting location holes are marked as an example in the picture below. Use the 6 holes to secure the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` to the :adi:`ADISUSB`. The 12 pin cable included with the :adi:`ADISUSB` will plug into the J1 connector on the :adi:`ADIS16227/PCBZ <en/mems-sensors/mems-accelerometers/adis16227/products/EVAL-ADIS16227/eb.html>` board.

|image6| |image7|

Step #3
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position (factory-default). That is the correct JP1 jumper setting on the :adi:`ADISUSB`) required for the :adi:`ADIS16227CMLZ <en/mems-sensors/mems-accelerometers/adis16227/products/product.html>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

NOTE: If JP1 is left on **+5v** the software will look like the following picture. Move JP1 to the\ **+3.3V** setting to correct the problem.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-screen-voltage_error.png
   :width: 800px

ADIS16227_Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16227 Evaluation Software <static/imported-files/eval_boards/ADIS1622x_eval_software.zip>` to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16227` on an :adi:`ADISUSB` evaluation system. The download file will contain three separate files: The CAB file (ADIS16227_EVAL_Rev_2.cab), the setup file (setup.exe) and the setup list. Copy these files to a convenient folder for running the application from.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-zipfile-download.png
   :width: 900px

Navigate to the folder where the files were saved and double click the setup.exe file. The following pictures are a guide for the :adi:`ADIS16227` software install. The **Welcome** screen will appear click **OK** to continue.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default settings (recommended) and click the computer icon button to go to the next step.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click **Continue**. The last picture confirms completion click **OK** to finish.

|image8| |image9|

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The ADIS16227_EVAL_Rev_2.cab file contains USB drivers that are compatible with both 32-bit and 64-bit Windows systems. The drivers are unpacked the same time the software application is loaded by double clicking the setup.exe file. The first time the :adi:`ADISUSB` board is plugged into the computer (using the included USB mini cable) the hardware is recognized and loaded. The computer **Hardware Wizard** will find and install the drivers by following the steps below.

|image10| |image11|

The following pictures show the final steps for USB driver install. Click on **Next** then click on **Finish** completing the installation.

|image12| |image13|

.. warning::

   **WARNING:** For those who are using Windows XP, Service Pack 3, additional steps are required for completing the driver installation. Please see page 8, on the :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>` for additional information on these steps.


ADIS16227 Evaluation SOFTWARE
-----------------------------

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2 will illuminate as soon as this connection is made. This indicates that the :adi:`ADISUSB` has power and is going through its start-up/initialization process. During the initialization process, several messages may appear on the screen. They are related to updating the :adi:`ADISUSB` firmware and establishing communication between the PC and the :adi:`ADISUSB`. After the updates are finished double click on the ADiS16227_Eval_Rev_2.exe file to launch the software application.

Main Window
~~~~~~~~~~~

Once the :adi:`ADIS16227` Evaluation Software starts-up, the Main Window will appear and look like the following picture. The second picture provides color-coded boxes to support further discussion of each function in this screen.

|image14| |image15|

The orange box identifies the drop-down menus, which provide a number of useful features. The **Product** option provides a list of products for :adi:`ADIS16227` Evaluation, click on **Product** and then select :adi:`ADIS16227`. The green box shows the current device selection, which in this case, identifies the :adi:`ADIS16227` as the current selection.

The **Registers** option provides a listing of user-configurable registers in the :adi:`ADIS16227` and also provides read/write access to each one of these registers.

The **Datalog** option provides the core data collection function.

The **Start** option will start the selected mode capture process.

The yellow box identifies the waveform recorder window. The window contains the three accelerometer responses. Also, each waveform matches the color of its register.

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write access to the user registers in the :adi:`ADIS16227`. The following picture shows the appearance of this window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-registers.png
   :width: 600px

The color coded boxes illustrate the different functions that this window provides.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-register-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the Control/Status, this drop-down control offers access to **Output** and **Calibration** registers.

The red box identifies all of the registers that are in the current category. Click on the register name to select a register for individual read/write access.

The green box identifies the read/write control options for the current register selection. Use the hexadecimal format when writing commands to a particular register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

APPLICATION TIP: The **Register Access** screen writes to user control registers, inside of the :adi:`ADIS16227`, two bytes at a time. So, when configuring a register, make sure to include the hexadecimal number for all 16-bits, before pressing the **Write Register** button. When using an embedded processor to write to user control registers, inside of the :adi:`ADIS16227`, each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the data-ready signal from the :adi:`ADIS16227`. The following picture represents the Data Capture window, right after opening it from the **Main Window** and the second picture provides color-coded boxes, in order to support further discussion of each function that is associated with this screen.

|image16| |image17|

**Note:** The Main screen datalog option should be checked to enable the datalog function.

The green box identifies the configuration box for the name and location of the data storage file. The yellow box identifies a number of configuration options for the data acquisition process. The **Scaled Units** option causes the software to convert the decimal, twos complement number into its representative value. For example, when enabling **Use Scaled Data,** the accelerometer outputs will be in units of g's `g-force <https://en.wikipedia.org/wiki/G-force>`_.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16227`-specific content, but the :doc:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16448>` has some good examples to start with.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-dimensions.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-pcbz-mount-holes.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-pcbz-schematic.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-pcbz-parts.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-pcbz-part-mounted.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-mount-locates.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/223-adisusb-mounted.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-prgm-group.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-finish.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-screen.png
   :width: 800px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-main-screen-defined.png
   :width: 800px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-datalog.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/227-datalog-defined.png
   :width: 400px
