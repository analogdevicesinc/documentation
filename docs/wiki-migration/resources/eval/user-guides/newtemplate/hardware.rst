**\*BOARD_NAME**\ \* User Guide
===============================

Introduction
------------

| The `board_name <https://wiki.analog.com/board_name>`__ is an 18-bit, 15 MSPS, 2 ppm linear data acquisition system with an easy to drive input impedance of 1.1 kΩ. The analog input range is 8.096 V peak-to-peak and can be driven in either single-ended or differential mode, providing flexibility for many different applications.
| The circuit is in field programmable gate array (FPGA) mezzanine card (FMC) form factor, powered with 12 V either from the FMC connector or an external supply. The digital interface uses serial low voltage differential signaling (LVDS), minimizing the input/output requirements and enabling easy integration with other FPGA designs.
| A separate data clock eases the timing requirements of the host FPGA. An on-board 120 MHz clock is forwarded to the FPGA and a CONVERT retiming flip-flop reduces jitter from the convert signal of the FPGA.

Features
~~~~~~~~

-  15 MSPS Throughput Rate
-  Guaranteed 18-Bit, No Missing Codes
-  No Pipeline Delay, No Cycle Latency
-  96 dB SNR (Typical)
-  164.5 dB dynamic range
-  2 ppm INL (Typical)
-  Serial LVDS Digital Interface
-  Flexible analog input drive (single-ended or differential mode)
-  On-board 120 MHz precision voltage-controlled crystal oscillator (VCXO)

Applications
~~~~~~~~~~~~

-  Flow cytometry
-  Optical pulse measurement
-  Fast control loops
-  Fast digital distortion correction
-  Image sensor digitization

--------------

Hardware Setup
--------------

| 
| ==== Equipment Needed ==== The following is the list of items needed in order to evaluate the CN0577:

Hardware
^^^^^^^^

-  `board_name <https://wiki.analog.com/board_name>`__ Circuit Evaluation Board
-  ZedBoard (AES-Z7EV-7Z020-G)
-  12 V power supply
-  Host PC
-  SD card (16 GB or larger)
-  LAN cable
-  SMA cables
-  XLR to SMA adapter cable
-  Audio analyzer (Audio Precision© APX525) or other input source (e.g., ADALM2000)

If using :adi:`ADALM2000` as input source:

-  :adi:`AD-M2KBNC-EBZ`
-  BNC to SMA cable

Software
^^^^^^^^

