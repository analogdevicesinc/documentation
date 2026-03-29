.. imported from: https://wiki.analog.com/resources/eval/user-guides/admx/eval-admx2501ebz

.. _ad-imp2501-sl hardware-guide:

Hardware User Guide
===================

The :adi:`AD-IMP2501DBZ-SL` and :adi:`AD-IMP2501EBZ-SL` are designed for evaluating impedance
analysis technology in an application that requires a small form factor and wide
frequency range. This platform is designed to get an impedance analysis evaluation set-up running quickly with only a provided USB cable and a computer.
This hardware guide will walk the user through the basic setup, the varying
jumper configurations for different measurement modes, and how to interface with
an external load that is more specific to his or her application.

Equipment Needed
----------------

Required Equipment
~~~~~~~~~~~~~~~~~~

#. **AD-IMP2501DBZ-SL**
#. **AD-IMP2501EBZ-SL**
#. USB C Cable
#. PC

USB drivers and terminal emulator required. Please see
:ref:`ad-imp2501-sl software-user-guide` for instructions to download and
install on your PC if not already installed.

.. _ad-imp2501-sl optional-equipment:

Optional Equipment
~~~~~~~~~~~~~~~~~~

#. Programming equipment for Firmware Updates

   - :adi:`MAX32625PICO2 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max32625pico2.html#eb-overview>`
     with ribbon cable

#. Impedance measurement accessories. Available from various test and
   measurement manufacturers, for example:

   - `Keysight's Impedance Measurement Accessories <https://www.keysight.com/en/pc-1000002552%3Aepsg%3Apgr/lcr-meter-impedance-measurement-product-accessories>`__
   - `B+K Precision TL89S1 SMD Test Fixture <https://www.digikey.com/en/products/detail/b-k-precision/TL89S1/7915183>`__
   - `B+K Precision TL89F1 4-Terminal Test Fixture for leaded components <https://www.digikey.com/en/products/detail/b-k-precision/TL89F2/6618989>`__
   - `SMA Male Pin to BNC Jack <https://www.digikey.com/en/products/detail/pomona-electronics/4290/678700>`__
   - `5 Pin DIN to Flying Lead Cable <https://www.mouser.com/ProductDetail/Kobiconn/172-181142-E?qs=lc2O%252BfHJPVYn95Mux3QdLQ%3D%3D>`__
   - `20 Position Cable Assembly Rectangular Socket to Socket <https://www.digikey.com/en/products/detail/samtec-inc/FFSD-10-D-18-00-01-N/6695449>`__

#. Calibration Standards and Accessories

   - `IET Labs <https://www.ietlabs.com/>`__ (former General Radio products)
   - `Keysight 42090A Open Termination <https://www.keysight.com/en/pd-1000003831%3Aepsg%3Apro-pn-42090A/open-termination-4-terminal-pair>`__
   - `Keysight 42091A Short Termination <https://www.keysight.com/en/pd-1000003830%3Aepsg%3Apro-pn-42091A/short-termination-4-terminal-pair>`__
   - `Keysight 42030A Four Terminal Pair Standard Resistor Set <https://www.keysight.com/en/pd-1000003832%3Aepsg%3Apro-pn-42030A/four-terminal-pair-standard-resistor-set>`__
   - `Keysight 16380A Standard Air Capacitor Set (1pF to 1000pF) <https://www.keysight.com/en/pd-1000003834%3Aepsg%3Apro-pn-16380A/standard-air-capacitor-set-1pf-to-1000pf>`__
   - `Keysight 16380C Capacitance Standard Set (0.01uF to 10uF) <https://www.keysight.com/en/pd-1000003833%3Aepsg%3Apro-pn-16380C/capacitance-standard-set-001uf-to-10uf>`__

#. LCR Meter for verification

   - `Keysight E4980A Precision LCR Meter <https://www.keysight.com/en/pd-715495-pn-E4980A/precision-lcr-meter-20-hz-to-2-mhz>`__

