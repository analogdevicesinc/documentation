ADXL362 Real-Time Evaluation System
===================================

.. important::

   This page is under construction.


Resources
---------

Kit Contents
~~~~~~~~~~~~

| 1 x Low-Power Inertial Sensor Evaluation Board (LP-ISEB) (also referred to as Motherboard)
| 1 x ADXL362 Satellite Board
| 1 x ADXL362 Micropower MEMS Accelerometer
| 1 x Ribbon Cable (connects Motherboard to Satellite board)
| 1 x USB cable (connects Motherboard to computer)
| 8 x Standoffs + screws (stabilize the Motherboard and Satellite board on a flat surface)

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Schematics: | `Motherboard <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/motherboard_schematic.pdf>`__ | `Satellite Board <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/satellite_board_schematic.pdf>`__ |
+=============+============================================================================================================================================+====================================================================================================================================================+
| Layouts:    | Motherboard                                                                                                                                | Satellite Board                                                                                                                                    |
+-------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Installation Files
~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   // //

   
   -  **Driver installer:** `.zip <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/adi_iseb_drivers.zip>`__
   -  **LabView environment and GUI installer:** :adi:`.zip <static/imported-files/eval_boards/ADXL362_EVB_GUI_Installer.zip>`
   


--------------

Quick Start Guide
-----------------

For first-time installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: center box

   
   +-------------------------------------------------------------------------------------------------------------------+


   
   | :!:\*\* If you've never used ANY of Analog Devices' Inertial Sensor Evaluation Kits before\*, start here! \*\*:!: |

   | *\*This includes any of ``EVAL-ADXL###Z-M``, ``EVAL-ADXRS###Z-M`` and ``EVAL-ADXL###Z-MLP``.*                     |
   +-------------------------------------------------------------------------------------------------------------------+
   


-  **Begin by installing the drivers.**
   Click on the link `above <https://wiki.analog.com/>`__ to download the driver installer. Extract the entire contents of the folder and run the file **ADI_ISEB_USB_Drivers.exe**.
   Follow the installer instructions to install the drivers.
   \* **Next, install the GUI.**
   Download and run the ADI-provided **LabView environment and GUI installer**, also `above <https://wiki.analog.com/>`__.
   Follow the installer instructions.
   ==== For returning users ====

   | **Prior to starting the GUI, plug in the system:**
|

.. container:: indent

   Connect the motherboard to the satellite board via the ribbon cable.

   |


.. container:: indent

   Then, connect the motherboard to the computer via the USB cable.


| The ADI installer places a shortcut to the GUI in the Start menu under ``All Programs`` -> ``Analog Devices - Inertial Sensor Eval``, as shown below. Click on this shortcut to start the evaluation system GUI.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/start_menu.png
   :alt: Click for full-size image
   :width: 200px

| The GUI starts up grayed out with all functions disabled. Before testing any devices, you must associate the software GUI with the installed hardware by selecting the appropriate COM port from the menu in the lower left corner. **Follow** :doc:`these instructions </wiki-migration/resources/eval/user-guides/inertial-mems/evalsystem/findyourcomport>` **if you do not know which COM port to use.**
| Selecting the appropriate COM port and clicking Connect should enable all GUI functionality.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/1.png
   :alt: Click for full-size image
   :align: center
   :width: 400px

// // To end the program, click the “Quit Program” button at the bottom right corner of the GUI screen, and then use the X at the top right to close the window.

--------------

Debug Tips
----------

In no particular order, here are a few tips for troubleshooting the system when things aren’t working:

