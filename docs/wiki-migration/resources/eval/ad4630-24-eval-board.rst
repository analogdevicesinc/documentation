AD4630/AD4030 Evaluation Board User Guide
=========================================

General Description
-------------------

| The EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ & EVAL-AD4630-16FMCZ evaluation boards enable quick and easy evaluation of the AD4X3X family of 24-bit & 16-bit precision successive approximation register (SAR) analog-to-digital converters (ADCs).
| The `AD4630-24 <http://www.analog.com/en/products/AD4630-24.html>`__ & `AD4630-16 <http://www.analog.com/en/products/AD4630-16.html>`__ are 2MSPS per channel, low power, dual channel 24-bit or 16-bit SAR ADCs while the `AD4030-24 <http://www.analog.com/en/products/AD4030-24.html>`__ is a single channel 24-bit precision SAR ADC that supports up to 2 MSPS per channel. The evaluation boards demonstrate the performance of either the AD4630-24, AD4030-24 or AD4630-16 and provides a configurable analog front end (AFE) for a variety of system applications.
| The evaluations board are designed for use with the Digilent `ZedBoard <http://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`__. The ZedBoard is used to control data capture and buffering. The evaluation board connects to the ZedBoard board via a field-programmable gate array (FPGA) mezzanine card (FMC) low pin count (LPC) connector. The ZedBoard hosts a Xilinx Zynq7000 SoC, which has two processor cores and programmable FPGA fabric. The ZedBoard connects to the PC through USB.
| ===== Evaluation Boards available ===== Two different EVAL board revision has been released on the market for AD4630-24 and AD4630-16, the old Rev C which is obsoleted and the new revision, Rev E. On the other hand, there is only one existing revision for AD4030-24, Rev A/B, which is still available:

| − **OLD** AD4630-24 and AD4630-16 **Rev C** (obsoleted) evaluation boards include:

-  Two differential input channels with SMA connectors
-  A high precision buffered band gap 5V reference (:adi:`LTC6655 <en/products/ltc6655.html>`).
-  An analog front end (AFE) that provides signal conditioning and drive for the AD4630-24 & AD4630-16. The AFE can be configured to use either the `ADA4896-2 <http://www.analog.com/en/products/ADA4896-2.html>`__ in a dual buffer configuration, or the `ADA4945-1 <http://www.analog.com/en/products/ADA4945-1.html>`__, a fully differential amplifier.
-  An optional 100 MHz clock source that provides a reference clock for the FPGA and ADC.
-  Full power supply solution that provides all the necessary voltage rails from a 12V supply that is provided from the ZedBoard through the FMC connector.

| 
| |image1|
| **Figure 1a. EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ. Rev C**

| − **NEW** AD4630-24 and AD4630-16 **Rev E** evaluation boards include:

-  Two differential input channels with SMA connectors
-  A high precision, low power and low noise 5V reference :adi:`ADR4550 <en/products/adr4550.html#part-details>`. There is also the option to mount a high precision buffered band gap 5V reference, the :adi:`LTC6655 <en/products/ltc6655.html>`.
-  An analog front end (AFE) that provides signal conditioning and drive for the AD4630-24 & AD4630-16. The AFE can be configured to use either the `ADA4896-2 <http://www.analog.com/en/products/ADA4896-2.html>`__ in a dual buffer configuration, or the `ADA4945-1 <http://www.analog.com/en/products/ADA4945-1.html>`__, a fully differential amplifier.
-  Multiple different input configurations with the amplifier `ADA4896-2 <http://www.analog.com/en/products/ADA4896-2.html>`__
-  An optional 100 MHz clock source that provides a reference clock for the FPGA and ADC.
-  New form format and improved full power supply solution that provides all the necessary voltage rails from a 12V supply that is provided from the ZedBoard through the FMC connector.
-  Extra connectors to supply the board externally if needed.

|

.. important::

   New boards EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ **REV E** have a date code bigger than DC>2435


| |image2|
| \**Figure 1b. New EVAL-AD4630-24FMCZ and EVAL-AD4630-16FMCZ. Rev E \*\*

| − AD4030-24 **Rev A/B** evaluation board includes:

