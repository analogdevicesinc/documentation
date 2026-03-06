ADIS16229 VIBRATION MONITORING DEMONSTRATION SYSTEM
===================================================

This system provides a simple way to demonstrate the concept of a remote vibration monitoring system, using the :adi:`ADIS16000` and :adi:`ADIS16229`. All of the necessary components fasten to a fluorescent yellow plate and the system requires two USB ports on a PC to support full operation. One of the USB cables manages communication with the Gateway node (:adi:`ADIS16000`) and the other supplies power to the vibration source. The vibration source is a simple, off-balance motor that comes in a black plastic case. The potentiometer provides a gross tuning method for controlling the amount of vibration on the platform.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229demo-completesystem01.png
   :width: 400px

BATTERY
=======

The ADIS16229AMLZ runs off of a +3.6Vdc, 1/2 AA, Lithium Ion battery. The one shown in this picture is manufactured by Saft (P/N: LS14250) and is available through many different online sources. Just Google-search "Saft LS-14250" to produce a list of sellers. The other parts for the battery assembly are: The battery holder 1/2AA cell Memory Protection Devices (P/N: BH1/2AA-3), Connector housing TE Connectivity (P/N: 1375820-2) and Connector Pins TE Connectivity (P/N: 1445336-3). The wire should be 22 AWG to 28 AWG and soldered to the battery holder posts.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/battery-assembly.png
   :width: 400px

DEMO PLATE ASSEMBLY
===================

This kit supports a very simple setup process.

Step #1: Verify all necessary materials
---------------------------------------

The following picture identifies all of the key components of this demonstration system.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-kitcontents04.png
   :width: 600px

Step #2: Install ADIS16000AMLZ Antenna
--------------------------------------

Start by installing the longer antenna on the :adi:`ADIS16000AMLZ's <ADIS16000>` SMA connector. This particular antenna has an elbow joint, which is flexible but tightens with the SMA connection. Make sure that its final orientation support supports full upright antenna positioning, once the antenna is secure. The following illustration provides the start, interim and final views of this installation process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_000-antenna04.png
   :width: 800px

Step #3: Install ADIS16229AMLZ Antenna
--------------------------------------

Install the shorter antenna onto the :adi:`ADIS16229AMLZ's <ADIS16229>` SMA connector. See the following pictures for the start, interim and complete states of this process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-antenna05.png
   :width: 800px

Step #4: Install ADIS16229AMLZ
------------------------------

Find the two holes on the side of the plate, located next to the black plastic motor case. Use (2) M2x0.4x12 machines screws (at least 8mm long) to secure this assembly to the plate. NOTE: The threads can strip, only tighten to "finger-snug."

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-install01.png
   :width: 800px

Step #5: Install Battery
------------------------

Install the battery, with the positive terminal on the side that has the red wire, as shown in the following pictures:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-battery03.png
   :width: 800px

Step #6: Connect EVAL-ADIS to PC
--------------------------------

Verify that **JP1** on the :adi:`EVAL-ADIS` is set to +3.3V, then connect it to the PC, using one of the Mini USB cables in the kit. **LED2** will illuminate immediately and **LED1** will take up to 10 seconds to illuminate. **\*LED2** indicates that the :adi:`EVAL-ADIS` now has power and **LED1** indicates that the :adi:`EVAL-ADIS` is communicating with the PC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_000-eval-adis01.png
   :width: 800px

Step #7: Connect Motor
----------------------

Before connecting the motor to the PC, turn the potentiometer all of the way, counter-clockwise, to set the vibration to its lowest possible setting. Then, connect the motor to a PC, using one of the Mini USB cables for power. After connecting this to the PC, turn the potentiometer in the clockwise direction, until the vibration level is sufficient for the demonstration.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-vibemotor.png
   :width: 800px

Step #8: Connect ADIS16229AMLZ to Battery
-----------------------------------------

When ready to start testing, connect the :adi:`ADIS16229AMLZ <ADIS16229>` to the battery. Use the following pictures to guide the installation process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_229-battery04.png
   :width: 800px

VIBRATION EVALUATION PROGRAM
============================

Software Download & Initial Setup
---------------------------------

