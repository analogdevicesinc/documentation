.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0240

.. _eval-cn0240-sdpz:

EVAL-CN0240-SDPZ
=================

Bidirectional High Voltage Current Measurement.

Overview
--------

:adi:`CN0240` is a circuit that monitors bidirectional current from sources with
DC voltages of up to +/-270 V with less than 1% linearity error. The load
current passes through a shunt resistor, which is external to the circuit. The
shunt resistor value is chosen so that the shunt voltage is approximately 100 mV
at maximum load current.

The :adi:`AD629` is a difference amplifier with a very high input common-mode
voltage range. It is a precision device that accurately measures and buffers
(G = 1) a small differential input voltage and rejects large positive
common-mode voltages up to 270 V. The output of the :adi:`AD629` is then
amplified by a factor of 100 through the dual, precision rail-to-rail output
operational amplifier :adi:`AD8622`.

The :adi:`AD8475` is a fully differential, attenuating amplifier with integrated
precision gain resistors. This funnel amplifier attenuates the signal (G = 0.4),
converts it from single-ended to differential, and level shifts the signal to
satisfy the analog input voltage range of the :adi:`AD7170`, a very low power
12-bit sigma-delta ADC. The measurement result from the :adi:`AD7170` is
provided as a digital code utilizing a simple 2-wire, SPI-compatible serial
interface.

The :adi:`ADuM5402` is a quad channel isolator that provides galvanic isolation
for the circuit. This is not only for protection but to isolate the downstream
circuitry from the high common-mode voltage. In addition to isolating the output
data, the digital isolator can also supply isolated +5 V for the circuit. The
reference voltage for the circuit is supplied by the :adi:`ADR435` precision
XFET voltage reference, which features low noise, high accuracy, and low
temperature drift performance.

The EVAL-CN0240-SDPZ board connects to ADI's System Demonstration Platform
(SDP) and is powered by a +6 V supply or +6 V wall wart.

.. figure:: cn0240-hw-1024.jpg
   :align: center

   EVAL-CN0240-SDPZ Evaluation Board

Required Equipment
------------------

- :adi:`EVAL-CN0240-SDPZ <CN0240>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0240 Evaluation Software
- Power supply: +6 V at 1 A (or +6 V wall wart)
- Dual power supply: +15 V and -15 V at 10 mA
- USB cable
- Shunt resistor with maximum voltage of 100 mV at maximum load current
- Source voltage and electronic load
- PC with Windows 7 (32-bit), Windows Vista (32-bit), or Windows XP with USB
  interface

.. warning::

   **High voltage!** This circuit may contain lethal voltages. **Do not**
   operate, evaluate, or test this circuit, or board assembly, unless you are a
   trained professional, who is qualified to handle high voltage circuitry.
   Before applying power, you must be familiar with the circuitry and all
   required precautions for working with high voltage circuits.

Hardware Setup
--------------

Block Assignments
~~~~~~~~~~~~~~~~~~

.. figure:: 1.png
   :align: center

   CN0240 Functional Block Diagram

- The EVAL-CN0240-SDPZ (CN-0240 board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B board) via the 120-pin connector.
- The :adi:`EVAL-SDP-CB1Z` (SDP-B board) connects to the PC via the USB cable.

.. list-table:: Terminal Block Assignments
   :header-rows: 1

   * - Connector
     - Function
   * - **J1**
     - 120-pin SDP connector
   * - **J2**
     - +6 V barrel connector (wall wart supply input)
   * - **J3**
     - +6 V DC power supply input
   * - **J4**
     - High voltage input terminals (+/-270 V max) for shunt resistor and load
   * - **J5**
     - +/-15 V supply input
   * - **J6**
     - Test point for SPI data lines

Test Setup
~~~~~~~~~~~

.. figure:: 9.png
   :align: center

   CN0240 Test Setup Diagram

#. Connect the 120-pin connector on the EVAL-CN0240-SDPZ evaluation board to
   the connector marked **CON A** on the :adi:`EVAL-SDP-CB1Z` evaluation (SDP)
   board.
#. Connect a shunt resistor across the **J4** input terminals with a load to
   ground.
#. With power to the supply off, connect a +6 V power supply to the pins
   marked **+6 V** and **GND** on the board. If available, a +6 V wall wart
   can be connected to the barrel connector on the board and used in place of
   the +6 V power supply.
#. Connect the USB cable supplied with the SDP board to the USB port on the PC.
#. Apply power to the +6 V supply (or wall wart) connected to the
   EVAL-CN0240-SDPZ evaluation board.
#. Launch the evaluation software.
#. Connect the USB cable from the PC to the USB mini connector on the SDP
   board.

.. important::

   Connect the **system ground** and the **PCB isolated ground** to guarantee
   correct voltage levels and operation. **Test point 31** and **test point 32**
   give access to the GND_ISO required to properly make this connection.

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0240_Evaluation_Software.zip** and run **setup.exe**.

   .. note::

      It is recommended that you install the CN0240 Evaluation Software to the
      default directory path
      ``C:\Program Files (x86)\Analog Devices\CN0240\`` and all National
      Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: 2.png
      :align: center

      CN0240 Evaluation Software Installer