-  If you see a yellow triangle next to the icon in the Device Manager, consult the Driver Troubleshooting section.
-  Verify the COM port in the Device Manager window. Ensure that you are connecting to this COM port when opening the GUI.
-  Reflash the firmware.
-  Make sure there is a part inside the socket: with the board unplugged (unpowered!), open the socket lid and look for a part. If you’re unsure, turn the (open) socket over into your hand and see if a part falls out. If it does, put it back in. If it does not, get another.
-  Try a new USB port; a new USB cable; and reconnect the ribbon cable, to isolate the possibility of a faulty connection.
-  Try restarting the connection. Follow these steps in this order:

   -  Quit the GUI and close the GUI window.

      -  Unplug the motherboard from the USB port.
      -  Count to 10.
      -  Plug the motherboard back in.
      -  Start the GUI and try again.

--------------

The GUI
-------

The ADXL362 Evaluation System GUI includes 4 tabs for evaluation of various paramaters:

+---------------------------------------------------------+----------------------------------------------------------------------------------+
| `Real-time data <https://wiki.analog.com/>`__:          | **View and save real-time acceleration measurements under user-input settings.** |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                         |                                                                                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
| `Power consumption <https://wiki.analog.com/>`__:       | **View real-time power consumption under user-input settings.**                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                         |                                                                                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
| `Temperature <https://wiki.analog.com/>`__:             | **View the effect of temperature on acceleration output.**                       |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                         |                                                                                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------+
| `Configuration <https://wiki.analog.com/>`__:           | **Write to and read from device registers.**                                     |
+---------------------------------------------------------+----------------------------------------------------------------------------------+

--------------

Real-Time Data
~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/2.png
   :alt: Click for full-size image
   :align: center
   :width: 600px

The Real Time Data tab configures the inertial sensor evaluation system and the ADXL362 for real-time acceleration monitoring. The tab contains an oscilloscope-like interface that you can use to view the output of the accelerometer and adjust the relevant parameters, such as output data rate, measurement range, output format, different work mode for power/noise tradeoff and Self Test (see figure above).

**Configuration options:**

-  **

.. container:: em

   Data Rate (Hz)


**: choose the desired output data rate from the pull-down list.
-  **

.. container:: em

   Range (g)


**: choose the desired full-scale measurement range from the pull-down list.
-  **

.. container:: em

   Output Format


**: choose between 8-bit and 12-bit (default) data.
-  **

.. container:: em

   Low Noise Mode


**: choose between Normal Mode (lowest power consumption), Low Noise Mode, and Ultralow Noise Mode (lowest noise).
-  **

.. container:: em

   Half BW


**: select whether the anti-aliasing filter bandwidth is set to 1/2 ODR (wider bandwidth for given ODR) or 1/4 ODR (less susceptibility to aliasing, therefore improved signal integrity).
-  **

.. container:: em

   Self Test


**: engage self-test. You should see an offset appear on all 3 outputs when you chose this option.

**Functionality:**

-  **

.. container:: em

   Begin real-time measurement


** by clicking the **``View Meas``** button. This causes many of the options and tabs to be grayed out or to disappear, to prevent software conflicts, until the Stop Meas button is clicked. The accelerometer output data then begins to flow across the screen.
-  **

.. container:: em

   Begin and save real-time measurement


** by clicking the **``View & Save Meas``** button.

.. container:: INDENT

   When this button is clicked, the user is prompted to specify a file name and location for saving the data. Data is saved into a tab-delimited .txt file. The first row of the file always contains column labels denoting Date, Time, X, Y, and Z (for acceleration data in *g*).

      The Save functionality is capable of saving unlimited data. To keep file size manageable, the data is split up into up to 11 separate .txt files. The first 10 files have a capacity of 64000 samples. The 11th file will contain all remaining data.
   The name and location of the first .txt file are specified by the user upon clicking the ``View & Save Meas`` button. All 11 files are created as soon as the first file name and location are specified. Consecutive numeric suffixes are appended to the specified file name, and all 11 files are saved to the same location. For example, if the first file is named ``ADXL362Test.txt`` and saved to the desktop, then 11 files will be automatically created on the desktop: ``ADXL362Test.txt``, ``ADXL362Test_1.txt``, ..., ``ADXL362Test_10.txt``. Files will be filled in order as data becomes available. When measurement is stopped (via the GUI), empty files are automatically deleted.


