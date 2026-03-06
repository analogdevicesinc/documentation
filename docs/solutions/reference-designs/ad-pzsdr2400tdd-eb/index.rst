.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-pzsdr2400tdd-eb

.. _ad-pzsdr2400tdd-eb:

AD-PZSDR2400TDD-EB
===================

The :adi:`AD-PZSDR2400TDD-EB` is an RF personality card that plugs into the
:adi:`ADRV1CRR-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`
carrier card. 35 mm U.FL coaxial cables connect the card to the
:adi:`ADRV9361-Z7035`, providing access to the transmit and receive inputs
of the :adi:`AD9361`.

The purpose of the AD-PZSDR2400TDD-EB is to provide the user with a 2.4 GHz
TDD path to condition the transmit or receive signals of the :adi:`AD9361`.
Selection of the TX or RX path is achieved by the 200 MHz to 2.7 GHz SPDT
switch :adi:`HMC546LP2`, controlled by the FPGA and accompanying software.
The transmit path consists of a 2.4 GHz filter, half-watt driver amplifier
:adi:`ADL5324`, and 2-watt power amplifier :adi:`HMC921`. The receive path
consists of the same 2.4 GHz filter as well as a low-loss LNA :adi:`HMC669`.

The AD-PZSDR2400TDD-EB board has two identical TX/RX channels that connect to
the two channels of the AD9361. Power and control for this board comes from the
40-pin connector that mates with the AES-PZSDRCC-FMC-G carrier. The board has
three settings: TX mode, RX mode, or TDD mode. Both TX/RX channels (1 and 2)
must be set in the same fashion --- you cannot transmit on channel 1 and receive
on channel 2 simultaneously. They are either both in TX mode or both in RX mode
at each point in time.

.. image:: pcb_top.jpg
   :align: center
   :width: 600

Functional Overview
-------------------

A functional block diagram of the system is given below. The system consists
of two transmit paths, two receive paths, and a power supply section.

.. figure:: 2400tdd_block_diagram.jpg
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB functional block diagram

Transmit
~~~~~~~~

The transmit path uses the following key components:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Description
   * - :adi:`ADL5324`
     - The ADL5324 incorporates a dynamically adjustable biasing circuit that
       allows for the customization of OIP3 and P1dB performance from 3.3 V to
       5 V, without the need for an external bias resistor.
   * - :adi:`HMC921`
     - The HMC921LP4E is a high linearity GaAs HBT MMIC 2-watt power amplifier
       operating from 0.4 to 2.7 GHz, housed in a RoHS-compliant 4x4 mm QFN
       leadless package.

Receive
~~~~~~~

The receive path uses the following key component:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Description
   * - :adi:`HMC669`
     - The HMC669LP3(E) is a versatile, high dynamic range GaAs MMIC Low Noise
       Amplifier that integrates a low-loss LNA bypass mode on the IC. The
       amplifier is ideal for receivers and LNA modules operating between 1.7
       and 2.2 GHz, providing 1.4 dB noise figure, 17 dB of gain, and +29 dBm
       IP3 from a single supply of +5 V at 86 mA.

Switching
~~~~~~~~~

The switching function uses the following key component:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Description
   * - :adi:`HMC546LP2`
     - The HMC546LP2(E) is a failsafe SPDT switch in a leadless DFN surface
       mount plastic package for use in transmit-receive and LNA protection
       applications which require very low distortion and high power handling
       of up to 10 watts. The device can control signals from 200 to 2700 MHz
       and is especially suited for WiMAX and WiBro repeaters, PMR, and
       automotive telematic applications.

Power Supply
~~~~~~~~~~~~

The board receives all power from the carrier board through a 40-pin connector.
The following key power supply components are used:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Component
     - Description
   * - :adi:`ADP2384`
     - 4 A, 20 V step-down switcher.
   * - :adi:`ADP7104`
     - High accuracy, 500 mA LDO.
   * - :adi:`ADM7171`
     - Ultra low noise, 1 A LDO.