-  :doc:`Analog Devices Kuiper Linux image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

| 
| ==== Hardware Configuration ====

Block Assignments
^^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/cn0577_block_terminal.png
   :align: center
   :width: 600px

+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Connector Name | Operation              | Description                                                                                                                                                                                                                       | Settings/Ranges                                            |
+================+========================+===================================================================================================================================================================================================================================+============================================================+
| P1             | Power Down (PD) Mode   | When PD is high CN0577 will operate normally, but when PD is low CN0577 board enters power-down mode and all circuitry (including LVDS interface) is shutdown.                                                                    | PD = High (Pins 1 and 2)                                   |
|                |                        |                                                                                                                                                                                                                                   | PD = Low (Pins 2 and 3)                                    |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| P2             | Test Pattern (TESTPAT) | Forces the LVDS data outputs to be a test pattern. When TESTPAT is high digital outputs are a test pattern, and when TESTPAT is low digital outputs are the ADC conversion result.                                                | TESTPAT = High (Pins 1 and 2) TESTPAT = Low (Pins 2 and 3) |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| P3             | Lane Mode Selection    | The ADC outputs two bits at a time on DA-/DA+ and DB-/DB+ when two-lane output mode is high, and the ADC outputs one bit at a time on DA-/DA+ and DB-/DB+ when two-lane output mode is low.                                       | TWOLANES = High (Pins 1 and 2)                             |
|                |                        |                                                                                                                                                                                                                                   | TWOLANES = Low (Pins 2 and 3)                              |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| P4             | FMC Connector (LPC)    | Low pin count FMC connector used to connect the EVAL-CN0577-FMCZ hardware to various different FPGA development boards and kits.                                                                                                  | N/A                                                        |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| J1             | Positive Analog Input  | This is the positive input to the EVAL-CN0577-FMCZ, which connects to external signal sources via an SMA connection.                                                                                                              | 0 to 4.096 V                                               |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| J2             | Negative Analog Input  | This is the negative input to the EVAL-CN0577-FMCZ, which connects to external signal sources via an SMA connection.                                                                                                              | 0 to -4.096 V                                              |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| J3             | External Clock         | If an external clocking source is desired in your system this is where you will need to connect it. Along with connecting it you will also need to update the solder jumper (JP14) to change from the onboard crystal oscillator. | On-board Crystal Oscillator (default 120MHz)               |
| JP14           |                        |                                                                                                                                                                                                                                   | External source (120MHz desired)                           |
+----------------+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

| 
| ==== Setting Up the Hardware ==== |Demo with AP as input source|

To set up the complete system using **Audio Precision audio analyzer** as input source, follow these steps:

-  Download and install the IIO Oscilloscope application on the PC, Mac, or Linux host.
-  Load the Analog Devices Kuiper Linux image onto the SD card.
-  Configure the SD card for the :adi:`EVAL-CN0577-FMCZ`.
-  Place the SD card into the ZedBoard.
-  Connect :adi:`EVAL-CN0577-FMCZ` to the ZedBoard through the FMC pin connector.
-  Connect the 12 V power supply jack on the ZedBoard.
-  Plug in the LAN cable from the ZedBoard to the host computer.
-  Connect the :adi:`EVAL-CN0577-FMCZ` to the Audio Precision audio analyzer using the XLR to SMA adapter cable.
-  Connect the ground of the :adi:`EVAL-CN0577-FMCZ` to the Audio Precision audio analyzer.
-  Connect the Audio Precision audio analyzer USB cable to PC.
-  Run the IIO Oscilloscope software and capture the resulting ADC data.

| 
|

.. tip::

   **For detailed instructions on the Software Setup, please visit:** :doc:`BOARD NAME Software User Guide </wiki-migration/resources/eval/user-guides/newtemplate/software>`


--------------

Test Results and Analysis
-------------------------

Fast Fourier Transform (FFT) techniques are used to test the ADC’s frequency response, distortion, and noise at the rated throughput. By applying a low distortion sine wave and analyzing the digital output using an FFT algorithm, the ADC’s spectral content can be examined for frequencies outside the fundamental. The LTC2387-18 provides guaranteed tested limits for both AC distortion and noise measurements.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/cn0577_22.png
   :align: center
   :width: 400px

At 40 kHz differential input signal, with an amplitude of 4.096 Vp-p sitting at a common-mode voltage of 2.048 V and ADC sampling at a rate of 15 MSPS; the measured lowest average SNR and THD is 82.6 dB and -84 dB, respectively.

Figure X shows the typical performance of CN0577 at different sampling rates and frequency input signal.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/cn0577_24.png
   :align: center
   :width: 400px

Figure X illustrates the typical DC histogram of CN0577, with REFIN equal to 2.048 V and a sample frequency of 15 MSPS.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/cn0577_26.png
   :align: center
   :width: 400px

Figure X presents the error between the ideal voltage and the corresponding voltage input for two different sampling rates, 5 MSPS and 15 MSPS.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/newtemplate/cn0577_27.png
   :align: center
   :width: 350px

| 

--------------

Additional Information and Useful Links
---------------------------------------

-  :adi:`CN0577 Circuit Note Page <CN0577>`
-  :adi:`LTC2387-18 Product Page <LTC2387-18>`
-  :adi:`ADR4520 Product Page <ADR4520>`
-  :adi:`ADA4945-1 Product Page <ADA4945-1>`
-  :adi:`ADN4661 Product Page <ADN4661>`
-  :adi:`ADG3241 Product Page <ADG3241>`
-  :adi:`LT3042 Product Page <LT3042>`
-  :adi:`LT3080 Product Page <LT3080>`
-  :adi:`LT3094 Product Page <LT3094>`
-  :adi:`LT1931 Product Page <LT1931>`

--------------

Reference Demo and Software Resources
-------------------------------------

-  `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__
-  :doc:`PyADI-IIO Installation Guide </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
-  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Kuiper Images </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  :doc:`CN0577 HDL Reference Design </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0577/hdl>`

--------------

Design and Integration Files
----------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-CN0577-FMCZ Design & Integration Files <CN0577-designsupport>`

   
   -  Schematics
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   


--------------

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-CN0577-FMCZ?&v=RevB>`__ to receive all these great benefits and more!


--------------

.. image:: https://wiki.analog.com/_media/navigation New Template#none#./
   :alt: Overview#none#

.. |Demo with AP as input source| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/demo_with_ap.png
   :width: 600px
