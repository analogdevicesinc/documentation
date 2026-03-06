Evaluating 14-/16-/18-Bit ADCs from the 8/10 LEAD PulSAR® Family
================================================================

Features
--------

Full-featured evaluation board for 8/10 lead PulSAR® ADCs Versatile analog signal conditioning circuitry On-board reference, reference buffers and ADC Drivers PC software for control and data analysis of time and frequency domain System Demonstration Board Compatible :adi:`EVAL-SDP-CB1Z <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html>`

--------------

Supported Devices
~~~~~~~~~~~~~~~~~

-  :adi:`AD7685`
-  :adi:`AD7686`
-  :adi:`AD7687`
-  :adi:`AD7688`
-  :adi:`AD7690`
-  :adi:`AD7691`
-  :adi:`AD7693`
-  :adi:`AD7942`
-  :adi:`AD7946`
-  :adi:`AD7980`
-  :adi:`AD7982`
-  :adi:`AD7983`
-  :adi:`AD7984`
-  :adi:`AD7988-1`/:adi:`AD7988-5` Both use the same evaluation board (EVAL-AD7988-5)
-  :adi:`AD7683`
-  :adi:`AD7684`
-  :adi:`AD7694`
-  :adi:`AD7915`
-  :adi:`AD7916`

Hardware
--------

.. tip::

   Note that we are only shipping REV C boards as of now. Please click on the link to the REV C user guide for this board in the section below. Rev A information is only here for legacy purposes.


--------------

REV A
~~~~~

REV A hardware is a very simple board which requires power supply rails from a bench-top power supply to power the board. This board interfaces to the SDP controller board. This board is no longer available to purchase and is shown here for legacy purposes.


|image1|

--------------

PMOD Compatible
~~~~~~~~~~~~~~~

PMOD compatible hardware is a very simple board which plugs directly into microprocessor and FPGA boards which have PMOD peripherals.

Complete details about the PulSAR ADC PMOD boards can be found by visiting our :doc:`PulSAR ADC PMOD Page </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods>`

-  SOFTWARE NOTE: If using the PMOD compatible version of the hardware, please install this version of the software. `PMOD Evaluation Boards Software <https://wiki.analog.com/ftp/ftp.analog.com/pub/cftl/eval-adxxxx-pmdz/1.0.0>`__
-  HARDWARE NOTE: If using the PMOD compatible version of the hardware, you will need to use the PMOD to SDP interposer board to fully evaluate the system. This PMOD to SDP interposer board can be used to connect any of the 10 PulSAR PMOD compatible boards to the PC or laptop. All detailed user information along with schematic, bill of materials, and layout files for this board can be found at out :doc:`PulSAR ADC PMOD Page </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods>`

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pulsar_pmod.jpg
   :align: center
   :width: 500px

--------------

REV C
~~~~~

The REV C board is the current board that is available for purchase. This board contains the on-board power supplies to power all portions of the board - the ADC, Reference, Amplifiers and SDP board. This board operates from a simple +9V wall adaptor which is included as part of the evaluation board kit. This board interfaces to the SDP controller board.

\**All documentation for this version of hardware is contained in the USER GUIDE \*\*\ :adi:`REV C USER GUIDE <static/imported-files/user_guides/UG-340.pdf>`

.. image:: https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_revc.jpg
   :align: center
   :width: 500px

--------------

.. important::

   All detail which follows applies to REV A hardware


--------------

General Description
-------------------

This evaluation board covers for the following 10 lead PulSAR® analog to digital converters (ADCs): :adi:`AD7685`\ (16-bit), :adi:`AD7686`\ (16-bit), :adi:`AD7687`\ (16-bit), :adi:`AD7688`\ (16-bit), :adi:`AD7690`\ (18-bit), :adi:`AD7691`\ (18-bit), AD7693 (16-bit), :adi:`AD7942`\ (14-bit), :adi:`AD7946`\ (14-bit), :adi:`AD7980`, :adi:`AD7988-1`, :adi:`AD7988-5`\ (16-bit), :adi:`AD7982`\ (18-bit), :adi:`AD7983`\ (16-bit), :adi:`AD7984`\ (16-bit), :adi:`AD7915`\ (16-bit), :adi:`AD7916`\ (16-bit). These low power ADCs offer very high performance of up to 18bits with throughputs ranging from 100ksps to 1MSPS. The evaluation board is designed to demonstrate the ADC's performance and to provide an easy to understand interface for a variety of system applications. A full description of these products is available in their respective data sheets and should be consulted when utilizing this evaluation board. The evaluation board is ideal for use with Analog Devices System Demonstration Board, (SDP). On-board components include a high precision buffered band gap 5.0V reference, (:adi:`ADR435`), reference buffers (:adi:`AD8032`), a signal conditioning circuit with two op-amps (:adi:`ADA4841-1`) and regulators to derive necessary voltage levels on board (:adi:`ADP3334`, :adi:`ADP3303`). This evaluation board interfaces to the SDP board via a 120 pin connector. SMB connectors, J3 and J4, are provided for the low noise analog signal source.

