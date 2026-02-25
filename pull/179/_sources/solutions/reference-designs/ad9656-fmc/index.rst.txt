.. _ad9656-fmc:

AD9656-FMC User Guide
=====================

Introduction
------------

The :adi:`AD9656` is a quad 16-bit, 125 MSPS analog-to-digital converter (ADC)
with an on-chip sample and hold circuit designed for low cost, low power, small
size, and ease of use. The AD9656EBZ board is built around the AD9656 chip and
pairs with a carrier board through an FMC connector. The ADC chip uses the
JESD204B protocol to transfer the data to the carrier board. The SPI protocol
is used by the carrier board to configure the parameters from the register file
of the ADC and the two clock chips.

Features
~~~~~~~~

- SPI interface for setup and control
- External, on-board oscillator
- On-board LDO regulator, needing a single external 6 V, 2 A dc supply
- ADC VREF configurable for ADC-internal reference, on-board reference, or
  off-board reference
- VisualAnalog and SPIController software interfaces

Supported Devices
-----------------

- :adi:`AD9656`

Supported Carriers
------------------

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`

Equipment Needed
----------------

- Analog signal source(s) and antialiasing filter(s)
- Sample clock source (if not using the on-board crystal oscillator)
- Switching power supply (6.0 V, 2.5 A) for the AD9656EBZ
- Switching power supply (12 V, 3.3 A) for the HSC-ADC-EVALEZ
- PC running Windows
- USB 2.0 port
- :adi:`AD9656 <EVAL-AD9656>` evaluation board (AD9656EBZ)
- :adi:`HSC-ADC-EVALEZ <hsadcevalboard>` FPGA-based data capture kit

Typical Measurement Setup
-------------------------

.. figure:: ad9656_typical_setup.png
   :align: center

   Evaluation board connection -- AD9656EBZ (left) and HSC-ADC-EVALEZ (right)

It is critical that the signal sources used for the analog input and clock have
very low phase noise (ideally approximately 100 fs rms jitter) to realize the
optimum performance of the signal chain. Proper filtering of the analog input
signal to remove harmonics and lower the integrated or broadband noise at the
input is necessary to achieve the specified noise performance.

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~

Before using the software for testing, configure the evaluation board as
follows:

#. Connect the evaluation board to the data capture board, as shown above.
#. On the ADC evaluation board, confirm that the jumpers are installed as
   shown in the jumper settings figure below.
#. The AD9656EBZ can be powered in one of three ways. The default is to
   have the board obtain its power from the HSC-ADC-EVALEZ through the FMC
   connector. For this configuration, jumper Pin 1 to Pin 2 on both P101 and
   P103.
#. Connect the 12 V, 3.3 A switching power supply to the HSC-ADC-EVALEZ
   board.
#. Connect the HSC-ADC-EVALEZ board (P702) to the PC using a USB cable.
#. On the ADC evaluation board, use a clean signal generator with low phase
   noise to provide an input signal to the desired channel(s). Use a shielded,
   RG-58, 50 ohm coaxial cable (optimally 1 m or shorter) to connect the
   signal generator. For best results, use a narrow-band, band-pass filter
   with 50 ohm terminations and an appropriate center frequency.

Power Supplies
^^^^^^^^^^^^^^

The AD9656EBZ can obtain its power through three configurations:

- **FMC connector (default)**: P101 and P103 both have Pin 1 tied to Pin 2.
  Power is sourced from the HSC-ADC-EVALEZ through the FMC connector. Do not
  connect the 6 V wall supply when using this mode.
- **Wall-mountable 6 V supply**: P101 and P103 both have Pin 2 tied to Pin 3.
  Connect the supply to P102 (2.1 mm inner diameter jack). The 6 V supply is
  fused and conditioned on the PCB before connecting to the LDO regulators.
- **External bench supplies**: Remove the E104, E105, E106, and E108 ferrite
  beads to disconnect the on-board LDOs. Install P104 and P105 headers and
  populate E110, E111, E112, and E113. Provide 1.8 V, 0.5 A for
  1.8V_DUT_AVDD, 1.8V_DRVDD, and 1.8V_DVDD (separate supplies recommended),
  and 3.3 V, 0.5 A for 3.3V_DIG.

.. important::

   When changing the configuration of P101 and P103, remove both jumpers first
   and then place them in the desired positions.

Input Signals
^^^^^^^^^^^^^

The four channel inputs on the evaluation board are set up for a double
balun-coupled analog input with a 50 ohm impedance. When connecting the ADC
clock and analog source, use clean signal generators with low phase noise (such
as the Rohde & Schwarz SMA or equivalent). Use a shielded, RG-58, 50 ohm
coaxial cable (optimally 1 m or shorter). A multipole, narrow-band band-pass
filter with 50 ohm terminations is recommended, connected as close to the
evaluation board as possible.

Clock
^^^^^

The default clock input circuit is derived from an on-board 125 MHz crystal
oscillator (Y801) feeding through a transformer-coupled circuit. The external
clock input (J302) is 50 ohm terminated and ac-coupled for single-ended
sinusoidal inputs. The transformer converts the single-ended input to a
differential signal that is clipped by CR301 before entering the ADC clock
inputs. The :adi:`AD9656` ADC has an internal clock divider (programmable divide
ratios of 1 through 8) to facilitate higher frequency clocks. When using the
internal divider with a higher input clock frequency, remove CR301 to preserve
the slew rate.

To use an external clock source, remove C302 (optionally) and Jumper J304 to
disable the oscillator, then connect the external clock source to J302
(labeled CLOCK+). Typical evaluation boards accept approximately 2.8 V p-p or
13 dBm sine wave input for the clock.

Jumper Settings
~~~~~~~~~~~~~~~

Set the jumper settings on the evaluation board for the required operating
modes before powering on.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Jumper
     - Description
   * - P101, P103
     - Determines the power source. Pin 1 to Pin 2: power from HSC-ADC-EVALEZ
       via FMC. Pin 2 to Pin 3: power from wall supply at P102. Unjumpered:
       external bench supplies via P104/P105.
   * - J304
     - Enables the on-board crystal oscillator. Remove this jumper (and
       optionally C302) if using an external off-board clock source.
   * - J206
     - Selects between internal VREF and external VREF. Connect Pin 3
       (DUT_SENSE) to Pin 5 (GND) for the ADC internal reference (default
       1 V, programmable from 1 V to 1.4 V via SPI Register 0x18 Bits[7:6]).
       For the on-board buffered reference, connect Pin 2 to Pin 1 and Pin 4
       to Pin 6, then adjust with potentiometer R247. For an external
       off-board reference, connect Pin 2 to Pin 1 and apply 1.0 V to 1.4 V
       to Pin 4.

.. figure:: ad9656_default_jumpers.png
   :align: center

   Default jumper connections for the AD9656EBZ board

Software Setup
--------------

Two software tools are used to configure and capture data from the AD9656:

- `VisualAnalog <https://www.analog.com/en/design-center/interactive-design-tools/visualanalog.html>`__
  -- sets up the data capture and displays FFT results