Hardware
--------

Main Components
~~~~~~~~~~~~~~~

.. figure:: parts_list.png
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB main components

Board Outline
~~~~~~~~~~~~~

The PCB measures 100 mm x 62 mm and has the same form factor as the RFSOM. The
mounting holes align with the carrier card (AES-PZSDRCC-FMC-G).

.. figure:: top_copper_top_overlay.png
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB top copper and overlay

.. figure:: pcb_dimensions.png
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB PCB dimensions

Layer Stackup
~~~~~~~~~~~~~

The AD-PZSDR2400TDD-EB is a 4-layer board.

.. figure:: layer_stackup_2.png
   :align: center
   :width: 600

   AD-PZSDR2400TDD-EB layer stackup

Configuration Options
---------------------

Several GPO and GPIO pins are brought to the RF card through connector J2,
found on the bottom of the PCB. These pins allow configuration of the PA, LNA,
and SPDT switch found on the PCB.

.. list-table::
   :header-rows: 1
   :widths: 18 12 25 10 25

   * - Control Name
     - Location
     - Device Controlled
     - Value
     - Action
   * - RF_GPIO0
     - P2 - 31
     - PA Channel 1 (:adi:`HMC921`)
     - 0/1
     - Disabled/Enabled
   * - RF_GPIO0
     - P2 - 31
     - PA Channel 2 (:adi:`HMC921`)
     - 0/1
     - Disabled/Enabled
   * - AD9361_GPO0
     - P2 - 09
     - LNA Channel 1 (:adi:`HMC669`)
     - 0/1
     - Bypassed/Enabled
   * - AD9361_GPO1
     - P2 - 11
     - LNA Channel 2 (:adi:`HMC669`)
     - 0/1
     - Bypassed/Enabled
   * - AD9361_GPO3
     - P2 - 15
     - SPDT Switch (:adi:`HMC546LP2`)
     - 0/1
     - RFC to TX/RFC to RX

Characteristics and Performance
-------------------------------

The following equipment was used to generate the characterization data:
Agilent Technologies E5071C ENA Series Network Analyzer (100 kHz to 8.5 GHz).

.. figure:: equipment.png
   :align: center
   :width: 500

   Test equipment setup

Receive Channels Gain vs. Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following plots show the gain versus frequency response of the receive
channels. Each plot contains two traces: the first shows the gain versus
frequency response when the LNA (:adi:`HMC669`) is enabled, and the second
shows the response when the LNA is bypassed.

.. figure:: hardware/rx1_unzoom_lna_comparison.jpg
   :align: center
   :width: 500

   Channel 1 - Gain vs. frequency response - 1 MHz to 6 GHz

.. figure:: hardware/rx1_zoom_lna_comparison.jpg
   :align: center
   :width: 500

   Channel 1 - Gain vs. frequency response - Zoomed in, 2.2 GHz to 2.7 GHz

.. figure:: hardware/rx2_unzoom_lna_comparison.jpg
   :align: center
   :width: 500

   Channel 2 - Gain vs. frequency response - 1 MHz to 6 GHz

.. figure:: hardware/rx2_zoom_lna_comparison.jpg
   :align: center
   :width: 500

   Channel 2 - Gain vs. frequency response - Zoomed in, 2.2 GHz to 2.7 GHz

Transmit Channels Gain vs. Frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following plots show the gain versus frequency response of the transmit
channels.

.. figure:: hardware/tx1_unzoom.jpg
   :align: center
   :width: 500

   Channel 1 - Gain vs. frequency response - 1 MHz to 6 GHz

.. figure:: hardware/tx1_zoom.jpg
   :align: center
   :width: 500

   Channel 1 - Gain vs. frequency response - Zoomed in, 2.2 GHz to 2.7 GHz

.. figure:: hardware/tx2_unzoom.jpg
   :align: center
   :width: 500

   Channel 2 - Gain vs. frequency response - 1 MHz to 6 GHz

