DEMO MANUAL EVAL-ADBMS1818
==========================

**ADBMS1818 Daisy Chain isoSPI Battery-Stack Monitor**

DESCRIPTION
-----------

Demonstration circuit EVAL_ADBMS1818 is a multicell battery stack monitor featuring the ADBMS1818, an 18-cell monitor on the EVAL_ADBMS1818. Multiple boards can be linked through a 2-wire isolated serial interface (isoSPI) to monitor any number of cells in a stack. The demo circuit also features reversible isoSPI enabling a fully redundant communication path.

The EVAL_ADBMS1818 can communicate to a PC by connecting directly to a DC2026 Linduino® One. The DC2026 must be loaded with the appropriate program (called a “sketch”) to control the battery stack monitor IC and receive data through a USB serial port. The DC2792/DC1941 can be connected to the DC2026 to provide a fully isolated isoSPI interface to the EVAL_ADBMS1818.

Design files for this circuit board are available at `www.analog.com/en/products/adbms1818.html <http://www.analog.com/en/products/adbms1818.html>`_

Evaluation board Schematic is available here: `eval-adbms1818_schematic.pdf <https://wiki.analog.com/_media/resources/eval/eval-adbms1818_schematic.pdf>`_

PERFORMANCE SUMMARY
-------------------

Specifications are at TA = 25°C

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_1.png
   :width: 400px

HARDWARE SETUP
--------------

Wiring J4 Connector
~~~~~~~~~~~~~~~~~~~

The EVAL_ADBMS1818 demo circuits (boards) have different connector pinouts. It is critical that the correct wiring is followed or there is a risk of damaging the demo board.

When connected to a battery stack, power for the EVAL_ADBMS1818 is provided by the cell group being monitored. To connect the cell group, separate the screw-terminal block section from the J4 connector. Then, insert the cell-voltage connections or resistors into the screw-terminal clamping contacts. These connections provide the power and input stimulus for the battery stack monitor IC.

Cell-voltages are wired to J4 starting from position 1 (most negative potential of the group). Please reference the appropriate demo board J4 connector pinout in Tables 1 and 2.

Alternatively, resistors can be used to simulate battery cell-voltages. 100Ω 0.5W or equivalent resistors are recommended because 100Ω (or lower values) typically will not induce measurement errors and the 0.5W (or greater rating) will keep the resistor temperatures low preventing power dissipation damage.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_2.png
   :width: 400px

EVAL_ADBMS1818 18 Resistor Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Carefully connect eighteen 100Ω resistors between each screw-terminal block clamping contact from position 1 to position 19 as shown in Table 2, EVAL_ADBMS1818 J4 Pinout. Provide a stack-equivalent power supply connection to position 19 (positive) and position 1 (negative). The power supply may be adjusted to provide the desired nominal cell-voltage (e.g. 59.4V will be 3.3V per cell).

JUMPERS
-------

The demo board jumpers must be set to match the desired mode of operation. The jumpers enable the Discharge Timer and select the serial communication mode to the battery stack monitor IC.

ISOMD Jumpers JP1–JP3
~~~~~~~~~~~~~~~~~~~~~

0: Set jumpers to 0 for standard SPI communication to the IC through the J3 connector.

1: Set jumpers to 1 for isoSPI communication to the IC through either the J1 or J2 connector.

SWTEN Jumper JP4
~~~~~~~~~~~~~~~~

0: Set jumpers to 0 for Discharge Timer disable.

1: Set jumpers to 1 for Discharge Timer enable.

EVAL_ADBMS1818 SERIAL INTERFACE OPTIONS
---------------------------------------

The EVAL_ADBMS1818 has several communication options. The DC2026 Linduino One provides a USB-to-SPI interface, and is ideal to interface from a PC to any SPI device. In this case, the DC2026 SPI interface can connect directly to the EVAL_ADBMS1818 (see section entitled DC2026 to EVAL_ADBMS1818 SPI Connection for details). Alternately, the DC2026 SPI can be translated to isoSPI via the DC2792 or DC1941 demo boards. The DC2792 is a dual master isoSPI demo board which can be connected as a typical single-ended isoSPI bus master or to both ends of a reversible con-figuration with two isoSPI bus masters. The DC1941 can be connected as a typical single-ended isoSPI bus master.

