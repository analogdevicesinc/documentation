.. _ad-m2kcompedu-ebz-hardware-guide:

Hardware Guide
==============

Overview
--------

The :adi:`AD-M2KCOMPEDU-EBZ` integrates stimulus generation, measurement access,
biasing, user controls, sensing, and communication functions into a compact
USB-powered board. The board complements :adi:`ADALM2000` and standard lab
equipment by providing:

- Standalone Arbitrary Waveform Generator with ±10 V max amplitude
- ±12 V on-board power supply
- TTL/PWM 5 V Clock Generator with adjustable frequency
- Two adjustable DC reference voltage generators covering a range of ±12 V DC
- Analog input (AI), analog output (AO), and digital output (DO)
- Power supplies, sensors, controls, and LED
- Display and transceiver
- Adjustable reference voltages and current functions

The Arduino UNO R4 support adds programmable control for menu operation,
calibration, signal-generator control, and embedded-system exercises.

Safety Information
------------------

.. caution::

   Do not operate the hardware in a manner not specified in this document and in
   the user documentation. Misuse of the hardware can result in a hazard. Damage
   to the hardware can compromise its built-in safety protections. Do not connect
   or disconnect the device while it is being supplied. If the hardware is
   damaged, return it to the Digitally Enhanced Analog Integrated Circuits
   Research Group at the Technical University of Cluj-Napoca for repair.

These requirements and limits are designed to provide reasonable protection
against harmful interference when the product is operated in its intended
operational electromagnetic environment. This product is intended for use in
residential locations and universities. Harmful interference may still occur
in a particular installation or when the product is connected to a test object.
To minimize the potential for the product to cause interference to radio and
television reception or to experience unacceptable performance degradation,
install and use this product in strict accordance with the instructions in the
product documentation.

Hardware Setup
--------------

This section presents detailed instructions on setting up the LM2K Companion
board.

Accessible Headers and Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a variety of on-board connectors that enable direct access to all
features of the LM2K Companion, thus minimizing the complexity of interconnection
with external devices such as Arduino, :adi:`ADALM2000`, Analog Discovery 
eries, and external M5STACK Display.

Arduino
^^^^^^^

The Arduino connectors/headers are located under the LM2K Companion board for
quick, non-invasive connections. These connectors are extended to the top of
the board in a pin-to-pin arrangement, allowing direct access to all Arduino
terminals—see Figure 1.

Additionally, the LM2K Companion board features a PCB window that provides
a clear view of the Arduino 8x12 LED matrix.

.. note::

   The Arduino has its own USB port used for power supply and configuration.
   However, this USB port does not provide power to the LM2K Companion board.
   The Arduino can only receive power from the LM2K Companion's 5 V bus due
   to the presence of diode D6—see Figure 2. This arrangement allows both
   USB ports to be connected to power supply/laptop without interfering,
   enabling "live programming".

.. figure:: Arduino-top-accessible-header-PCB-view.png
   :align: center
   :width: 600px

   Arduino top accessible headers: PCB view

.. figure:: Arduino-top-accessible-header-Schematic-View.png
   :align: center
   :height: 600px

   Arduino top accessible headers: Schematic view

.. note::

   Although the user has access to all Arduino terminals, please note that some
   of them are already connected to the LM2K Companion onboard devices, so they
   should not be used otherwise.

For instance, the SPI port is already connected to the :adi:`AD9833` signal
generator and the :adi:`AD5443` DAC. However, only the SS/CS lines are reserved,
therefore more SPI devices can be connected to the port, with other SS/CS lines.

In a similar manner, the I2C port connects to the display and the :adi:`AD5625`
DAC. However, more I2C devices can be connected to it, if the devices I2C addresses
do not conflict with the existing ones (0x3C for the display and 0x1E for 
:adi:`AD5625`).

.. figure:: Arduino-top-headers-for-end-user.png
   :align: center
   :width: 400px

   Arduino top headers for end user.

The list of Arduino ports already used and/or reserved by the LM2K Companion
functionality is presented in Table 1.

