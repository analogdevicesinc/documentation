.. _eval-cn0178-sdpz:

EVAL-CN0178-SDPZ
=================

Wideband True RMS RF Power Detector (50 MHz to 9 GHz).

Overview
--------

:adi:`CN0178 <CN0178>` is a circuit that measures the rms signal strength of
RF signals with varying crest factors (peak-to-average ratio) over a dynamic
range of approximately 65 dB and operates at frequencies from 50 MHz up to
9 GHz using the :adi:`ADL5902` TruPwr detector. The measurement result is
provided as serial data at the output of a 12-bit ADC. A simple 4-point system
calibration at ambient temperature is performed in the digital domain.

The :adi:`ADL5902` provides a solution in a variety of high frequency systems
requiring an accurate measurement of signal power. It can operate from 50 MHz
to 9 GHz and can accept inputs from -62 dBm to at least +3 dBm with large
crest factors, such as GSM, CDMA, W-CDMA, TD-SCDMA, WiMAX, and LTE modulated
signals.

The :adi:`AD7466` is a 12-bit, high speed, low power, successive approximation
ADC. It operates from a single 1.6 V to 3.6 V power supply and features
throughput rates up to 200 kSPS with low power dissipation. It contains a low
noise, wide bandwidth track-and-hold amplifier which can handle input
frequencies in excess of 3 MHz.

The EVAL-CN0178-SDPZ board connects to ADI's System Demonstration Platform
(SDP) and is powered by a +6 V supply or +6 V wall wart.

.. figure:: cn0178-hw-1024.jpg
   :align: center

   EVAL-CN0178-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0178-SDPZ <EVAL-CN0178-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B Board)
- CN0178 Evaluation Software
- +6 V power supply or +6 V wall wart (e.g., Agilent E3631A)
- PC with Windows 7 (32-bit), Windows Vista (32-bit), or Windows XP;
  USB interface
- RF signal source (e.g., Rohde & Schwarz SMT-03)
- Coaxial RF cable with SMA connectors

General Setup
-------------

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: cn0178_block_diagram.png
   :align: center

   CN0178 system block diagram

