.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0204

.. _eval-cn0204-sdpz:

EVAL-CN0204-SDPZ
=================

High Voltage Programmable Analog Output.

Overview
--------

:adi:`CN0204` is a full-function, high voltage (up to 44 V), flexible,
programmable analog output solution that meets most requirements for
programmable logic controller (PLC) and distributed control system (DCS)
applications. It provides all the typical voltage and current output ranges
with 16-bit resolution and no missing codes, 0.05% linearity, and less than
0.2% total output error. Furthermore, it also contains key features for
industrial applications, such as on-chip output fault detection, CRC checking
to prevent packet error (PEC), and flexible power-up options, making it an
ideal choice for robust industrial control systems. No external precision
resistors or calibration routines are needed to maintain consistent
performance in mass production, thereby making it ideal for PLC or DCS
modules.

The :adi:`AD5751` is a single-channel, low-cost, precision voltage/current
output driver developed to meet the requirements of industrial process control
applications. The :adi:`AD5751` is specified to operate with a power supply
range from 10.8 V to 55 V, and the voltage output can be up to 44 V. The
voltage output range can be programmed for the standard output ranges and 20%
overrange settings for PLC and DCS applications: 0 V to 5 V, 0 V to 10 V,
0 V to 6 V, 0 V to 12 V. In addition, two high voltage output ranges are
also provided: 0 V to 40 V and 0 V to 44 V. The current output, which is
provided on a separate pin, can be programmed for the standard ranges of
4 mA to 20 mA, 0 mA to 20 mA, 0 mA to 24 mA. There is also a 2% overrange
setting which provides 3.92 mA to 20.4 mA, 0 mA to 20.4 mA, and 0 mA to
24.5 mA. The voltage and current output pins can be tied together to configure
the end system as a single-channel output if desired.

The :adi:`AD5662` is a low-power (0.75 mW typical at 5 V), rail-to-rail
output, 16-bit nanoDAC device. The :adi:`AD5662` guarantees +/-1 LSB DNL
under a wide range of reference voltages that can vary from 0.75 V to the VDD
supply. In this circuit, the :adi:`AD5751` and :adi:`AD5662` operate from a
common reference source of 4.096 V, provided by the :adi:`ADR444`.

The :adi:`ADuM1301 <ADUM1301>` and :adi:`ADuM5401 <ADUM5401>` provide all the
necessary signal isolation between the microcontroller and the analog signal
chain. They are both based on the iCoupler technology. Additionally, the
ADuM5401 provides an isolated 5 V power supply for all the circuit on the
secondary side.

Devices for PLC and DCS applications generally need ESD protection and
overvoltage protection much higher than the formal recommended specifications.
Thus, external 64 V, 1500 W transient voltage suppressors (TVS); a 50 mA,
30 V PolySwitch; and power Schottky diodes are built into the EVAL-CN0204-SDPZ
circuit board to provide higher voltage ESD protection, 50 mA overcurrent, and
64 V overvoltage protection.

.. figure:: cn0204_board.jpg
   :width: 600px
   :align: center

   EVAL-CN0204-SDPZ evaluation board

Required Equipment
------------------

- :adi:`EVAL-CN0204-SDPZ <CN0204>` evaluation board
- :adi:`EVAL-SDP-CB1Z` controller board (SDP-B board)
- CN0204 Evaluation Software
- +/-25 V/1 A triple output DC power supply (Agilent E3631A or equivalent)
- Digital multimeter for verification (optional, Agilent 34401A)
- USB cable
- PC with USB interface running Windows 7 or higher

Hardware Setup
--------------

Block Assignments
~~~~~~~~~~~~~~~~~

.. figure:: cn0204_block_diagram.png
   :width: 600px
   :align: center

   EVAL-CN0204-SDPZ block assignments

- The EVAL-CN0204-SDPZ (CN0204 Board) connects to the :adi:`EVAL-SDP-CB1Z`
  (SDP-B Board) via the 120-pin connector (SDP CONN).
- The :adi:`EVAL-SDP-CB1Z` (SDP-B Board) connects to the PC via the USB
  cable.
- Terminal block **CN1** is the current output.
- Terminal block **CN2** is the +6 V power supply input.
- Terminal block **CN3** is the +/-50 V power supply input.

  - Connect the **+25 V** power supply to the **12-50 VIN** terminal.
  - Connect the **-25 V** power supply to the **GND_ISO** terminal.

- Terminal block **CN4** is the voltage output.

  - **Optionally**, if **JP3** is open, the output voltage feedback can be
    configured by connecting **VSENSE+** to a selected node in the load
    circuit.