-  One differential input channel with SMA connectors
-  A high precision buffered band gap 5V reference (:adi:`LTC6655 <en/products/ltc6655.html>`).
-  An analog front end (AFE) that provides signal conditioning and drive for the AD4030-24. The AFE can be configured to use either the `ADA4896-2 <http://www.analog.com/en/products/ADA4896-2.html>`__ in a dual buffer configuration, or the `ADA4945-1 <http://www.analog.com/en/products/ADA4945-1.html>`__, a fully differential amplifier.
-  An optional 100 MHz clock source that provides a reference clock for the FPGA and ADC.
-  Full power supply solution that provides all the necessary voltage rails from a 12V supply that is provided from the ZedBoard through the FMC connector.

| 
| |image3|
| **Figure 1c. EVAL-AD4030-24FMCZ. Rev A/B**

| Full descriptions of these products are available in their respective data sheets, which should be consulted when using the evaluation board.

Features
--------

-  On-board voltage reference, clock source, and ADC drivers
-  Versatile analog signal conditioning circuitry
-  FMC-LPC system board connector
-  ACE PC software for configuration and data analysis (time and frequency domain)
-  Compatible with other off-the-shelf controller boards

Evaluation Board Kit Contents
-----------------------------

-  EVAL-AD4630-24FMCZ, EVAL-AD4030-24FMCZ or EVAL-AD4630-16FMCZ evaluation board
-  Micro-SD memory card (with adapter) containing system board boot software and Linux OS
-  Optional - ZedBoard (system controller board )

Equipment Needed
----------------

-  PC with Windows 7 or Windows 10 operating system
-  Digilent ZedBoard with 12 V wall adapter power supply
-  Precision signal source
-  SMA Cable(s) (input to evaluation board)
-  Recommended - Band-pass filter centered on test signal frequency.

Quick Start Guide
-----------------

.. important::

   To avoid potential issues, ensure the ZedBoard VADJ SELECT = 2.5V. |image4|\


-  Download and install the ACE Software tool from the :adi:`ACE` download page. If ACE is already installed, make sure you have the latest version by using the ‘Check For Updates’ option in the ACE sidebar.
-  An ACE Quickstart guide is available here: :doc:`ACE Quickstart - Using ACE and Installing Plug-ins </wiki-migration/resources/tools-software/ace/userguide/quickstart>`
-  Insert the EVAL-SD-KUIPERZ SD card into the SD card slot on the underside of the ZedBoard.

.. note::

   If there is a need to re-image or create a new SD card, instructions are available here: :doc:`ADI Kuiper Linux with support for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace>`.


-  Ensure the ZedBoard boot configuration jumpers are set to use the SD card as shown.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zedboard-sd-card-boot-jumpers.png
   :align: center
   :width: 200px

.. important::

   To avoid potential damage, ensure the VADJ SELECT jumper is set to the correct voltage for the Product Evaluation Board.


-  Connect the Product Evaluation Board to the FMC connector on the ZedBoard.

.. note::

   There may be additional steps and hardware required for a given Product Evaluation Board, for example, function generators connections and setup. This information may be included with the eval kit or in the User guide for the corresponding Product Evaluation Boards page that can be found by searching :adi:`Product Evaluation Boards and Kits <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits.html>`.


-  Connect the USB cable from the PC to the J13/USB OTG port and the PSU to J20/DC input.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/zedboard-usb_otg-power.png
   :align: center
   :width: 200px

-  Slide SW8/POWER switch to the ON position. The green LD13/POWER LED should turn on.
-  The blue LD12/DONE LED & red LD0 LED should start blinking ~20-30 seconds later which indicates the boot process is complete.

.. tip::

   Linux versions prior to ADI Kuiper Linux for Evaluation version 2024-8-27 will instead boot with the BLUE LD12/DONE LED blinking immediately and LD7 blinking after ~20-30Seconds. This may indicate that an improved version of the ACE plugin is available if the SD-Card is updated to the latest version.


-  Launch the ACE software from the Analog Devices folder in the Windows Start menu. The Evaluation Board should appear in the ACE Start Tab >> Attached Hardware view.

