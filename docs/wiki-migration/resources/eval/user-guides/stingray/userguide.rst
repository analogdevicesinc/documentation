ADAR1000EVAL1Z (STINGRAY) ANALOG BEAMFORMING FRONT-END
======================================================

GENERAL DESCRIPTION
===================

The ADAR1000-EVAL1Z evaluation board is an analog beamforming front-end designed for testing the performance of the :adi:`adar1000` and :adi:`adtr1107`. The :adi:`adar1000` is an 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer IC. The :adi:`adtr1107` is a 6 GHz to 18 GHz, Front-End Transmit/Receive module.

The ADAR1000-EVAL1Z board consists of 8 RF cells. Each cell contains a core :adi:`adar1000` surrounded by four :adi:`ADTR1107s <adtr1107>`. All RF input/outputs on the evaluation board are brought out to SMPM coaxial connectors. There is a 12V power input and all required voltage rails for the board are generated on-board. Digital control of the board as well as the beamformers is enabled using either an :adi:`System Demonstration Platform (SDP-S) <SDP-S>` connector or a dual PMOD interface. Control signals for the board are expected to be 3.3V logic with on-board level translators converting this to the on-chip logic level of 1.8V.


|image1|

.. container:: centeralign

   \ **Figure 1A: ADAR1000EVAL1Z Front**\


   |image2|

.. container:: centeralign

   \ **Figure 1B: ADAR1000EVAL1Z Back**\


   |image3|

.. container:: centeralign

   \ **Figure 1C: ADAR1000EVAL1Z with Heatsink**\


   |image4|

.. container:: centeralign

   \ **Figure 1D: ADAR1000EVAL1Z with Antenna Tiles**\


--------------

Main RFICs
----------

ADAR1000: 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`ADAR1000 Product page <adar1000>`
-  :doc:`ADAR1000 Datasheet and Silicon Errata </wiki-migration/resources/errata/adar1000>`

ADTR1107: 6 GHz to 18 GHz, Front-End Transmit/Receive Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`ADTR1107 Product page <adtr1107>`

Peripheral ICs
--------------

RF Detector Block
~~~~~~~~~~~~~~~~~

-  :adi:`HMC948 Log Detector <hmc948>`
-  :adi:`ADA4807-1 180MHz, Rail-to-Rail Input/Output Operational Amplifier <ada4807-1>`
   \* :adi:`LTC2314-14 14-Bit, 4.5Msps Serial Sampling ADC <ltc2314-14>`

Power Generation
~~~~~~~~~~~~~~~~

-  :adi:`LT8652S Dual Channel 18V/8.5A, Synchronous Step-Down Silent Switcher <lt8652s>`
   \* :adi:`LT8642S 18V/10A Synchronous Step-Down Silent Switcher 2 <lt8642s>`
   \* :adi:`LT3093 –20V/200mA, Ultralow Noise, Ultrahigh PSRR Negative Linear Regulator <lt3093>`
   \* :adi:`LT3094 −20V/500mA, Ultralow Noise, Ultrahigh PSRR Negative Linear Regulator <lt3094>`
   \* :adi:`LT8606 42V/350mA Synchronous Step-Down Regulator <lt8606>`
   \* :adi:`ADP150-1.8 1.8V Ultralow Noise, 150 mA CMOS Linear Regulator <adp150>`
   \* :adi:`ADP5074 2.4A, DC-to-DC Inverting Regulator <adp5074>`

Control & Monitoring
~~~~~~~~~~~~~~~~~~~~

-  :adi:`ADM1172-1 Hot Swap Controller with Power-Fail Comparator <adm1172>`
   \* :adi:`ADM1186-2 Quad Voltage Sequencer and Monitor with Programmable Timing <adm1186>`
   \* :adi:`LTC2992 Dual, Wide-Range Power Monitor with GPIO <ltc2992>` **(RevB only)**
   \* :adi:`LTC4301 Supply Independent Hot Swappable 2-Wire Bus Buffer <ltc4301>` **(RevB only)**

--------------

REQUIREMENTS
============

Documents
---------

