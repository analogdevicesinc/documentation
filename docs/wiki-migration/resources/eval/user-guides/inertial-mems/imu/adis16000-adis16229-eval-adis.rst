ADIS16000/ADIS16229 Evaluation with EVAL-ADIS
=============================================

OVERVIEW
--------

The :adi:`ADIS16000` and :adi:`ADIS16229` enable creation of a simple wireless vibration-sensing network for a wide variety of industrial-equipment applications. . The ADIS16000 provides the gateway function, which manages the network, while the ADIS16229 provides the remote sensing function. The :adi:`ADIS16000` SPI interface provides simple connectivity with most embedded processor platforms and the SMA connector interface enables the use of many different antennas. This module supports up to six :adi:`ADIS16229` devices at one time, using a proprietary wireless protocol. Once it has appropriate power on the VDD pin, the ADIS16000 will automatically begin a self-initialization process. Once this process is complete, the SPI interface activates and provides access to its register structure. The SPI interface supports connectivity with most embedded processor platforms, using the connection diagram below. The factory default configuration for DO1 provides a busy indicator signal that indicates when to avoid SPI communication requests.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-hook-up.png
   :align: center
   :width: 600px

REQUIRED MATERIALS
------------------

:adi:`ADIS16000AMLZ <ADIS16000>`

ADIS16COM1/PCBZ

:adi:`ADIS16229AMLZ <ADIS16229>`

:adi:`EVAL-ADIS`

Personal Computer

\* Windows

\* Net Framework 3.5

DEMO SYSTEM
-----------

:doc:`ADIS16229 Wireless Vibration Monitoring Demonstration System </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationdemo>`

Click on the link above to visit a demo system developed around the ADIS16000/ADIS16229.

ADIS16000 INSTALLATION ON EVAL-ADIS
-----------------------------------

For those who would prefer to perform PC-based evaluation of the ADIS16000/ADIS16229, before developing their own embedded system, the :adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system. This section focuses on mounting the :adi:`ADIS16000AMLZ <ADIS16000>`, ADIS16COM1/PCBZ and the :adi:`ADIS16229AMLZ <ADIS16229>` to complete the system shown below.

|image1| |image2|

.. container:: center round box

   **NOTE:** Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the setup. Wait until after the software installation is complete.


Step #1
~~~~~~~

Use the 4 M2 x.4 x 6mm screws from the included bag and line up the ADIS16COM1/PCBZ board with the highlighted "A" holes on the :adi:`EVAL-ADIS`. The mounting location holes are marked as an example in the picture below.

|image3| |image4|

.. warning::

   **WARNING:** Make sure that the connector cable going from J1 on the :adi:`EVAL-ADIS` is properly aligned to the J1 connector on the ADIS16COM1/PCBZ. The 16 pin cable is included with the :adi:`EVAL-ADIS` and proper mating is essential for correct operation.


.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-interface-mnt.png
   :width: 900px

Step #2
~~~~~~~

Carefully insert the :adi:`ADIS16000AMLZ <ADIS16000>` into the mating connector J2 of the previously installed ADIS16COM1/PCBZ interface board. Secure the board using the provided M3x .5 x 12mm screws (M3 washers are optional) and the M3 hex nuts.

|image5| |image6|

ADIS16229 INSTALLATION
----------------------

This section is a continuation and focuses on :adi:`ADIS16229AMLZ <ADIS16229>` setup to complete the system. The ADIS16229AMLZ provides a lead structure that enables simple connection with standard batteries. The SMA connector interface enables the use of many different antennas.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-asy1.png
   :width: 800px

.. _step-1-1:

Step #1
~~~~~~~

The :adi:`ADIS16229AMLZ <ADIS16229>` module is a 47.0x37.6x22.6mm PCB structure and provides 2 mounting holes. This example uses 2 M2 x .4 x 6mm screws to secure the :adi:`ADIS16229AMLZ <ADIS16229>` to an aluminum block. The standard (3.6 volt 1/2 AA) battery has been inserted into the battery holder and ready to be plugged into the :adi:`ADIS16229AMLZ <ADIS16229>` module. The battery connector should be inserted as shown in the picture with the keyed tabs sliding on and locking in the connector.

|image7| |image8|

.. warning::

   **WARNING:** Make sure the connector cable and the battery are installed correctly or the :adi:`ADIS16229AMLZ <ADIS16229>` may be damaged.


.. _step-2-1:

Step #2
~~~~~~~

The antenna connections to the SMA's are simple screw on connectors. Start by inserting the antenna straight onto the the SMA then gently screw it in. This should require very little force.

|image9| |image10| |image11|