.. figure:: hardware/tx2_zoom.jpg
   :align: center
   :width: 500

   Channel 2 - Gain vs. frequency response - Zoomed in, 2.2 GHz to 2.7 GHz

Switch Isolation
~~~~~~~~~~~~~~~~

The following plots detail the isolation provided by the :adi:`HMC546LP2` for
both channels.

.. figure:: hardware/isolation_ch1_unzoom_ensm_test_enabled.jpg
   :align: center
   :width: 500

   HMC546LP2 Isolation Test, RX Channel 1 - Signal driving TX1, switch
   alternating between TX to RFC and RX to RFC, measuring signal present
   on RX1

.. figure:: hardware/isolation_ch1_zoom_ensm_test_enabled.jpg
   :align: center
   :width: 500

   HMC546LP2 Isolation Test, RX Channel 1 - Zoomed in, 2.2 GHz to 2.7 GHz

.. figure:: hardware/isolation_ch2_unzoom_ensm_test_enabled.jpg
   :align: center
   :width: 500

   HMC546LP2 Isolation Test, RX Channel 2 - Signal driving TX2, switch
   alternating between TX to RFC and RX to RFC, measuring signal present
   on RX2

.. figure:: hardware/isolation_ch2_zoom_ensm_test_enabled.jpg
   :align: center
   :width: 500

   HMC546LP2 Isolation Test, RX Channel 2 - Zoomed in, 2.2 GHz to 2.7 GHz

Layout Considerations
---------------------

The :adi:`ADL5324` has several passive components surrounding the IC which
directly influence the tuning frequency of the device. The location of these
capacitors is critical to the accurate determination of the tuning frequency.

.. figure:: tuning_component_placement.png
   :align: center
   :width: 400

   ADL5324 tuning component placement

The component spacing for tuning capacitors C1 and C2 is detailed in the
:adi:`ADL5324` datasheet over a variety of frequencies. A table from the
datasheet, detailing this information, is listed below.

.. figure:: tuning_component_table.png
   :align: center
   :width: 600

   ADL5324 tuning component values from datasheet

Placement of the AC coupling capacitors, power supply bypassing capacitors,
and DC bias inductor should follow the recommendation of the datasheet but
are slightly less critical than the tuning capacitors.

FCC/CE Certification
--------------------

Both `CE <https://en.wikipedia.org/wiki/CE_marking>`__ and
`FCC <https://en.wikipedia.org/wiki/FCC_Declaration_of_Conformity>`__
certifications are necessary for system-level products.

Because ADI boards are custom-built evaluation kits destined for professionals
to be used solely at research and development facilities for such purposes, they
are considered exempt from the EU product directives and normally are not tested
for CE or FCC compliance.

If you choose to use your board to transmit using an antenna, it is your
responsibility to make sure that you are in compliance with all laws for the
country, frequency, and power levels in which the device is used. Additionally,
some countries regulate reception in certain frequency bands. It is the
responsibility of the user to maintain compliance with all local laws and
regulations.

HDL Reference Design
--------------------

AD9361 TDD Mode HDL Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the :adi:`AD9361` RF Agile Transceiver in TDD (Time Division Duplex)
mode, the user has multiple solutions to control the time period of the receive
and transmit bursts. The internal enable state machine (ENSM) of the device can
either be controlled by SPI writes or by the ENABLE/TXNRX pins. SPI control is
considered asynchronous to the DATA_CLK because the SPI_CLK can be derived from
a different clock reference and still function properly. The SPI control ENSM
method is recommended when real-time control of the synthesizers is not
necessary.

The ENABLE/TXNRX pin control method is recommended if the base-band processor
(BBP) has extra control outputs that can be controlled in real time, allowing a
simple two-wire interface to control the state of the AD9361 device.

ENABLE/TXNRX Pin Control
^^^^^^^^^^^^^^^^^^^^^^^^^

