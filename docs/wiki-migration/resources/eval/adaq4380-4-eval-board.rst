ADAQ4380-4 Evaluation Board User Guide
======================================

General Description
-------------------

The EV-ADAQ4380-4FMCZ evaluation board enables simplified evaluation of the ADAQ4380-4 Quad, 16-bit, 4 MSPS precision µModule® data acquisition solution. The evaluation board demonstrates the performance of the ADAQ4380-4 µModule and is a versatile tool for variety of applications.

The ADAQ4380-4 µModule combines multiple common signal processing and conditioning blocks into a single device that includes a low noise, fully differential analog-to-digital converter (ADC) drivers, a high precision 3.3V reference chip, low noise reference buffer, a high resolution, 16-bit, 4 MSPS simultaneous sampling successive approximation register (SAR) ADC, a low noise and all the critical passive components necessary for optimum performance. A full description of this product is available in the ADAQ4380-4 data sheet, which must be consulted when using the evaluation board.

The EV-ADAQ4380-4FMCZ evaluation board interfaces with high-speed system demonstration platform SDP-H1 (EVAL-SDP-CH1Z) board via a 160-pin connector as shown in Figure 1.

Features
--------

-  Full featured evaluation board of ADAQ4380-4
-  On-board voltage reference, clock source, and ADC drivers
-  Versatile analog signal conditioning circuitry
-  FMC-LPC system board connector
-  ACE PC software for configuration and data analysis (time and frequency domain)

Evaluation Board Kit Contents
-----------------------------

-  EV-ADAQ4380-4FMCZ evaluation board

Equipment Needed
----------------

-  PC with Windows 7 or Windows 10 operating system
-  SDP-H1 (EVAL-SDP-CH1Z) controller board
-  Precision signal source (such as APX500 series)
-  SMA cables (input to evaluation board)
-  Recommended - Band-pass filter centered on test signal frequency

Software Needed
---------------

-  EV-ADAQ4380-4FMCZ ACE plugin
-  SDP-H1 driver

Evaluation Board Hardware
-------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/adaq4380-4_fig2.png
   :width: 600px

**Figure 1. EV-ADAQ4380-4FMCZ Simplified Evaluation Board Block Diagram**

.. image:: https://wiki.analog.com/_media/resources/eval/picture.png
   :width: 600px

**Figure 2. EV-ADAQ4380-4FMCZ Evaluation System**

.. image:: https://wiki.analog.com/_media/resources/eval/picture.png
   :width: 600px

**Figure 3. EV-ADAQ4380-4FMCZ**

Setting Up the Evaluation Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure 1 shows the simplified evaluation board block diagram of the EV-ADAQ4380-4FMCZ connected to the SDP-H1 controller board. The board consists of one µModule (U1, ADAQ4380-4), on-board power supplies to power the necessary supply rails using the LT8362 (U2), and the ADP7142 (U3). Optional buffers, ADA4625-2 (A1 to A4), are included when evaluating the ADAQ4380-4 where sensors require high input impedance and further amplification is required.

SDP-H1 Controller Board
~~~~~~~~~~~~~~~~~~~~~~~

The EV-ADAQ4380-4FMCZ evaluation board uses an SPI interface and is connected to the high speed controller board for the system demonstration platform (SDP-H1) controller board. The SDP-H1 board requires power from a 12 V wall adapter. The SDP-H1 has a Xilinx® Spartan 6 and an ADSP-BF527 processor with connectivity to the PC through a USB 2.0 high speed port. The controller boards allow the configuration and capture of data on the daughter boards from the PC via a USB.

The SDP-H1 has an FMC low pin count (LPC) connector with full differential LVDS and singled-ended LVCMOS support. It also features the 160-pin connector, found on the SDP-B, which exposes the Blackfin® processor peripherals. This connector provides a configurable serial, parallel I2C and SPI, and general-purpose input/output (GPIO) communications lines to the attached daughter boar for the functional description of the on-board power supplies.

Power Supplies
~~~~~~~~~~~~~~

