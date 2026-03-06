.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cn0363-pmdz

.. _cn0363:

CN0363 User Guide
==================

Introduction
------------

The EVAL-CN0363-PMDZ is a colorimeter reference design based on the
:adi:`AD7175-2` sigma-delta ADC, the :adi:`AD5201` digital potentiometer, and
the :adi:`ADPD1080` photometric front end. The HDL reference design implements
function blocks to communicate over SPI with the AD7175-2 to configure it and
receive raw ADC data, as well as configure the AD5201 digital potentiometer.
The data received from the ADC is passed to a digital synchronous detector
processing pipeline and written to system memory using DMA.

The EVAL-CN0363-PMDZ is a dual-channel colorimeter featuring a modulated light
source transmitter, programmable gain transimpedance amplifiers on each
channel, and a very low noise 24-bit sigma-delta ADC. By using modulated light
and digital synchronous detection rather than a constant (dc) source, the
system strongly rejects any noise sources at frequencies other than the
modulation frequency, providing excellent accuracy.

The dual-channel circuit measures the ratio of light absorbed by the liquids
in the sample and reference containers at three different wavelengths. This
forms the basis of many chemical analysis and environmental monitoring
instruments used to measure concentrations and characterize materials through
absorption spectroscopy.

.. figure:: colorimeter_block_diagram.png
   :align: center

   CN0363 system block diagram

Circuit Description
~~~~~~~~~~~~~~~~~~~

A clock set to a user-programmable frequency modulates one of the three LED
colors (Red, Green, Blue) with a constant current driver built around the
:adi:`AD8615` op amp, the :adi:`ADG819` switch, and the :adi:`AD5201` digital
potentiometer. A beamsplitter sends half the light through the sample container
and half through the reference container. The :adi:`ADA4528-1`, configured as a
transimpedance amplifier, converts the photodiode current into an output
voltage square wave whose amplitude is proportional to the light transmitted
through the sample or reference containers. The transimpedance amplifiers use
ADG633 single-pole, double-throw (SPDT) switches to select one of two
transimpedance gains. The :adi:`AD7175-2` sigma-delta ADC samples the voltage
and sends the digital data to an FPGA for digital demodulation.

.. figure:: CN0363_sch.jpg
   :align: center

   CN0363 circuit schematic

For a thorough circuit description, see the
:adi:`CN0363 Circuit Note <media/en/reference-design-documentation/reference-designs/CN0363.pdf>`.

Supported Devices
-----------------

- :adi:`AD7175-2`
- :adi:`AD5201`
- :adi:`ADPD1080`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Hardware
--------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0363-PMDZ requires an external DC power supply in the range of 6 V
to 12 V connected to the screw terminal on the board. The PWR_LED indicator
illuminates when the board is powered. The analog portion of the circuit is
supplied by AVDD = 5 V from an ADP7102 low dropout regulator. The digital
portion is supplied by IOVDD = 3.3 V from an ADP1720 low dropout regulator.
Alternatively, IOVDD can be supplied from the PMOD connector VCC via a link
option. The 2.5 V reference voltage is supplied by the internal 2.5 V reference
of the AD7175-2 ADC.

.. figure:: cn0363_top_pwr.jpg
   :align: center

   EVAL-CN0363-PMDZ power connections

The ZedBoard requires a separate 12 V DC power supply connected to its DC
power jack.

IOVDD can be selected using header JP1:

- Pins 1-2 shorted: IOVDD sourced from the onboard regulator
- Pins 2-3 shorted: IOVDD sourced from the PMOD interface

.. figure:: cn0363_iovdd_1.jpg
   :align: center

   JP1 IOVDD selection

Input Interface
~~~~~~~~~~~~~~~

The EVAL-CN0363-PMDZ accommodates two vials: one for the reference container
and one for the sample container. A beamsplitter provides similar light to
both vials. The system requires an initial calibration to compensate for
misalignment between the LEDs, beamsplitter, and photodiodes, as well as to
compensate for any mismatch in the response of the photodiodes.

.. figure:: cn0363_top_1.jpg
   :align: center

   EVAL-CN0363-PMDZ board with vial holder

Vial Holder
^^^^^^^^^^^

The beamsplitter, reference vial, and sample vial are held in a mechanical
holder specifically designed for an 18 mm x 30 mm plate beamsplitter. Slots are
provided to hold the reference vial filled with distilled water and the sample
vial filled with the test liquid. Vials that can fit inside a 1 inch x 1 inch
slot can be used with the EVAL-CN0363-PMDZ.

