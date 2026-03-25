Hardware
========

Motor Control Background
-------------------------

A motor drive is a system that varies the motor electrical input power to
control the shaft torque, speed, or position. Motor drives can be classified
as:

- **Application specific drive** -- designed to run a specific motor in a
  specific application (e.g., variable speed pump drive)
- **Standard drive** -- general-purpose motor speed controller for a variety
  of motors within a given power range
- **Servo drive** -- delivers accurate and high dynamic control of position,
  speed, or torque down to zero speed; typically used in automation
- **High performance servos** -- best in class accuracy and connectivity;
  typically used in CNC and pick-and-place machines

**Brushed DC Motor Control**

The Brushed DC motor is the simplest type to control. The most common
technique to vary the applied voltage is Pulse Width Modulation (PWM), where
constant-amplitude voltage pulses of varying widths are applied to the motor.
A single transistor and diode can control speed (proportional to ON duty
cycle, positive torque only). An H-bridge power circuit enables four-quadrant
control with forward/reverse motion and braking.

**Brushless DC Motor Control**

BLDC motor windings generate a trapezoidal back EMF synchronized to the rotor
magnet position. Hall effect sensors detect the rotor position and indicate
the flat-top portion for each winding's back EMF. Two commutation schemes are
supported:

- **Star connection** -- For any one segment, two windings are in the flat-top
  portion. Electronic control leaves one winding open, connects one to the
  lower DC rail, and controls the third with PWM. The PWM fill factor controls
  motor speed.
- **Delta connection** -- Two windings connect to the positive voltage supply
  and a third connects to the negative supply. PWM fill factor controls speed.

**Sensorless control** can be achieved by detecting BEMF zero crossings for
each phase. This lowers system cost and increases reliability but cannot
reliably detect zero crossings at low motor speeds.

Interfaces
----------

The controller board provides the following interfaces:

- 2x Gigabit Ethernet PHYs for industrial communication
- Hall sensor interface (single-ended and differential)
- Encoder interface
- Resolver interface
- Isolated ADC interfaces for current and voltage measurement
- Isolated Xilinx XADC interface
- BEMF zero-cross detection for sensorless BLDC/PMSM operation

All control and feedback signals are fully isolated.

Controller Board (AD-FMCMOTCON1-EBZ)
-------------------------------------

.. figure:: controller_block_diagram_simplified.png
   :align: center

   Controller board simplified block diagram

Controller Board Key Parts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Category
     - Part
     - Description
   * - Measurement
     - :adi:`AD7401A`
     - 5 kV rms isolated 2nd order sigma-delta modulator
   * - Measurement
     - :adi:`ADA4084-2`
     - 30 V, low noise, rail-to-rail I/O, low power op amp
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
   * - Power
     - :adi:`ADM660`
     - CMOS switched-capacitor voltage converter
   * - Isolation
     - :adi:`ADuM7640`
     - Triple channel digital isolator
   * - Voltage Translation
     - :adi:`ADG3308`
     - 8-channel bidirectional level translator
   * - Multiplexers
     - :adi:`ADG704`
     - CMOS, low voltage 2.5 Ohm 4-channel multiplexer
   * - Multiplexers
     - :adi:`ADG759`
     - CMOS low voltage, 3 Ohm 4-channel multiplexer
   * - Ethernet
     - 88E1512
     - Marvell integrated 10/100/1000 Mbps EEE transceiver

Low Voltage Drive Board (AD-DRVLV1-EBZ)
----------------------------------------

.. figure:: lv_block_diagram_simplified.png
   :align: center

   Low voltage drive board simplified block diagram

The drive board connects to the controller board and provides:

- Power stage for Brushed DC / BLDC / PMSM / Stepper motors up to 48 V and 18 A
- Integrated overcurrent protection
- Current measurement using isolated ADCs (:adi:`AD7401A`)
- Bus voltage, phase currents, and total current analog feedback signals
- PGAs to maximize current measurement input range
- BEMF zero-cross detection for sensorless control of PMSM or BLDC motors

Dynamometer (AD-DYNO1-EBZ)
---------------------------

.. figure:: dyno_diagram.png
   :align: center

   Dynamometer system block diagram

The AD-DYNO1-EBZ dynamometer drive system provides:

- Two BLDC motors connected in a dyno setup
- Electronically adjustable load set using onboard buttons and LCD
- Programmable step and ramp load changes
- Measurement and display of load motor phase currents and speed
- External control using Analog Discovery

ADC FPGA Interface
------------------

The :adi:`AD7401` isolated sigma-delta modulators on the controller board use a
two-wire signal interface with the FPGA:

- 10 / 20 MHz clock input
- 1-bit digital data stream output

Data reconstruction uses a SINC3 filter. Typical filter output characteristics:

- Output code: 16 bit
- Sampling rate: 78 kHz

The output code resolution and sampling rate can be controlled by changing the
filter model and decimation ratio. Polyphase interpolation filters are used to
increase the system sampling rate.

Position and Speed Sensor FPGA Interface
----------------------------------------

A single digital interface supports multiple position sensor types:

- Single-ended Hall
- Differential Hall
- BEMF
- Encoder

Three digital signals connect the hardware to the FPGA:

- Hall A / BEMF A / Encoder Channel A
- Hall B / BEMF B / Encoder Channel B
- Hall C / BEMF C / Encoder Index

Sensor selection is done with jumpers on the controller board. The hardware
conditions the analog signals and sends clean digital signals to the FPGA.
