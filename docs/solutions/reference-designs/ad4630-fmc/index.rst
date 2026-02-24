.. _ad4630-fmc:

AD4630-FMC User Guide
=====================

Introduction
------------

The EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, and EVAL-AD4630-16FMCZ evaluation
boards enable quick and easy evaluation of the AD4x3x family of 24-bit and
16-bit precision successive approximation register (SAR) analog-to-digital
converters (ADCs).

The :adi:`AD4630-24` and :adi:`AD4630-16` are 2 MSPS per channel, low power,
dual channel, 24-bit or 16-bit SAR ADCs, while the :adi:`AD4030-24` is a
single channel, 24-bit precision SAR ADC supporting up to 2 MSPS.

The evaluation boards are designed for use with the ZedBoard. The ZedBoard
controls data capture and buffering, and connects to the evaluation board via
an FMC LPC connector. The ZedBoard hosts a Xilinx Zynq-7000 SoC with dual
ARM Cortex-A9 processors and programmable FPGA fabric. It communicates with
the PC through USB or Ethernet.

Supported Devices
-----------------

- :adi:`AD4630-24`
- :adi:`AD4030-24`
- :adi:`AD4630-16`

Evaluation Boards
-----------------

- :adi:`EVAL-AD4630-24 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-24.html>`
- :adi:`EVAL-AD4630-16 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-16.html>`
- :adi:`EVAL-AD4030-24 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4030-24.html>`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Equipment Needed
~~~~~~~~~~~~~~~~

- PC with Windows 7 or Windows 10 operating system
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  with 12 V wall adapter power supply
- Precision signal source
- SMA cable(s)
- Recommended: band-pass filter centered on the test signal frequency

Evaluation Board Kit Contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ, or EVAL-AD4630-16FMCZ evaluation
  board
- Micro-SD memory card (with adapter) containing system board boot software
  and Linux OS
- Optional: ZedBoard (system controller board)

Evaluation Board Revisions
--------------------------

Two different evaluation board revisions exist for the AD4630-24 and AD4630-16:

EVAL-AD4630-24/16FMCZ Rev C (Obsolete)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: eval-ad4630-16_top.jpg
   :align: center
   :width: 500

   EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ, Rev C

- Two differential input channels with SMA connectors
- High precision buffered band gap 5 V reference (:adi:`LTC6655`)
- Configurable AFE with :adi:`ADA4896-2` (dual buffer) or :adi:`ADA4945-1`
  (fully differential amplifier)
- Optional 100 MHz clock source for FPGA and ADC
- Full power supply solution from 12 V via FMC connector

EVAL-AD4630-24/16FMCZ Rev E (Current)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cb-ad464030-24fmcz_top-evaluation-board.jpg
   :align: center
   :width: 500

   EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ, Rev E

Rev E boards have a date code greater than DC>2435.

- Two differential input channels with SMA connectors
- High precision, low power, low noise 5 V reference (:adi:`ADR4550`), with
  option to mount :adi:`LTC6655`
- Configurable AFE with :adi:`ADA4896-2` (multiple input configurations) or
  :adi:`ADA4945-1` (fully differential amplifier)
- Optional 100 MHz clock source for FPGA and ADC
- Improved power supply solution from 12 V via FMC connector
- Extra connectors for external power supply

EVAL-AD4030-24FMCZ Rev A/B
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: eval-ad4030-24_top.jpg
   :align: center
   :width: 500

   EVAL-AD4030-24FMCZ, Rev A/B

- One differential input channel with SMA connectors
- High precision buffered band gap 5 V reference (:adi:`LTC6655`)
- Configurable AFE with :adi:`ADA4896-2` (dual buffer) or :adi:`ADA4945-1`
  (fully differential amplifier)
- Optional 100 MHz clock source for FPGA and ADC
- Full power supply solution from 12 V via FMC connector

Evaluation Board Hardware
-------------------------

Power Supplies (Rev C / Rev A/B)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The primary 12 V supply comes from the ZedBoard through the FMC connector.
Each voltage rail is brought out to turrets for easy measurement. A bench
supply can be used to drive these turrets for manual powering when current
measurements are required.

.. list-table:: On-board power supplies (Rev C / Rev A/B)
   :header-rows: 1

   * - Power Supply
     - Function
     - Min (V)
     - Max (V)
   * - +12V
     - Primary supply via FMC connector
     - N/A
     - N/A
   * - GND
     - Ground connection
     - N/A
     - N/A
   * - +3.3V
     - Digital logic supply
     - 3.26
     - 3.33
   * - +1.8V
     - ADC supply
     - 1.77
     - 1.81
   * - VIO
     - ADC digital I/O supply
     - 1.8
     - 1.87
   * - +5V
     - ADC supply
     - 5.26
     - 5.4
   * - REFIN
     - ADC reference input
     - 4.95
     - 5.05
   * - VAMP+
     - Positive amplifier supply
     - 5.36
     - 5.47
   * - VAMP-
     - Negative amplifier supply
     - -3.5
     - -3.28
   * - VP1
     - Switcher input (5.7 V)
     - 5.45
     - 5.75
   * - REF
     - ADC reference output
     - 4.95
     - 5.05
   * - EN
     - Power supply enable
     - 1.75
     - 1.85