This section will offer software tips for using this demonstration system. For a complete guide to the Vibration Evaluation Program, click on the following link: :doc:`Vibration Evaluation Program Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/vibrationevaluationprogram>`

Getting Started
---------------

After starting the software by double-clicking on the software's executable file, a number of things will take place. These items may appear to happen in alternate orders, but first, the USB connection window will appear and another Window will appear, with a message of updating the :adi:`eval-adis` firmware.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-01.png
   :width: 400px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-02.png
   :width: 400px

This will be followed by an attempt to connect with the sensor, which will take approximately 5 seconds, then a "success" message, if the connection was completed and verified:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-04.png
   :width: 400px

Click on **OK** and the **Main Menu** will appear.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-mainmenu01.png
   :width: 800px

Managing Error Messages
-----------------------

.. container:: center round box

   <fc #800000>\ **Typical Error Messages and Solutions:** </fc>

   
   The application would fail to start in the event of no USB connection to the Evaluation board. When the user sees the following error message, Ensure that ADIS16000 is connected to the Eval Board.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/device_selection.jpg
      :align: center
      :width: 300px
   
   When the user sees the following error message, Ensure that ADIS16000 is selected in **Devices** drop-down menu.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/16228.jpg
      :align: center
      :width: 300px
   
   User is notified of an unsuccessful addition of a sensor node to the network as shown below.
   
   .. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/16629_unsuccessful_addition.jpg
      :align: center
      :width: 300px
   
   Unsuccessful addition of the sensor node can occur under the following circumstances..
   
   **Case 1:** A new sensor node had not been powered on during the initial start of the application. If this is the case, User can turn on the sensor and follow `connecting nodes <https://wiki.analog.com/vibrationdemo>`__ section for adding the new sensor.
   
   **Case 2:** ADIS16000 had been reset and the sensor node is already part of the network with a sensor identifier flashed in it. As a result, the sensor node does not respond to the command for adding a new sensor to Gateway. In order to check this case, follow the instructions for scanning the network in the `Network Control section <https://wiki.analog.com/vibrationdemo>`__ to update the :adi:`ADIS16000` (Gateway) with already existing nodes.
   
   **Case 3:** ADIS16000 or ADIS16229 is in an unknown state. Power cycle both the parts and restart the application.
   


Connecting to ADIS16229 Nodes
-----------------------------

A user can add more sensors to the network by clicking on Network menu to invoke the Network control window followed by a 3 step process. The new sensors that need to be added to the network needs to be powered on one at a time during this process.

Step 1: Turn on one new sensor node that needs to be added to the network. Sensors already in the network can remain powered on.

Step 2: Click on the desired new sensor # in the network control window which is not active (not already assigned).

Step 3: Click on **Add Sensor** button to add the new sensor.

After a wait time of 5 seconds, the sensor should be successfully added to the network. Now the user could move on to the addition of the next new node if needed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_add_sensor.jpg
   :align: center
   :width: 700px

Network Control
---------------

When the sensor nodes are already connected to the network and Gateway Node is reset using Software reset or a Power cycle, the sensor nodes can be retrieved by using the following steps.

**Step 1:** Click on the Network menu to invoke the Network control Window **Step 2:** Click on **Scan Network** button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/scan_network.jpg
   :align: center
   :width: 600px

The Gateway node checks for every node in the network ( Node 1 through 6) and updates its sensor map at the end of it.

Demo Modes
----------

Click on the **Demo** option in the Menu bar to reveal two different options: **Network Manual FFT** and **Network Periodic FFT**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-06.png
   :width: 800px

Network Manual FFT
------------------

The **Network Manual FFT** option causes the :adi:`ADIS16229` to run a continuous loop of data capture, analysis, and communication of the FFT results to the **FFT Display Window** in the Vibration Analysis Software. This is the simplest mode to run a demonstration in but it will only support ~14-16 hours of battery life. The following screen shows the FFT, with a relatively low noise floor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-07.png
   :width: 800px

Once this mode is in operation, you can hit the **Stop** button to stop it or you can hit the **Esc** key. This function is still being tested and improved. At the present time, using the **Esc** seems to be more robust.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-06a.png
   :width: 800px