.. image:: https://wiki.analog.com/_media/resources/eval/ad4630-24-eval-board/ace_attached_hw-screen.png
   :align: center
   :width: 200px

Setting Up the Evaluation Board
-------------------------------

| Figure 1 illustrates the evaluation system components. To use the system, connect the evaluation board to the ZedBoard, connect a micro-USB cable to the USB OTG port, apply power to the ZedBoard, open the ACE GUI, and supply an input stimulus to one or both ADC channels.

| Each ADC channel has dedicated SMA connectors that support either a singled-ended or differential input. The signals on these inputs are injected to the configurable AFE (see the **Analog Front End** section below for more details). The digital interface to the system controller board uses level shifters to translate between the VIO supply of the AD4630-16 and the I/O voltage of the Zynq 7000 on the ZedBoard. By default, the evaluation board is powered from the system controller board 12V supply through the FMC connector. The **Power Supplies** section contains a list of optional on-board connections that can be used to connect external supplies and references to the board.

Evaluation Board Hardware (EVAL-AD4630-24/16FMCZ REV C and EVAL-AD4030-24FMCZ REV A/B)
--------------------------------------------------------------------------------------

| |image5|
| **Figure 2. EVAL-AD4630-XXFMCZ Evaluation System**

Power Supplies
~~~~~~~~~~~~~~

The primary 12V supply to the EVAL-AD4X30-XXFMCZ comes from the ZedBoard through the FMC connector. 12V is regulated down to an intermediate voltage with a switcher and then is post regulated down to the various voltage rails. 12V is also used to generate the negative rails for the buffers and final drive amplifiers.

| Each of the voltage rails are brought out to turrets so they can be easily measured (see **Figure 1**). A bench supply can be used to drive these turrets to supply the evaluation board manually. This is useful if a current measurement is required. Each supply is decoupled where it enters the board and at each device. A single ground plane is used on this board to minimize the effect of high frequency interference. The voltage ranges listed in the table below represent the expected ranges for the board. If the user desires to connect external supplies to the board, the amplifier data sheets and the `AD4630-24 datasheet <http://www.analog.com/en/products/AD4630-24.html>`__, `AD4030-24 datasheet <http://www.analog.com/en/products/AD4030-24.html>`__ or `AD4630-16 datasheet <http://www.analog.com/en/products/AD4630-16.html>`__ should be consulted to ensure that the external supply values comply with the device requirements.

============ ========================================= ======== ========
Power Supply Function                                  Min. (V) Max. (V)
============ ========================================= ======== ========
+12V         12V primary supply via FMC connector      N/A      N/A
GND          Ground connection                         N/A      N/A
+3.3V        3.3V for various digital logic            3.26     3.33
+1.8V        1.8V for the ADC                          1.77     1.81
VIO          1.8V supply for the ADC digital I/O       1.8      1.87
+5V          5V for the ADC                            5.26     5.4
REFIN        5V ADC reference input                    4.95     5.05
VAMP+        Positive supply for the amplifiers        5.36     5.47
VAMP-        Negative supply for the amplifiers        -3.5     -3.28
VP1          5.7V at the input of the switcher         5.45     5.75
REF          5V at the ADC reference output            4.95     5.05
EN           1.8V enable signal for the power supplies 1.75     1.85
============ ========================================= ======== ========

| \*\* *Table 1. On-Board Power Supplies* \*\*
| ==== Reference Circuit ==== By default, the on-board LT6655 provides a 5 V reference to the AD4630-24, AD4030-24 & AD4630-16. It drives the REFIN pin of the ADC through an R-C filter (R=100Ω, C=1μF) that reduces the low frequency noise. The REFIN pin is connected to an internal buffer, eliminating the need for an external buffer. However, if the user desires to use an external reference that drives the internal buffer, it can be attached the EXT REF SMA connector (see figure below). R137 should be populated with a zero ohm resistor, and R136 should be open. The internal buffer can be bypassed by attaching an external reference to the REF turret on the board. To reduce the ADC power consumption, the internal reference buffer can be disabled (see respective products data sheet).

| |image6|
| **Figure 3. EVAL-AD4X30-XXFMCZ Reference circuit (AD4630-24 shown. Configuration applies to all parts)**

