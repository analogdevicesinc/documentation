EV-ADF41513SD3Z User Guide
==========================

Evaluating the ADF41513 Integer N, Fractional-N PLL Synthesizer and ADF5709 VCO
-------------------------------------------------------------------------------

Features
--------

-  :adi:`ADF41513` frequency synthesizer,
-  :adi:`ADF5709` 9.85 GHz to 20.5 GHz wideband VCO,
-  :adi:`LT3045` and :adi:`LT3042` regulators,
-  Includes 100 MHz crystal oscillator and on-board active loop filter,
-  Header connectivity to allow use of :adi:`SDP-S` connector with USB interface,
-  Externally powered by 5.5 V and 25 V supplies

Evaluation Kit Contents
-----------------------

-  EV-ADF41513SD3Z evaluation board

Board Design Files
------------------

-  `Gerber <https://wiki.analog.com/_media/undefined/ev-adf41513sd3z_gerbers.zip>`_
-  `Schematic <https://wiki.analog.com/_media/resources/eval/02-067120-01-b.pdf>`_

Equipment Needed
----------------

-  Windows-based PC with USB port for evaluation software
-  Power supply (5.5 V)
-  Power supply (25 V)
-  :adi:`SDP-S` controller board
-  Spectrum analyzer

Online Resources
----------------

-  :adi:`ADF41513` data sheet
-  :adi:`ADF5709` data sheet

General Description
-------------------

The :adi:`EV-ADF41513SD3Z` evaluation board can be used to evaluate all the features and the performance of the ADF41513. The EV-ADF41513 includes an on-board 9.85 GHz to 20.5 GHz ADF5709 VCO. The EV-ADF41513SD3Z board include the ADF41513 frequency synthesizer, 100 MHz reference (crystal oscillator (XO)), loop filter, universal serial bus (USB) interface, low noise LT3045/LT3042 voltage regulators, and a USB cable to connect the board to a PC USB port. For easy programming of the synthesizer, download the Windows®-based software from the ADF41513 product page at www.analog.com/ADF41513. The evaluation board requires a :adi:`SDP-S`, which is not included with the kit. The SDP-S allows software programming of the ADF41513 device through a USB interface. Consult the ADF41513 data sheet in conjunction with this user guide when working with the evaluation boards.

Getting Started
---------------

Software Installation Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the EV-ADF41513SD3Z control software from the ADF41513 product page at www.analog.com/ADF41513. For the software installation procedure, see the PLL Software Installation Guide :adi:`UG-476`.

Evaluation Board Hardware
-------------------------

The EV-ADF41513SD1Z and EV-AD41513SD2Z require the SDP-S platform that uses the EVAL-SDP-CS1Z. Use of SDP-B is not recommended. The evaluation board schematics, assembly, silkscreen, and bill of materials are available in the Evaluation Board Schematics and Artwork section and Ordering Information section. The Gerber fabrication files are available on the :adi:`ADF41513` product pages on analog.com.

Evaluation Board Setup Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the software, perform the following steps:

-  After installation, click the ADF41513 icon on the desktop or select Analog Devices > ADF41513 from the Start menu.
-  In the Select Device and Connection tab, click Connect (see Figure 1).
-  Approximately 5 sec to 10 sec after connecting the board, the connection status in the bottom left corner changes from No device connected to Connected.

Under File, the current settings can be saved to or loaded from a text file.

.. image:: https://wiki.analog.com/_media/resources/eval/fig1.png
   :width: 400px

Figure 1. Software Front Panel Display, Select Device and Connection Tab

Power Supplies
~~~~~~~~~~~~~~

The board is powered by a 5.5 V (300 mA) power supply connected to the red and black banana connectors. Connect the red connector to a 5.5 V power supply and the black connector to ground. Connect a 25 V (20 mA) power supply to either the V+SMA SMA connector or the test point labeled V+. These connectors power the loop filter op amp. By default, two LDO regulators provide power. The EV-ADF41513SD3Z includes a dedicated 5 V LDO powering the ADF5709 VCO.

