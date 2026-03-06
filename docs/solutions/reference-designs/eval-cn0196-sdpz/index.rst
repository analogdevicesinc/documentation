.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0196

.. _eval-cn0196-sdpz:

EVAL-CN0196-SDPZ
=================

Isolated H-Bridge Gate Driver with PWM Control.

Overview
--------

:adi:`CN0196` is an H-bridge composed of high-power switching MOSFETs that are
controlled by low-voltage logic signals. The circuit provides a convenient
interface between logic signals and the high-power bridge. The bridge uses low
cost N-channel power MOSFETs for both the high and low sides of the H-bridge.
The circuit also provides galvanic isolation between the control side and power
side. This circuit can be used in motor control, power conversion with embedded
control interface, lighting, audio amplifiers, and uninterruptible power
supplies (UPS).

.. figure:: cn0196_board.png
   :align: center

   EVAL-CN0196-EB1Z Evaluation Board

Modern microprocessors and micro converters are generally low power and operate
on low supply voltages. Source and sink current for 2.5 V CMOS logic outputs
ranges from uA to mA. Driving an H-bridge switching 12 V with a 4 A peak
current requires the use of carefully selected interface and level translation
components, especially if low jitter is needed.

The :adi:`ADG787` is a low voltage CMOS device that contains two independently
selectable single-pole double-throw (SPDT) switches. With a 5 V DC power
supply, a voltage as low as 2 V is a valid high input logic voltage. Therefore,
the :adi:`ADG787` provides appropriate level translation from the 2.5 V
controlling signal to the 5 V logic level needed to drive the
:adi:`ADuM7234 <ADUM7234>` half-bridge driver.

The :adi:`ADuM7234 <ADUM7234>` is an isolated, half-bridge gate driver that
employs Analog Devices' iCoupler technology to provide independent and isolated
high-side and low-side outputs making it possible to use N-channel MOSFETs
exclusively in the H-bridge. There are several benefits in using N-channel
MOSFETs: N-channel MOSFETs typically have one third of the on resistance of
P-channel MOSFETs and higher maximum current; they switch faster, thereby
reducing power dissipation; and the rise time and fall time is symmetrical.

The 4 A peak drive current of the ADuM7234 ensures that the power MOSFETs can
switch on and off very fast, thereby minimizing the power dissipation in the
H-bridge stage. The maximum drive current of the H-bridge in this circuit can
be up to 85 A, which is limited by the maximum allowable MOSFET current.

The :adi:`ADuC7061 <ADUCM360>` is a low power, ARM7-based precision analog
microcontroller with integrated pulse width modulated (PWM) controllers that
have outputs that can be configured to drive an H-bridge after suitable level
translation and conditioning.

.. figure:: cn0196_block_diagram.png
   :align: center

   CN0196 Test Setup Functional Block Diagram

Required Equipment
------------------

- EVAL-CN0196-EB1Z circuit evaluation board
- EVAL-ADuC7061-MKZ evaluation board
- DC supply or battery: +12 V, 10 A
- Load (e.g., Coilcraft SER2014-402 power inductor)
- Oscilloscope with current probe
- USB cable
- PC with Windows XP, Windows Vista (32-bit), or Windows 7 (32-bit)

Hardware Setup
--------------

General Setup
~~~~~~~~~~~~~

- Connect the controlling signals from the EVAL-ADuC7061 and CN0196 according
  to the jumper configuration found in the Connectors and Jumper
  Configurations section below.
- Connect the jumpers: **LK1** pin 1 and 2, **LK2** pin 2 and 3, **LK3** pin
  1 and 2, and short **LK4** pin.
- Apply +12 V power supply to **J4** of the CN0196 board.
- Connect the USB cable from the PC to the USB mini connector on the
  EVAL-ADuC7061-MKZ board.
- Connect an inductor as a load between **OUT1** and **OUT2** of **J3**.

Connectors and Jumper Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0196_connectors.png
   :align: center

   EVAL-CN0196-EB1Z Connectors and Jumper Locations

**Switch S1**: ON state provides isolated side PWM pulses; OFF state makes the
PWM disappear.

**Jumper Link LK1**: Shorting pin 1 and 2 sets the source terminal of the
ADG787 to 5 V; shorting pin 2 and 3 sets to 0 V.

**Header J1**: Provides connection of the controlling signals between
EVAL-CN0196-EB1Z and EVAL-ADuC7061-MKZ as shown in the table below.

.. list-table::
   :header-rows: 1

   * - EVAL-ADuC7061-MKZ
     - EVAL-CN0196-EB1Z
   * - PWRIN J1-1
     - +5V_2 J1-1
   * - GND J1-2
     - GND2 J1-2
   * - PWM1 J2-25
     - PWM1_I J1-4
   * - PWM0 J2-26
     - PWM0_I J1-5
   * - DVDD J2-28
     - +2V5 J1-3

**Jumper Link LK2**: Shorting pin 1 and 2 sets the source terminal of the
ADG787 to 5 V; shorting pin 2 and 3 sets to 0 V.

**Jumper Link LK3**: If pin 1 and 2 is shorted, disabling the ADuM7234 for
under voltage condition is generated on board. Shorting pin 2 and 3 will
provide externally disabling the isolator via J1-6 header.