Power Supplies (Rev E)
~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: On-board power supplies (Rev E)
   :header-rows: 1

   * - Power Supply
     - Function
     - Min (V)
     - Max (V)
   * - +12V
     - Primary supply via FMC connector
     - N/A
     - N/A
   * - GND
     - Ground connection
     - N/A
     - N/A
   * - +3.3V
     - Digital logic supply
     - 3.26
     - 3.33
   * - +1.8V
     - ADC supply
     - 1.77
     - 1.81
   * - VIO
     - ADC digital I/O supply
     - 1.77
     - 1.81
   * - +5.4V
     - ADC supply
     - 5.34
     - 5.46
   * - REFIN
     - ADC reference input
     - 4.95
     - 5.05
   * - VAMP+
     - Positive amplifier supply
     - 6.35
     - 6.5
   * - VAMP-
     - Negative amplifier supply
     - -3.35
     - -3.28
   * - VP1
     - Switcher input (7.5 V)
     - 7.425
     - 7.575
   * - REF
     - ADC reference output
     - 4.95
     - 5.05
   * - EN
     - Power supply enable
     - 1.75
     - 1.85

.. figure:: powertree.png
   :align: center

   Power tree for EVAL-AD4630-24/16FMCZ Rev E

Reference Circuit
~~~~~~~~~~~~~~~~~

**Rev C / Rev A/B:** The on-board :adi:`LTC6655` provides a 5 V reference to
the ADC. It drives the REFIN pin through an R-C filter (R=100 Ohm, C=1 uF)
that reduces low frequency noise.

**Rev E:** The on-board :adi:`ADR4550` provides a 5 V reference. It drives the
REFIN pin through an R-C filter (R=100 Ohm, C=22 uF). There is also an option
to mount the :adi:`LTC6655` or LTC6655LN reference.

.. figure:: ad4630_ref_ckt.png
   :align: center

   Reference circuit (Rev C / Rev A/B; AD4630-24 shown, applies to all parts)

.. figure:: reference2.png
   :align: center

   Reference circuit (Rev E; AD4630-24 shown, applies to all parts)

To use an external reference that drives the internal buffer, attach it to the
EXT REF SMA connector. The internal buffer can be bypassed by attaching an
external reference to the REF turret on the board.

Clock Circuit
~~~~~~~~~~~~~

The ZedBoard uses a 100 MHz reference clock to generate its internal clocks
and the sample clock for the ADC. An on-board 100 MHz, low-jitter crystal
oscillator provides this clock as the default configuration.

To use an external clock source, remove the appropriate resistor (R55 for
Rev C, R1 for Rev E) and connect an external clock source to the CLK IN SMA
connector. The external clock frequency must be 100 MHz or less, and the
external clock level should be 10 to 12 dBm.

.. figure:: eval-ad4630-24_clk_ckt.png
   :align: center

   Clock circuit (Rev C; AD4630-24 shown, applies to all parts)

Analog Front End
~~~~~~~~~~~~~~~~

The evaluation board has a flexible driver network supporting multiple
topologies:

- **Differential Amplifier (default)** - :adi:`ADA4945-1` fully differential
  amplifier driving the ADC with unity gain. Supports single-ended and
  differential sources. Best distortion performance. No changes required from
  default configuration.
- **Dual Buffer** - :adi:`ADA4896-2` dual unity gain buffer for best noise
  performance due to low voltage and current noise (1 nV/rtHz and 2.8 pA/rtHz).
  Offers 10 MOhm common mode input impedance.
- **Buffer with Gain** - Combination of ADA4896-2 and ADA4945-1 for
  applications requiring high input impedance with gain.
- **Direct Drive** - Allows the ADC to be driven directly from the SMA
  connectors for evaluation with external driver configurations.

.. note::

   The ADA4945-1 driver on the evaluation board preserves the differential
   value of IN+ - IN- but inverts the signal polarity injected to the ADC.
   If a positive DC signal is applied, connect it to IN_A/B-. A negative DC
   signal should be connected to IN_A/B+ to preserve polarity.