.. table:: Used Arduino Pins
   
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | Arduino      | LM2K                                                      | Notes: IN/OUT wrt Arduino                                             |
   |              +-----------------------------------------+-----------+-----+                                                                       |
   | Pin goes to  | Net name                                | Connector | Pin |                                                                       |
   +==============+=========================================+===========+=====+=======================================================================+
   | SCL          | ARD_SCL                                 | P4        | 10  | Pulled-Up to 5 V with 10K, shared I2C line; use only with compatible  |
   |              |                                         |           |     | I2C devices.                                                          |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | SDA          | ARD_SDA                                 | P4        | 9   | Pulled-Up to 5 V with 10K, shared I2C line; use only with compatible  |
   |              |                                         |           |     | I2C devices.                                                          |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | A0           | ARD_A0__ROT_A                           | P1        | 1   | Dig Input: Menu rotary encoder signal. Pulled-up to 5 V with 10K.     |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | A1           | ARD_A1__ROT_B                           | P1        | 2   | Dig Input: Menu rotary encoder signal. Pulled-up to 5 V with 10K.     |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | RX + D0      | ROT_BTN                                 | P3        | 1   | Dig Input: Menu rotary encoder push button. Pulled-up to 5 V with     |
   |              |                                         |           |     | 10K.                                                                  |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D6/PWM       | SWITCH_SQR_SIG_GEN / LED_D_K            | P3        | 7   | Dig Output: SQW signal generator (SG) attenuator. Controls U1         |
   |              |                                         |           |     | :adi:`ADG444` switch.                                                 |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D13/SCK      | SCLK_DAC / ARD_D13_ARD_SCK_ARD_R4_CANRX | P4        | 6   | SPI port clock signal. Already connected to the signal-generator      |
   |              |                                         |           |     | devices. Also shared with CAN RX when CAN jumpers are used.           |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D12/MISO     | SDO_DAC / ARD_D12_ARD_MISO_LED_G_K      | P4        | 5   | SPI MISO / SDO signal. Already connected to signal-generator devices. |
   |              |                                         |           |     | Also connected to 7-segment LED G cathode when jumper is used.        |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D11/PWM/MOSI | DIN_DAC / ARD_D11_ARD_MOSI_ARD_PWM      | P4        | 4   | SPI MOSI / data input, already connected to the signal-generator DAC. |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D10/PWM      | ARD_D10_ARD_CS1_ARD_R4_CANTX            | P4        | 3   | Reserved as chip-select for the onboard signal generator. Also shared |
   |              |                                         |           |     | with CAN TX when CAN jumpers are used.                                |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D9/PWM       | PWM_OUT / ARD_D9_ARD_PWMOUT_CLK         | P4        | 2   | Reserved: PWM output of the hex inverting Schmitt trigger / CLK       |
   |              |                                         |           |     | buffer.                                                               |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+
   | D8           | SYNCN_DAC / ARD_D8_LED_F_K              | P4        | 1   | Reserved for signal-generator DAC sync/chip-select control. Also      |
   |              |                                         |           |     | connected to 7-segment LED F cathode when jumper is used.             |
   +--------------+-----------------------------------------+-----------+-----+-----------------------------------------------------------------------+


The remaining Arduino pins are either available or conditionally available to the
end user, depending on the selected LM2K Companion functions.

.. note::

   Arduino reserved pins/ports have double functionality that serves the LM2K
   Companion in the following use cases:

   - Sig Gen Control: Priority 1. All Sig Gen controls are directly connected
     to the Arduino header; no jumpers are required.
   - CAN RX/TX config: Priority 2, all CAN RX/TX pins can be connected to
     Arduino header via dedicated Jumpers P21, P22—see Figure 4.
   - 7 Segments LED display control: Priority 2, all LED cathodes can be
     connected to Arduino header via dedicated Jumpers P23, P31—see Figure 5.

Thus, only one use-case is recommended to be used at a time to avoid inputs/outputs
overdrive.

.. figure:: CAN-to-Arduino-connection-Jumpers-P21-P22.png
   :align: center
   :width: 600px

   CAN to Arduino connection Jumpers P21 and P22

.. figure:: 7seg_cathodes_arduino_jumpers_p23_p31.png
   :align: center
   :height: 500px

   7-Segment display cathodes to Arduino connection jumpers P23-P31

The Arduino pins not listed as already connected or reserved may still be conditionally
assigned to optional LM2K Companion functions, such as CAN or the 7-segment display.
Table 2 lists the Arduino header pins that are available or conditionally available
to the end user.

.. table:: Available Arduino Pins

   +--------------+------+------+-----------------------------------------------------------------------+
   | Arduino      | LM2K        | Notes: IN/OUT wrt Arduino                                             |
   |              +------+------+                                                                       |
   | Pin goes to  | Port | Pin  |                                                                       |
   +==============+======+======+=======================================================================+
   | ARD_A2       | P1   | A2   | Available analog input / GPIO for end-user use.                       |
   +--------------+------+------+-----------------------------------------------------------------------+
   | ARD_A3       | P1   | A3   | Available analog input / GPIO for end-user use.                       |
   +--------------+------+------+-----------------------------------------------------------------------+
   | ARD_A4       | P1   | A4   | Available analog input / GPIO for end-user use.                       |
   +--------------+------+------+-----------------------------------------------------------------------+
   | ARD_A5       | P1   | A5   | Available only if the 7-segment decimal point connection is not used. |
   +--------------+------+------+-----------------------------------------------------------------------+
   | NC           | P2   | 1    | NC                                                                    |
   +--------------+------+------+-----------------------------------------------------------------------+
   | IOREF        | P2   | 2    | Arduino IO reference pin; not used by LM2K circuitry.                 |
   +--------------+------+------+-----------------------------------------------------------------------+
   | RESET        | P2   | 3    | Arduino RESET pin; not used by LM2K circuitry. Not a GPIO.            |
   +--------------+------+------+-----------------------------------------------------------------------+
   | +3.3 V       | P2   | 4    | Arduino +3.3 V unfiltered.                                            |
   +--------------+------+------+-----------------------------------------------------------------------+
   | +5 V         | P2   | 5    | Arduino +5 V, D6 cathode, 250 mV lower than LM2K Companion +5 V bus   |
   |              |      |      | if Arduino USB or power jack is not plugged in.                       |
   +--------------+------+------+-----------------------------------------------------------------------+
   | GND          | P2   | 6, 7 | Arduino GND.                                                          |
   +--------------+------+------+-----------------------------------------------------------------------+
   | VIN          | P2   | 8    | Arduino VIN header pin; not connected to LM2K circuitry.              |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D1/TX        | P3   | 2    | Available only if 7-segment LED A cathode is not used.                |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D2           | P3   | 3    | Available only if 7-segment LED B cathode is not used.                |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D3/PWM       | P3   | 4    | Available only if 7-segment LED C cathode is not used.                |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D4           | P3   | 5    | Available only if the CAN function for Arduino is not used.           |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D5/PWM       | P3   | 6    | Available only if the CAN function for Arduino is not used.           |
   +--------------+------+------+-----------------------------------------------------------------------+
   | D7           | P3   | 8    | Available only if 7-segment LED E cathode is not used.                |
   +--------------+------+------+-----------------------------------------------------------------------+
   | GND          | P4   | 7    | Arduino GND.                                                          |
   +--------------+------+------+-----------------------------------------------------------------------+
   | ARE          | P4   | 8    | Arduino AREF.                                                         |
   +--------------+------+------+-----------------------------------------------------------------------+


