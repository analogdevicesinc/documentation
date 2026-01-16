AD-PS3803-RD
============

PoE+ with Ideal Diode Bridge to Isolated Flyback DC/DC (12V, 2A)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. figure:: ad-ps3803-rd_angle.jpg
  :width: 400 px
  :align: left

  AD-PS3803-RD Board

The :adi:`AD-PS3803-RD` reference design is a power converter
capable of harnessing any IEEE802.3at (PoE+, Type 2)-compliant downstream
power over Ethernet (PoE) supply to provide a galvanically isolated DC power.

At the core of this solution is the :adi:`LT8306` 60V no-opto flyback
controller, stepping down the 37V to 57V PoE input voltage to a 12V, 24W
DC output.

The on-board :adi:`LT4275` LTPoE++/PoE+/PoE power delivery (PD)
controller handles interfacing and power delivery to any PoE supply.

The :adi:`LT4321` ideal diode bridge controller is used for improved
end-to-end power delivery efficiency and eased thermal design by utilizing low
RDS(ON) N-Channel FETs, replacing the eight-diode configuration typically found
in passive PoE rectifier bridge.

The AD-PS3803-RD also has auxiliary DC power support for a wide input range of
37V to 57V.

Features
--------

- Galvanically isolated 12 V flyback DC output with up to 24 W of output power
  capability
- No transformer third winding or opto-isolator for output regulation
- Supports IEEE802.3at (PoE+, Type 2) and IEEE802.3bt (PoE++, Type 3 and 4)
  interfacing and power supply control via a configurable jumper array
- Supports a wide input DC auxiliary power of 37 V to 57 V

Applications
------------

- Industrial Automation
- Surveillance Camera Systems
- VoIP Phones
- Payment Terminal Systems
- Wireless Access Points

Block Diagram
--------------

.. figure:: ad-ps3803-rd_block_diagram.png

  AD-PS3803-RD Simplified System Block Diagram

Specifications
--------------

.. csv-table:: Board Performance Summary
   :file: specifications.csv

Components and Connections
--------------------------

Basic Input and Output Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ad-ps3803-rd_03.png

   Basic Input Output Ports

.. warning::

   Observe correct polarity for each port connection to prevent
   damaging the device.

Power Supply Ports
~~~~~~~~~~~~~~~~~~

Power the board either through its RJ45 female connector (PoE input)
or via its DC auxiliary terminals.

Both ports can handle input voltage of 37 V:sub:`DC` to 57 V:sub:`DC`.

- **P1** - RJ45 input port for PoE from PSE
- **AUX+** - Positive input terminal for auxiliary DC power supply
- **AUX-** - Negative input terminal for auxiliary DC power supply

Output Ports
~~~~~~~~~~~~

- **VOUT+** - Positive output terminal of the board
- **VOUT-** - Negative output terminal of the board
- **TP14** - POE_OUT+ terminal. This is the positive terminal of the
  passthrough voltage from either the PoE input or the auxiliary input.
- **TP15** - POE_OUT- terminal. This is the positive terminal of the
  passthrough voltage from either the PoE input or the auxiliary input.
- **P2** - RJ45 output port for PHY

LED Indicators
~~~~~~~~~~~~~~

- **DS1** - Indicator for successful PD and PSE handshaking. This should remain
  turned on during normal operation.

Test Points
~~~~~~~~~~~~

Numerous test points such as turrets and test pads were added for
easier probing of signals.

.. figure:: ad-ps3803-rd_04.png

  Board Test Points

Ethernet Pairs
~~~~~~~~~~~~~~

- **TP1** - DATA-1 wire pair test pad
- **TP2** - DATA-2 wire pair test pad
- **TP3** - SPARE-1 wire pair test pad
- **TP4** - SPARE-2 wire pair test pad

Accessory Test Points
~~~~~~~~~~~~~~~~~~~~~

- **TP5** - Turret for AUX+ terminal
- **TP6** - Turret for AUX- terminal
- **TP7** - Test pad for T2P~
- **TP8** - Test pad for PWRGD
- **VPORT+** - Test pad for the positive terminal of the rectified voltage
  after the ideal diode bridge
- **VPORT-** - Test pad for the negative terminal of the rectified voltage
  after the ideal diode bridge
