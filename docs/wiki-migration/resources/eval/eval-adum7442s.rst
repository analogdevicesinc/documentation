ADuM7442S Evaluation Board User Guide
=====================================

| 
| ===== Preface ===== This wiki site includes information about the :adi:`EVAL-ADUM7442S <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADUM7442S.html>`; the evaluation board for the :adi:`adum7442S`.

The :adi:`adum7442s` data sheet provides a significant amount of information to aid in understanding of the device and can assist in the evaluation process. The data sheet along with this user guide and supporting linked files found in the Helpful Documents and ADuM7442S Evaluation Board Files sections below should be consulted when using the evaluation board.

| 
| ===== Evaluation Board Features =====

-  Access to all 4 data channels
-  Multiple connection options
-  Ability to power each side of isolator independently
-  User configurable load options for the input and output channels
-  Support for Tektronix active probes
-  Installed with ADuM7442AF-EMX engineering unit (same form, fit and function over full temp range as flight units)

| 
| ===== Helpful Documents =====

-  :adi:`ADuM7442S Data Sheet </media/en/technical-documentation/data-sheets/ADUM7442S.pdf>`
-  :adi:`"Bits Per Second Make My Head Hertz" <analog-dialogue/raqs/raq-issue-101.html>`, *Analog Dialogue Article, Rarely Asked Questions - Issue 101, January 2014*
-  :adi:`an-1109` Application Note, *Recommendations for Control of Radiated Emissions with iCoupler Devices*

| 

ADuM7442S Evaluation Board Files
--------------------------------

-  ADuM7442S Evaluation Board Schematic Rev A : `02_043503-01-a-1_wiki.pdf <https://wiki.analog.com/_media/resources/eval/02_043503-01-a-1_wiki.pdf>`__
   \* ADuM7442S Evaluation Board Assembly Rev B : `01-043503-01-b-1_wiki.pdf <https://wiki.analog.com/_media/resources/eval/01-043503-01-b-1_wiki.pdf>`__
   \* ADuM7442S Evaluation Board BOM Rev A : `05_043503-a.xlsx <https://wiki.analog.com/_media/resources/eval/05_043503-a.xlsx>`__
   \* ADuM7442S Evaluation Board Gerber Files Rev B : `08_043503b.pdf <https://wiki.analog.com/_media/resources/eval/08_043503b.pdf>`__

|

General Description
-------------------

| The :adi:`EVAL-ADuM7442S <adum7442s>` (shown in Figure 1 below) supports the :adi:`adum7442s` 25MBPS Space Grade Quad Channel Digital Isolator. The evaluation board provides access to all 4 channels, support for signal fanout and loopback as well as optimal bypass capacitance. Signals can be brought onto the board by the edge-mounted SMA connectors or wired directly by utilizing unpopulated header positions. Decoupled terminal blocks are provided for power connections along with support for edge-mounted SMA connectors. Compatibility with Tektronix active probes is provided by the inclusion of 200 mil header positions.
| The board follows best printed circuit board (PCB) design practices for 4-layer boards, including a full power and ground plane on each side of the isolation barrier. While the PCB does implement a distributed capacitive bypass (consisting of closely spaced power and ground planes on the inner layers) to minimize noise and EMI transmission, no other mitigation design features are included. In cases of high speed operation or when ultralow emissions are required, please refer to the :adi:`an-1109` Application Note for additional board layout techniques.

| 
| |image1|
|

.. container:: centeralign

   Figure 1. EVAL-ADuM7442S


   | 

Evaluation Board Circuitry
--------------------------

Connectors
~~~~~~~~~~

The PCB provides support for three types of interconnections:

-  SMA edge-mounted connectors
-  Through-hole signal ground pairs
-  Terminal blocks for power connections

With these three options, both temporary and permanent connections to the board can easily be made.

SMA connectors are provided for each Data I/O Channel with positions available for V\ :sub:`DD1` and V\ :sub:`DD2` power supplies. The Data I/O Channel SMA connectors are low profile, provide an excellent mechanical connection and support 50Ω coaxial cabling. Depending on cabling used for the I/O, a SMA to BNC adapter may be required for connecting to standard lab equipment.

