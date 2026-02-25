.. _ad9082-fmca-ebz:

AD9082-FMCA-EBZ User Guide
============================

Introduction
------------

The :adi:`AD9082-FMCA-EBZ <EVAL-AD9082>` is an FMC evaluation board for the
:adi:`AD9082` Mixed-Signal Front End (MxFE™). The :adi:`AD9082` is a highly
integrated device featuring four 16-bit, 12 GSPS RF DAC cores and two 12-bit,
6 GSPS RF ADC cores (4D2AC model). A 2D2AC model (2 DACs, 2 ADCs) is also
supported. The evaluation board connects to an FPGA carrier through an FMC HPC
connector and supports both JESD204B (8B10B) and JESD204C (64B66B) serial
interfaces.

The :adi:`AD9082` is well suited for wideband and multiband direct-to-RF
applications requiring simultaneous transmission and reception. The device
features up to 8 transmit and 8 receive lanes running at up to 24.75 Gbps per
lane (JESD204C), on-chip clock multiplier, and extensive DSP capability
including digital up/down converters (DUC/DDC), programmable FIR filters, and
NCOs.

Supported Devices
-----------------

- :adi:`AD9082`
- :adi:`AD9207` (companion ADC)
- :adi:`AD9177` (companion DAC)

Supported Carriers
------------------

- :xilinx:`VCK190 <products/boards-and-kits/vck190.html>` — FMC+ Slot
- :xilinx:`VCU118 <products/boards-and-kits/vcu118.html>` — FMC+ Slot
- :xilinx:`VPK180 <products/boards-and-kits/vpk180.html>` — FMC+ Slot
- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>` — FMC HPC Slot (JESD204B only)
- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` — FMC HPC Slot (JESD204B only)

.. note::

   JESD204B and JESD204C (64B66B) are both supported for VCK190, VCU118, and
   VPK180. Only JESD204B (8B10B) is supported for ZC706 and ZCU102.

Hardware Overview
-----------------

The AD9082-FMCA-EBZ shares the same PCB layout as the AD9081-FMCA-EBZ. The
key difference is the mounted MxFE device: the AD9082-FMCA-EBZ carries the
:adi:`AD9082` (4D2AC: 4 DACs, 2 ADCs), while the AD9081-FMCA-EBZ carries the
:adi:`AD9081` (4D4AC: 4 DACs, 4 ADCs).

Board summary:

- **Power delivery**: via FMC connector (uModule and LDO regulators)
- **Analog front-end balun**: BALH-0009SMG
- **Clock input balun**: SMP + BAL-0416
- **On-board crystal oscillator**: 100 MHz (used with on-board HMC7044)
- **Clock chip**: HMC7044 — provides DAC/ADC clocks and FPGA SERDES reference clocks
- **VADJ range**: 1.2V – 3.3V

.. image:: ../images/eval_ad9082.png
   :align: center
   :width: 450

The complete hardware user guide is available at
:adi:`UG-1829 <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`.