By default, all the required supply rails on the EV-ADAQ4380-4FMCZ are powered by a 3.3 V rail coming from the SDP-H1 board. The EV-ADAQ4380-4FMCZ can be powered from an external 3.3 V supply applied using the 3V3 pin header. See Table 2 for external supplies configuration. The EV-ADAQ4380-4FMCZ positive rails, 5 V (+VS), 3.4 V (VCC), and 3.4 V (VLOGIC), are generated from a combination of the on-board power supplies, U2 (LT8362), U3 (ADP7142-5.0), and the integrated 3.4 V output LDO.

Decoupling capacitors for ADAQ4380-4 supply pins are integrated in the μModule, adding external capacitors won’t be necessary. A single ground plane is used on this board to minimize the effect of high frequency noise interference.

| \*\* *Table 1. On-Board Power Supplies* \*\*
| ^Power Supply ^Function ^Min (V) ^Max (V) ^

+-----------------+----------------------------------------------------------+------+------+
| +6.0V           | 6 volts input supply voltage for LT8362                  | 5.9  | 6.1  |
+-----------------+----------------------------------------------------------+------+------+
| +5.0V (default) | 5 volts analog supply for VS+, REFIN, IN_LDO, and EN_LDO | 4.95 | 5.05 |
+-----------------+----------------------------------------------------------+------+------+
| +3.4V           | 3.4 volts for the ADC's VCC and VLOGIC supply            | 3.35 | 3.45 |
+-----------------+----------------------------------------------------------+------+------+
| GND             | Ground connection                                        | N/A  | N/A  |
+-----------------+----------------------------------------------------------+------+------+

Analog Inputs
~~~~~~~~~~~~~

The SMB connectors (INA+ and INA−, INB+ and INB−, INC+ and INC−, and IND+ and IND-) on EV-ADAQ4380-4FMCZ are used to provide analog inputs from a low noise, audio precision signal source (such as the SYS-2700 or the APx555 series). Analog inputs are directly feed thru ADAQ4380-4 as shown in Figure 20. The optional amplifiers ADA4625-2 (A1, A2, A3, and A4), can be set up in any gain configuration (unity-gain as default) to drive the inputs of ADAQ4380-4 for high input impedance applications. In the default board configuration, analog input signals are fed directly to the inputs of ADAQ4380-4, bypassing A1-A4 amplifiers.

To evaluate dynamic performance, a fast Fourier transform (FFT), integral nonlinearity (INL), differential nonlinearity (DNL), or time domain (waveform, histogram) test can be performed by applying a very low distortion ac source (see Figure 19 to Figure 23). For low input frequency testing below 100 kHz, it is recommended to use a low noise, audio precision signal source, APX-555 set at high performance sine generator. A different precision signal source can be used alternatively with additional band-pass filtering. The filter bandwidth depends on input bandwidth of interest.

Multiple link options must be set correctly for the appropriate operating setup before applying the power and signal to the evaluation board. The EV-ADAQ4380-4FMCZ is factory configured to provide the appropriate input signal type, single-ended or fully differential, and different gain/attenuation or input range scaling. Table 2 and Table 3 lists the required jumper positions and link options for different configurations.

| \*\* *Table 2. Link Options with Factory Default Setting* \*\*
| ^Link ^Default ^Function ^Comment ^

+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| LKA, LKB, LKC, LKD | 1 and 2, 7 and 8, 9 and 10, 11 and 12 | ADAQ4380-4 Gain Configuration       | Gain=0.3. See Figure 3 to Figure 6 for the configuration for different gain options.                                                                  |
+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| J1                 | 1 and 2                               | +3.3 V Input                        | Takes 3.3 V from the FMC. Change shunt position to Pin 2 and Pin 3 when using external power supply.                                                  |
+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| J2                 | 1 and 2                               | VLOGIC Input                        | Utilizes the 3.4V from the integrated LDO. Change shunt position to Pin 2 and Pin 3 for external VLOGIC.                                              |
+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| J3                 | 1 and 2, 3 and 4, 5 and 6             | ADAQ4380-4 Power Supply             | Utilizes the on-board +5V power supply. Disconnect shunts when supplying external voltages to Vs+, Vs-, and IN_LDO thru their respective header pins. |
+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| J4                 | Open                                  | MODE_FDA and PD_FDA control voltage | Connect shunt to pin 1 and pin2, and pin3 and pin 4 to enter low power mode, and shutdown mode for FDA, respectively.                                 |
+--------------------+---------------------------------------+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

