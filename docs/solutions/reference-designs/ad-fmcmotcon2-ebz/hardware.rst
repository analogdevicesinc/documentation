Hardware
========

Controller Board Key Parts
--------------------------

.. image:: controller_block_diagram_simplified.png
   :align: center

.. list-table::
   :header-rows: 1

   * - Category
     - Part
     - Description
   * - Measurement
     - :adi:`AD8137`
     - Differential ADC driver
   * - Measurement
     - :adi:`AD8646`
     - 24 MHz rail-to-rail dual op amp
   * - Measurement
     - :adi:`AD2S1210`
     - Variable resolution 10-bit to 16-bit R/D converter with reference oscillator
   * - Power
     - :adi:`ADuM5000`
     - isoPower integrated isolated DC-to-DC converter
   * - Power
     - :adi:`ADP1614`
     - 1000 mA, 2.5 MHz buck-boost DC-to-DC converter
   * - Isolation
     - :adi:`ADuM7640`
     - 1 kV RMS six-channel digital isolator
   * - Isolation
     - :adi:`ADuM1400`
     - Quad channel digital isolator
   * - Isolation
     - :adi:`ADM2486`
     - Isolated RS-485 transceiver
   * - Isolation
     - :adi:`ADuM1250`
     - Hot-swappable dual I2C isolator
   * - Voltage Translation
     - :adi:`ADG3308`
     - 8-channel bidirectional level translator
   * - Multiplexers
     - :adi:`ADG759`
     - CMOS low voltage, 3 Ohm 4-channel multiplexer
   * - Communication
     - :adi:`ADN4662`
     - Single, 3 V, CMOS, LVDS differential line receiver
   * - Ethernet
     - 88E1512
     - Marvell integrated 10/100/1000 Mbps EEE transceiver

Low Voltage Drive Board (AD-DRVLV2-EBZ)
----------------------------------------

The drive board connects to the controller board and provides:

- Power stage for motors up to 48 V and 20 A, driving two motors simultaneously
- Supported motor types: BLDC, PMSM, Brushed DC, Stepper (bipolar/unipolar)
- High frequency drive stage using ADI isolated gate drivers
- Integrated overcurrent and reverse voltage protection
- Current and voltage measurement using isolated ADCs

  - Current measurement on 2 phases for 2 motors
  - DC link voltage measurement

- BEMF zero-cross detection for sensorless control of PMSM or BLDC motors
- Separate voltage supplies for the 2 motors

.. figure:: lv_block_diagram_simplified.png
   :align: center

   AD-DRVLV2-EBZ block diagram

.. list-table::
   :header-rows: 1

   * - Category
     - Part
     - Description
   * - Measurement
     - :adi:`AD7403`
     - 16-bit isolated 2nd order sigma-delta modulator
   * - Measurement
     - :adi:`AD8207`
     - Zero drift, high voltage, bidirectional difference amplifier
   * - Measurement
     - :adi:`CMP04`
     - Quad low power, precision comparator
   * - Power
     - :adi:`ADuM5000`
     - isoPower integrated isolated DC-to-DC converter
   * - Power
     - :adi:`ADP1621`
     - Constant-frequency, current-mode step-up DC/DC controller
   * - Power
     - :adi:`ADP2301`
     - 1.2 A, 20 V, 1.4 MHz non-synchronous step-down switching regulator
   * - MOSFET Drivers
     - :adi:`ADuM5230`
     - Isolated half-bridge driver with integrated high-side supply
   * - MOSFET Drivers
     - :adi:`ADuM7223`
     - Isolated precision half-bridge driver, 4.0 A output

**Drive Board Switches**

.. image:: lv_reset.png
   :align: center

- **Emergency Stop** (S2): Latching emergency stop switch. When triggered, the
  supply for the power stage is turned off.
- **Reset** (S1): Reset switch for the emergency stop latch. Pressing S1 when
  S2 is not pressed turns the power stage on.

Signal Measurement Chain
------------------------

The motor control system measures Ia (phase A current), Ib (phase B current),
and Vbus using signal chains that involve components from both the controller
and low voltage drive boards. The entire analog front end is placed on the
drive board and only digital signals are exchanged between the controller and
drive boards.