Thermal Considerations
~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD9082` can consume up to 13 W in some operating modes, causing die
temperature to approach its 120 °C maximum. A heat sink with integrated fan is
shipped with the evaluation board. Install the fan/heat sink before first use:

1. Remove the blue frame clip by lifting the metal tab free.
2. Peel off the thin plastic tape to expose the adhesive on the heat sink base.
3. Center the heat sink over the IC package, clear of the RF baluns, and press
   firmly for 10 seconds.
4. Connect the fan power cable.

The fan starts spinning when power is applied. If the fan does not spin, the
two mounting screws may be over-tightened — loosen them slightly with a
Phillips screwdriver.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The schematic is available at
:adi:`ad9081-mxfe-fmca-revc-eval-board-schematic.pdf <media/en/technical-documentation/eval-board-schematic/ad9081-mxfe-fmca-revc-eval-board-schematic.pdf>`.

Design files (schematic, layout, BOM) for both EVAL-AD9081 and EVAL-AD9082 are
available in the archive
:adi:`ad9081-ad9082.zip <media/en/evaluation-documentation/evaluation-design-files/ad9081-ad9082.zip>`.

JESD204B/C Interface
--------------------

The :adi:`AD9082` supports both JESD204B (8B10B encoding) and JESD204C
(64B66B encoding) serial data interfaces. The configurable link parameters are:

- **JESD_MODE**: ``8B10B`` (JESD204B) or ``64B66B`` (JESD204C)
- **[RX/TX]_LANE_RATE**: lane rate in Gbps for the RX (MxFE → FPGA) and TX
  (FPGA → MxFE) links
- **REF_CLK_RATE**: reference clock frequency in MHz for 64B66B mode
  (LANE_RATE / 66)
- **[RX/TX]_JESD_M**: number of converters per link
- **[RX/TX]_JESD_L**: number of lanes per link
- **[RX/TX]_JESD_S**: number of samples per converter per frame
- **[RX/TX]_JESD_NP**: bits per sample (16-bit only)
- **[RX/TX]_NUM_LINKS**: number of links (equals number of MxFE devices)

All supported RX/TX link modes are documented in
:adi:`UG-1578 <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`.

HDL Reference Design
--------------------

The HDL reference design is shared with the AD9081-FMCA-EBZ project.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/ad9082_fmca_ebz`

HDL Documentation
~~~~~~~~~~~~~~~~~

- `AD9081/AD9082 HDL Reference Design Documentation <https://analogdevicesinc.github.io/hdl/projects/ad9081_fmca_ebz/index.html>`__

Linux Software Support
----------------------

Linux Driver
~~~~~~~~~~~~

The :adi:`AD9082` is supported by the AD9081/AD9082 MxFE Linux IIO driver:

- :git-linux:`drivers/iio/adc/ad9081.c`

The driver exposes the device through the IIO (Industrial I/O) subsystem and
supports both the transmit (DAC) and receive (ADC) paths.

Software Tools
~~~~~~~~~~~~~~

The evaluation board is supported by the Libiio library, which is
cross-platform (Windows, Linux, macOS) with bindings for C, C#, Python, and
MATLAB. Common tools include:

- :ref:`iio-oscilloscope` — GUI for visualizing IIO device data (FFT, time domain)
- :external+pyadi-iio:doc:`index` — Python bindings for IIO devices

Evaluation with ACE Software
-----------------------------

The :adi:`AD9082` evaluation board is designed to work with the ADS9-V2EBZ
FPGA-based data capture board and the
`ACE <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`__
(Analysis, Control, Evaluation) software platform from Analog Devices.

Equipment Needed
~~~~~~~~~~~~~~~~

- PC running Windows with a USB 3.0 port
- AD9082-FMCA-EBZ evaluation board
- ADS9-V2EBZ FPGA-based data capture board
- USB 3.0 cable (Type-A to Type-B)
- Low phase-noise signal generator for ADC input
- Low phase-noise clock source (if using external direct clock mode)
- SMA and SMP cables as required

Required Documents
~~~~~~~~~~~~~~~~~~

- :adi:`AD9082 Datasheet <media/en/technical-documentation/data-sheets/AD9082.pdf>`
- :adi:`UG-1578, AD9081/AD9082 Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
- :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`

ACE Plugin Installation
~~~~~~~~~~~~~~~~~~~~~~~~

1. Download and install
   `ACE <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`__
   if not already installed.
2. Download the AD9081/AD9082 ACE plugin from the
   :adi:`EVAL-AD9082 software section <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9082.html#eb-relatedsoftware>`
   or install it via ACE's Plugin Manager (Tools > Manage Plug-Ins).
3. Connect the ADS9-V2EBZ to the PC via a USB 3.0 cable and power it on.
4. Launch ACE. The AD9081/AD9082 plugin icon should appear on the start page
   if the hardware is detected.

.. figure:: ace_start_page.png
   :align: center
   :width: 250

   ACE start page showing the MxFE plugin

5. Click the plugin icon to open the Board View. Click "Program FPGA Image"
   to load the FPGA bitstream for communicating with the evaluation board.

.. figure:: ace_board_view.png
   :align: center
   :width: 500

   ACE Board View for the AD9081/AD9082 evaluation board