- **PWRGD** - Power good indicator. This terminal is pulled high when
  negotiation with PSE is established and power is available. Logic level is
  equal to voltage at POE_OUT+ terminal with respect to POE_OUT-.
- **T2P~** - PSE type indicator. Pulled down when a IEEE802.3at (PoE+, Type 2)
  compliant PSE is connected. A square wave with 50% duty cycle can be read when
  a LTPoE+.+ compliant PSE is detected.
- **TP16** - Turret for VOUT+ terminal
- **TP17** - Turret for VOUT- terminal

Class Select Jumpers
~~~~~~~~~~~~~~~~~~~~

The board's operating power level can be configured by changing the
position of the class select jumpers, allowing different PSEs to be compatible
with the device.

.. figure:: ad-ps3803-rd_05.png

   Class Select Jumper Array


**Table 1: Jumper Position**

=============== ===================== =====================
**Power Level** **Jumper 1 Position** **Jumper 2 Position**
=============== ===================== =====================
25.5 W          JP9                   JP10
38.7 W          JP11                  JP12
52.7 W          JP13                  JP14
70.0 W          JP15                  JP16
90.0 W          JP17                  JP18
=============== ===================== =====================

Circuit Evaluation
------------------

AD-PS3803-RD Quick Start Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power over Ethernet using a Power Sourcing Equipment (PSE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Figures 6 and 7 show the setup for evaluating the AD-PS3803-RD
using a PSE. A resistive load or an active load can be used at the
output stage of the device.

.. tip::
  Default class select shunt positions are at
  **JP9** and **JP10** on the AD-PS3803-RD board.

  With this configuration, any PSE with sufficient power will turn on the board.
  Refer to Table 2 for the shunt positions in selecting a different power level.

#. Check the power delivery capacity of the PSE, ensure that it can provide the
   required power and load.

   .. important::
      Avoid selecting a jumper configuration corresponding to a higher power level
      than the PSE can provide. Otherwise, the PSE will not turn on the board after
      its classification stage.

#. Connect the output of the PSE to the RJ45 connector (P1) on the AD-PS3803-RD
   board using a CAT5e or CAT6 Ethernet cable.
#. After connection has been established, verify that the LED (DS1) is on. This
   indicates successful handshaking between the PSE and AD-PS3803-RD.
#. Check for the proper output voltages. The output at the VOUT+ and VOUT- ports
   should be regulated at 12 V (±5%).
#. Once the proper output voltage is established, connect the load at the VOUT+
   and VOUT- ports of the AD-PS3803-RD, observing proper polarity of the
   terminals.
#. Adjust the load current within the operating range and observe the output
   voltage regulation, ripple voltage, and other parameters.

   .. note::

      The AD-PS3803-RD requires a very small minimum load to maintain good
      output voltage regulation. A Zener diode is placed on the output to clamp
      the voltage to 13V at no load.

   .. figure:: ad-ps3803-rd_06.png

      AD-PS3803-RD Setup with a Power Sourcing Equipment (PSE)

   .. figure:: ad-ps3803-rd_07.png

      AD-PS3803-RD Setup  Using a PSE Board Module

   .. figure:: ad-ps3803-rd_08.png

      Example Setup using a PSE Module (DC2541A)

Auxiliary Power Supply
^^^^^^^^^^^^^^^^^^^^^^

Refer to Figure 9 for evaluating the AD-PS3803-RD using an auxiliary
power supply. A resistive load or an active load can be used at
the output stage of the device.

#. Connect the auxiliary supply to the AUX+ to AUX- inputs. Observe proper
   polarity of voltage connection before turning on the auxiliary power supply.
#. Turn on the auxiliary power supply and verify that the LED (DS1) is on.
#. Check for the proper output voltages. The output at the VOUT+ and VOUT- ports
   should be regulated at 12 V (±5%).
#. Once the proper output voltage is established, connect the load at the VOUT+
   and VOUT- ports of the AD-PS3803-RD as illustrated in Figure 9.

.. warning::

   Observe correct polarity of connections to prevent damaging the device.

.. figure:: ad-ps3803-rd_09.png

   AD-PS3803-RD Test Setup using an Auxiliary Power Supply

Demo Setup
----------

Equipment Needed
~~~~~~~~~~~~~~~~

- One (1) Programmable DC power supply capable of 60V/3A (DC power supply)
- One (1) DC2541A PSE controller board (PSE)
- One (1) RJ45-to-RJ45 Ethernet cable
- One (1) Digital multimeter (Voltmeter #1)
- One (1) Electronic load capable of 12V/2A (DC electronic load)

Getting Started
~~~~~~~~~~~~~~~

.. note::

   The setup described below uses the DC2541A Demo Board as PSE Controller.
   Other PSE boards can also be used as alternative, but ensure that the
   interface and power range is compatible with the AD-PS3803-RD.

#.  Before connecting any power supplies, adjust the DC power supply’s output
    to 0V and set the current limit to 0.1A.
#.  Turn the supply OFF.
#.  Connect all the equipment, as shown in Figure 1. Do NOT connect the
    Ethernet cable to AD-PS3803-RD yet.

    .. figure:: ad-ps3803-rd_10.png

       AD-PS3803 Test Setup Diagram

#.  Verify that the electronic load is initially at the OFF position.
#.  Ensure that the indicated jumper position for DC2541A is set correctly,
    as shown in Table 1 and Figure 3.

**Table 2: DC2541A PSE Board Jumper Configuration**

+------------+------------+------------+------------+------------+------------+
| PSE        | Power      | PORT+      | MID        | DUALPD     | LEGACY     |
| Type       | Mode       | (JP1) /    | (JP3)      | (JP4)      | (JP5)      |
|            | (JP6)      | PORT-(JP2) |            |            |            |
+============+============+============+============+============+============+
| IEEE       | Type 2     | 2-PAIR     | LO/HI      | LO         | LO         |
| 802.3at    | (25.5W)    |            |            |            |            |
| Type 2     |            |            |            |            |            |
| (25.5W)    |            |            |            |            |            |
+------------+------------+------------+------------+------------+------------+

.. figure:: ad-ps3803-rd_11.png

   Jumper Connections

Test Measurement
~~~~~~~~~~~~~~~~

#. Turn the DC power supply ON and set the voltage to approximately 48V.
#. Set the DC power supply current limit to 1A.
#. Connect the RJ45-to-RJ45 Ethernet cable to AD-PS3803-RD, as illustrated in
   Figure 1.
#. Turn ON the DC electronic load and set carefully set the current to 2A only.
#. Check the output voltage reading from Voltmeter #1 and verify that it is
   within the maximum and minimum limits, as indicated in Table 3.

**Table 3: Output Voltage Limits**

================================== ========================== ===========
**Assembly**                       **Output Voltage Range (V)
                                   [Voltmeter #1]**
================================== ========================== ===========
AD-PS3803-RD                       Minimum (V)                Maximum (V)
                                   11.76                      12.24
================================== ========================== ===========

#. Set the DC power supply voltage to approximately 57V.
#. Verify that the DC electronic load is still set to the current of 2A.
#. Check the output voltage reading from Voltmeter #1 and verify that it is
   within the maximum and minimum limits as indicated in Table 3.
#. Set the DC electronic load to 0A.
#. Disconnect the RJ45-to-RJ45 Ethernet cable from AD-PS3803-RD.

.. figure:: ad-ps3803-rd_12.png

   AD-PSD3803 Actual Test Setup

System Performance
------------------

Efficiency
~~~~~~~~~~

Below figure shows the efficiency performance of AD-PS3803-RD at PoE input voltage
of 48V and 57V.

.. figure:: ad-ps3803-rd_13.png
   :width: 500 px

   AD-PS3803-RD Efficiency vs. Load Current Performance

Output Regulation
~~~~~~~~~~~~~~~~~~

The AD-PS3803-RD maintains within ±5% across its entire output current
capability.

.. figure:: 014.png

  AD-PS3803-RD: Output Voltage vs. Load Current Performance

Resources
---------

- :adi:`LT8306 Product Page <lt8306>`
- :adi:`LT4275 Product Page <lt4275>`
- :adi:`LT4321 Product Page <lt4321>`
- :adi:`DC2541A Demo Manual <media/en/technical-documentation/user-guides/DC2541A.PDF>`

Design & Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`AD-PS3803-RD Design & Integration Files <ad-ps3803-rd-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project
   - LTspice Simulation

Help and Support
----------------

For questions and more information, please visit the
:ez:`Analog Devices Engineer Zone <reference-designs>`.
