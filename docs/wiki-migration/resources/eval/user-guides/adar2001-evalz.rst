EVALUATING THE ADAR2001 4-CHANNEL 4x FREQUENCY MULTIPLIER/FILTER
================================================================

GENERAL DESCRIPTION
===================

The ADAR2001-EVALZ evaluation board is designed for testing the performance of the :adi:`adar2001`. The :adi:`adar2001` is a 4-channel 4x Frequency Multiplier/Filter designed for mmWave security imaging applications. All RF input/outputs are brought out to 2.92mm (K) coaxial connectors. On-board logic level translators convert between the external logic level and the on-chip level of 1.8V.

There is an :adi:`Analog Devices System Demonstration Platform (SDP) <SDP>` connector which can be used in conjunction with an :adi:`SDP` controller board to manipulate the internal registers as well as cycle through the programmed modes of the two internal state machines.

The :adi:`adar2001` has two integrated state machines, one for the Multiplier section and another for the Transmitter section. The sequencers are configured through the SPI, and can be used to quickly cycle through pre-programmed states. These sequencers can be exercised in one of two ways:

-  External Advance and Reset Pins:

   -  TxADV - Transmitter Advance (Pin 8)
   -  TxRST - Transmitter Reset (Pin 9)
   -  MADV - Multiplier Advance (Pin 10)
   -  MRST - Multiplier Reset (Pin 11)

-  SPI writes to the SEQUENCER_CTRL_SPI register (0x44)

| 
| |ADAR2001-EVALZ Board|

.. container:: centeralign

   \ **Figure 1: ADAR2001-EVALZ Board**\


--------------

RELATED PARTS
=============

ADAR2004: 10GHz to 40GHz 4-Channel Rx Mixer With 4x LO
------------------------------------------------------

-  :adi:`ADAR2004 Product page <adar2004>`
-  :doc:`ADAR2004-EVALZ Wiki </wiki-migration/resources/eval/user-guides/adar2004-evalz>`

AD9083: 16-Channel, 100MHz Bandwidth, JESD204B Analog-to-Digital Converter
--------------------------------------------------------------------------

-  :adi:`AD9083 Product page <ad9083>`

ADF5610: Microwave Wideband Synthesizer with Integrated VCO
-----------------------------------------------------------

-  :adi:`ADF5610 Product page <adf5610>`

--------------

REQUIREMENTS
============

Equipment
~~~~~~~~~

-  ADAR2001-EVALZ Evaluation Board
-  PC running Windows XP or higher
-  :adi:`SDP-S` USB interface board
-  Network Analyzer ≥ 40GHz
-  Spectrum Analyzer ≥ 40GHz
-  Signal Generator ≥ 10GHz
-  Power Supply: 2.5V, ≥ 1A

Documents
~~~~~~~~~

-  :adi:`ADAR2001 Datasheet <media/en/technical-documentation/data-sheets/ADAR2001.pdf>`
-  `ADAR2001-EVALZ Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/02_048668d_top.pdf>`__
-  `ADAR2001-EVALZ Layout File <https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/08_048668d.zip>`__
-  `ADAR2001-EVALZ Gerbers <https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/adar2001_fab.zip>`__

Software
~~~~~~~~

-  :adi:`Analog Devices, Inc., Analysis \| Control \| Evaluation (ACE) <ace>`

--------------

EVALUATION BOARD HARDWARE
=========================

`Figure 1 <https://wiki.analog.com/>`__ shows the ADAR2001-EVALZ evaluation board, with 8 RF connectors for the four transmitter outputs and 1 RF connector for the multiplier input. A single BNC connector is provided to apply the required 2.5V power supply. An :adi:`SDP` connector is also included to interface with a USB port on a Windows based PC. The ADAR2001-EVALZ board requires the use of an :adi:`SDP-S` or :adi:`SDP-B` board along with the ACE software to program the device. :adi:`ace` is available for download at :adi:`www.analog.com/ace <ace>` The :adi:`SDP` control boards are not included with the evaluation board and must be purchased separately. These boards can be ordered through local Analog Devices distributors as well as from :adi:`www.analog.com/sdp <sdp>`. The RF and digital interfaces for the ADAR2001-EVALZ are shown in `Figure 2 <https://wiki.analog.com/>`__.

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The ADAR2001-EVALZ board must be powered from an external power supply with a voltage level of 2.5V. This power supply must have a current capability of at least 1A.