.. important::

   Power on the EVAL-CN0204-SDPZ through the triple output power supply and
   the SDP-B board through the PC **separately** before connecting the two
   boards together.

Jumper Settings
~~~~~~~~~~~~~~~

See the table in the image below for the jumper settings. Values in red are
the default settings for the EVAL-CN0204-SDPZ.

.. figure:: cn0204_jumper_settings.jpg
   :width: 600px
   :align: center

   EVAL-CN0204-SDPZ jumper settings

Key jumpers include:

- **JP1** -- SPI address configuration for the AD5751.
- **JP3** -- VSENSE+ configuration (closed by default for local sense).

Software Setup
--------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract **CN0204 Evaluation Software** and open **setup.exe**.

   .. note::

      It is recommended to install the software to the default path
      ``C:\Program Files (x86)\Analog Devices\CN0204\`` and all National
      Instruments products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0204_install_step1.png
      :width: 600px

      CN0204 installer welcome screen

#. Press **Next** to view the installation review page.

   .. figure:: cn0204_install_step2.png
      :width: 600px

      Installation review page

#. Press **Next** to start the installation.

   .. figure:: cn0204_install_step3.png
      :width: 600px

      Installation progress

#. Upon completion of the CN0204 Evaluation Software installation, the
   installer for the ADI SDP Drivers will execute.

   .. note::

      It is recommended to close all other applications before clicking
      **Next**. This will make it possible to update relevant system files
      without having to reboot your computer.

   .. figure:: cn0204_sdp_drivers.png
      :width: 600px

      ADI SDP Drivers installer

#. Press **Next** to set the installation location for the SDP Drivers.

   .. note::

      It is recommended to install the drivers to the default path
      ``C:\Program Files\Analog Devices\SDP\Drivers``.

   .. figure:: cn0204_driver_directory.png
      :width: 600px

      SDP Drivers installation directory

#. Press **Next** to install the SDP Drivers. When prompted by Windows
   Security, press **Install**.

   .. figure:: cn0204_windows_security.png
      :width: 600px

      Windows Security driver installation prompt

#. Press **Finish** to complete the installation.

   .. figure:: cn0204_install_complete.png
      :width: 600px

      Installation complete

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main Window
^^^^^^^^^^^

.. figure:: cn0204_software_main.jpg
   :width: 600px
   :align: center

   CN0204 evaluation software main window

The evaluation software provides the following controls and sections:

**Title Bar:**

- **Connect** button -- Starts the connection with the CN0204 evaluation
  board.
- **Disconnect** button -- Ends the connection with the CN0204 evaluation
  board.

**System Configuration:**

- **Connector** -- Selects which 120-pin connection of the SDP-B board to
  use.
- **SCLK (Hz)** -- Sets the SPI clock frequency used by the evaluation
  board.

**AD5751 Configuration:**

- **JP1 Configuration** -- Sets the SPI address of the AD5751 based on the
  position of JP1.
- **Range Select** -- Sets the voltage/current output range.
- **Toggle CLEAR** -- Sets the outputs to the zero/midscale voltage value or
  the minimum value of the selected current range.

**AD5751 Error Indicator:**

- **Vout Fault** -- There is a short circuit on the VOUT pin.
- **Iout Fault** -- There is an open circuit on the IOUT pin.
- **Over Temp** -- The AD5751 core temperature exceeds 150 degrees C.
- **PEC Error** -- CRC-8 error checking detected an interface error.

**Output Setting:**

- **Write AD5662** -- Writes the hexadecimal value in the left field to the
  AD5662 output voltage.
- **Reset AD5751** -- Resets the AD5751 to its power-on state.

**Quit** -- Exits the software application.

Running the System
^^^^^^^^^^^^^^^^^^

#. Open the **CN0204.exe** application from the default installation
   location.
#. Set the correct connector and SCLK settings for the board in the System
   Configuration section.
#. Click the **Connect** button.
#. Upon successful connection, select the desired range of output on the
   Range Select drop-down menu.
#. Input a hex value equivalent of the desired output level in the Output
   Setting section.
#. Click **Write AD5662**.
#. Click **Disconnect** if finished.

Documents
---------

- :adi:`CN0204 Circuit Note <CN0204>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0204-SDPZ Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0204-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`AD5751 Product Page <AD5751>`
- :adi:`AD5662 Product Page <AD5662>`
- :adi:`ADR444 Product Page <ADR444>`
- :adi:`ADuM5401 Product Page <ADUM5401>`
- :adi:`ADuM1301 Product Page <ADUM1301>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
