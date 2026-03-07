EV1HMC8362LP6G/EV1HMC8364LP6G User Guide
========================================

Evaluating the HMC8362/HMC8364 Low Noise Quadband Voltage Controlled Oscillators (VCOs)
---------------------------------------------------------------------------------------

Features
--------

-  Self contained board, Including :adi:`HMC8362` or :adi:`HMC8364` low noise quadband VCO,
-  :adi:`ADG1604` 4:1 multiplexer,
-  Filtering options,
-  :adi:`LT3042` voltage regulator
-  Header connectivity to allow use of Arduino Uno, Linduino :adi:`DC2026C` microcontroller, or :adi:`SDP-K1` connector
-  Externally powered by a single 6.0 V supply

Evaluation Kit Contents
-----------------------

EV1HMC8362LP6G or EV1HMC8364LP6G evaluation board

Schematics, Gerbers, BOM, Software
----------------------------------

EV1HMC8362LP6G
~~~~~~~~~~~~~~

-  `Schematic <https://wiki.analog.com/_media/resources/eval/ev1hmc8362lp6g.pdf>`_
-  `BOM <https://wiki.analog.com/_media/resources/eval/hmc8362_evalboard.xlsx>`_

EV1HMC8364LP6G
~~~~~~~~~~~~~~

-  `Schematic <https://wiki.analog.com/_media/resources/eval/ev1hmc8364lp6g.pdf>`_
-  `BOM <https://wiki.analog.com/_media/resources/eval/hmc8364_evalboard.xlsx>`_

Equipment Needed
----------------

-  Power supply (6 V)
-  Power supply (low noise, variable 0 V to 13.5 V)
-  50 Ω terminations
-  Signal source analyzer

Online Resources
----------------

-  :adi:`HMC8362` data sheet
-  :adi:`HMC8364` data sheet
-  Linduino :adi:`DC2026C` Demo Manual

General Description
-------------------

The EV1HMC8362LP6G and EV1HMC8364LP6G allow the evaluation of the performance of the :adi:`HMC8362` and :adi:`HMC8364` low noise quadband voltage controlled oscillators (VCOs). A photograph of the evaluation board is shown in Figure 1. The evaluation board contains the :adi:`HMC8362` or :adi:`HMC8364` VCO, an :adi:`LT3042` ultralow noise voltage regulator, a jumper, an :adi:`ADG1604` 4:1 multiplexer, sub¬miniature Version A (SMA) and 2.92 mm K connectors. Consult the :adi:`HMC8362` and :adi:`HMC8364` data sheets in conjunction with this user guide when working with the evaluation boards.

EV1HMC8362LP6G/EV1HMC8364LP6G EVALUATION BOARD PHOTOGRAPH
---------------------------------------------------------

|image1| Figure 1. Evaluation Board

GETTING STARTED
---------------

EVALUATION BOARD SETUP PROCEDURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the EV1HMC8362LP6G or EV1HMC8364LP6G for the first time, perform the following steps.

-  Verify that the analog power supply that is used to power the evaluation board configured to allow an output of 6.0 V and 200 mA of compliance current.
-  Disable the power supply output.
-  Using a double shielded BNC cable and a BNC to SMA adapter, connect the analog power supply to J1.
-  Use the supplied shorting jumpers to configure the logic, as shown in Figure 2. In the configuration shown in Figure 2, the :adi:`ADG1604` multiplexer, VCO 1 of the :adi:`HMC8362` or :adi:`HMC8364`, and the output buffer amplifier are all enabled. When a jumper is disconnected the corresponding signal is pulled up to VCC. To reset a pin, connect the shorting jumper from the pin to the adjacent ground (GND). Figure 2 is annotated in green to indicate where a jumper is connected, and therefore is shorted to ground.
-  Connect the low noise, variable power supply to the SMA connector on the tuning port (J2) using a double shielded BNC cable and a BNC to SMA adapter. Torque this connection to 8 in/lb using an SMA torque wrench.
-  Connect a 50 Ω RF cable capable of mating to the 2.92 mm K connector at J3 and torque this connection to 8 in/lb. Connect the other end of the cable to a signal source analyzer.
-  Enable the 6 V power supply. Approximately 103 mA is drawn if the part is configured correctly.
-  Enable the variable power supply and adjust the tuning voltage to within the range of the VCO band being used.
-  Verify that the correct output frequency is observed on the signal source analyzer. An example using the :adi:`HMC8362` is outlined in the Evaluation and Test section.

|image2| Figure 2. Connector P1 Jumper Configuration: Alternative 5 V Supply, Multiplexer, One VCO, and Buffer Amplifier Enabled

EVALUATION BOARD HARDWARE
-------------------------

The EV1HMC8362LP6G and EV1HMC8364LP6G are identical except for Resistor R6, which sets the current limit function of the :adi:`LT3042`, and C31 which is the AC coupling capacitor on the RF output port. The evaluation board schematics, assembly, silkscreen, and bill of materials are available in the Evaluation Board Schematics and Artwork section and Ordering Information section. The gerber fabrication files are available on the :adi:`HMC8362`\ and :adi:`HMC8364` product pages on analog.com.

