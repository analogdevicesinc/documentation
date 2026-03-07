EVALUATING THE ADAR2004 10GHz to 40GHz 4-CHANNEL Rx MIXER WITH 4x LO
====================================================================

GENERAL DESCRIPTION
===================

The ADAR2004-EVALZ evaluation board is designed for testing the performance of the :adi:`adar2004`. The :adi:`adar2004` is a 10GHz to 40GHz 4-channel Rx Mixer with an integrated 4x multiplier on the LO input port and is designed for mmWave security imaging applications. All RF inputs are brought out to 2.92mm (K) coaxial connectors while the IF outputs are delivered using SMA connectors. On-board logic level translators convert between the external logic level and the on-chip level of 1.8V.

There is an :adi:`Analog Devices System Demonstration Platform (SDP) <SDP>` connector which can be used in conjunction with an :adi:`SDP` controller board to manipulate the internal registers as well as cycle through the programmed modes of the two internal state machines.

The :adi:`adar2004` has two integrated state machines, one for the LO Multiplier section and another for the Receiver section. The sequencers are configured through the SPI, and can be used to quickly cycle through pre-programmed states. These sequencers can be exercised in one of two ways:

-  External Advance and Reset Pins:

   -  RxRST - Receiver Reset (Pin 29)

      -  RxADV - Receiver Advance (Pin 30)
      -  MRST - Multiplier Reset (Pin 31)
      -  MADV - Multiplier Advance (Pin 32)

-  SPI writes to the SEQUENCER_CTRL_SPI register (0x2A)

| 
| |image1|

.. container:: centeralign

   \ **Figure 1: ADAR2004-EVALZ Board**\


--------------

RELATED PARTS
=============

ADAR2001: 4-Channel 4x Frequency Multiplier/Filter
--------------------------------------------------

-  :adi:`ADAR2001 Product page <adar2001>`
-  :doc:`ADAR2001-EVALZ Wiki </wiki-migration/resources/eval/user-guides/adar2001-evalz>`

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
---------

-  ADAR2004-EVALZ Evaluation Board
-  PC running Windows XP or higher
-  :adi:`SDP-S` USB interface board
-  Network Analyzer ≥ 40GHz
-  Spectrum Analyzer ≥ 40GHz
-  LO Signal Generator ≥ 2.5GHz
-  RF Signal Generator ≥ 10GHz
-  Power Supply: 2.5V, ≥ 1A

Documents
---------

-  :adi:`ADAR2004 Datasheet <media/en/technical-documentation/data-sheets/ADAR2004.pdf>`
-  `ADAR2004-EVALZ Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/02_048685d_top.pdf>`_
-  `ADAR2004-EVALZ Layout File <https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/08_048685d.zip>`_
-  `ADAR2004-EVALZ Gerbers <https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/adar2004_fab.zip>`_

Software
--------

-  :adi:`Analog Devices, Inc., Analysis \| Control \| Evaluation (ACE) <ace>`

--------------

EVALUATION BOARD HARDWARE
=========================

`Figure 1 <https://wiki.analog.com/>`_ shows the ADAR2004-EVALZ evaluation board, with 8 RF connectors for the four receiver inputs, 1 RF connector for the LO input, and 8 SMA connectors for the four differential IF outputs. A single BNC connector is provided to apply the required 2.5V power supply. An :adi:`SDP` connector is also included to interface with a USB port on a Windows based PC. The ADAR2004-EVALZ board requires the use of an :adi:`SDP-S` or :adi:`SDP-B` board along with the ACE software to program the device. :adi:`ace` is available for download at :adi:`www.analog.com/ace <ace>` The :adi:`SDP` control boards are not included with the evaluation board and must be purchased separately. These boards can be ordered through local Analog Devices distributors as well as from :adi:`www.analog.com/sdp <sdp>`. The RF and digital interfaces for the ADAR2004-EVALZ are shown in `Figure 2 <https://wiki.analog.com/>`_.

Power Supply Requirements
-------------------------

The ADAR2004-EVALZ board must be powered from an external power supply with a voltage level of 2.5V. This power supply must have a current capability of at least 1A.