USING OTHER SPI MASTER BOARDS
-----------------------------

When a different SPI master microcontroller board is used instead of the DC2026, more components or equipment are required to properly interface to the demo boards. Here are the requirements:

SPI MISO Line
~~~~~~~~~~~~~

Most SPI master microcontroller boards will not have a SPI MISO line pull-up. A 5kΩ pull-up resistor is required on the SPI MISO line because the battery stack monitor IC SDO is an open drain NMOS output pin. Otherwise, the SPI MISO line will be floating where the SPI readback of each byte will typically appear as no response or all ones or 0xFFs. There are several places where the pull-up resistor can be installed. On the EVAL_ADBMS1818, a 0603 size 5kΩ resistor can be soldered onto R8 or on the microcontroller board, a 5kΩ resistor can be added between the micro-controller SPI MISO line and the microcontroller VCC pin.

isoSPI IC Power
~~~~~~~~~~~~~~~

A separate 5V power supply is required when using a different SPI master microcontroller board. The DC2026 J1 header provides power for the isoSPI IC through the 14-pin ribbon cable into the DC2792 J1 header or the DC1941 J2 header. Refer to demo manual DC2792A or demo manual DC1941D for external power supply instructions.

EVAL_ADBMS1818 SPI CONNECTION
-----------------------------