AFE Component Changes (Rev C / Rev A/B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Configuration
     - Purpose
     - Required Changes from Default
   * - Differential Amplifier
     - Best distortion
     - No changes required
   * - Dual Buffer
     - Best noise
     - Remove: R10, R12, R119, R120, R121, R122 (Ch A); R20, R22, R123, R124,
       R125, R126 (Ch B). Install: R31, R33, R47, R49 (Ch A); R60, R62, R75,
       R78 (Ch B)
   * - Buffer with Gain
     - High impedance + gain
     - Remove: R120, R121 (Ch A); R124, R125 (Ch B). Install: R31, R127, R28,
       R47, R128, R43 (Ch A); R60, R129, R57, R78, R130, R72 (Ch B)
   * - Direct Drive
     - External driver eval
     - Remove: R10, R12, R119, R122 (Ch A); R20, R22, R123, R126 (Ch B).
       Install: R28, R29, R120, R121, R43, R44 (Ch A); R124, R57, R58, R125,
       R72, R73 (Ch B)

AFE Component Changes (Rev E)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Configuration
     - Purpose
     - Required Changes from Default
   * - Differential Amplifier
     - Best distortion
     - No changes required
   * - Dual Buffer
     - Best noise
     - Remove: R17, R23, R19, R25, R42, R45, R44, R48. Install: R114, R108,
       R112, R106, R139, R136, R137, R134
   * - Buffer with VOCM
     - High impedance + DC offset
     - Remove: R17, R23, R19, R25, R42, R45, R44, R48. Install: R114, R108,
       R112, R106, R139, R136, R137, R134, R120, R119, R103, R102, R142,
       R141, R132, R131
   * - Direct Drive
     - External driver eval
     - Remove: R17, R23, R19, R25, R42, R45, R44, R48. Install: R121, R118,
       R104, R105, R143, R140, R133, R130

Quick Start
-----------

1. Ensure the ZedBoard VADJ SELECT jumper is set to **2.5 V**.
2. Insert the Kuiper Linux SD card into the SD card slot on the ZedBoard.
3. Set the ZedBoard boot configuration jumpers for SD card boot.
4. Connect the evaluation board to the FMC connector on the ZedBoard.
5. Connect a USB cable from the PC to J13 (USB OTG) and the power supply
   to J20 (DC input).
6. Slide SW8 (POWER) to the ON position. The green LD13 (POWER) LED should
   turn on. The blue LD12 (DONE) and red LD0 LEDs should start blinking after
   approximately 20-30 seconds, indicating the boot process is complete.
7. Connect the desired input signal to the appropriate SMA connectors on the
   evaluation board.
8. Launch the ACE software or connect via IIO.

.. note::

   If the SD card needs to be re-imaged, instructions are available in the
   `ADI Kuiper Linux <https://wiki.analog.com/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`__
   documentation.

System Operational Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Maximum sampling rate by device configuration
   :header-rows: 1

   * - Clocking Mode
     - Lane Mode
     - Data Rate
     - Data Format
     - Max Sampling Rate
   * - SPI
     - 1
     - SDR
     - 24-bit
     - 2 MSPS
   * - SPI
     - 1
     - DDR
     - 32 or 24-bit
     - 2 MSPS
   * - SPI
     - 2
     - SDR or DDR
     - 32 or 24-bit
     - 2 MSPS
   * - SPI
     - 4
     - SDR or DDR
     - 32 or 24-bit
     - 2 MSPS
   * - Echo Clock
     - 1
     - SDR
     - 24-bit
     - 2 MSPS
   * - Echo Clock
     - 1
     - DDR
     - 32 or 24-bit
     - 2 MSPS
   * - Echo Clock
     - 2
     - SDR or DDR
     - 32 or 24-bit
     - 2 MSPS

.. note::

   The sampling rate in single lane, 32-bit output formats in SDR mode is
   limited by the FPGA SPI engine. This is not a limitation of the
   AD4630/AD4030 device.

HDL Reference Design
--------------------

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad4630_fmc`

Software Support
----------------

ACE Software
~~~~~~~~~~~~

The ADI `ACE <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`__
application provides a plug-and-play evaluation experience with the ZedBoard,
enabling quick board configuration, data capture, and analysis (time and
frequency domain).

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

- :git-linux:`drivers/iio/adc/ad4630.c`

pyadi-iio
~~~~~~~~~

The `pyadi-iio <https://analogdevicesinc.github.io/pyadi-iio/>`__ library
provides Python bindings for the AD4630/AD4030 family. Example scripts are
available in the
`source repository <https://github.com/analogdevicesinc/pyadi-iio/tree/main/examples/ad4630>`__.

A basic usage example:

.. code-block:: python

   import adi

   device_name = "ad4630-24"

   # Instantiate ADC (Ethernet connection)
   adc = adi.ad4630(uri="ip:analog.local", device_name=device_name)
   # For USB connection, use: uri="usb:x.x.x" (from iio_info -s)

   # Configure
   adc.rx_buffer_size = 2**12
   adc.sample_rate = 2000000

   # Capture data
   data = adc.rx()

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

For precision ADC questions, visit the
:ez:`Precision ADCs Forum <data_converters/precision_adcs>`.