P1 and P2 terminal blocks are provided for power connection although power can be wired directly to the PCB via the P9 and P10 through-hole connectors. Each through-hole pair provides a power ground pair with power on the Pin 1 hole. The pin spacing of each through-hole connector is 200 mils between centers. This matches the pin spacing required for Tektronix active scope probes. If a scope probe connection is desired, the header (Samtec Part # MTSW-202-12-G-S-730) shown in Figure 2 below can be soldered into the through-hole positions. Note that the signal pin must be trimmed to match the height requirement of the probe.

|

| |image2|
|

.. container:: centeralign

   Figure 2. Tektronix Scope Probe Header


Power Input
~~~~~~~~~~~

| Each side of the :adi:`adum7442s` iCoupler isolator requires an off-board power source. The power supplies for each side of the isolator can be common or independent, depending on the requirements of the application. Refer to the :adi:`adum7442s` data sheet for proper voltage ranges and combinations.
| When common-mode voltages are not present, a single supply and ground can be shared for both sides of the part (across the isolation barrier). This is particularly useful for functional testing of the device. If common-mode voltages are to be applied across the isolation barrier, independent power supplies must be provided for each side of the isolator.
| A ground plane and a power plane are present on Layer 2 and Layer 3 of the PCB on each side of the isolation barrier. Power connects to V\ :sub:`DD1A` and V\ :sub:`DD1B` for Side 1 and to V\ :sub:`DD2A` and V\ :sub:`DD2B` for Side 2. The A and B power pins on each side cannot be powered separately.

Data I/O Structures
~~~~~~~~~~~~~~~~~~~

| Each data channel has a variety of structures to help configure, load and monitor both the input and output. Figure 3 below shows one of the data paths from an external connection to the DUT pin. Each channel has similar connections.
| Starting at the external connection, the signal path is

-  Edge-mounted SMA Connector.
-  Two standard 0805 pad layouts are provided with 100Ω resistors installed on the input side of the channel. This combined resistance of 50Ω provides a termination for coaxial cabling and standard lab equipment.
-  A standard 0805 pad layout with a 0Ω resistor installed that allows the coaxial and termination structures to be connected to the rest of the signal path.
-  A 0603 pad layout between the signal and ground where a load capacitor or resistor can be installed.
-  A populated 2-pin header provides a signal ground pair that can be used for clip leads or for shorting a channel to ground temporarily.
-  There are groupings of three open through holes consisting of a signal and two ground connections. These holes can be used for hardwiring signal wires into the PCB or for installing a header (Samtec Part # MTSW-202-12-G-S-730) that will accept a Tektronix active probe (see Figure 2).
-  A 0805 pad layout between the signal path and V\ :sub:`DDX` can be used for installing a pull-up resistor.
-  Pads to the adjacent channels are provided to allow permanent connection of adjacent channels. Inputs can be fanned out to several channels or inputs and outputs can be connected together to allow signals to loopback.

| 
| |image3|
|

.. container:: centeralign

   Figure 3. Configuration and Monitoring Structures (Showing a Datapath from an External Connection to the DUT Pin)

   | Note : The numbered components in this Figure correspond to the descriptions in the Data I/O Structures Section above.


| ====Bypass On The PCB====

| Several positions and structures are provided that result in optimum bypass of the evaluation board. 10uF 0805 capacitors are installed at the power connectors (with options for through-hole capacitors if desired) to compensate for long cables to the power supply. For isolator decoupling, .1uF 0603 capacitors are installed on the top side of the PCB at each V\ :sub:`DDXX` pin.
| A distributed capacitive bypass (consisting of tightly coupled power and ground planes on the inner layers) is implemented on the PCB to supplement the standard bypass capacitors. This helps to minimize noise and EMI transmission without using complex design features.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/eval-adum7442s.png
   :width: 450px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/tek_active_probe.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/data_i_o_structure.png
   :width: 700px
