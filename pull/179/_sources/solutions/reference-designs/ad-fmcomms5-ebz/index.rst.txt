.. _ad-fmcomms5-ebz:

AD-FMCOMMS5-EBZ
================

The :adi:`AD-FMCOMMS5-EBZ` is an FMC board featuring two :adi:`AD9361` RF
Agile Transceivers, designed to demonstrate how to design a platform based on
multiple devices for MIMO applications. For systems requiring more than two
input or two output channels, multiple AD9361 devices and a common reference
oscillator are required.

.. image:: fmcomms5-loopback.jpg
   :align: center
   :width: 500

.. note::

   The AD-FMCOMMS5-EBZ uses a dual FMC connector. This means the base board
   requires two adjacent FMC connectors. Suitable base boards are ZC702,
   ZC706, and ZCU102.

Introduction
------------

For many Broadband Wireless Access (BWA) systems, MIMO operation and RF
beamforming are proven techniques for maximizing throughput and efficient
spectrum utilization. The AD-FMCOMMS5-EBZ provides 4 Rx and 4 Tx channels
using two synchronized :adi:`AD9361` devices.

The purpose of the AD-FMCOMMS5-EBZ is to provide a platform which demonstrates
how to connect and synchronize (at the RF side) multiple AD9361s for MIMO
applications. To help with algorithm and array processing development, there
are a variety of resources available, from MIMO encoding/decoding IP blocks to
`MATLAB Phased Array System Toolbox <https://www.mathworks.com/products/phased-array.html>`__.

