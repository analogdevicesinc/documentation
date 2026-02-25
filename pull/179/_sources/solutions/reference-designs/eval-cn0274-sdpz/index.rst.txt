.. _eval-cn0274-sdpz:

EVAL-CN0274-SDPZ
=================

Ultra-Low Power Standalone Motion Switch

Overview
--------

The :adi:`ADXL362` is a tri-axis, ultra-low power digital accelerometer capable
of detecting motion depending on user defined activity and inactivity
thresholds. Unlike accelerometers that use power duty cycling to achieve low
power consumption, the :adi:`ADXL362` does not alias input signals by
undersampling; it measures continuously at all data rates. By mapping activity
and inactivity detection to the interrupt pins, the user can drive the enable
pin of an :adi:`ADP195`. When activated, this logic controlled switch provides
power to downstream circuitry. All communications to the accelerometer are
performed using a Serial Peripheral Interface (SPI).

Required Equipment
------------------

- :adi:`EVAL-CN0274-SDPZ <EVAL-CN0274-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CS1Z <SDP-S>` evaluation board (SDP-S board)
- CN0274 Evaluation Software (supplied with provided CD in kit)
- Power supply: 2 AAA batteries or +3.0 V supply
- 1 USB Type-A plug to USB Mini-B plug cable

.. figure:: cn0274-setupdiagram.jpg

   EVAL-CN0274-SDPZ system setup diagram

Minimum PC/System Requirements
-------------------------------

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Evaluation Software
------------------------------------

#. Extract the files within the file **CN0274 SDP Eval Software.zip** and open
   the file **setup.exe**. It is recommended that you install the CN0274 SDP
   Evaluation Software to the default directory path
   ``C:\Program Files\Analog Devices\CN0274\`` and all National Instruments
   products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0274-evaluation_software-destination_directory-1.jpg

      CN0274 evaluation software destination directory

#. Press **Next** to proceed through the installation wizard.

   .. figure:: cn0274-evaluation_software-destination_directory-2.jpg

      CN0274 evaluation software installation wizard

#. Press **Next** to start the installation.

   .. figure:: cn0274-evaluation_software-installation_complete.jpg

      CN0274 evaluation software installation complete

#. Press **Next** to complete the evaluation software installation.

#. Upon completion of the installation of the **CN0274 SDP Eval Software**, the
   installer for the **ADI SDP Drivers** will execute. Follow the on-screen
   prompts to install the drivers.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0274-sdpdrivers-setup_wizard.jpg

      ADI SDP Drivers setup wizard

   .. figure:: cn0274-sdpdrivers-destination_directory.jpg

      ADI SDP Drivers destination directory

#. Press **Next** to proceed with the SDP driver installation.

#. It is recommended that you install the drivers to the default directory path
   ``C:\Program Files\Analog Devices\SDP\Drivers\``.

#. Press **Next** to install the drivers and complete the installation of all
   software necessary to evaluate the **EVAL-CN0274-SDPZ**.

Hardware Setup
--------------

#. Place two batteries into the connector on the bottom of the
   :adi:`EVAL-CN0274-SDPZ <EVAL-CN0274-SDPZ>` board. Ensure the batteries are
   size AAA and are the correct polarity.

   .. figure:: cn0274-hardware-batteries.jpg
      :width: 200px

      Battery connector on the bottom of the EVAL-CN0274-SDPZ

   .. figure:: cn0274-hardware-cn0274.jpg
      :width: 200px

      EVAL-CN0274-SDPZ evaluation board

#. Connect the :adi:`EVAL-SDP-CS1Z <SDP-S>` and the
   :adi:`EVAL-CN0274-SDPZ <EVAL-CN0274-SDPZ>` PCBs using the 120-pin male and
   female connectors found on the respective boards.

   .. figure:: cn0274-hardware-notconnected-sdps-cn0274.jpg
      :width: 200px

      EVAL-SDP-CS1Z and EVAL-CN0274-SDPZ before connection

   .. figure:: cn0274-hardware-displaying_connectors.jpg
      :width: 200px

      120-pin connectors on the evaluation boards

   .. figure:: cn0274-hardware-connectorscloseup.jpg
      :width: 200px

      Close-up of the 120-pin connectors

   .. figure:: cn0274-hardware-connected-sdps-cn0274.jpg
      :width: 200px

      EVAL-SDP-CS1Z and EVAL-CN0274-SDPZ connected