EVAL-ADMX2001EBZ Terminal Description
-------------------------------------

.. figure:: images/eval-admx2001ebz_diagram_3.png
   :width: 600px

.. list-table::
   :header-rows: 1

   * - Terminal Name
     - Description
   * - H_CUR
     - Signal source terminal. It generates the excitation required for
       measurement. This terminal can source up to +/-5V @ 50mA
   * - H_POT
     - Voltage sense terminal. Connect to H_CUR at the device under test (DUT)
   * - L_POT
     - Voltage sense terminal. Connect to L_CUR at the device under test (DUT)
   * - L_CUR
     - Current sense terminal. Return path for the excitation signal. Connect to
       the opposite end of the DUT as H_CUR
   * - UART TX
     - UART transmitter pin. Connect to TX pin on the UART to USB cable. Uses
       3.3V logic
   * - UART RX
     - UART receiver pin. Connect to RX pin on the UART to USB cable. Uses 3.3V
       logic
   * - UART GND
     - UART ground. Connect to ground pin on the UART to USB cable
   * - CLK_SEL
     - Jumper selection of internal or external clock. Set to internal for
       default operation
   * - TRIG_IN
     - Trigger input. Use for hardware-timed acquisition only, otherwise leave
       disconnected
   * - TRIG_OUT
     - Measurement complete trigger out
   * - CLK_IN
     - External clock input. Use a LVCMOS 50MHz clock signal and set CLK_SEL to
       EXT position
   * - CLK_OUT
     - Clock output. These two terminals have a buffered replica of the 50MHz
       main clock
   * - PMOD
     - Controller and Peripheral PMOD terminals for SPI port
   * - Header P6 pins [9-10]
     - Digital output 0-1
   * - Header P7 pins [1-6]
     - Digital output 2-7

AD-IMP2501DBZ-SL Pin Configuration and Descriptions
---------------------------------------------------

.. figure:: images/ad-imp2501ebz-sl_pinout.png
   :width: 600px

