HDL Reference Design
====================

Two HDL reference designs are provided targeting different use cases:

- **Xilinx ISE HDL Project + Chipscope Interface** -- Simple design for manual
  control and monitoring of system parameters through Chipscope. The design
  contains ADC interface, motor controller, and speed sensor interface blocks,
  all connected to Chipscope ILA and VIO modules.
- **HDL Project for Linux** -- Design with AXI Lite and AXI Streaming
  interfaces, infrastructure for Linux support, and integration of
  automatically generated HDL code for the Simulink-designed motor controller.

.. figure:: mc_design.png
   :align: center

   Linux-targeted HDL reference design block diagram

The Linux-targeted HDL design contains the following blocks:

- **ADC Interface** -- Communicates with the :adi:`AD7401` sigma-delta
  modulators and implements SINC3 filters for demodulating the 1-bit stream.
  Exposes AXI Lite registers and an AXI Streaming interface for DMA data
  transfer.
- **Controller Interface** -- Interfaces to IP control blocks and streams
  real-time data to the application layer via AXI Streaming and DMA.
- **MathWorks FOC IP** -- FOC controller model provided by MathWorks,
  integrated as a standalone IP core packaged using the Simulink Workflow
  Advisor. Exposes AXI-Lite control registers, encoder input, current
  measurement data, inverter control, and monitoring signals. All monitoring
  signals connect to the Controller Interface IP for observation from the
  Linux IIO Oscilloscope application. The AXI-Lite registers can be directly
  accessed through a UIO driver in the ADI Linux distribution for Zynq.
- **Position and Speed Processing** -- Converts Hall, BEMF, and Encoder signals
  into speed and position data. Exposes AXI Lite registers and AXI Streaming
  interface for DMA.

Vivado Design Generation
------------------------

Start Vivado in GUI mode. Generate the project using the Vivado TCL console:

.. code-block:: tcl

   cd [project_path]/projects/motor_control/zed
   source ./system_project.tcl

This generates the complete system and creates the bitfile.

HDL Source Code
---------------

- :git-hdl:`hdl_2014_r1:projects/motor_control`