There is an on-board LDO (U105) which generates the 1.8V required to safely drive the digital pins of the :adi:`adar2004`. This supply has an associated jumper, JP1, which can be used to enable and disable the 1.8V supply.

RF Input and Output Signals
---------------------------

| The ADAR2004-EVALZ board has 21 edge-mounted and 2 vertical RF connectors which are described in Table 1.
| **Table 1: RF Connectors**

+--------------+------------------+-------------+------------+----------------------------------+
| Connector(s) | Name(s)          | Orientation | Series     | Description                      |
+==============+==================+=============+============+==================================+
| J1, J2       | RFIN1-, RFIN1+   | Edge-launch | 2.92mm (K) | Channel 1 Differential RF Input  |
+--------------+------------------+-------------+------------+----------------------------------+
| J3, J4       | RFIN2-, RFIN2+   | Edge-launch | 2.92mm (K) | Channel 2 Differential RF Input  |
+--------------+------------------+-------------+------------+----------------------------------+
| J5, J6       | RFIN3+, RFIN3-   | Edge-launch | 2.92mm (K) | Channel 3 Differential RF Input  |
+--------------+------------------+-------------+------------+----------------------------------+
| J7, J8       | RFIN4+, RFIN4-   | Edge-launch | 2.92mm (K) | Channel 4 Differential RF Input  |
+--------------+------------------+-------------+------------+----------------------------------+
| J9, J10      | IFOUT1+, IFOUT1- | Edge-launch | SMA        | Channel 1 Differential IF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J11, J12     | IFOUT1+, IFOUT1- | Edge-launch | SMA        | Channel 1 Differential IF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J13, J14     | IFOUT1+, IFOUT1- | Edge-launch | SMA        | Channel 1 Differential IF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J15, J16     | IFOUT1+, IFOUT1- | Edge-launch | SMA        | Channel 1 Differential IF Output |
+--------------+------------------+-------------+------------+----------------------------------+
| J17          | LOIN             | Edge-launch | 2.92mm (K) | Single-ended LO Input            |
+--------------+------------------+-------------+------------+----------------------------------+
| J19          | MADV             | Vertical    | SMA        | Multiplier Advance               |
+--------------+------------------+-------------+------------+----------------------------------+
| J20          | RxADV            | Vertical    | SMA        | Receiver Advance                 |
+--------------+------------------+-------------+------------+----------------------------------+
| J21, J22     | RF THRU-CAL      | Edge-launch | 2.92mm (K) | Thru-cal                         |
+--------------+------------------+-------------+------------+----------------------------------+
| J23, J24     | IF THRU-CAL      | Edge-launch | SMA        | Thru-cal                         |
+--------------+------------------+-------------+------------+----------------------------------+

|image2| **

.. container:: centeralign

   Figure 2: ADAR2004-EVALZ Connections


**

Digital Signals
---------------

The :adi:`sdp` board operates with logic levels of 3.3V, while the :adi:`adar2004` requires logic levels of 1.8V. To protect the :adi:`adar2004`, level translators (U102, U103, U104) have been included between the :adi:`sdp` connector and the rest of the board. If digital signals are applied using any method below other than the :adi:`sdp` connector, the applied logic levels must be set to 1.8V. Violating this could stress the :adi:`adar2004` beyond it’s designed limits and could result in permanent damage to the part. The level translator ICs have two separate supply voltages, one per side, which are used to set the logic level for that side of the translator. The :adi:`sdp` side voltage level is 3.3V and is taken directly from the :adi:`sdp` interface board. The :adi:`adar2004` side voltage level is 1.8V and is taken from the on-board LDO, U105. To use this :adi:`sdp` interface, the 1.8V rail must be enabled using jumper JP1.

SPI Control
~~~~~~~~~~~

The ADAR2004-EVALZ board SPI interface is meant to be driven using the :adi:`sdp` connector, P101, however, test points are also provided as an alternative. The test points are labelled with the SPI signal names (SCLK, SDIO, CSB, SDO).

The test point signals are not routed through level translators to protect the :adi:`adar2004` in case of an overvoltage scenario. Therefore, if these test points are used to drive the SPI, the input logic level must be set to 1.8V. This was done to provide a simple interface which isn’t limited in speed by the translator devices.

