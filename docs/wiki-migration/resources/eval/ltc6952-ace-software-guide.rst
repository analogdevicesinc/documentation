DC2609A ACE Software User Guide
===============================

Description
-----------

Demonstration circuit 2609A features the LTC6952, an Ultralow Jitter, 4.5GHz PLL with 11 Outputs, and JESD204B Support. By default, the DC2609A is powered by two supplies. The 9V-12V supply input powers the onboard reference and VCO circuitry, along with the LTC6952 5V supply pin. The 4V-6V supply input powers the LTC6952 3.3V supply pins. A reduced power option is provided to allow the LTC6952’s output supply pins to connect to an LTC Silent Switcher® and the LTC6952 input supply pins to connect to a low noise LDO. All differential inputs and six of the differential outputs are populated with 0.5” spaced SMA connectors. These outputs are AC-coupled with 50Ω transmission lines making them suitable to drive 50Ω impedance instruments. The remaining five differential outputs are terminated with 100Ω. The LTC6952’s EZSync™ and SYSREF request functions are available via the LTC6952 SPI interface or the EZS_SRQ SMA/turret connectors. The DC2609A, DC2610A, and DC2611A SMA placement were designed for ease of connection for all multi-part synchronization and SYSREF request modes. The VTUNE and VCO SMAs can mate directly with the DC2664A VCO rider board. This option allows for a quick method to evaluate multiple VCOs. A DC2026 USB serial controller board is used for SPI communication with the LTC6952, controlled by the ACE™ software and LTC6952 Plugin.


|image1|

.. note::

   Figure 1: DC2609A Board View and Connections


Getting Started
---------------

The DC2609A is easy to set up to evaluate the performance of the LTC6952. Follow the procedure below. The ACE Software and the DC2026 are required to control the DC2609A through a personal computer (PC)

DC2026 Linduino Board Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to Figure 2. Set the JP3 jumper to the 3.3V (preferred) or 5V position. Connect the DC2026 to one of your computer’s USB ports with the included USB cable. The DC2026 has the ability to run Linduino code, refer to :adi:`Design Center <en/design-center/evaluation-hardware-and-software/linduino.html?doc=DC2609A.pdf>`.


|image2|

.. note::

   Figure 2: DC2026 Connector Locations


ACE and Plugin Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install the LTC6952 plug-in from the ACE start-up page. You can install ACE from :adi:`ACE Software Page <en/design-center/evaluation-hardware-and-software/ace-software.html>`

-  On the ACE start-up page locate and click the Plug-in Manager on the sidebar.
-  Select Available Packages from the panel second sidebar
-  Search for Board.LTC6952 and install plug-in

|image3|

.. note::

   Figure 3: ACE Plugin Search Screen


Evaluation Board Set-Up
~~~~~~~~~~~~~~~~~~~~~~~

-  Connect J30, J32, and J33 to the appropriate power supplies and apply power (see Figure 1 and the Typical DC2609A Requirements and Characteristics table).
-  Connect the DC2026 to the DC2609A with the provided ribbon cable
-  Run the ACE application. Double click the LTC6952 icon that appears on the Attached Hardware tab when the DC2026 board is connected and attached to the board. If the icon does not appear, consider re-installing the LTC6952 plug-in or try refreshing the Attached hardware icon.
-

|image4|

.. note::

   Figure 4: Attached Hardware Tab


-  Connection is automatically established with DC2026. You can navigate to board and chip view.
-  Double click the LTC6952 Board Icon and the tab shown in Figure 5 appears.
-  Double click the LTC6952 icon that appears on the LTC6952 Board tab to open the main control window shown in Figure 6

|image5|

.. note::

   Figure 5: ACE Plugin DC2609A Board View


General Software Features
~~~~~~~~~~~~~~~~~~~~~~~~~

In chip view, one can find various control features of LTC6952. One can read and control all registers which mentioned in the :adi:`LTC6952 datasheet <LTC6952>`. On board, VCO is a narrow band and must be operated in a 4 GHz region. Fpfd Fref and Fvco can be set by changing R Divider (RD) and N divider (ND) Values.

Register Hb00 can easily be read by clicking the “Check Status Register” button. Small LED icons will be lit if the register bit value is high. Stat Pin output mask register value can be set visually to reflect which information will be carried to Stat Pin Output.

The clock distribution circuit consists of eleven paths. Each path can be controlled individually. SRQEN bit, MODE, Power-down modes, divider value, digital delay, and analog delay of each channel can be modified from the chip view.

EZsync mode and SYSREF features can be controlled from the chip view. EZSync Mode, SRQ Mode, and SysRef Pulse count can be adjusted.

The main controls are available in the high-level register map shown in Figure 7. To modify registers, perform the following steps:

-  Modify registers as desired.
-  Click Apply Changes to load the modified setting to the device. This action loads the updated registers only.

By clicking Proceed to Memory Map button or Memory Map Side-By-Side button, register values can be seen.


|image6|

.. note::

   Figure 6: LTC6952 Chip View on ACE


CML OUTPUTS, OUT[10:0]
----------------------

The DC2609A has 11 CML outputs. OUT[9:0] have matching trace lengths, which are optimized for skew measurements. OUT10’s trace lengths are longer than the other outputs traces due to the shape of the DC2609A.

Six of these outputs are AC-coupled and brought out to SMAs (OUT9, OUT8, OUT5, OUT4, OUT1, and OUT0). To drive 50Ω impedance instruments connect OUTx+ to the instrument and OUTx– to a 50Ω termination, or vice versa.

The remaining five outputs (OUT10, OUT7, OUT6, OUT3, and OUT2) are terminated with a 100Ω resistor onboard. To connect these outputs to a 50Ω instrument, remove the 100Ω termination, and install the appropriate SMAs and AC blocking capacitors.