- `SPIController <https://www.analog.com/en/design-center/interactive-design-tools/spicontroller.html>`__
  -- configures the ADC registers via SPI

Setting Up the ADC Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Start VisualAnalog. The appropriate part type should be listed in the status
   bar of the **New Canvas** window. Select the template that corresponds to
   the type of testing to be performed (Average FFT is a good starting test).
#. After the template is selected, a message may appear asking if the default
   configuration can be used to program the FPGA. If this message appears,
   click **Yes**.
#. Click the **Expand Display** button (bottom right corner of the window) to
   view the canvas and associated functional blocks.
#. Click the **Settings** button on the **ADCDataCapture** block.
#. In the **General** tab, select **AD9656** as the device and enter the sample
   clock frequency (125 MHz default). Select the channels to test and the FFT
   capture depth (total of all channel capture depths cannot exceed 256k).
#. In the **Capture Board** tab, enter 60 in the **Fill Delay** field. Browse
   to the FPGA program file for the AD9656 (typically at
   ``C:\Program Files\Analog Devices\VisualAnalog\Hardware\HADv6\AD9656_hadv6fmc.mcs``).
   Click **Program**.
#. In the **Device** tab, check the **Enable Data Capture Controls** checkbox.
   Set **GTX RX Equalization** to 6, **Encode** to 125 MSPS, and **Number of
   lanes** to 2 Lanes (at least 2 lanes are required for 125 MSPS).

Setting Up the SPI Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open SPIController. If prompted for a configuration file, select the
   ``.cfg`` file whose name begins with AD9656. Verify the **CHIP ID(1)** box
   is filled to confirm the correct configuration is loaded.
#. Click the **New DUT** button.
#. In the **ADCBase0** tab, locate the **CLOCK DIVIDE(B)** box to configure the
   clock divide ratio if needed. Use the **MODES(8)** box to perform a Digital
   Reset if necessary (for example, after any interruption of the ADC clock).
#. In the **ADCBase1** tab, set the number of lanes. This must match the
   setting made in VisualAnalog.
#. Other settings on the **ADCBase0** tab and the **ADC A** through **ADC D**
   tabs can be used to configure individual channel modes. See the :adi:`AD9656`
   data sheet for details.
#. Invoke a **Digital Reset** before testing, then select **Chip Run** to
   return to normal operation.
#. To begin testing, click the **Run** or **Continuous Run** button in the
   VisualAnalog toolbar.

Adjusting the Input Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Adjust the amplitude of the input signal so that the fundamental is at the
   desired level. Examine the **Fund Power** reading in the left panel of the
   **VisualAnalog Graph - AD9656 FFT** window.
