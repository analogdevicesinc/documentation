.. _ad-pqmon-sl software-guide:

Software User Guide
===================

Equipment needed
----------------

- AC power supply or connection to mains for the measurement side
- Mains or USB type C connector cable for supplying power to the board
- PC running Windows or Linux
- Cable to build the assembly
- USB type C connector cable to connect to the USB port of the PC. (this can be
  used also to deliver power to the board)
- :adi:`AD-PQMON-SL` evaluation board

*Optional:*

- :adi:`MAX32625PICO` for debug and programming

Testing
-------

The following software is needed for testing the :adi:`AD-PQMON-SL` board:

- Firmware (link available in the resources section)
- `Scopy <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/scopy-windows-x86_64-setup-7797088.zip>`__
  with the :adi:`AD-PQMON-SL` add-on

For Scopy installation, follow the steps indicated
:external+scopy:doc:`in the user guide <user_guide/index>`.

After making the board connections and installing Scopy,
connect to the GUI by following these steps:

- Connect the USB Type-C cable from the AD-PQMON-SL board to your PC.
- Launch the installed Scopy application.
- Click the “+” button as shown in the following image:

  .. figure:: scopy0.jpg

- In the window that opens, click the refresh button as shown in the following image:

  .. figure:: scopy2.jpg

- From the drop-down menu labeled ``PORT NAME``, select the COM port connected
  to the AD-PQMON-SL board (for example, COM37).

  .. figure:: scopy3.jpg

- After selecting the correct COM port, the URI field will be automatically populated.

  .. figure:: scopy4.jpg

- Click the ``Verify`` button.

  .. figure:: scopy5.jpg

- Ensure that ``PQMPlugin`` is selected in the plugin list.

  .. figure:: scopy6.jpg

- Click the ``ADD DEVICE`` button.

  .. figure:: scopy7.jpg

- In the next window, click the ``Connect`` button.

  .. figure:: scopy8.jpg

- A confirmation message, as shown in the following image, indicates a successful connection.

  .. figure:: scopy9.jpg

Measurements
------------

- The measurements tabs are available on the left side of the GUI:

  .. figure:: scopy10.jpg

RMS Tab
~~~~~~~

- The RMS tab can be activated by clicking on it and then selecting the
  Run button.

  .. figure:: scopy11.jpg

  .. figure:: scopy12.jpg

- The PQEvents indicator notifies the user when a PQ event has occurred. Events are
  saved in the log file if logging is enabled.

  .. figure:: scopy12_1.jpg

- If an event occurs during the session, the PQEvents indicator will become
  active. The event details can be found in the log file (in the RMS tab, only PQ
  events are logged). The indicator remains active until the user clicks on it, which
  resets the indicator. Even if the indicator is not reset, any new event will be
  registered in the log file.

  .. figure:: scopy13_5.jpg

- Logging can be enabled only when the measurement is not running. First, select the
  LOG button. Then, specify a log directory by clicking the button highlighted in the
  following image.

  .. figure:: scopy12_2.jpg

- Choose a folder where the data will be saved in CSV format. The
  file will be named as follows: “nameofactivewindow_date_time.csv”
  (e.g. rms_01-01-2024_11-00-00).

  .. figure:: scopy12_3.jpg

- After the folder is selected, data will be recorded during a session. The
  session starts when the Run button is activated and ends when it is
  stopped.

  .. figure:: scopy12_4.jpg

  .. figure:: scopy12_5.jpg

- A snapshot of an RMS log file is shown in the following image. As seen,
  several PQ events occurred during the session.

  .. figure:: rms_tab_events.jpg
     :width: 1000px

Harmonics Tab
~~~~~~~~~~~~~~

- The Harmonics tab can be activated by clicking on it and then selecting the
  Run button.

- To display the harmonics for different waveforms, select the desired line from the
  table above the graph.

- The THD (Total Harmonic Distortion) values are shown for each measurement next to the THD label.

- The PQEvents indicator notifies the user when a PQ event has occurred. Events are
  saved in the log file if logging is enabled.

  .. figure:: scopy13.jpg

- The user can select between viewing harmonics or interharmonics.

  .. figure:: scopy13_1.jpg

- Logging can be enabled only when the measurement is not running. First, select the
  LOG button. Then, specify a log directory by clicking the button highlighted in the following image.

  .. figure:: scopy13_2.jpg

- Choose a folder where the data will be saved in CSV format. The
  file will be named as follows: “nameofactivewindow_date_time.csv”
  (e.g. harmonics_01-01-2024_11-00-00).

  .. figure:: scopy13_3.jpg

- After the folder is selected, data will be recorded during a session. The
  session starts when the Run button is activated and ends when it is
  stopped.

  .. figure:: scopy13_4.jpg