Evaluation Kit Contents (REV A)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Evaluation board for ADC where U10 is populated for the device ordered.
-  Business card advising location of user software download. User software is available to download directly from the product webpage. This ensures user always has the latest software.

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

-  :adi:`SDP <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html>`\ board - System Demonstration Board, (:adi:`EVAL-SDP-CB1Z <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html>`) used for data transfer from ADC to PC via USB
-  Bench-top power supply for +Vs, -Vs, Vdd, GND
-  Standard USB-A to Mini-B cable
-  Signal source; AC source with low distortion, DC source with low noise

System Requirements
^^^^^^^^^^^^^^^^^^^

-  PC operating Windows® XP (SP2), Windows® Vista™ or Windows® 7 Business/Enterprise/Ultimate editions (32-/64-Bit systems)
-  USB Port

Evaluation Board Software
=========================

Installing the Software
-----------------------

`Evaluation Board Software version 1.1 <https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_rev_a_gerbers.zip>`__ is available to download.

.. tip::

   The software install is a two part install, user should proceed through both parts prior to connecting board for first time


Install the software prior to connecting the SDP board to the USB port of the PC. This ensures that the SDP board is recognized when it connects to the PC.

-  Start the Windows® operating system and insert CD.
-  The installation software should launch automatically. If it does not, run the setup.exe file from the CD.
-  After installation is completed, power-up the EVAL board as described in Power Supplies section.
-  Plug the evaluation board into the SDP board and the SDP board into the PC using the USB cable included in the box.
-  When the software detects the EVAL board, proceed through any dialog boxes that appear to finalize the installation.

The default location for the software is C:\\Program Files\\Analog Devices\\10 Lead PulSAR ADCs This location contains the executable software, datasheets and example files.

Install Steps
~~~~~~~~~~~~~

Proceed through the install allowing the software and drivers to be placed in the appropriate locations. Only after the software and drivers have been installed should you connect the SDP board to the PC. There are two portions to the software install. Firstly the software related to the evaluation board as shown in Figure 2. |image2| *Figure 2. Evaluation Board Software Installation Launches*

|image3| *Figure 3. Choose Folder Location, Default Folder Shown*

|image4| *Figure 4. Accept National Instruments Software License Agreement*

|image5| *Figure 5. Click Next >> to Install Software*

|image6| *Figure 6. Bar Showing Installation Progress*

|image7| *Figure 7. Installation Complete, Click Next >> to Complete and Finish*

The second part of the software installation is the drivers related to the SDP board. These must be installed for the evaluation board to function correctly. See Figure 8 to Figure 13.

|image8| *Figure 8. Installation for SDP Starting*

|image9| //Figure 9. Click Next >> to Install the ADI SDP Drivers //

|image10| *Figure 10. Choose Install Location, Default Folder Shown*

|image11| *Figure 11. Installation in Progress*

|image12| *Figure 12. Click Finish to Complete Installation*

When you first plug in the SDP board via the USB cable provided, allow the new Found Hardware Wizard to run. You can check that the drivers and the board are connected correctly by looking at the Device Manager of the PC. The Analog Devices System Development Platform (32MB) should appear under ADI Development Tools.

|image13| *Figure 14. Device Manager*

======== Evaluation Board Hardware========

Setting Up the Evaluation Board
-------------------------------

The board consists of the specific ADC (U10) with reference (:adi:`ADR435`\ U6) and ADC Drivers (:adi:`ADA4841-1` U8, U12) The evaluation board is a flexible design that enables the user to adjust compensation components in addition to operating from adjustable bench top power supply.

Power Supplies
--------------

The evaluation board requires power from an external bench top supply, applied to J1 connector.

**Table 1. External Power Supply Required (max 12V across +Vs to -Vs)**