Clock Circuit
~~~~~~~~~~~~~

| The ZedBoard uses a 100MHz reference clock to generate its internal clocks as well as the sample clock for the AD4630-24, AD4030-24 or AD4630-16. To simplify system operation an on-board 100MHz, low-jitter crystal oscillator (XO) on the EVAL-AD4X30-XXFMCZ board supplies this clock as the default configuration, as shown in the figure below. To use an external clock source, remove R55 and connect an external clock source to J1, the CLK IN SMA. **The external clock frequency must be < 100 MHz**. The user should take care to use a low jitter clock source to achieve best system performance. The external clock level should be 10 to 12 dBm.

| |image7|
| **Figure 4. EVAL-AD4X30-XXFMCZ clock circuit (AD4630-24 shown. Configuration applies to all parts)**
| ==== Analog Front End ==== The EVAL-AD4X30-XXFMCZ has a flexible driver network that can be configured for a variety topologies. The default network is shown in Figure 5, in which the ADA4945-1 fully differential amplifier is driving the ADC. It can accommodate both single-ended and differential signal sources, and drives the ADC differentially. As populated, it has a unity gain. When using a single-ended source, the unused input should be terminated with the equivalent source impedance. **Note:** As implemented, the AD4945-1 driver on the evaluation board preserves the differential value of IN+ - IN- (with appropriate gain scaling applied), but inverts the signal polarity that is injected to the ADC. Hence, if a positive DC signal is applied to the input, it should be attached to IN_A/B-, and likewise, a negative DC signal should be attached to IN_A/B+ to preserve the signal polarity.

| |image8|
| **Figure 5. Differential Driver AFE (default) (AD4630-24 shown. Configuration applies to all parts)**

+----------------------------------------------+---------------------------------------------------------+
| Function:                                    | Single ended to differential via differential amplifier |
+==============================================+=========================================================+
| Comments:                                    | Best distortion                                         |
+----------------------------------------------+---------------------------------------------------------+
| Required changes from default configuration: | No changes required                                     |
+----------------------------------------------+---------------------------------------------------------+

| **Table 2. EVAL-AD4620-16FMCZ Default AFE Configuration**
| A second topology can be seen in Figure 6. This topology consists of a pair of unity gain buffers, the ADA4896-2. It also can be driven by either a singled-ended or differential source. This network is ideal for observing the best noise performance of the AD4630-16, due to the low voltage and current noise of the ADA4896-2 (1 nV/rtHz and 2.8 pA/rtHz, respectively). It also offers a common mode input impedance of 10 MΩ and a wide input common mode voltage range of -4.9V to +4.1V (when using +/- 5V supplies). **Note:** This driver circuit also inverts the polarity of the input signal. To preserve polarity when measuring DC voltages, connect a positive voltage to IN_A/B-. Likewise, a negative DC voltage should be connected to IN_A/B+.

| |image9|
| **// Figure 6. Dual Buffer AFE (AD4630-24 shown. Configuration applies to all parts) //**

+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function:                                    | Differential input using buffer amplifiers                                                                                                                      |
+==============================================+=================================================================================================================================================================+
| Comments:                                    | Best noise & relaxed drive requirement for signal source                                                                                                        |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Required changes from default configuration: | Remove: R10, R12,R119, R120, R121 & R122 (Ch. A); R20, R22, R123, R124, R125 & R126 (Ch. B). Install: R31, R33, R47, & R49 (Ch. A); R60, R62, R75 & R78 (Ch. B) |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

| \*\* *Table 3. Unity Gain Dual Buffer Configuration* \*\*

| Figure 7 shows a driver network which combines the ADA4896-2 with the ADA4945-1. This circuit is ideal for applications that require a high input impedance along with gain to maximize the input range of the ADC. The gain of the ADA4945-1 can modified by changing either the feedback resistors or input resistors.

| |image10|
| **Figure 7. High Impedance Buffer with Gain AFE (AD4630-24 shown. Configuration applies to all parts)**

