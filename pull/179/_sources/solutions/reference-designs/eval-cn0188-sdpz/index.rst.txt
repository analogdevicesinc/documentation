.. _eval-cn0188-sdpz:

EVAL-CN0188-SDPZ
=================

Current Monitoring for -48 V Telecom Power Systems.

Overview
--------

:adi:`CN0188 <CN0188>` is a circuit that monitors current in individual
channels of -48 V systems to better than 1% accuracy. The load current passes
through a shunt resistor, which is external to the circuit. The shunt resistor
value is chosen so that the shunt voltage is approximately 50 mV at maximum
load current. The entire circuit operates on a single +3.3 V supply.

The :adi:`AD7171` is a very low power, 16-bit, analog-to-digital converter
(ADC). It contains a precision, 16-bit, sigma-delta ADC and an on-chip
oscillator. The measurement result from the AD7171 is provided as a digital
code utilizing a simple 2-wire, SPI-compatible serial interface. Optional
galvanic isolation is provided by the :adi:`ADuM5402 <ADUM5402>` quad channel
isolator. In addition to isolating the output data, the digital isolator can
also supply isolated +3.3 V for the circuit.

The :adi:`ADA4051-2` is a CMOS, micropower, zero-drift operational amplifier
utilizing an innovative chopping technique. This amplifier features rail-to-rail
input/output swing and extremely low offset voltage while operating from a
1.8 V to 5.5 V power supply.

The :adi:`ADR381` is a precision 2.500 V band gap voltage reference featuring
high accuracy, high stability, and low power consumption in a tiny footprint.
It is a micropower, low dropout voltage (LDV) device that provides a stable
output voltage from supplies as low as 300 mV above the output voltage.

The EVAL-CN0188-SDPZ board connects to ADI's System Demonstration Platform
(SDP) and is powered by a +6 V supply or +6 V wall wart.

.. figure:: cn0188_hardware.jpg
   :width: 600px
   :align: center

   EVAL-CN0188-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0188-SDPZ <EVAL-CN0188-SDPZ>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0188 evaluation software
- +6 V power supply or +6 V wall wart
- USB cable
- Shunt resistor with maximum voltage of 50 mV at maximum load current
- Electronic load
- PC with the following minimum requirements:

  - Windows 7 (32-bit), Windows Vista (32-bit), or Windows XP
  - USB interface

General Setup
-------------

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: cn0188_block_diagram.png
   :width: 600px
   :align: center

   EVAL-CN0188-SDPZ block assignments

- The **EVAL-CN0188-SDPZ** (CN0188 board) connects to the **EVAL-SDP-CB1Z**
  (SDP-B board) via the 120-pin connector.
- The **EVAL-SDP-CB1Z** (SDP-B board) connects to the PC via the USB cable.
- Terminal block **J2** is the +6 V barrel connector for wall wart supply
  input.
- Terminal block **J3** is the test point for 6 V DC output.
- Terminal block **J4** contains the input terminals for R\ :sub:`shunt` and
  load to ground.

Test Setup
~~~~~~~~~~

.. figure:: cn0188_test_setup.png
   :width: 600px
   :align: center

   EVAL-CN0188-SDPZ test setup diagram

1. Connect the 120-pin connector on the EVAL-CN0188-SDPZ evaluation board to
   the connector marked **CON A** on the EVAL-SDP-CB1Z evaluation (SDP) board.

2. Connect a shunt resistor across the input terminals with a load to ground
   as indicated in the test setup diagram.

3. With power to the supply off, connect a +6 V power supply to the pins
   marked **+6V** and **GND** on the board.

   .. note::

      If available, a +6 V wall wart can be connected to the barrel connector
      on the board and used in place of the +6 V power supply.

4. Connect the USB cable supplied with the SDP board to the USB port on the PC.

5. Apply power to the +6 V supply (or wall wart) connected to the
   EVAL-CN0188-SDPZ evaluation board.

6. Launch the evaluation software.

7. Connect the USB cable from the PC to the USB mini connector on the SDP
   board.

.. important::

   Connect the **system ground** and the **PCB isolated ground** to guarantee
   correct voltage levels and operation. **Test point 31** and **test point 32**
   give access to the GND_ISO required to properly make this connection.

Installing the Evaluation Software
------------------------------------