State Machine Control
~~~~~~~~~~~~~~~~~~~~~

The ADAR2004-EVALZ board has multiple interfaces for driving the :adi:`adar2004`\ ’s internal state machines. The :adi:`sdp` controller board can activate these lines both through the SPI interface, or through the GPIO pins on the :adi:`sdp` connector, P101. Test points are also provided as an alternative and are labelled with the signal names (MRST, RxRST, MADV, RxADV). The reset lines (MRST, RxRST) also have pushbuttons (S1, S2) that can be used to reset the sequencers by hand. The advance lines (MADV, RxADV) also have surface mount SMA connectors (J19, J20) to provide the highest speed interface for cycling through the sequencer states.

Only the signals in/out of the :adi:`sdp` connector are routed through the level translation circuitry. Therefore, if either the test points or SMA connectors are used to drive the sequencer control lines, the input logic level must be set to 1.8V.

| Also, if the SMA connectors are used to drive the sequencers at high speed, it’s best practice to terminate the signal lines in 50Ω using resistors R114 and R115. By default, these resistors are not installed.

--------------

EVALUATION AND TEST PROCEDURES
==============================

Hardware Setup
--------------

|image3| **

.. container:: centeralign

   Figure 3: Typical ADAR2004-EVALZ setup for RF measurements


**

`Figure 3 <https://wiki.analog.com/>`_ shows a typical test setup for RF measurements using a spectrum analyzer. Note that any loss in the test setup needs to be calibrated out for the most accurate measurements. The procedure for building this test setup is outlined below:

-  Connect the power supply to J18. Leave the supply disabled.
-  Connect the RF signal generator (10GHz to 40GHz) to any RF input connector between J1-J8. Leave the generator output disabled. Note that it is best practice to differentially test the :adi:`adar2004` using a balun or hybrid coupler, but it isn't required. If testing single-ended, be sure to terminate the unused output in 50Ω.
-  Connect the LO signal generator (2.5GHz to 10GHz) to J17. Leave the generator disabled.
-  Connect the spectrum analyzer to the IF output connector accompanying the RF input connector chosen for the input signal (e.g., connect to the Channel 1 IF output if the input signal goes in to the Channel 1 RF input). Note that by default, the IF outputs have a balun installed, so only the positive (+) side of each IF output channel will present a signal.
-  Set the power supply to deliver a 2.5V rail with a current limit of 500mA.
-  Check that JP1 is in position to enable the 1.8V digital supply voltage.
-  Set the RF signal generator to provide an input signal at 19.1GHz with a power level of -50dBm.
-  Set the LO signal generator to provide an input signal at 4.75GHz with a power level of -20dBm.
-  Turn on the power supply, RF signal generator and LO signal generator.

Test Setup Loss Calibration
---------------------------

The loss of the test setup must be removed for accurate data to be taken. The included thru-cals have a trace that is twice the length of the RF input traces as well as a trace that is twice the length of the IF output traces. Both test coupons include two connectors, therefore, the approximate loss of the evaluation board’s RF input traces or IF output traces can be removed from the system by measuring the thru-cals and dividing the loss by two.

Any extra external components (balun, combiner, RF cabling, attenuator pads, etc.) should also be calibrated out of the system.

Software Initialization
-----------------------

|image4| **

.. container:: centeralign

   Figure 4: Access the** :adi:`adar2004` **Plugin from ACE


**

-  Download and install :adi:`ace` by following the instructions in the `ACE user manual <http://swdownloads.analog.com/ACE/ACE_User_Manual_rev3.pdf>`_.
-  Connect the :adi:`sdp` controller board to both the PC and the ADAR2004-EVALZ.
-  Open :adi:`ace` and connect to the board by double-clicking on the ":adi:`adar2004` Board" plugin in the "Attached Hardware" section of the Start page. See `Figure 4 <https://wiki.analog.com/>`_.

|image5| **

.. container:: centeralign

   Figure 5:** :adi:`adar2004` **Main GUI Overview


**

Mutliplier Block Setup
----------------------

