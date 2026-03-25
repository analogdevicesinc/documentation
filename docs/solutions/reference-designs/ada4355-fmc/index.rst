.. imported from: https://wiki.analog.com/resources/eval/ada4355_evaluation_board

ADA4355-FMC
===========

ADA4355 Receive uModule Evaluation System.

Overview
--------

The :adi:`ADA4355` evaluation system enables evaluation of the :adi:`ADA4355`
receive uModule by coupling an Analog Devices evaluation board with a Xilinx
KC705 FPGA platform. The KC705 provides memory, GPIOs, and processing power
for control and data manipulation functions managed through a MATLAB-based
graphical interface.

The evaluation board features:

- Transimpedance amplifier gain adjustment
- Analog low-pass filter selection
- Laser driver circuitry with configurable current settings
- On-board high-voltage bias generator for photo detector reverse bias
- Pulse width configuration (2 ns steps, max 20 us)

Supported Devices
-----------------

- :adi:`ADA4355`

Hardware Setup
--------------

Equipment Needed
~~~~~~~~~~~~~~~~

- :adi:`ADA4355` evaluation board
- Xilinx KC705 FPGA evaluation platform
- DC2159A communication interface board
- 12 V power supply for FPGA board
- 5 V regulated supply for :adi:`ADA4355` board (user-provided)
- High-voltage supply for photo detector reverse bias (or use on-board
  generator)
- USB cable for connection to DC2159A

Software
--------

The :adi:`ADA4355` evaluation board test software provides a MATLAB-based
graphical interface for device control and data analysis.

The software requires the MATLAB Runtime engine and installs to the default
location on the host PC.

Features
~~~~~~~~

- **Device configuration**: transimpedance amplifier gain, analog low-pass
  filter selection, photo detector reverse bias voltage control
- **Laser driver control**: enable/disable, DC and pulsed laser current
  settings
- **Data capture**: sample collection and frame averaging
- **Analysis tools**: moving average filtering with adjustable window sizes,
  FFT analysis panel
- **Measurement**: dual-cursor functionality with delta calculations
- **Visualization**: zoom and pan capabilities
- **Data export**: export captured data for offline analysis

Help and Support
----------------

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
