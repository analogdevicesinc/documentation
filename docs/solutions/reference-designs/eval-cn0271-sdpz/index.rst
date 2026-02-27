.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0271

.. _eval-cn0271-sdpz:

EVAL-CN0271-SDPZ
=================

Thermocouple Signal Conditioning with Cold Junction Compensation.

Overview
--------

:adi:`CN0271` is a complete thermocouple signal conditioning circuit with cold
junction compensation followed by a 16-bit sigma-delta ADC. The :adi:`AD8495`
thermocouple amplifier provides a simple, low cost solution for measuring K type
thermocouple temperatures, including cold junction compensation.

A fixed gain instrumentation amplifier in the :adi:`AD8495` amplifies the small
thermocouple voltage to provide a 5 mV/°C output. The high common-mode
rejection of the amplifier blocks common-mode noise that the long thermocouple
leads can pick up. For additional protection, the high impedance inputs of the
amplifier make it easy to add extra filtering.

The :adi:`AD8476` differential amplifier provides the correct signal levels and
common-mode voltage to drive the :adi:`AD7790` 16-bit sigma-delta ADC.

The circuit provides a compact, low cost solution for thermocouple signal
conditioning and high resolution analog-to-digital conversion.

.. figure:: cn0271-schematic.png

   CN0271 circuit schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`EVAL-CN0271-SDPZ <CN0271>` evaluation board (CN-0271 board)
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V power supply or equivalent DC power supply
- CN0271 Evaluation Software
- USB Type-A to USB Mini-B cable
- K-type thermocouple millivolt source
- K-type thermocouple male-to-male cable
- PC with the following minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

Hardware Setup
--------------

- The EVAL-CN0271-SDPZ (CN-0271 board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B board) via the 120-pin connector at **J3**.
- The EVAL-CFTL-6V-PWRZ +6 V power supply powers the CN-0271 board via the
  DC barrel jack at **J5** or the screw terminal at **J4**.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B board) connects to the PC via the USB cable.
- The thermocouple connects to the CN-0271 board via the thermocouple connector
  at **J1**.

.. figure:: cn0271-test_setup.png

   CN0271 test setup

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0271 SDP Eval Software.zip** and run **setup.exe**.

   .. note::

      It is recommended that you install the CN0271 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0271\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0271-install1.png

      CN0271 software installation wizard

#. Click **Next** to view the installation review page.

   .. figure:: cn0271-install2.png

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: cn0271-install3.png

      Installation progress

#. Upon completion of the CN0271 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0271-install4.png

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0271-install5.png

      SDP Drivers installation location

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: cn0271-install6.png

      Installation complete

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Control and Indicator Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0271-software.png

   CN0271 Evaluation Software -- Acquire Data tab

.. figure:: cn0271-software2.png

   CN0271 Evaluation Software -- Configure System tab

#. **Connect/Reconnect Button** -- When pressed, the SDP-B board makes a USB
   connection to the CN-0271 board. A connection to the SDP-B board must be
   made to use the software.
#. **Samples Numerical Control** -- Determines how many samples to acquire
   after the Acquire Samples button has been pressed.

   .. note::

      If the Enable Real-Time checkbox is checked, this value is ignored.

#. **Acquire Samples Button** -- When pressed, the SDP-B board collects
   conversion data and presents the acquisitions in the chart.
#. **Stop Acquiring Button** -- When pressed, the software stops collecting
   data from the CN-0271 board.
#. **Save Data Button** -- When pressed, the software saves the data collected
   to a tab-delimited ASCII spreadsheet file.
#. **Control Tabs**

   - *Acquire Data* -- Brings the data collection chart to the front.
   - *Configure System* -- Brings the system configuration settings to the
     front.
   - *SDP Board Information* -- Brings the SDP board revision information to
     the front.

#. **Enable Real-Time Checkbox** -- When checked, the SDP-B board acquires
   samples until the Stop Acquiring button is pressed.
#. **Current Temperature Numerical Indicator** -- Displays the current
   temperature measurement.
#. **Chart Controls** -- Allow the user to zoom-in, zoom-out, and pan through
   the data collected.