There is an on-board LDO (U105) which generates the 1.8V required to safely drive the digital pins of the :adi:`adar2001`. This supply has an associated jumper, JP1, which can be used to enable and disable the 1.8V supply.

RF Input and Output Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The ADAR2001-EVALZ board has 11 edge-mounted and 2 vertical RF connectors which are described in Table 1.
| **Table 1: RF Connectors**

+--------------+------------------+-------------+------------+----------------------------------+
| Connector(s) | Name(s)          | Orientation | Series     | Description                      |
+==============+==================+=============+============+==================================+
| J1, J2       | RFOUT1+, RFOUT1- | Edge-launch | 2.92mm (K) | Channel 1 Differential RF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J3, J4       | RFOUT2+, RFOUT2- | Edge-launch | 2.92mm (K) | Channel 2 Differential RF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J5, J6       | RFOUT3-, RFOUT3+ | Edge-launch | 2.92mm (K) | Channel 3 Differential RF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J7, J8       | RFOUT4-, RFOUT4+ | Edge-launch | 2.92mm (K) | Channel 4 Differential RF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J9           | RFIN             | Edge-launch | 2.92mm (K) | Single-ended RF Input            |
+--------------+------------------+-------------+------------+----------------------------------+
| J11          | MADV             | Vertical    | SMA        | Multiplier Advance               |
+--------------+------------------+-------------+------------+----------------------------------+
| J12          | TxADV            | Vertical    | SMA        | Transmitter Advance              |
+--------------+------------------+-------------+------------+----------------------------------+
| J13, J14     | RF THRU-CAL      | Edge-launch | 2.92mm (K) | Thru-cal                         |
+--------------+------------------+-------------+------------+----------------------------------+

|image1| **

.. container:: centeralign

   Figure 2: ADAR2001-EVALZ Connections


**

Digital Signals
~~~~~~~~~~~~~~~

The :adi:`sdp` board operates with logic levels of 3.3V, while the :adi:`adar2001` requires logic levels of 1.8V. To protect the :adi:`adar2001`, level translators (U102, U103, U104) have been included between the :adi:`sdp` connector and the rest of the board. If digital signals are applied using any method below other than the :adi:`sdp` connector, the applied logic levels must be set to 1.8V. Violating this could stress the :adi:`adar2001` beyond it’s designed limits and could result in permanent damage to the part. The level translator ICs have two separate supply voltages, one per side, which are used to set the logic level for that side of the translator. The :adi:`sdp` side voltage level is 3.3V and is taken directly from the :adi:`sdp` interface board. The :adi:`adar2001` side voltage level is 1.8V and is taken from the on-board LDO, U105. To use this :adi:`sdp` interface, the 1.8V rail must be enabled using jumper JP1.

SPI Control
^^^^^^^^^^^

The ADAR2001-EVALZ board SPI interface is meant to be driven using the :adi:`sdp` connector, P101, however, test points are also provided as an alternative. The test points are labelled with the SPI signal names (SCLK, SDIO, CSB, SDO).

The test point signals are not routed through level translators to protect the :adi:`adar2001` in case of an overvoltage scenario. Therefore, if these test points are used to drive the SPI, the input logic level must be set to 1.8V. This was done to provide a simple interface which isn’t limited in speed by the translator devices.

State Machine Control
^^^^^^^^^^^^^^^^^^^^^

The ADAR2001-EVALZ board has multiple interfaces for driving the :adi:`adar2001`\ ’s internal state machines. The :adi:`sdp` controller board can activate these lines both through the SPI interface, or through the GPIO pins on the :adi:`sdp` connector, P101. Test points are also provided as an alternative and are labelled with the signal names (MRST, TxRST, MADV, TxADV). The reset lines (MRST, TxRST) also have pushbuttons (S1, S2) that can be used to reset the sequencers by hand. The advance lines (MADV, TxADV) also have surface mount SMA connectors (J11, J12) to provide the highest speed interface for cycling through the sequencer states.