An SPI connection begins with the SPI master con-nected to the first (or “bottom”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained onto the isoSPI bus. Communication begins from the first (or “bottom”) EVAL_ADBMS1818 then to the next “upper” EVAL_ADBMS1818 then finally to the last (or “top”) EVAL_ADBMS1818.

Figure 1 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the EVAL_ADBMS1818 in SPI mode. This EVAL_ADBMS1818 is the first (or “bottom”) board of the stack.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the “bottom” EVAL_ADBMS1818 J3 header.

b. Set JP1–JP3 to 0 for SPI communication.

c. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

3. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack. More EVAL_ADBMS1818 “upper” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “bot-tom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector to the next “upper” or “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector.

b. Set the next “upper” or “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

4. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage connections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used.

a. Plug the screw-terminal blocks into the J4 cell-voltage connectors.

5. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_3.png

**Figure 1. DC2026 SPI Connection to the “Bottom” EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

DC2792 TO EVAL_ADBMS1818 TYPICAL ISOSPI CONNECTION
--------------------------------------------------

A typical isoSPI connection begins with the isoSPI master connected to the first (or “bottom”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained onto the isoSPI bus. Communication begins from the first (or “bottom”) EVAL_ADBMS1818 then to the next “upper” EVAL_ADBMS1818 then finally to the last (or “top”) EVAL_ADBMS1818.

Figure 2 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the DC2792 Dual Master isoSPI demo board.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the DC2792 J1 header.

3. Connect the DC2792 to the EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the first (or “bottom”) board of the stack.

a. Connect a RJ45 patch cable from the DC2792 J2 MAIN RJ45 connector to the “bottom” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector. b. Set the “bottom” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

4. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack. More EVAL_ADBMS1818 “upper” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “bot-tom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector to the next “upper” or “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector.

b. Set the next “upper” or “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

5. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage connections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used.

a. Plug the screw-terminal blocks into the J4 cell-voltage connectors.

6. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_4.png

**Figure 2. DC2792 Typical isoSPI Connection to the “Bottom” EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

DC2792 TO EVAL_ADBMS1818 REVERSE ISOSPI CONNECTION
--------------------------------------------------

A reverse isoSPI connection begins with the isoSPI master connected to the last (or “top”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained onto the isoSPI bus. Communication begins from the last (or “top”) EVAL_ADBMS1818 then to the next “lower” EVAL_ADBMS1818 then finally to the first (or “bottom”) EVAL_ADBMS1818.

Figure 3 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the DC2792 Dual Master isoSPI demo board.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the DC2792 J1 header.

3. Connect the DC2792 to the EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack.

a. Connect a RJ45 patch cable from the DC2792 J2 MAIN RJ45 connector to the “top” EVAL_ADBMS1818 J1 iso-SPI B RJ45 connector.

b. Set the “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

c. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

4. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the first (or “bottom”) board of a two-board stack. More EVAL_ADBMS1818 “lower” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector to the next “lower” or “bottom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector.

b. Set the next “lower” or “bottom” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

5. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage con-nections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used.

a. Plug the screw-terminal blocks into the J4 cell-voltage connectors.

6. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_5.png

**Figure 3. DC2792 Reverse isoSPI Connection to the “Top” EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

DC2792 TO EVAL_ADBMS1818 REDUNDANT ISOSPI CONNECTION
----------------------------------------------------

A redundant isoSPI connection begins with the primary (or “main”) isoSPI master connected to the first (or “bottom”) EVAL_ADBMS1818 and has a backup auxiliary (or “aux”) isoSPI master connected to the last (or “top”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained between the two isoSPI masters on the isoSPI bus. Primary (or “main”) communication begins from the first (or “bot-tom”) EVAL_ADBMS1818 then to the next “upper” EVAL_ADBMS1818 then finally to the last (or “top”) EVAL_ADBMS1818. The backup auxiliary (or “aux”) communication begins in the reverse direction to provide coverage when a possible isoSPI daisy-chain break occurs.

Figure 4 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the DC2792 Dual Master isoSPI demo board.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the DC2792 J1 header.

3. Connect the DC2792 primary (or “main”) isoSPI master to the first (or “bottom”) EVAL_ADBMS1818 board of the stack.

a. Connect a RJ45 patch cable from the DC2792 J2 MAIN RJ45 connector to the “bottom” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector.

b. Set the “bottom” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

c. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

4. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack. More EVAL_ADBMS1818 “upper” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “bottom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector to the next “upper” or “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector.

b. Set the next “upper” or “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

5. Connect the DC2792 auxiliary (or “aux”) isoSPI master to the last (or “top”) EVAL_ADBMS1818 board of the stack.

a. Connect a RJ45 patch cable from the DC2792 J3 AUX RJ45 connector to the “top” EVAL_ADBMS1818 J1 iso-SPI B RJ45 connector.

6. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage connections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used. Plug screw-terminal blocks into the J4 cell-voltage connectors.

7. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_6.png

**Figure 4. DC2792 Redundant isoSPI Connections to the “Bottom” and “Top”EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

DC1941 ISOSPI MASTER SETTINGS
-----------------------------

The DC1941 jumpers must first be properly set to inter-face between DC2026 and EVAL_ADBMS1818.

Refer to Demo Manual DC1941D for jumper setting details.

Figure 5 shows the proper board settings.

1. JP2: VCC = DC590.

2. JP3: ENABLE = EN.

3. JP4: SLOW = 0.

4. JP5: MODE = MASTER.

5. JP6: VCCS = VCC.

6. JP7: PHA = 1.

7. JP8: POL = 1.

8. JP9, JP10: VTH = VTH2.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_7.png

**Figure 5. DC1941 isoSPI Master Mode Jumper Settings**

DC1941 TO EVAL_ADBMS1818 TYPICAL ISOSPI CONNECTION
--------------------------------------------------

A typical isoSPI connection begins with the isoSPI master connected to the first (or “bottom”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained onto the isoSPI bus. Communication begins from the first (or “bottom”) EVAL_ADBMS1818 then to the next “upper” EVAL_ADBMS1818 then finally to the last (or “top”) EVAL_ADBMS1818.

Figure 6 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the DC1941 isoSPI demo board.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the DC1941 J2 header.

3. Refer to the DC1941 isoSPI Master Settings section of this demo manual to properly setup the DC1941.

4. Connect the DC1941 to the EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the first (or “bottom”) board of the stack.

a. Connect a RJ45 patch cable from the DC1941 J1 RJ45 connector to the “bottom” EVAL_ADBMS1818 J2 iso-SPI A RJ45 connector.

b. Set the “bottom” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

c. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

5. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack. More EVAL_ADBMS1818 “upper” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “bot-tom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector to the next “upper” or “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector.

b. Set the next “upper” or “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

6. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage con-nections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used.

a. Plug the screw-terminal blocks into the J4 cell-voltage connectors.

7. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_8.png

**Figure 6. DC1941 Typical isoSPI Connection to the “Bottom” EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

DC1941 TO EVAL_ADBMS1818 REVERSE ISOSPI CONNECTION
--------------------------------------------------

A reverse isoSPI connection begins with the isoSPI master connected to the last (or “top”) EVAL_ADBMS1818. Additional EVAL_ADBMS1818 boards can be daisy-chained onto the isoSPI bus. Communication begins from the last (or “top”) EVAL_ADBMS1818 then to the next “lower” EVAL_ADBMS1818 then finally to the first (or “bottom”) EVAL_ADBMS1818.

Figure 7 shows the following connections for two boards on a stack interfaced to a PC:

1. Connect a USB cable from the PC USB port to the DC2026 J5 connector.

2. Connect the DC2026 to the DC1941 isoSPI demo board.

a. Connect a 14-pin ribbon cable from the DC2026 J1 header to the DC1941 J2 header.

3. Refer to the DC1941 isoSPI Master Settings section of this demo manual to properly setup the DC1941.

4. Connect the DC1941 to the EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the last (or “top”) board of a two-board stack.

a. Connect a RJ45 patch cable from the DC1941 J1 RJ45 connector to the “top” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector.

b. Set the “top” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

c. JP4 can be 0 or 1 depending if the Discharge Timer function is being used.

5. Connect or daisy-chain the EVAL_ADBMS1818 to another EVAL_ADBMS1818 in isoSPI mode. This EVAL_ADBMS1818 is the first (or “bottom”) board of a two-board stack. More EVAL_ADBMS1818 “lower” boards can be daisy-chained together in the same manner.

a. Connect a RJ45 patch cable from the “top” EVAL_ADBMS1818 J2 isoSPI A RJ45 connector to the next “lower” or “bottom” EVAL_ADBMS1818 J1 isoSPI B RJ45 connector.

b. Set the next “lower” or “bottom” EVAL_ADBMS1818 JP1–JP3 to 1 for isoSPI communication.

6. CAUTION! Prevent damage to the EVAL_ADBMS1818. Refer to Tables 1 and 2 and confirm that the cell-voltage con-nections to screw-terminal block matches the J4 pinout of the EVAL_ADBMS1818 version being used.

a. Plug the screw-terminal blocks into the J4 cell-voltage connectors.

7. Refer to the Software Setup section of this demo manual to properly setup the PC with the Arduino IDE software to allow communication to the EVAL_ADBMS1818 boards.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_9.png

**Figure 7. DC1941 Reverse isoSPI Connection to the “Top” EVAL_ADBMS1818 in a Two-Board EVAL_ADBMS1818 Stack**

SOFTWARE SETUP
--------------

The EVAL_ADBMS1818 can be controlled by the DC2026 Linduino One board. The DC2026 is part of the Arduino compatible Linduino platform that provides example code that will demonstrate how to control the multicell battery stack monitor ICs. Compared to most Arduino compatible microcontroller boards, the DC2026 offers conveniences such as an isolated USB connection to the PC, built-in SPI MISO line pull-up to properly interface with the battery stack monitor IC open drain SDO, and an easy rib-bon cable connection for SPI communication through the EVAL_ADBMS1818 14-pin QuikEval J3 connector.

Arduino IDE Setup
~~~~~~~~~~~~~~~~~

1. Download then install the Arduino IDE onto the PC. Detailed instructions can be found at `www.analog.com/en/products/LTC6820.html <http://www.analog.com/en/products/LTC6820.html>`_ under the quick start tab.

2. Set the Arduino IDE to open BMS Sketchbooks. From within the Arduino IDE, click on File menu select Preferences. Then under Sketchbook location: select Browse, and locate the path to the extracted bmsSketchbookBeta.zip file that was provided by ADI.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_10.png

.. _software-setup-1:

SOFTWARE SETUP
~~~~~~~~~~~~~~

3. Close then re-open the Arduino IDE to enable the use of the Sketchbook Location that was previously set.

4. Select the correct COM port to allow communication to DC2026 through USB. Under the Tools menu, select

Port →Select the highest number COMxx with the “✔” checkmark symbol. There may be more than one option; DC2026 is usually the highest COM port number. The PC screenshots used in this example show the DC2026 connected to COM6.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_11.png

5. Select the correct Arduino compatible microcontroller board. Under the Tools menu, select Board → Arduino/ Genuino Uno with the “l” black dot symbol.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_12.png

6. Open one of the programs or “sketches” associated with the EVAL_ADBMS1818. In this example, ADBMS1818 sketch will be opened instead of a LTC6812-1 sketch. Under the File menu, select Sketchbook → Part Number → ADI-Parts → EVAL_ADBMS1818.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_13.png

7. Upload the EVAL_ADBMS1818 sketch onto the DC2026 by clicking on the Upload button on the top left corner. When this process is completed there will be a “Done uploading” message on the bottom left corner.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_14.png

8. Open the Arduino Serial Monitor tool. Click on the Serial Monitor button on the top right corner then the Serial Monitor window will open and show on the top left corner the COMxx used.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_15.png
   :width: 200px

9. Configure the Serial Monitor to allow communication to the DC2026 through USB. On the bottom of the Serial Monitor window, set the following, starting from bottom left to bottom right:

a. Click on the Autoscroll checkbox for the “” check-mark symbol.

b. Select Both NL & CR on the left dropdown menu.

c. Select 115200 baud on the right dropdown menu.

d. As shown below, when configured correctly the EVAL_ADBMS1818 sketch menu will appear.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_16.png

APPENDIX A THE SKETCHBOOK CONTENTS
----------------------------------

The bmsSketchbook will generally contain the follow-ing folders: Libraries, Part Number, Documentation, and Utilities.

**Libraries directory:** contains a subdirectory for each IC in the sketchbook. Each subdirectory contains a .cpp and .h file. These files contain all of the constant definitions and low-level IC command implementations. Porting to a different microcontroller requires changes to some library files.

**Part Number directory:** contains example control pro-grams for each IC. Inside the Part Number folder, each BMS IC has a sketch(.ino) file that implements a control program to evaluate the functionality of the IC. This sketch allows the user to control the IC through a serial terminal and make all primary measurements. This sketch also allows for evaluation of self-test and discharge features of the IC. Generally, the name of a sketch relates to the IC’s demo board. For example, the sketch for LTC6804 is DC1942.ino, for LTC6811 it is DC2259.ino, and for ADBMS1818 it is EVAL_ADBMS1818.ino.

**Utilities directory:** contains support programs, including a program that emulates a standard Linear Technology DC590 isolated USB to serial controller.

**Documentation directory:** contains html documentation for the provided code base. Documentation for all of the BMS ICs can be accessed by opening the Linduino.html file, as found in the main sketchbook directory (shown below) and in the Documentation directory.

.. image:: https://wiki.analog.com/_media/resources/eval/eval-adbms1818_17.png

What Is A Sketch
~~~~~~~~~~~~~~~~

A “sketch” is simply another word for a microcontroller/ Linduino program. The term is generally only used when referring to Arduino based programs, as sketches have several abstractions that remove some of the complexity of a standard microcontroller(MCU) program. All sketches contains two primary functions, the setup() and the loop() function. These are in fact the only functions that are mandatory in a sketch and are almost always implemented in some form in a typical MCU program. The setup() function is run once at power on or after the MCU is reset. The setup() function generally is used to initialize the MCU peripheral circuits and to initialize all of the control variables. The loop() function is similar to a main() function that has implemented an infinite loop inside a standard C program. The code within the loop() function is typically where the primary program code is placed. The code within the loop() function will repeat infinitely.

Sketch Modifications
~~~~~~~~~~~~~~~~~~~~

Sketches can be modified to a set of applications specific requirements. All sketches are written such that the most common modifications can be made by changing the variables listed in the /\*Setup Variables \*/ table at the top of the sketch. For reference, example modifications to a DC2259 (LTC6811) sketch are shown below. These modifications are applicable to most of the available BMS ICs in the sketchbook.

Common modifications can be made by changing the Setup Variables. The most common application changes are listed below. After the variables are changed, the sketch will need to be recompiled and uploaded to the Linduino.

1. To change the number of ICs in the isoSPI network, change the TOTAL_IC variable. A number between 1 and 4 should be entered. In an application that has 2 devices in the network the modified line will look like:

::

   const uint8_t TOTAL_IC = 2;

2. Often an application may need to sample data at a rate faster than the default 500ms (2Hz). To modify the loop/ sample rate the MEASUREMENT_LOOP_TIME variable should be changed. The loop time must be entered in milliseconds and should be a number larger than 20ms. To change the loop rate to roughly 10 measurements a second the loop rate should be changed to 100mS. The modified line will look like:

::

   const uint16_t MEASUREMENT_LOOP_TIME = 100;

3. It is possible to modify which measurements fall within the loop during the Loop Measurements command. The following list are the measurements that can be looped:

::

   const uint8_t MEASURE_CELL = ENABLED; // This is ENABLED or DISABLED
   const uint8_t MEASURE_AUX = DISABLED; // This is ENABLED or DISABLED
   const uint8_t MEASURE_STAT = DISABLED; //This is ENABLED or DISABLED

By default only a cell measurement is done, as noted by MEASURE_CELL = ENABLED. What measurements are made can be changed by setting what the Measure field is equal to. To Measure Cells and the Status register but not the AUX register, the variables would be setup as shown below:

::

   const uint8_t MEASURE_CELL = ENABLED; // This is ENABLED or DISABLED
   const uint8_t MEASURE_AUX = DISABLED; // This is ENABLED or DISABLED
   const uint8_t MEASURE_STAT = ENABLED; //This is ENABLED or DISABLED

.. _appendix-a-the-sketchbook-contents-1:

APPENDIX A THE SKETCHBOOK CONTENTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. ADC conversion settings can also be modified in the Setup Variables section. The default setup is to run the ADC in ‘Normal’ mode, which has a 7kHz filter code; in this mode the ADC_OPT bit is Disabled. Typical choice for which cell to convert is ALL. Full ADC conversion programming requires setting ADC_OPT,

ADC_CONVERSION_MODE, CELL_CH_TO_CONVERT, AUX_CH_TO_CONVERT and STAT_CH_TO_CONVERT. These variables are programmed with constants listed in the LTC68xy_daisy.h file. For simplicity they are also listed below:

::

   MD_422HZ_1KHZ
   MD_27KHZ_14KHZ
   MD_7KHZ_3KHZ
   MD_26HZ_2KHZ
   ADC_OPT_ENABLED
   ADC_OPT_DISABLED  
   CELL_CH_ALL  
   CELL_CH_1and7
   CELL_CH_2and8
   CELL_CH_3and9
   CELL_CH_4and10
   CELL_CH_5and11
   CELL_CH_6and12

To set the ADC to have a 1kHz filter corner the ADC_OPT and ADC_CONVERSION_MODE variables would be changed to:

::

   ADC_OPT = ADC_OPT_ENABLED;
   ADC_CONVERSION_MODE = MD_422HZ_1KHZ;

To convert only cells 2 and 8,

::

   CELL_CH_TO_CONVERT = CELL_CH_2and8;

5. In another example, the user may want to change the undervoltage and overvoltage thresholds. Each number is based on an LSB of 100µV.

::

   //Under Voltage and Over Voltage Thresholds
   const uint16_t OV_THRESHOLD = 41000;
   // Over voltage threshold ADC Code. LSB = 0.0001
   const uint16_t UV_THRESHOLD = 30000;
   // Under voltage threshold ADC Code. LSB = 0.0001
