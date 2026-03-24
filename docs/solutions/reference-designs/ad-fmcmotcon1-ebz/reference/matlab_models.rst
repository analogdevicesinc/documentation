.. _ad_fmcmotcon1_ebz matlab-models:

Simulink Controller Models
===============================================================================

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

The Vivado HDL design is provided with an integrated FOC and speed & torque
controller generated from a Simulink model provided by MathWorks. The
controller is designed in Simulink and the corresponding HDL code is generated
using the MathWorks HDL Coder.

Field Oriented Controller (FOC)
-------------------------------------------------------------------------------

The FOC controller model is provided by MathWorks and is integrated in the
HDL design as a standalone IP core. Below is a top-level diagram of the
controller's Simulink model. For more information about the model, check the
MathWorks website.

.. figure:: ../images/foc_simulink.jpg
   :alt: FOC Simulink model — top level diagram
   :align: center
   :width: 700

   FOC Simulink model — top level diagram

The controller model is packaged into an IP core using the Simulink Workflow
Advisor. It exposes a set of AXI-Lite registers that can be used to control
the IP's operation, as well as a set of interface signals for encoder input,
current measurement data, inverter control, and internal operations monitoring.
All monitoring signals connect to an ADI IP which allows these signals to be
monitored from the Linux IIO Scope application. The AXI-Lite registers exposed
by the controller IP core can be directly accessed through a UIO driver present
in the ADI Linux distribution for Zynq.

The table below lists the exposed AXI-Lite registers.

.. list-table::
   :header-rows: 1
   :widths: 22 8 18 5 47

   * - Register name
     - Address
     - Data format
     - Type
     - Description
   * - ``axi_controller_mode``
     - 0x100
     - 2-bit word
     - W
     - Sets the controller's operation mode: 3 = open loop, 2 = closed loop,
       1 = standby.
   * - ``axi_command``
     - 0x104
     - Signed fixed point 18.8
     - W
     - Motor reference speed in rad/s.
   * - ``axi_velocity_p_gain``
     - 0x108
     - Signed fixed point 18.16
     - W
     - Proportional gain of the velocity PI controller.
   * - ``axi_velocity_i_gain``
     - 0x10C
     - Signed fixed point 18.15
     - W
     - Integral gain of the velocity PI controller.
   * - ``axi_current_p_gain``
     - 0x110
     - Signed fixed point 18.10
     - W
     - Proportional gain of the current PI controller.
   * - ``axi_current_i_gain``
     - 0x114
     - Signed fixed point 18.12
     - W
     - Integral gain of the current PI controller.
   * - ``axi_open_loop_bias``
     - 0x118
     - Signed fixed point 18.14
     - W
     - Open loop control command bias.
   * - ``axi_open_loop_scalar``
     - 0x11C
     - Signed fixed point 18.16
     - W
     - Open loop control command gain.
   * - ``axi_encoder_zero_offset``
     - 0x120
     - Signed fixed point 18.14
     - W
     - Encoder offset.
   * - ``axi_electrical_pos_err``
     - 0x124
     - Signed fixed point 19.14
     - R
     - Error between actual electrical position and encoder position.

Execute the following steps:

-  Set the FOC controller in open loop mode and wait for the user to start
   the motor by clicking the Run checkbox in IIO Scope.
-  Calibrate the encoder readings to remove the offset between the motor's
   actual electrical position and the position read from the encoder.
-  Set the motor's reference speed.
-  Start the FOC controller in closed loop mode.

The IP core exposes a set of signals for interfacing with the rest of the
system. The table below lists the exposed interface signals.

.. list-table::
   :header-rows: 1
   :widths: 22 5 6 20 47

   * - Signal name
     - Dir.
     - Width
     - Data format
     - Description
   * - ``adc_current1``
     - I
     - 18
     - Signed fixed point 18.17
     - Phase A current measurement
   * - ``adc_current2``
     - I
     - 18
     - Signed fixed point 18.17
     - Phase B current measurement
   * - ``encoder_a``
     - I
     - 1
     - Boolean
     - Encoder channel A
   * - ``encoder_b``
     - I
     - 1
     - Boolean
     - Encoder channel B
   * - ``encoder_index``
     - I
     - 1
     - Boolean
     - Encoder index
   * - ``pwm_a``
     - O
     - 1
     - Boolean
     - Phase A PWM control signal
   * - ``pwm_b``
     - O
     - 1
     - Boolean
     - Phase B PWM control signal
   * - ``pwm_c``
     - O
     - 1
     - Boolean
     - Phase C PWM control signal
   * - ``mon_phase_voltage_a``
     - O
     - 32
     - Signed fixed point 32.12
     - Phase A voltage in Volts
   * - ``mon_phase_voltage_b``
     - O
     - 32
     - Signed fixed point 32.12
     - Phase B voltage in Volts
   * - ``mon_phase_current_a``
     - O
     - 32
     - Signed fixed point 32.15
     - Phase A current in Amps
   * - ``mon_phase_current_b``
     - O
     - 32
     - Signed fixed point 32.15
     - Phase B current in Amps
   * - ``mon_rotor_position``
     - O
     - 32
     - Signed fixed point 32.14
     - Rotor mechanical position in radians
   * - ``mon_electrical_position``
     - O
     - 32
     - Signed fixed point 32.14
     - Rotor electrical position in radians
   * - ``mon_rotor_velocity``
     - O
     - 32
     - Signed fixed point 32.8
     - Rotor velocity in rad/s
   * - ``mon_d_current``
     - O
     - 32
     - Signed fixed point 32.15
     - d current in Amps
   * - ``mon_q_current``
     - O
     - 32
     - Signed fixed point 32.15
     - q current in Amps

Below is a picture containing the output of the script, the IIO Scope
settings, and a controller monitored signals plot.

.. figure:: ../images/mc_full_sc.jpg
   :alt: IIO Scope with FOC controller active
   :align: center
   :width: 700

   IIO Scope with FOC controller active