- The EVAL-CN0178-SDPZ (CN0178 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector.
- The SDP-B Board connects to the PC via the USB cable.
- Terminal block **J1** is the +6 V power supply input.
- Terminal block **J2** is the +6 V barrel connector for wall wart supply.
- **J3** is the SMA connector for RF input.

Test Setup
~~~~~~~~~~

.. figure:: cn0178_test_setup.png
   :align: center

   CN0178 test setup

#. Connect the 120-pin connector on the EVAL-CN0178-SDPZ to the connector
   marked "CON A" on the :adi:`EVAL-SDP-CB1Z`.
#. Connect the RF signal source to the EVAL-CN0178-SDPZ via the SMA RF input
   connector.
#. With power to the supply off, connect a +6 V power supply to the pins
   marked "+6V" and "GND" on the board. Alternatively, a +6 V wall wart can
   be connected to the barrel connector.
#. Connect the USB cable supplied with the SDP board to the USB port on the PC.
#. Apply power to the +6 V supply (or wall wart).
#. Launch the evaluation software.
#. Connect the USB cable from the PC to the USB mini connector on the SDP
   board.

.. important::

   Do **not** connect the USB cable to the Mini-USB connector on the SDP board
   before turning on the dc power supply for the EVAL-CN0178-SDPZ.

Calibration
~~~~~~~~~~~

Because the slope and intercept of the system vary from device to device, a
system level calibration is **required**. For this board, a 4-point calibration
is used to correct for some non-linearity in the RF detector's transfer
function, particularly at the low end.

#. Apply four known signal levels to the ADL5902. These should be well within
   the linear operating range of the device.

   .. figure:: cn0178_transfer_function.png
      :align: center

      ADL5902 RF detector transfer function

#. Measure the corresponding output codes from the ADC.
#. Calculate SLOPE and INTERCEPT calibration coefficients using the following
   equations:

   - **SLOPE_1** = (CODE_1 - CODE_2) / (PIN_1 - PIN_2)
   - **INTERCEPT_1** = CODE_1 / (SLOPE_ADC / PIN_1)

#. This calculation is repeated using CODE_2/CODE_3 and CODE_3/CODE_4 to
   calculate SLOPE_2/INTERCEPT_2 and SLOPE_3/INTERCEPT_3 respectively.
#. These are used to calculate the unknown input power level:

   - **PIN** = (CODE / SLOPE) + INTERCEPT

#. The observed code from the ADC is compared to the calibration coefficient
   codes to retrieve the appropriate SLOPE and INTERCEPT. For example, if CODE
   from the ADC is between CODE_1 and CODE_2, then SLOPE_1/INTERCEPT_1 should
   be used.

Installing the Evaluation Software
-----------------------------------

#. Extract the file **CN0178_Evaluation_Software.zip** and open **setup.exe**.

   .. note::

      It is recommended to install the CN0178 Evaluation Software to the
      default path ``C:\Program Files (x86)\Analog Devices\CN0178\`` and all
      National Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0178_install_1.png
      :align: center

      CN0178 evaluation software installer

#. Click **Next** to view the installation review page.

   .. figure:: cn0178_install_2.png
      :align: center

      Installation review page

#. Click **Next** to start the installation.

   .. figure:: cn0178_install_3.png
      :align: center

      Installation progress

#. Upon completion, the ADI SDP Drivers installer will execute.

   .. note::

      Close all other applications before clicking "Next" to allow system file
      updates without rebooting.

   .. figure:: cn0178_install_4.png
      :align: center

      SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      Recommended path: ``C:\Program Files\Analog Devices\SDP\Drivers``

   .. figure:: cn0178_install_5.png
      :align: center

      SDP Drivers installation path

#. Press **Install** to install the SDP Drivers. Click **Finish** when done.

   .. figure:: cn0178_install_6.png
      :align: center

      SDP Drivers installation complete

Using the Evaluation Software
------------------------------

Main Window
~~~~~~~~~~~

.. figure:: cn0178_software_main.png
   :align: center

   CN0178 evaluation software main window

The evaluation software provides the following controls and displays:

#. **Connect** button -- Starts the connection between the CN0178 Evaluation
   Board and SDP-B Controller Board.
#. **Disconnect** button -- Ends the connection.
#. **SDP Connector** -- Selects which 120-pin connection of the SDP-B Board to
   use.
#. **Input Power** -- Indicate input signal power level.
#. **Frequency** -- Indicate input signal frequency.
#. **Data Acquisition** controls:

   .. figure:: cn0178_software_data_acq.png
      :align: center

      Data acquisition controls

   - **Sample Data** -- Start acquisition of measurement data
   - **Remove Data Point** -- Remove a data point from samples
   - **Clear Data** -- Clear the current measurement data
   - **Save Data** -- Save measurement data to file

#. **Sample Data Graph** tab -- Shows the XY plot of ADC code and output error
   (%) with respect to the input power. Contains plot options for
   interpolation and color settings.

   .. figure:: cn0178_data_graph.png
      :align: center

      Sample data graph tab

#. **Calibration** tab:

   - **Calibration Inputs** -- Four-point input power levels used for
     calibration
   - **Calibration Data** -- Enable calibration of the device
   - **Calibration Coefficients** -- Read only; calculated calibration
     coefficients based on four-point input power levels

#. **Administration** tab:

   .. figure:: cn0178_admin_tab.png
      :align: center

      Administration tab

   - **Read Firmware** -- Reads the firmware of the evaluation board
   - **Flash LED** -- Flashes the LED on the SDP controller board

#. **Quit** button -- Closes the evaluation software.

Running the System
~~~~~~~~~~~~~~~~~~

#. Open the **CN0178.exe** application from the default installation location.
#. Set the correct connector and click the **Connect** button.
#. Upon successful connection, calibrate the device through the
   **Calibration** tab.
#. After proper calibration, set the correct input parameters and control the
   data measurement through the data acquisition control buttons.
#. Click **Disconnect** when finished.
#. Click **Quit** to exit the program.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0178-SDPZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0178-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Documents
---------

- :adi:`CN0178 Circuit Note <CN0178>`

Additional Information
----------------------

- :adi:`ADL5902 Product Page <ADL5902>`
- :adi:`AD7466 Product Page <AD7466>`
- :adi:`ADG3231 Product Page <ADG3231>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
