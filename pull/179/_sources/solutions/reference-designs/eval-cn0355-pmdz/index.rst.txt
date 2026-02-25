.. _eval-cn0355-pmdz:

EVAL-CN0355-PMDZ
=================

Low Power Bridge Sensor Signal Conditioner with Temperature Compensation.

Overview
--------

:adi:`CN0355 <CN0355>` is a complete low power signal conditioner for a
bridge-type sensor and includes a temperature compensation channel. It is ideal
for a variety of industrial pressure sensors and load cells that operate with
drive voltages between 5 V and 15 V.

The circuit can process full-scale signals from approximately 10 mV to 1 V
using the internal PGA of the 24-bit sigma-delta ADC, making it suitable for a
wide variety of pressure sensors.

The entire circuit uses only three ICs and requires only 1 mA (excluding the
bridge current). A ratiometric technique ensures that the accuracy and
stability of the system does not depend on a voltage reference.

Required Equipment
------------------

- :adi:`EVAL-CN0355-PMDZ <EVAL-CN0355-PMDZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- :adi:`SDP-PMD-IB1Z <SDP-PMD-IB1Z>` interposer board
- CN0355 evaluation software (supplied on CD in kit)
- +6 V DC power supply
- USB Type-A to USB Mini-B cable
- Pressure transducer (e.g., Honeywell NSCSANN600MGUNV)
- 2/3/4-wire RTD sensor

  .. note::

     An RTD sensor can be bypassed by shorting the P9 connector on the
     EVAL-CN0355-PMDZ evaluation board.

Minimum PC/System Requirements
-------------------------------

- Windows XP SP2, Windows Vista, or Windows 7
  Business/Enterprise/Ultimate editions
- Intel Pentium processor (x86 compatible), 1 GHz or faster
- 512 MB RAM and 2 GB available hard disk space
- .NET 3.5 Framework

Installing the Evaluation Software
------------------------------------

1. Extract the file **CN0355 Eval Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0355 evaluation software to the
      default directory path
      **C:\\Program Files\\Analog Devices\\CN0355\\** and all National
      Instruments products to **C:\\Program Files\\National Instruments\\**.

   .. figure:: cn0355_image1.png
      :align: center

      CN0355 software installer

2. Click **Next** to view the installation review page.

3. Click **Next** to start the installation.

4. Upon completion of the installation of the CN0355 evaluation software, the
   installer for the **ADI SDP Drivers** will execute.

5. Click **Next** to finish the installation.

6. Click **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path **C:\\Program Files\\Analog Devices\\SDP\\Drivers**.

7. Press **Next** to install the **SDP Drivers** and complete the installation
   of all software.

8. Click **Finish** when done.

Connecting the Hardware
------------------------

.. figure:: cn0355_image8.png
   :align: center

   Hardware connection diagram

1. Plug the mini end of the USB cable into connector **J1** of the
   EVAL-SDP-CB1Z and connect the other end of the USB cable to the PC.

2. Connect the 120-pin connector of the SDP-PMD-IB1Z circuit board to the
   connector marked **CON A** on the EVAL-SDP-CB1Z evaluation (SDP) board.
   Nylon hardware should be used to firmly secure the two boards using the
   holes provided at the ends of the 120-pin connectors.

3. Populate a jumper across **JP1** to give +3.3 V voltage output on the PMOD
   terminal, as shown in the label on the SDP-PMD-IB1Z.

4. Connect the 12-pin right angle male pin header of EVAL-CN0355-PMDZ to the
   12-pin right angle female pin header of SDP-PMD-IB1Z.

5. Connect the +6 V DC power supply or equivalent to **JP1**, the barrel jack
   wall wart terminal of the SDP-PMD-IB1Z interposer board.

6. Connect the RTD sensor to **P2** of EVAL-CN0355-PMDZ.

7. Set **P3** and **P4** jumper configuration according to the type of RTD
   sensor that will be used.

   .. note::

      Jumper pin configuration to set up the RTD sensor can be seen on the
      back of the EVAL-CN0355-PMDZ evaluation board.

8. Connect the pressure transducer to **P1** of EVAL-CN0355-PMDZ.

9. Set **P5**, **P6**, and **P7** jumper configuration to the desired
   bridge-type transducer voltage drive.

   .. note::

      Jumper pin configuration to set up the bridge-type transducer voltage
      drive can be seen on the back of the EVAL-CN0355-PMDZ evaluation board.

10. Plug in the wall wart and connect it to connector **P8** of the
    EVAL-CN0355-PMDZ.

RTD and Bridge Type Transducer Interfacing
-------------------------------------------

.. figure:: cn0355_image9.png
   :align: center

   RTD and bridge type transducer interfacing diagram

Interface the RTD and bridge-type transducer to the EVAL-CN0355-PMDZ as shown
in the diagram above.

Opening and Enabling the Evaluation Software
----------------------------------------------

.. figure:: cn0355_image16.png
   :align: center

   CN0355 evaluation software

1. Launch the executable found at
   **C:\\Program Files\\Analog Devices\\CN0355**.

2. Click the **Run** button to start using the program.

3. After clicking the **Run** button, a prompt will appear informing the user
   that the SDP is now ready to acquire data and the rest of the buttons found
   in System Controls will be enabled.

Using the Evaluation Software
------------------------------

.. figure:: cn0355_image15.png
   :align: center

   CN0355 evaluation software controls

The following software controls are available, grouped by their location in
the software GUI:

1. **System Controls**:

   a. **Run** -- Configures the AD7793 by writing to the necessary registers.
      A prompt will appear informing the user if the ADC was properly
      configured.
   b. **Stop** -- Halts or pauses data acquisition. Resumes when the Run
      button is pressed again.
   c. **Save Data** -- Saves all data displayed in the LabVIEW chart.
   d. **Clear Data** -- Clears all data displayed in the LabVIEW chart.

2. **Main Tab** -- Contains the displays for the Data Graph, System, and SDP
   Board Firmware Revision:

   a. **Data Graph** -- A waveform chart displaying the pressure readings and
      temperature readings taken after performing system calibration.

   b. **System Calibration** -- Contains the controls necessary to calibrate
      the entire system using either 2-point or 4-point linear interpolation.
      Also contains the settings for the ADC data rate and RTD values.

      - **ADC and RTD Setting** -- Provides the capability to set the ADC data
        rate and the flexibility to use different values of RTD by entering the
        values in the given input box under RTD Value.

      - **Calibration Options** -- Defines the calibration type to be
        performed.

        .. note::

           The chosen calibration settings will be enabled for configuration
           and the other calibration will be disabled and greyed out.

      - **2-Point Calibration** -- Defines the values of the parameters used
        to calculate the pressure read by the transducer using two data points
        calibration without temperature compensation:

        - **Voltage Drive** -- Defines the voltage used to drive the
          bridge-type transducer.
        - **Minimum Range** -- Determines the minimum operating pressure range
          of the transducer.
        - **Maximum Range** -- Determines the maximum operating pressure range
          of the transducer.
        - **Sensitivity** -- Gives the mV sensitivity of the device over the
          defined voltage drive specified at full scale span.

          .. note::

             Sensitivity information can be found in the transducer datasheet.

      - **4-Point Calibration** -- Defines the values of the parameters used
        to calculate the pressure read by the transducer using four data points
        calibration with temperature compensation:

        - **Pressure 1** -- Defines the first pressure value point.
        - **Pressure 2** -- Defines the second pressure value point.
        - **Pressure Full Scale** -- Defines the maximum operating pressure
          range.
        - **Set Calibration Point @ temp 1** -- Captures the voltage reading
          generated at the transducer specified at temp 1 and at a defined
          pressure value:

          - *Pressure 1 @ temp 1* -- Sets the first calibration point at temp 1
            and pressure set at Pressure 1.
          - *Pressure 2 @ temp 1* -- Sets the second calibration point at
            temp 1 and pressure set at Pressure 2.

        - **Set Calibration Point @ temp 2** -- Captures the voltage reading
          generated at the transducer specified at temp 2 and defined pressure
          settings:

          - *Pressure 1 @ temp 2* -- Sets the third calibration point at
            temp 2 and pressure set at Pressure 1.
          - *Pressure 2 @ temp 2* -- Sets the fourth calibration point at
            temp 2 and pressure set at Pressure 2.

      - **Save or Load Cal Settings** -- Allows the user to save or recall
        calibration setups formatted in .xls files:

        - To save calibration settings, click **Save**, choose the desired
          location and provide a file name with .xls extension.
        - To recall calibration settings, click the folder icon to browse for
          the settings file and click **Load Calibration**.

3. **SDP Board Firmware Revision** -- Provides details on the firmware version
   of the Blackfin used by the SDP board.

Calibration Procedure
---------------------

This section explains the steps required to properly calibrate the
EVAL-CN0355-PMDZ.

.. admonition:: Pre-Calibration Notes

   - Choose the desired calibration option:

     - 2-point calibration does not require a temperature oven. It only
       requires the table to be filled in with numbers from the datasheet.
     - 4-point calibration requires an oven with calibrated temperature sensor
       and calibrated pressure source.
     - Dwell time of the temperature depends on the equipment being used.

   - The voltage drive set in the evaluation software should correspond to the
     configured jumper setup on the EVAL-CN0355-PMDZ.
   - All units are in PSI.
   - Sensitivity is usually found in the datasheet of the transducer to be
     used.

2-Point Calibration
~~~~~~~~~~~~~~~~~~~~

**Step 1** -- Set the voltage used to drive the transducer.

**Step 2** -- Set the minimum and maximum operating range of the sensor in PSI.

**Step 3** -- Set the sensitivity of the transducer that will be used.

**Step 4** -- Go to the Data Graph panel to view the measurement.

4-Point Calibration
~~~~~~~~~~~~~~~~~~~~

**Step 1** -- Define any two known pressure points where the calibration
conditions will be set and where the 4 points will be defined.

**Step 2** -- Set the temperature chamber at temp 1.

**Step 3** -- Under the Pressure Setting options, choose "Pressure 1 @ temp 1"
while the pressure at the chamber is set to the stated value in Pressure 1.

**Step 4** -- Click **Set Calibration Point @ temp 1** to read the voltage
generated by the transducer and the temperature voltage generated across the
RTD.

**Step 5** -- Set the chamber pressure to the stated value in Pressure 2 and
then choose "Pressure 2 @ temp 1" under the Pressure Setting options.

**Step 6** -- Click **Set Calibration Point @ temp 1** to read the voltage
generated by the transducer and the temperature voltage generated across the
RTD.

**Step 7** -- Click **Set Calibration Point @ temp 1** to read the voltage
generated by the transducer.

**Step 8** -- Set the temperature chamber at temp 2.

**Step 9** -- Repeat Steps 3 through 7 under the Temperature 2 column.

Documents
---------

- :adi:`CN0355 Circuit Note <CN0355>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0355-PMDZ Design & Integration Files
   <https://www.analog.com/cn0355-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD7793 Product Page <AD7793>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