Cleaning Procedure
^^^^^^^^^^^^^^^^^^

To obtain the most accurate results when taking measurements, follow these
steps:

#. The vials and beamsplitter must be meticulously cleaned.
#. Wash the vials and beamsplitter with soap and deionized water.
#. Soak the vials and beamsplitter in hydrochloric acid solution.
#. Rinse with ultra-filtered deionized water.
#. Polish with silicone oil.

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~~

The board uses the extended SPI PMOD interface to connect to the FPGA
development board via the PMOD JA connector on the ZedBoard.

.. list-table::
   :header-rows: 1

   * - Pin Number
     - Pin Function
     - Mnemonic
   * - P.1
     - Chip Select
     - AD_CS
   * - P.2
     - Gain Control-Reference
     - GAIN0
   * - P.3
     - Data In
     - AD_DIN
   * - P.4
     - Gain Control-Sample
     - GAIN1
   * - P.5
     - Data Out
     - AD_DOUT
   * - P.6
     - LED Select
     - DA_CS
   * - P.7
     - Serial Clock
     - AD_CLK
   * - P.8
     - LED Clock
     - LED_CLK
   * - P.9
     - Digital Ground
     - GND
   * - P.10
     - Digital Ground
     - GND
   * - P.11
     - Digital Power
     - VCC
   * - P.12
     - Digital Power
     - VCC

Design Resources
~~~~~~~~~~~~~~~~

The complete design support package containing schematic, assembly drawing,
layout files, Gerber files, and bill-of-materials is available at the
:adi:`CN0363 Design Support Package <CN0363-DesignSupport>`.

HDL Reference Design
--------------------

SPI Communication
~~~~~~~~~~~~~~~~~

.. figure:: cn0363_hdl_spi.png
   :align: center

   CN0363 SPI communication block diagram

The SPI Engine Framework is used for SPI communication. This allows flexibility
to access all configuration registers for both connected SPI devices
dynamically from software, as well as allowing low-latency and high-throughput
automated access to the SPI bus when capturing sample data from the ADC.

The SPI-Engine AXI core is mapped into the system peripheral memory bus via an
AXI-Lite interface and can be accessed by the CPU. Its interrupt signal is
connected to the processing system. The core has two primary functions: giving
direct access to the SPI bus for configuring device registers, and controlling
the SPI-Engine offload core.

The SPI-Engine interconnect core gives both the SPI-Engine AXI and SPI-Engine
offload core access to the SPI-Engine execution core. The offload core is
connected to the first interconnect slave port, which gives it priority over
the AXI core. This prioritization is necessary because reading ADC result data
is timing-critical, while changing configuration registers typically is not.

The SPI-Engine offload core reads the ADC result data and feeds it into the
processing pipeline. Software is responsible for setting up the core with the
correct SPI message to read the ADC result register, as well as enabling the
core when the ADC converter is active. Once the core is set up and enabled, the
stored SPI message is executed when the data ready (RDY) signal from the ADC is
detected.

The SigmaDelta SPI core monitors the low-level SPI bus and extracts the data
ready signal, which is multiplexed over the same physical wire as the SPI MISO
signal. The data ready signal is connected to the SPI-Engine offload core
(which starts reading the ADC conversion result when asserted) and to the
processing pipeline (which takes a snapshot of the excitation signal phase).
This allows precise time-stamping of the excitation signal phase in relation to
the ADC conversion time.

Synchronous Detector Processing Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: cn0363_hdl_processing.png
   :align: center

   CN0363 processing pipeline block diagram

The processing pipeline consists of the following stages:

#. **Phase/Data Sync** - Takes a snapshot of the phase counter on conversion
   done, then waits for the corresponding data sample from the ADC. Converts
   data from offset binary to two's complement.
#. **High-pass Filter** - Removes noise below 50 Hz and any DC components.
#. **CORDIC Demodulator** - Calculates the data multiplied by both cosine and
   sine of the phase. Outputs demodulated in-phase (I) and quadrature (Q)
   components.
#. **Low-pass Filter** - Removes frequency components different from the
   excitation frequency.
#. **Sequencer** - Cycles through input data, intermediate results, and final
   processing results, sending them to the DMA controller.