After starting this mode, start turning the potentiometer on the motor, until it starts to respond. After it starts vibrating, turn it down as low as possible, without completing stopping the vibration. When the motor is on, it typically generates enough sound to hear.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-08.png
   :width: 800px

While tweaking the motor up, notice the change in the FFT result, on the y-axis in particular.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-09.png
   :width: 800px

To change the scale on the plot, hover the mouse pointer over the results area and **Right Click** to reveal the scale adjustment window.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-10.png
   :width: 800px

Click on the **>** button in this window to increase the range on the scale.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-11.png
   :width: 800px

Click on **Close** to close the scale adjustment box.

If the motor vibration is high enough, the plate could start moving around on its surface. Notice the change in the FFT profile: the magnitude increases, but at the lower frequencies.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-12.png
   :width: 800px

Network Periodic FFT
--------------------

Going back to the **Main Window** and the **Demo** option, the **Network Periodic FFT** mode will cause the :adi:`adis16229` to wake-up every 10 seconds, collect data, analyze the data, transmit the results to the PC (through the :adi:`ADIS16000`, ADIS16COM1/PCBZ and the :adi:`EVAL-ADIS`) and then go back to sleep again. When using this mode, the LED on the :adi:`ADIS16229` will blink when it is on (approximately one time every 10 seconds). Also, note that the **System Development Platform Wait** window will appear during the "Sleep time" for the :adi:`ADIDS16229 <ADIS16229>`.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-14.png
   :width: 800px

When using this mode, use the **Esc** key to break this process.

Alarm Demonstration
-------------------

Step #1: Calculate Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's start with a simple example, where we will set a single alarm band to monitor in this demo system. The following figure establishes the start frequency, stop frequency on one of the levels (Alarm 1), which serves as the "warning" level.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-01.png
   :width: 800px

Step #2: Configure Alarms
~~~~~~~~~~~~~~~~~~~~~~~~~

After establishing the start frequency, stop frequency and alarm threshold levels, click on the **Alarm** menu option and then, select the **Alarm Settings** option. The following graphic highlights the entries that will realize the settings from the first step in this process.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-02.png
   :width: 800px

Start by updating the boxes with the entries in the graphic below. Note that the "262" simply sets Alarm 2 at a level that is 2x greater than Alarm 1. After the entries are complete, click on **Write to DUT** and wait for the Yellow update box to disappear (this will happen quickly). After this, close window and return to the **Main Menu**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-03.png
   :width: 800px

Step #3: Enable Alarms
~~~~~~~~~~~~~~~~~~~~~~

Go into the **Register Access** Menu and scroll down to the **ALM_CTRL**, located at addess **0x30**, as shown in the screen. Select the register.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-04.png
   :width: 800px

Enter "2" into the **User Entry Box**, as shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-05.png
   :width: 800px

Click on **Write** as shown in the graphic below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-06.png
   :width: 800px

Step #4 - Configure Remote Sensor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scroll up to find the **GLOB_CMD_G** register, located at address **0x12**, as shown in the graphic below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-07.png
   :width: 800px

Select this register with the mouse and then enter **2** into the **User Entry** box.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-08.png
   :width: 800px

Click on **Write**, as shown in the graphic below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-09.png
   :width: 800px

Step #5 - Check Results in Main Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go back to the **Main Menu** and click on the **Alarm** option, then click on the **Alarm Status Form**. This will reveal a blank status form.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-11.png
   :width: 800px

Click on **Start** and notice the FFT results. Reveal the **Alarm Status Form** and determine if the vibration exceeds an alarm level.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-12.png
   :width: 800px

Experiment with increasing the vibration and try again.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-13.png
   :width: 800px

Step #6 - Check Results in Register Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on **Update Registers in Category**. The following graphic shows the results that come from the **ALM_Y_STAT**, **ALM_Y_PEAK** and **ALM_Y_FREQ** registers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/229_vibedemo_vep-alarmdemo-10.png
   :width: 800px

Additional Resources
--------------------

:doc:`ADIS16000/ADIS16229/EVAL-ADIS Wiki Guide </wiki-migration/resources/eval/user-guides/inertial-mems/imu/adis16000-adis16229-eval-adis>`
