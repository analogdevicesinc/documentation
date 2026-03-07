Equipment needed
================

-  AC power supply or connection to mains for the measurement side.
-  Mains or USB type C connector cable for supplying power to the board.
-  PC running Windows or Linux.
-  Cable to build the assembly.
-  USB type C connector cable to connect to the USB port of the PC. (this can be used also to deliver power to the board).
-  :adi:`AD-PQMON-SL <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-pqmon-sl.html>` evaluation board.

*Optional*: :adi:`MAX32625PICO <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max32625pico.html#eb-overview>` for debug and programming.

Testing
=======

For testing the following software is needed:

-  Firmware (link available in the resources section)
-  `Scopy <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/scopy-windows-x86_64-setup-7797088.zip>`_ with the :adi:`AD-PQMON-SL <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-pqmon-sl.html>` addon.

For installing Scopy follow the steps indicated :doc:`here </wiki-migration/university/tools/m2k/scopy>`

After the board connections are made and Scopy is installed, the user can connect to the GUI following the next steps:

-  Connect the USB cable to the PC,
-  Open the previously installed version of scopy.
-  Select the "+" button highlighted in the following image

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy0.jpg
   :align: center
   :width: 600px

-  In the window that opens hit the refresh button highlighted in the following image:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy2.jpg
   :align: center
   :width: 600px

-  Select the COM port that is connected to the PQM board from the drop down menu “PORT NAME” (In the presented case is COM37)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy3.jpg
   :align: center
   :width: 600px

-  After selecting this COM port the URI field is populated.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy4.jpg
   :align: center
   :width: 600px

-  Press the “Verify” button

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy5.jpg
   :align: center
   :width: 600px

-  Select the “PQMPlugin” if not already selected.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy6.jpg
   :align: center
   :width: 600px

-  Press the “ADD DEVICE“ button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy7.jpg
   :align: center
   :width: 600px

-  In the following window press the “Connect” button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy8.jpg
   :align: center
   :width: 600px

-  A message similar with the one highlighted in the following image shows that a successful connection has been made.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy9.jpg
   :align: center
   :width: 600px

Measurements
------------

-  The measurements tabs are available on the left side of the GUI:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy10.jpg
   :align: center
   :width: 600px

Rms tab
~~~~~~~

-  The Rms tab can be activated by clicking on it and afterwards selecting the Run button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy11.jpg
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12.jpg
   :align: center
   :width: 600px

-  The PQEvents indicator warns the user that a PQ event occurred. The events are saved in the log file if logging is active.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12_1.jpg
   :align: center
   :width: 600px

-  If an event occurs during the session the PQEvents indicator will become active. The event can be found in the log file (in the rms tab only the PQ events data is logged into the file). The indicator remains on until the user clicks on it. This will reset the indicator. Even if the indicator is not reset any new event will be registered in the log file.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13_5.jpg
   :align: center
   :width: 600px

-  Logging can be activated only when the measurement is not running. First the LOG button needs to be selected. A log directory needs to be specified after selecting the button highlighted in the following image.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12_2.jpg
   :align: center
   :width: 600px

-  A folder where the data will be saved in csv format needs to be specified. The file is saved with the following name: "nameofactivewindow_date_time.csv" (e.g. rms_01-01-2024_11-00-00).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12_3.jpg
   :align: center
   :width: 600px

-  After the folder is selected, the data will be recorded during a session. The session starts when the running button is activated and ends when it is stopped.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12_4.jpg
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy12_5.jpg
   :align: center
   :width: 600px

-  A snapshot of a rms log file is presented in the following image. As one can see, during the presented session several PQevents occurred.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/rms_tab_events.jpg
   :align: center
   :width: 600px

Harmonics tab
~~~~~~~~~~~~~

-  The Harmonics tab can be activated by clicking on it and afterwards selecting the Run button.
-  To display the harmonics for different waveforms select the line from the table above the graphic.
-  The THD values are shown for each measurement after the THD label.
-  The PQEvents indicator warns the user that an event occurred. The events are saved in the log file if logging is active.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13.jpg
   :align: center
   :width: 600px

-  The user can select between harmonics or inter harmonics.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13_1.jpg
   :align: center
   :width: 600px

-  Logging can be activated only when the measurement is not running. First the LOG button needs to be selected. A log directory needs to be specified after selecting the button highlighted in the following image.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13_2.jpg
   :align: center
   :width: 600px

-  A folder where the data will be saved in csv format needs to be specified. The file is saved with the following name: "nameofactivewindow_date_time.csv" (e.g. harmonics_01-01-2024_11-00-00).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13_3.jpg
   :align: center
   :width: 600px

-  After the folder is selected, the data will be recorded during a session. The session starts when the running button is activated and ends when it is stopped.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy13_4.jpg
   :align: center
   :width: 600px