+-------------------------+--------------------+------------------------------------+
| Pin Number              | Mnemonic           | Description                        |
+=========================+====================+====================================+
| P1.1, P1.2, P1.7, P1.8, | AGND               | Ground                             |
| P1.17, P1.22, P1.28,    |                    |                                    |
| P1.31, P1.32            |                    |                                    |
+-------------------------+--------------------+------------------------------------+
| P1.3                    | L_CUR              | Low Current signal                 |
+-------------------------+--------------------+------------------------------------+
| P1.4                    | L_POT              | Voltage measurement low potential  |
|                         |                    | terminal                           |
+-------------------------+--------------------+------------------------------------+
| P1.5                    | H_CUR              | High Current or signal             |
+-------------------------+--------------------+------------------------------------+
| P1.6                    | H_POT              | Voltage measurement high potential |
|                         |                    | terminal                           |
+-------------------------+--------------------+------------------------------------+
| P1.9                    | SQWOUT             | Square-Wave Output                 |
+-------------------------+--------------------+------------------------------------+
| P1.10                   | TX_OUT_SELECT      | Drive Mode Select                  |
+-------------------------+--------------------+------------------------------------+
| P1.11                   | CAN0B_RX           | Controller Area Network Receive    |
|                         |                    | Input                              |
+-------------------------+--------------------+------------------------------------+
| P1.12, P1.15, P1.16,    | GPIO               | General Purpose Input Output       |
| P1.18, P1.20, P1.21,    |                    |                                    |
| P1.23, P1.24            |                    |                                    |
+-------------------------+--------------------+------------------------------------+
| P1.13                   | CAN0B_TX           | Controller Area Network Transmit   |
|                         |                    | Output                             |
+-------------------------+--------------------+------------------------------------+
| P1.14                   | OWM_IO             | 1-Wire Controller Data             |
+-------------------------+--------------------+------------------------------------+
| P1.19                   | OWM_PE             | 1-Wire Controller Pull-up Enable   |
+-------------------------+--------------------+------------------------------------+
| P1.25                   | ST_ENABLE          | Self-Test Enabled                  |
+-------------------------+--------------------+------------------------------------+
| P1.26                   | OUTPUT_ENABLE      | CSignal Output Enabled             |
+-------------------------+--------------------+------------------------------------+
| P1.27                   | ST_ENABLE_N        | Self-Test Not Enabled              |
+-------------------------+--------------------+------------------------------------+
| P1.29                   | MCU_RESET_N        | Active-Low. External System Reset  |
|                         |                    | Input                              |
+-------------------------+--------------------+------------------------------------+
| P1.30                   | PDOWN              | Power-Down Output                  |
+-------------------------+--------------------+------------------------------------+
| P2.1                    | I2C_SCL            | I2C Serial Clock                   |
+-------------------------+--------------------+------------------------------------+
| P2.2                    | SPI2A_SCK          | SPI Clock                          |
+-------------------------+--------------------+------------------------------------+
| P2.3                    | I2C_SDA            | I2C Serail Data                    |
+-------------------------+--------------------+------------------------------------+
| P2.4                    | SPI2A_CITO         | SPI Controller In Target Out       |
+-------------------------+--------------------+------------------------------------+
| P2.5                    | POWER_GOOD         | Power Boot-up Verification Signal  |
+-------------------------+--------------------+------------------------------------+
| P2.6                    | SPI2A_SDIO2        | SPI Data 2                         |
+-------------------------+--------------------+------------------------------------+
| P2.7, P2.13, P2.14,     | AGND               | Ground                             |
| P2.20, P2.21, P2.27,    |                    |                                    |
| P2.28                   |                    |                                    |
+-------------------------+--------------------+------------------------------------+
| P2.8                    | SPI2A_COTI         | SPI Controller Out Target In       |
+-------------------------+--------------------+------------------------------------+
| P2.9                    | UART_RX            | UART Receive                       |
+-------------------------+--------------------+------------------------------------+
| P2.10                   | SPI2B_SDIO3        | SPI Data 3                         |
+-------------------------+--------------------+------------------------------------+
| P2.11                   | UART_TX            | UART Transmit                      |
+-------------------------+--------------------+------------------------------------+
| P2.12                   | SPI2A_SS0          | SPI Target Select 0                |
+-------------------------+--------------------+------------------------------------+
| P2.15                   | SPI2A_SS1          | SPI Target Select 1                |
+-------------------------+--------------------+------------------------------------+
| P2.16                   | SWDIO              | Serial Wire Debug I/O              |
+-------------------------+--------------------+------------------------------------+
| P2.17                   | USBC_DM            | USBC Differential pair D-          |
+-------------------------+--------------------+------------------------------------+
| P2.18                   | SWDCLK             | Serial Wire Debug Clock            |
+-------------------------+--------------------+------------------------------------+
| P2.19                   | USBC_DP            | USBC Differential pair D+          |
+-------------------------+--------------------+------------------------------------+
| P2.22                   | VDD_3P3_D          | +3.3V Digital Rail output from     |
|                         |                    | AD-IMP2501DBZ-SL                   |
+-------------------------+--------------------+------------------------------------+
| P2.23                   | VDD_3P3_A          | +3.3V Analog Rail output from      |
|                         |                    | AD-IMP2501DBZ-SL                   |
+-------------------------+--------------------+------------------------------------+
| P2.24                   | VDD_1P8            | +1.8V Rail output from             |
|                         |                    | AD-IMP2501DBZ-SL                   |
+-------------------------+--------------------+------------------------------------+
| P2.25                   | VCC                | +5V Rail output from               |
|                         |                    | AD-IMP2501DBZ-SL                   |
+-------------------------+--------------------+------------------------------------+
| P2.26                   | VEE                | -5V Rail output from               |
|                         |                    | AD-IMP2501DBZ-SL                   |
+-------------------------+--------------------+------------------------------------+
| P2.29, P2.30            | FC_VPOWER_IN       | Input Power Supply for             |
|                         |                    | AD-IMP2501DBZ-SL (+5V nominal)     |
+-------------------------+--------------------+------------------------------------+
| All Other Pins          | DNC                | Do Not Connect                     |
+-------------------------+--------------------+------------------------------------+