#. **System Status String Indicator** -- Displays a message detailing the
   current state of the software.
#. **System Status LED Indicator** -- Displays the current state of the
   software in the form of an LED. There are three status LED colors:

   - |inactive| Inactive
   - |busy| Busy
   - |error| Error

   .. |inactive| image:: cn0272-software-inactive.png
   .. |busy| image:: cn0272-software-busy.png
   .. |error| image:: cn0272-software-error.png
#. **Update Rate Radio Buttons** -- Used to change the output word rate of the
   :adi:`AD7790`. The default value is 120 Hz.
#. **Burnout Current Radio Buttons** -- When enabled, the 100 nA current
   sources in the signal path are activated.

   .. important::

      The burnout currents can be enabled only when the buffer is active.

#. **Buffer Select Radio Buttons** -- Used to set the mode of the
   :adi:`AD7790`. The default value is Unbuffered Mode.

   - *Buffered Mode* -- Turns the on-chip analog input channel buffer of the
     :adi:`AD7790` **ON**.
   - *Unbuffered Mode* -- Turns the on-chip analog input channel buffer of the
     :adi:`AD7790` **OFF**.

#. **Channel Selection Radio Buttons** -- Used to select the analog input
   channel of the :adi:`AD7790` for conversion. The default value is
   AIN(+)-AIN(-).

   - *AIN(+)-AIN(-)* -- Normal operation of the :adi:`AD7790`.
   - *AIN(-)-AIN(-)* -- Shorts the analog input channels of the :adi:`AD7790`.
   - *Vdd Monitor* -- Monitors the voltage applied to the Vdd pin of the
     :adi:`AD7790`. The voltage is attenuated by 5 and the resultant voltage is
     applied to the sigma-delta modulator using an internal 1.17 V reference
     for analog-to-digital conversion.

#. **Mode Register Numerical Indicator** -- Displays the current contents of
   the Mode Register of the :adi:`AD7790`.
#. **Filter Register Numerical Indicator** -- Displays the current contents of
   the Filter Register of the :adi:`AD7790`.
#. **Low Calibration Temperature Numerical Control** -- Used to modify the low
   calibration temperature setpoint. The default value is 20 deg C.
#. **High Calibration Temperature Numerical Control** -- Used to modify the
   high calibration temperature setpoint. The default value is 900 deg C.
#. **Calibrate Button** -- Calibrates the system using the values populated in
   the calibration temperature numerical controls.

Establishing a USB Connection Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.
#. Open the file named **CN0271.exe** in the installation directory.

   .. note::

      If the software was installed to the default location it will be found at
      ``C:\Program Files\Analog Devices\CN0271\CN0271.exe``.

#. Click the **Connect/Reconnect Button**. A window with a progress bar will
   load.

   .. figure:: cn0271-software-wait.png

      USB connection progress bar

#. Upon success, the System Status String Indicator will display
   *SDP Board Ready to Acquire Data*.

Acquiring a Fixed Sample Size of Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Establish a USB connection link.
#. Adjust the **Samples Numerical Control** to the number of samples to be
   acquired.
#. Ensure that the **Enable Real-Time Checkbox** is cleared.
#. Click the **Acquire Samples Button**.
#. Wait until the acquisition is complete.

Acquiring Data in Real-Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Establish a USB connection link.
#. Ensure that the **Enable Real-Time Checkbox** is checked.
#. Click the **Acquire Samples Button**.
#. Click the **Stop Acquiring Button** to stop the acquisition.

Saving Data to a Spreadsheet File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Establish a USB connection link.
#. Capture data.
#. Click the **Save Data Button**.
#. Browse to the directory location where the spreadsheet file is to be saved.
#. Name the file.
#. Click the **OK Button**.

.. note::

   The software saves the spreadsheet file as ASCII text with columns separated
   by tabs.

Documents
---------

- :adi:`CN0271 Circuit Note <CN0271>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0271-SDPZ Design & Integration Files
   <https://www.analog.com/cn0271-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD8495 Product Page <AD8495>`
- :adi:`AD8476 Product Page <AD8476>`
- :adi:`AD7790 Product Page <AD7790>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