In TDD, the state of the TXNRX pin controls whether the AD9361 will transition
from ALERT to RX or ALERT to TX. If TXNRX is high, the device will move into
the TX state. If TXNRX is low, the device will move into the RX state. The
TXNRX pin level should be set during the ALERT state. The logic level of TXNRX
must not change during the RX, TX, or FDD states. The role of the ENABLE pin is
to transition the ENSM state to the next state, and can be operated in pulse
mode or level mode.

.. figure:: ad9361_tdd_pincntr_pulse.png
   :align: center
   :width: 700

   Enable Pulse Mode (TDD)

.. figure:: ad9361_tdd_pincntr_level.png
   :align: center
   :width: 700

   Enable Level Mode (TDD)

By default, the ENABLE and TXNRX pins are controlled by GPIOs. This solution,
similarly to the SPI write ENSM control, cannot provide real-time control of
these pins.

TDD Controller
^^^^^^^^^^^^^^

The **axi_ad9361** IP core has an integrated TDD controller, which provides the
ability to control the ENABLE/TXNRX pins in real time. The TDD controller
consists of a counter that counts on every positive edge of FB_CLK, and several
software-accessible registers that define the time when the ENABLE and TXNRX
pins should be set or reset.

.. figure:: ad9361_tdd_ip_bd_v3.png
   :align: center
   :width: 600

   axi_ad9361 IP core block diagram with integrated TDD controller module

The foundation of the TDD controller is a counter that can be configured to
count until a specified frame length. The maximum value of the counter can be
defined by dividing the desired frame length by the current FB_CLK clock period.
For example, for a 10 ms frame length when FB_CLK is 122.88 MHz, the value of
the ``REG_TDD_FRAME_LENGTH`` register must be 1228800.

After defining the frame length, the user can define one or two sets of
pointers, which specify the exact location within a frame when the device will
start or stop a receive or transmit burst.

Starting and stopping a **receive burst** consists of the following action
points, each defining a pointer:

#. Enabling the RX synthesizer
#. Enabling the RX RF path inside the device (ALERT to RX state transition)
#. Enabling the RX data path inside the FPGA (the core starts to get valid data
   from the device interface)
#. Disabling the RX data path inside the FPGA
#. Disabling the RX RF path inside the device (RX to ALERT state transition)
#. Disabling the RX synthesizer

Starting and stopping a **transmit burst** consists of the following action
points, each defining a pointer:

#. Enabling the TX synthesizer
#. Enabling the TX RF path inside the device (ALERT to TX state transition)
#. Enabling the TX data path inside the FPGA (the core starts to push valid data
   to the device interface)
#. Disabling the TX data path inside the FPGA
#. Disabling the TX RF path inside the device (TX to ALERT state transition)
#. Disabling the TX synthesizer

After enabling the TDD controller, the counter starts counting and compares its
value to the pointer values. When there is a match, the corresponding control
signal is asserted. Using this method, the controller generates six control
signals: ``VCO_RX_EN``, ``VCO_TX_EN``, ``RF_RX_EN``, ``RF_TX_EN``,
``RX_DP_EN``, and ``TX_DP_EN``. Using these control signals, the
:git-hdl:`TDD interface module <library/axi_ad9361/axi_ad9361_tdd_if.v>` drives
the ENABLE and TXNRX pins accordingly.

TDD Synchronization
^^^^^^^^^^^^^^^^^^^

TDD systems use the same frequency channel for both uplink (UL) and downlink
(DL) transmission, but at different times. This scheme allows dynamic allocation
of the amount of time for UL and DL, resulting in asymmetric UL/DL transmission.
To prevent unwanted interference between different transmission links, network
synchronization is required between base stations and users. In practice, this
synchronization can be obtained by using IEEE 1588 or GPS.

The reference design contains a pulse generator core
(:git-hdl:`util_tdd_sync <library/util_tdd_sync>`), which is independent of the
**axi_ad9361** core and can generate a small pulse in a defined time interval.
This pulse is fed into both **axi_ad9361** cores and resets the counter, keeping
the two controllers synchronized.

.. figure:: util_tdd_sync.png
   :align: center
   :width: 250

   util_tdd_sync core

