AD9574 Evaluation Board User Guide
==================================

Evaluation Board Features
-------------------------

-  Simple power connection using 6 V wall adapter and on-board voltage regulators

   -  Regulator easily bypassed for power measurements

-  12 ac-coupled SMA connectors for outputs
-  SMA input connectors for

   -  2 single-ended reference clock inputs
   -  Reference monitor clock input

-  Prepopulated 25MHz CMOS XOs for asynchronous operation
-  On-board jumpers for easy configuration of pin programmable functions
-  Status LEDs for diagnostic signals
-  Easy access to digital I/O and diagnostic signals via 12 pin header

Equipment Needed
----------------

-  Reference oscillator or signal generator (optional)
-  Other evaluation board to be clocked or test equipment

   -  Oscilloscope, spectrum analyzer, phase noise analyzer

-  SMA cables (50 Ω)
-  6 V wall supply (provided)
-  USB cable (provided)

Online Resources
----------------

Documents Needed

-  :adi:`AD9574 data sheet <static/imported-files/data_sheets/AD9574.pdf>`

General Description
-------------------

--------------

The :adi:`AD9574` evaluation board is a compact, easy-to-use platform for evaluating all features of the :adi:`AD9574`. The :adi:`AD9574` provides a multiple output clock generator function comprising of a dedicated PLL core optimized for Ethernet and gigabit line card applications. Configuring the :adi:`AD9574` for a particular application requires only the connection of external pull-up or pull-down resistors to the appropriate pin program reader pins (PPRx). These pins provide control of the internal dividers for establishing the desired frequency translations, clock output functionality, and input reference functionality. Connecting an external 19.44 MHz or 25 MHz oscillator to one or both of the REF0_P/REF0_N or REF1_P/REF1_N reference inputs results in a set of output frequencies prescribed by the PPRx pins. Connecting a stable clock source (8 kHz/10 MHz/19.44 MHz/25 MHz/38.88 MHz) to the monitor clock input enables the optional monitor circuit providing quality of service (QoS) status for REF0 or REF1.

|

.. container:: centeralign


|image1|

   |
   
   .. container:: centeralign

      //Figure 1. AD9574/PCBZ //

   


Evaluation Board Hardware
-------------------------

--------------

The following instructions are for setting up the physical connections to the AD9574/PCBZ evaluation board.

Power Connections
~~~~~~~~~~~~~~~~~

Connect the included 6V wall supply to P500 to power all of the necessary on board components. Ensure the P501 jumper is connected between pins 1 and 2 and P502 is connected between pins 1 and 2. Alternatively, the user may remove the jumper at P502 and connect an external 3.3V supply to pin 2 and pin 3 (GND).

Signal Connections
~~~~~~~~~~~~~~~~~~

Reference Inputs (REFx)
^^^^^^^^^^^^^^^^^^^^^^^

| The AD9574/PCBZ allows for the reference inputs to be clocked by one of two crystal oscillators (XO) at Y202 and Y204 or via single ended SMA connectors J217 and J215. The default signal path is to use 25MHz CMOS XOs for both REF0_P and REF1_P.
| The following board modifications from the default BOM are required to use the SMA reference input connectors to supply a differential reference instead of the 25MHz XOs:

-  Remove R217, R218, R224, and R225
-  Place C221, C222, C226, and C227

| 
| The following board modifications from the default BOM are required to use the SMA reference input connectors to supply an external single ended CMOS reference input instead of the 25MHz XOs:

-  Remove R214, R217, R218, R221, R224, R225, T201 and T202
-  Place R212, R219, C221, C222, C226, and C227 with 0Ω resistors.

| 
|

.. important::

   Although the AD9574 evaluation board has the footprint for two crystal resonators Y201 and Y203, the AD9574 is not specified to work with crystal resonators and their usage in conjunction with the AD9574 is not recommended


Monitor Clock Input (MCLK_x)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The AD9574/PCBZ provides a signal path to the MCLK_x inputs using SMA connector J216. The default BOM configuration allows for a 3.3V single ended CMOS signal to be applied to SMA connector J216 with the monitor clock input set to differential using the PPR6 biasing jumpers.
| The following board modifications from the default BOM are required to use a single ended 3.3V CMOS signal with the monitor clock set to a single ended receiver:

-  Replace C231 0Ω resistor.

| 
| The following board modifications from the default BOM are required to convert a single ended signal to differential with the monitor clock receiver set to a differential receiver:

-  Remove R226 and R226
-  Place balun T203

Pin Programming and Jumper Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9574/PCBZ contains jumpers to bias the following pins on the :adi:`AD9574`:

-  PPRx
-  REF_SEL
-  REFMON

The following subsections describe the various configuration options for these pins.

PPRx
^^^^

| The AD9574 makes use of seven PPRx pins to configure the device. Internal circuitry scans the PPRx pins for the presence of resistor terminations and configures the device accordingly. The array of jumper headers near the bottom of the evaluation board allow for easy configuration of the 7 PPR pin terminations. A PPRx pin scan occurs automatically as part of the power-on reset sequence or following assertion of the RESET pin. Each PPRx pin controls a specific function or functional block within the device as defined in **Table 1**.
| **Table 1. PPRx Pin Function and Jumper Assignments**
| ^Mnemonic ^Assigned Evaluation Board Jumpers ^Function Assignment ^