-  **

.. container:: em

   Stop real-time measurement


** by clicking the **``Stop Meas``** button.

**Other readouts / indicators:**

-  **

.. container:: em

   Output Graph


**

   -  X-, y-, and z-axis acceleration values are plotted on the graph in white, red, and green respectively.
   -  Data can be shown in LSBs or in *g*'s, as selected by the ``Output - LSB`` or ``Acceleration - g`` tab above the graph.
   -  Use the controls in the top-right of the graph frame to recenter, zoom, and move the graph.
   -  Double-click on any of the axes values and type in a new value to re-scale that axis.
   -  Right-click in the graph area for additional options.

-  **

.. container:: em

   Bias Values


**

   -  **Current Vs [V]**: shows the measured supply voltage to the ADXL362.
   -  **Current**: shows the current consumption of the ADXL362 in µA.
   -  **Current VDD I/O [V]**: shows the measured supply voltage to the digital portion of the ADXL362 (digital logic and SPI communication).
   -  **Temp [degC]**: shows the ambient temperature, as measured by a sensor on the satellite board.

-  **

.. container:: em

   Output Values


**

   -  Shows x-, y-, and z-axis output values in LSBs and in *g*'s. The conversion to *g*'s assumes ideal scale factor.

--------------

Power Consumption
~~~~~~~~~~~~~~~~~

When used properly, the ADXL362 offers extremely low *system-level* power consumption in addition to its own device-level power savings. A deep FIFO, robust motion (and lack-of-motion) detection, and autonomous interrupt processing allow the accelerometer to operate as a motion sensor and a power manager without the intervention of a host processor. The Power Consumption tab is designed to highlight some of the ADXL362's system-level power savings features.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/3.png
   :alt: Click for full-size image
   :align: center
   :width: 600px

The following functionality is available to you within the Power Consumption tab:

Modes of Operation
^^^^^^^^^^^^^^^^^^

-

.. container:: em

   Measurement


: Configures the accelerometer for measurement mode, in which acceleration is sampled continuously at the specified data rate.
-

.. container:: em

   Standby


: Configures the accelerometer for Standby. The device is non-operational and consumes only 10 nA.
-

.. container:: em

   Auto Sleep


: Configures the accelerometer for autosleep. When inactivity is detected, the accelerometer enters a low-power, low-bandwidth mode; when activity is detected, the accelerometer enters measurement mode.
-

.. container:: em

   Wake Up


: Configures the accelerometer for wakeup mode. This is a low-power, low-bandwidth mode in which acceleration is sampled ~6 times per second, and the accelerometer sleeps to conserve power between samples.

-

.. container:: em

   Meas Range


: select the desired full-scale measurement range.
-

.. container:: em

   Data Rate (Hz)


: choose the desired output data rate from the pull-down list.
-

.. container:: em

   Half BW


: select whether the anti-aliasing filter bandwidth is set to 1/2 ODR (wider bandwidth for given ODR) or 1/4 ODR (less susceptibility to aliasing, therefore improved signal integrity).
-

.. container:: em

   Low Noise Mode


: choose between Normal Mode (lowest power consumption), Low Noise Mode, and Ultralow Noise Mode (lowest noise).

Activity Configuration
^^^^^^^^^^^^^^^^^^^^^^

-

.. container:: em

   ✔ Activity Interrupt


: when checked, enables activity detection.
-

.. container:: em

   THRESH_ACT [mg]


: specify the threshold, in m\ *g*, for activity detection.
-

.. container:: em

   Time_Act [num]


: specifies the number of consecutive samples that must be above the activity threshold (THRESH_ACT) for an activity event.
-

.. container:: em

   Coupling


: selects between AC (Referenced) and DC (Absolute) activity detection.

Temperature
~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/4.png
   :alt: Click for full-size image
   :width: 600px

Configuration
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/5.png
   :alt: Click for full-size image
   :width: 600px