Working in conjunction with ADI ADALM2000 & Discovery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADALM female connectors/headers P12 is located on the left of the LM2K Companion
board for quick, non-invasive plug-in connections. A male type of connector
(P16) is placed right next to it, in a pin-to-pin vertical mirror arrangement,
allowing direct access to all ADALM or Discovery
ports.

.. figure:: adalm_top_accessible_headers_pcb.png
   :align: center
   :width: 400px

   ADALM top accessible headers: PCB view

.. figure:: adalm_top_accessible_headers_schematic.png
   :align: center
   :width: 650px

   ADALM top accessible headers: Schematic view

.. figure:: adalm_plugin.jpg
   :align: center
   :width: 400px

   ADALM plug-in

.. figure:: analog_discovery_plugin.jpg
   :align: center
   :width: 400px

   Analog Discovery plug-in

External M5STACK Display
^^^^^^^^^^^^^^^^^^^^^^^^^

There is a dedicated connector for an additional M5STACK Display P34.

.. note::

   A HY2.0-4P cable is necessary.

.. figure:: m5stack_display_connector.png
   :align: center
   :width: 400px

   External M5STACK display connector and cable

Generic Jumpwire IO bridge (P17 + P19)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LM2K Companion board includes two 8-pin female headers (P17 and P19),
connected pin-to-pin. These connectors form a generic jump-wire IO bridge that
can be used to route user-defined signals or external connections across the board.

All eight IO bridge lines are available for end-user configuration. Since these
lines are not assigned to a fixed onboard function, the user must verify the
signal source, voltage level, and direction before connecting external circuitry.

.. figure:: p17_p19_io_bridge_schematic.png
   :align: center
   :height: 400px

   P17+P19 IO Bridge connectors: Schematic view

.. figure:: p17_p19_io_bridge_pcb.jpg
   :align: center
   :width: 400px

   P17+P19 IO Bridge connectors: PCB view

Power supplies of the LM2K Companion board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LM2K Companion board is supplied from a +5 V USB source through the USB
Type-C connector P6.

- Connect the USB-C cable from a standard phone charger (min 1A) to the USB
  Type-C port named P6 on the board. Green LED DS1 (+VBUS) indicates the presence
  of input power supply.

.. note::

   It does not indicate that the board is powered ON, it just indicates the
   presence of input supply power—see Figure 13.

- Power ON the LM2K Companion Board via S1 slide switch. When S1 is switched
  to "ON" position, the Green LED DS2 (+5 V) lights up indicating that +VBUS
  power is delivered to the Board +5 V.

.. note::

   If DS2 LED does not light up when S1 is in ON position, the over current
   protection may have been triggered, or the input power supply is no longer
   available—check DS1 LED status!

- Over current protection (OCP) threshold is set at 900 mA. In the event of an
  OCP, the board is auto powered OFF. Remove the Load/short-circuit from the 5 V
  Supply and power OFF the board. A power ON/OFF/ON cycle is required to reset
  the OCP.

.. note::

   Do not short the +5V_ard with the 5V bus, as this will bypass the anti-reverse
   supply diode D6. This may cause interference between the two USB power
   suppliers: Charger/PC-Laptop (assuming that the Arduino board is connected
   to a PC/Laptop). Moreover, the 5V bus is no longer protected by the LM2K
   Companion onboard OCP circuit and it will take power from 5V_ard bus.

.. figure:: power_connection_usb_c.png
   :align: center
   :width: 400px

   Power connection to the LM2K Companion V3: USB-C plug

.. figure:: lm2k_powered_usb_c.png
   :align: center

   LM2K Companion board powered through the USB-C input

.. caution::

   Power the LM2K Companion board from a 5 V USB charger, a standard phone
   charger, or a PC/laptop USB port.
   
   **Normal operation:** **Green LED D12** continuously lit; Red LED D6 off

.. caution::

   **Current limit: LED DS2 blinking:** The 500 mA current limit is reached. Remove
   the USB-C cable from P6 USB Type C receptacle and check the schematic on the
   breadboard in order to find a possible short circuit between power rails
   (for example 5 V shorted to ground or 12 V shorted to ground) or a high
   current path (the total current consumption must be under 900 mA)

.. caution::

   The current limiter Q1 NMOS switch gets hot during short circuit! DO NOT
   TOUCH! Touching it can result in a HAZARD.

Available Fixed Power supply outputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power consumption of LM2K Companion board is limited to 4.5 W from the
5 V USB supply. The current consumption is limited to 900 mA. The LM2K
Companion provides:

- +5 V supply rail
- 2x +3.3 V from Arduino AND/OR Local LDO
- ±12 V symmetrical supply rails

The 5 V supply rail
^^^^^^^^^^^^^^^^^^^^

The maximum available power at the 5 V supply rail is 3.5 W (5 V·700 mA). The
LM2K Companion quiescent current is approximately 200 mA, that leaves the user
with approx. 700 mA available current.