Both filters are configured in a time-division-multiplexing configuration,
sharing logic for filter output calculation between channels. This is possible
because the ADC output data rate is 50 kHz while the FPGA pipeline runs at
100 MHz, giving approximately 2000 clock cycles per high-pass filter result
and 1000 clock cycles per low-pass filter result.

The various broadcasting blocks in the processing pipeline forward data to the
next processing element as well as to the sequencer that sends data to the DMA.
This allows inspection of intermediate results at each stage.

Phase/Data Sync Core
^^^^^^^^^^^^^^^^^^^^

.. figure:: cn0363_phase_data_sync.png
   :align: center

   CN0363 Phase Data Sync block diagram

The Phase Data Sync core prepares the ADC conversion result data, aligns it
with the excitation phase, and feeds both to the processing pipeline.

.. list-table::
   :header-rows: 1

   * - Signal
     - Type
     - Description
   * - ``clk``
     - Clock
     - All other signals are synchronous to this clock
   * - ``resetn``
     - Active low reset
     - Resets the internal state machine
   * - ``processing_resetn``
     - Active low reset
     - Indicates the processing pipeline is in reset
   * - ``S_AXIS_SAMPLE``
     - AXI-Stream slave
     - Input sample data stream
   * - ``M_AXIS_SAMPLE``
     - AXI-Stream master
     - Output sample data stream
   * - ``M_AXIS_PHASE``
     - AXI-Stream master
     - Output phase data stream
   * - ``sample_has_stat``
     - Input
     - Whether incoming data has the STAT register appended
   * - ``conv_done``
     - Input
     - Conversion done signal from the ADC
   * - ``phase``
     - Input
     - Current excitation signal phase
   * - ``overflow``
     - Output
     - Asserted if a new sample arrives before the previous one is consumed

The core takes raw ADC sample data from the ``S_AXIS_SAMPLE`` stream, assembles
it into a 24-bit word, and converts it from offset binary to two's complement
signed format. When a rising edge is detected on ``conv_done``, the core
snapshots the ``phase`` input. This phase value is assumed to correspond to
the next incoming data sample. The data and phase are aligned and output on
``M_AXIS_SAMPLE`` and ``M_AXIS_PHASE``.

If ``sample_has_stat`` is asserted, the core receives 32-bit samples instead of
24-bit, where the last 8 bits contain the ADC STAT register. This register
includes channel identification information, which can be used to detect and
correct channel swaps.

DMA Sequencer Core
^^^^^^^^^^^^^^^^^^

.. figure:: cn0363_dma_sequencer.png
   :align: center

   CN0363 DMA Sequencer block diagram

The DMA Sequencer core links the processing pipeline to the DMA controller. It
accepts data from the pipeline and sends it to the DMA controller. The core is
only active when the DMA controller signals that it is waiting for data; when
inactive, it asserts ``processing_resetn`` to keep the processing pipeline in
reset.

.. list-table::
   :header-rows: 1

   * - Signal
     - Type
     - Description
   * - ``clk``
     - Clock
     - All other signals are synchronous to this clock
   * - ``resetn``
     - Active low reset
     - Resets the internal state machine
   * - ``phase``
     - AXI-Stream slave
     - Phase data channel
   * - ``data``
     - AXI-Stream slave
     - Sample data channel
   * - ``data_filtered``
     - AXI-Stream slave
     - Filtered sample data channel
   * - ``i_q``
     - AXI-Stream slave
     - Demodulated I/Q sample data channel
   * - ``i_q_filtered``
     - AXI-Stream slave
     - Filtered demodulated I/Q sample data channel
   * - ``dma_wr``
     - FIFO Write master
     - DMA write interface
   * - ``overflow``
     - Output
     - Asserted on DMA interface overflow
   * - ``channel_enable``
     - Input
     - Data channel enable mask
   * - ``processing_resetn``
     - Output
     - Reset signal for the processing pipeline

When active, the core cycles through the input channels in the following order:

#. Phase (reference channel)
#. Data (reference channel)
#. Filtered data (reference channel)
#. I component (reference channel)
#. Q component (reference channel)
#. Filtered I component (reference channel)
#. Filtered Q component (reference channel)
#. Phase (sample channel)
#. Data (sample channel)
#. Filtered data (sample channel)
#. I component (sample channel)
#. Q component (sample channel)
#. Filtered I component (sample channel)
#. Filtered Q component (sample channel)

