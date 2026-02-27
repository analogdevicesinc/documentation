.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0272

.. _eval-cn0272-sdpz:

EVAL-CN0272-SDPZ
=================

High-Speed Photodiode Signal Conditioning with Dark Current Compensation.

Overview
--------

:adi:`CN0272` is a high-speed photodiode signal conditioning circuit with dark
current compensation. The system converts current from a high-speed silicon
PIN photodiode and drives the inputs of a 20 MSPS ADC. This combination of
parts offers spectral sensitivity from 400 nm to 1050 nm with 49 nA of
photocurrent sensitivity, a dynamic range of 91 dB, and 2 MHz of bandwidth.
The signal conditioning circuitry consumes only 40 mA of current from the
+/-5 V supplies, making this configuration suitable for portable high-speed,
high-resolution light intensity applications such as pulse oximetry.

Other suitable applications for this circuit include analog opto-isolators and
applications that require larger bandwidth and less resolution such as adaptive
speed control systems.

.. figure:: cn0272-simplified_schematic.png
   :width: 800 px
   :align: center

   CN0272 Simplified Schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` evaluation board **(SDP-B Board)**
- :adi:`EVAL-CN0272-SDPZ <EVAL-CN0272-SDPZ>` daughter board **(CN0272 Board)**
- :adi:`EVAL-CFTL-6V-PWRZ` power supply or equivalent +6 V power supply
- CN0272 SDP evaluation software (supplied with provided CD in kit)
- PC with minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

- USB Type-A to USB Mini-B cable
- Light source between 400 nm to 1050 nm (not included in kit)
- SMB connector (optional -- needed if an external voltage bias for the
  photodiode is to be used)

General Setup
-------------

- The :adi:`EVAL-CN0272-SDPZ <EVAL-CN0272-SDPZ>` Board connects to the
  :adi:`EVAL-SDP-CB1Z` SDP-B Board via the 120-pin connector.
- The :adi:`EVAL-CFTL-6V-PWRZ` DC power supply powers the CN0272 Board via
  the DC barrel jack.
- The SDP-B Board connects to the PC via the USB cable.

.. figure:: cn0272-test_setup.png
   :width: 700 px
   :align: center

   CN0272 General Test Setup

Software Installation
---------------------

#. Extract **CN0272 SDP Eval Software.zip** and run **setup.exe**.

   .. note::

      It is recommended to install the CN0272 SDP evaluation software to the
      default directory path ``C:\Program Files\Analog Devices\CN0272\`` and
      all National Instruments products to
      ``C:\Program Files\National Instruments\``.

   .. figure:: cn0272-install1.png
      :width: 500 px
      :align: center

      CN0272 Software Installer

#. Click **Next** to view the installation review page.

   .. figure:: cn0272-install2.png
      :width: 500 px
      :align: center

      Installation Review Page

#. Click **Next** to start the installation.

   .. figure:: cn0272-install3.png
      :width: 500 px
      :align: center

      Installation in Progress

#. Upon completion of the CN0272 SDP Eval Software installation, the installer
   for the **ADI SDP Drivers** will execute.

   .. note::

      Close all other applications before clicking **Next** to allow updating
      relevant system files without rebooting.

   .. figure:: cn0272-install4.png
      :width: 500 px
      :align: center

      ADI SDP Drivers Installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended to install the drivers to the default directory path
      ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0272-install5.png
      :width: 500 px
      :align: center

      SDP Drivers Installation Location

#. Press **Next** to install the SDP Drivers and complete the installation.
   Click **Finish** when done.

   .. figure:: cn0272-install6.png
      :width: 500 px
      :align: center

      SDP Drivers Installation Complete

Connecting the Hardware
-----------------------

#. Connect **J4** of the :adi:`EVAL-CN0272-SDPZ <EVAL-CN0272-SDPZ>` (CN0272
   Board) to **CON A** of the :adi:`EVAL-SDP-CB1Z` (SDP-B Board).

   .. figure:: cn0272-hardware.png
      :width: 600 px
      :align: center

      CN0272 Board Connected to SDP-B Board

#. Select the voltage bias of the photodiode:

   a. **Onboard -5 V bias**: Populate **JP1** with a shorting jumper in the
      default position.

      .. figure:: cn0272-hardware2.png
         :width: 600 px
         :align: center

         JP1 Configuration for Onboard -5 V Bias

   b. **External voltage bias**: Populate **JP1** with a shorting jumper in
      the alternate position.

      .. warning::

         When using an external voltage to bias the photodiode, a SMB
         connector must also be connected to **J2**. The other end of this
         cable must connect to a voltage supply of 15 V or less.

      .. figure:: cn0272-hardware3.png
         :width: 600 px
         :align: center

         JP1 Configuration for External Voltage Bias

#. Connect a +6 V supply to the barrel jack or the screw terminal on the
   CN0272 Board.

   .. figure:: cn0272-hardware4.png
      :width: 600 px
      :align: center

      Power Supply Connection

#. Connect the USB cable to the SDP-B Board and the PC.

   .. figure:: cn0272-hardware5.png
      :width: 600 px
      :align: center

      USB Cable Connection

Using the Evaluation Software
------------------------------

Software Controls and Indicators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0272-software.png
   :width: 800 px
   :align: center

   CN0272 Evaluation Software Front Panel