The 5 V supply rail is accessible at the female port P5/5 and TP3.

LED DS2 GREEN lit indicates the normal operation of the 5 V VCC power supply.

.. figure:: 5v_supply_rail_connector.png
   :align: center

   +5V supply rail connector pin location

.. note::

   The 5 V supply rail is not regulated on board, thus the voltage level is
   determined by the USB VBUS. This was found to be in the range of 4.8 V up
   to 6 V, depending on the USB power supply.

.. note::

   The voltage level at this pin is not regulated on board, it is determined
   by the VBUS+ level at the USB-C.

Two options for the +3.3 V supply rail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LM2K Companion board provides two possible sources for the +3.3 V supply
rail. The active source is selected using the P35 selection jumper. The +3.3 V
rail can be supplied either from the Arduino board or from an on-board LDO.
The +3.3V rail selected by the P35 jumper is then used to power all the +3.3 V
auxiliary circuitry on the LM2K Companion (Audio Amp, 20 MHz CLK, Programmable
Waveform Generator).

.. note::

   **The signal generator functions only if the P35 jumper is present, connecting
   the mid-pin with one of the side pins.** It is recommended to supply the signal
   generator from the on-board LDO – that is, connect the P35 jumper to the top
   pin, denoted 3V3_KIT, as this provides a more stable and noise-free power
   supply than the 3V3_ARD line.

.. figure:: p35_3v3_supply_source_selection_pcb.png
   :align: center
   :width: 400px

   P35 +3.3V supply source selection jumper: PCB view

.. figure:: p35_3v3_supply_source_selection_schematic.png
   :align: center
   :width: 400px

   P35 +3.3V supply source selection jumper: Schematic view

Arduino +3.3 V rail
""""""""""""""""""""

The +3.3V_ARD supply rail is provided by the Arduino via port P2/4, thus it is
available only if the Arduino is connected to the LM2K. This rail is regulated
by the Arduino local LDO and has a current capability of about 30 mA. The Arduino
provides overcurrent protection / short circuit protection, but such an event
might cause the Arduino to shut down / reset.

.. figure:: 3v3_supply_rail_pin_location.jpg
   :align: center
   :width: 400px

   +3.3V supply rail pin location