+--------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Power Supply | Voltage Range | Purpose                                                                                                                                                                                                                                                                                                                                                                              |
+==============+===============+======================================================================================================================================================================================================================================================================================================================================================================================+
| +Vs          | +7.5V         | Supplies :adi:`ADR435`, regulator :adi:`ADP3334` which supplies +7V to +Vs of :adi:`ADA4841-1`, regulator :adi:`ADP3303` which supplies +5V to :adi:`SDP <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html>`                                                                                                                                              |
+--------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| -Vs          | -2V           | Amplifier :adi:`ADA4841-1` negative rail                                                                                                                                                                                                                                                                                                                                             |
+--------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vdd          | 2.5V          | ADC Supply Rail for following ADCs AD7980, AD7982, AD7983, AD7984, AD7988-5                                                                                                                                                                                                                                                                                                          |
+--------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | 5V            | ADC Supply Rail for following ADCs AD7685, AD7686, AD7687, AD77688, AD7690, AD7691, AD7693, AD7694, AD7942, AD7946                                                                                                                                                                                                                                                                   |
+--------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On board regulators generate required levels from the applied +Vs rail. The regulators used are the ADP3334 (U9) which supplies +7V for the +Vs of the ADC driver amplifier (ADA4841), while the ADP3303-5 delivers 5V to the SDP board connector, J2 to power the SDP board. The SDP in turn provides a 3.3V V_DRIVE which supplies the IOVDD of the ADC in addition to the logic gates (U1, U3, U4). Each supply is decoupled where it enters the board and again at each device. A single ground plane is used on this board to minimize the effect of high frequency noise interference.

Reference
~~~~~~~~~

An external 5V reference (:adi:`ADR435` U6) is used to supply the ADCs. This reference is buffered by the :adi:`AD8032`.

Serial Interface
~~~~~~~~~~~~~~~~

The evaluation board uses the SPORT interface from the :adi:`SDP <en/system-demonstration-platform/controller-boards/evaluation/SDP-B/eb.html>`\ BF527 DSP. A number of AND gates are used to clock and gate the SPORT transfer to the ADC device. See U1, U3, U4.

Solder Links
~~~~~~~~~~~~

There is one 3 Solder Link Option on the board. It is configured depending on which generic of ADC is on the specific evaluation board as described below. **Table 2. Solder Link Default Setting**

+------+---------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link | Setting | Configuration      | Generic                                                                                                                                                                                                                                                                                                                                                        |
+======+=========+====================+================================================================================================================================================================================================================================================================================================================================================================+
| SL1  | A       | Differential Input | :adi:`AD7687`, :adi:`AD7688`, :adi:`AD7690`, :adi:`AD7691`, :adi:`AD7982`, :adi:`AD7984`, :adi:`AD7915`, :adi:`AD7916`                                                                                                                                                                                                                                         |
+------+---------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SL1  | B       | Single Ended Input | :adi:`AD7685`, :adi:`AD7686`, :adi:`AD7942`, :adi:`AD7946`, :adi:`AD7980`, :adi:`AD7983`                                                                                                                                                                                                                                                                       |
+------+---------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Analog Inputs
~~~~~~~~~~~~~

The analog inputs to the evaluation board are J3 and J4 SMB (push on) connectors. These inputs are buffered with dedicated amplifier circuitry (U8 and U12) and discrete as shown in the schematic. The circuit allows for different configurations, input range scaling, filtering, addition of a DC component, use of different op-amp and supplies. The analog input amplifiers are set as unity gain buffers at the factory. The Amplifier positive rail is driven from +7V (from :adi:`ADP3334`, U9), this could be changed to a different value as required, the negative amplifier rail is driven from –Vs which is applied direct to the board. The range of supply possible is listed in Table 1. The default configuration sets both U8 and U12 at mid-scale generated from a buffered reference voltage divider (VCM). The evaluation board is factory configured for providing either a single ended path or a fully differential path as described in Table 2. For dynamic performance, an FFT test can be done by applying a very low distortion AC source. For low frequency testing, the Audio Precision source can be used directly as the outputs on these are isolated. Set the outputs for balanced and floating. Different sources can be used however, most are single ended and use a fixed output resistance. Since the evaluation board uses the amplifiers in unity gain, the non-inverting input has a common mode input with a series 590 ohm resistor and it needs to be taken into account when directly connecting a source (voltage divider).

Board Operation
---------------

-  Connect SDP controller board to the evaluation board with the J2 connector (screw into place as required). The software is configured to find the evaluation board on either connector of the SDP board.
-  Power board with appropriate supply as described.
-  Connect to PC with USB cable provided
-  Launch software. Click Start > All Programs > Analog Devices > 10 Lead PulSAR ADCs.
-  Apply signal source and capture data

.. image:: https://wiki.analog.com/_media/resources/eval/ad7980_sdp1z.jpg
   :align: center
   :width: 300px

Running the software with hardware connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run the program, do the following:

-  Click Start > All Programs > Analog Devices > 10 Lead PulSAR ADCs. To uninstall the program, click Start > Control Panel > Add or Remove Programs > 10 Lead PulSAR ADCs.
-  If the SDP board is not connected to the USB port when the software is launched, a connectivity error is displayed.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp_-_no_hardware.jpg
   :align: center
   :width: 200px