+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Function:                                    | High impedance input with gain                                                                                                          |
+==============================================+=========================================================================================================================================+
| Comments:                                    | Relaxed drive requirements from signal source plus signal scaling.                                                                      |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Required changes from default configuration: | Remove:R120, R121 (Ch. A);R124, R125 (Ch. B). Install: R31, R127, R28, R47, R128 & R43 (Ch. A); R60, R129, R57, R78, R130 & R72 (Ch. B) |
+----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

| **// Table 4. High Impedance with Gain Configuration //**
| Figure 8 shows an input configuration that allows the AD4630-16 to be directly driven from the SMA connectors. This enables testing with alternative driver configurations mounted on an external PCB.

| |image11|
| **Figure 8. Direct Driven Inputs (AD4630-24 shown. Configuration applies to all parts)**
| ^ Function: \| Direct input path \| ^ Comments: \| Supports evaluation with an alternative driver \| ^ Required changes from default configuration: \| Remove: R10, R12, R119 & R122 (Ch A); R20, R22, R123, R126 (Ch B). Install: R28, R29, R120, R121, R43 & R44 (Ch A); R124, R57, R58, R125, R72 & R73 (Ch B) \|
| \*\* *Table 5. Direct Drive Configuration* \*\*

Evaluation Board Hardware (EVAL-AD4630-24/16FMCZ REV E)
-------------------------------------------------------

| |image12|

| **Figure 9. EVAL-AD4630-XXFMCZ Evaluation System**

.. _power-supplies-1:

Power Supplies
~~~~~~~~~~~~~~

The primary 12V supply to the EVAL-AD4X30-XXFMCZ comes from the ZedBoard through the FMC connector. 12V is regulated down to an intermediate voltage, +7.5V, with a switcher and then is post regulated down to the various voltage rails. 12V is also used to generate the negative rails, -3.3V for the buffers and final drive amplifiers.

| Each of the voltage rails are brought out to turrets so they can be easily measured (see **Figure 1**). A bench supply can be used to drive these turrets to supply the evaluation board manually. This is useful if a current measurement is required. Each supply is decoupled where it enters the board and at each device. A single ground plane is used on this board to minimize the effect of high frequency interference. The voltage ranges listed in the table below represent the expected ranges for the board. If the user desires to connect external supplies to the board, the amplifier data sheets and the `AD4630-24 datasheet <http://www.analog.com/en/products/AD4630-24.html>`__, `AD4030-24 datasheet <http://www.analog.com/en/products/AD4030-24.html>`__ or `AD4630-16 datasheet <http://www.analog.com/en/products/AD4630-16.html>`__ should be consulted to ensure that the external supply values comply with the device requirements.

============ ========================================= ======== ========
Power Supply Function                                  Min. (V) Max. (V)
============ ========================================= ======== ========
+12V         12V primary supply via FMC connector      N/A      N/A
GND          Ground connection                         N/A      N/A
+3.3V        3.3V for various digital logic            3.26     3.33
+1.8V        1.8V for the ADC                          1.77     1.81
VIO          1.8V supply for the ADC digital I/O       1.77     1.81
+5.4V        5.4V for the ADC                          5.34     5.46
REFIN        5V ADC reference input                    4.95     5.05
VAMP+        Positive supply for the amplifiers        6.35     6.5
VAMP-        Negative supply for the amplifiers        -3.35    -3.28
VP1          7.5V at the input of the switcher         7.425    7.575
REF          5V at the ADC reference output            4.95     5.05
EN           1.8V enable signal for the power supplies 1.75     1.85
============ ========================================= ======== ========

| \*\* *Table 6. On-Board Power Supplies* \*\*
| The following block diagram shows all the different power supplies options available in the new evaluation board. In case necessary, it is possible to supply all the LDOs directly with external power supplies via J7 and J8. There is also two different options to generate the -3.3V although only the LT3093 is mounted on the board.
| |image13|
| **Figure 10. Power-tree**

Reference Circuit
~~~~~~~~~~~~~~~~~