The on-board 3.3 V LDO (ADM7150ARDZ-3.3)
"""""""""""""""""""""""""""""""""""""""""

The LM2K Companion board also includes an on-board +3.3V LDO, implemented with
the ADM7150ARDZ-3.3; it has a current capability of maximum 800mA. This supply
option allows the board to generate its own regulated +3.3 V rail, independently
of the Arduino +3.3 V output. The on-board LDO that powers the +3.3V_KIT line.

.. figure:: 3v3_local_ldo_p35_schematic.png
   :align: center
   :width: 400px

   +3.3V Local LDO and P35 Selection Jumper: Schematic view

The ±12 V symmetrical supply rails
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ±12 V Rails are generated locally/on-board by the M1 circuit (TEM 3-0522N)
that is a fully integrated Switched-Mode Power Supply with fixed output voltages
at +12 V and -12 V with a current capability up to 125 mA per rail.

.. note::

   The available current for these supply rails is lower than 125 mA because the
   rails also supply on-board circuitry.

LEDs DS3 and DS4 lit GREEN indicate the "OK" status of the ±12 V supply:

- LED DS4 (green): When lit, it indicates the presence of +12 V supply rail.
- LED DS3 (green): When lit, it indicates the presence of -12 V supply rail.

.. note::

   The LED voltage drops are used as reference for the ±12 V Reference voltage
   generator/buffers described in the Adjustable Voltage and Current references
   section. The ±12 V supply rails are available for the user at P5 connector,
   pins 1 and 3, and TP5 and 6—see Figure 20.

.. figure:: 12v_symmetrical_supply_connector.png
   :align: center
   :height: 400px 

   ±12V symmetrical supply rail connector TP and pin location

Ground pins
^^^^^^^^^^^^

There is a single ground plane, common for all analog and digital sections,
also with the Arduino and ADALM/Discovery interfaces.

Multiple GND pins, both male and female, are available across the LM2K Companion
board—see Figure 21. Additional test pins are also provided on the board for
measurement and debugging purposes.

.. figure:: gnd_tp_pin_location.png
   :align: center
   :width: 700px

   TP and pin location GND provides access to board ground

Adjustable Voltage and Current references
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two adjustable voltage references and one current source reference
available onboard for the end-user:

Adjustable VREF_DC [-12 V, +12 V] range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LM2K Companion board has two adjustable DC reference voltage outputs,
REF1 and REF2. They are adjustable via the trimpot multiturn resistors R21
and R22 in the [-12 V, +12 V] range. Turn clockwise to increase the reference
voltage.

.. note::

   VREF outputs are low impedance outputs driven by an :adi:`ADA4511-2` op amp
   that can drive up to 22 mA of load (sink or source) in normal operation
   conditions and 60 mA in short circuit conditions.

These Adjustable VREF_DC are derived from two references/fixed voltage levels
obtained from the power supply status LEDs DS3 and DS4, VLED_FORWARD, dropout
referred to GND. They are denoted as REF_P and REF_N and have typical values of
+1.9 V and -1.9 V respectively. A fixed gain factor of 6.4 V/V is used to amplify
the non-inverting input voltage levels (INAP_REF & INBP_REF) set by the multiturn
resistors connected to these VLED_FORWARD reference voltage levels—see Figure 22.

.. figure:: adjustable_vref_dc_schematics.png
   :align: center
   :width: 400px

   Adjustable VREF_DC generators schematics

The adjustable output voltages REF1, REF2 and their reference levels REF_P and
REF_N are accessible at the connector P5, pins 8 and 9, and pins 11 and 12,
respectively—see Figure 23.

.. figure:: adjustable_vref_connector_pin_location.png
   :align: center
   :width: 400px

   Adjustable VREF connector and pin location on the board

DC current source with adjustable IDC between 350 µA and 60 mA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LM2K Companion board has one reference DC current source (:adi:`LT3092`)
adjustable in the range [350 µA to 60 mA]. Turn clockwise to increase the reference
current.

.. note::

   This current source is supplied from the +12 V rail and has a typical dropout
   of 1.2 V, thus can operate up to 10.8 V voltage levels. The output current is
   filtered with a 0.22 µF capacitor to ground, thus the user can expect a large
   inrush/initial current when connecting the source to the load, due to the charge
   accumulated in the filtering cap.

The adjustable current is accessible at the connector P5, pin 13—see Figure 24.

.. figure:: adjustable_current_source_connector.jpg
   :align: center
   :width: 400px

   Adjustable current source connector/pin location on the board

Audio amplifier
~~~~~~~~~~~~~~~

The LM2K Companion board includes a Headphone Audio Amplifier (:adi:`AD8532`)
with configurable voltage gain of 1:10:100 V/V for Right channel and fixed unity
gain on Left channel. It also has fine trim adjustable attenuation up to 1:10V/V
on both channels.

The left channel gain configuration is realized by means of Jumpers P38 & P39
while the attenuation for both channels is adjustable via multi-turn trimpots
R54 and R55. Turn clockwise to increase the attenuation.

In addition, the right channel can be re-configured as a microphone amplifier
via P18 jumper, thus connecting the amplifier input path to Jack input port
P15 pin 4.

.. note::

   Both the inputs and outputs are DC decoupled by means of series capacitors
   C35, C36 and C40 C42 respectively to operate with the asymmetric/single supply
   of the amplifier. Microphone input path is pre-biased with a 2.2 kΩ resistor
   to 3.3 V rail (phantom-power).

The amplifier is supplied from the +3.3 V rail; thus, the user can expect a
maximum output voltage excursion equal to its supply in no load conditions.

Also, the amplifier has external 15 Ω output resistors (R58, R59) for short
circuit protection; thus, the user can expect reduced output voltage swing
when driving a heavy load (4 to 32 Ω).

.. figure:: audio_amplifier_pcb_location.png
   :align: center
   :height: 400px

   Audio amplifier PCB location and its connectors

The section includes 3.5 mm female jack input and output ports, together with
associated jumper pins for jumper-wire connections—see Figure 25.

Onboard Sensors
~~~~~~~~~~~~~~~

There are two types of sensors placed on the LM2K Companion board available for
the end-user: one temperature sensor and two light sensors (IR & LDR)

Temperature sensor
^^^^^^^^^^^^^^^^^^

The LM2K Companion includes a temperature sensor (:adi:`TMP01`) with an analog 
(VPTAT: 5 mV/°K) output voltage characteristic. VPTAT varies from 1.165 V at 
−40 °C to 1.79 V at +85°C.

It also provides two active-low open-drain digital status outputs: 
:math:`\overline{OVER}` and :math:`\overline{UNDER}`, with preset thresholds
of 19 °C and 29 °C and hysteresis—see Figure 26.

.. figure:: tmp01_hysteresis_profile.png
   :align: center
   :width: 400px

   TMP01 Hysteresis Profile

The three outputs are available to the user at P13 port—see Figure 27.

.. note::

   A quick sensor test can be performed by touching A5 integrated circuit
   package: it will trigger the :math:`\overline{OVER}` status output. 4.7 kΩ
   pull-up resistors are recommended to be used for the status outputs.

.. figure:: temperature_sensor_tmp01_pcb.png
   :align: center

   Temperature sensor TMP01 PCB location.

Light sensors: IR TX/RX & LDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The LM2K Companion includes one IR LED, one IR phototransistor, and one
photoresistor for a wider light spectrum. The IR LED, IR phototransistor
and photoresistor terminals are accessible through the corresponding P9 and P10
headers—see Figure 28 and Figure 29.

.. figure:: light_sensors_ir_ldr_pcb.png
   :align: center

   Light Sensors IR TX/RX & LDR PCB location and connectors

.. figure:: light_sensors_ir_ldr_schematic.png
   :align: center
   :width: 600px

   Light sensors IR TX/RX and LDR schematic view.

User-accessible multi-turn potentiometers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LM2K Companion includes four multiturn linear potentiometers, with all
three terminals available to the user at header P7: R103 = 2 kΩ, R104 = 5 kΩ,
R105 = 10 kΩ, R106 = 100 kΩ.

.. figure:: user_potentiometers_schematics.png
   :align: center
   :width: 650px

   User-accessible multi-turn potentiometers schematics

.. figure:: user_potentiometers_pcb.png
   :align: center
   :height: 500px

   User-accessible multi-turn potentiometers and connector PCB location.

Digital/Binary controls
~~~~~~~~~~~~~~~~~~~~~~~~

The digital control section contains six logic controls implemented with 4
slide switches (Instances S6, S2, S4, S8) and 2 tactile push-buttons
(Instances S7 and S5).

Out of the four slide switches, only the first two comprise a 1.8ms debounce
circuitry (denoted SW1_DB and SW2_DB) while the last two (denoted SW3 & SW4)
do not. Similar case for the tactile push buttons; the first one is debounced
while the second is not.

The debounced digital controls are also buffered with HEX inverters (U6, 74AHCT14PW,118)
for enhanced switching noise immunity and low output impedance/large fanout.

Logic 0/1 is obtained as follows:

- Slide switch -> slide downwards='0' / slide forward='1'.
- Tactile push-button -> pressed & held='0' / released = '1'.

All digital controls are 5 V TTL and are current-limited to a short-circuit
current of maximum 15 mA per output by means of output series resistors of 330 Ω.

The digital states can be monitored by using the 7 Seg LED Display (common Anode,
open cathode -> lit= '0' logic). Each will be lit when a logic "1" is applied
to the input (J9 connector).

The digital/binary control switches and their corresponding outputs are accessible
on the PCB "BTNs and SWITCHES" section—see Figure 32.

.. figure:: digital_binary_control_pcb.png
   :align: center
   :width: 600px

   Digital/binary control location on PCB

.. figure:: digital_section_schematic.png
   :align: center
   :width: 700px

   Circuit schematic of the digital section

7-Segment Display
~~~~~~~~~~~~~~~~~~

The LM2K Companion board is equipped with an SMD_LED 7-segment with decimal
point (DP). The display uses common anodes connected to +5 V and series resistors
of 1K. The cathodes are accessible at P23 to P31 2x8 pins header (bottom row).

On the top row of these headers, there are direct connections to the Arduino
digital IO, thus placing jumpers to close these headers creates a quick link
between the cathodes and Arduino outputs.

.. figure:: 7seg_smd_led_pcb.png
   :align: center

   7-Segment SMD-LED PCB location and connector jumpers

.. figure:: 7seg_display_schematics.png
   :align: center
   :width: 500px

   7-Segment display schematics

CAN transceiver
~~~~~~~~~~~~~~~~

The LM2K board contains a +5 V CAN transceiver (:adi:`MAX33042`\ E) with
integrated protection for industrial applications. This device has extended
±40 V fault protection for equipment where overvoltage protection is required.
It also incorporates high ±40 kV ESD Human Body Model (HBM) protection and an
input common-mode range (CMR) of ±25 V.

- The data IO (RX/TX) of the transceiver are accessible via P21 and P22 3-pin
  headers that can also be configured as a quick-link to Arduino IO by using jumpers.
- The transceiver connects to CAN-bus at the P32 and P33 female 3-pin headers
  that are pin-to-pin linked for chained connection.
- The board also presents a 2x60 Ω (120 Ω) termination for the CAN-bus connection
  that is permanently connected.

.. figure:: can_arduino_jumpers_p21_p22_p33_p32.png
   :align: center
   :width: 600px

   CAN to Arduino connection Jumpers P21-P22, P33-P32.

.. figure:: can_schematics.png
   :align: center

   CAN schematics

Signal and PWM/CLK generator
----------------------------

Both the Signal and PWM/CLK generators are controlled from software, implemented
on an Arduino R4 Wi-Fi board, featuring an RA4M1 series microcontroller from Renesas,
running on a 48 MHz clock.

The software displays the Sig Gen or PWM/CLK menu to set the signal parameters
on the MIDAS display screen via on-board Rotary Encoder.

Navigating in the menu is straightforward:

- **Rotate Left or Right**: Change highlighted item in the menu or if an item
  is selected: Adjust the value of the selected item
- **Press**: Select an item or change selection
- **Long Press**: Exit to the upper-level menu

On-board signal generator
~~~~~~~~~~~~~~~~~~~~~~~~~

The Sine/Triangle/Square wave signal generator is based on the :adi:`AD9833`
Programmable WaveformnGenerator with an SPI interface, using SS_AD9833 =
Arduino Pin 10, controlled by the software on the Arduino R4 board.

At the :adi:`AD9833` output, the C24 capacitor removes the DC component;
afterwards the signal is sent through the R6-R39 divider, switchable by the
:adi:`ADG444` controlled switch, to the :adi:`AD5443` Multiplying DAC (MDAC),
as Figure 37 shows. Also both the :adi:`ADG444` and the :adi:`AD5443` are
controlled by the software running on the Arduino R4 board: the :adi:`ADG444`
with a GPIO port (Arduino Pin 6), while the :adi:`AD5443` with the SPI interface
with SS_AD5433 = Arduino Pin 8.

.. figure:: signal_generator_sig_gen_mdac_schematics.png
   :align: center

   Signal generator Sig_Gen, controlled switch and MDAC schematics

The :adi:`AD5443` is a 12-bit current output, with an R-2R configuration,
presenting a typical input equivalent resistance of 10 kΩ.

When sine or triangle wave is generated by the :adi:`AD9833`, its nominal output
amplitude is 600 mVpp. The :adi:`ADG444` switch must be off, so this value is
divided by the MDAC input resistance:

.. math::

   V_{REF\_SIN\_NOM} = \frac{10k\Omega}{R_6 + 10k\Omega} \cdot 600mV_{pp} = 545mV_{pp}

When square wave is generated by the :adi:`AD9833`, its nominal output amplitude
is 3.3 Vpp. The :adi:`ADG444` switch must be on, so this value is divided by R39
and the MDAC input resistance:

.. math::

   V_{REF\_SQW\_NOM} = \frac{(10k\Omega || R_{39})}{R_6 + (10k\Omega || R_{39})} \cdot 3.3V_{pp} = 540mV_{pp}

The output of the :adi:`AD5443` DAC is converted to voltage by A6, an :adi:`AD8065`
op amp. Because the RFB feedback input also features a 10KΩ typical resistance,
the output of the op amp will be equal to VREF divided by the DAC value:

.. math::

   V_{O\_A6} = \frac{D}{2^{12}} \cdot V_{REF\_DAC}

where D is the DAC value, that is, the fractional representation of the digital
word loaded to the DAC, D = 0…4095.

The output of A6 is followed by two stages, both implemented with an :adi:`AD8066`
op amp, see the schematic in Figure 38. The total gain of the two stages can be
calculated as:

.. math::

   G_{Siggen} = \left(1 + \frac{R_{40}}{R_{13}}\right) \cdot \left(-\frac{R_{44}}{R_{43}}\right) = 6.9 \cdot (-5.9) = -40.71

.. figure:: signal_generator_output_stage_schematics.png
   :align: center

   Signal generator Sig_Gen output stage schematics

Although the gain is inverting, this does not change the signal generator behavior.
The final amplifier output of the signal generator is accessible at the "SIG GEN"
section at P8 and TP15, noted as "OUT_SG" on the silk screen—see Figure 40.

The maximum output amplitude of the signal generator is, for sine and triangle wave:

.. math::

   |V_{Out\_Siggen\_Sine}| = \left|V_{REF\_SIN\_NOM} \cdot \frac{D}{2^N} \cdot G_{Siggen}\right| = \frac{D}{2^N} \cdot 22.186V_{pp} = max.\ 22.18V_{PP}

and for the square wave:

.. math::

   |V_{Out\_Siggen\_SQW}| = \left|V_{REF\_SQW\_NOM} \cdot \frac{D}{2^N} \cdot G_{Siggen}\right| = \frac{D}{2^N} \cdot 21.983V_{pp} = max.\ 21.978V_{PP}

Note that the output amplitude is limited by the software to maximum 20 VPP. If
we express the output voltage in function of the D value sent to the :adi:`AD5443` DAC,
that is, express the number of volts per 1 LSB, we have the following nominal values:

For sine and triangle wave:

.. math::

   V_{lsb\_Siggen\_Sine} = V_{Out\_Siggen\_Sine}\big|_{D=1} = \frac{22.186V}{4096\ lsb} = 5.4165\ mV/lsb

For square wave:

.. math::

   V_{lsb\_Siggen\_SQW} = V_{Out\_Siggen\_SQW}\big|_{D=1} = \frac{21.983V}{4096\ lsb} = 5.3669\ mV/lsb

Note that these are nominal values and depend on many factors such as the
:adi:`AD9833`'s real output voltage, the non-zero error, the monotony of the :adi:`AD5443`
DAC, and the resistor's tolerances. The above values are set by constants in the software
application and can be adjusted in the calibration
menu.

.. figure:: signal_generator_output_connector.png
   :align: center
   :width: 400px

   Signal generator Sig_Gen output connector

The Sig Gen output is protected against short circuit damage by means of a 220 Ω / 2 W
(R50) output series resistor that is included in the negative feedback loop. Thus, the
output impedance of the Sig Gen is <1 Ω up to 54 mA load currents (12 V/220 Ω).

The absolute maximum output swing is dependent on the loading current such that:

.. math::

   Sig\_Gen_{out\_max/min} = \pm |12V - I_{LOAD} \cdot 220|

This includes both the Offset and amplitude.

Example: For a 50 Ω standard Load, the max/min output level can be calculated as:

.. math::

   Sig\_Gen_{out\_max/min}\bigg|_{50\Omega} = \pm \frac{Z_{LOAD}}{Z_{LOAD} + 220} \cdot 12V = \pm \frac{50}{50 + 220} \cdot 12V = \pm 2.22V

Setting the amplitude above this value determines the :adi:`AD8066` operational
amplifier output to saturate, thus truncated waveforms are achieved at the Sig_Gen
output.

The Sig_Gen output can also be driven into saturation with HiZ loads if the sum of
amplitude and offset settings exceeds the ±12 V supply rail. The Sig_Gen parameters
settings menu does not limit the user to enter values that will saturate the Sig_Gen
output, precisely for educational purposes. In this way truncated waveforms can be
obtained.

.. note::

   The LM2K Sig_Gen has a bandwidth limitation of 2MHz, however, setting the
   frequency higher than 400 kHz will result in attenuated amplitude versus
   the set amplitude. The expected Sine amplitude attenuation for a specific
   frequency can be estimated considering the frequency characteristic that
   presents a -20 dB/decade slope past the cutoff frequency of @400 kHz. While 
   for the square wave, the bandwidth limitation impacts the rise/fall edge
   rates first @200 kHz and only later the amplitude.

On-board signal generator's DC offset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DC offset of the signal generator is provided by the :adi:`AD5625R` 12-bit
quad DAC, controlled by the I2C protocol, as shown in Figure 40. Two of the DAC
outputs are fed to the one op amp differential amplifier implemented by the
:adi:`ADA4077-1`.

The output voltage at the differential amplifier can be expressed as:

.. math::

   V_{OUT\_OFFSET\_DAC} = \frac{R_{45}}{R_{41}} \cdot (V_{VOUT\_DAC\_1} - V_{VOUT\_DAC\_2}) = 0.36 \cdot (V_{VOUT\_DAC\_1} - V_{VOUT\_DAC\_2})

.. figure:: signal_generator_dc_offset_schematics.png
   :align: center

   Signal generator DC offset generation schematics

The differential amplifier's output is connected to the noninverting input of
the output stage, as Figure 41 shows. As the maximum value of
:math:`(V_VOUT_DAC_1 - V_VOUT_DAC_2)`` is ±5 V, it follows that the maximum
DC output voltage of the signal generator is:

.. math::

   V_{OUT\_MAX\_SIG\_GEN}\bigg|_{DC} = \left(1 + \frac{R_{44}}{R_{43}}\right) \cdot V_{OUT_{OFFSET_{DAC}}} = 6.9 \cdot 0.36 \cdot (\pm 5V) = \pm 12.42V

.. figure:: signal_generator_dc_offset_output_stage.png
   :align: center

   Signal generator DC offset at the output stage

Note that the output offset voltage is limited by software to ±10 V. Also note
that the signal generator menu allows stopping the :adi:`AD9833` wave output
(waveform: OFF) and adjusting the DC offset to a nonzero value. In this way,
the signal generator can be used as a third DC reference voltage.

Expressing the signal generator's DC output in terms of V per LSB, results:

.. math::

   V_{lsb\_DC\_OFFSET} = \frac{|V_{OUT\_MAX\_SIG\_GEN}|_{DC}|}{4096} = 3.032mV/lsb

Like the signal generator amplitude V/LSB values, this is a nominal value and
can also slightly differ in the real circuit. However, due to the :adi:`AD5625R`'s
internal precision voltage reference and the 1% tolerance resistances used in
the gain stages, this value is not adjusted in software during calibration. Instead,
the calibration procedure adjusts the Signal Generator's initial offset to 0 as
close as possible.

PWM/CLK generator
~~~~~~~~~~~~~~~~~

The PWM/Clock signal generator is implemented by the RA4M1 microcontroller's
Timer peripheral, connected to a PWM output (pin D9/PWM on the Arduino R4).
Frequency and Duty cycle can be set in PWM/CLK operating mode interface of
the signal generator menu.

Note that both the signal generator and the PWM/CLK generator can run independently,
set from the generator menu.

The output of the PWM generator is then buffered using two HEX inverters,
providing the 5V-TTL clock and an inverted version of the Clock signal: CLK/PWM
and :math:`\overline{CLK}`/:math:`\overline{PWM}`. The two clock signals are
accessible at TP17 and TP21 and connector P14 pin 7 and 8—see Figure 43.

Furthermore, the CLK real-time state can be monitored with the dedicated LED
DS5 that lights up green when PWM/CLK outputs state is logic '1' up to 20 Hz.
For higher frequency (larger than about 25 Hz), the PWM output can be used to
modulate the brightness of the DS5 LED.

.. figure:: clk_pwm_output_connector.png
   :align: center
   :width: 400px

   CLK/PWM output test points and connector location

Display
-------

The LM2K Companion board includes a MIDAS MDOB128064V2V-Y graphic OLED
monochrome display, 128 x 64 Pixels, accessible via I2C. This display is
directly connected to the Arduino plugin header at P4/9,10 (SDA, SCL). Two
pull up 10 kΩ resistors (R8, R9) are placed on the board for the
SDA and SCL I2C bus. Note that the I2C address is 0x3C.


.. figure:: main_oled_display_midas.png
   :align: center
   :width: 400px

   Main OLED Display – MIDAS

.. grid::
   :widths: 60% 40%

   .. figure:: main_oled_display_schematic1.png
      :align: center
      :height: 350px

      Main OLED Display – schematic connections

   .. image:: main_oled_display_schematic2.png
      :align: center
      :height: 350px

      
      

Menu - User Interface
---------------------

Calibration procedure interface (Sig Gen offset and amplitude)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Operating modes interface:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sig_Gen and PWM/CLK generator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Sig_Gen menu is accessible using a rotary encoder with push-to-click
functionality. The selection is highlighted by a borderline around the target
parameters. A click on the rotary encoder allows the user to edit the selected
parameter. After the edit is done, a second click on the rotary encoder will
jump back to the parameters list.

The Sig Gen and PWM/CLK menu includes access to following parameters:

- Waveform type: Off/Sine/Triangle/Square/PWM/CLK.
- Peak to peak amplitude: In the range of [100 mV – 20 V], 100 mV steps.
- Frequency: In the range of [10 Hz – 2 MHz] ([1Hz…2MHz] for PWM).
- DC offset in the range of [-10 V +10 V], 100 mV steps.
- PWM/CLK duty cycle: In the range of [1% - 99%]

The Peak-to-peak amplitude and offset settings are available only for the Sinus,
Triangle, and Square waveforms, while the PWM/CLK signals are 5 V TTL routed on
separated output pins—see PWM/CLK generator section.

The edited Sig_Gen parameters are updated instantaneously, no click to confirm
is required.

.. figure:: sig_gen_menu.png
   :align: center
   :width: 400px

   Sig_Gen MENU

Offset DAC as Programmable Supply Rail / Audio DSP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AD5625RBRUZ-1 DAC in conjunction with Arduino can be programmed to
work as a custom waveform generator OR an audio DSP. The on-board signal generator
can be set to deliver a 0 V DC level at OUT_STAGE1, thus enabling the user to
experiment with the DAC via I2C, and routing the amplified signal to the Sig_Gen
output that can be further routed to the audio amplifier such that the result can
be heard via headphones or speaker.