Loop Filter
~~~~~~~~~~~

The loop filter component placement is shown in Figure 2. The full loop filter can be found in the schematic. For the best in-band phase noise at 15 GHz, use the following components with a 2.4 mA charge pump current and narrow antibacklash pulse (ABP) setting.

-  C1 = 82 pF, C2 = 22 nF, C3 = 200 pF, C4 = 56 pF
-  R1 = 220 Ω, R2 = 280 , R3 = 1 kΩ

Narrower loop filter bandwidths have lower spurious signals.

.. image:: https://wiki.analog.com/_media/resources/eval/fig2.png
   :width: 400px

Figure 2. Loop Filter Placement

Reference Source
~~~~~~~~~~~~~~~~

The evaluation board contains a 100 MHz single-ended output 5 mm x 7.5 mm XO from Crystek Corporation. The reference source at Y1/Y2 is dual footprint which allows the use of both 5 mm x 7.5 mm and 9 mm x 14 mm XO packages if they are pin compatible. The default 100 MHz XO uses a 3.3 V supply but a 5 V supply XO can be powered from the 5 V LDO by removing R31 and populating R29 with 0 Ω. When using an external reference, remove R8 to disconnect the XO stub and remove R20 to power down the XO. Connect the external reference to the SMA connector labeled REFIN.

Default Configuration
~~~~~~~~~~~~~~~~~~~~~

All components necessary for local oscillator (LO) generation are inserted on the EV-ADF41513SD3Z board. The board is shipped with the ADF41513 synthesizer, ADF41513 VCO, 100 MHz reference XO, and a 416 kHz loop filter (assuming charge pump current (ICP) = 2.4 mA and RF VCO frequency (RFOUT) = 15 GHz).

Evaluation Board Software
-------------------------

Main Controls
~~~~~~~~~~~~~

The Main Controls tab (see Figure 3) selects the RF and user configurable register settings. Consult the register descriptions of the ADF41513 data sheet for details. The default setting is recommended for most registers. In the RF Settings area, ensure that the VCOout (MHz) box equals the VCO frequency fed back to the PLL. Ensure that the value in the Reference freq. box equals the applied reference signal. The phase frequency detector (PFD) frequency is calculated from the reference frequency, the R counter, the reference doubler, and the reference divide by 2. Ensure that the value in the PFD (MHz) box matches the value specified in the loop filter design. In the Register 5 area, select the value in the CP Current drop down box that matches the value used for the loop filter design.

.. image:: https://wiki.analog.com/_media/resources/eval/fig3.png
   :width: 400px

Figure 3. Software Front Panel Display, Main Controls Tab

Evaluation and Test
-------------------

To evaluate and test the performance of the EV-ADF41513SD3Z, use the following procedure:

-  Install the ADF41513 software (see the PLL Software Installation Guide).
-  If using a PC with Windows 10, follow the hardware driver installation procedure.
-  Connect the evaluation board to the SDP-S board.
-  Connect the 5.5 V power supply to the banana connectors.
-  Connect the 25 V power supply to the V+SMA connector.
-  Power on the 5.5 V and 25 V supplies. There is no sequencing requirement.
-  Connect the USB cable from the SDP-S board to the PC.
-  Run the ADF41513 software.
-  Select ADF41513 and SDP board (black) in the Select Device and Connection tab (see Figure 1).
-  Click the Main Controls tab, and set the VCOout (MHz) box to a frequency of 15,000 MHz (see Figure 5).
-  Click Write Initialization Sequence in the Registers area.
-  Connect the spectrum analyzer to SMA Connector RFOUT.
-  Measure the output spectrum and single sideband phase noise.

Figure 4 shows a phase noise plot of the SMA RFOUT at 15 GHz.

.. image:: https://wiki.analog.com/_media/resources/eval/fswp_screenshot_2021-07-06_15-50-46.png
   :width: 600px

Figure 4. Single Sideband Phase Noise
