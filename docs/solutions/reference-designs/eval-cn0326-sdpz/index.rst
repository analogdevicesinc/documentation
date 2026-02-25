.. _eval-cn0326-sdpz:

EVAL-CN0326-PMDZ
=================

Isolated Low Power pH Sensor Signal Conditioner and Digitizer.

.. toctree::
   :hidden:

   ADICUP360/ADICUP3029 Demo <software>

Overview
--------

:adi:`CN0326` is a completely isolated low power pH sensor signal conditioner
and digitizer with automatic temperature compensation for high accuracy. The
circuit gives 0.5% accurate pH readings for pH values from 0 to 14 with greater
than 14 bits of noise-free code resolution and is suitable for a variety of
industrial applications such as chemical, food processing, water, and waste
water analysis.

This circuit supports a wide variety of pH sensors that have very high internal
resistance that can range from 1 MOhm to several GOhm. Digital signal and power
isolation provides immunity to noise and transient voltages often encountered
in harsh industrial environments.

The circuit consists of a pH probe buffer, a Pt1000 RTD for temperature
compensation, and a 24-bit ADC (:adi:`AD7793`) with 3 differential analog
inputs.

The pH probe consists of a glass measuring electrode and a reference electrode.
When the probe is placed in a solution, the measuring electrode generates a
voltage depending on the hydrogen activity of the solution, which is compared to
the potential of the reference electrode. As the solution becomes more acidic
(pH < 7) the potential of the glass electrode becomes more positive (+mV) in
comparison to the reference electrode; and as the solution becomes more alkaline
(pH > 7) the potential of the glass electrode becomes more negative (-mV) in
comparison to the reference electrode.

The ADC analog differential channels are:

- **AIN1(+)/AIN1(-)** -- pH probe (voltage full range: +/-414 mV at 25 deg C
  to +/-490 mV at 80 deg C)
- **AIN2(+)/AIN2(-)** -- Pt1000 RTD (voltage full range: 210 mV to 290 mV
  with 210 uA excitation current)
- **AIN3(+)/AIN3(-)** -- Bias current (used to minimize voltage errors)

PMOD Interface
~~~~~~~~~~~~~~~

The EVAL-CN0326-PMDZ uses the extended SPI PMOD interface. The 3.3 V power for
the PMOD comes directly from the host board it is connected to.

.. list-table:: P1 Pin Assignments
   :header-rows: 1

   * - Pin Number
     - Pin Function
     - Mnemonic
   * - Pin 1
     - Chip Select
     - CS_N
   * - Pin 2
     - Master Out Slave In
     - DIN
   * - Pin 3
     - Master In Slave Out
     - DOUT
   * - Pin 4
     - Serial Clock
     - SCLK
   * - Pin 5
     - Digital Ground
     - DGND
   * - Pin 6
     - Digital Power
     - VDD
   * - Pin 7
     - Not Connected
     - NC
   * - Pin 8
     - Not Connected
     - NC
   * - Pin 9
     - RCout
     - RCOUT
   * - Pin 10
     - Not Connected
     - NC

Required Equipment
------------------

**Hardware**

- :adi:`EVAL-CN0326-PMDZ` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`SDP-PMD-IB1Z` interposer board
- EVAL-CFTL-6V-PWRZ +6 V DC power supply
- USB Type-A to USB Mini-B cable
- pH probe with BNC connector
- RTD sensor with RCA connector

**Software**

- `CN0326 Evaluation Software
  <https://swdownloads.analog.com/cse/cftl/CN0326/2.0.0/CN0326_Evaluation_Software.zip>`__
  (also supplied on CD)

**Minimum PC Requirements**

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM, 2 GB available disk space
- .NET Framework 3.5

Hardware Setup
--------------

.. figure:: cn0326fig11.jpg
   :align: center

   EVAL-CN0326-PMDZ hardware connection setup

#. Plug the mini end of the USB cable into connector **J1** of the
   :adi:`EVAL-SDP-CB1Z` and connect the other end to the PC. Verify that
   *ADI Development Tools* appears in Device Manager.

   .. figure:: device_manager.png
      :align: center
      :width: 500px

      ADI Development Tools in Device Manager

#. Remove the jumper across **JP1** on the :adi:`SDP-PMD-IB1Z`.
#. Connect the 120-pin connector of the :adi:`SDP-PMD-IB1Z` to the connector
   marked **CON A** on the :adi:`EVAL-SDP-CB1Z`. Secure with nylon hardware
   using the holes provided at the ends of the 120-pin connectors.
#. Connect the EVAL-CFTL-6V-PWRZ to **J1** barrel jack of the
   :adi:`SDP-PMD-IB1Z`, and **wait 10 seconds** before continuing.
#. Connect the 12-pin right-angle male pin header of the :adi:`EVAL-CN0326-PMDZ`
   to the 12-pin right-angle female pin header of the :adi:`SDP-PMD-IB1Z`.
#. Connect the pH probe to **J1** on the :adi:`EVAL-CN0326-PMDZ`.
#. Connect the RTD sensor to **P1** on the :adi:`EVAL-CN0326-PMDZ`.
#. Place the jumper across **JP1** on the :adi:`SDP-PMD-IB1Z`, positioned to
   +3.3 V.