#. **SDP Connector Dropdown Menu** -- Selects which connector on the SDP-B
   Board the CN0272 Board is connected to (connectorA or connectorB). Must be
   selected before clicking the Connect to SDP-B Board button.
#. **Connect to SDP-B Board Button** -- Establishes the USB connection between
   the SDP-B Board and the CN0272 Board. A connection must be made before
   using the software.
#. **Take Snapshot(s) Button** -- Collects a single snapshot or multiple
   snapshots depending on the acquisition mode setting.

   .. note::

      A **Snapshot** is a collection of analog-to-digital conversions, sampled
      at 20 MSPS, acquired by the SDP-B Board and displayed in the graph.

#. **Save Snapshot(s) Button** -- Saves a single snapshot or a collection of
   snapshots to a tab-delimited ASCII spreadsheet file.
#. **Acquisition Mode Radio Buttons**:

   - *Single Snapshot* -- Collects a single snapshot of data.
   - *Multiple Snapshots* -- Collects multiple snapshots of data.

#. **Conversions in Snapshot Numerical Control** -- Determines the number of
   conversions in a single snapshot (range: 1 to 65,536).
#. **Snapshots to Take Numerical Control** -- Determines the number of
   snapshots to collect (range: 1 to 65,536). Only enabled in Multiple
   Snapshots mode.
#. **Snapshot Delay (ms) Numerical Control** -- Determines the delay in
   milliseconds between snapshots (range: 1 to 65,536). Only enabled in
   Multiple Snapshots mode.
#. **Control Tabs**:

   - *Photocurrent Results* -- Displays the Photocurrent Results graph.
   - *Histogram Results* -- Displays the Histogram Results graph.
   - *Configure* -- Displays the System Settings.

#. **Graph Controls** -- Allow zooming in, zooming out, and panning through
   the displayed snapshot.
#. **Graph Units Radio Buttons** -- Determines the Y-axis units of the
   snapshot displayed in the graph.
#. **Snapshot Displayed Numerical Control/Indicator** -- Determines the
   current snapshot displayed in the graph. Also acts as an indicator during
   multiple snapshot acquisition. Only enabled in Multiple Snapshots mode.
#. **System Status String Indicator** -- Displays a message detailing the
   current state of the software.
#. **System Status LED Indicator** -- Displays the current software state as
   a colored LED:

   - |inactive| Inactive
   - |busy| Busy
   - |powerdown| ADC in Power-Down
   - |error| Error

   .. |inactive| image:: cn0272-software-inactive.png
   .. |busy| image:: cn0272-software-busy.png
   .. |powerdown| image:: cn0272-software-powerdown.png
   .. |error| image:: cn0272-software-error.png

Establishing a USB Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install the software and connect the hardware as described above.
#. Open **CN0272.exe** from the installation directory.

   .. note::

      Default installation location:
      ``C:\Program Files\Analog Devices\CN0272\CN0272.exe``

#. Select the connector from the **SDP Connector Dropdown Menu**.
#. Click the **Connect to SDP-B Board Button**. A progress bar window will
   load.

   .. figure:: cn0272-software-wait.png
      :align: center

      USB Connection Progress Bar

#. Upon success, the System Status String Indicator displays
   *SDP-B Ready to Take Snapshot(s)*.

Capturing a Single Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Select *Single Snapshot* as the acquisition mode.
#. Set the number of conversions in the snapshot.
#. Click the **Take Snapshot(s)** button.

Capturing Multiple Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Select *Multiple Snapshots* as the acquisition mode.
#. Set the number of conversions in each snapshot.
#. Set the number of snapshots to take.
#. Set the snapshot delay.
#. Click the **Take Snapshot(s)** button.

Displaying a Specific Snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Select *Multiple Snapshots* as the acquisition mode.
#. Set the number of conversions in each snapshot.
#. Set the number of snapshots to take.
#. Set the snapshot delay.
#. Click the **Take Snapshot(s)** button.
#. Type the number of the desired snapshot into the **Snapshot Displayed
   Numerical Control**.

Saving a Single Snapshot to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Capture a single snapshot.
#. Click the **Save Snapshot(s)** button.
#. Select either **Microamps (uA)** or **ADC Codes**.

   .. figure:: cn0272-software-save_units.png
      :align: center

      Save Units Selection Dialog

#. Click **OK**.
#. Browse to the save location, name the file, and click **OK**.

.. note::

   The software saves the spreadsheet file as ASCII text with tab-separated
   columns.

Saving Multiple Snapshots to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB connection.
#. Capture multiple snapshots.
#. Click the **Save Snapshot(s)** button.
#. Select either **All Snapshots** or **Range of Snapshot(s)**.

   - If *Range of Snapshot(s)* is selected, input the subset of snapshots to
     save.

#. Select either **Microamps (uA)** or **ADC Codes**.

   .. figure:: cn0272-software-save_full.png
      :align: center

      Save Multiple Snapshots Dialog

#. Click **OK**.
#. Browse to the save location, name the file, and click **OK**.

.. note::

   The software saves the spreadsheet file as ASCII text with tab-separated
   columns.

Documents
---------

- :adi:`CN0272 Circuit Note <CN0272>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0272-SDPZ Design & Integration Files
   <https://www.analog.com/cn0272-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
