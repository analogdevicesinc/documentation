.. _eval-adbms6830bmsw software-guide:

Software User Guide
====================

This software guide provides the essential steps for USB-to-SPI firmware
installation, launching the GUI, configuring the launcher, establishing
interface connections, and utilizing various tabs for effective device
evaluation. This covers tasks such as daisy chain configuration, quick
measurements, custom command sequences, scheduling, memory mapping, 
plotting, data recall, diagnostics, and EIS measurements.

Downloads
---------

.. admonition:: Download

   Evaluation GUI for ADI Broadmarket BMS products:
   :adi:`BMS Browser GUI Broadmarket <resources/evaluation-hardware-and-software/software/software-download.html?swpart=SD_ELPTRFU>`

Firmware
--------

Installing the Firmware
~~~~~~~~~~~~~~~~~~~~~~~

#.  Connect the microcontroller board (for this example, SDP-K1) to the host PC.
#.  Go to the USB_TO_SPI_FIRMWARE directory and find the latest firmware.
#.  Drag and drop the appropriate firmware file (e.g., ``SDP_K1_PyBMS_USB_TO_SPI_Bytes_Debug_USB_Port.hex`` 
    or ``usb-to-spi-max32690.hex``) onto the corresponding MCU’s USB drive 
    (e.g., SDP USB drive) to update the firmware. 
    
    .. figure:: usb_spi_firmware_list.png
       :align: center
  
       USB-to-SPI Firmware Location

.. tip:: 

   This software setup uses the SDP-K1 as microcontroller board, but users
   may also use the :adi:`AD-APARD32690-SL`. In order to flash the firmware image 
   on the :adi:`AD-APARD32690-SL` MCU board, it needs to be connected to 
   the :adi:`MAX32625PICO` programming adapter board.

**Instructions for flashing firmware image on MAX32625PICO**

#.  Access the `MAX32625PICO Firmware Repository <https://github.com/analogdevicesinc/max32625pico-firmware-images>`__
    and download the image for the specific MCU (e.g., MAX32690).
#.  Do not connect the MAX32625PICO from the PC and the MCU board that you are
    using (e.g., AD-APARDMAX32690-SL, MAX32670 MCU base board).
#.  Plug the micro-USB cable only in the MAX32625PICO.
#.  Press the button on the MAX32625PICO and then plug the other end of the
    micro-USB cable into the PC. (Do not release the button until the MAINTENANCE
    drive is mounted). 

    .. figure:: max32625pico_flasher.png
       :width: 300 px
       :align: center
  
       MAX32625PICO Firmware Flasher Button

#. Release the button once the MAINTENANCE drive is mounted.
#. Drag and drop (to the MAINTENANCE drive) the firmware image.
#. After a few seconds, the MAINTENANCE drive will disappear and be replaced by
   a drive named **DAPLINK**. This indicates that the process is complete, and the
   MAX32625PICO can now be used to flash the firmware to the Maxim MCU (e.g.,
   AD-APARD32690-SL, MAX32670 MCU base board) as indicated by Step #3 in
   "Installing the Firmware".

Application Software (GUI)
---------------------------

The EVAL-ADBMS6830BMSW comes with a graphical user interface (GUI) that
continuously monitors crucial BMS parameters. This interface facilitates
complete system control, enabling faster prototyping and development.

Launching the Graphical User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. To launch the GUI, navigate to the BMS_BROWSER_GUI_BroadMarket_V2.0.0 directory.
#. Double-click the ``BMS_BROWSER_GUI_BroadMarket_V2.0.0.exe`` file.

   .. figure:: bms_bm_browser_gui.png
      :align: center

      BMS Browser GUI BroadMarket Software Location

Launcher Configuration
^^^^^^^^^^^^^^^^^^^^^^^

#. Use the launcher page to configure a daisy chain of ADBMS devices.
#. Select an appropriately flashed microcontroller board (for this example,
   SDP-K1).
#. Launch the evaluation GUI.

Establishing Interface Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The Interface Connection section displays available SDP-K1 devices on the
   left.