Only the signals in/out of the :adi:`sdp` connector are routed through the level translation circuitry. Therefore, if either the test points or SMA connectors are used to drive the sequencer control lines, the input logic level must be set to 1.8V.

| Also, if the SMA connectors are used to drive the sequencers at high speed, it’s best practice to terminate the signal lines in 50Ω using resistors R114 and R115. By default, these resistors are not installed.

--------------

EVALUATION AND TEST PROCEDURES
==============================

Hardware Setup
~~~~~~~~~~~~~~

|image2| **

.. container:: centeralign

   Figure 3: Typical ADAR2001-EVALZ setup for RF measurements


**

`Figure 3 <https://wiki.analog.com/>`__ shows a typical test setup for RF measurements using a spectrum analyzer. Note that any loss in the test setup needs to be calibrated out for the most accurate measurements. The procedure for building this test setup is outlined below:

-  Connect the power supply to J10. Leave the supply disabled.
-  Connect the RF signal generator to J9. Leave the generator output disabled.
-  Connect the spectrum analyzer to any RF output connector (J1-J8). Note that it is best practice to differentially test the :adi:`adar2001` using a balun or hybrid coupler, but it isn't required. If testing single-ended, be sure to terminate the unused output in 50Ω.
-  Set the power supply to deliver a 2.5V rail with a current limit of 500mA.
-  Check that JP1 is in position to enable the 1.8V digital supply voltage.
-  Set the RF signal generator to provide an input signal at 4.75GHz with a power level of -20dBm.
-  Turn on the power supply and RF signal generator.

Test Setup Loss Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The loss of the test setup must be removed for accurate data to be taken. The included thru-cal has a trace that is twice the length of the RF output traces and includes two RF connectors. Therefore, the approximate loss of the evaluation board’s RF output traces can be removed by measuring the thru-cal and dividing the loss by two.

Any external components (balun, combiner, RF cabling, attenuator pads, etc.) should also be calibrated out of the system.

Software Initialization
~~~~~~~~~~~~~~~~~~~~~~~

|image3| **

.. container:: centeralign

   Figure 4: Access the** :adi:`adar2001` **Plugin from ACE


**

-  Download and install :adi:`ace` by following the instructions in the `ACE user manual <http://swdownloads.analog.com/ACE/ACE_User_Manual_rev3.pdf>`__.
-  Connect the :adi:`sdp` controller board to both the PC and the ADAR2001-EVALZ.
-  Open :adi:`ace` and connect to the board by double-clicking on the ":adi:`adar2001` Board" plugin in the "Attached Hardware" section of the Start page. See `Figure 4 <https://wiki.analog.com/>`__.

|image4| **

.. container:: centeralign

   Figure 5:** :adi:`adar2001` **Main GUI Overview


**

Mutliplier Block Setup
~~~~~~~~~~~~~~~~~~~~~~

| The Multiplier block is designed to take a CW input between 2.5GHz to 10GHz, multiply the frequency by 4, and set the power level. This block also contains bandpass filters with a programmable corner frequency before the Transmitter block and lowpass/notch filters after the Transmitter block. To accomplish this, the Multiplier block has 3 parallel signal paths, each of which is designed to handle a portion of the total frequency band. To ensure that the highest quality signal is fed to the Transmitter block, the correct multiplier band must be selected for the frequency of interest and the bandpass filter must be set to the appropriate corner for the frequency range of interest. See Table 2 for a breakdown of the multiplier bands with respect to frequency.
| **Table 2: Multiplier/Filter settings for optimal harmonic rejection**