**Connector J3**:

.. list-table::
   :header-rows: 1

   * - Pin Number
     - Description
   * - J3-1
     - VDD: Power supply of the load
   * - J3-2
     - VDD: Power supply of the load
   * - J3-3
     - OUT1: Connection of the inductor load
   * - J3-4
     - OUT2: Connection of the inductor load
   * - J3-5
     - GND: Ground connection
   * - J3-6
     - GND: Ground connection

**Connector J4**: Connects +12 V power supply and ground return.

**Connector J2**: Connection of an external supply up to +20 V if jumper link
LK4 is not shorted.

**Jumper Link LK4**: Shorting this pin sets the VDD voltage to +12 V.

Software Setup
--------------

Software and Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the file **CN0196 Eval Software.zip** and open **setup.exe**.

   .. note::

      It is recommended that you install the CN0196 SDP Evaluation Software to
      the default directory path
      ``C:\Program Files\Analog Devices\CN0196\`` and all National Instruments
      products to ``C:\Program Files\National Instruments\``.

   .. figure:: cn0196_license_agreement.png
      :align: center

      CN0196 Software License Agreement

#. Follow the on-screen prompts to install the software.

Downloading Firmware to EVAL-ADuC7061-MKZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the EVAL-ADuC7061-MKZ to the PC using a USB cable, then find the
   COM port assigned to this board in the Device Manager.

   .. figure:: cn0196_device_manager.png
      :align: center

      Device Manager Showing USB Serial Port Assignment

#. Open the software **ARMWSD.exe** located in the ARMWSD folder, or at
   ``C:\Program Files\Analog Devices\CN0196\ARMWSD\ARMWSD.exe``.

   .. figure:: cn0196_armwsd.png
      :align: center

      ARMWSD Firmware Download Tool

#. Click the **Configure** button. Go to the **Parts** tab and select
   **ADuC7061**. Go to the **Comms** tab and set the serial port according to
   the port number indicated in the PC Device Manager and set the baud rate
   to 9600.

   .. figure:: cn0196_armwsd_configure.png
      :align: center

      ARMWSD Configure Dialog -- Parts and Comms Tabs

#. Change to the **Commands** tab and set the Flash and Run selection.

   .. figure:: cn0196_armwsd_commands.png
      :align: center

      ARMWSD Configure Dialog -- Commands Tab

#. After setting the configuration, click **Browse** and select the file
   **PWM Generator for EVAL-CN0196-EB1Z.hex** found in the EVAL-ADuC7061-MKZ
   Firmware folder. Then click **Start**. A message will tell how to download
   the firmware: press **S2** on the EVAL-ADuC7061-MKZ and hold it down, then
   click **S1** on the EVAL-ADuC7061-MKZ. After the downloading process shows
   "Flashing Complete", click the **Run** button.

   .. figure:: cn0196_armwsd_download.png
      :align: center

      ARMWSD Firmware Download and Flashing Process

Using the Evaluation Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation software front panel provides the following controls:

.. figure:: cn0196_software_pwm.png
   :align: center

   CN0196 Evaluation Software -- PWM Configuration Tab

.. figure:: cn0196_software_load.png
   :align: center

   CN0196 Evaluation Software -- Load Configuration Tab

**Section 1 -- Connection Controls**

- **Connect** -- Sets up connection between EVAL-CN0196-EB1Z and
  EVAL-ADuC7061-MKZ.
- **Disconnect** -- Disconnects the hardware.
- **STOP APP** -- Closes the CN0196 evaluation software.

**Section 2 -- PWM Controls**

- **PWM Pulse Width** -- Sets the PWM pulse width up to 12.8 ms.

  .. note::

     Pulse width should be less than half of the pulse interval.

- **PWM Interval** -- Sets the PWM interval up to 12.8 ms depending on the
  configured PWM pulse width.
- **Start/Stop** -- Provides continuous and discontinuous pulses.
- **High Side Shot** -- When pressed, the PWM waveform will display the
  voltage on the high side MOSFETs Q1 and Q2.
- **Low Side Shot** -- When pressed, the PWM waveform will display the voltage
  on the low side MOSFETs Q3 and Q4.
- **Reset** -- Resets all the configuration and hardware connection.

**Section 3 -- PWM Waveform Display**: Displays the PWM waveform (V) vs.
Time (s) depending on the configuration set on the PWM controls.

**Section 4 -- Status Display**: Displays the current status/activity being
performed in the software.

**Section 5 -- Load Controls**

- **VDD** -- Controls the supply voltage up to 20 V.
- **Inductor** -- Controls the inductor value up to 100 mH to be used as a
  load.

**Section 6 -- Inductor Waveform Display**: Displays the Inductor (A) vs.
Time (s) waveform.

Documents
---------

- :adi:`CN0196 Circuit Note <CN0196>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0196-EB1Z Design & Integration Files
   <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/CN0196-DesignSupport.zip>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - PADS Project

Additional Information
----------------------

- :adi:`ADG787 Product Page <ADG787>`
- :adi:`ADuM7234 Product Page <ADUM7234>`
- :adi:`ADuC7061 Product Page <ADUCM360>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