.. note::

   This reference design does not provide a complete solution for network
   synchronization. It is intended to showcase the TDD support of the AD9361.

**util_tdd_sync Parameters:**

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Name
     - Default
     - Description
   * - ``TDD_SYNC_PERIOD``
     - 100000000
     - Relative time between two synchronization pulses. The actual time is the
       value multiplied by the ``clk`` clock period.

**util_tdd_sync IO Ports:**

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Name
     - Type
     - Description
   * - ``clk``
     - Clock
     - Driven by the system clock (S_AXI_ACLK), which is a 100 MHz clock
       signal.
   * - ``rstn``
     - Reset
     - Active low reset, driven by the system reset (S_AXI_RSTN).
   * - ``sync_mode``
     - Input
     - If asserted, the internally generated sync signal will be assigned to
       ``sync_out``; otherwise ``sync_out`` will get the ``sync_in`` value.
       This pin is connected to the ``tdd_sync_cntr`` pin of the axi_ad9361
       core.
   * - ``sync_in``
     - Input
     - External input signal, which comes from the other terminal.
   * - ``sync_out``
     - Output
     - Connected to the ``tdd_sync`` pin of the axi_ad9361 core.

To activate the sync pulse generator, the software needs to set the
``REG_TDD_SYNC_TERMINAL_TYPE`` register to ``0x01``.

**TDD_SYNC Interface IO Mapping:**

.. list-table::
   :header-rows: 1
   :widths: 25 25 20 15

   * - Carrier Name
     - Connector Name
     - Port Name
     - FPGA IO Pin
   * - AES-PZSDRCC-FMC-G
     - PMOD1 / P11
     - PMOD1[5]
     - W19
   * - ZC706
     - PMOD1 / J58
     - PMOD1_5_LS
     - AA20

TDD Scope Captures
^^^^^^^^^^^^^^^^^^^

.. figure:: tdd_scope_1.png
   :align: center
   :width: 600

   TDD controller scope capture 1

.. figure:: tdd_scope_2.png
   :align: center
   :width: 600

   TDD controller scope capture 2

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adrv9361z7035`

Software
--------

Linux Device Tree Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using this card on the PicoZed SDR SOM Development Kit, a specific device
tree must be used for TDD operation.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Function
     - File
   * - ADRV9361-Z7035 FMC RFCARD TDD Device Tree
     - :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035-fmc-rfcard-tdd.dts`

This device tree includes the device tree for the PicoZed SDR SOM Development
Kit but configures the :adi:`AD9361` for TDD operation:

#. Sets the AD9361 for TDD mode.
#. Sets TX LO frequency to RX LO frequency.
#. Enables AD9361 GPO2 and GPO3 to slave the ENSM RX and TX states.
#. Enables AD9361 GPO0 and GPO1 to control the external LNAs for RX1 and RX2.
#. Configures LNA gain and bypass loss.

TDD Controller Linux Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The TDD HDL core driver is a platform driver and can currently only be
instantiated via device tree.

Required device tree properties:

- ``compatible``: Should always be ``"adi,axi-tdd-1.00"``
- ``reg``: Base address and register area size. This parameter expects a
  register range.
- ``adi,profile-config0``: At least one (maximum 7) configuration profile
  should be defined. A profile contains the register values for the TDD
  controller timing parameters.

Example device tree node:

.. code-block:: dts

   cf_ad9361_tdd_core_0: cf-ad9361-tdd-core-lpc@79028000 {
       compatible = "adi,axi-tdd-1.00";
       reg = <0x79028000 0x1000>;
       /* Master Configuration Profile */
       adi,profile-config0 = <0 1228800 1 1198080 771920 771920 1198080
                              39832 771536 781032 1197696 44832 766536
                              786032 1192696>;
       /* Slave Configuration Profile */
       adi,profile-config1 = <0 1228800 0 771920 1198080 1198080 771920
                              781032 1197696 39832 771536 786032 1192696
                              44832 766536>;
   };

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.

.. esd-warning::
