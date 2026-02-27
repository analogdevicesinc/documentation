.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0189

.. _eval-cn0189-sdpz:

EVAL-CN0189-SDPZ
=================

Tilt Measurement Using a Dual-Axis Accelerometer.

Overview
--------

The :adi:`ADXL203` is a polysilicon surface-micromachined sensor and signal
conditioning circuit. Acceleration in the X or Y axis produces a corresponding
output voltage on the XOUT or YOUT output pins of the device. The X axis and
Y axis are perpendicular to one another.

The :adi:`AD8608` quad op amp buffers, attenuates, and level shifts the
:adi:`ADXL203` outputs so they are at the proper levels to drive the inputs of
the :adi:`AD7887`. The :adi:`AD7887` is configurable for either dual or single
channel operation via the on-chip control register. In this application it is
configured for dual channel mode, allowing the user to monitor both outputs of
the :adi:`ADXL203`, providing a more accurate and complete tilt measurement
solution.

Required Equipment
------------------

- :adi:`EVAL-CN0189-SDPZ <EVAL-CN0189-SDPZ>` evaluation board
- One SDP controller board:

  - :adi:`EVAL-SDP-CS1Z <SDP-S>` (SDP-S board), or
  - :adi:`EVAL-SDP-CB1Z` (SDP-B board)

- CN0189 evaluation software
- :adi:`EVAL-CFTL-6V-PWRZ <EVAL-CFTL-6V-PWRZ>` (+6 V power supply) or
  equivalent
- USB Type-A plug to USB Mini-B plug cable

Minimum PC/System Requirements
-------------------------------

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

How to Install the Evaluation Software
---------------------------------------

#. Extract the files within the file **CN0189 SDP Eval Software.zip** and open
   the file **setup.exe**. It is recommended that you install the CN0189 SDP
   Evaluation Software to the default directory path
   ``C:\Program Files\Analog Devices\CN0189\`` and all National Instruments
   products to ``C:\Program Files\National Instruments\``.
#. Press **Next**.
#. Press **Next**.
#. Upon completion of the installation of the **CN0189 SDP Eval Software**, the
   installer for the **ADI SDP Drivers** will execute. Follow the on-screen
   prompts to install the drivers. It is recommended that you close all other
   applications before clicking **Next**. This will make it possible to update
   relevant system files without having to reboot your computer.
#. Press **Next**.
#. It is recommended that you install the drivers to the default directory path
   ``C:\Program Files\Analog Devices\SDP\Drivers\``.
#. Press **Next** to install the drivers and complete the installation of all
   software necessary to evaluate the EVAL-CN0189-SDPZ.

Hardware Setup
--------------

#. Connect the :adi:`EVAL-SDP-CS1Z <SDP-S>` (or :adi:`EVAL-SDP-CB1Z`) and the
   :adi:`EVAL-CN0189-SDPZ <EVAL-CN0189-SDPZ>` PCBs using the 120-pin male and
   female connectors found on the respective boards.

   .. figure:: cn0189-hardware-displaying_connectors.jpg

      EVAL-CN0189-SDPZ and SDP board connectors

   .. figure:: cn0189-hardware-connected-sdps-cn0189.jpg

      EVAL-CN0189-SDPZ connected to SDP board

#. Plug in the DC barrel jack to connector **J3** of the EVAL-CN0189-SDPZ and
   the mini end of the USB cable into connector **J2** of the SDP board.
   Connect the other end of the USB cable to the PC.

   .. figure:: CN0189-Hardware-Connected-SDPS-Power-CN0189.jpg

      Power supply connected to EVAL-CN0189-SDPZ

   .. figure:: cn0189-hardware-connected-usb-sdps-cn0189.jpg

      USB cable connected to SDP board

Software Setup
--------------

Opening and Enabling the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Launch the executable found at
   ``C:\Program Files\Analog Devices\CN0189`` and press the **Connect**
   button.

Software Controls
~~~~~~~~~~~~~~~~~~

The following is a list of all available software controls, grouped according
to their location in the software:

**System Controls**

- **Connect** -- Configures the :adi:`AD7887` by writing to the necessary
  registers.
- **Disconnect** -- Disconnects the EVAL-CN0189-SDPZ board.
- **Connector A** -- Allows the user to select which connector of the SDP
  board is being utilized.

**Conversion Mode Controls**

*Continuous Conversion Mode*

- This control brings the user to the Demonstration tab and locks out
  unnecessary tabs.
- **Click to Begin Continuous Sampling** -- Starts the demonstration mode
  which measures the angle the PCB makes with the gravity vector and displays
  it.

*Single Sample Mode*

- This control brings the user to the Sample Data tab and locks out
  unnecessary tabs.
- **Input Angle** -- Having set the PCB at a specific angle, this control
  allows the user to input that angle and compare the ADC result with the
  actual angle.
- **Single Sample** -- Instructs the ADC to sample and convert one
  acceleration reading from each axis.
- **Clear Data** -- Clears the X-Y plot.
- **Remove Data Point** -- Removes the last data point from the X-Y plot.
- **Save Data** -- Prompts and allows the user to save their data to a text
  file.

Calibration Procedure
~~~~~~~~~~~~~~~~~~~~~~

#. Select **Single Sample** in the **Conversion Mode Controls**. Calibration
   can only be performed in the Single Sample mode.
#. Navigate to the **Calibrate** tab.
#. To manually enter or change calibration coefficients, press the **Manual
   Coefficient Input** button and enter the appropriate offset and sensitivity
   values for each axis (in g's).
#. To perform a four-point calibration, press the **Four Point Calibration**
   button:

   a. Orient the PCB so the X-axis is pointing up. Press **Sample Data** while
      rotating the PCB to find the largest output voltage for the X-axis. This
      voltage corresponds to the +1g value for the X-axis.
   b. Orient the PCB so the X-axis is pointing down. Press **Sample Data**
      while rotating the PCB to find the smallest output voltage for the
      X-axis. This voltage corresponds to the -1g value for the X-axis.
   c. Orient the PCB so the Y-axis is pointing up. Press **Sample Data** while
      rotating the PCB to find the largest output voltage for the Y-axis. This
      voltage corresponds to the +1g value for the Y-axis.
   d. Orient the PCB so the Y-axis is pointing down. Press **Sample Data**
      while rotating the PCB to find the smallest output voltage for the
      Y-axis. This voltage corresponds to the -1g value for the Y-axis.
   e. Press **Calibrate** to calculate the offset and sensitivity values for
      each axis.
   f. Any further calculations or conversions performed anywhere in the
      software (Demonstration tab or Sampled Data tab) will utilize the offset
      and sensitivity values calculated here.

Documents
---------

- :adi:`CN0189 Circuit Note <CN0189>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0189-SDPZ Design & Integration Files
   <https://www.analog.com/cn0189-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADXL203 Product Page <ADXL203>`
- :adi:`AD8608 Product Page <AD8608>`
- :adi:`AD7887 Product Page <AD7887>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
