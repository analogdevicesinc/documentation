.. imported from: https://wiki.analog.com/resources/eval/ad9265-fmc-125ebz

.. _ad9265-fmc:

AD9265-FMC User Guide
=====================

.. warning::

   Support for the AD9265-FMC is discontinued starting with the 2022_R2 Kuiper
   Linux release. It will not be supported in future releases. The HDL project
   source code is still available on the main branch.

Introduction
------------

The :adi:`AD9265` is a 16-bit, 125 MSPS analog-to-digital converter (ADC)
featuring a wide bandwidth differential sample-and-hold analog input amplifier
supporting a variety of user-selectable input ranges. This reference design
includes a data capture interface and the external DDR-DRAM interface for
sample storage. It allows programming the device and monitoring its internal
status registers.

The board provides three possible clock paths for clocking the AD9265:

- External passive clock (default)
- Optional active clock path using the AD9517
- Optional oscillator

Features
~~~~~~~~

- Full featured evaluation board for the :adi:`AD9265`
- SPI interface for setup and control
- External, on-board oscillator, and :adi:`AD9517` clocking options
- Balun/transformer or amplifier input drive option
- LDO regulator or switching power supply options
- VisualAnalog and SPI controller software interfaces

Supported Devices
-----------------

- :adi:`AD9265`

Supported Carriers
------------------

- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` LPC Slot

Equipment Needed
----------------

- Analog signal source (such as Rohde & Schwarz SMA 100A Signal Generator)
- Antialiasing filter (narrow-band band-pass filter with 50 ohm terminations)
- Sample clock source (if not using the on-board oscillator)
- 12 V power supply
- 1-meter SMA cable
- PC running Windows
- USB Mini-B cable
- :adi:`AD9265` evaluation board (AD9265-FMC-125EBZ)
- :adi:`SDP <sdp>` System Development Platform Kit (EVAL-SDP-CH1Z)

Typical Measurement Setup
-------------------------

.. figure:: ad9265_fmc_125ebz_typical_setup.jpg
   :align: center

   Evaluation board connection -- AD9265-FMC-125EBZ (left) and
   EVAL-SDP-CH1Z SDP-H1 (right)

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as
follows:

#. Connect the evaluation board to the data capture board, as shown in the
   figure above.
#. Connect one 12 V switching power supply to the EVAL-SDP-CH1Z SDP-H1 board.
#. Connect the SDP-H1 board to the PC with a USB cable (connect to J1).
#. To use the on-board clock, connect Pin 1 and Pin 3 on P2. If using an
   external clock signal, remove the connector on P2 and use a clean signal
   generator connected to J201.
#. On the ADC evaluation board, use a clean signal generator with low phase
   noise to provide an input signal to the input channel (J100). Use a 1 m,
   shielded, RG-58, 50 ohm coaxial cable. For best results, use a narrow-band,
   band-pass filter with 50 ohm terminations and an appropriate center
   frequency.

Software Setup
--------------

Two software tools are used to configure and capture data from the AD9265:

- `VisualAnalog <https://www.analog.com/en/design-center/interactive-design-tools/visualanalog.html>`__
  -- sets up the data capture and displays FFT results
- `SPIController <https://www.analog.com/en/design-center/interactive-design-tools/spicontroller.html>`__
  -- configures the ADC registers via SPI

Setting Up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Start VisualAnalog.
#. Select **AD9265** and double-click **FFT** in the New Canvas window.
#. Click **Settings** under the **ADC Data Capture** section.
#. Set the device to **AD9265**.
#. Navigate to **Capture Board** and browse for the FPGA image file
   (``ad9265_sdph1.bin``).
#. Click **Program** and verify that LED0 on the SDP-H1 lights up. Then click
   **OK**.

Setting Up the SPI Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Start SPIController.
#. If a message appears saying "Read Test Failure", select **Ignore**.
#. Click **File > Cfg Open** and select the file named
   ``ad9265_16bit_125MSspiR03.cfg``.
#. If a second "Read Test Failure" message appears, select **Ignore** again.
#. Click **Config > Controller Dialog**.
#. Deselect **SDO Active** and click **OK**.
#. Click **Read Chip ID** and **Read Chip Grade** to verify communication.
#. Return to VisualAnalog and click the **Play** button to begin data capture.