#. Click **Next** to view the installation review page.

   .. figure:: 3.png
      :align: center

      Installation Review Page

#. Click **Next** to start the installation.

   .. figure:: 4.png
      :align: center

      Installation Progress

#. Upon completion of the CN0240 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: 5.png
      :align: center

      ADI SDP Drivers Installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: 6.png
      :align: center

      SDP Drivers Installation Location

#. Press **Install** to install the SDP Drivers and complete the installation
   of all software. Click **Finish** when done.

   .. figure:: 7.png
      :align: center

      SDP Drivers Installation Complete

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: 10.png
   :align: center

   CN0240 Evaluation Software Main Window

**Main Window Controls:**

#. **Connect** -- Starts the connection between the CN0240 evaluation board and
   the SDP-B controller board.
#. **Disconnect** -- Ends the connection between the CN0240 evaluation board
   and the SDP-B controller board.
#. **Data Acquisition Controls:**

   .. figure:: 11.png
      :align: center

      Data Acquisition Controls

   - **Select SDP Connector** -- Selects which 120-pin connection of the SDP-B
     board to use.
   - **Shunt voltage** -- Shunt voltage measurement from shunt resistor.
   - **Sample Data** -- Start acquisition of measurement data.
   - **Remove Data Point** -- Remove a data point from samples.
   - **Calculate errors** -- Calculate conversion errors in ADC.
   - **Save Data** -- Save measurement data to file.
   - **Clear Data** -- Clear all data collected from the chart history.

#. **Sample Data Graph Tab** -- Shows the XY plot of ADC code and output error
   (%) with respect to the shunt voltage.

   .. figure:: 14.png
      :align: center

      Sample Data Graph Tab

   - **Plot Options** -- Edit plot display and options such as interpolation
     and color of output waveform.

#. **Configure Tab:**

   .. figure:: 13.png
      :align: center

      Configure Tab

   - **SDP Connector** -- Selects which 120-pin connection of the SDP-B board
     to use.
   - **Flash LED** -- Flashes the LED on the SDP controller board.
   - **Read Firmware** -- Reads the firmware of the CN0240 evaluation board.

#. **Quit** -- Closes the evaluation software.

Running the System
~~~~~~~~~~~~~~~~~~~

#. Open the CN0240.exe application from the default installation location.
#. Set the correct connector and click the **Connect** button.
#. Upon successful connection, set the desired input signal parameters such as
   shunt voltage.
#. Start and control data acquisition through the data acquisition control
   buttons.
#. Output data will be shown in the graph. Edit graph through plot options and
   check boxes provided.
#. Click **Disconnect** if finished.
#. Click **Quit** to exit the program.

Documents
---------

- :adi:`CN0240 Circuit Note <CN0240>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0240-SDPZ Design & Integration Files
   <https://www.analog.com/cn0240-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS project

Additional Information
----------------------

- :adi:`AD629 Product Page <AD629>`
- :adi:`AD8622 Product Page <AD8622>`
- :adi:`AD8475 Product Page <AD8475>`
- :adi:`AD7170 Product Page <AD7170>`
- :adi:`ADuM5402 Product Page <ADUM5402>`
- :adi:`ADR435 Product Page <ADR435>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