General Setup
-------------

The following figure shows the basic connections required for evaluating the
ADMX2501B.

.. figure:: images/fishercat_hardware_setup.png
   :width: 800px

- Insert the AD-IMP2501DBZ-SL module into the AD-IMP2501EBZ-SL board in the
  location shown above. Use the small white triangle on both the module and the
  carrier board to orient properly. The connectors are different sizes, so they
  can only be inserted in one orientation shown, but excessive force in the
  wrong orientation could damage the connectors.
- Use the picture below and the following tables to install the correct jumpers
  for your desired operation. The first table is for power and general
  communication. The second table is for EIS on board measurements. The third
  table is for EIS off board measurements.

.. figure:: images/fishercat_jumper_positions.png
   :width: 600px

- Verify jumpers are installed in the locations designated by the following
  table for power and communication.

+-------------------------+--------------------+------------------------------------+
| Jumper Designation      | Install Position   | Description                        |
+=========================+====================+====================================+
| P4                      | Not Installed      | Programming Header                 |
+-------------------------+--------------------+------------------------------------+
| P5                      | Not Installed      | Debug UART RX                      |
+-------------------------+--------------------+------------------------------------+
| P6                      | Not Installed      | Debug UART TX                      |
+-------------------------+--------------------+------------------------------------+
| P11                     | Pins 1-2           | USB C Power Supply                 |
+-------------------------+--------------------+------------------------------------+
| P14                     | Pins 1-2           | USB C DM                           |
+-------------------------+--------------------+------------------------------------+
| P15                     | Pins 1-2           | USB C DP                           |
+-------------------------+--------------------+------------------------------------+
| P16                     | Pins 1-2           | FTDI UART RX                       |
+-------------------------+--------------------+------------------------------------+
| P17                     | Pins 1-2           | FTDI UART TX                       |
+-------------------------+--------------------+------------------------------------+
| P18                     | Pins 1-2           | FTDI Power                         |
+-------------------------+--------------------+------------------------------------+
| P20                     | Not Installed      | CAN Bus                            |
+-------------------------+--------------------+------------------------------------+

- For EIS on board measurements install jumpers according to the following
  table. Note that to select an onboard load, both jumpers, corresponding to the
  appropriate load, need to be installed. If the user selects their own
  component in position 8, no jumpers should be installed on P21 or P22.

+-------------------------+--------------------+------------------------------------+
| Jumper Designation      | Install Position   | Description                        |
+=========================+====================+====================================+
| P27                     | Pins 1-2           | EIS HCUR                           |
+-------------------------+--------------------+------------------------------------+
| P28                     | Pins 1-2           | EIS HPOT                           |
+-------------------------+--------------------+------------------------------------+
| P29                     | Pins 1-2           | EIS LPOT                           |
+-------------------------+--------------------+------------------------------------+
| P30                     | Pins 1-2           | EIS LCUR                           |
+-------------------------+--------------------+------------------------------------+
| P23                     | Pins 1-2           | HCUR to HPOT connection            |
+-------------------------+--------------------+------------------------------------+
| P24                     | Pins 1-2           | LCUR to LPOT connection            |
+-------------------------+--------------------+------------------------------------+
| P21                     | Selectable                                              |
|                         | Pins 1-2           | 10k ohms                           |
|                         | Pins 3-4           | 1k ohms                            |
|                         | Pins 5-6           | 100 ohms                           |
|                         | Pins 7-8           | 10 ohms                            |
|                         | Pins 9-10          | 0 ohms                             |
+-------------------------+--------------------+------------------------------------+
| P22                     | Selectable                                              |
|                         | Pins 1-2           | 10k ohms                           |
|                         | Pins 3-4           | 1k ohms                            |
|                         | Pins 5-6           | 100 ohms                           |
|                         | Pins 7-8           | 10 ohms                            |
|                         | Pins 9-10          | 0 ohms                             |
+-------------------------+--------------------+------------------------------------+
| P8                      | Not Installed      | User Selectable Load               |
+-------------------------+--------------------+------------------------------------+
| P12                     | Pins 1-2           | EIS HCUR SMA/Onboard               |
|                         | Pins 5-6           | EIS HPOT SMA/Onboard               |
|                         | Pins 9-10          | EIS LPOT SMA/Onboard               |
|                         | Pins 13-14         | EIS LCUR SMA/Onboard               |
+-------------------------+--------------------+------------------------------------+