| The Multiplier block is designed to take a CW input between 2.5GHz to 10GHz and multiply the frequency by 4. This block also contains bandpass filters with a programmable corner frequency. To accomplish this, the Multiplier block has 3 parallel signal paths, each of which is designed to handle a portion of the total frequency band. To ensure that the highest quality signal is fed to the Receiver block, the correct multiplier band must be selected for the frequency of interest and the bandpass filter must be set to the appropriate corner for the frequency range of interest. See Table 2 for a breakdown of the multiplier bands with respect to frequency.
| **Table 2: Multiplier/Filter settings for optimal harmonic rejection**

+----------------+-------------------+------------------------------------------------+------+--------------------------+
| LO Input (GHz) | Internal LO (GHz) | Multiplier Band                                | BPF  | MULT_EN_x Register Value |
+================+===================+================================================+======+==========================+
| 2.40 to 3.00   | 9.6 to 12         | Low Band Active *(Mid and High Bands Ready)*   | LOW  | 0xFA                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+
| 3.00 to 4.00   | 12 to 16          | Low Ban Active *(Mid and High Bands Ready)*\ d | HIGH | 0x7A                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+
| 4.00 to 5.00   | 16 to 20          | Mid Band Active *(Low and High Bands Ready)*   | LOW  | 0xEE                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+
| 5.00 to 6.25   | 20 to 25          | Mid Band Active *(Low and High Bands Ready)*   | HIGH | 0x6E                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+
| 6.25 to 8.00   | 25 to 32          | High Band Active *(Low and Mid Bands Ready)*   | LOW  | 0xEB                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+
| 8.00 to 10.10  | 32 to 40.4        | High Band Active *(Low and Mid Bands Ready)*   | HIGH | 0x6B                     |
+----------------+-------------------+------------------------------------------------+------+--------------------------+

Follow the below steps to configure the Multiplier block for an LO signal of 4.75GHz (mixer LO signal of 19GHz):

-  If the recommended bias conditions aren't sufficient, choose bias points from the dropdowns for the LO input buffer stages. Click on the amplifier itself to enable the buffer. The buffer will change from grey to blue.
-  If the recommended bias condition isn't sufficient, choose a bias point from the dropdown for the Mid-Band multiplier/amplifier. Check the “Active” box next to the multiplier/amplifier. This will enable the circuit and change the input/output switches to the middle setting. The “Ready” checkbox should automatically be checked as well. The Mid-Band amplifier will change from grey to blue.
-  Be sure that the box setting the bandpass filters to their low corners is **not** checked.
-  Click “Apply Changes” at the top-left of the page to write all the new settings to the part.

Receiver Block Setup
--------------------

The Receiver block is designed to take a received signal from the 4 external antennae as well as an LO signal from the Multiplier block, amplify and convert the received signal to an IF using all four LNA/Mixer channels, and scale the output signal using four independently controlled IF amplifiers. To accomplish this, the Receiver block contains four Low Noise Amplifiers (LNAs), four active mixers, two stages of active LO splitters and four Variable Gain Amplifiers (VGAs). It should be noted that all four channels are intended to be operated together, but any combination of channels can be enabled at once.

Follow the below steps to configure the Receiver block to receive a signal at 19.1GHz and use the 19GHz signal from the Multiplier block to output an IF signal at 100MHz on all channels:

-  Enable all channels by clicking all the enable checkboxes to the left of the LNAs.
-  If the recommended bias condition isn't sufficient, choose a bias point for the LNAs from the dropdown.
-  If the recommended bias condition isn't sufficient, choose a bias point for the Mixers from the dropdown.
-  If the recommended bias condition isn't sufficient, choose a bias point for the VGAs from the dropdown.
-  If the recommended bias condition isn't sufficient, choose a gain setting for each VGA using the associated dropdown.
-  If the recommended bias condition isn't sufficient, choose an output common mode voltage (V\ :sub:`OCM`) from the dropdown.
-  If the recommended bias condition isn't sufficient, choose a bias point for each stage of the active splitters from the dropdowns. Enable the splitters by clicking them. They will change from grey to blue.
-  Enable all the LNAs by clicking the "Enable LNAs" checkbox. The LNAs will turn from grey to blue.
-  Enable all the Mixers by clicking the "Enable Mixers" checkbox. The Mixers will turn from grey to blue.
-  Enable all the VGAs by clicking the "Enable VGAs" checkbox. The VGAs will turn from grey to blue.
-  Set the gain of the IF amps using the pulldowns. Note that 0x7 corresponds to maximum gain.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Sequencer Programming
---------------------

