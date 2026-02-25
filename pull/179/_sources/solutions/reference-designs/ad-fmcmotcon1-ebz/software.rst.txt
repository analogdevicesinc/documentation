Software Support
================

Linux IIO Drivers
-----------------

The Linux Industrial I/O (IIO) drivers for the motor control solution require
the HDL cores to have a specified register map. A DMA interface is set up for
high-speed data transfer using multiple multiplexed data channels.

.. list-table::
   :header-rows: 1

   * - IIO Driver
     - Description
     - Channels
   * - **ad-mc-adc**
     - Controller board ADC driver
     - CH1: Ia, CH2: Ib, CH3: It, CH4: Vbus
   * - **ad-mc-adc2**
     - Low voltage drive board ADC driver
     - CH1: Ia, CH2: Ib, CH3: It
   * - **ad-mc-speed**
     - Speed and position processing block
     - CH1: Speed measurement
   * - **ad-mc-ctrl**
     - Motor controller block
     - CH1--CH8: Controller monitoring signals

Example device tree entries for the motor control IIO drivers:

.. code-block:: none

   ad-mc-adc@40500000 {
       compatible = "xlnx,axi-ad-mc-adc-1.00.a";
       reg = <0x40500000 0x10000>;
       dmas = <&axi_dma_0 0>;
       dma-names = "ad-mc-adc-dma";
   };

   axi_dma_1: axidma1@40420000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40420000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 54 0>;
       clocks = <&clkc 16>;
       dma-channel {
           adi,buswidth = <32>;
           adi,type = <0>;
       };
   };

   ad-mc-ctrl@40520000 {
       compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
       reg = <0x40520000 0x10000>;
       dmas = <&axi_dma_1 0>;
       dma-names = "ad-mc-ctrl-dma";
   };

   axi_dma_2: axidma2@40410000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40410000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 56 0>;
       clocks = <&clkc 16>;
       dma-channel {
           adi,buswidth = <32>;
           adi,type = <0>;
       };
   };

   ad-mc-speed@40510000 {
       compatible = "xlnx,axi-ad-mc-speed-1.00.a";
       reg = <0x40510000 0x10000>;
       dmas = <&axi_dma_2 0>;
       dma-names = "ad-mc-speed-dma";
   };

   axi_dma_3: axidma3@40430000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40430000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 53 0>;
       clocks = <&clkc 16>;
       dma-channel {
           adi,buswidth = <64>;
           adi,type = <0>;
       };
   };

   ad-mc-adc2@40530000 {
       compatible = "xlnx,axi-ad-mc-adc-1.00.a";
       reg = <0x40530000 0x10000>;
       dmas = <&axi_dma_3 0>;
       dma-names = "ad-mc-adc-dma";
   };

IIO Oscilloscope
----------------

The ADI IIO Oscilloscope application is used for monitoring and controlling the
AD-FMCMOTCON1-EBZ board when using the Linux operating system. Two main tabs
are used: **Capture** and **Motor Control**.

**Capture -- Current Monitoring**

Two sets of :adi:`AD7401A` ADCs provide current monitoring:

- Controller board ADCs (``ad-mc-adc``): in_voltage0 = Ia, in_voltage1 = Ib,
  in_voltage2 = It, in_voltage3 = Vbus. The signal is pre-amplified on the
  drive board; amplification controlled by GPO0 and GPO1 pins.
- Drive board ADCs (``ad-mc-adc2``): in_voltage0 = Ia, in_voltage1 = Ib,
  in_voltage2 = It (no preamplification).

**Capture -- Speed Monitoring**

The speed IP monitors the number of counts (in 10 ns units) between two motor
commutations. To display speed in RPM, enable the 1/x option and multiply by
25,000,000.

.. image:: mc_speed_sc.png
   :align: center

**Capture -- FOC Controller Monitoring**

The MathWorks FOC IP exposes the following monitoring signals:

- voltage_0 / voltage_1: Phase A / B voltage
- voltage_2 / voltage_3: Phase A / B current
- voltage_4: Rotor mechanical position
- voltage_5: Rotor velocity
- voltage_6 / voltage_7: d / q current

.. image:: mc_full_sc.png
   :align: center

**Motor Control -- Manual Control**

.. image:: mc_manual_ctrl.png
   :align: center

.. list-table::
   :header-rows: 1

   * - Control
     - Description
   * - Run
     - Starts the motor
   * - Delta
     - Selects between Star and Delta commutation sequence
   * - Direction
     - Selects clockwise or counterclockwise rotation
   * - Controller Type
     - Selects between Manual PWM drive or MathWorks FOC controller
   * - PWM
     - In manual mode, sets PWM between 50%--100%