- For EIS off board measurements using the SMA connectors, install jumpers
  according to the following table. Connect SMA cables to J1-J4, and verify no
  jumpers are installed on P8, P21, P22, P23, and P24.

+-------------------------+--------------------+------------------------------------+
| Jumper Designation      | Install Position   | Description                        |
+=========================+====================+====================================+
| P27                     | Pins 1-2           | EIS HCUR                           |
+-------------------------+--------------------+------------------------------------+
| P28                     | Pins 1-2           | EIS HPOT                           |
+-------------------------+--------------------+------------------------------------+
| P29                     | Pins 1-2           | EIS LPOT                           |
+-------------------------+--------------------+------------------------------------+
| P30                     | Pins 1-2           | EIS LCUR                           |
+-------------------------+--------------------+------------------------------------+
| P23                     | Not Installed      | HCUR to HPOT connection            |
+-------------------------+--------------------+------------------------------------+
| P24                     | Not Installed      | LCUR to LPOT connection            |
+-------------------------+--------------------+------------------------------------+
| P21                     | Not Installed                                           |
|                         |                    | 10k ohms                           |
|                         |                    | 1k ohms                            |
|                         |                    | 100 ohms                           |
|                         |                    | 10 ohms                            |
|                         |                    | 0 ohms                             |
+-------------------------+--------------------+------------------------------------+
| P22                     | Not Installed                                           |
|                         |                    | 10k ohms                           |
|                         |                    | 1k ohms                            |
|                         |                    | 100 ohms                           |
|                         |                    | 10 ohms                            |
|                         |                    | 0 ohms                             |
+-------------------------+--------------------+------------------------------------+
| P8                      | Not Installed      | User Selectable Load               |
+-------------------------+--------------------+------------------------------------+
| P12                     | Pins 1-2           | EIS HCUR SMA/Onboard               |
|                         | Pins 5-6           | EIS HPOT SMA/Onboard               |
|                         | Pins 9-10          | EIS LPOT SMA/Onboard               |
|                         | Pins 13-14         | EIS LCUR SMA/Onboard               |
+-------------------------+--------------------+------------------------------------+

- For EIS off board measurements using the DIN connector, only change jumpers on
  P12 according to the following table. Connect DIN cable to P7.

+-------------------------+--------------------+------------------------------------+
| Jumper Designation      | Install Position   | Description                        |
+=========================+====================+====================================+
| P12                     | Pins 3-4           | EIS HCUR DIN                       |
|                         | Pins 7-8           | EIS HPOT DIN                       |
|                         | Pins 11-12         | EIS LPOT DIN                       |
|                         | Pins 15-16         | EIS LCUR DIN                       |
+-------------------------+--------------------+------------------------------------+

- Connect the USB C cable to P3 on AD-IMP2501EBZ-SL and the host PC.
- An LED on the top side of the AD-IMP2501DBZ-SL should turn on, blink twice, and turn off. It should now only turn on when data is being processed.