- If an event occurs during the session, the PQEvents indicator will become
  active. The event details can be found in the log file. The log file in the Harmonics
  tab contains both the harmonics values and the PQ events, interleaved at the time
  the event occurred. The indicator remains active until the user clicks on it, which
  resets the indicator. Even if the indicator is not reset, any new PQ event will be
  registered in the log file.

- A snapshot of a harmonics log file containing only harmonics data is
  shown in the following image.

  .. figure:: harmonics_tab_log.jpg
     :width: 1000px

- In the following snapshot, PQ events can be seen interleaved with
  the harmonics values.

  .. figure:: harmonics_tab_events.jpg
     :width: 1000px

Waveforms Tab
~~~~~~~~~~~~~

- The Waveform tab can be activated by clicking on it and afterwards select the
  Run button.

  .. figure:: scopy16.jpg

- The upper side graph is the voltage and the one to the bottom is the current.
  To zoom in use the mouse to click and drag.

  .. figure:: scopy17.jpg

- The log file can also be activated in the waveforms tab in the same manner
  explained in the rms or harmonics sections, but in this case the PQ events is
  not present. If PQ events need to be recorded, then the other two tabs (rms,
  harmonics) must be used. The data logged in this tab contains only the
  waveforms values.

  .. figure:: scopy17_1.jpg

-  A snapshot of a log file can be seen in the following image.

   .. figure:: waveforms_tab_log.jpg

Settings Tab
~~~~~~~~~~~~~

- The Settings tab is used to read and set the thresholds and the config values.
  Activate it by selecting it from the right-side menu.

  .. figure:: scopy18.jpg

- To see all the parameters scroll down

  .. figure:: scopy18_1.jpg

- To read the values that are currently set click the Read button.

  .. figure:: scopy18_2.jpg

  .. figure:: scopy18_3.jpg

- To modify a parameter select it, change its value to the desired one and click
  the Set button.

.. tip::

   More information about the **Scopy PQMON addon** can
   be consulted
   :external+scopy:doc:`here <plugins/pqm/index>`

The system comes pre-programmed with a firmware that works with the **Scopy**
application, allowing complete system evaluation.

**Scopy** will work only with the official
:git-no-OS:`firmware releases <projects/eval-pqmon>`

.. _ad-pqmon-sl software-guide firmware-update:

Firmware Update
---------------

Firmware update using a prebuilt hex file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PQMON hex file download  <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/eval-pqmon.hex>`__

**Step 1 - MAX32625PICO Firmware Update**

- Download the :adi:`MAX32650FTHR` firmware image from
  :git-max32625pico-firmware-images:`here <master:/>`

  .. figure:: scopy23.jpg

- Follow the procedure indicated
  :git-max32625pico-firmware-images:`here <master:#how-to-update-the-firmware+>`
  to load the new firmware.

**Step 2 - Connect the MAX32625PICO to the AD-PQMON-SL Board**

- Connect the Cortex Debug Cable to the :adi:`MAX32625PICO`
  with the connector key directed towards the outside of the board.

- Connect the programmer to the board as shown in the following picture.

  .. figure:: scopy24.jpg

**Step 3 - Power up the board by connecting the USB type C cable**

.. figure:: scopy25.jpg

**Step 4 - Flashing the firmware to the AD-PQMON-SL**

- If the :adi:`MAX32625PICO` is not connected to the PC USB port, connect it now.
- Once connected, the DAPLINK should appear as a storage device on your PC.

  .. figure:: scopy26.jpg
     :width: 300

- Open the DAPLINK storage device.
- Drag and drop the provided .hex file into the DAPLINK drive.
  The firmware will be written to the target MCU.

Building the Project
~~~~~~~~~~~~~~~~~~~~~

Preliminary requirements
^^^^^^^^^^^^^^^^^^^^^^^^

The licensed software library that works in conjunction with the
:adi:`ADE9430` IC can be obtained from
`here <https://form.analog.com/form_pages/softwaremodules/SRF.aspx>`__.

After obtaining the libraries, the following files need to be added to the
project:

pqlib_dir

.. code-block::

    |  libadi_pqlib_cm4_gcc.a
    └───include
        |   ade9430.h
        |   adi_pqlib_debug.h
        |   adi_pqlib_error.h
        |   adi_pqlib_memory.h
        |   adi_pqlib_profile.h
        |   adi_pqlib_version.h
        |   adi_pqlib.h
        └───config
            └───adi_pqlib_cfg.h

It can be integrated into the project by defining the ``PQLIB_PATH`` to point to
the ``pqlib_dir`` path.

Build and Run
^^^^^^^^^^^^^

The project is based on a :adi:`MAX32650` microcontroller. It can be
built and run by running the following script:

.. code:: bash

   # remove build directory
   make reset
   # select platform
   export PLATFORM=maxim
   # select controller type
   export TARGET=max32650
   # build and flash the code
   make PQLIB_PATH=<path_to_library> run
