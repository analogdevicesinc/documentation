.. _ad_fmcmotcon1_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

.. _ad_fmcmotcon1_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

The motor control system consists of three boards that work together.

.. figure:: images/ad-fmcmotcon1-ebz_top.jpg
   :alt: AD-FMCMOTCON1-EBZ controller board
   :align: center
   :width: 400

   AD-FMCMOTCON1-EBZ

:ref:`AD-FMCMOTCON1-EBZ <ad_fmcmotcon1_ebz controller-board>` - Controller
board, compatible with all Xilinx FPGA platforms with FMC LPC or HPC
connectors.

- 2x Gbit Ethernet PHYs for high-speed industrial communication
- Hall, Differential Hall, Encoder, and Resolver interfaces
- Current and voltage measurement using isolated ADCs (:adi:`AD7401A`)
- Xilinx XADC interface
- Fully isolated control and feedback signals

.. note::

   The AD-FMCMOTCON1-EBZ supports Brushed DC, BLDC, PMSM, and Stepper motors.
   For an overview of motor drive classifications (application-specific,
   standard, servo, high-performance) and the PWM, H-bridge, star/delta, and
   sensorless control techniques used in this system, see the
   :ref:`Motor Control Theory <ad_fmcmotcon1_ebz introduction>`
   page.

.. figure:: images/ad-drvlv1-ebz_top.jpg
   :alt: AD-DRVLV1-EBZ low voltage drive board
   :align: center
   :width: 400

   AD-DRVLV1-EBZ

:ref:`AD-DRVLV1-EBZ <ad_fmcmotcon1_ebz lv-board>` - Low voltage drive board.
Connects to the Controller board with a power stage that drives Brushed DC /
BLDC / PMSM / Stepper motors up to 48 V and 18 A.

- Integrated over-current protection
- Current measurement using isolated ADCs
- Bus voltage, phase currents and total current analog feedback signals
- PGAs to maximize the current measurement input range
- BEMF zero-crossing detection for sensorless control of PMSM or BLDC motors

.. figure:: images/ad-dyno1-ebz.jpg
   :alt: AD-DYNO1-EBZ dynamometer drive system
   :align: center
   :width: 400

   AD-DYNO1-EBZ

:ref:`AD-DYNO1-EBZ <ad_fmcmotcon1_ebz dyno>` - Dynamometer drive system
(optional). An electronically adjustable load for testing real-time motor
control performance.

- Two BLDC motors connected in a dyno setup
- Electronically adjustable load via onboard buttons and LCD
- Programmable step and ramp load changes
- Measurement and display of load motor phase currents and speed
- External control using Analog Discovery

Additional hardware documentation:

- :ref:`Signal measurement chain <ad_fmcmotcon1_ebz signal-chain>` - Ia/Ib,
  It, and Vbus measurement chains with signal conditioning and XADC interface
  formulas.
- :ref:`Dyno test procedure <ad_fmcmotcon1_ebz dyno>` - Step-by-step
  procedure for running dyno verification tests with IIO Oscilloscope.

.. _ad_fmcmotcon1_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

HDL reference designs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two HDL reference designs are provided for the AD-FMCMOTCON1-EBZ: a
Vivado/Linux design with full AXI infrastructure and MathWorks FOC integration,
and a simpler ISE design for manual control via Chipscope.

.. _ad_fmcmotcon1_ebz hdl-linux:

Xilinx HDL Reference Design (Linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This design targets Zynq-based FPGA systems and includes complete Linux
infrastructure. The reference design contains HDL blocks for interfacing with
the various components of the motor control hardware:

-  **ADC Interface** - Implements communication with the :adi:`AD7401`
   sigma-delta modulators on the AD-FMCMOTCON1-EBZ, including the SINC3 filters
   for demodulating the 1-bit digital stream. Exposes AXI-Lite registers and an
   AXI Streaming interface connected to a DMA controller for real-time data
   streaming to the application layer.
-  **Controller Interface** - Implements the interface to IP control blocks in
   the system. AXI Streaming interface with DMA for real-time data streaming.
-  **MathWorks FOC IP** - FOC controller model provided by MathWorks, integrated
   as a standalone IP core packaged using the Simulink Workflow Advisor. Exposes
   AXI-Lite registers for operation control and interface signals for encoder
   input, current measurement, inverter control, and monitoring. Monitoring
   signals connect to the Controller Interface IP and are accessible from IIO
   Scope. AXI-Lite registers are accessible via the UIO driver in the ADI Zynq
   Linux distribution.
-  **Position & Speed Processing** - Implements the algorithm for converting
   Hall, BEMF, and Encoder signals into speed and position data. Exposes
   AXI-Lite registers and an AXI Streaming interface with DMA.

.. figure:: images/mc_design.jpg
   :alt: Vivado reference design block diagram
   :align: center
   :width: 600

   Vivado reference design block diagram

**Vivado design generation**

Start Vivado in GUI mode on a Windows host and run from the TCL console:

.. code-block::

   cd [project_path]/projects/motor_control/zed
   source ./system_project.tcl

This generates the entire system and creates the bitfile. For instructions on
how to set up Linux on the ZedBoard, see the
:ref:`Linux on Zynq Quick Start Guide <ad_fmcmotcon1_ebz zedboard_quickstart>`.

.. _ad_fmcmotcon1_ebz hdl-ise:

Xilinx ISE HDL Reference Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This design targets Zynq-based FPGA systems. The reference design contains
HDL blocks for interfacing with the various components of the motor control
hardware:

-  **ADC Interface** - Implements communication with the :adi:`AD7401` sigma-delta
   modulators on the AD-FMCMOTCON1-EBZ and the SINC3 filters for demodulating
   the 1-bit digital stream.
-  **Controller** - Implements the motor control algorithm, designed and
   simulated in Simulink (MathWorks) and translated to HDL using the MathWorks
   HDL Coder.
-  **Speed Sensor Interface** - Implements the algorithm for converting Hall,
   BEMF, and Encoder signals into speed and position data.

All HDL blocks connect to Chipscope ILA and VIO modules which provide the
means to monitor and control their operation. Details about the Chipscope
interface and how to run the ISE project can be found in the
:ref:`ISE Project with Chipscope Quick Start Guide
<ad_fmcmotcon1_ebz chipscope_quickstart>`.

Linux software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software suite for Linux consists of:

- :external+kuiper:doc:`Kuiper Linux <index>` - includes IIO subsystem drivers
  for the motor control solution (see driver table below).
- :ref:`iio-oscilloscope` - Graphical monitoring and control of the motor
  drive system.

.. _ad_fmcmotcon1_ebz linux-drivers:

IIO drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 15 40 45

   * - Driver
     - Description
     - Channels
   * - ``ad-mc-adc``
     - Controller board ADCs
     - CH1 Ia, CH2 Ib, CH3 It, CH4 Vbus
   * - ``ad-mc-adc2``
     - Low voltage drive board ADCs
     - CH1 Ia, CH2 Ib, CH3 It
   * - ``ad-mc-speed``
     - Speed and position processing block
     - CH1 Speed measurement
   * - ``ad-mc-ctrl``
     - Motor controller block
     - CH1-CH8 controller monitoring signals

.. _ad_fmcmotcon1_ebz iio-scope:

IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The IIO Oscilloscope has two main tabs: **Capture** and **Motor Control**.

**Current monitoring (Capture tab)**

Controller board ADC channels (signal pre-amplified on the Low Voltage Drive
board; amplification controlled by GPO0 and GPO1):

- ``in_voltage0`` - IA
- ``in_voltage1`` - IB
- ``in_voltage2`` - IT
- ``in_voltage3`` - VBUS

.. figure:: images/mc_adc1_sc.jpg
   :align: center
   :width: 600

   Current measurement - controller board ADCs

Low voltage drive board ADC channels (signal not pre-amplified):

- ``in_voltage0`` - IA
- ``in_voltage1`` - IB
- ``in_voltage2`` - IT

.. figure:: images/mc_adc2_sc.jpg
   :align: center
   :width: 600

   Current measurement - drive board ADCs

**Speed monitoring (Capture tab)**

The speed IP reports the number of counts (in 10 ns units) between two motor
commutations. To display speed in RPM, enable the **1/x** option and multiply
by **25,000,000**.

.. figure:: images/mc_speed_sc.jpg
   :align: center
   :width: 600

   Speed measurement

**Manual Control (Motor Control tab)**

.. figure:: images/mc_manual_ctrl.jpg
   :align: center
   :width: 400

   Manual control interface

.. list-table::
   :header-rows: 1

   * - Control
     - Description
   * - Run
     - Starts the motor
   * - Delta
     - Star-like vs Delta commutation sequence
   * - Direction
     - Clockwise / counterclockwise rotation
   * - Controller Type
     - Manual PWM drive or :ref:`MathWorks FOC Controller <ad_fmcmotcon1_ebz matlab-models>`
   * - PWM
     - In Manual mode, settable between 50%-100%

**Matlab Controller (Motor Control tab)**

Selects the :ref:`MathWorks FOC IP <ad_fmcmotcon1_ebz matlab-models>`.

.. figure:: images/mc_foc_ctrl.jpg
   :align: center
   :width: 500

   Matlab FOC controller interface

Advanced control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Simulink controller models <ad_fmcmotcon1_ebz matlab-models>` - FOC
(field-oriented control) controller generated from a MathWorks Simulink model
using HDL Coder and integrated into the Vivado HDL design via AXI-Lite.

.. _ad_fmcmotcon1_ebz qdesys-ip:

QDESYS Motor Control IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A FOC implementation targeted for the AD-FMCMOTCON1-EBZ is available from
`QDESYS <http://www.qdesys.com/>`_. The control algorithm is provided as a
highly optimized IP that can be integrated in the FPGA project. Below are
screenshots from the user application provided with the IP, taken while running
with the AD-FMCMOTCON1-EBZ.

.. figure:: images/qdesys_main_panel.jpg
   :alt: QDESYS main panel
   :align: center
   :width: 400

   QDESYS main panel

.. figure:: images/qdesys_pwm_panel.jpg
   :alt: QDESYS PWM control panel
   :align: center
   :width: 400

   QDESYS PWM control panel

.. figure:: images/qdesys_current_settings.jpg
   :alt: QDESYS current settings panel
   :align: center
   :width: 400

   QDESYS current settings panel

.. figure:: images/qdesys_rpfm_panel.jpg
   :alt: QDESYS RPFM control panel
   :align: center
   :width: 400

   QDESYS RPFM control panel

.. figure:: images/qdesys_currents.jpg
   :alt: QDESYS phase currents plot
   :align: center
   :width: 400

   QDESYS phase currents plot

.. figure:: images/qdesys_currents_xy.jpg
   :alt: QDESYS stator currents vs space plot
   :align: center
   :width: 400

   QDESYS stator currents vs space plot

.. toctree::
   :hidden:

   reference/controller_board
   reference/lv_board
   reference/signal_chain
   reference/dyno
   reference/background
   reference/matlab_models