| \*\* *Table 3. Jumper Options with Factory Default Setting* \*\*
| ^Jumper ^Default ^Function ^Comment ^

+--------------------------------------------+------------------------------------+--------------------------------+-------------------------------------------------------------------+
| JP1, JP5, JP10, JP14                       | Position B                         | Optional buffers               | Change shunt to position A to use the optional ADA4625-2 buffers. |
+--------------------------------------------+------------------------------------+--------------------------------+-------------------------------------------------------------------+
| JP2, JP6, JP9, JP13                        | Position A                         | Optional buffers               | Change shunt to position B to use the optional ADA4625-2 buffers. |
+--------------------------------------------+------------------------------------+--------------------------------+-------------------------------------------------------------------+
| JP3, JP4, JP7, JP8, JP11, JP12, JP15, JP16 | Not Installed                      | Optional buffers               | Install 0 Ω to use the optional ADA4625-2 buffers.                |
+--------------------------------------------+------------------------------------+--------------------------------+-------------------------------------------------------------------+
| R2, R4, R6, R8                             | Not Installed (Fully Differential) | ADAQ4380-4 Input Configuration | Install 0 Ω for single-ended input configuration.                 |
+--------------------------------------------+------------------------------------+--------------------------------+-------------------------------------------------------------------+

Link Configuration for Different Gain Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiple link options must be set correctly for appropriate gain configuration of the ADAQ4380-4. Figure 4 to Figure 7 shows the required link positions to set the proper gain configuration of EV-ADAQ4380-4FMCZ.

LKA, LKB, LKC, and LKD connections are designed such that different link positions and combinations will be identical on Channels A and B, whereas Channels C and D connections are mirror of Channel B and A, respectively. Figure 4 to Figure 7 link connections will be applicable for all the channels.

.. image:: https://wiki.analog.com/_media/resources/eval/gain_0.3.png
   :width: 400px

**Figure 4. Gain = 0.3 V/V**

.. image:: https://wiki.analog.com/_media/resources/eval/gain_0.6.png
   :width: 400px

**Figure 5. Gain = 0.6 V/V**

.. image:: https://wiki.analog.com/_media/resources/eval/gain_1.0.png
   :width: 400px

**Figure 6. Gain = 1.0 V/V**

.. image:: https://wiki.analog.com/_media/resources/eval/gain_1.6.png
   :width: 400px

**Figure 7. Gain = 1.6 V/V**

| \*\* *Table 4. Different Gain Configurations for the links of EV-ADAQ4380-4FMCZ* \*\*
| ^Gain ^Input Range ^Input Signal on Pins ^Test Conditions ^

+---------+-------------+--------------------------------------+----------------------------------------------------------------------------------------------------+
| 0.3 V/V | *+*\ 11 V   | INx2+ and INx2-                      | For LKA, LKB, LKC, and LKD, install shunt 1 to 2, 7 to 8, 9 to 10, and 11 to 12. See Figure 4.     |
+---------+-------------+--------------------------------------+----------------------------------------------------------------------------------------------------+
| 0.6 V/V | *+*\ 5.5 V  | INx2+ and INx2-                      | For LKA, LKB, LKC, and LKD, install shunt 1 to 2, and 7 to 8. See Figure 5.                        |
+---------+-------------+--------------------------------------+----------------------------------------------------------------------------------------------------+
| 1.0 V/V | *+*\ 3.3 V  | INx1+ and INx1-                      | For LKA, LKB, LKC, and LKD, install shunt 1 to 3, and 5 to 7. See Figure 6.                        |
+---------+-------------+--------------------------------------+----------------------------------------------------------------------------------------------------+
| 1.6 V/V | *+*\ 2.06 V | INx1+ and INx2+, and INx1- and INx2- | For LKA, LKB, LKC, and LKD, install shunt to 1 and 2, 3 and 4, 5 and 6, and 7 and 8. See Figure 7. |
+---------+-------------+--------------------------------------+----------------------------------------------------------------------------------------------------+

Optional Buffers and Filters Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EV-ADAQ4380-4FMCZ includes optional amplifiers for further amplification and filtering. By default, these amplifiers are bypassed and not connected to the analog input signal path.