#. Repeat this procedure for other channels as desired.
#. Click the floppy-disk icon within the FFT window to save the performance
   data as a .csv file for plotting or analysis.

.. figure:: ad9656_fft_example.png
   :align: center

   VisualAnalog FFT graph window showing typical AD9656 performance

Troubleshooting
~~~~~~~~~~~~~~~

**Lack of SPI communication:**

- In the **Global** tab of SPIController, push the **Read** button in the
  **GENERIC READ/WRITE** window. This reads ADC register 0x00. If SPI
  communication is working and the ADC is powered, the value ``0x18``
  hexadecimal will appear. If the contents show ``0x00``, the ADC is not
  powered or SPI communication is not working.
- Check that there is correct power to the AD9656EBZ board and to the
  HSC-ADC-EVALEZ.
- Check that the USB cable is properly connected from the PC to the
  HSC-ADC-EVALEZ.
- The LED on the VisualAnalog **ADCDataCapture** block should be green. If it
  is red, push the USB button on the same block to refresh the connection.

**If the FFT plot appears abnormal:**

- Go to the **ADCBase0** tab and toggle **Chip Power Mode** in **MODES(8)**
  from **Chip Run** to **Reset** and back.
- If you see a normal noise floor when you disconnect the signal generator,
  ensure you are not overdriving the ADC. Reduce the input level if necessary.
- In VisualAnalog, check that the **Number Format** in the **Input Formatter**
  block matches the data format selected in the **SPIController ADCBase0
  OUTPUT MODE(14)** window (twos complement by default).

**If the FFT appears normal but performance is poor:**

- Make sure that an appropriate filter is used on the analog input.
- Make sure the signal generators for the clock and analog input are clean
  (low phase noise).
- Change the analog input frequency slightly if noncoherent sampling is being
  used.
- Make sure the SPI configuration file matches the product being evaluated.

**If the FFT window remains blank after Run is clicked:**

- Make sure the evaluation board is securely connected to the HSC-ADC-EVALEZ
  board.
- Verify the correct FPGA program was installed by clicking **Settings** in
  the **ADC Data Capture** block and checking the **FPGA** tab for the proper
  ``.mcs`` file (must contain "AD9656" in the filename).
- Verify the **CONFIG_DONE** LED is illuminated on the HSC-ADC-EVALEZ board.
  If not, reprogram the FPGA from the **FPGA** tab.
- On the AD9656EBZ, check the LED next to the reset button (S501). If it is
  not lit, push the reset button and try running again.

HDL Reference Design
--------------------

The reference design is a processor-based ARM embedded system. The cores are
programmable through an AXI-Lite interface. The data path consists of a DMA
interface for the receive path.

The digital interface consists of 4 receive lanes running at 2.5 Gbps. The
transceivers interface to the cores at 128 bits @ 62.5 MHz. The data is
received based on the configuration (programmable) from separate receive chains.

The ADC data is sent to the DDR via DMA. The core also supports PN monitoring
at the sample level. This is different from the JESD204B specific PN sequence.

The device control and monitor signals are interfaced to a GPIO module. The SPI
signals are controlled by a separate AXI-based SPI core.

Block Diagrams
~~~~~~~~~~~~~~

.. figure:: ad9656_block_diagram.png
   :align: center

   AD9656 block diagram

.. figure:: xilinx_block_diagram.png
   :align: center

   Xilinx block diagram

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9656_fmc`

Building the HDL Project
~~~~~~~~~~~~~~~~~~~~~~~~

The design is built upon ADI's generic HDL reference design framework. ADI
does not distribute pre-built bitstream files, so the project must be built
from source. Clone the HDL repository and, with the correct tools installed,
navigate to the project directory and run ``make``:

.. code-block:: bash

   cd hdl/projects/ad9656_fmc/zcu102
   make

Software Support
----------------

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/ad9656_fmc`
- :git-no-OS:`drivers/adc/ad9656`

The No-OS project provides bare metal support for the AD9656-FMC. The
following driver components are used:

- :git-no-OS:`AD9656 driver <drivers/adc/ad9656>`
- :git-no-OS:`AXI ADC core driver <drivers/axi_core/axi_adc_core>`
- :git-no-OS:`AXI DMAC driver <drivers/axi_core/axi_dmac>`
- :git-no-OS:`JESD204 driver <drivers/axi_core/jesd204>`
- :git-no-OS:`Xilinx platform drivers <drivers/platform/xilinx>`

To set up the software:

#. Clone the No-OS GitHub repository
#. Build the project located at ``projects/ad9656_fmc``
#. Follow the instructions in the
   `ADI No-OS build guide <https://analogdevicesinc.github.io/no-OS/doxygen/build_guides.html>`__

More Information
----------------

- :adi:`AD9656 Product Page <AD9656>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