1. Extract the file **CN0188_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0188 evaluation software to the
      default directory path
      **C:\\Program Files (x86)\\Analog Devices\\CN0188\\** and all National
      Instruments products to **C:\\Program Files\\National Instruments\\**.

   .. figure:: cn0188_installer_step_1.png
      :width: 500px
      :align: center

      CN0188 evaluation software installer -- welcome screen

2. Click **Next** to view the installation review page.

   .. figure:: cn0188_installer_step_2.png
      :width: 500px
      :align: center

      CN0188 evaluation software installer -- installation review

3. Click **Next** to start the installation.

   .. figure:: cn0188_installer_step_3.png
      :width: 500px
      :align: center

      CN0188 evaluation software installer -- installation progress

4. Upon completion of the installation of the **CN0188 Evaluation Software**,
   the installer for the **ADI SDP Drivers** will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0188_installer_step_4.png
      :width: 500px
      :align: center

      ADI SDP Drivers installer -- welcome screen

5. Press **Next** to set the installation location for the **SDP Drivers**.

   .. note::

      It is recommended that you install the drivers to the default directory
      path **C:\\Program Files\\Analog Devices\\SDP\\Drivers**.

   .. figure:: cn0188_installer_step_5.png
      :width: 500px
      :align: center

      ADI SDP Drivers installer -- installation location

6. Press **Install** to install the **SDP Drivers** and complete the
   installation of all software. Click **Finish** when done.

   .. figure:: cn0188_installer_step_6.png
      :width: 500px
      :align: center

      ADI SDP Drivers installer -- installation complete

Using the Evaluation Software
------------------------------

Main Window
~~~~~~~~~~~

.. figure:: cn0188_main_window.png
   :width: 700px
   :align: center

   CN0188 evaluation software -- main window

The evaluation software main window provides the following controls and
indicators:

1. **Connect Button** -- Starts the connection between the CN0188 evaluation
   board and the SDP-B controller board.

2. **Disconnect Button** -- Ends the connection between the CN0188 evaluation
   board and the SDP-B controller board.

3. **Select SDP Connector** -- Selects which 120-pin connection of the SDP-B
   board to use.

4. **Shunt Voltage Input** -- Determines input shunt voltage level in
   millivolts.

5. **Temperature** -- Temperature level test conditions of input signal.

6. **Data Acquisition Controls**:

   .. figure:: cn0188_data_acquisition.png
      :width: 600px
      :align: center

      CN0188 evaluation software -- data acquisition controls

   - **Sample Data** -- Starts acquisition of measurement data.
   - **Remove Data Point** -- Removes a data point from samples.
   - **Save Data** -- Saves measurement data to file.
   - **Clear Data** -- Clears the current measurement data.

7. **Sample Data Graph Tab** -- Shows the XY plot of ADC code and output error
   (%) with respect to the shunt voltage:

   .. figure:: cn0188_sample_graph.png
      :width: 600px
      :align: center

      CN0188 evaluation software -- sample data graph

   - **ADC Code Plot Enable** -- Shows or hides the ADC Code plot.
   - **Error Plot Enable** -- Shows or hides the Error plot.
   - **Converted Shunt Voltage** -- Shunt voltage value from the ADC.
   - **Over/Under Voltage Indicator** -- Indicates over or under voltage
     conditions.
   - **Plot Options** -- Edit plot display and options like interpolation and
     color of output waveform.

8. **Administration Tab**:

   .. figure:: cn0188_admin_tab.png
      :width: 600px
      :align: center

      CN0188 evaluation software -- administration tab

   - **Flash LED** -- Flashes the LED on the SDP controller board.
   - **Read Firmware** -- Reads the firmware of the evaluation board.

9. **Quit Button** -- Closes the evaluation software.

Running the System
~~~~~~~~~~~~~~~~~~

1. Open the **CN0188.exe** application from the default installation location.
2. Set the correct connector and click the **Connect** button.
3. Upon successful connection, set the desired input signal parameters such as
   shunt voltage and temperature.
4. Start and control data acquisition through the data acquisition control
   buttons.
5. Output data will be shown in the graph. Edit the graph through plot options
   and check boxes provided.
6. Click **Disconnect** when finished.
7. Click **Quit** to exit the program.

Documents
---------

- :adi:`CN0188 Circuit Note <CN0188>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0188-SDPZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0188-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Additional Information
----------------------

- :adi:`AD7171 Product Page <AD7171>`
- :adi:`ADuM5402 Product Page <ADUM5402>`
- :adi:`ADA4051-2 Product Page <ADA4051-2>`
- :adi:`ADR381 Product Page <ADR381>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