+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| Input (GHz)   | Output (GHz) | Multiplier Band                              | BPF  | ATTN | LPF/Notch | MULT_EN_x Register Value | MULT_PASS_x Register Value |
+===============+==============+==============================================+======+======+===========+==========================+============================+
| 2.50 to 3.00  | 10 to 12     | Low Band Active *(Mid and High Bands Ready)* | LOW  | 0x13 | ON        | 0x7A                     | 0xD3                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 3.00 to 3.50  | 12 to 14     | Low Band Active *(Mid and High Bands Ready)* | HIGH | 0x07 | ON        | 0x7A                     | 0x47                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 3.50 to 4.00  | 14 to 16     | Low Band Active *(Mid and High Bands Ready)* | HIGH | 0x13 | ON        | 0x7A                     | 0x53                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 4.00 to 5.00  | 16 to 20     | Mid Band Active *(Low and High Bands Ready)* | LOW  | 0x1F | OFF       | 0x6E                     | 0x9F                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 5.00 to 6.25  | 20 to 25     | Mid Band Active *(Low and High Bands Ready)* | HIGH | 0x1F | OFF       | 0x6E                     | 0x1F                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 6.25 to 8.00  | 25 to 32     | High Band Active *(Low and Mid Bands Ready)* | LOW  | 0x1F | OFF       | 0x6B                     | 0x9F                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+
| 8.00 to 10.00 | 32 to 40     | High Band Active *(Low and Mid Bands Ready)* | HIGH | 0x1F | OFF       | 0x6B                     | 0x1F                       |
+---------------+--------------+----------------------------------------------+------+------+-----------+--------------------------+----------------------------+

Follow the below steps to configure the Multiplier block for an input signal of 4.75GHz (Tx signal of 19GHz):

-  If the recommended bias conditions aren't sufficient, choose bias points from the dropdowns for the RF input buffer stages. Click on the amplifier itself to enable the buffer. The buffer will change from grey to blue.
-  If the recommended bias condition isn't sufficient, choose a bias point from the dropdown for the Mid-Band multiplier/amplifier. Check the “Active” box next to the multiplier/amplifier. This will enable the circuit and change the input/output switches to the middle setting. The “Ready” checkbox should automatically be checked as well. The Mid-Band amplifier will change from grey to blue.
-  Be sure that the box setting the bandpass filters to their low corners is **not** checked.
-  Check the box enabling the notch filters after the Tx Power Amplifiers.
-  Choose the desired attenuation setting from the dropdown.
-  Click “Apply Changes” at the top-left of the page to write all the new settings to the part.

Transmitter Block Setup
~~~~~~~~~~~~~~~~~~~~~~~

The Transmitter block is designed to take a CW signal from the Multiplier block, split it to one of 4 channels, and amplify the signal to a power level appropriate for transmission towards a target. To accomplish this, the Transmitter block contains 2 stages of active splitters and 4 Power Amplifiers (PAs). It should be noted that only one channel is intended to be operating at any one time.

Follow the below steps to configure the Transmitter block to output the 19GHz signal from the Multiplier block on Channel 3:

-  If the recommended bias condition isn't sufficient, choose a bias point for the first active splitter. Click on the splitter to enable it. The splitter will change from grey to blue.
-  If the recommended bias condition isn't sufficient, choose a bias point for the second set of active splitters. Click on the splitter leading to Channels 3 and 4 to enable it. The splitter will change from grey to blue.
-  If the recommended bias condition isn't sufficient, choose a bias point for the PAs. Check the “Active” box next to Channel 3. This PA will change from grey to blue and the “Ready” checkbox will be enabled as well.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Sequencer Programming
~~~~~~~~~~~~~~~~~~~~~

The two built-in state machines can be used to quickly change the operating state of the :adi:`adar2001` without having to perform multiple fast SPI writes.

There are default modes already written to the control registers to facilitate easy testing of the :adi:`adar2001`\ ’s functions, but the modes and states are fully configurable to allow for any valid conditions to be tested.

“Modes” refer to the configuration of the :adi:`adar2001`, while “States” refer to the order in which the modes will be cycled through when using the two state machines.