#. Left-side selection determines the device for launching the evaluation GUI
   with the ``Launch`` button.
#. If the GUI is open, the connected COM port appears on the right.
#. Click ``Disconnect`` to terminate the connection for a new one.
#. Use the refresh button to reload the available MCU boards list.

.. figure:: interface_connection_v2.0.png
   :align: center
  
   Interface Connection Section

Daisy Chain Connection
^^^^^^^^^^^^^^^^^^^^^^

The Daisy Chain section facilitates the
creation of a daisy chain using compatible ADBMS devices. This process
involves selecting a generation of ADBMS devices, adding devices to the daisy
chain, and configuring the setup for the evaluation GUI.

.. figure:: daisy_chain_connection_v.2.0.png
   :align: center
  
   Daisy Chain Connection Setting

#. **Select ADBMS Generation:**

   - Navigate to the Daisy Chain section.
   - Use the first option to choose a specific generation of ADBMS devices.
   - Note: Devices within a selected generation are compatible and can be used
     together in the evaluation GUI.

#. **Add Devices to the Daisy Chain:**

   - After selecting the generation, locate the available devices list.
   - Choose a device for the daisy chain.
   - Press the right chevron button to append the selected device to the daisy
     chain.
   - This added device becomes the next farthest in the daisy chain.

#. **Remove Devices from the Daisy Chain:**

   - To remove a device, go to the daisy chain table.
   - Select the device you want to remove.
   - Press the trash can button to delete the selected device from the daisy
     chain.

#. **Configure Daisy Chain for GUI Launch:**

   - In the Interface Connection section, select the desired MCU board.
   - Configure the daisy chain in the Daisy Chain section.
   - Click on the launch button to initiate the evaluation GUI.

Graphical User Interface Tabs
-----------------------------

Quick Measure
~~~~~~~~~~~~~

The Quick Measure tab simplifies metric measurement with a preloaded command
sequence. Note that it supports a single device in the daisy chain, and key
features enhance configuration and visualization. 

.. figure:: quick_measure_utility.png
   :align: center
  
   Quick Measure Tab

#. **Preloaded Commands:**

   - Access the Quick Measure tab for easy metric measurement with a preloaded
     command sequence.

#. **Daisy Chain Limitation:**

   - Note: Quick Measure tab supports only a single device in the daisy chain,
     configured for the last device.

#. **Quick Configuration:**

   - Utilize the lower-left section for swift changes to commonly modified
     bitfields.

#. **Numeric Data Display:**

   - In the lower-right section, view numeric data returned from devices.
   - Control plotted data on the central plot using checkboxes.

#. **Central Plot Visualization:**

   - The central plot provides a graphical representation of captured data.
   - X-axis: Sample number; Y-axis: Metric-specific variation.

#. **Measurement Loop Control:**

   - Initiate and terminate the measurement loop with the top button.
   - The button turns yellow during loop activation and green when deactivated.

Sequences
~~~~~~~~~~

The Sequences tab enables the creation and management of
custom command sequences. Load and save sequences, divided into Init and Loop
lists. The Init list initializes the daisy chain once, while the Loop list
runs continuously until stopped. Toggle between lists using the corresponding
buttons at the top.

.. figure:: sequences.png
   :align: center
  
   Sequences Tab

#. **Load Existing Sequence:**

   - Use the Existing Sequence Files select bar to choose an existing sequence
     file.
   - Select the desired sequence from the Existing Sequences select bar.

#. **Save Sequence:**

   - In the New Sequence File text area, enter the name for the new sequence
     file.
   - Specify the sequence name in the New Sequence Name text area.
   - Press the save button to save the sequence.

#. **Load Defaults:**

   - Load the default command list for the Quick Measure tab by pressing the
     Load Defaults button.
   - All sequence files are saved in the installation location under the
     data/sequence directory.

#. **Add Command:**

   - On the left side of the screen, use the select boxes and buttons to add a
     command to the selected command list.
   - Select a command from the Commands select box to load available bitfields
     on the bottom left.
   - Modify bitfields as needed and press ``Add`` to add the command to the list on
     the right side.