#. Plug the mini end of the USB cable into connector **J2** of the
   :adi:`EVAL-SDP-CS1Z <SDP-S>`. Connect the other end of the USB cable into
   the laptop or PC.

   .. figure:: cn0274-hardware-connected-usb-sdps-cn0274.jpg
      :width: 200px

      Complete setup with USB connected

Opening and Enabling the Evaluation Software
----------------------------------------------

#. Launch the executable found at ``C:\Program Files\Analog Devices\CN0274``
   and press the **Connect** button.

   .. figure:: cn0274-evaluation_software-front_panel.jpg

      CN0274 evaluation software front panel

#. After pressing the **Connect** button, a prompt will appear informing the
   user if the accelerometer was properly configured. Press **Ok** and the
   software is ready to use. If the accelerometer is not configured properly,
   disconnect the entire setup and start over.

   .. figure:: cn0274-evaluation_software-accelerometer_configuration_successful.jpg

      Accelerometer configuration successful prompt

Using the Evaluation Software
------------------------------

System Controls
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Control
     - Description
   * - Connect
     - Configures the :adi:`ADXL362` by writing to the necessary registers. A
       prompt will appear informing the user if the accelerometer was properly
       configured.
   * - Disconnect
     - Disconnects the EVAL-CN0274-SDPZ board.

Data Acquisition Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Control
     - Description
   * - Start Sampling
     - Polls the data ready bit in the :adi:`ADXL362` status register. When
       this bit is set, LabVIEW reads the data registers and displays the
       acceleration data for each axis on the chart found in the evaluation
       software.
   * - Stop Sampling
     - Stops LabVIEW from reading and displaying acceleration data.
   * - Save Data
     - Saves all data displayed in the LabVIEW chart. Data will still be saved
       even if the display is disabled.

Accelerometer Controls
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 35

   * - Control
     - Description
   * - Activity Threshold
     - Sets the Activity threshold for all axes of the :adi:`ADXL362`. When
       looking for activity, any single sample that crosses this threshold will
       wake the accelerometer and cause it to begin searching for inactivity.
       This threshold is an absolute value; it is not referenced to acceleration
       reading.
   * - Inactivity Threshold
     - Sets the Inactivity threshold for all axes of the :adi:`ADXL362`. When
       looking for inactivity, a number of samples (defined by the user) must
       cross this threshold in order for the accelerometer to sleep and cause it
       to begin searching for activity. This threshold is referenced to the
       acceleration reading. For example, if the acceleration reads 0g and the
       Inactivity threshold is set for 0.5g, the chart will display one solid
       line (the acceleration reading) and two dotted lines (the acceleration
       reading +/- 0.5g).
   * - Inactivity Time (Samples)
     - Sets the number of acceleration samples for all three axes that must be
       inside the threshold window for the :adi:`ADXL362` to enter the asleep
       state.
   * - Measurement Range (g's)
     - Sets the measurement range of the :adi:`ADXL362` in g's. Choices are
       +/-2g, +/-4g, +/-8g.

Acceleration Data Plots
~~~~~~~~~~~~~~~~~~~~~~~~~

The main display section of the software contains a chart which graphically
displays acceleration data for each axis as well as a numerical display showing
the most recent acceleration conversion for each axis. An LED indicator shows
the current state of the device (Active = Green, Inactive = Red).

- **X-Axis Plot Disabled/Enabled** -- Disables or enables the graphical display
  for the X-axis.
- **Y-Axis Plot Disabled/Enabled** -- Disables or enables the graphical display
  for the Y-axis.
- **Z-Axis Plot Disabled/Enabled** -- Disables or enables the graphical display
  for the Z-axis.

Documents
---------

- :adi:`CN0274 Circuit Note <CN0274>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0274-SDPZ Design & Integration Files
   <https://www.analog.com/cn0274-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADXL362 Product Page <ADXL362>`
- :adi:`ADP195 Product Page <ADP195>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