Clocking Modes
~~~~~~~~~~~~~~

The evaluation board supports two clocking modes:

- **On-board clocking (HMC7044 + on-chip PLL)**: The on-board 100 MHz crystal
  oscillator feeds the HMC7044 clock chip, which generates the DAC/ADC clocks
  and FPGA SERDES reference clocks. This is the default mode and requires no
  external clock source.
- **External direct clock**: An external clock source is connected directly to
  the MxFE device, bypassing the HMC7044 and on-chip PLL. This mode supports
  a wider range of operating configurations but requires external
  instrumentation.

Refer to
:adi:`UG-1829 <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`
for details on switching between clocking modes.

Setting Up a Narrowband Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following procedure configures the :adi:`AD9082` in a single-band
250 MSPS I/Q data rate setup with direct RF sampling. The on-board HMC7044
and on-chip PLL provide the DAC and ADC clocks.

.. figure:: narrowband_setup.png
   :align: center
   :width: 600

   Narrowband mode setup block diagram

**Configuring the device in ACE:**

1. Open ACE and click the AD9081/AD9082 plugin icon.
2. Double-click the chip block in the Board View to open the Chip View.
3. In the Quick Configuration section, set the parameters as shown in the
   figures below. The steps are numbered in sequence.

.. figure:: 3_chip_setup1.png
   :align: center
   :width: 400

   Quick Configuration step 1: JESD204 setup

.. figure:: 4_chip_setup2.png
   :align: center
   :width: 400

   Quick Configuration step 2: clock configuration

.. figure:: 5_chip_setup3.png
   :align: center
   :width: 400

   Quick Configuration step 3: ADC/DAC configuration

.. figure:: 6_chip_setup4.png
   :align: center
   :width: 400

   Quick Configuration step 4: NCO and DDC/DUC configuration

4. Click **Apply**.

.. image:: 7_Apply.png
   :align: center
   :width: 200

5. Wait several seconds for ACE and the ADS9-V2EBZ hardware to configure the
   device. When configuration is complete, the Chip View displays the status
   readouts.

.. figure:: 8_chip_view_after_apply.png
   :align: center
   :width: 500

   Chip View status readouts after successful configuration

**Capturing an ADC FFT:**

6. Click **Proceed to Analysis** to open the Analysis view.
7. With no input signal connected, capture an FFT to verify the noise floor.

.. figure:: 9_analysis_view.png
   :align: center
   :width: 500

   Analysis view showing a no-input FFT

8. Connect a signal generator to any ADC input. Set the frequency to
   3.207 GHz (the NCO is tuned to 3.2 GHz). Adjust the amplitude to achieve
   approximately -1 dBFS at the ADC input.

**Setting up DAC output with DPG Lite:**

9. Open DPG Downloader Lite. Select a Single Tone waveform and configure the
   GUI for the desired output frequency.
10. Press the **Play** button to enable the DAC output.
11. Use an SMA cable to connect a DAC output to an ADC input on the
    evaluation board for an external loopback test. Capture the FFT in ACE
    to verify the DAC output.

Setting Up a Wideband Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The wideband mode configures the :adi:`AD9082` in a single-band 1000 MSPS
I/Q data rate setup with direct RF sampling. The setup procedure is similar
to the narrowband case, with different Quick Configuration parameters.

.. figure:: wideband_setup.png
   :align: center
   :width: 600

   Wideband mode setup block diagram

In the Quick Configuration section, set the JESD204 parameters for the higher
data rate and update the clock configuration accordingly. Click **Apply** and
wait for the device to be configured. Then proceed to DPG Lite setup and ADC
FFT capture as described in the narrowband procedure above.

ADC Performance Note
--------------------

The :adi:`AD9082` ADC noise performance depends on the operating configuration.
When the DACs are active (transceiver mode), ADC noise is higher than in
receive-only mode. The figures below show the ADC FFT at 2.7 GHz (-1 dBFS)
under each condition:

.. figure:: ad9082_2p7ghz_adconlyfft.png
   :align: center

   2.7 GHz -1 dBFS tone: AD9082 configured in receive-only mode

