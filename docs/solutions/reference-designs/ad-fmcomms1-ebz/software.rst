Software and HDL
================

Digital Interface Timing Validation
------------------------------------

Both the :adi:`AD9122` (DAC) and :adi:`AD9643` (ADC) have tight FPGA-to-converter
digital interface timing requirements. The system software uses on-chip
verification mechanisms to ensure reliable data transfer across voltage,
temperature, and different carrier boards.

AD9122 (DAC)
~~~~~~~~~~~~

The AD9122 provides timing verification via its on-chip Sample Error Detection
(SED) circuitry. The SED compares input data samples captured at the digital
input pins with comparison values loaded over SPI. Differences are detected
and stored in error registers.

The SED circuitry operates on four 16-bit input words (I0, Q0, I1, Q1) loaded
to registers ``0x68``-``0x6F``. Three flag bits in register ``0x67`` indicate
comparison results, and registers ``0x70``-``0x73`` accumulate per-bit error
information.

The system software loads a predetermined pattern, enables SED, and sends
data over the high-speed interface. If errors are detected, the DCI (Data
Clock Input) delay is adjusted using a programmable delay (350 ps to 925 ps).

.. figure:: ad9122_dci.png
   :align: center
   :width: 400

   AD9122 DCI delay adjustment

.. note::

   DCI delay adjustment compensates for clock-to-data skew but does not
   resolve data pin-to-pin timing issues, which must be handled inside the
   FPGA.

AD9643 (ADC)
~~~~~~~~~~~~

The :adi:`AD9643` uses its built-in test mode register (``0x0D``) to generate
known PN sequences (LFSR/PRBS) for timing verification. The ADC PN sequences
use the following polynomials:

- **Long**: x\ :sup:`16` + x\ :sup:`6`
- **Short**: x\ :sup:`8` + x\ :sup:`6` + x\ :sup:`0`

The HDL includes a PN monitor module that verifies the received sequence.
When mismatches occur, the DCO (Data Clock Output) delay is adjusted via SPI
register ``0x017``, providing a fine delay range from 100 ps to 3200 ps.

.. figure:: ad9643_dco.png
   :align: center
   :width: 500

   AD9643 DCO delay adjustment

HDL Reference Design
--------------------

The reference design is a processor-based embedded system using DDS for
flexible internal signal generation, external memory via VDMA for waveforms,
FFT processing for spectrum analysis, and DMA transfers for ADC data to DDR.

Key IP cores:

- **cf_axi_adc**: ADC interface (AXI streaming)
- **cf_axi_dds**: DAC DDS interface (AXI streaming)
- I/Q correction HDL available for Simulink-based matrix multiplication

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`hdl_2016_r1:projects/fmcomms1`

Linux Drivers
-------------

The following IIO subsystem drivers are used:

.. list-table::
   :header-rows: 1

   * - Device
     - Driver
     - Function
   * - :adi:`AD9523-1`
     - :git-linux:`drivers/iio/frequency/ad9523.c`
     - PLL clock generator
   * - :adi:`ADF4351`
     - :git-linux:`drivers/iio/frequency/adf4350.c`
     - Synthesizer / LO tuning
   * - :adi:`AD8366`
     - :git-linux:`drivers/iio/amplifiers/ad8366.c`
     - Variable gain amplifier
   * - :adi:`AD9643`
     - :git-linux:`drivers/iio/adc/cf_axi_adc_core.c`
     - ADC digital interface
   * - :adi:`AD9122`
     - :git-linux:`drivers/iio/frequency/cf_axi_dds.c`
     - DAC / DDS interface
   * - I2C-SPI Bridge
     - :git-linux:`drivers/spi/spi-xcomm.c`
     - PIC microcontroller bridge

Linux Applications
------------------

- **IIO Oscilloscope**: Full graphical interface for device control and data
  capture. Can be used locally (HDMI + USB keyboard) or remotely over the
  network.
- **Shell scripts**: Command-line control of DDS frequencies, amplitudes, and
  LO sweep via sysfs attributes.
- **fru_dump**: Reads the FRU EEPROM for board identification and calibration
  data.
- **xcomm_cal**: Board calibration utility.

I/Q Correction
--------------

The board provides an I/Q correction framework to compensate for amplitude
offset, phase offset, and DC bias in baseband signals caused by component
mismatches. Without correction, image interference creates an error floor
limiting demodulation performance.

The correction uses a two-step implementation: matrix parameter calculation
(MATLAB/Simulink) and hardware multiplication (HDL). Simulink models are
provided for calculating the correction matrix parameters.