#. Verify *ADI Development Tools* still appears in Device Manager. If not,
   repeat from step 1.

   .. figure:: device_manager.png
      :align: center
      :width: 500px

      ADI Development Tools in Device Manager

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0326 Eval Software.zip** and run **setup.exe**.

   .. note::

      It is recommended that you install the CN0326 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0326\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: fig1.jpg
      :align: center

      CN0326 Evaluation Software setup wizard

#. Click **Next** to view the installation review page.

   .. figure:: fig2.jpg
      :align: center

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: fig3.jpg
      :align: center

      Installation progress

#. Upon completion of the CN0326 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: fig4.jpg
      :align: center

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: fig5.jpg
      :align: center

      SDP Drivers installation location

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: fig7.jpg
      :align: center

      SDP Drivers installation complete

Opening and Enabling the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: fig9.jpg
   :align: center

   CN0326 Evaluation Software main window

#. Launch the executable found at ``C:\Program Files\Analog Devices\CN0326``
   and press the **Connect** button.
#. After pressing the **Connect** button, a prompt will appear informing the
   user that the SDP is now ready to acquire data and the remaining controls in
   System Controls will be enabled.
#. Press the **Run** button to start using the program.

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: circuit_note_fig_9.jpg
   :align: center

   CN0326 Evaluation Software GUI overview

The following are the available software controls grouped by their location in
the software GUI:

**System Controls**

- **Connect** -- Configures the :adi:`AD7793` by writing to the necessary
  registers. A prompt will appear informing the user if the ADC was properly
  configured.
- **Run** -- Polls the data ready bit in the :adi:`AD7793` status register.
  When this bit is set, LabVIEW reads the data registers and displays the pH
  reading and the temperature data on the chart.
- **Save Data** -- Saves all data displayed in the LabVIEW chart.
- **Clear Data** -- Clears all data displayed in the LabVIEW chart.

**Data Graph** -- Waveform chart visually displaying the pH readings and the
temperature readings taken after clicking the Run button.

**Calibration Settings** -- Two-point linear interpolation calibration:

- **Voltage Offset Calibration** -- Removes the offset introduced by the pH
  probe and by the system after clicking the Remove Offset Voltage button.
- **Buffer Solution 1** -- Option to choose the source of the temperature
  coefficient table for buffer solution 1, either NIST Standard or a custom
  table. Sets the first point for calibration after clicking Calibration
  Point 1.
- **Buffer Solution 2** -- Option to choose the source of the temperature
  coefficient table for buffer solution 2, either NIST Standard or a custom
  table. Sets the second point for calibration after clicking Calibration
  Point 2.

**Measured Results** -- Displays the pH reading, the corresponding voltage, and
the slope (mV/pH).

**Continuous Temperature Compensation** -- Enable or disable continuous
temperature compensation for pH reading.

**Data Rate** -- Modify the data acquisition rate (applies instantly by clicking
the Refresh Rate button).

**RTD Value** -- Allows use of other RTD values according to requirements.

**Save/Recall Calibration Settings** -- Save the current calibration setup to a
text file or recall a previously saved calibration setup.

.. note::

   An example of a format for the calibration setup can be found in the Design
   Support Package in the folder named *Calibration Text Format*.

Calibration
~~~~~~~~~~~~

.. note::

   A minimum of two buffer solutions of different pH values must be selected.
   One of these buffer solutions should be pH 7 for zero-point compensation.
   The second buffer solution should have a pH value near the anticipated
   measuring range. The third buffer solution will be needed if the expected
   measuring range covers both the acidity and alkalinity range, where the pH
   value of the second and third buffer solutions should fall under the acid
   region and alkaline region respectively. The chosen buffer solutions should
   differ by at least 2 pH units. Allow the pH probe to stabilize in the buffer
   solution before taking readings.

#. **Step 1** -- Immerse the pH probe and temperature sensor into a pH 7 buffer
   solution for zero-point compensation. Click **Remove Offset Voltage** once
   the pH voltage reading becomes stable.
#. **Step 2** -- Rinse the electrode assembly with deionized water and immerse
   the pH probe with the temperature sensor into the second chosen buffer
   solution. Select the source of the buffer solution temperature coefficient
   table (NIST Standard or custom). Click **Calibration Point 1** to set the
   second point of calibration.
#. **Step 3** -- Rinse the electrode assembly with deionized water and immerse
   the pH probe with the temperature sensor into the third chosen buffer
   solution. Select the source of the buffer solution temperature coefficient
   table (NIST Standard or custom). Click **Calibration Point 2** to set the
   third point of calibration.

Documents
---------

- :adi:`CN0326 Circuit Note <CN0326>`
- `AD7793 Data Sheet
  <https://www.analog.com/media/en/technical-documentation/data-sheets/AD7793.pdf>`__

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0326-PMDZ Design & Integration Files
   <https://www.analog.com/cn0326-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7793 Product Page <AD7793>`
- :adi:`EVAL-SDP-CB1Z Product Page <EVAL-SDP-CB1Z>`
- :adi:`SDP-PMD-IB1Z Product Page <SDP-PMD-IB1Z>`
- :doc:`ADICUP360/ADICUP3029 Demo <software>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
