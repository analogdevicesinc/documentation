.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0350

.. _eval-cn0350-pmdz:

EVAL-CN0350-PMDZ
=================

Charge Input Data Acquisition System for Piezoelectric Sensors.

Overview
--------

:adi:`CN0350` provides a robust and complete solution for processing charge
input signals into digital code, for acceleration and shock measurements where
piezoelectric sensors with charge output are used. The design solution is
optimized for high precision and low cost measurement, using only two active
devices, and has a total error less than 0.25% FSR after calibration over a
+/-10 degrees C temperature range. The accuracy depends on the calibration.

The circuit shown in Figure 1 incorporates the :adi:`AD8608` quad op-amp and the
:adi:`AD7091R` 12-bit successive approximation (SAR) ADC to convert the charge
output from piezoelectric sensors into digital code.

The circuit has a 12-pin PMOD connector on board, which can be used for
connection to a microprocessor or FPGA.

The :adi:`CN0350 Circuit Note <CN0350>` discusses the design steps needed to
optimize the circuit for a specific bandwidth including noise analysis and
component selection considerations.

The performance of the circuit can be demonstrated with the use of the Analog
Devices :adi:`EVAL-SDP-CB1Z` controller board and :adi:`SDP-PMD-IB1Z`
SDP-to-PMOD interposer board, both optional purchase items. This user guide
discusses how to use the evaluation software to collect data from the
EVAL-CN0350-PMDZ evaluation board.

.. figure:: cn0350_hw_375.jpg
   :align: center
   :width: 400

   EVAL-CN0350-PMDZ Evaluation Board

.. figure:: cn0350_overview_fig_1.png
   :align: center

   Charge Input Single Supply Data Acquisition System for Piezoelectric Sensors
   (All Connections and Decoupling Not Shown)

Required Equipment
------------------

- :adi:`EVAL-SDP-CB1Z` Controller Board (SDP-B Board)
- :adi:`EVAL-CN0350-PMDZ <CN0350>` Evaluation Board
- :adi:`EVAL-CFTL-6V-PWRZ` +6 V Power Supply or equivalent
- :adi:`SDP-PMD-IB1Z` SDP-to-PMOD Interposer Board
- Voltage source (signal generator)
- Multimeter (to measure the input current)
- `CN0350 Evaluation Software <https://www.analog.com/CN0350>`__
  (supplied with provided CD in kit)
- PC with the following minimum requirements:

  - Windows XP Service Pack 2 (32-bit)
  - USB type A port
  - Processor rated at 1 GHz or faster
  - 512 MB RAM and 500 MB available hard disk space

- USB type A to USB type mini-B cable (provided with the
  :adi:`EVAL-SDP-CB1Z` Controller Board)

General Setup
-------------

- The :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) powers the
  :adi:`SDP-PMD-IB1Z` (Interposer Board) via the DC barrel jack.
- The :adi:`SDP-PMD-IB1Z` (Interposer Board) connects to the
  :adi:`EVAL-SDP-CB1Z` (SDP-B Board) via the 120-pin connector A.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB cable.
- The EVAL-CN0350-PMDZ connects to the Interposer Board via the 12-pin header
  PMOD connector (J2 and J3).
- The voltage generator connects to the EVAL-CN0350-PMDZ via the terminal
  block J1.

.. figure:: cn0350_general_setup.png
   :align: center

   CN0350 General Test Setup

Installing the Software
-----------------------

#. Load the evaluation software by placing the CN0350 evaluation software disc
   in the CD drive of the PC. You can also download the most up-to-date copy of
   the evaluation software from the
   `CN0350 product page <https://www.analog.com/CN0350>`__. Open the file
   ``setup.exe``.

   .. note::

      It is recommended that you install the CN0350 Evaluation Software to the
      default directory path ``C:\Program Files\Analog Devices\CN0350\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0350_installing_sw_1.png
      :align: center

      CN0350 Software Installer Welcome Screen

#. Click **Next** to view the installation review page.

   .. figure:: cn0350_installing_sw_2.png
      :align: center

      Installation Review Page

#. Click **Next** to start the installation.

   .. figure:: cn0350_installing_sw_3.png
      :align: center

      Installation Progress

#. Upon completion of the installation of the CN0350 Evaluation Software, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0350_installing_sw_4.png
      :align: center

      ADI SDP Drivers Installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\DriversR2``.

   .. figure:: installing_sw_5.png
      :align: center

      SDP Drivers Installation Location

#. Press **Next** to install the SDP Drivers and complete the installation of
   all software. Click **Finish** when done.

   .. figure:: cn0350_installing_sw_6.png
      :align: center

      SDP Drivers Installation Complete

   .. figure:: installing_sw_6a.png
      :align: center

      Installation Finished

Connecting the Hardware
-----------------------