-  :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>`
-  :adi:`ADTR1107 Datasheet <media/en/technical-documentation/data-sheets/ADTR1107.pdf>`
-  `Assembly Drawing <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_assembly_v2.pdf>`__
-  `Board Dimensions <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_dimensions.zip>`__
-  Rev. A design:

   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/059522a_modified.pdf>`__
   -  `BOM <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/059522a_bom.zip>`__

-  Rev. B/C design:

   -  `Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/02_059522b_top.pdf>`__
   -  `BOM <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/059522b_bom.zip>`__

Hardware
--------

-  ADAR1000-EVAL1Z Evaluation Board Kit
-  Snap-on Antenna Board (available upon request)
-  SMPM-SMA cabling to interface with the RF ports
-  Digital controller and any associated hardware (:adi:`SDP-S` or PMOD)

|

.. warning::

   The SDP-S is the only SDP controller which will work with Stingray.

   | All other SDP controllers (SDP-B, SDP-H1, SDP-K1) are **NOT** compatible with the Stingray platform.


Suggested Test Equipment
------------------------

-  20GHz RF Signal Generator
-  20GHz Spectrum Analyzer
-  20GHz Vector Network Analyzer
-  Thermal Camera (optional)
-  Oscilloscope (optional)
-  RF Power Meter (optional)

Software/Digital Control
------------------------

PMOD Control
~~~~~~~~~~~~

-  Two 12-pin PMOD cables (`Example <https://www.mouser.com/ProductDetail/Samtec/IDSD-06-D-1800-R?qs=0lQeLiL1qybunuONxYyYYQ%3D%3D>`__)
-  Four 12-pin 0.100" male-male headers (`Example <https://www.digikey.com/en/products/detail/samtec-inc/TSW-106-22-T-D/7867287>`__)
-  Example PMOD digital controllers:

   -  `Raspberry Pi <https://www.raspberrypi.org/>`__
   -  FPGA demonstration board
   -  `Arduino <https://www.arduino.cc/>`__
   -  `FTDI <https://www.ftdichip.com/>`__

SDP Control
~~~~~~~~~~~