.. container:: center round box

   **NOTE:** The antenna used in this :adi:`ADIS16229AMLZ <ADIS16229>` demonstration is: Linx Technology part number ANT-916-CW-QW-SMA. The antenna for the :adi:`ADIS16000AMLZ <ADIS16000>` is: Linx Technology part number ANT-916-CW-HWR-SMA. These are provided for the demonstration and may not suit all applications.


VIBRATION SOFTWARE INSTALLATION
-------------------------------

The :adi:`ADIS16229` vibration software link will be available shortly for download to a personal computer, which enables PC-based evaluation of the :adi:`ADIS16229` on an :adi:`EVAL-ADIS` evaluation system. The download file will contain three separate files: The USB drivers (SDPDrivers.exe), the application file (Vibration_Evaluation.exe) and the compressed zip file. Copy these files to a convenient folder for running the application from.

USB Driver Installation
-----------------------

After downloading the EVAL-ADIS USB Driver file, extract the SDPDrivers.exe file from the zip file, into a convenient location and then double click on it to start the process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-000.png
   :width: 500px

When the setup wizard opens, click on **Next** to start the installation process

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-001.png
   :width: 500px

Click on **Next** to accept the default driver location.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-002.png
   :width: 500px

The process will involve at least two progress bars that look like the following:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-003.png
   :width: 500px

If you encounter this type of message during the process, click on **Install** to continue with the installation.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-003a.png
   :width: 500px

Once the installation has completed, click on **Finish** to complete the process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/USBDriver-Install-004.png
   :width: 500px

VIBRATION SOFTWARE GUIDE
------------------------

The user upon successful installation of the required Vibration Evaluation application and successful setup of Evaluation Hardware can proceed to power up ADIS16000 (Gateway Node) and one ADIS16229 (Sensor Node) at a time. The user can then proceed to start the Evaluation application.

Main Menu Overview
------------------

When the application is opened, SPI communication is setup between ADIS16000 (Gateway Node) and the Evaluation board. Upon successful SPI communication with ADIS16000, a command to add a sensor node to the network is issued. A User message briefly appears on the screen to let the user know that ADIS16000 is actively looking to add a sensor node to its network. When the sensor node is added to the network, the following message is displayed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-sensor-added.png
   :align: center
   :width: 400px

When the user clicks on **ok** in the above message, the main window with an active tab 'Sensor 1' appears on the screen as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-main.png
   :align: center
   :width: 700px

.. container:: center round box

   <fc #800000>\ **Error Messages:** </fc>

   
   The application would fail to start in the event of no USB connection to the Evaluation board. When the user sees the following error message, Ensure that ADIS16000 is connected to the Eval Board.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/error-16000-not-found.png
      :align: center
      :width: 300px
   
   When the user sees the following error message, Ensure that ADIS16000 is selected in **Devices** drop-down menu.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/error-wrong-device.png
      :align: center
      :width: 300px
   
   User is notified of an unsuccessful addition of a sensor node to the network as shown below.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/error-sensor1-nf.png
      :align: center
      :width: 300px
   
   Unsuccessful addition of the sensor node can occur under the following circumstances..
   
   **Case 1:** A new sensor node had not been powered on during the initial start of the application. If this is the case, User can turn on the sensor and follow `connecting nodes <https://wiki.analog.com/adis16000-adis16229-eval-adis>`_ section for adding the new sensor.
   
   **Case 2:** ADIS16000 had been reset and the sensor node is already part of the network with a sensor identifier flashed in it. As a result, the sensor node does not respond to the command for adding a new sensor to Gateway. In order to check this case, follow `Scan Network section <https://wiki.analog.com/adis16000-adis16229-eval-adis>`_ for updating Gateway with already existing nodes.
   
   **Case 3:** ADIS16000 or ADIS16229 is in an unknown state. Power cycle both the parts and restart the application.
   


Manual Trigger Mode
-------------------

A sensor was successfully added to the network. User can start a FFT capture from sensor 1 by clicking on **Start** button. Any user initiated command is issued to the sensor node whose tab is currently active. For example, if Sensor 1 tab is held active by clicking on it and then a start command is issued, FFT capture is obtained from Sensor Node 1.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-manual-fft.png
   :align: center
   :width: 700px

Automatic/Period Mode
---------------------

In order to change the mode from Manual to Periodic FFT, the drop down box needs to be clicked and appropriate mode can be selected as shown below. Automatic mode is started with a default update interval of 2 secs. The automatic or periodic mode can be stopped by double clicking **<fc #800000>Esc key</fc>** twice by the user. The user is required to do this to take control of the application in Periodic mode.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-periodic-fft.png
   :align: center
   :width: 700px

Reconfiguring the Sensor Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

User can read the registers of the sensor by clicking on the menu **Register access** in the main window. A window with registers of Page 0 and Page X (x being the sensor node that is active) is displayed as shown below.

Sensor node can be updated in a 4 step process..

