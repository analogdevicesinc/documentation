.. _eval-cn0218-sdpz:

EVAL-CN0218-SDPZ
=================

High Common-Mode Voltage Current Shunt Monitor.

Overview
--------

:adi:`CN0218` is a circuit that monitors current in systems with high positive
common-mode DC voltages of up to +500 V with less than 0.2% error. The load
current passes through a shunt resistor, which is external to the circuit. The
circuit is designed for a full-scale shunt voltage of 500 mV at maximum load
current.

The :adi:`AD8212` is a high common-mode voltage, current shunt monitor. It
accurately amplifies a small differential input voltage in the presence of
large common-mode voltages up to 65 V (>500 V with an external PNP
transistor). The :adi:`AD8605` is a single rail-to-rail input and output,
single-supply amplifier featuring very low offset voltage, low input voltage
and current noise, and wide signal bandwidth.

The :adi:`AD7171` is a very low power, 16-bit, analog-to-digital converter
(ADC). It contains a precision, 16-bit, sigma-delta ADC and an on-chip
oscillator. The measurement result from the :adi:`AD7171` is provided as a
digital code utilizing a simple 2-wire, SPI-compatible serial interface.

The :adi:`ADuM5402 <ADUM5402>` is a quad channel isolator that provides
galvanic isolation for the circuit. This is not only for protection but to
isolate the downstream circuitry from the high common-mode voltage. In addition
to isolating the output data, the digital isolator can also supply isolated
+3.3 V for the circuit. The :adi:`ADR381` is a precision 2.500 V band gap
voltage reference featuring high accuracy, high stability, and low power
consumption in a tiny footprint. It is a micropower, low dropout voltage (LDV)
device that provides a stable output voltage from supplies as low as 300 mV
above the output voltage.

The EVAL-CN0218-SDPZ connects to ADI's System Demonstration Platform (SDP)
and is powered by a +6 V supply or +6 V wall wart.

.. warning::

   **High voltage!** This circuit may contain lethal voltages. **Do not**
   operate, evaluate, or test this circuit, or board assembly, unless you are
   a trained professional, who is qualified to handle high voltage circuitry.
   Before applying power, you must be familiar with the circuitry and all
   required precautions for working with high voltage circuits.

Required Equipment
------------------

- :adi:`EVAL-CN0218-SDPZ <CN0218>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0218 Evaluation Software
- +6 V DC power supply or +6 V wall wart
- USB Type-A to USB Mini-B cable
- Shunt resistor with maximum voltage of 500 mV at the maximum load current
- Electronic load
- PC with the following minimum requirements:

  - Windows 7 (32-bit), Windows Vista (32-bit), or Windows XP
  - USB interface

Hardware Setup
--------------

Block Assignments
~~~~~~~~~~~~~~~~~

- **J1** -- SDP 120-pin connector
- **J2** -- +6 V barrel connector for wall wart supply input
- **J3** -- +6 V DC power supply terminal
- **J5** -- Input terminals for shunt resistor and load to ground
- **TP31, TP32** -- GND_ISO access points

Test Setup
~~~~~~~~~~

#. Connect the 120-pin connector on the EVAL-CN0218-SDPZ to the connector
   marked **CON A** on the :adi:`EVAL-SDP-CB1Z` (SDP-B board).
#. Connect a shunt resistor across the input terminals with a load to ground.
#. With power to the supply off, connect a +6 V power supply to the pins
   marked "+6V" and "GND" on the board.

   .. note::

      If available, a +6 V wall wart can be connected to the barrel connector
      on the board and used in place of the +6 V power supply.

#. Connect the USB cable supplied with the SDP board to the USB port on the PC.
#. Apply power to the +6 V supply (or wall wart) connected to the
   EVAL-CN0218-SDPZ.
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
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0218_Evaluation_Software.zip** and open the file
   **setup.exe**.

   .. note::

      It is recommended that you install the CN0218 Evaluation Software to the
      default directory path
      ``C:\Program Files (x86)\Analog Devices\CN0218\`` and all National
      Instruments products to ``C:\Program Files\National Instruments\``.

#. Click **Next** to view the installation review page.
#. Click **Next** to start the installation.
#. Upon completion of the installation of the CN-0218 Evaluation Software, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended that you close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended that you install the drivers to the default directory
      path ``C:\Program Files\Analog Devices\SDP\Drivers``.

#. Press **Install** to install the SDP Drivers and complete the installation
   of all software. Click **Finish** when done.

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main Window
^^^^^^^^^^^

The main evaluation software window provides the following controls:

#. **Connect Button** -- Starts the connection between the CN0218 evaluation
   board and the SDP-B controller board.
#. **Reset and Disconnect** -- Resets the board and ends the connection between
   the CN0218 evaluation board and the SDP-B controller board.
#. **Stop Button** -- Stops collecting data from the CN0218 board.
#. **Test Setup Tab** -- Shows the acquired measurement data in terms of shunt
   voltage with respect to samples.

   - **Shunt Voltage** -- Shunt voltage measurement output from ADC.
   - **Click to Start Sampling** -- Starts acquisition of measurement data.
   - **Clear Data** -- Clears all data collected from the chart history.
   - **Save Data to File** -- Saves measurement data to file.

#. **Configure Tab**

   - **Flash LED** -- Flashes the LED on the SDP controller board.
   - **Read Firmware** -- Reads the firmware of the CN0218 evaluation board.

#. **Plot Options** -- Edit plot display and options like interpolation and
   color of output waveform.

Running the System
^^^^^^^^^^^^^^^^^^

#. Open the **CN0218.exe** application from the default installation location.
#. Click the **Connect** button.
#. Upon successful connection, start and control data acquisition through the
   data acquisition control buttons.
#. Output data will be shown in the graph. Edit graph through plot options and
   check boxes provided.
#. Click **Disconnect** if finished.
#. Click **Quit** to exit the program.

Documents
---------

- :adi:`CN0218 Circuit Note <CN0218>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0218-SDPZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0218-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`AD8212 Product Page <AD8212>`
- :adi:`AD7171 Product Page <AD7171>`
- :adi:`ADuM5402 Product Page <ADUM5402>`
- :adi:`AD8605 Product Page <AD8605>`
- :adi:`ADR381 Product Page <ADR381>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