.. figure:: ad9082_2p7ghz_trxmodefft.png
   :align: center

   2.7 GHz -1 dBFS tone: AD9082 configured as a transceiver (DACs ON)

Programmable Filter (PFILT)
---------------------------

The :adi:`AD9082` includes a Programmable FIR Filter (PFILT) that can be used
for bandpass compensation and ADC response equalization. PFILT coefficients are
designed in MATLAB using the
`High Speed Converter Toolbox <https://github.com/analogdevicesinc/HighSpeedConverterToolbox>`__
and loaded into the ACE plugin in hexadecimal format (2's complement).

To use the PFILT:

1. Design the compensation filter in MATLAB using
   ``MxFEADCCompensationFilterDesign_BPF.m`` from the HighSpeedConverterToolbox.
2. Convert the MATLAB-generated decimal coefficients to 2's complement
   hexadecimal format.
3. In the ACE plugin chip view, open the Programmable Filter configuration
   block, select the filter mode (Real N Tap for I or Q), and load the
   coefficient file.
4. Click "Configure Filter Block" and wait several seconds for the
   coefficients to load into the PFILT hardware.
5. Proceed to the Analysis view to capture an FFT and verify the filter
   response.

Refer to :adi:`UG-1829 <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`
for the full bandwidth ADC use case configuration required before loading PFILT
coefficients.

Troubleshooting
---------------

Board Not Functioning Properly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Verify the evaluation board is firmly seated in the FMC connector.
- After ACE programs the FPGA, power is supplied to the evaluation board.
  Confirm that all power-rail LEDs are lit.

.. figure:: ceboard_power_rail_led.jpg
   :align: center
   :width: 500

   LEDs denoting power to the various rails on the evaluation board

- Verify the eRPC server connected successfully: the Chip Info UID should
  read a non-zero value. If UID reads 0x0, power-cycle the board and restart
  all software.

ACE Is Slow to Capture Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Use a USB 3.0 cable between the ADS9-V2EBZ board and the PC.
- Connect to a USB 3.0 port on the PC.
- Restart all software and hardware if the issue persists.

Unable to Capture Data After Device Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If only four of six LEDs are lit on the FPGA board after device setup, data
capture may have failed.

.. figure:: ads9v2_unsuccessful_capture.jpg
   :align: center
   :width: 400

   LED status on ADS9-V2EBZ following an unsuccessful data capture

When using an external direct clock:

- Verify the clock and refclock frequencies are set as described in UG-1829.
- Check all cable connections are secure.
- If the problem persists, open DPG Lite, download a tone, then retry capture.
  A successful capture shows all LEDs lit.

.. figure:: ads9v2_successful_capture.jpg
   :align: center
   :width: 400

   LED status on ADS9-V2EBZ following a successful data capture

HMC7044 Configuration Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "HMC7044 Configuration Error" appears in ACE when the selected mode
requires a reference frequency that cannot be generated from the on-board
100 MHz crystal oscillator via the HMC7044. Not all modes in UG-1578 are
achievable with the on-board clocking.

.. figure:: hmc7044_config_error.png
   :align: center
   :width: 500

   HMC7044 Configuration Error (REFCLK value cannot be supported using a
   100 MHz crystal oscillator)

To use such modes, switch to an external direct clock, which bypasses the
HMC7044.

ACE Does Not Auto-Detect Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the hardware is not auto-detected after powering the ADS9-V2EBZ and
starting ACE, try a different USB 3.0 cable before reinstalling the plugin or
the full ACE package.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B/C High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__
- :adi:`UG-1578, AD9081/AD9082 Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
- :adi:`UG-1829, Evaluation Board User Guide <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`
- :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
- :adi:`JESD204C Primer: Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
- :adi:`JESD204C Primer: Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Support
-------

Analog Devices provides online support for the reference design via the
EngineerZone forums:

- :ez:`FPGA Reference Designs <fpga>` — HDL reference design questions
- :ez:`Linux Software Drivers <linux-software-drivers>` — Linux driver and device tree questions

.. esd-warning::
