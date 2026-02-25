.. _cn0561:

EVAL-CN0561-ARDZ
================

IEPE/ICP Piezoelectric Vibration Measurement System.

.. image:: eval-cn0561-ardz_angle-evaluation-board.jpg
   :align: center
   :width: 500

Overview
--------

Monitoring the health of machinery can help predict changes in a machine's
condition. There are many methods of tracking a machine's condition, but
vibration analysis is the most commonly used one. By tracking the vibration
analysis data over time, one can determine when a fault or failure is going to
occur, along with the source of the fault. Knowing the condition of a certain
machine will help not only increase efficiency and productivity, but create a
safer working environment.

The reference design shown below shows a high resolution, wide-bandwidth, high
dynamic range, Integrated Electronics Piezoelectric (IEPE) compatible interface
data acquisition system (DAQ) for interfacing with Integrated Circuit Piezo
(ICP)/IEPE piezo vibration sensors. This reference design is an AC-coupled
solution targeted for wide band IEPE based sensors.

By looking at the complete data set from the vibration sensor in the frequency
domain (DC to 50 kHz), the type and source of a machine fault can be better
predicted using the position, amplitude and number of harmonics found in the
FFT spectrum.

The data acquisition board incorporates a precision alias-free quad-channel
24-bit, 1.496 MSPS continuous-time sigma-delta ADC :adi:`AD4134`, an
instrumentation amplifier with differential output :adi:`LTC6373`, and a 250 mA
programmable 2-terminal current source :adi:`LT3092`. Analog input fault
detection and protection is provided by the switch :adi:`ADG5462F`. The data
acquisition board is an Arduino compatible form factor and can be interfaced
and powered directly from most Arduino compatible development boards.

The :adi:`CN0561` has 2 channels of IEPE interface and 2 channels for general
data acquisition.

Features:

- Data acquisition solution fully characterized over -40°C to 85°C
- Throughput of up to 1496 kSPS
- Alias-free and resistive inputs: No low pass filter or driver needed
- Powered and interfaced directly through an Arduino compatible development board

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: blockdiagramcn561.jpg
   :align: center

Simplified Signal Chain Schematic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: figure_1_2.jpg
   :align: center

Hardware Setup
--------------

Documents Needed
~~~~~~~~~~~~~~~~

- :adi:`AD4134 Data Sheet <AD4134>`
- :adi:`CN0561 Circuit Note <CN0561>`

Equipment Required
~~~~~~~~~~~~~~~~~~

- :adi:`CN0561 Circuit Evaluation Board (EVAL-CN0561-ARDZ) <CN0561>`
- NUCLEO-H563ZI board
- IIO Oscilloscope software
- USB Type-C to USB cable
- Precision AC source (for example, AP2700, Brüel & Kjær, or similar precision
  sine generator)

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The basic test setup requires the EVAL-CN0561-ARDZ board to be plugged into
the NUCLEO-H563ZI board. The NUCLEO-H563ZI board is required to capture and
display the data. Software is available from the
`IIO Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`__
page.

.. figure:: fig_7.png
   :align: center

Mount the EVAL-CN0561-ARDZ evaluation board on the carrier board
(NUCLEO-H563ZI) by plugging it into the Arduino header as shown below.

.. figure:: fig_8.jpg
   :align: center

To test the basic functionality of the board, connect a precision, high quality
sine wave or arbitrary waveform generator to the analog input connector of the
EVAL-CN0561-ARDZ board.

Follow these steps to set up the EVAL-CN0561-ARDZ and the associated software:

#. Connect the USB-C cable to the NUCLEO-H563ZI board and to a USB port of
   your laptop.
#. Connect a 12 V power supply to the CN0561-ARDZ P16.
#. The connected green LED lights up on the NUCLEO-H563ZI board, next to the
   USB-C connector.
#. Give analog input signal using the connectors J6 and J8 on the
   EVAL-CN0561-ARDZ analog input SMA connectors.
#. Open the file explorer and open the folder NOD_H563ZI. Copy the file
   ``EVAL-CN0561-ARDZ.bin`` to the above folder. The file in the folder will
   disappear and the file explorer will close automatically once the file is
   copied.
#. The USB connection creates a COM port to connect to the IIO Oscilloscope GUI
   running on Windows. The COM port assigned to a device can be seen through
   the Device Manager on Windows-based operating systems.
#. Open the IIO Oscilloscope connection dialog and select the COM port for
   NUCLEO-H563ZI. Select the COM port and baud rate 230400. Click the
   **Refresh** button.
#. IIO OSC shows the device name. Click the **Connect** button.
#. Select the AD4134 from the device name drop down.
#. Power on the sine or arbitrary waveform generator:

   - Set the signal type to sine wave.
   - Set level to 1 V p-p at 1 kHz.
   - Enable the output.

