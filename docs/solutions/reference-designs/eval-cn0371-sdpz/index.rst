.. _eval-cn0371-sdpz:

EVAL-CN0371-SDPZ
=================

Complete LVDT Signal Conditioning Circuit.

Overview
--------

:adi:`CN0371` is a complete linear variable differential transformer (LVDT)
signal conditioning circuit that can accurately measure linear position or
linear displacement from a mechanical reference. Synchronous demodulation in
the analog domain is used to extract the position information and provides
immunity to external noise. A 24-bit sigma-delta ADC digitizes the position
output for high accuracy.

LVDTs utilize electromagnetic coupling between the movable core and the coil
assembly. This contactless (and therefore frictionless) operation is a primary
reason why they are widely used in aerospace, process controls, robotics,
nuclear, chemical plants, hydraulics, power turbines, and other applications
where operating environments can be hostile and long life and high reliability
are required.

The entire circuit, including the LVDT excitation signal, consumes only 10 mW
of power. The circuit excitation frequency and output data rates are SPI
programmable. The system has a programmable bandwidth versus dynamic range
trade-off. It supports bandwidths of over 1 kHz, and at a bandwidth of 20 Hz,
the circuit has a dynamic range of 100 dB, making it ideal for precision
industrial position and gauging applications.

.. figure:: cn0371-simplified_schematic.png
   :align: center

   CN0371 Simplified Schematic

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`EVAL-CN0371-SDPZ <CN0371>` evaluation board (CN-0371 board)
- EVAL-CFTL-LVDT linear variable differential transformer (Measurement
  Specialties E-100 Economy Series LVDT)
- CN-0371 Evaluation Software
- EVAL-CFTL-6V-PWRZ (+6 V DC power supply)
- USB Type-A to USB Mini-B cable
- PC with the following minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB Type-A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

Hardware Setup
--------------

General Setup
~~~~~~~~~~~~~

- The :adi:`EVAL-CN0371-SDPZ <CN0371>` (CN-0371 board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B board) via the 120-pin connector.
- The EVAL-CFTL-6V-PWRZ (+6 V DC power supply) powers the EVAL-CN0371-SDPZ
  via the DC barrel jack.
- The EVAL-CFTL-LVDT (LVDT) connects to the EVAL-CN0371-SDPZ via the 6-pin
  header at **J3**.

.. figure:: cn0371-test_setup.png
   :align: center

   CN0371 Test Setup

Connecting the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the EVAL-CFTL-LVDT (LVDT) to **J3** of the EVAL-CN0371-SDPZ
   (CN-0371 board) as depicted in the wiring diagram below.

   .. note::

      If a different LVDT is used other than the E-100 LVDT from Measurement
      Specialties, Inc., the wiring schematic will be different.

   .. figure:: cn0371-wiring_schematic.png
      :align: center

      LVDT Wiring Schematic for J3

#. Connect **P3** of the EVAL-CN0371-SDPZ (CN-0371 board) to **CON A** of the
   :adi:`EVAL-SDP-CB1Z` (SDP-B board).
#. Connect the USB cable to **J1** of the :adi:`EVAL-SDP-CB1Z` (SDP-B board).

.. figure:: cn0371-hardware1.jpg
   :align: center

   CN0371 Hardware Connection

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0371 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN-0371 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0371\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.
#. Click **Next** to start the installation.
#. Upon completion of the installation of the CN-0371 Evaluation Software, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linearity and Calibration Tabs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0371-software1.png
   :align: center

   Linearity and Calibration Tabs

#. **Displacement Display** -- The upper left hand corner shows the current
   measurement displacement in terms of voltage (V) and distance in
   millimeters (mm). In order to get accurate measurements, the system should
   be calibrated as described below.

#. **Calibration Tab** -- The system can be calibrated using a two-point
   calibration:

   - Place the core at the maximum displacement. Enter the displacement in the
     Distance field, then click **Set new MAX**.
   - Place the core at the minimum displacement. Enter the displacement in the
     Distance field, then click **Set new MIN**.
   - This completes the calibration.

#. **Linearity Table** -- The table can be filled out and linearity
   automatically calculated as follows:

   - Set the core to a known position. Enter that position in the Distance (MM)
     field. Click **Get new data point**. This creates a new entry in the
     Linearity table. The linearity is calculated and the data point is added to
     the Linearity plot.
   - Additional data points can be added in a similar manner. The data points
     do not need to be linearly spaced or taken in a particular order.

#. **Error Calculation** -- The linearity error is calculated based on the
   distance from an ideal straight line between the two calibration points
   taken.

Live Measurement and Noise Data Tabs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0371-software2.png
   :align: center

   Live Measurement and Noise Data Tabs

#. **Live Measurement Chart** -- The live measurement chart shows the last
   200 ADC readings taken. The data shown is displayed in volts (left side
   vertical axis) and millimeters (right side vertical axis) based on the most
   recent calibration.

#. **Noise Data Tab** -- Noise data in volts (RMS), volts (p-p), ENOBs (RMS)
   and ENOBs (p-p) are displayed. The volts are calculated based on the 3.3 V
   ADC reference. ENOB measurements are based on full-scale voltage in the
   Settings tab.

Live Measurement and Settings Tabs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0371-software3.png
   :align: center

   Live Measurement and Settings Tabs

#. **Settings Tab**

   - **Full-Scale Range** -- Enables users to scale the voltage used for the
     ENOBs calculations in the Noise Data tab.
   - **Measure I/Q** -- Allows selecting either the Phase 0 or Phase 90
     setting on the :adi:`ADA2200`.
   - **Data Rate Divider** -- Sets the :adi:`AD7192` output data rate. This
     value can be set from 1 to 1023.
   - **Output Data Rate** -- The calculated ADC data rate. It is equal to
     4800 / (Data Rate Divider).

Documents
---------

- :adi:`CN0371 Circuit Note <CN0371>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0371-SDPZ Design & Integration Files
   <https://www.analog.com/cn0371-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`ADA2200 Product Page <ADA2200>`
- :adi:`AD7192 Product Page <AD7192>`
- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