**Motor Control -- MathWorks FOC Controller**

When the MathWorks FOC controller is selected, the ``foc_script.sh`` script
(located under ``/usr/local/bin/``) controls operation:

1. Sets the FOC controller to open loop mode and waits for the user to start
   the motor by clicking Run in IIO Scope.
2. Calibrates encoder readings to remove the offset between actual electrical
   position and encoder position.
3. Sets the motor reference speed.
4. Starts the FOC controller in closed loop mode.

Simulink Models
---------------

The Vivado HDL design includes an integrated FOC and speed/torque controller
generated from a MathWorks Simulink model. The controller is designed in
Simulink and the corresponding HDL code is generated using the MathWorks HDL
Coder. The controller model is packaged into an IP core using the Simulink
Workflow Advisor.

.. figure:: foc_simulink.png
   :align: center

   Top-level diagram of the FOC controller Simulink model

FOC Controller AXI-Lite Registers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Register
     - Address
     - Format
     - Type
     - Description
   * - axi_controller_mode
     - 0x100
     - 2-bit word
     - W
     - Operation mode: 3=open loop, 2=closed loop, 1=standby
   * - axi_command
     - 0x104
     - Signed fixed 18.8
     - W
     - Motor reference speed in rad/s
   * - axi_velocity_p_gain
     - 0x108
     - Signed fixed 18.16
     - W
     - Proportional gain of velocity PI controller
   * - axi_velocity_i_gain
     - 0x10C
     - Signed fixed 18.15
     - W
     - Integral gain of velocity PI controller
   * - axi_current_p_gain
     - 0x110
     - Signed fixed 18.10
     - W
     - Proportional gain of current PI controller
   * - axi_current_i_gain
     - 0x114
     - Signed fixed 18.12
     - W
     - Integral gain of current PI controller
   * - axi_open_loop_bias
     - 0x118
     - Signed fixed 18.14
     - W
     - Open loop control command bias
   * - axi_open_loop_scalar
     - 0x11C
     - Signed fixed 18.16
     - W
     - Open loop control command gain
   * - axi_encoder_zero_offset
     - 0x120
     - Signed fixed 18.14
     - W
     - Encoder offset
   * - axi_electrical_pos_err
     - 0x124
     - Signed fixed 19.14
     - R
     - Error between actual and encoder electrical position

FOC Controller Interface Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Signal
     - Direction
     - Width
     - Format
     - Description
   * - adc_current1
     - I
     - 18
     - Signed fixed 18.17
     - Phase A current measurement
   * - adc_current2
     - I
     - 18
     - Signed fixed 18.17
     - Phase B current measurement
   * - encoder_a
     - I
     - 1
     - Boolean
     - Encoder channel A
   * - encoder_b
     - I
     - 1
     - Boolean
     - Encoder channel B
   * - encoder_index
     - I
     - 1
     - Boolean
     - Encoder index
   * - pwm_a
     - O
     - 1
     - Boolean
     - Phase A PWM control signal
   * - pwm_b
     - O
     - 1
     - Boolean
     - Phase B PWM control signal
   * - pwm_c
     - O
     - 1
     - Boolean
     - Phase C PWM control signal
   * - mon_phase_voltage_a
     - O
     - 32
     - Signed fixed 32.12
     - Phase A voltage in Volts
   * - mon_phase_voltage_b
     - O
     - 32
     - Signed fixed 32.12
     - Phase B voltage in Volts
   * - mon_phase_current_a
     - O
     - 32
     - Signed fixed 32.15
     - Phase A current in Amps
   * - mon_phase_current_b
     - O
     - 32
     - Signed fixed 32.15
     - Phase B current in Amps
   * - mon_rotor_position
     - O
     - 32
     - Signed fixed 32.14
     - Rotor mechanical position in radians
   * - mon_electrical_position
     - O
     - 32
     - Signed fixed 32.14
     - Rotor electrical position in radians
   * - mon_rotor_velocity
     - O
     - 32
     - Signed fixed 32.8
     - Rotor velocity in rad/s
   * - mon_d_current
     - O
     - 32
     - Signed fixed 32.15
     - d current in Amps
   * - mon_q_current
     - O
     - 32
     - Signed fixed 32.15
     - q current in Amps

QDESYS Motor Control IP
------------------------

A Field Oriented Control (FOC) implementation for the AD-FMCMOTCON1-EBZ is
available from `QDESYS <http://www.qdesys.com/>`__. The control algorithm is
provided as a highly optimized IP core that can be integrated in the FPGA
project.

Support
-------

If you have any questions regarding the AD-FMCMOTCON1-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