#. Run the software and capture the resulting ADC data and FFT data.
#. Go to the Capture Window and press the **Enable all** button.

Connectors
~~~~~~~~~~

All connectors listed below provide extensive options for interacting with the
data acquisition board.

- P1, P2, P4, P5: Arduino connectors
- P17: Arduino Zio connector
- P3: FMCZ connector
- P6, P7: SMA connectors for IEPE sensor connection
- P8, P9: Analog inputs for data acquisition
- P16: External power input: 9 V to 12 V
- P14: External +15 V/-15 V supply for analog front end
- J6, J8: SMA connectors for analog inputs to channel 0
- J5, J7: SMA connectors for analog inputs to channel 3
- P11, P12: Optional connectors for analog inputs to channels 1 and 2

Arduino Pin Assignments
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: arduino.jpg
   :align: center

Test Points
~~~~~~~~~~~

.. figure:: testpoint.jpg
   :align: center

Configurations
~~~~~~~~~~~~~~

**Jumper P10 - ASRC and SRC Mode Selection**

- CLOSE: ASRC Mode — DCLK and ODR pins are inputs
- OPEN: SRC Mode — DCLK and ODR pins are outputs

**Jumpers P13 and P15 - Analog Front End Amplifier Supply Selection**

- CLOSE 1-2 & OPEN 2-3: On-board +15 V/-15 V supply
- CLOSE 2-3 & OPEN 1-2: External +15 V/-15 V supply from P14

**Instrumentation Amplifier Gain Settings**

Gain is controlled using the GPIO functionality of the :adi:`AD4134` which is
accessible via SPI. Configure the GPIOs as outputs using the
``GPIO_DIR_CTRL`` register. Use ``GPIO_DATA`` to write high and low levels on
the pins.

Gain settings apply to groups of CH0 & CH1, and CH2 & CH3 independently.

.. figure:: user_guide_gain_cn0561.jpg
   :align: center

LED Indicators
~~~~~~~~~~~~~~

- DS1: Fault flag LED that glows when an input fault occurs on the
  :adi:`ADG5462F`

Host Processor Connector
~~~~~~~~~~~~~~~~~~~~~~~~

Arduino and Zio connectors P1, P2, P4, P5, and P17 connect to 3.3 V Arduino
boards.

Firmware
--------

Precision Converters Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0561-ARDZ is supported by the Precision Converters Firmware
project. Firmware for the NUCLEO-H563ZI platform is available at:

- `AD4134 IIO Firmware <https://analogdevicesinc.github.io/precision-converters-firmware/source/projects/ad4134_iio/ad4134_iio.html>`__

Software Support
----------------

Linux Driver and HDL Reference Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0561-ARDZ is also supported by an HDL reference design targeting
FPGA carrier boards. The HDL design uses the SPI Engine Framework to interface
with the :adi:`AD4134` ADC in slave mode, with the FPGA generating both DCLK
and ODR signals. The following carriers are supported:

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ on FMC slot
- `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__ on Arduino-type headers
- `DE10-Nano <https://www.intel.com/content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`__

When using the HDL reference design, the following jumper positions are
required on the EVAL-CN0561-ARDZ:

- P10: Mounted (ASRC mode)
- P13: Position 1-2 (on-board +/-15 V supply)
- P15: Position 1-2 (on-board +/-15 V supply)

**HDL Reference Design**

- :git-hdl:`CN0561 HDL Reference Design <projects/cn0561>`
- `CN0561 HDL Project Documentation <https://analogdevicesinc.github.io/hdl/projects/cn0561/index.html>`__

**Linux Software**

- :git-linux:`AD4134 Linux driver <drivers/iio/adc/ad4134.c>`
- :git-linux:`AD4134 devicetree binding <Documentation/devicetree/bindings/iio/adc/adi,ad4134.yaml>`
- :git-linux:`ZedBoard Linux device tree <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad4134.dts>`

Schematic, PCB Layout, Bill of Materials
-----------------------------------------

- :adi:`EVAL-CN0561-ARDZ Design & Integration Files <cn0xxx-designsupport>`

  - Schematics
  - PCB Layout
  - Bill of Materials

More Information and Useful Links
----------------------------------

- :adi:`CN0561 Circuit Note Page <CN0561>`
- :adi:`CN0561 Design Support Package <CN0561-DesignSupport>`
- :adi:`AD4134 Product Page <AD4134>`
- :adi:`ADG5462F Product Page <ADG5462F>`
- :adi:`ADR444 Product Page <ADR444>`
- :adi:`ADG3308 Product Page <ADG3308>`
- :adi:`LT3092 Product Page <LT3092>`
- :adi:`LTC6373 Product Page <LTC6373>`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