-  If an event occurs during the session the PQEvents indicator will become active. The event can be found in the log file. The log file in the harmonic tab contains the data regarding the harmonics values and the PQ events intercalated with it at the time that the event occurred. The indicator remains on until the user clicks on it. This will reset the indicator. Even if the indicator is not reset any new PQ event will be registered in the log file.
-  A snapshot of the harmonics log file containing only harmonics data is presented in the following image.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/harmonics_tab_log.jpg
   :align: center
   :width: 600px

-  In the following snapshots PQ events can be observed being intercalated with the harmonics values.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/harmonics_tab_events.jpg
   :align: center
   :width: 600px

Waveforms tab
~~~~~~~~~~~~~

-  The Waveform tab can be activated by clicking on it and afterwards select the Run button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy16.jpg
   :align: center
   :width: 600px

-  The upper side graph is the voltage and the one to the bottom is the current. To zoom in use the mouse to click and drag.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy17.jpg
   :align: center
   :width: 600px

-  The log file can also be activated in the waveforms tab in the same manner explained in the rms or harmonics sections, but in this case the PQ events is not present. If PQ events need to be recorded, then the other two tabs (rms, harmonics) must be used. The data logged in this tab contains only the waveforms values.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy17_1.jpg
   :align: center
   :width: 600px

-   A snapshot of a log file can be seen in the following image.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/waveforms_tab_log.jpg
   :align: center
   :width: 300px

Settings tab
~~~~~~~~~~~~

-  The Settings tab is used to read and set the thresholds and the config values. Activate it by selecting it from the right-side menu.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy18.jpg
   :align: center
   :width: 600px

-  To see all the parameters scroll down

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy18_1.jpg
   :align: center
   :width: 600px

-  To read the values that are currently set click the Read button.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy18_2.jpg
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy18_3.jpg
   :align: center
   :width: 600px

-  To modify a parameter select it, change its value to the desired one and click the Set button.

|

.. note::

   More information about the **Scopy PQMON addon** can be consulted `here <https://analogdevicesinc.github.io/scopy/plugins/pqm/index.html>`_

   | The system comes pre-programmed with a firmware that works with the **Scopy** application, allowing complete system evaluation.
   | **Scopy** will work only with the official :git-no-OS:`firmware releases <projects/eval-pqmon>`


Firmware Update
---------------

Firmware update using a prebuilt hex file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PQMON hex file download <https://swdownloads.analog.com/cse/scopy/ad-pqmon-sl/eval-pqmon.hex>`_

Step 1 - :adi:`max32625pico` firmware update Download the :adi:`MAX32650FTHR` firmware image from :git-max32625pico-firmware-images>`__

.. image:: https://wiki.analog.com/_media/:`here <resources/eval/user-guides/ad-pqmon-sl/scopy23.jpg
   :align: center
   :width: 300px

Follow the procedure indicated `here <https://github.com/analogdevicesinc/max32625pico-firmware-images?tab=readme-ov-file#how-to-update-the-firmware>` to load the new firmware.

Step 2 – Connect the :adi:`max32625pico` to the :adi:`ad-pqmon-sl` board Connect the Cortex Debug Cable to the :adi:`max32625pico` with the connector key directed towards the outside of the board.

Connect the programmer to the board as shown in the following picture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy24.jpg
   :align: center
   :width: 600px

Step 3 - Power up the board by connecting the USB type C cable.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy25.jpg
   :align: center
   :width: 600px

Step 4 - Flashing the firmware to the ad-pqmon-sl

If the :adi:`max32625pico` is not connected to the PC USB port connect it. The DAPLINK should appear as a storage device on the PC.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-pqmon-sl/scopy26.jpg
   :align: center
   :width: 300px

Open the DAPLINK. Drag and drop the provided \*.hex file into DAPLINK. The firmware will be written on the target MCU.

Firmware update building the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preliminary requirements
^^^^^^^^^^^^^^^^^^^^^^^^

The licensed software library that works in conjunction with the :adi:`ADE9430` IC can be obtained from `here <https://form.analog.com/form_pages/softwaremodules/SRF.aspx>`_.

After obtaining the libraries, the following files need to be added to the project:

pqlib_dir

::

   |   libadi_pqlib_cm4_gcc.a
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

It can be integrated into the project by defining the \`PQLIB_PATH\` to point to the \`pqlib_dir\` path.

Build and run
^^^^^^^^^^^^^

The project is based on a :adi:`MAX32650` microcontroller. It can be built and run by running the following script:

.. code:: bash

   # remove build directory
   make reset
   # select platform
   export PLATFORM=maxim
   # select controller type
   export TARGET=max32650
   # build and flash the code
   make PQLIB_PATH=<path_to_library> run

.. tip::

   **If you want to go to the Hardware Page, click here:** `AD-PQMON-SL Hardware User Guide <https://wiki.analog.com/[[/resources/eval/user-guides/ad-pqmon-sl/hardware>`_