==== ========= =================================================
PPR0 P402-P404 Reference input configuration
PPR1 P406-P408 Frequency translation settings
PPR2 P410-P412 OUT0_x and OUT1_x configurations
PPR3 P414-P416 OUT4_x and OUT5_x configurations
PPR4 P418-P420 OUT6_x configuration
PPR5 P422-P424 Reference clock frequency monitor error threshold
PPR6 P426-P428 Monitor clock (MCLK) input configuration
==== ========= =================================================

| Each set of 3 jumpers allows for the user to configure various PPRx pins to one of 8 states. These states are defined in **Table 2**.
| **Table 2. PPRx States**
| ^State ^Resistance ^Terminus ^

= ===== ===
0 820Ω  GND
1 1.8kΩ GND
2 3.9kΩ GND
3 8.2kΩ GND
4 820Ω  VDD
5 1.8kΩ VDD
6 3.9kΩ VDD
7 8.2kΩ VDD
= ===== ===

There are three headers, each 3 pins wide, to select the 8 states listed in **Table 2**. **Figure 2** shows a layout capture of the available jumpers for a single PPRx pin. **Figure 3** shows an example configuration to set PPR0 to state 0.

|

.. container:: centeralign


|image2|

   |
   
   .. container:: centeralign

      //Figure 2. PPRx Jumper Configuration //

   


|

.. container:: centeralign


|image3|

   |
   
   .. container:: centeralign

      //Figure 3. Example Configuration for State 0 //

   


Note that only two jumpers are needed to correctly terminate each PPRx pin; one to set the resistance value and one to terminate the resistance to VCC or GND. Please refer to the :adi:`AD9574` datasheet or page 3 of the evaluation board schematic for more information about the available settings for each PPRx pin.

REF_SEL and REFMON
^^^^^^^^^^^^^^^^^^

| The REF_SEL and REFMON pins are tied low or high via jumpers P101 and P102 respectively.*\* Table 3*\* shows the functions of these pins.
| **Table 3. REF_SEL and REFMON Settings**
| ^Pin Name ^Jumper ^Connected to GND ^Connected to VCC ^

======= ==== ========================= ========================
REF_SEL P101 REF0                      REF1
REFMON  P102 Reference monitor disable Reference monitor enable
======= ==== ========================= ========================

Status LEDs
~~~~~~~~~~~

There are 5 status LEDs:

-  DS102 reflects the state of REF_SW output pin: high when a reference switch is in progress
-  DS103 reflects the state of REF_ACT output pin: low when REF0 is the active reference and high when REF1 is the active reference
-  DS104 reflects the state of REF_FHI output pin: high when the reference frequency is above the upper threshold limit
-  DS105 reflects the state of REF_FLO output pin: high when the reference frequency is below the lower threshold limit
-  DS106 reflects the state of LD output pin: low when the PLL is unlocked and high when the PLL is locked

Quick Start Guide
-----------------

--------------

The quick start section covers simple PLL operation to lock the :adi:`AD9574` PLL and output various frequencies on OUT0 through OUT6. See the :adi:`AD9574` datasheet for a detailed explanation of the various :adi:`AD9574` features.

**Table 4** describes a summary of one possible operating mode of the :adi:`AD9574` which is setup used for this quick start guide.

**Table 4. Quick Start Summary**

=================================== ==================
Parameter                           Value
=================================== ==================
Input Frequency and Logic Type      25MHz, 3.3V CMOS
PLL VCO Frequency                   2500MHz
Reference Doubler Enable/Disable    Disable
Reference Monitor Threshold         +/- 50ppm
MCLK Input Frequency and Logic Type 10MHz 3.3V CMOS
Reference Doubler Enable/Disable    Disable
OUT0 Frequency and Logic Type       25MHz 3.3V CMOS
OUT1 Frequency and Logic Type       25MHz 3.3V CMOS
OUT2 Frequency and Logic Type       156.25MHz HSTL
OUT3 Frequency and Logic Type       156.25MHz HSTL
OUT4 Frequency and Logic Type       100MHz HSTL
OUT5 Frequency and Logic Type       125MHz HSTL
OUT6 Frequency and Logic Type       33.33MHz 3.3V CMOS
=================================== ==================

Use the following steps to lock the AD9574 PLL to the on board 25MHz XO and output the frequencies listed in **Table 4**.

-  Connect the 6V wall supply to P500 with jumpers P501 and P502 set to short pins 1 and 2.
-  Connect a 10MHz 3.3V CMOS signal to J216
-  Set the following PPRx states using the jumpers outlines in **Table 1**:

   -  PPR0: State 0

      -  PPR1: State 0
      -  PPR2: State 3
      -  PPR3: State 0
      -  PPR4: State 7
      -  PPR5: State 4
      -  PPR6: State 6

The <fc #FF0000>red</fc> LED labeled DS106 is connected to the LD pin through a buffer and should be illuminated indicating that the AD9574 is now in a locked condition.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9574/ad9574_cropped.jpg
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9574/pprx_1.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9574/pprx_2.png
   :width: 200px