POWER SUPPLIES
~~~~~~~~~~~~~~

The EV1HMC8362LP6G and EV1HMC8364LP6G boards are powered by a 6 V dc (150 mA) power supply connected to the SMA connector J1 labeled 6.0 V. This supply path includes a single ultralow noise, (LDO) regulator, the :adi:`LT3042`. As an extra safeguard, the :adi:`LT3042` is configured to use the current-limit feature. A resistor (R6) sets the current limit on ILIM (Pin 5) of the :adi:`LT3042` to 114 mA (R6 = 1100 Ω) on EV1HMC8362LP6G and 156 mA (R6 = 806 Ω) for the EV1HMC8364LP6G. Users that intend to use an external power supply such as the Linduino® or Arduino® Uno microcontroller to directly program the logic from the P3 header must remove the five 10 kΩ resistors (R18, R26, R35, R36, and R37) or damage may occur. A second low noise power supply cable providing up to 13.5 V is required to tune the VCOs. Use of a noisy power supply on the tuning port results in narrow-band FM modulation and sidebands.

VOLTAGE CONTROLLED OSCILLATOR (VCO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`HMC8362` and :adi:`HMC8364` models include a total of four VCO cores that generate a range of fundamental frequencies. The frequency range of each core overlaps the adjacent core to allow continuous frequency coverage including any supply and temperature variation. By generating fundamental frequencies, the need for additional filtering can be reduced or eliminated because there are no subharmonics. The tuning sensitivity across the band is similar for each core, which simplifies the loop filter design. Any frequency planning or dynamic loop bandwidth adjustment required to manage spurs or settling time is made easier by the consistent tuning sensitivity from core to core. The integrated common tuning (VTUNE on J2) and RF output ports (RF1) simplify layout. Each band has an allowable tune voltage of 1.0 V dc to 13.5 V dc. The oscillator cores must be selected, one at a time, depending on the frequency range required at any point in time by the application. The VCO cores are selected by simply enabling the supply voltage at its respective bias pin (VC1 through VC4). The EV1HMC8362LP6G and EV1HMC8364LP6G boards accomplish this VCO core selection through the use of the :adi:`ADG1604` 4:1 multiplexer. The VCO cores can be enabled and disabled in any sequence desired. The EV1HMC8362LP6G and EV1HMC8364LP6G boards include additional filtering to prevent supply voltage overshoot and undershoot, which can damage the device if overshoot exceeds 5.5 V. This filtering provides 5 V of biasing that settles within about 1 µs.

BUFFER AMPLIFIER
~~~~~~~~~~~~~~~~

The buffer amplifier used in the :adi:`HMC8362` and :adi:`HMC8364`\ is a broadband cascode design that draws approximately 12 mA and is shared by all four VCO cores. Pin 8 (VCB) of the :adi:`HMC8362` and :adi:`HMC8364` provides the bias voltage for the upper half of the cascode amplifier. The VCO outputs provide the biasing for the lower half of the cascode amplifier stage. When one of the four VCOs is enabled, the cascode amplifier becomes fully enabled and provides an output signal at Pin 5. The buffer amplifier was designed to handle the power supplied by only one VCO at a time. To prevent long-term damage that can occur if more than one VCO is powered up simultaneously, the EV1HMC8362LP6G and EV1HMC8364LP6G boards incorporate the :adi:`ADG1604` 4:1 multiplexer. As configured on the EV1HMC8362LP6G and EV1HMC8364LP6G, the :adi:`ADG1604` multiplexer incorporates exclusive OR (XOR) logic and the ability to break contact with one VCO for a minimum of 30 ns before closing the contacts on the next switch to power up a different VCO core. To minimize the switching time of the :adi:`ADG1604`, 5 V logic is used but 3 V can also be used through an external power supply or microcontroller such as a Linduino or Arduino Uno. Refer to the :adi:`ADG1604` data sheet for more information regarding the :adi:`ADG1604` logic and use with other logic levels. Users can opt to leave the VCO enabled and power down Pin 8 (VCB) to mute the output signal, which leaves the lower stage of the cascode enabled. However, because the upper circuitry is disabled, RF is not routed to the output. Figure 5 shows the :adi:`HMC8362` with VC1 enabled but the output buffer muted (VCB_EN on P3 = 0). For additional details on the buffer amplifier circuitry, consult the :adi:`HMC8362` or :adi:`HMC8364` data sheet.

RF OUTPUT
~~~~~~~~~

The EV1HMC8362LP6G and EV1HMC8364LP6G boards have a single RF output port (RF1). RF1 is supplied by a buffer amplifier that is common to all four VCO cores. RF1 (J3) is a single-ended RF output that operates up to 26.6 GHz. The actual frequency range and power level at any given time depends on which model is being evaluated and the VCO core that is enabled. Consult the :adi:`HMC8362` and :adi:`HMC8364` data sheets for additional information relative to the specific model being evaluated for more information.

LOOP FILTER
~~~~~~~~~~~

Although the EV1HMC8362LP6G and EV1HMC8364LP6G boards do not incorporate the entire loop filter, they do provide the means to filter noise that may appear on the tuning port when evaluating only the VCOs. By default, a 100 pF capacitor (C12) is placed near Pin 27 (VTUNE) of the :adi:`HMC8362` and :adi:`HMC8364` to filter high frequency noise that may couple onto the tune port path when evaluating the various VCOs. The EV1HMC8362LP6G and EV1HMC8364LP6G boards also include placements for the last pole of a loop filter on the tuning port path for use when configuring the :adi:`HMC8362` and :adi:`HMC8364` with an Analog Devices, Inc., standalone phase-locked loop (PLL) product like the ADF41513. Although the tuning port path and input capacitance of the VCO makes up the last pole of the loop filter, this user guide refers to the last pole as that which can be accessed by the user. Due to the increased length of the loop filter path that typically occurs when using evaluation boards to build a synthesizer, placement of the loop filter components becomes critical. Loop stability and overall performance is improved by placing the first pole of the loop filter as close to the PLL charge pump (CP) output as possible while placing the last pole as close to the tuning port pin (VTUNE) of the VCO. The placement of any additional poles that may exist between the first and last pole of the loop filter are not as critical. Therefore, these filter poles remain on the ADF41513. The placements for this last pole on the EV1HMC8362LP6G and EV1HMC8364LP6G are populated by default and consist of R32 (0 Ω by default) and a 100 pF capacitor (C12) near Pin 27 (VTUNE). Users can replace these components with the proper values as needed. The tuning voltage requirements of the :adi:`HMC8362` and :adi:`HMC8364` (1.0 V to 13.5 V) require an active loop filter to be used unless the charge pump of the PLL can output at least 14 V. The PLL evaluation board typically includes placements for the operational amplifier, its biasing circuitry, and any component placements. Therefore, these components are not included on the EV1HMC8362LP6G and EV1HMC8364LP6G. SMA Connector J2 provides means to connect the PLL CP output to the tuning port (VTUNE) when the EV1HMC8362LP6G and EV1HMC8364LP6G are used with an optional PLL evaluation board. J2 can also be used to manually tune the VCO within its band when evaluating the open-loop VCO performance.

DEFAULT CONFIGURATION
~~~~~~~~~~~~~~~~~~~~~

All components necessary for local oscillator generation are inserted on the EV1HMC8362LP6G and EV1HMC8364LP6G boards.

EVALUATION BOARD SOFTWARE
-------------------------

SOFTWARE
~~~~~~~~

Currently there is no software available for the EV1HMC8362LP6G and EV1HMC8364LP6G because they can be evaluated without the use of software. However, the EV1HMC8362LP6G and EV1HMC8364LP6G are configured in a manner that allows use of a Linduino :adi:`DC2026C`, Arduino Uno, :adi:`SDP-K1` or similar microcontroller board, which may be beneficial for users needing to develop and test switching algorithms for their application. To connect the :adi:`SDP-K1` interface board to the EV1HMC8362LP6G or EV1HMC8364LP6G, flip the :adi:`SDP-K1` board over so that the digital input/output pins (Pin 8 through Pin 14) of the :adi:`SDP-K1` line up with Pin 3 to Pin 15 of Connector P3, respectively as shown in Figure 3.

|image3| Figure 3. SDP-K1 Board mounted to EV1HMC8362LP6

EVALUATION AND TEST
-------------------

To configure the EV1HMC8362LP6G and EV1HMC8364LP6G for the first time, follow Step 1 through Step 6 outlined in the Evaluation Board Setup Procedure section. The frequency vs. tune voltage listed in the following steps are specific to the EV1HMC8362LP6G, but the same process is applicable to the EV1HMC8364LP6G. The frequency range and performance are different.

-  Enable the variable power supply and adjust the tuning voltage to 8.45 V.
-  If the EV1HMC8362LP6G is configured correctly, a signal at approximately 13.5 GHz with approximately 0 dBm to 2 dBm of output power appears on a spectrum analyzer or signal source analyzer. Refer to Figure 4.
-  Remove the bias for the buffer amplifier (VCB), which results in the output power decreasing by approximately 28 dBm. Refer to Figure 5.
-  Finally, use the signal source analyzer to measure the phase noise. Refer to Figure 6.

|image4| Figure 4. EV1HMC8362LP6G, VCO Band 1, VTUNE = 8.45 V, 13.5 GHz, Includes Insertion Loss of RF Cable

|image5| Figure 5. EV1HMC8362LP6G, VCO Band 1, VTUNE = 8.45 V, 13.5 GHz, Buffer Amplifier Disabled (RF1 Output Muted), Includes Insertion Loss of RF Cable

|image6| Figure 6. EV1HMC8362LP6G Phase Noise at RF1, VCO Band 1, VTUNE = 8.45 V, 13.5 GHz

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/figure_1_evb_pic.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/figure_2_p1_connector.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/figure_3_sdp-k1_board_mounted_to_ev1hmc8362lp6.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/figure_3_vco_band_1.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/figure_4._ev1hmc8362lp6g_vco_band_1_vtune_8.45_v_13.5_ghz_buffer_amplifier_disabled.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/figure_5_vco_band_1_pn_at_rf1.png
   :width: 400px