-  `SDP Drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`__
-  `Basic SDP Test Program <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_test.zip>`__ (Windows 10 might try to block this, you'll have to explicitly allow it in your security settings)
-  :adi:`SDP-S controller board <sdp-s>`

.. note::

   SDP Control is fine for initial characterization. Recommended to use the linux drivers for end system control for easier software control and software scalability.


Software
~~~~~~~~

-  :git-linux:`ADAR1000 LibIIO Linux Driver <drivers/iio/beamformer/adar1000.c>`

   -  :doc:`Driver Documentation </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adar1000>`

-  :git-pyadi-iio>`__ interface for LibIIO

   -  `ADAR1000 wrapper <https::`PyADI-IIO </github.com/pyadi-iio?master/adi/adar1000.py>`
   -  `ADAR1000 Documentation <https://analogdevicesinc.github.io/pyadi-iio/devices/adi.adar1000.html>`__
   -  `Example for single ADAR1000 <https://github.com/pyadi-iio?master/examples/adar1000_single_example.py>`__
   -  `Example for array of ADAR1000s <https://github.com/pyadi-iio?master/examples/adar1000_array_example.py>`__

--------------

BOARD DESIGN
============

The ADAR1000-EVAL1Z evaluation board has 8 SMPM RFIO connectors for the 8 cells on the component side of the board. There are 33 SMPM connectors on the opposite side of the board. 32 of these correspond to the 32 RF channels while the last connector goes to the RF detector and ADC combo on the bottom of the board which is intended to be used for calibration.

Two 6-pin Molex "Mini-Fit Jr." connectors are provided to apply the required 12V power supply. One is for the power supply input, and the other can be used to daisy-chain a second board to power both boards using one power supply. Note that the included power supply can only support two ADAR1000-EVAL1Z boards.

Power Supply
------------

The ADAR1000-EVAL1Z board must be powered from the included power supply with a voltage level of 12V. There is an on-board power management tree which generates the required voltage rails for all of the associated parts.

RF Input and Output Signals
---------------------------

The ADAR1000-EVAL1Z board has 41 surface-mounted SMPM connectors which are described in Table 1. **

.. container:: center

   Table 1: RF Connectors


**

+----------------------------------------------------+---+--------------------------------------------------------------------+---+-----------------------------+
| Connector(s)                                       |   | Name(s)                                                            |   | Description                 |
+====================================================+===+====================================================================+===+=============================+
| J1 - J8                                            |   | RFIOx                                                              |   | ADAR1000 RFIO Connectors    |
+----------------------------------------------------+---+--------------------------------------------------------------------+---+-----------------------------+
| J1_1 - J1_8, J2_1 - J2_8, J3_1 - J3_8, J4_1 - J4_8 |   | ANT1_1 - ANT1_8, ANT2_1 - ANT2_8, ANT3_1 - ANT3_8, ANT4_1 - ANT4_8 |   | Antenna Connectors          |
+----------------------------------------------------+---+--------------------------------------------------------------------+---+-----------------------------+
| J9                                                 |   | N/A                                                                |   | RF Detector Input Connector |
+----------------------------------------------------+---+--------------------------------------------------------------------+---+-----------------------------+

|ADAR1000-EVAL1Z Component Side Overview| **

.. container:: centeralign

   Figure 2: ADAR1000-EVAL1Z Component Side Overview


**

|ADAR1000-EVAL1Z Antenna Side Overview| **

.. container:: centeralign

   Figure 3: ADAR1000-EVAL1Z Antenna Side Overview


**

Digital Signals
---------------

The digital input signals are intended to be 3.3V logic while the :adi:`adar1000` requires logic levels of 1.8V. To protect the :adi:`adar1000`, level translators have been included between the digital connectors and the :adi:`ADAR1000s <adar1000>`. There are test points on the 1.8V side of the level translators, but these are not meant to be used to inject signals, only to view the signals reaching the :adi:`ADAR1000s <adar1000>`.

PMOD Pinout
^^^^^^^^^^^

|PMOD Pinout| **

.. container:: centeralign

   Figure 4: ADAR1000-EVAL1Z PMOD Pinout


**

SPI Control
^^^^^^^^^^^

The ADAR1000-EVAL1Z has five chip-select lines available for use. Four of these lines (CSB1, CSB2, CSB3, CSB4) are intended to be used for the :adi:`ADAR1000s <adar1000>` while the last line (CSB5) is dedicated for the RF detector/ADC combo on the antenna side of the board.

Each :adi:`adar1000` has two ADDRx pins which can be used to control 4 separate :adi:`ADAR1000s <adar1000>` using only one CSB line. See the :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>` for details on this. As the ADAR1000-EVAL1Z has eight :adi:`ADAR1000s <adar1000>`, a minimum of two CSB lines are needed to have control over all the individual ICs. There are two CSB selector switches (S1, S2) which select the CSB line for the associated side of the board. Looking at the component side of the board, the left four :adi:`ADAR1000s <adar1000>` use the CSB line selected by S1 while the right four :adi:`ADAR1000s <adar1000>` use the CSB line selected by S2.

|CSB Selector Switches| **

.. container:: centeralign

   Figure 5: CSB Selector Switches


**

The ADAR1000-EVAL1Z alone demonstrates a small beamformer array, but multiple boards can also be stacked and combined to create larger arrays. In order to simplify the digital interface, two boards can be controlled using one digital controller if the two boards use all four of the available CSB lines without worrying about talking to the wrong IC.

--------------

EVALUATION
==========

Hardware Setup
--------------

Mechanical Parts
~~~~~~~~~~~~~~~~

-  1x ADAR1000-EVAL1Z board with heatsink already attached
-  2x Uprights with 16 screws attached (6 per leg for the ADAR1000-EVAL1Z board, 1 per leg for the feet)
-  2x Feet with angles installed

Mechanical Assembly
~~~~~~~~~~~~~~~~~~~

-  Using a **3/32 inch allen key**, connect the feet to the uprights using the **2 silver screws** already installed at the bottom of the upright. The screws should be snug, but don't need to be cranked down.
-  Using a **5/64 inch allen key**, connect the ADAR1000-EVAL1Z board to the uprights, one at a time using the **12 black screws** already installed in the uprights. The uprights are attached via the **front (component side)** of the ADAR1000-EVAL1Z board. The screws should be snug, but don't need to be cranked down.
-  The platform should now be fully assembled. Compare the result to the `assembly drawing <https://wiki.analog.com/_media/resources/eval/user-guides/stingray/stingray_assembly_v2.pdf>`__ to ensure proper assembly.

Test Setup Assembly
~~~~~~~~~~~~~~~~~~~

-  Follow the `Mechanical Assembly <https://wiki.analog.com/>`__ instructions.
-  Plug the included power supply into an outlet before connecting the power supply to P1 in the lower left-hand side of the board. Once finished, a red LED (D3) should be lit in the bottom-left corner of the board.
-  Connect your digital controller of choice to the appropriate connector (P3/P4 for PMOD control, P5 for :adi:`SDP-S` control).
-  Disable any test equipment of interest, and connect it to the ADAR1000-EVAL1Z board.

Board Power Control
-------------------

The ADAR1000-EVAL1Z board's power tree is controlled using two signals, **PWR_UP_DOWN** and **+5V_CTRL**. Due to the default settings of the :adi:`adar1000` on powerup, the :adi:`adtr1107` PAs need to be protected so as not to be destroyed when power is applied. The easiest way to control this is to power everything on the board except for the :adi:`ADTR1107s' <adtr1107>` +5V rail, initialize the :adi:`ADAR1000s <adar1000>` to put the :adi:`adtr1107` PAs into a safe state, and then power up the +5V rail.

Both **PWR_UP_DOWN** and **+5V_CTRL** are controlled with pulses, not logic levels, as they are inputs to flip-flops rather than enable signals directly.

Powerup Procedure
^^^^^^^^^^^^^^^^^

**1.** Apply +12V to either P1 or P2. Note the red LED (D3) on the bottom of the board. When lit, 12V is applied and the hot swap circuit is active. At this point, no RF rails are powered, but some miscellaneous rails are up:

-  +3.3V_INT (U8, :adi:`lt8606`)
-  +1.8V_INT (U9, :adi:`adp150`)
-  -6.0V_INT (U10, :adi:`ADP5074`)

**2.** Configure the LTC2992 by following the `CONFIGURING THE LTC2992 <https://wiki.analog.com/>`__ section below.

**3.** Pulse the **PWR_UP_DOWN** signal to sequence the first RF power rails. Once the power sequencer is finished, the ADAR1000s are fully powered up and the ADTR1107s are partially powered. This is indicated with an orange LED (D6).

-  +3.3V (U11, :adi:`lt8642s`)
-  -3.3V (U13, :adi:`lt3093`)
-  -5.0V (U14, :adi:`lt3094`)

|

.. note::

   The :adi:`adm1186` power sequencer's **enable** and **power_good** signals can be read using the on-board :adi:`ltc2992`. The **enable** signal is connected to GPIO1 and the **power_good** signal is connected to GPIO3.


   | **BE SURE TO CONFIGURE THE LTC2992 SUCH THAT ALL
   GPIO PINS ARE HI-Z! SEE** `CONFIGURING THE LTC2992 <https://wiki.analog.com/>`__


**4.** Initialize the ADAR1000s to put the ADAR1000-EVAL1Z into a known safe state with the ADTR1107 PAs pinched off. See the :doc:`Recommended ADAR1000 Initialization Sequences </wiki-migration/resources/eval/user-guides/stingray/userguide>` section for a recommended set of SPI writes.

**5.** Now that the ADTR1107 PAs are pinched off, +5V can safely be applied. This is accomplished by pulsing the **+5V_CTRL** signal. Once the +5V rail is up, a green LED (D4) is lit showing that the board is fully powered up.

-  +5.0V (U12, :adi:`lt8652S`)

.. note::

   The *internal* **+5V_CTRL** (after U3) and the :adi:`LT8652's <lt8652>` **power_good** signals can be read using the on-board :adi:`ltc2992`. The **+5V_CTRL** signal is connected to GPIO2 and the **power_good** signal is connected to GPIO4.

   
   |

   | **BE SURE TO CONFIGURE THE LTC2992 SUCH THAT ALL
   GPIO PINS ARE HI-Z! SEE** `CONFIGURING THE LTC2992 <https://wiki.analog.com/>`__


Powerdown Procedure
^^^^^^^^^^^^^^^^^^^

-  Pulse the **+5V_CTRL** signal to bring down the +5V power supply rail. The green LED will turn off indicating that the rail is down.
-  Pulse the **PWR_UP_DOWN** signal to tell the power sequencer to bring down the other RF rails in reverse order from powerup.

.. note::

   It is possible to only pulse **PWR_UP_DOWN** to turn off the board as disabling the power sequencer will also bring down the +5V rail. This is not recommended as it's safer to intentionally bring down +5V first, and will guarantee that any software controlling the board will not lose the current state.


Software Control
----------------

-  Follow the `Powerup Procedure <https://wiki.analog.com/>`__ to safely turn the board on.
-  At this point, the board is fully enabled, but all amplifiers are powered down. In order to pass signals, the board needs to be put into either Rx or Tx mode and the :adi:`adtr1107` amplifiers properly biased up. See the :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>` for information on how to do this.

RF Detector and ADC Combination
-------------------------------

There is an on-board RF detector/ADC combo which can be used to help calibrate the ADAR1000-EVAL1Z or measure test signals. The circuit is located on the antenna side of the board near the bottom.

The RF detector is the :adi:`hmc948` which feeds an :adi:`ada4807-1` unity gain buffer. The :adi:`ada4807-1` output then goes to the :adi:`LTC2314-14`. See the :adi:`LTC2314-14 Datasheet <media/en/technical-documentation/data-sheets/231414fa.pdf>` for information on retrieving data from the ADC.

The :adi:`hmc948` has approximately 54dB of dynamic range at 10GHz centered at -24dBm.

--------------

Recommended ADAR1000 Initialization Sequences
=============================================

.. note::

   The below sequences don't take into account the different hardware addresses of the various ADAR1000s. Consult the :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>` for more information on the hardware addressing.


.. note::

   The below sequences don't take into account the issues described in the :doc:`ADAR1000 Silicon & Datasheet Errata </wiki-migration/resources/errata/adar1000>`. Consult these documents for more information about how to properly communicate with all parts on the board.


.. note::

   The below sequences don't account for the fact that the Stingray uses two CSB lines to address all of the ADAR1000s on the board. In order to configure all chips, the sequences must be run on each required CSB line individually.


Initial Powerup
---------------

.. code:: python

   """
   This sequence is suggested to be run after powering the +3.3V, -3.3V, and -5.0V rails on the Stingray board, 
   but before powering the +5.0V rail. This will help protect the ADTR1107 PAs. It will put the chips into a 
   known safe state on powerup.
       Format: (Register, Data, Description)
   """
   INIT_SEQUENCE = [
       # HOUSEKEEPING
       (0x000, 0x81, 'Reset'),
       (0x401, 0x02, 'Allow LDO adjustments from user settings'),
       (0x400, 0x55, 'Adjust LDO Settings'),
       (0x038, 0x60, 'Bypass the beam and bias RAM (enable SPI)'),
       (0x02E, 0x7F, 'Enable all Rx channels, LNA, VGA, Vector Mod'),
       (0x02F, 0x7F, 'Enable all Tx channels, PA, VGA, Vector Mod'),
       (0x034, 0x08, 'Set LNA preamplifier to nominal bias'),
       (0x035, 0x55, 'Set Rx VGA and Vector Mod to nominal bias'),
       (0x036, 0x2D, 'Set Tx VGA and Vector Mod to nominal bias'),
       (0x037, 0x06, 'Set Tx PA preamplifier to nominal bias'),

       # PA BIAS VALUES
       (0x029, 0x85, 'Set PA1_BIAS_ON value (≈ -2.5V)'),
       (0x02A, 0x85, 'Set PA2_BIAS_ON value (≈ -2.5V)'),
       (0x02B, 0x85, 'Set PA3_BIAS_ON value (≈ -2.5V)'),
       (0x02C, 0x85, 'Set PA4_BIAS_ON value (≈ -2.5V)'),
       (0x046, 0x85, 'Set PA1_BIAS_OFF value (≈ -2.5V)'),
       (0x047, 0x85, 'Set PA2_BIAS_OFF value (≈ -2.5V)'),
       (0x048, 0x85, 'Set PA3_BIAS_OFF value (≈ -2.5V)'),
       (0x049, 0x85, 'Set PA4_BIAS_OFF value (≈ -2.5V)'),

       # LNA BIAS VALUES
       (0x02D, 0x68, 'Set LNA_BIAS_ON value (≈ -2.0V)'),
       (0x04A, 0x68, 'Set LNA_BIAS_OFF value (≈ -2.0V)'),

       # TR CONTROL STATE
       (0x031, 0x90, 'Disable Tx/Rx using SPI TR control'),

       # Enable PA/LNA DACs
       (0x030, 0x50, 'Enable the PA and LNA output DACs'),
   ]

Max Gain & 0° Phase
-------------------

.. code:: python

   """
   Sequence to set all ADAR1000 channels to maximum gain and 0° phase.
       Format: (Register, Data, Description)
   """
   CHANNEL_SETUP = [
       # Rx GAIN
       (0x010, 0xFF, 'Set channel 1 Rx to maximum gain'),
       (0x011, 0xFF, 'Set channel 2 Rx to maximum gain'),
       (0x012, 0xFF, 'Set channel 3 Rx to maximum gain'),
       (0x013, 0xFF, 'Set channel 4 Rx to maximum gain'),
       
       # Rx PHASE
       (0x014, 0x3F, 'Set channel 1 Rx I Vector Modulator to 0°'),
       (0x015, 0x20, 'Set channel 1 Rx Q Vector Modulator to 0°'),
       (0x016, 0x3F, 'Set channel 2 Rx I Vector Modulator to 0°'),
       (0x017, 0x20, 'Set channel 2 Rx Q Vector Modulator to 0°'),
       (0x018, 0x3F, 'Set channel 3 Rx I Vector Modulator to 0°'),
       (0x019, 0x20, 'Set channel 3 Rx Q Vector Modulator to 0°'),
       (0x01A, 0x3F, 'Set channel 4 Rx I Vector Modulator to 0°'),
       (0x01B, 0x20, 'Set channel 4 Rx Q Vector Modulator to 0°'),
       
       # Tx GAIN
       (0x01C, 0xFF, 'Set channel 1 Tx to maximum gain'),
       (0x01D, 0xFF, 'Set channel 2 Tx to maximum gain'),
       (0x01E, 0xFF, 'Set channel 3 Tx to maximum gain'),
       (0x01F, 0xFF, 'Set channel 4 Tx to maximum gain'),
       
       # Tx PHASE
       (0x020, 0x3F, 'Set channel 1 Tx I Vector Modulator to 0°'),
       (0x021, 0x20, 'Set channel 1 Tx Q Vector Modulator to 0°'),
       (0x022, 0x3F, 'Set channel 2 Tx I Vector Modulator to 0°'),
       (0x023, 0x20, 'Set channel 2 Tx Q Vector Modulator to 0°'),
       (0x024, 0x3F, 'Set channel 3 Tx I Vector Modulator to 0°'),
       (0x025, 0x20, 'Set channel 3 Tx Q Vector Modulator to 0°'),
       (0x026, 0x3F, 'Set channel 4 Tx I Vector Modulator to 0°'),
       (0x027, 0x20, 'Set channel 4 Tx Q Vector Modulator to 0°')
   ]

Disable
-------

.. code:: python

   """
   This sequence will disable the ADAR1000 and put the chip into a low power state.
       Format: (Register, Data, Description)
   """
   DISABLE = [
       (0x029, 0x85, 'Set CH1 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02A, 0x85, 'Set CH2 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02B, 0x85, 'Set CH3 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02C, 0x85, 'Set CH4 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02D, 0x68, 'Set LNA_BIAS_ON to minimal power (≈ -2.0V)'),
       (0x030, 0x50, 'Enable the LNA bias DAC output'),
       (0x031, 0x90, 'Put ADAR1000 into SPI-controlled TR state and disable TX_EN/RX_EN bits')
   ]

Rx Enable
---------

.. code:: python

   """
   This sequence will configure the ADAR1000 for Rx and set the LNAs to full power.
   Be sure you know what you're doing!
       Format: (Register, Data, Description)
   """
   RX_SETUP = [
       (0x030, 0x40, 'Disable the LNA bias DAC output to allow the ADTR1107 LNAs to self-bias'),
       (0x031, 0xB0, 'Put ADAR1000 into SPI-controlled Rx mode')
   ]

Tx Enable (Reduced Power)
-------------------------

.. code:: python

   """
   This sequence will configure the ADAR1000 for Tx and set the PAs to a reduced power state.
   Be sure you know what you're doing!
       Format: (Register, Data, Description)
   """
   TX_SETUP_REDUCED_POWER = [
       (0x029, 0x42, 'Set CH1 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02A, 0x42, 'Set CH2 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02B, 0x42, 'Set CH3 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02C, 0x42, 'Set CH4 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x031, 0xD2, 'Put ADAR1000 into SPI-controlled Tx mode')
   ]

Tx Enable
---------

.. code:: python

   """
   This sequence will configure the ADAR1000 for Tx and set the PAs to full power.
   Be sure you know what you're doing!
       Format: (Register, Data, Description)
   """
   TX_SETUP = [
       (0x029, 0x38, 'Set CH1 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02A, 0x38, 'Set CH2 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02B, 0x38, 'Set CH3 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02C, 0x38, 'Set CH4 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x031, 0xD2, 'Put ADAR1000 into SPI-controlled Tx mode')
   ]

--------------

Configuring the LTC2992
=======================

| On powerup, the LTC2992 is configured with GPIO3 held low. To properly power the Stingray board, this pin needs to be set to Hi-Z. Complete the below I2C writes to ensure that all GPIO pins are set to Hi-Z:

.. note::

   The LTC2992's I2C 7-bit address is 0x6A, its 8-bit address is 0xD4.

   
   Looking at the schematic for the board, it would seem that the address pins are pulled down (resulting in the address being 0x6F according to Table 3 of the :adi:`LTC2992 datasheet <media/en/technical-documentation/data-sheets/ltc2992.pdf>`), but the 100kΩ resistors are too weak to overcome the internal circuitry of the LTC2992, so the actual address is 0x6A.


.. note::

   The LTC2992 requires repeated START conditions for readback.


.. code:: python

   """
   This sequence will set the LTC2992's GPIO pins to Hi-Z.
       Format: (Register, Data, Description)
   """
   LTC2992_SETUP = [
       (0x96, 0x00, 'Set GPIO1-GPIO3 pins to Hi-Z'),
       (0x97, 0x00, 'Set GPIO4 pin to Hi-Z')
   ]

--------------

Stingray Board Cell & Channel Maps
==================================

Cell Map
--------

|ADAR1000-EVAL1Z Cell Mapping|

.. container:: centeralign

   \ **Figure 6: ADAR1000-EVAL1Z Cell Mapping**\


Channel Map
-----------

|ADAR1000-EVAL1Z Channel Mapping|

.. container:: centeralign

   \ **Figure 7: ADAR1000-EVAL1Z Channel Mapping**\


Channel Map (Back of Board)
---------------------------

|ADAR1000-EVAL1Z Channel Mapping (Back of Board)|

.. container:: centeralign

   \ **Figure 8: ADAR1000-EVAL1Z Channel Mapping (Back of Board)**\


Support
-------

For additional questions or support, please visit the Engineering Zone forum at :ez:`q-a <adef-system-platforms/f/q-a>`.

:doc:`ADAR1000EVAL1Z Homepage </wiki-migration/resources/eval/user-guides/stingray>`

:doc:`X Band Development Platform </wiki-migration/resources/eval/user-guides/x-band-platform>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/adar1000eval1z_bottom-web.gif
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/adar1000eval1z_top-web.gif
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/adar1000eval1z_top_kit.jpg
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/adar1000eval1z_bottom_kit-web.jpg
   :width: 200px
.. |ADAR1000-EVAL1Z Component Side Overview| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/component_side_overview.png
   :width: 1300px
.. |ADAR1000-EVAL1Z Antenna Side Overview| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/antenna_side_overview.png
   :width: 800px
.. |PMOD Pinout| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/pmod_pinout.png
   :width: 600px
.. |CSB Selector Switches| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/csb_selectors.jpg
.. |ADAR1000-EVAL1Z Cell Mapping| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/cell_mapping.png
.. |ADAR1000-EVAL1Z Channel Mapping| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/channel_mapping.png
.. |ADAR1000-EVAL1Z Channel Mapping (Back of Board)| image:: https://wiki.analog.com/_media/resources/eval/user-guides/stingray/channel_mapping_reverse.png