| By default, the on-board ADR4550 provides a 5 V reference to the AD4630-24 & AD4630-16. It drives the REFIN pin of the ADC through an R-C filter (R=100Ω, C=22μF) that reduces the low frequency noise. The REFIN pin is connected to an internal buffer, eliminating the need for an external buffer. However, if the user desires to use an external reference that drives the internal buffer, it can be attached the J5 SMA connector (see figure below). R124 should be populated with a zero ohm resistor, and R116 and R123 should be open. The internal buffer can be bypassed by attaching an external reference to the REF turret on the board. To reduce the ADC power consumption, the internal reference buffer can be disabled (see respective products data sheet). There is also the option to mount the LTC6655 or the LTC6655LN reference which is suitable to use it together with the unbuffered input of the ADC.

.. _section-1:

| |image14|
| **Figure 11. EVAL-AD4630-XXFMCZ Reference circuit (AD4630-24 shown. Configuration applies to all parts)**

.. _clock-circuit-1:

Clock Circuit
~~~~~~~~~~~~~

| The ZedBoard uses a 100MHz reference clock to generate its internal clocks as well as the sample clock for the AD4630-24 or AD4630-16. To simplify system operation an on-board 100MHz, low-jitter crystal oscillator (XO) on the EVAL-AD4630-XXFMCZ board supplies this clock as the default configuration, as shown in the figure below. To use an external clock source, remove R1 and connect an external clock source to J6, the CLK IN SMA. **The external clock frequency must be < 100 MHz**. The user should take care to use a low jitter clock source to achieve best system performance. The external clock level should be 10 to 12 dBm.

| |image15|
| **Figure 12. EVAL-AD4630-XXFMCZ clock circuit (AD4630-24 shown. Configuration applies to all parts)**
| ==== Analog Front End ==== The EVAL-AD4630-XXFMCZ has a flexible driver network that can be configured for a variety topologies. The default network is shown in Figure 13, in which the ADA4945-1 fully differential amplifier is driving the ADC. It can accommodate both single-ended and differential signal sources, and drives the ADC differentially. As populated, it has a unity gain. When using a single-ended source, the unused input should be terminated with the equivalent source impedance. **Note:** As implemented, the AD4945-1 driver on the evaluation board preserves the differential value of IN+ - IN- (with appropriate gain scaling applied), but inverts the signal polarity that is injected to the ADC. Hence, if a positive DC signal is applied to the input, it should be attached to IN_A/B-, and likewise, a negative DC signal should be attached to IN_A/B+ to preserve the signal polarity.

| |image16|
| **Figure 13. Differential Driver AFE (default) (AD4630-24 shown. Configuration applies to all parts)**

+----------------------------------------------+---------------------------------------------------------+
| Function:                                    | Single ended to differential via differential amplifier |
+==============================================+=========================================================+
| Comments:                                    | Best distortion                                         |
+----------------------------------------------+---------------------------------------------------------+
| Required changes from default configuration: | No changes required                                     |
+----------------------------------------------+---------------------------------------------------------+

| **Table 7. EVAL-AD4620-16FMCZ Default AFE Configuration**
| There is one buffer used to generate common mode voltage, U26. The voltage can be adjusted from 0V to Vref by selecting correctly the ratio between R98, (or R122 or R99) and R5.
| |image17|
| **// Figure 14. Common mode voltage generation //**
| A second topology can be seen in Figure 15. This topology consists of a pair of unity gain buffers, the ADA4896-2. It also can be driven by either a singled-ended or differential source. This network is ideal for observing the best noise performance of the AD4630-16, due to the low voltage and current noise of the ADA4896-2 (1 nV/rtHz and 2.8 pA/rtHz, respectively). It also offers a common mode input impedance of 10 MΩ and a wide input common mode voltage range of -4.9V to +4.1V (when using +/- 5V supplies). To use the full span of the ADC the input signal of each buffer needs to be centered at 2.5V

| |image18|
| **// Figure 15. Dual Buffer AFE.//**

+----------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Function:                                    | Differential input using buffer amplifiers                                                                    |
+==============================================+===============================================================================================================+
| Comments:                                    | Best noise & relaxed drive requirement for signal source                                                      |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Required changes from default configuration: | Remove: R17, R23, R19, R25, R42, R45, R44 and R48. Install: R114, R108, R112, R106, R139, R136, R137 and R134 |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------+

