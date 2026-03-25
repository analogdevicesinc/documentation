.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0535

.. _eval-cn0535-ardz:

EVAL-CN0535-FMCZ
=================

High-Performance Flexible Data Acquisition System.

Overview
--------

A data acquisition (DAQ) system measures real world physical phenomena such as
temperature, force, acceleration, or vibration, converting measurements into
digital values for data processing, storage, or transmission to a remote
location. A typical DAQ system is comprised of a sensor, analog filtering and
signal conditioning circuitry, an analog-to-digital converter (ADC), and digital
controller. Components for a DAQ solution are selected on a per application
basis. Some DAQ systems are designed to minimize the overall system DC error from
sensor, with fast settling filters for control-loop or multiplexed applications.
Others are designed to provide superior AC performance, with low distortion and
flat frequency response.

The :adi:`CN0535 <CN0535>` data acquisition system has simplified many of these
design challenges into a single, flexible DAQ platform which can be used across
a wide range of AC and DC applications.

The wide input voltage range, high input impedance, and high input common mode
voltage allows most sensors and signal sources to be connected directly to the
input, without additional signal conditioning. The system has a programmable gain
block for attenuation or amplification of the input signal in order to optimally
utilize the input range of the ADC.

The DC and AC performance of this system have been optimized to provide
exceptional performance across the entire analog input bandwidth. The low input
bias current minimizes the DC error due to a sensor's output impedance, and the
high common-mode rejection ratio (CMRR) minimizes the impact of common-mode
noise pickup from the environment, especially when the sensor is located far
from the DAQ system. All while carefully considering the AC effects and not
adding overall noise and distortion into the system.

The ADC has fully programmable digital filters with adjustable bandwidth and data
rate, which can be tailor fitted to specific system requirements. The system's
analog filter rejects frequencies at multiples of the sampling frequency,
eliminating aliasing concerns.

.. figure:: block_diagram.jpg
   :align: center

   CN0535 system block diagram

Key components:

- :adi:`AD7768-1` -- 24-bit sigma-delta ADC
- :adi:`LTC6373` -- Programmable gain instrumentation amplifier
- :adi:`ADA4945-1` -- Differential ADC driver
- :adi:`ADR444` -- Precision voltage reference
- :adi:`ADP2300` -- Buck converter
- :adi:`ADP7182` -- LDO regulator
- :adi:`LT3095` -- Ultralow noise LDO regulator
- :adi:`AD8628` -- Precision op amp

Hardware Setup
--------------

Equipment Required
~~~~~~~~~~~~~~~~~~

- EVAL-CN0535-FMCZ circuit evaluation board
- EVAL-SDP-CH1Z system demonstration platform board
- AP2700 signal source or equivalent
- 12 V DC power supply
- USB cable

Hardware Connection
~~~~~~~~~~~~~~~~~~~

.. figure:: hardware_setup.jpg
   :align: center

   EVAL-CN0535-FMCZ hardware setup overview

To begin using the evaluation board, take the following steps:

#. Ensure the EVAL-SDP-CH1Z system demonstration platform board is disconnected
   from the PC. Install the :adi:`AD7768-1 evaluation board software
   <EVAL-AD7768-1>`. Restart the PC after the software installation is
   complete.
#. Connect the EVAL-SDP-CH1Z system demonstration platform board to the
   EVAL-CN0535-FMCZ reference design board. The J4 connector of the
   EVAL-SDP-CH1Z connects to the receiving socket, P1, on the EVAL-CN0535-FMCZ.

   .. figure:: cn0535_sdp_connection.jpg
      :align: center
      :width: 400px

      SDP-CH1Z to CN0535 board connection

#. Ensure the evaluation boards are connected firmly together by screwing them
   together.
#. Connect the 12 V DC supply to the EVAL-SDP-CH1Z system demonstration
   platform board and then connect to the PC using the supplied USB cable.
   Choose to automatically search for the drivers for the EVAL-SDP-CH1Z if
   prompted by the operating system.
#. Launch the AD7768-1 evaluation board software from the Analog Devices
   subfolder in the Programs menu.