**Ia, Ib Current Measurement**

The Ia and Ib currents are sensed using 10 mOhm shunt resistors. The
:adi:`AD7403` isolated sigma-delta modulator is placed in the proximity of the
shunt resistor to reduce noise coupling. The small differential voltage on the
shunt resistor is measured directly without the need for extra interfacing and
signal conditioning circuitry. The digital data and clock signals travel the
entire length of the drive and controller boards to the FPGA, ensuring
measurement quality is not affected by the long signal path.

.. image:: current_chain.png
   :align: center

**Vbus Voltage Measurement**

Vbus sensing is done on the drive board using a resistive divider and the
:adi:`AD7403` sigma-delta modulator. The combination of the isolated
sigma-delta modulator and an analog reconstruction filter provides a convenient
way to achieve analog isolation of the XADC input signals.

.. image:: vbus_chain.png
   :align: center

Dynamometer (AD-DYNO2-EBZ)
---------------------------

The AD-DYNO2-EBZ dynamometer drive system provides:

- Two BLDC motors connected in a dyno setup
- Electronically adjustable load set using onboard buttons and LCD
- Programmable step and ramp load changes
- Measurement and display of load motor phase currents and speed
- External control and monitoring interface

.. figure:: dyno_diagram.png
   :align: center

   AD-DYNO2-EBZ block diagram

.. list-table::
   :header-rows: 1

   * - Category
     - Part
     - Description
   * - Power
     - :adi:`ADuM5000`
     - isoPower integrated isolated DC-to-DC converter
   * - Power
     - :adi:`ADP3335`
     - High accuracy ultralow quiescent current, 500 mA anyCAP LDO
   * - Isolation
     - :adi:`ADuM3223`
     - 3 kV RMS isolated precision half-bridge driver, 4 A output
   * - Control
     - :adi:`ADuC7023`
     - Precision analog microcontroller, 12-bit analog I/O, ARM7TDMI MCU

**Dynamometer User Guide**

The system is equipped with an LCD which displays information about the state of
the load. Three push buttons below the LCD are used to display and configure
system parameters. The **+/-** buttons navigate through the menu and change
parameters, while the **Enter** button confirms parameter changes or enters/
exits menu screens.

Menu structure:

- **Main Menu** -- Displayed at power up.
- **Measurement Menu** -- Displays RMS phase currents and motor speed. The load
  can be adjusted by pressing the **+** or **-** buttons. Press **Enter** to
  return to the main menu.
- **Waveforms Menu** -- Select ramp or step load.
- **Step Load Menu** -- Select **Step** to start toggling the load. Press
  **+** or **-** to toggle between preset step values.
- **Ramp Load Menu** -- Press **+** or **-** to change ramp period.
- **Settings Menu** -- Change duty cycle step and view system information.

**External Control**

To interface the dynamometer with an external control system, slide switch S2
to the EXT_CTRL position and connect to header P1.

.. image:: dyno_ext_control.png
   :align: center

.. list-table::
   :header-rows: 1

   * - Dyno Signal
     - Description
   * - I_A
     - Phase A motor current (185 mV/A)
   * - I_B
     - Phase B motor current (185 mV/A)
   * - PWM1
     - Phase A PWM (3.3 V levels)
   * - PWM2
     - Phase B PWM (3.3 V levels)
   * - PWM3
     - Phase C PWM (3.3 V levels)

The system needs a 5 V, 500 mA power supply. The power connector is a
2.1 x 5.5 mm jack with the center pin positive.

ADC FPGA Interface
------------------

The :adi:`AD7403` isolated sigma-delta modulators on the controller board use a
two-wire signal interface with the FPGA:

- 10 / 20 MHz clock input
- 1-bit digital data stream output

Data reconstruction uses a SINC3 filter. Typical filter output characteristics:

- Output code: 16 bit
- Sampling rate: 78 kHz

The output code resolution and sampling rate can be controlled by changing the
filter model and decimation ratio. Polyphase interpolation filters are used to
increase the system sampling rate.