Each channel has a corresponding bit in ``channel_enable``. Only channels with
their enable bit set are sent to the DMA; others are discarded. During normal
operation, typically only the final processing results are captured.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/cn0363`

Software Support
----------------

Linux Device Driver
~~~~~~~~~~~~~~~~~~~

The EVAL-CN0363-PMDZ uses Linux drivers in the IIO framework. The AD7175-2 ADC
is supported by the AD7173 family driver.

- :git-linux:`drivers/iio/adc/ad7173.c`

Since the drivers use the IIO framework, the
:doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application can be
used to access raw sample data from the EVAL-CN0363-PMDZ. This is mainly
intended for debugging purposes.

Colorimeter Application
~~~~~~~~~~~~~~~~~~~~~~~

The primary application for interacting with the EVAL-CN0363-PMDZ is the ADI
Colorimeter application. It can be used to gather, manage, and compare
processed sample data from the board.

The application provides the following features:

- **Automated Data Collection** - Performs an automated sample analysis that
  cycles through all three colors (Red, Green, Blue) and calculates the
  absorbance factor for each. Samples can be matched against a sample library
  or saved for future use.
- **Current/Absorbance Measurement** - Provides direct access to the LED and
  gain controls and allows periodic capture and visualization of raw data.
  Controls include excitation frequency, excitation current, LED selection,
  and per-channel gain selection (33 kOhm or 1 MOhm).
- **Sample Library** - Allows managing and comparing previously saved sample
  data. Multiple samples can be selected to directly compare absorbance values.
- **Calibration** - For optimum performance, the application must be calibrated
  to the connected board and environment. Calibration is performed with
  distilled water in both the reference and sample probes while shielding the
  photodiodes from ambient light. Calibration data can be exported and imported.

Source code is available in the
`colorimeter repository <https://github.com/analogdevicesinc/colorimeter>`__.

Quick Start Guide
-----------------

Hardware Setup
~~~~~~~~~~~~~~

The required hardware for the EVAL-CN0363-PMDZ system:

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
  Rev C or later
- EVAL-CN0363-PMDZ board
- Two vials: one filled with distilled water (reference) and one with the
  sample liquid under test
- SD card (8 GB minimum) preloaded with the
  :doc:`Kuiper Linux </linux/kuiper/index>`
- 12 V DC power supply for the ZedBoard
- 6 V to 12 V DC power supply for the EVAL-CN0363-PMDZ
- HDMI monitor and USB keyboard/mouse
- Ethernet cable with internet connection (only required for software updates)

.. figure:: cn0363_setup.png
   :align: center

   EVAL-CN0363-PMDZ system connection diagram

Connect the system as follows:

#. Connect the PMOD JA connector of the ZedBoard to the PMOD connector on
   the EVAL-CN0363-PMDZ
#. Connect USB mouse and keyboard to the ZedBoard (J13)
#. Connect the 12 V power supply to the ZedBoard (J20)
#. Set the ZedBoard VADJ jumper to 3.3 V
#. Insert the SD card into the ZedBoard (J12)
#. Connect the HDMI monitor to the ZedBoard (J9)
#. Connect the 6 V to 12 V power supply to the EVAL-CN0363-PMDZ screw
   terminal

.. figure:: colorimeter_test_setup.png
   :align: center
   :width: 400

   EVAL-CN0363-PMDZ test setup

Boot (JP7-JP11) and MIO0 (JP6) jumpers must be set to SD card boot mode.
Install jumpers JP2 and JP3 to enable USB peripheral devices.

Starting the System
~~~~~~~~~~~~~~~~~~~

Power on the ZedBoard by setting the main power switch (SW8). After a few
seconds the blue DONE LED (LD12) will illuminate. After approximately
30 seconds the system boots and the desktop appears on the HDMI monitor.

.. figure:: cn0363_zed_startup_1.png
   :align: center

   ZedBoard desktop after boot

Close the ADI IIO Oscilloscope if it opens automatically, as it is not required
for the EVAL-CN0363-PMDZ. To start the colorimeter application, go to the
top-left **Applications Menu**, navigate to the **Other** section, and click
**ADI CN0363 Colorimeter**.

.. figure:: cn0363_zed_startup_2.png
   :align: center

   CN0363 Colorimeter application running

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`CN0363 Circuit Note <CN0363>`
- :adi:`CN0363 Design Support Package <CN0363-DesignSupport>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