To view the current Mode or State settings, first go to a sequencer programming tab at the top of the screen the two sub-blocks are labelled “Multiplier Block” and “Tx Block”. Choose a view type from the “Current View” box. The top checkbox will show the settings for the Modes. The middle checkbox will show the settings for the States. The bottom checkbox will show the settings from the current configuration. With the sequencer disabled, the “manual” settings will be shown. These are loaded from the SPI mode registers (0x45-0x48) With the sequencer enabled, the settings from the current index in the state machine will be shown. See “VIEW TYPE” in `Figure 6 <https://wiki.analog.com/>`__ and `Figure 8 <https://wiki.analog.com/>`__.

Multiplier/Filter Mode Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image5| **

.. container:: centeralign

   Figure 6: Multiplier/Filter sequencer configuration page


**

To change any of the pre-programmed Multiplier/Filter Sequencer modes, follow the below steps:

-  Switch the view to the tab named "Multiplier Block."
-  Change the various settings in the block diagram to configure the mode as desired. This block operates in the same manner as the settings on the main page. The only difference is that there aren’t any available settings for the bias points of the various parts of the chip. The bias settings are globally set on the main page and cannot be changed using the state machine.
-  Once the configuration is satisfactory, choose which mode to apply the settings to using the left-hand dropdown, and click “Apply Visible Settings to Mode”. See “RECONFIGURE MODE” in `Figure 6 <https://wiki.analog.com/>`__.
-  Repeat this process to configure all the modes of interest.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Multiplier/Filter State Order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the modes have been configured, they must be linked to the states for the sequencer to cycle through.

To change the order and/or depth of the state machine, follow the below steps:

-  Change the depth of the state machine by using the labelled dropdown. See "STATE MACHINE DEPTH" in `Figure 6 <https://wiki.analog.com/>`__. Note that this number indicates the total number of states in use, n. The reset state isn't included, which is why Mode 0 is always linked to the reset state. `Figure 7 <https://wiki.analog.com/>`__ shows how the state machine pointer moves with Advance and Reset pulses.


|num_mult_states.png|

   |image6|

**

.. container:: centeralign

   Figure 7: Multiplier/Filter State machine pointer diagram


**

-  To set the order of the states, choose a mode from the middle Mode dropdown to apply to a state. Choose a state from the middle State dropdown. The current setting of that state will appear in the text on the right. Click the button labelled “Apply Selected Mode to State”, and the readout will update to reflect the change. See “RECONFIGURE STATE” in `Figure 6 <https://wiki.analog.com/>`__.
-  Repeat the process until all the desired states are set.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Transmitter Mode Settings
^^^^^^^^^^^^^^^^^^^^^^^^^

|image7| **

.. container:: centeralign

   Figure 8: Transmitter sequencer configuration page


**

To change any of the pre-programmed Transmitter Sequencer modes, follow the below steps:

-  Switch the view to the tab names "Tx Block."
-  Change the various settings in the block diagram to configure the mode as desired. This block operates in the same manner as the settings on the main page. The only difference is that there aren’t any available settings for the bias points of the various parts of the chip. The bias settings are globally set on the main page and cannot be changed using the state machine.
-  Once the configuration is satisfactory, choose which mode to apply the settings to using the left-hand dropdown, and click “Apply Visible Settings to Mode”. See “RECONFIGURE MODE” in `Figure 8 <https://wiki.analog.com/>`__.
-  Repeat this process to configure all the modes of interest.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Transmitter State Order
^^^^^^^^^^^^^^^^^^^^^^^

Once the modes have been configured, they must be linked to the states for the sequencer to cycle through.

To change the order and/or depth of the state machine, follow the below steps:

-  Change the depth of the state machine by using the labelled dropdown. See “STATE MACHINE DEPTH” in `Figure 8 <https://wiki.analog.com/>`__. Note that this number indicates the total number of states in use, n, not including the reset state which is always linked to Mode 0. See `Figure 9 <https://wiki.analog.com/>`__ for a diagram of the state machine indexing.


|num_tx_states.png|

   |image8|

**

.. container:: centeralign

   Figure 9: Transmitter State machine pointer diagram


**

-  To set the order of the states, choose a mode from the middle Mode dropdown to apply to a state. Choose a state from the middle State dropdown. The current setting of that state will appear in the text on the right. Click the button labelled “Apply Selected Mode to State”, and the readout will update to reflect the change. See “RECONFIGURE STATE” in `Figure 8 <https://wiki.analog.com/>`__.
-  Repeat the process until all the desired states are set.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Sequencer Control
^^^^^^^^^^^^^^^^^