Should evaluation require, these amplifiers could be utilized via jumpers JP1 – JP16, see Figure 29. A1-A4 are designed for buffering, amplification, and filtering. The filters can be configured as a Sallen-Key low pass or high pass filter.

.. image:: https://wiki.analog.com/_media/resources/eval/lpf.png
   :width: 400px

**Figure 8. 2nd Order Lowpass Filter Topology**

.. image:: https://wiki.analog.com/_media/resources/eval/hpf.png
   :width: 400px

**Figure 9. 2nd Order Highpass Filter Topology**

Evaluation Software
-------------------

Software Installation
~~~~~~~~~~~~~~~~~~~~~

Before using the EV-ADAQ4380-4FMCZ download and install the ACE (Analysis, Control, Evaluation) software. Download the software from :adi:`en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software`.html.

ACE is a desktop software application allowing the evaluation and control of multiple evaluation systems across the Analog Devices product portfolio. The installation process consists of the ACE software installation and the SDP-H1 driver installation.

To ensure that the evaluation system is correctly recognized when it is connected to the PC, install the ACE software and the SDP-H1 driver before connecting the EV-ADAQ4380-4FMCZ and SDP-H1 board to the USB port of the PC.

Installing ACE
~~~~~~~~~~~~~~

To install the ACE software, take the following steps:

1. Download the ACE software to a Windows-based PC.

2. Double-click the ACEInstall.exe file to begin the installation. By default, the software is saved to the following

3. A dialog box appears asking for permission to allow the program to make changes to the PC. Click Yes to begin the installation process.

4. Click Next > to continue the installation, as shown in Figure 10.

.. image:: https://wiki.analog.com/_media/resources/eval/ace_setup.png
   :width: 600px

**Figure 10. Evaluation Software Install Confirmation**

5. Read the software license agreement and click I Agree (see Figure 11).

.. image:: https://wiki.analog.com/_media/resources/eval/license_agreement.png
   :width: 600px

**Figure 11. License Agreement**

6. Choose an installation location and click Next (see Figure 12).

.. image:: https://wiki.analog.com/_media/resources/eval/install_location.png
   :width: 600px

**Figure 12. Choose Install Location**

7. Select the Pre-Requisites checkbox to include the installation of the SDP-H1 driver. Click Install (see Figure 13).

.. image:: https://wiki.analog.com/_media/resources/eval/choose_components.png
   :width: 600px

**Figure 13. Choose Components**

8. The Windows Security window appears. Click Install (see Figure 13). The installation is in progress. No action is required (see Figure 14).

.. image:: https://wiki.analog.com/_media/resources/eval/windows_security.png
   :width: 600px

**Figure 14. Windows Security Window**

.. image:: https://wiki.analog.com/_media/resources/eval/installation_in_progress.png
   :width: 600px

**Figure 15. Installation in Progress**

9. The installation is complete (see Figure 16). Click Next > and then click Finish to complete.

.. image:: https://wiki.analog.com/_media/resources/eval/instllation_complete.png
   :width: 600px

**Figure 16. Installation Complete**

Software Operation
------------------

Launching the Software
~~~~~~~~~~~~~~~~~~~~~~

When the EV-ADAQ4380-4FMCZ and SDP-H1 boards are properly connected to the PC, launch the ACE software. To launch the ACE software, take the following steps:

-  From the Start menu, select All Programs > Analog Devices > ACE> ACE.exe to open the main software window shown in Figure 17.
-  The EV-ADAQ4380-4FMCZ icon appears in the Attached Hardware section.
-  If the EV-ADAQ4380-4FMCZ is not connected to the USB port via the SDP-H1 board when the software is launched, the EV-ADAQ4380-4FMCZ board icon does not appear in the Attached Hardware section. Connect the EV-ADAQ4380-4FMCZ and SDP-H1 board to the USB port of the PC and wait a few seconds, then continue following these instructions.
-  Double-click the EV-ADAQ4380-4FMCZ board icon to open the window shown in Figure 17.
-  Click Software Defaults and then click Apply Changes.
-  Click Proceed to Analysis to open the EV-ADAQ4380-4FMCZ analysis shown on Figure 18.

Exiting the Software
~~~~~~~~~~~~~~~~~~~~

To exit the software, click file icon on the upper right tab and then click Exit.