The two built-in state machines can be used to quickly change the operating state of the :adi:`adar2004` without having to perform multiple fast SPI writes.

There are default modes already written to the control registers to facilitate easy testing of the :adi:`adar2004`\ ’s functions, but the modes and states are fully configurable to allow for any valid conditions to be tested.

“Modes” refer to the configuration of the :adi:`adar2004`, while “States” refer to the order in which the modes will be cycled through when using the two state machines.

To view the current Mode or State settings, first go to a sequencer programming tab at the top of the screen the two sub-blocks are labelled “Multiplier Block” and “Rx Block”. Choose a view type from the “Current View” box. The top checkbox will show the settings for the Modes. The middle checkbox will show the settings for the States. The bottom checkbox will show the settings from the current configuration. With the sequencer disabled, the “manual” settings will be shown. These are loaded from the SPI mode registers (0x2B-0x2F) With the sequencer enabled, the settings from the current index in the state machine will be shown. See “VIEW TYPE” in `Figure 6 <https://wiki.analog.com/>`_ and `Figure 8 <https://wiki.analog.com/>`_.

Multiplier/Filter Mode Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image6| **

.. container:: centeralign

   Figure 6: Multiplier/Filter sequencer configuration page


**

To change any of the pre-programmed Multiplier/Filter Sequencer modes, follow the below steps:

-  Switch the view to the tab named "Multiplier Block."
-  Change the various settings in the block diagram to configure the mode as desired. This block operates in the same manner as the settings on the main page. The only difference is that there aren’t any available settings for the bias points of the various parts of the chip. The bias settings are globally set on the main page and cannot be changed using the state machine.
-  Once the configuration is satisfactory, choose which mode to apply the settings to using the left-hand dropdown, and click “Apply Visible Settings to Mode”. See “RECONFIGURE MODE” in `Figure 6 <https://wiki.analog.com/>`_.
-  Repeat this process to configure all the modes of interest.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Multiplier/Filter State Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the modes have been configured, they must be linked to the states for the sequencer to cycle through.

To change the order and/or depth of the state machine, follow the below steps:

-  Change the depth of the state machine by using the labelled dropdown. See "STATE MACHINE DEPTH" in `Figure 6 <https://wiki.analog.com/>`_. Note that this number indicates the total number of states in use, n. The reset state isn't included, which is why Mode 0 is always linked to the reset state. `Figure 7 <https://wiki.analog.com/>`_ shows how the state machine pointer moves with Advance and Reset pulses.


|num_mult_states.png|

   |image7|

**

.. container:: centeralign

   Figure 7: Multiplier/Filter State machine pointer diagram


**

-  To set the order of the states, choose a mode from the middle Mode dropdown to apply to a state. Choose a state from the middle State dropdown. The current setting of that state will appear in the text on the right. Click the button labelled “Apply Selected Mode to State”, and the readout will update to reflect the change. See “RECONFIGURE STATE” in `Figure 6 <https://wiki.analog.com/>`_.
-  Repeat the process until all the desired states are set.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Receiver Mode Settings
~~~~~~~~~~~~~~~~~~~~~~

|image8| **

.. container:: centeralign

   Figure 8: Receiver sequencer configuration page


**

To change any of the pre-programmed Receiver Sequencer modes, follow the below steps:

-  Switch the view to the tab names "Rx Block."
-  Change the various settings in the block diagram to configure the mode as desired. This block operates in the same manner as the settings on the main page. The only difference is that there aren’t any available settings for the bias points of the various parts of the chip. The bias settings are globally set on the main page and cannot be changed using the state machine.
-  Once the configuration is satisfactory, choose which mode to apply the settings to using the left-hand dropdown, and click “Apply Visible Settings to Mode”. See “RECONFIGURE MODE” in `Figure 8 <https://wiki.analog.com/>`_.
-  Repeat this process to configure all the modes of interest.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Receiver State Order
~~~~~~~~~~~~~~~~~~~~

Once the modes have been configured, they must be linked to the states for the sequencer to cycle through.