The Multiplier/Filter and Transmitter sequencers must be enabled before they can control the configuration of the associated :adi:`adar2001` blocks. To enable the state machines, the checkboxes in the “STATE MACHINE CONTROL” section of the main page must be checked. See `Figure 5 <https://wiki.analog.com/>`__. These checkboxes are also available in the "STATE MACHINE CONTROL" sections of the individual sequencer tabs. See `Figure 6 <https://wiki.analog.com/>`__ and `Figure 8 <https://wiki.analog.com/>`__.

When the state machines are enabled, the lights at the top of the control box will show in green. Also, the top-left section of each sequencer block on the main page will change to show that the state machine is controlling the block, rather than the SPI.

Once the state machines are enabled, the latching style must be selected. By default, when a pin is pulsed, the upcoming state is loaded into memory on the rising edge of the pulse and is latched out to the individual blocks as quickly as possible. This is necessary to allow direct SPI control of the blocks, but may require special consideration for timing. See the datasheet for details. If latching is enabled, the commands aren't sent out to the blocks until the falling edge of the pulse. This helps to align all the chip changes so that they happen at once.

Because the latch is the last check before the data is sent to the various internal blocks, when using the :adi:`adar2001` in “manual” or SPI mode, the latching must be disabled for both sequencers. If this isn’t done, the blocks will never receive the new instructions unless the external sequencer pins are pulsed. This would be uncommon since the sequencers are disabled in this mode of operation.

When the sequencers are enabled, the state machine pointers can be moved using the buttons at the bottom of the State Machine Control section. The labelled MADV, MRST, TxADV, TxRST will directly pulse the associated pin on the :adi:`adar2001`. If necessary, it’s possible to advance or reset both sequencers simultaneously by using the respectively labelled buttons.

When enabled, the State Machine Control section will also reflect the current State and Mode for each sequencer.

ADC Block
~~~~~~~~~

The :adi:`adar2001` has an 8 bit on-chip ADC with a 5-position multiplexer at the input. The multiplexer is used to direct the desired signal to the ADC for measurement. The multiplexer connects to the output of 4 power detectors (one for each RF output channel) as well as a temperature diode. Follow the below steps to enable the ADC for reading:

-  Be sure that the chip’s power bit is enabled at the top left of the main page.
-  Turn on the ADC’s power bit by clicking it. The ADC will change color from grey to blue.
-  Enable the internal ADC clock by clicking it. The clock will change from grey to blue.
-  Choose a clock frequency from the dropdown menu.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Channel Power Detection
^^^^^^^^^^^^^^^^^^^^^^^

Once the ADC section has been enabled and configured, the on-chip power detectors can be used to determine the output power for each channel. Follow the below steps:

-  Enable the desired detector by clicking it. The diode symbol will change from grey to blue.
-  Click the switch to change the selected input to the detector of choice (positions 1 – 4).
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.
-  Click the “Measure ADC” button. A power reading will appear in the box below the button.

Temperature Sensor
^^^^^^^^^^^^^^^^^^

Once the ADC section has been enabled and configured, the on-chip temperature sensor can be used to determine the junction temperature of the :adi:`adar2001`. Follow the below steps:

-  Click the switch to change the selected input to the temperature sensor (position 0).
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.
-  Click the “Measure ADC” button. A temperature reading will appear in the box below the button.

.. |ADAR2001-EVALZ Board| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/1_adar2001_board.png
   :width: 500px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/2_adar2001_connections.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/3_adar2001_setup.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/4_adar2001_access_ace_plugin.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/5_adar2001_main_gui_overview.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/6_multiplier_sequencer_configuration.png
.. |num_mult_states.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/num_mult_states.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/7_state_machine_loop.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/8_transmitter_sequencer_configuration.png
.. |num_tx_states.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/num_tx_states.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2001/7_state_machine_loop.png
   :width: 400px