**Step 1:** Hold the respective sensor node active by clicking on its tab in the main wondow and then Click on Register access menu.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-register-menu.png
   :align: center
   :width: 600px

**Step 2:** In the register access menu, Scroll down to the registers of the respective sensor page indicated by Page column of the Table as shown below. Click on the register that needs to be modified

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-registers-defined.png
   :align: center
   :width: 600px

**Step 3:** Enter the new value in the box and hit Write.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-update-reg.png
   :align: center
   :width: 600px

**Step 4:** Scroll up to registers in Page 0 and then Select COMMAND_16K. Write the command 0x02 which is a command to update the sensor node. A wait of 400 ms will ensure that the sensor is updated with the new settings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-glob-cmd-reg-update.png
   :align: center
   :width: 600px

<fc #800000>\ **Sensor Reconfiguration in Periodic mode**\ </fc>

The user can alternately use Register access to set up the periodic mode. When a remote sensor is set up in periodic mode using Register access and data collection is started, the sensor can be stopped only by writing **0x800** to the <fc #800000>\ **COMMAND_S**\ </fc> register in the corresponding sensor page. **Writing 0x02 to COMMAND_16K should not be issued** to stop periodic mode. When the sensor is in periodic mode, it wakes up and updates the Gateway with the new data and also checks if any of its configuration had been changed by the user since its last update.

<blockquote> **If a stop command(0x800) is issued in COMMAND_S of the respective sensor page of Gateway, then the sensor reads the stop command and stops going further into sleep. The part puts itself in manual periodic mode and waits to get more commands for further action.** </blockquote>

<blockquote> **Instead of a stop command(0x800) if other the sensor registers are changed in its page, then the sensor reads those changes in its subsequenct update and reconfigures itself before going back to periodic mode.** </blockquote>

Connecting to ADIS16229 Nodes
-----------------------------

A user can add more sensors to the network by clicking on Network menu to invoke the Network control window followed by a 3 step process. The new sensors that need to be added to the network needs to be powered on one at a time during this process.

Step 1:Turn on one new sensor node that needs to be added to the network. Sensors already in the network can remain powered on.

Step 2:Click on the desired new sensor # in the network control window which is not active (not already assigned).

Step 3: Click on ADD sensor button to add the new sensor.

After a wait time of 5 seconds, the sensor should be successfully added to the network. Now the user could move on to the addition of the next new node if needed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-network.png
   :align: center
   :width: 700px

Alarm Configuration
-------------------

User can configure alarm thresholds for various sample rate options and bands using the Alarm Settings window that is invoked by clicking on Alarms menu

User can load a default setting for Alarms by first clicking on **Read Default Values** button and then clicking on **Write to Dut** button. After a wait time of 400 msecs, User can check if the operation was successful by clicking on **Read from DUT** button. Please note that **Write to DUT** command in the application flashes the settings on the part.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_alarm_settings.jpg
   :align: center
   :width: 600px

After this step, User can enable Alarms using the steps detailed in section Reconfiguring the Sensor nodes by

**Step 1 :** Write 0x03 to ALM_CTRL register in the respective sensor page.

**Step 2 :** Write 0x02 to COMMAND_16K in page 0 to update the sensor node that was recently updated in the previous step.

At this point, the Alarms are enabled in the sensor. Alarm status page can be opened to monitor alarms beyond this point.

The user can initiate a capture in Manual FFT mode to check for the Alarms. At the end of the capture, the Alarm status should refresh indicating the status of Alarms in the capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-alarms-status.png
   :align: center
   :width: 700px

When an alarm is triggered, the alarm status window indicates it with a yellow shade or a red shade on the corresponding band and axis in the table. The yellow shade indicates a lower threshold alarm has been activated. The red shade indicates that the higher threshold has been activated in the corresponding band and axis.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-alarm-level.png
   :align: center
   :width: 700px

Network Control
---------------

When the sensor nodes are already connected to the network and Gateway Node is reset using Software reset or a Power cycle, the sensor nodes can be retrieved by using the following steps.

**Step 1:** Click on the Network menu to invoke the Network control Window **Step 2:** Click on **Scan Network** button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-scan-network.png
   :align: center
   :width: 700px

The Gateway node checks for every node in the network( Node 1 through 6) and updates its sensor map at the end of it.

QUICK LINKS TO KEY ENGINEER ZONE CONTENT
----------------------------------------

MARC: Think about title for best branding

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-parts.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-system.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-16000-gateway.png
   :width: 480px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-16pin-cable.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-interface-16000amlz-mnt.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16000amlz.png
   :width: 290px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-block-mnt.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-batt1.png
   :width: 450px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-antenna-install.png
   :width: 460px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-blk-mnt-plugged-in.png
   :width: 370px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229-system-done.png
   :width: 850px