To change the order and/or depth of the state machine, follow the below steps:

-  Change the depth of the state machine by using the labelled dropdown. See “STATE MACHINE DEPTH” in `Figure 8 <https://wiki.analog.com/>`_. Note that this number indicates the total number of states in use, n, not including the reset state which is always linked to Mode 0. See `Figure 9 <https://wiki.analog.com/>`_ for a diagram of the state machine indexing.


|num_Rx_states.png|

   |image9|

**

.. container:: centeralign

   Figure 9: Receiver State machine pointer diagram


**

-  To set the order of the states, choose a mode from the middle Mode dropdown to apply to a state. Choose a state from the middle State dropdown. The current setting of that state will appear in the text on the right. Click the button labelled “Apply Selected Mode to State”, and the readout will update to reflect the change. See “RECONFIGURE STATE” in `Figure 8 <https://wiki.analog.com/>`_.
-  Repeat the process until all the desired states are set.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Sequencer Control
~~~~~~~~~~~~~~~~~

The Multiplier/Filter and Receiver sequencers must be enabled before they can control the configuration of the associated :adi:`adar2004` blocks. To enable the state machines, the checkboxes in the “STATE MACHINE CONTROL” section of the main page must be checked. See `Figure 5 <https://wiki.analog.com/>`_. These checkboxes are also available in the "STATE MACHINE CONTROL" sections of the individual sequencer tabs. See `Figure 6 <https://wiki.analog.com/>`_ and `Figure 8 <https://wiki.analog.com/>`_.

When the state machines are enabled, the lights at the top of the control box will show in green. Also, the top-left section of each sequencer block on the main page will change to show that the state machine is controlling the block, rather than the SPI.

Once the state machines are enabled, the latching style must be selected. By default, when a pin is pulsed, the upcoming state is loaded into memory on the rising edge of the pulse and is latched out to the individual blocks as quickly as possible. This is necessary to allow direct SPI control of the blocks, but may require special consideration for timing. See the datasheet for details. If latching is enabled, the commands aren't sent out to the blocks until the falling edge of the pulse. This helps to align all the chip changes so that they happen at once.

Because the latch is the last check before the data is sent to the various internal blocks, when using the :adi:`adar2004` in “manual” or SPI mode, the latching must be disabled for both sequencers. If this isn’t done, the blocks will never receive the new instructions unless the external sequencer pins are pulsed. This would be uncommon since the sequencers are disabled in this mode of operation.

When the sequencers are enabled, the state machine pointers can be moved using the buttons at the bottom of the State Machine Control section. The labelled MADV, MRST, RxADV, RxRST will directly pulse the associated pin on the :adi:`adar2004`. If necessary, it’s possible to advance or reset both sequencers simultaneously by using the respectively labelled buttons.

When enabled, the State Machine Control section will also reflect the current State and Mode for each sequencer.

ADC Block
---------

The :adi:`adar2004` has an 8 bit on-chip ADC which can be used to measure internal temperature. Follow the below steps to enable the ADC for reading:

-  Be sure that the chip’s power bit is enabled at the top left of the main page.
-  Turn on the ADC’s power bit by clicking it. The ADC will change color from grey to blue.
-  Enable the internal ADC clock by clicking it. The clock will change from grey to blue.
-  Choose a clock frequency from the dropdown menu.
-  Click “Apply Changes” at the top-left of the page to send the new settings to the chip.

Temperature Sensor
~~~~~~~~~~~~~~~~~~

Once the ADC section has been enabled and configured, the on-chip temperature sensor can be used to determine the junction temperature of the :adi:`adar2004`. Clicking the "Measure ADC" button will request a reading from the :adi:`adar2004`. A temperature value will appear in the box below the button.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/1_adar2004_board.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ADAR2004/2_adar2004_connections.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ADAR2004/3_adar2004_setup.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/4_adar2004_access_ace_plugin.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/5_adar2004_main_gui_overview.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/6_multiplier_sequencer_configuration.png
.. |num_mult_states.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/num_mult_states.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/7_state_machine_loop.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/8_receiver_sequencer_configuration.png
.. |num_Rx_states.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/num_Rx_states.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adar2004/7_state_machine_loop.png
   :width: 400px