#. Connect the differential input to the SMB connectors (J3 and J4). P7 can
   also be used as a connection for the input if the source uses wires.

   .. figure:: input_port.jpg
      :align: center
      :width: 400px

      Differential input connections (J3, J4, and P7)

#. Click the **Sample** button on the AD7768-1 evaluation software.

Below are measured values with a 5.9 Vpp sine input from an AP2700 signal
source.

.. figure:: fft.jpg
   :align: center
   :width: 400px

   FFT measurement result

.. figure:: time_domain.jpg
   :align: center
   :width: 400px

   Time domain waveform measurement

System Gain Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the gain by configuring the switch (S2) on the EVAL-CN0535-FMCZ board.
The following table shows the system gain and the corresponding input voltage
ranges.

.. figure:: system_gain_config.jpg
   :align: center

   System gain configuration switch (S2) settings

.. list-table:: System Gain and Input Voltage Ranges
   :header-rows: 1
   :widths: 20 20 30

   * - S2 Setting
     - System Gain
     - Input Voltage Range
   * - 0.25 V/V
     - 0.125 V/V
     - +/-24 V (48 Vpp)
   * - 0.5 V/V
     - 0.25 V/V
     - +/-12 V (24 Vpp)
   * - 1 V/V
     - 0.5 V/V
     - +/-6 V (12 Vpp)
   * - 2 V/V
     - 1 V/V
     - +/-3 V (6 Vpp)
   * - 4 V/V
     - 2 V/V
     - +/-1.5 V (3 Vpp)
   * - 8 V/V
     - 4 V/V
     - +/-0.75 V (1.5 Vpp)
   * - 16 V/V
     - 8 V/V
     - +/-0.375 V (0.75 Vpp)

ADC Driver (ADA4945-1) Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the ADC driver mode by configuring the switch (S2) on the
EVAL-CN0535-FMCZ board. The :adi:`ADA4945-1` can be set to full power mode or
low power mode.

.. figure:: adc_driver_config.jpg
   :align: center

   ADC driver (ADA4945-1) configuration switch settings

Software GUI Setup
------------------

GUI Main Window
~~~~~~~~~~~~~~~

.. figure:: gui_main.jpg
   :align: center
   :width: 600px

   AD7768-1 evaluation software GUI main window

The main window of the GUI allows the user to configure the following settings
on the ADC:

#. **Buffer Control** -- Allows the user to configure the internal ADC input and
   reference buffers.

   .. figure:: buffer.jpg
      :align: center
      :width: 400px

      Buffer control settings

#. **Digital Filter Control** -- Allows the user to select the digital filter
   setting of the ADC.

   .. figure:: filter.jpg
      :align: center
      :width: 400px

      Digital filter control settings

#. **MCLK DIV** -- Allows the user to configure the MCLK divider setting on the
   ADC.

   .. figure:: mclk.jpg
      :align: center
      :width: 400px

      MCLK divider settings

#. **Power Mode** -- Sets the power mode setting on the ADC. The user can select
   from Fast, Median, and Low power mode settings.

   .. figure:: pwrmd.jpg
      :align: center
      :width: 400px

      Power mode settings

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0535-FMCZ Design & Integration Files
   <https://www.analog.com/cn0535-designsupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Software Projects and Platforms
-------------------------------

.. toctree::

   CN0535 + SDP-K1 <sdp-k1>

Additional Information
----------------------

- :adi:`CN0535 Circuit Note <CN0535>`
- `CN0535 Design Support Package
  <https://www.analog.com/CN0535-DesignSupport>`__
- :adi:`AD7768-1 Product Page <AD7768-1>`
- :adi:`LTC6373 Product Page <LTC6373>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADR444 Product Page <ADR444>`
- :adi:`AD8628 Product Page <AD8628>`
- :adi:`LT3095 Product Page <LT3095>`
- :adi:`ADP2300 Product Page <ADP2300>`
- :adi:`ADP7182 Product Page <ADP7182>`

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`EngineerZone <ez/reference-designs>`.