Adjusting the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Adjust the amplitude of the input signal so that the fundamental is at
   approximately -1.0 dBFS. Examine the **Fund Power** reading in the left
   panel of the **VisualAnalog Graph - AD9265 Average FFT** window.
#. Click the disk icon within the **Graph** window to save the performance plot
   data as a .csv file for further analysis.

.. figure:: ad9265_typical_window.png
   :align: center

   VisualAnalog FFT graph window showing typical AD9265 performance

Troubleshooting
~~~~~~~~~~~~~~~

**If the FFT plot appears abnormal:**

- If you see a normal noise floor when you disconnect the signal generator
  from the analog input, ensure you are not overdriving the ADC. Reduce the
  input level if necessary.
- In VisualAnalog, click the **Settings** button in the **Input Formatter**
  block. Check that **Number Format** is set to the correct encoding (offset
  binary by default).

**If the FFT appears normal but performance is poor:**

- Make sure that an appropriate band-pass filter is used on the analog input.
- Make sure that the signal generators for the clock and analog input are clean
  (low phase noise).
- Change the analog input frequency slightly if noncoherent sampling is being
  used, or use coherent frequencies.
- Make sure the SPI configuration file matches the product being evaluated.
- Make sure there is no extra stress or torque on the clock and analog input
  connectors.

**If the FFT window remains blank after Run is clicked:**

- Make sure the evaluation board is securely connected to the SDP-H1 board.
- Make sure the FPGA has been programmed by verifying that the **FPGA_DONE**
  LED is illuminated on the SDP-H1 board. If not, reprogram the FPGA through
  VisualAnalog. If the LED still does not illuminate, disconnect the USB and
  power cord for 15 seconds, reconnect, and repeat the setup process.
- Make sure the correct FPGA bin file was used.
- Verify that the correct sample rate is programmed. Click **Settings** in the
  **ADC Data Capture** block and confirm the **Clock Frequency** is correct.
- Ensure the ADC has a valid clock input.

HDL Reference Design
--------------------

The reference design uses the :git-hdl:`AXI AD9265 IP core <library/axi_ad9265>`
to interface the :adi:`AD9265` ADC in LVDS mode. The IP core handles the LVDS
deserialization, data formatting, and provides an AXI-based register map for
monitoring and control. Data is moved from the IP core output to memory via
DMA.

The top module instantiates the LVDS interface module, the channel processing
module, the ADC common register map, the AXI handling interface, and a delay
control module.

The LVDS interface module handles the input clock, data, and over-range signals
using IO block primitives. Each data line passes through an IDELAYE2 block for
independent delay adjustment through the delay controller register map. The
channel processing module implements PRBS monitoring (PN9 and PN23), data
format conversion, and DC filtering.

IP Core Configuration
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     - Default Value
   * - ``ID``
     - Core ID, should be unique for each AD9265 IP in the system
     - 0
   * - ``DEVICE_TYPE``
     - Select between 7 Series (1), Ultrascale (2), or Ultrascale+ (3) devices
     - 0
   * - ``ADC_DATAPATH_DISABLE``
     - If set, datapath processing is bypassed and output data is taken
       directly from the AD9265
     - 0
   * - ``IO_DELAY_GROUP``
     - Delay group name for the delay controller
     - ``"adc_if_delay_group"``

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9265_fmc`
- :git-hdl:`library/axi_ad9265`

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad9265_fmc/zc706
   make

Software Support
----------------

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/ad9265-fmc-125ebz`

The No-OS project provides bare metal support for the AD9265-FMC. To set up
the software:

#. Clone the No-OS GitHub repository
#. Build the project located at ``projects/ad9265-fmc-125ebz``
#. Follow the instructions in the
   `ADI No-OS build guide <https://analogdevicesinc.github.io/no-OS/doxygen/build_guides.html>`__

More Information
----------------

- :adi:`AD9265 Product Page <AD9265>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `AXI AD9265 IP Core Documentation <https://analogdevicesinc.github.io/hdl/library/axi_ad9265/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