Refer to LTC6952 data sheet for differential termination options.

Typical DC2609A Requirements and Characteristics
------------------------------------------------

+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter           | Direction              | Physical Location               | Details                                                                                                                                                                                                                                 |
+=====================+========================+=================================+=========================================================================================================================================================================================================================================+
| 9V-12V Power Supply | Input                  | J30 Banana Jack                 | Powers the onboard 8V VCO, the onboard 3.3V reference, and the LTC6952 5V VCP+ supply pins. Power down onboard reference (U2) by setting jumper JP2 to position 2-3. Power down onboard VCO (U9) by setting jumper JP3 to position 2-3. |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4V-6V Power Supply  | Input                  | J32 Banana Jack                 | Powers the LTC6952 3.3V supply pins (VOUT+, VREF+, VVCO+, and VD +). Option available to power supplies from a single LDO, or an LDO and an LTC Silent Switcher.                                                                        |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GND                 | Output                 | J33 Banana Jack                 | Pair with J30 and J32                                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT9+; OUT9–        | Output                 | J3 and J4 SMA\*                 | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT8+; OUT8–        | Output                 | J5 and J6 SMA\*                 | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT5+; OUT5–        | Output                 | J19 and J20 SMA\*               | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT4+; OUT4–        | Output                 | J17 and J18 SMA\*               | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT1+; OUT1–        | Output                 | J11 and J12 SMA\*               | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT0+; OUT0–        | Output                 | J9 and J10 SMA\*                | CML, AC-Coupled, 800mVpk Differential                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT10+; OUT10–      | Output (Not Connected) | J1 and J2 SMA (N.P\ :sup:`1`)   | Onboard Differential 100Ω termination                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT7+; OUT7–        | Output (Not Connected) | J7 and J8 SMA (N.P\ :sup:`1`)   | Onboard Differential 100Ω termination                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT6+; OUT6–        | Output (Not Connected) | J21 and J22 SMA (N.P\ :sup:`1`) | Onboard Differential 100Ω termination                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT3+; OUT3–        | Output (Not Connected) | J15 and J16 SMA (N.P\ :sup:`1`) | Onboard Differential 100Ω termination                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| OUT2+; OUT2–        | Output (Not Connected) | J13 and J14 SMA (N.P\ :sup:`1`) | Onboard Differential 100Ω termination                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VCO+; VCO–          | Input (Not Connected)  | J28 and J29 SMA                 | Default: Not Connected                                                                                                                                                                                                                  |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REF+;REF–           | Input                  | J24 and J25 SMA                 |                                                                                                                                                                                                                                         |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EZS_SRQ+            | Input                  | J27 SMA /E1 Turret              | Default: Preferred Single-Ended Input                                                                                                                                                                                                   |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EZS_SRQ–            | Input                  | J26 SMA /E3 Turret              | Default: Shorted to GND                                                                                                                                                                                                                 |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ISD                 | Input                  | Test Point                      | 3.3V(Default): Device Active, set by pull-up resistor GND: Shut Down Device                                                                                                                                                             |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| STAT                | Output                 | JP1 Jumper                      | Red LED D1 illuminates when STAT pin in high state                                                                                                                                                                                      |
+---------------------+------------------------+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\*Any unused RF output must be powered down or terminated with 50Ω, or poor spurious performance may result.

:sup:`1`\ Not Populated

Troubleshooting
---------------

**If the green LEDs (D2, D3, or D4) do not illuminate:**

-  Verify J30 measures between 9V and 12V
-  Verify the JP3 and JP5 jumpers are installed correctly (refer to the DC2609A schematic sheet 3)
-  Verify the output voltages at pin 10 of U7, U8, and U11 are correct

   -  U7 = 3.3V
   -  U8 = 8V
   -  U11 = 5V

\**If the green LED (D5) does not illuminate: \*\*

-  Verify J32 measures between 4V and 6V (see the Typical DC2609A Requirements and Characteristics)
-  Verify that JP4, JP6, and JP7 jumpers are installed correctly (refer to the DC2609A schematic sheet 3)
-  Verify the voltages at jumper JP6 and JP7 are correct

   -  JP6 = 3.3V
   -  JP7 = 3.3V

\**If the red LED (D1) does not illuminate: \*\*

-  In ACE Chip View, click “Check Register Status”. STAT Output Pin should match STAT Pin Mask And Output.

\**Verify DC2609A and LTC6952 Plugin Communication: \*\*

To verify communication with the DC2609A, Go to the start page or system view page and click the button shown below.


|image7|

.. note::

   Figure 7: Attached Hardware Tab on ACE


LEDs on the Serial Interface Boards don’t light up, then perform the following steps:

-  Ensure the DC2026 is connected to the PC
-  Disconnect and Reconnect DC2026 to PC
-  Ensure DC2026 is connected to DC2609A
-  Close ACE and Restart
-  Verify the DC2026 has the DC590B Emulator Sketch loaded by contacting the factory or following these steps.

   -  `Download QuikEval™ <http://ltspice.analog.com/software/ltcqev.exe>`__
   -  Run QuickEval (Linduino connected to PC)

If QuickEval does not find a DC590B, reload the DC590 Linduino sketch To use the LTSketchbook refer to the :adi:`Linduino Design Center <en/design-center/evaluation-hardware-and-software/linduino.html?doc=DC2609A.pdf>` for instructions on how to start using Linduino

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dc2609a-board-view.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/dc2026-connector-location.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace-plugin-search-screen.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/board.ltc6952-plugin-attached-hardware-screen.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ltc6952-boardview-on-ace.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ltc6952-chipview-on-ace.png
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ltc6952-verify-comm.png