#. **Manage Commands:**

   - On the right side, select a command to highlight it for modification.
   - Replace, move (drag and drop), or delete the highlighted command using the
     corresponding buttons.

#. **SPI Bus and Chip Select:**

   - Under the Command select bar, use the SPI Bus and SPI CS Select bars to
     change the SDP-K1 SPI bus and chip select for the command.

#. **Optional Map Key:**

   - Below the SPI Bus and SPI CS Select bars, use the optional Map Key field to
     apply a label to the command.
   - Labels organize output data, grouping commands with the same label together
     for focused data analysis.

Scheduler
~~~~~~~~~~

The Scheduler tab provides insights into the execution
time of sequences from the Sequences tab. It allows combining sequences for a
complete execution loop. Key features enable precise timing adjustments and
visualization. 

.. figure:: scheduler_v2.0.png
   :align: center
  
   Scheduler Tab

#. **Timing Adjustments:**

   - Utilize the SPI Clock field to adjust timings based on the system SPI clock
     frequency (kHz).
   - The MCU Command To Command Overhead field adjusts timing between commands
     to accommodate MCU transaction timings.
   - The FDTI field represents the total loop time, used for margin
     calculations.

#. **Initialization and Sequence Management:**

   - Choose the Initialization field to pick the sequence for daisy chain
     initialization.
   - The Available Cycle Sequences list displays all available sequences for
     scheduling.
   - Use the Add button to add selected cycles to the schedule.

#. **Hardware Timers and Timing Verification:**

   - Add hardware timers to cycle sequences with the Add Cycle Timers field for
     timing verification in freerun mode.

#. **Schedule Management:**

   - Remove and Clear buttons allow removal of cycles from the schedule.
   - Drag and drop cycles to rearrange them within the schedule.

#. **Schedule Overview:**

   - The schedule table displays added cycles, their execution time, and margin
     for the selected daisy chain.
   - The plot at the bottom visually represents the same information in a
     waterfall format.

#. **Transfer for Real Hardware Timing:**

   - Use the Transfer button to move all cycles into a single sequence in the
     Sequences tab.
   - Run the transferred sequence to assess real hardware timing.

Memory Map
~~~~~~~~~~~

The Memory Map tab provides a numerical output for the
active command loop, organized into tables for user convenience. It offers
customization and error highlighting for effective data analysis.

.. figure:: memory_map_v2.0.0.png
   :align: center
  
   Memory Map Tab

#. **Organized Data Display:**

   - Access the Memory Map tab for a numerical output of the currently running
     command loop.
   - Multiple tables organize the data into useful groups.

#. **Table Management:**

   - Each table can be minimized for a more streamlined view.

#. **Default View and Map Key Selection:**

   - The default view presents all data from the command list.
   - Use the Map Key select bar to switch to a specific group of data for
     focused analysis.

#. **Device-specific Data:**

   - Tables contain data returned by all devices in the daisy chain.

#. **Error Highlighting:**

   - Rows highlight in orange if data returned with a PEC error.
   - Valid data does not have any highlighting for easy differentiation.

Plots
~~~~~

The Plots tab provides a graphical representation of data
collected through the running command loop. It offers customization options
for focused analysis and allows for the export of captured data for further
analysis. 

.. figure:: plotfilter_v2.0.0.png
   :align: center
  
   Plots Tab

#. **Plot Selection:**

   - Use the Plot Selection area at the top to control the central Plot.
   - Checkboxes in the Plot Filter area at the bottom filter data for the Plot.

#. **Metric Plotting:**

   - Check the Plot Filter checkboxes for desired metrics and device numbers.
   - Additional checkboxes allow for plotting all devices for a metric, all
     metrics for a device, or all metrics for all devices.

#. **Save and Load Filter Setups:**

   - Save a filter setup for future use by providing a name in the Save Plot
     Filter text box and clicking Save.
   - Load existing filter setups using the Load Plot Filter select.

#. **Map Key Group Selection:**

   - Narrow data to a specific map key group using the Map Key select in the
     Plot Selection area.