| \*\* *Table 8. Unity Gain Dual Buffer Configuration* \*\*
| If the signal generator connected to the inputs of the ADC cannot generate a DC offset, there is the option to use the VOCM buffer to create an DC offset and connect it to the non-inverting input of the ADA4896 amplifiers like Figure 16.

| |image19|
| **Figure 16. High Impedance Buffer with VOCM generated internally**

+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function:                                    | High impedance input with gain                                                                                                                                |
+==============================================+===============================================================================================================================================================+
| Comments:                                    | Relaxed drive requirements from signal source plus DC offset.                                                                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Required changes from default configuration: | Remove: R17, R23, R19, R25, R42, R45, R44 and R48. Install: R114, R108, R112, R106, R139, R136, R137, R134, R120, R119, R103, R102, R142, R141, R132 and R131 |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

| **// Table 9. High Impedance Buffer with VOCM //**
| Another option available (Figure 17) on the board is to use the ADA4896 in an inverting configuration with the possibility of connecting an DC offset on the non-inverting pin. I this case it is necessary to have two input signals delayed 180º and select the correct resistors values to generate a 2.5V (R98 and R3) as VOCM.

| |image20|
| **Figure 17. High Impedance Buffer with VOCM generated internally**

+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function:                                    | High impedance input with gain                                                                                                                               |
+==============================================+==============================================================================================================================================================+
| Comments:                                    | Relaxed drive requirements from signal source plus DC offset.                                                                                                |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Required changes from default configuration: | Remove: R17, R23, R19, R25, R42, R45, R44 and R48. Install: R126, R96, R112, R106, R145, R129, R137, R134, R120, R119, R103, R102, R142, R141, R132 and R131 |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

| **// Table 10 High Impedance Buffer with VOCM //**
| Figure 18 shows an input configuration that allows the AD4630-16 to be directly driven from the SMA connectors. This enables testing with alternative driver configurations mounted on an external PCB.

| |image21|
| **Figure 18. Direct Driven Inputs (AD4630-24 shown. Configuration applies to all parts)**
| ^ Function: \| Direct input path \| ^ Comments: \| Supports evaluation with an alternative driver \| ^ Required changes from default configuration: \| Remove: R17, R23, R19, R25, R42, R45, R44 and R48. Install: R121, R118, R104, R105, R143, R140, R133 and R130.\|
| \*\* *Table 10. Direct Drive Configuration* \*\*

Controller Board
----------------

The ZedBoard, which is the system controller board, enables the configuration of the ADC and capture of data from the evaluation board by the PC via USB (or Ethernet). The AD4X30-XX family of parts support a multi-lane serial port interface (SPI) for each data converter channel. The SPI interface for each channel is connected to the ZedBoard via the FMC connector (P1). The ZedBoard™ functions as the communication link between the PC and connected evaluation board. It buffers samples captured from the evaluation board in its DDR3 memory. The ZedBoard board requires power from a 12V wall adapter (included with the ZedBoard). It hosts a Xilinx® ZYNQ® 7020 SoC, which contains two ARM® Cortex-A9 Processors and a Series-7 FPGA with 85k Programmable Logic cells. A Linux OS runs on the host processor system. It communicates with the PC through either a USB 2.0 high speed port or a 10/100/1000 Ethernet port. The default software configuration uses USB.

EVALUATION HARDWARE SETUP
~~~~~~~~~~~~~~~~~~~~~~~~~

When the ACE evaluation software installation is complete, take the following steps to set up the ZedBoard and the evaluation board together:

1. Insert the SD card provided with the evaluation board into J12 on the ZedBoard

2. Connect the Evaluation board to the FMC connector of the ZedBoard.

3. Connect the provided power supplies to J20 on the ZedBoard.

4. Connect the USB cable to the USB OTG (J13) on the ZedBoard and to the computer

5. Connect the desired input signal to the appropriate input on the evaluation board (J2-J5)

6. Move SW8 to the ON position to start the ZedBoard

7. Start the ACE evaluation software (Refer to section below).

Software Support
----------------