If you are just starting a design, or investigating the AD9361 for the first
time, it is suggested to get familiar with the single AD9361 based platforms
(:ref:`AD-FMCOMMS2-EBZ <ad-fmcomms2-ebz>` or
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`) first.

Multi-Chip Synchronization
--------------------------

.. figure:: ad9361.svg
   :align: center

   AD9361 simplified block diagram

The AD9361 utilizes a fractional-N synthesizer in the baseband PLL block to
generate the desired sample rate. This synthesizer generates the ADC sample
clock, DAC sample clock, and baseband digital clocks from any reference clock
in the specified frequency range.

For MIMO systems requiring more than two input or two output channels, multiple
AD9361 devices and a common reference oscillator are required. Each AD9361
includes its own baseband PLL that generates sampling and data clocks from the
reference clock input, so an additional control mechanism is required to
synchronize multiple devices.

Clock Distribution
~~~~~~~~~~~~~~~~~~

On the AD-FMCOMMS5-EBZ, an :adi:`ADCLK846` (U301) Clock Fanout Buffer accepts
a 40 MHz Rakon oscillator (Y301) and drives:

- ``XTALN_A`` to the "A" AD9361 device (XTALN pin floating per datasheet)
- ``XTALN_B`` to the "B" AD9361 device
- ``REF_CLK_FMC`` back to the FMC connector

The ``SYNC_IN`` pin on the AD9361 is driven directly from the FPGA,
length-matched to both AD9361 devices, so the edge hits both parts at the same
time. The total number of devices that can be connected in parallel is limited
only by the drive capability of the clock and logic signals.

MCS Software
~~~~~~~~~~~~

From a software perspective, MCS requires programming a few registers in the
correct order and asserting ``SYNC_IN`` at the right time.

**Linux**: The
`libad9361-iio <https://github.com/analogdevicesinc/libad9361-iio>`__ helper
library manages the MCS sequence. The implementation is in
`ad9361_multichip_sync.c <https://github.com/analogdevicesinc/libad9361-iio/blob/master/ad9361_multichip_sync.c>`__.

**No-OS**: Before initializing the parts, set
``AD9361_InitParam.gpio_sync`` accordingly. After initialization, call
``ad9361_do_mcs(phy_master, phy_slave)`` to synchronize both devices.

When MCS Must Be Repeated
~~~~~~~~~~~~~~~~~~~~~~~~~

Any change that can affect device synchronization requires repeating the MCS
sequence:

- Baseband PLL (BBPLL) rate changes (device data rates)
- FIR Filter enable/disable when the BBPLL must change
- Changing either Tx or Rx LO settings

RF Phase Synchronization
------------------------

The AD9361 does not include internal RF synchronization. The ability to
synchronize the internal RF local oscillators requires external assistance.
There are two methods to solve this:

#. **Internal LOs + FPGA correction**: Measure the phase difference in the
   internal LOs and correct in the FPGA
#. **External LO**: Use an external LO signal (e.g., :adi:`ADF5355`)

Internal LOs + FPGA Correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FMCOMMS5 board includes two :adi:`ADG918` wide band (-3 dB at 4 GHz)
switches that connect either Tx1B from either AD9361 device to Rx1C on either
AD9361 device. This allows four different measurement states:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Output \\ Input
     - Device A (Rx1C)
     - Device B (Rx1C)
   * - Device A (Tx1B)
     - **1**
     - **2**
   * - Device B (Tx1B)
     - **3**
     - **4**

These states are controlled by 2 GPIO pins from the FPGA (``CAL_SW_1`` and
``CAL_SW_2``).

.. figure:: switches.png
   :align: center

   AD-FMCOMMS5-EBZ calibration switch matrix

Using these switches, the phase difference between the two receivers can be
measured using a common transmitter reference. The HDL reference design
includes a loopback path for time-domain alignment between Rx and Tx. The
phase correction is applied through internal phase shifters in the HDL
reference design's ADC and DAC cores.

The calibration procedures are implemented in both IIO-Oscilloscope and in the
`libad9361 phase sync library <https://github.com/analogdevicesinc/libad9361-iio/blob/master/ad9361_fmcomms5_phase_sync.c>`__.

When Phase Calibration Must Be Repeated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Phase calibration must be repeated after any change that can cause the RF LOs
to go out of phase:

- Changes to the internal RX/TX RFPLLs (LOs)
- After MCS is performed

.. note::

   TDD mode (where the LOs get turned off) cannot be used with RF-level phase
   coherency. Users should keep the LOs on by using FDD mode.

External LO (ADF5355)
~~~~~~~~~~~~~~~~~~~~~

When using an external LO such as the :adi:`ADF5355` on the FMCOMMS5, the
transceiver still has a random phase relation, but it is limited to a 0 or
180 degree offset. This offset is due to the input divider on the external LO
input pins and cannot be bypassed. The phase relationship is randomized when
the transceivers are power cycled or the external LO power drops below a
certain threshold.

**Rev C**: The :adi:`ADF5355` is populated on the board. Select the appropriate
device tree on the SD Card to enable control via IIO. An :adi:`HMC744` buffer
distributes the LO to both AD9361 devices.

**Rev B**: The board has layout provisions for the ADF5355. In the interim, an
external LO signal can be injected into J302 via the Inphi 13617 distributor.

Hardware
--------

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Rev C**:

- `AD-FMCOMMS5-EBZ Design & Integration Files <https://www.analog.com/media/en/reference-design-documentation/design-integration-files/ad-fmcomms5-ebz-designsupport.zip>`__
  (Schematic, PCB Layout, Bill of Materials, Allegro Project)

**Rev B**:

- :dokuwiki:`Rev B Schematic <resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_schematic.pdf>`
- :dokuwiki:`Rev B BOM <resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5-bom.xls>`
- :dokuwiki:`Rev B Build Files <resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_build.zip>`
- :dokuwiki:`Rev B Allegro Board File <resources/eval/user-guides/ad-fmcomms5-ebz/fmcomms5_revb.7z>`

Hardware Revisions
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Revision
     - Notes
   * - Rev-A/B
     - Unmatched trace lengths, RF switches limited to < 900 MHz
   * - Rev-C
     - Phase-matched traces, improved RF switches for higher frequencies

.. warning::

   Rev-B has an errata: :adi:`ADF5355` pin 5 (AVDD) is a floating node. The
   fix is to short pin 5 (AVDD) with pin 4 (CE) to make a connection to
   VDD_EXT_LO_3P3.

   .. figure:: fmcomms5_rework.png
      :align: center

      AD-FMCOMMS5-EBZ Rev B ADF5355 rework

I/O Voltage
~~~~~~~~~~~~

The AD-FMCOMMS5-EBZ (AD9361) assumes a VDD_INTERFACE voltage between 1.71 V
and 2.625 V (1.8 V to 2.5 V +/- 5%). On your FPGA carrier board, ensure that
VADJ is between these levels.

.. warning::

   Setting VADJ to 3.3 V will damage the part.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

**RF Ports**

By default the FMCOMMS5 is configured with Minicircuits
`TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`__ baluns on the
Rx1A, Rx2A, Rx1C, Tx1A, Tx2A, and Tx1B channels. This wideband balun allows
tuning across the entire 6 GHz range of the AD9361, although performance may
be compromised at some frequencies.

**Reference Clock**

By default the FMCOMMS5 uses a Rakon 40 MHz RXO3225M as the reference clock,
distributed by the :adi:`ADCLK846` to both :adi:`AD9361` devices, the
:adi:`ADF5355`, and back to the FMC connector. The on-board reference can be
bypassed by placing C301 (0.1 uF) and removing R360, then injecting an
external reference into J301 (50 ohm terminated). The level must not exceed
the :adi:`ADCLK846` input conditions (1.8 V p-p). If the reference clock
frequency is changed, the device tree must be updated accordingly.

**External PLL (Rev C)**

The on-board :adi:`ADF5355` LO signal normally flows through C331 and C332
(C390 and R350 are DNI). To bypass the ADF5355 and use an external LO,
rotate C332 by 90 degrees onto the C390 pad and remove C331 placing R350. An
external reference can then be injected into J302. The level must not exceed
the :adi:`HMC744` input conditions.

.. warning::

   The hardware modifications involve tiny 0402 (1 x 0.5 mm) components and
   should be performed by skilled professionals only.

Phase Performance
~~~~~~~~~~~~~~~~~

Traces between baluns and SMAs are not phase-matched on Rev-A and Rev-B, which
can cause phase misalignment. This is corrected on Rev-C. The phase offset
from trace mismatches can be estimated using:

   phase = 360 * D * f / c

where D is the trace length difference in meters, f is the frequency in Hz,
and c is the speed of light in FR4 (approximately 15 cm/ns). Board files for
each revision provide the actual trace lengths.

These phase estimates can be used to correct for trace mismatches through the
internal phase shifters in the HDL reference design's ADC and DAC cores using
the ``calibphase`` properties.

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
   * - :xilinx:`ZC702 <products/boards-and-kits/ek-z7-zc702-g.html>`
     - Yes
     - Yes
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes
   * - :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
     - Yes
     - Yes

HDL Reference Design
--------------------

The reference design uses two synchronized AD9361 instances with clock
distribution and synchronization logic. It reuses the AD9361 reference design
with multi-channel extensions.

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/fmcomms5`

Software Support
----------------

Linux Drivers
~~~~~~~~~~~~~

- :git-linux:`AD9361 Linux Driver <drivers/iio/adc/ad9361.c>`
- :git-linux:`AXI ADC HDL Linux Driver <drivers/iio/adc/cf_axi_adc_core.c>`
- :git-linux:`AXI DAC DDS Linux Driver <drivers/iio/frequency/cf_axi_dds.c>`

Device Trees
~~~~~~~~~~~~

- :git-linux:`ZC702 DTS <arch/arm/boot/dts/xilinx/zynq-zc702-adv7511-ad9361-fmcomms5.dts>`
- :git-linux:`ZC706 DTS <arch/arm/boot/dts/xilinx/zynq-zc706-adv7511-ad9361-fmcomms5.dts>`
- :git-linux:`ZCU102 DTS <arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9361-fmcomms5.dts>`

IIO Oscilloscope Plugin
~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope includes a dedicated FMCOMMS5 plugin for dual-device
control. The plugin view is divided into four sections:

- **Device Global Settings**: ENSM mode, calibration mode, rate governor,
  FIR filter configuration, path rates, and DCXO tuning. These settings apply
  to both AD9361 devices.
- **Receive Chain**: RF bandwidth, sampling rate, RF port select, LO
  frequency, fastlock mode, tracking calibrations (quadrature, RF DC, BB DC),
  hardware gain, RSSI, and gain control mode.
- **Transmit Chain**: RF bandwidth, sampling rate, RF port select, LO
  frequency, fastlock mode, and per-channel TX attenuation (0 to -89.75 dB
  in 0.25 dB steps).
- **FPGA Settings**: DDS mode selection (one/two CW tones, independent I/Q,
  DAC buffer, disabled), tone parameters (frequency, scale, phase), and RX
  phase rotation.

.. note::

   In the main capture window, channels must be enabled in I/Q pairs
   (e.g., voltage0 and voltage1). The number of enabled pairs must be equal
   between both devices. Channels voltage0-3 correspond to Device A, and
   voltage4-7 correspond to Device B.

Phase Synchronization Procedure (IIO-Oscilloscope)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Rev-A and Rev-B boards, low LO frequencies are recommended due to severe
attenuation from onboard RF switches above 1 GHz.

#. Ensure the default driver configuration is active (remove
   ``~/.osc_profile.ini`` and reboot). Default: 30.72 MSPS, 18.00 MHz RF
   bandwidth, all LOs at 2.4 GHz.
#. From the FMCOMMS5 panel, match all LOs to the same frequency for all four
   data paths.
#. Disable all receiver trackings: Quadrature, RF DC, and BB DC.
#. Put all receivers into **manual** Gain Control Mode with equal gain levels.
#. From the FMComms2/3/4/5 Advanced panel, select the FMComms5 tab and click
   **Reset Calibration**.
#. Click **MCS Sync**.
#. Click **Calibrate** to launch the procedure.
#. After calibration completes, disable Quadrature tracking again to maintain
   minimal ambiguity over time.

Additional Software and Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `libad9361-iio <https://github.com/analogdevicesinc/libad9361-iio>`__:
  Multi-chip sync and phase sync helper library
- MATLAB/Simulink libiio clients
- GNU Radio with MIMO support
- `Phased Array System Toolbox <https://www.mathworks.com/products/phased-array.html>`__
  examples
- Phase synchronization tools and calibration utilities

More Information
----------------

- :ref:`AD-FMCOMMS2-EBZ User Guide <ad-fmcomms2-ebz>`
- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- :adi:`AD9361 Product Page <AD9361>`

Support
-------

If you have any questions regarding the AD-FMCOMMS5-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