Simply connect the EVAL board to the USB port of the PC, wait a few seconds, click Rescan, and follow the instructions.

.. image:: https://wiki.analog.com/_media/resources/eval/sdp_-_found_board.jpg
   :align: center
   :width: 200px

The software connects to the board and displays the following:

.. image:: https://wiki.analog.com/_media/resources/eval/sdp_-_wait.jpg
   :align: center
   :width: 200px

Once the board has been correctly detected, the software panel will open. The example below shows the AD7691 panel.

.. image:: https://wiki.analog.com/_media/resources/eval/ad7691_panel.jpg
   :align: center

Description of User Panel
~~~~~~~~~~~~~~~~~~~~~~~~~

The following is the description of the user panel:

-  File menu with choice of

   -  Load Data: load previously captured data
   -  Save Data as .tsv: save captured data in tsv (tab separated values) format for future analysis
   -  Save Picture: use to save the current screen capture
   -  Print
   -  Exit

-  When hardware is connected to the USB port, the software automatically detects which generic is connected and displays it here. Without hardware, the software can be operated in standalone mode for data analysis, and the part information will note the part number pulled from the saved data file.
-  Sampling Frequency: The default sampling frequency will match the maximum sample rate of the ADC connected to the board. The user can adjust the sampling frequency; however, there are limitations around the sample frequency related to the SCLK frequency applied. The sample frequency must be an integer divider of the SCLK frequency. In addition, where unusable sample frequencies are input, the software automatically adjusts the sample frequency accordingly. Units can be entered, such as 10k for 10,000 Hz. Because the maximum sample frequency possible is device dependent, with some of the ADCs capable of operating up to 250 kSPS, while others can go to 1.3 MSPS, the software will match the particular ADC ability. If the user enters a value larger than the ability of the existing device, the software will indicate this and revert to the maximum sample frequency.
-  SCLK Frequency: The default SCLK frequency is set to 60 MHz, which is the maximum allowable from the SDP. The SCLK is applied to the ADC SCK pin. The SDP board limits the SCLK frequency, nominal values for correct operation are 60 MHz, 30 MHz, and 20 MHz. Where the user adjusts the SCLK/sample rate to values that are not supported by the SDP clock or the ADC sample rate, the software overrides by adjusting values accordingly and identify this to the user. The SCLK frequency will be rounded down.
-  External reference voltage. By default, this reference is 5V (:adi:`ADR435` on board reference). The min/max voltage calculations are based on this reference voltage. If user changes the reference voltage, then they should change this input accordingly.
-  “Read” : to perform a single capture
-  “Start” : to perform a continuous capture from the ADC.
-  “Stop”: to stop streaming data
-  Select the number of samples to analyse, when running continuously, this number will be limited to 65536 samples.
-  There are four tabs available displaying the data in different formats, this are listed here and described in more detail later.

   -  Waveform tab
   -  Histogram
   -  FFT
   -  Summary

.. image:: https://wiki.analog.com/_media/resources/eval/value_change_dialog_box.jpg
   :align: center
   :width: 200px

Design Support Package
======================

.. tip::

   Note the following documents apply to Rev A hardware


REV A HARDWARE INFORMATION
==========================

Schematic
~~~~~~~~~

`Schematic in .pdf format <https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_reva.pdf>`__

`Schematic in Mentor Graphics Pads format 9.3 <https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_reva_pads_schematic.zip>`__

`Layout in Mentor Graphics Pads Layout <https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_reva_pads_layout.zip>`__

Gerber Files
~~~~~~~~~~~~

`10_lead_pulsar_rev_a_gerbers.zip <https://wiki.analog.com/_media/resources/eval/10_lead_pulsar_rev_a_gerbers.zip>`__

Bill of Materials
~~~~~~~~~~~~~~~~~

The attached .zip file contains bill of material for the following boards: :adi:`AD7685`, :adi:`AD7687`, :adi:`AD7688`, :adi:`AD7690`, :adi:`AD7691`, :adi:`AD7942`, :adi:`AD7980`, :adi:`AD7982`, :adi:`AD7983`, :adi:`AD7984`\ and :adi:`CN0261`. `BOM <https://wiki.analog.com/_media/resources/eval/bom.zip>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/10_lead_pulsar.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/10322-002.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/10322-003.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/10322-004.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/10322-005.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/10322-006.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/10322-007.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/10322-008.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/10322-009.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/10322-010.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/10322-011.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/10322-013.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/10322-014.jpg
   :width: 400px