The ADI ACE application provides a ‘plug and play’ evaluation experience, enabling users to get up and running quickly with the product evaluation board. ACE can configure the embedded software on supported controller boards and provides a quick and easy way to get setup, configure the board and perform data capture and analysis and/or waveform generation. For ACE installation and documentation instructions see www.analog.com/ace. Make sure to follow the instructions to install the necessary evaluation board plug-in support.

-  If the machine that ACE is installed on has internet access, you can find/install/update plug-ins directly from the ACE application. For environments without internet access, you can download these plug-ins from the previous link to portable storage and install them into ACE.
-  Note: Product specific documentation for the evaluation software can be found within the ACE plug-in.

The controller board supported by ACE with this product evaluation board is the ZedBoard.

System Operational Constraints
------------------------------

Sampling Frequency
~~~~~~~~~~~~~~~~~~

The following table illustrates the maximum sampling rates that can be achieved based on the device configuration. Note that the FPGA SPI engine only supports Zone 2 data transfers from the AD4630/AD4030.

\**Table 11. Maximum sampling rate by device configuration **^ Clocking Mode ^ Lane Mode (per channel) ^ Data Rate ^ Data format ^ Max sampling rate ^ \| SPI \| 1 \| Single (SDR) \| 32-bit \| 1.75 MSPS (**\ note 1\ **) \| \| ::: \| ::: \| SDR \| 24-bit \| 2 MSPS \| \| ::: \| ::: \| Dual (DDR) \| 32 or 24-bit \| 2 MSPS \| \| ::: \| 2 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \| ::: \| 4 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \| Echo Clock \| 1 \| SDR \| 32-bit \| 1.75 MSPS (**\ note 1\ **) \| \| ::: \| ::: \| SDR \| 24-bit \| 2 MSPS \| \| ::: \| ::: \| DDR \| 32 or 24-bit \| 2 MSPS \| \| ::: \| 2 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \| \| ::: \| 4 \| SDR or DDR \| 32 or 24-bit \| 2 MSPS \|**\ Note 1*\*: The sampling rate in Single lane, 32-bit output formats in SDR mode are limited by the FPGA SPI engine. This is not a limitation of the AD4630/AD4030 device.

Software Developers Guide
-------------------------

Analog Devices supports the development of custom applications using the EVAL-AD4X30-XX system and are described in the :doc:`AD463x and AD403x Developer's Guide </wiki-migration/resources/eval/ad4630-24-eval-board/ad4630-24-developer-guide>`

.. tip::

   Visit :doc:`AD463x and AD403x Developer's Guide </wiki-migration/resources/eval/ad4630-24-eval-board/ad4630-24-developer-guide>` for an overview of the additional software drivers that are provided with the evaluation system


Evaluation Board Support and Troubleshooting
--------------------------------------------

Technical Support
~~~~~~~~~~~~~~~~~

| Technical support for the evaluation board hardware and software can be obtained by posting a question to ADI's :ez:`EngineerZone <data_converters/precision_adcs>` technical support community for precision ADCs.
| The evaluation board schematic and other board files can be found on the :adi:`EVAL-AD4630-16FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-16.html>`, :adi:`EVAL-AD4630-24FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4630-24.html>` & :adi:`EVAL-AD4030-24FMCZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4030-24.html>` web pages.

Troubleshooting
~~~~~~~~~~~~~~~

A troubleshooting guide can be found at: :doc:`Troubleshooting Guide for ADI Kuiper Linux for ACE Evaluation </wiki-migration/resources/tools-software/linux-software/adi-kuiper_ace_troubleshooting>`. The latter covers some tips related to ZedBoard startup and the SD card containing the Kuiper Linux image.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/eval-ad4630-16_top.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/cb-ad464030-24fmcz_top-evaluation-board.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/52675_2.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adj.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/20220509_112436.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ad4630_ref_ckt.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/eval-ad4630-24_clk_ckt.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ad4630_fda_ckt.svg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ad4630_dual_buf_ckt.svg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ad4630_cascaded_buf_fda_ckt.svg
   :width: 800px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ad4630_direct_drive_ckt.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/d_ad4630-24_setup.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/powertree.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/reference2.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/clock_diagram.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/differential.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/vocm.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/single_ended_config1.png
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/config2.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/config3.png
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/ad4630_direct_drive_ckt.png
   :width: 600px