#. Connect the :adi:`EVAL-CFTL-6V-PWRZ` (+6 V DC Power Supply) to the barrel
   jack **J1** of the :adi:`SDP-PMD-IB1Z` (Interposer Board) as depicted below.

   .. note::

      Make sure that the jumper is positioned as shown below.

   .. figure:: cn0350_connecthw_1.png
      :align: center
      :width: 600

      Power Supply Connection to Interposer Board

#. Connect the 120-pin connector on the :adi:`SDP-PMD-IB1Z` (Interposer Board)
   to the 120-pin connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z`
   (SDP-B Board).

   .. figure:: cn0350_connecthw_2.png
      :align: center
      :width: 600

      Interposer Board to SDP-B Board Connection

#. Connect the USB cable supplied with the :adi:`EVAL-SDP-CB1Z` (SDP-B Board)
   to the USB port on the PC and the SDP Board.

   .. figure:: cn0350_connecthw_3.png
      :align: center
      :width: 600

      USB Connection to SDP-B Board

   .. note::

      Verify that the SDP Drivers are loaded properly. Open the Device Manager
      and check if the SDP Board is recognized. If not, repeat steps 1--3.

   .. figure:: cn0350_connecthw_3a.png
      :align: center

      Device Manager Showing SDP Board

#. Connect the EVAL-CN0350-PMDZ (CN0350 Board) to the :adi:`SDP-PMD-IB1Z`
   (Interposer Board) via the 12-pin header PMOD connector.

   .. figure:: cn0350_connecthw_4.png
      :align: center
      :width: 600

      CN0350 Board Connected to Interposer Board

#. Connect the input voltage generator to J1 Terminal Block located on the
   EVAL-CN0350-PMDZ (CN0350 Board). The positive end of the voltage generator
   has to be wired to the input marked with **CAL** and the negative end of the
   voltage generator has to be wired to the input marked with **NEG**.

#. After a proper connection of the hardware to the PC, the CN0350 Evaluation
   Software can be used to calibrate the board and capture data.

Using the Evaluation Software
------------------------------

Software Control and Indicator Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0350_using_sw_1.png
   :align: center

   CN0350 Evaluation Software -- Acquire Data Tab

.. figure:: cn0350_using_sw_2.png
   :align: center

   CN0350 Evaluation Software -- Calibrate System Tab

.. figure:: cn0350_using_sw_3.png
   :align: center

   CN0350 Evaluation Software -- SDP Revision Tab

The CN0350 evaluation software provides the following controls and indicators:

#. **Acquire Data Button** -- When this button is pressed, the SDP-B Board will
   collect conversion data and present it in the graph.

#. **Clear Data Button** -- When this button is pressed, the software will clear
   all data collected from the graph history.

#. **Save Data Button** -- When this button is pressed, the software will save
   the captured data to a tab-delimited ASCII spreadsheet file. The units of the
   saved data depend on the chosen graph units (6).

#. **Control Tabs**:

   - *Acquire Data Main* -- Clicking this tab brings the data collection graph
     to the front.
   - *Calibrate System* -- Clicking this tab brings the system calibration
     settings to the front.
   - *SDP Revision* -- Clicking this tab brings the SDP board information
     window to the front.

#. **Numerical Indicator** -- Displays the current reading value. The value
   units depend on the chosen graph units (6).

#. **Graph Units Radio Buttons** -- Determines the units of the data displayed
   in the graph and the numerical indicator.

#. **ADC Settings** -- Controls the SPI communication settings. The
   **Sample Rate (Hz)** control determines the conversion frequency and the
   **Samples** control determines the number of samples to be captured when
   clicking the Acquire Data button. The maximum sample rate is set to 620 kHz
   and the maximum samples are set to 1M. Changing these controls automatically
   changes the x-axis time on the graph.

#. **Graph** -- Displays the collected data. The units on the graph depend on
   the chosen graph units (6).

#. **Graph Controls** -- Allow the user to zoom in, zoom out, and pan through
   the collected data.

#. **System Status String Indicator** -- Displays a message to the user
   detailing the current state of the software.

#. **System Status LED Indicator** -- Displays the current state of the software
   in the form of an LED. There are four status LED colors:

   .. list-table::
      :header-rows: 0

      * - .. image:: cn0350_using_sw_12inactive.png
        - Inactive
      * - .. image:: cn0350_using_sw_12busy.png
        - Busy
      * - .. image:: cn0350_using_sw_12error.png
        - Error
      * - .. image:: cn0350_using_sw_12waiting.png
        - Waiting for user action

#. **Calibration Coulombs Numerical Control** -- Set this control to the input
   coulombs in pC, used to calibrate the board.

#. **Calibrate Button** -- Pressing this button initiates a calibration of the
   board. After pressing this button, follow the instructions to calibrate the
   board.

#. **Sensor Sensitivity Numerical Control** -- Used if a real piezoelectric
   sensor is used to capture data. Set the sensor sensitivity in pC/g here to be
   able to display correctly the captured data as acceleration (g). Another
   calibration is not needed for that purpose.

#. **SDP Firmware Revision** -- Read-only data. After the connection is
   established with the SDP Board, the basic information for the controller can
   be found here.

Establishing a USB Connection Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Follow the instructions to properly install the software and connect the
   hardware as described in the previous sections.

#. Open the file named ``CN0350.exe`` in the installation directory.

   .. note::

      If the software was installed to the default location it will be found at
      ``C:\Program Files\Analog Devices\CN0350\CN0350.exe``.

#. The software should connect to the board automatically. If the hardware is
   not recognized by the PC, a window will appear indicating that the software
   is waiting for proper hardware connection. If that happens, perform the
   hardware connection procedure described in the previous section. After
   connecting the hardware, the list in the window will populate. Choose the
   connected hardware and click **Select**.

   .. figure:: cn0350_establishing_connection_3.png
      :align: center

      Hardware Connection Selection Dialog

#. Upon success, the **System Status String Indicator** will display
   *SDP Board Ready to Acquire Data*.

Calibrating the CN0350 Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For calibration, an adjustable amplitude and frequency low-impedance output
voltage source is required with sine wave output. The power supply voltage
source has to be very well isolated from the circuit (the computer).

Connect the voltage source (voltage generator) as shown in the figure below.
The positive end of the voltage source is wired to the **CAL** input of the
board. The negative end is wired to the **NEG** input. With the described
configuration the board can be calibrated for various input ranges by changing
the amplitude of the voltage source or the calibration capacitance.

The amount of the input charge is determined by the formula Q = Ccal * Vin. The
figure below shows a calibration configuration for 1000 pC at the input of the
board (Vin = 1 V, Ccal = 1 nF). Note that a 1 nF capacitor is populated on the
board, but you can use TP1 and TP2 to add an additional capacitor in parallel.

.. note::

   The output voltage of the charge amplifier must not exceed the input range
   of the ADC. For a 1 nF calibration capacitor, do not apply more than 1 V
   to the input of the board (Vout = Q/C2). If you need to calibrate the system
   for more than 1000 pC, add an external capacitor in parallel to C2 using TP3
   and TP4.

.. figure:: cn0350_calibrating_fig2.png
   :align: center

   Calibration Configuration for 1000 pC Input

Calibration Procedure Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB Connection Link.
#. Click the **Calibrate System** tab.
#. Set the **Calibration Coulombs Control** to the coulombs that will be
   applied to the board during calibration.
#. Press the **Calibrate** button.
#. A pop-up window appears. Apply the coulombs to the input of the board as
   described and click **OK**.

   .. note::

      If you press **Cancel** at this point you will exit the calibration
      procedure but the board will not be able to capture data properly.

#. A second pop-up window appears. Remove the input voltage source from the
   board input. When ready, press **OK**.

   .. note::

      If you press **Cancel** the board will still not be calibrated.

.. figure:: cn0350_cal_procedure_steps_6.png
   :align: center

   Calibration Step -- Apply Input Coulombs

.. figure:: cn0350_cal_procedure_steps_6a.png
   :align: center

   Calibration Step -- Remove Input Source

Acquiring Data
~~~~~~~~~~~~~~

Once calibrated, the board can be used to capture data from real piezoelectric
sensors. The positive end of the piezoelectric sensor should be wired to **POS**
on the board and the negative to **NEG**. In order to display the result from
the sensor as acceleration (g), adjust the **Sensor Sensitivity Control** to
equal the sensitivity of the sensor.

Another method to demonstrate the functionality of the board is to use the
voltage generator connected to the calibration input. By changing the input
voltage amplitude or the calibration capacitor, various input coulombs can be
provided to the input of the board.

#. Establish a USB Connection Link.
#. Click the **Acquire Data** button.

Saving Data to a Spreadsheet File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Establish a USB Connection Link.
#. Capture data as described above.
#. Click the **Save Data** button.

   .. figure:: cn0350_saving_data_3.png
      :align: center

      Save Data Dialog

#. Click the **OK** button.
#. Browse to the directory location where the spreadsheet file is to be saved.
#. Name the file.
#. Click the **OK** button.
#. Open with Notepad or similar. The saved data shows the collected data
   according to the chosen **Graph Units Radio Buttons**.

   .. note::

      The software saves the spreadsheet file as ASCII text with columns
      separated by tabs.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `CN0350 Design & Integration Files <https://www.analog.com/CN0350>`__

   - Schematics
   - PCB Layout
   - Bill of Materials

Additional Information
----------------------

- :adi:`AD8608 Product Page <AD8608>`
- :adi:`AD7091R Product Page <AD7091R>`
- :adi:`CN0350 Circuit Note <CN0350>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