#. **Plot Options:**

   - Choose between line chart and histogram using the Plot Selection Type
     select.

#. **Export Data:**

   - Click the Export Data button to export captured data as a CSV file for
     further analysis.
   - Data is exported to the data directory, grouped by map key.

Data Recall
~~~~~~~~~~~

The Data Recall tab allows you to retrieve and plot data
from previous freerun sessions stored in a database file. The interface is
similar to the Plots tab with added functionality for selecting the database
file and test run.

.. figure:: data_recall.png
   :align: center
  
   Data Recall Tab

#. **Access Data Recall Tab:**

   - Navigate to the Data Recall tab for recalling and plotting data from
     previous freerun sessions.

#. **Database File Selection:**

   - Click on the select box under the Database Names label.
   - Choose the desired database file; the default is data.db.

#. **Test Run Selection:**

   - Click on the select box under the Test Run IDs label.
   - Pick the specific test run from the list, arranged chronologically and UTC
     timestamped.

#. **Load Test Run:**

   - Click the Load Test Run button to recall data from the selected database
     file and test run.

#. **Customize Plot:**

   - After loading the test run, customize the plot using the same methods as
     the Plots tab.
 
Diagnostics
~~~~~~~~~~~~

The Diagnostics tab offers a straightforward way to execute on-device diagnostics 
following the device’s safety manual. It displays available diagnostics, test logs, 
and results for a single device.

.. figure:: diagnostics.png
   :align: center
  
   Diagnostics Tab

#. **Access Diagnostics Tab:**

   - Navigate to the Diagnostics tab for on-device diagnostics execution.

#. **Device Selection:**

   - Use the Device Selection bar to switch between devices.

#. **Run Diagnostics:**

   - In the ``Functions`` section on the left, click on the button with the name of
     the desired diagnostic.
   - The diagnostic runs, and results are displayed on the right side:
     highlighted green for pass and red for failure.

#. **Diagnostic Log:**

   - A log of diagnostic-specific data appears in the center of the screen.
   - The log provides context for understanding why a diagnostic may have
     failed.

Custom GUI Configuration
------------------------

The configuration settings in the GUI’s ``config.json`` file
allow users to tailor the software to their specific needs, providing a more
customized and efficient experience.

This section explores the three key settings: ``auto_detect_sdp``, ``limit_usb_polling``, 
and  ``display_user_manual_on_start`` - that users can adjust to better align the 
software to their intended applications.

Key Settings
~~~~~~~~~~~~

auto_detect_sdp:
^^^^^^^^^^^^^^^^

- **Purpose:** Determines whether the software automatically connects to all
  comports or requires manual selection of the NUCLEO comport.
- **Default Setting:** true
- **Modification:**

  - Open the config.json file located in the base directory of the software.
  - Locate the ``auto_detect_sdp`` setting and change its value to false.
  - Save the changes.

limit_usb_polling:
^^^^^^^^^^^^^^^^^^

- **Purpose:** Controls the poll rate of the NUCLEO comport, balancing CPU usage
  and sample rate.
- **Default Setting:** false
- **Modification:**

  - Open the config.json file.
  - Find the ``limit_usb_polling`` setting and change its value to true if a
    reduced poll rate is preferred.
  - Save the changes.

display_user_manual_on_start:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Purpose:** Governs whether the user manual is displayed each time the
  software starts.
- **Default Setting:** true
- **Modification:**

  - Open the config.json file.
  - Locate the ``display_user_manual_on_start`` setting and change its value to
    false if you prefer not to see the manual on startup.
  - Save the changes.

.. tip::

   By adjusting these configuration settings in the config.json file, 
   users can optimize the software’s behavior to better suit their requirements. 
   Whether it’s fine-tuning comport connections, managing CPU usage, or controlling 
   the display of the user manual, these settings provide a flexible approach to enhancing 
   the software’s usability. Make sure to save your changes and restart the software 
   for the modifications to take effect.

Further Help
------------

For questions and more information about this product, connect with us through
the :ez:`Analog Devices EngineerZone <reference-designs>`.
