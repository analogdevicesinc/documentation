Evaluating the ADRF6850 100 MHz to 1000 MHz Integrated Broadband Receiver
=========================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to evaluate :adi:`ADRF6850` integrated broadband receiver using :adi:`ADRF6850-EVALZ <eval-adrf6850>` and the :adi:`sdp-s` controller board developed by Analog Devices.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. ADRF6850 Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  Data Sheet: :adi:`ADRF6850 <media/en/technical-documentation/data-sheets/ADRF6850.pdf>`
-  Schematics: `ADRF6850-EVALZ Rev A <https://wiki.analog.com/_media/resources/eval/sdp/adrf6850-evalz_schematic.pdf>`__
-  Bill of Materials: `ADRF6850-EVALZ Rev A <https://wiki.analog.com/_media/resources/eval/sdp/adrf6850-evalz_bom_customer.xlsx>`__
-  PCB Gerber Files: `ADRF6850-EVALZ Rev A <https://wiki.analog.com/_media/resources/eval/sdp/adrf6850-evalz_gerber_files.zip>`__
-  PCB Layout: `ADRF6850-EVALZ Rev A <https://wiki.analog.com/_media/resources/eval/sdp/adrf6850-evalz_layout.pdf>`__

Software Needed
---------------

Labview-based Controller Software (runs on PC with Windows 10 or earlier version Windows OS)

Hardware Needed
---------------

-  :adi:`ADRF6850-EVALZ <eval-adrf6850>` Board
-  :doc:`SDP-S </wiki-migration/resources/eval/sdp/sdp-s/getting_started>` (EVAL-SDP-CS1Z) Board which comes with USB A to mini-B cable
-  Windows P.C. with ADRF6850 Software
-  3.3Vdc 0.5A Power Supply
-  0V Power Supply (or short VGAIN test point to GND)
-  Spectrum Analyzer (to observe 20MHz tone)
-  High-Frequency Signal Generator (to output 520MHz at 0dBm level)
-  50Ω SMA termination
-  2 SMA Cables

Quick Start Guide
-----------------

Evaluation Software Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Extract the ADRF6850_USB_v1_Installer zip file.
-  Inside the folders, run setup.exe.
-  Follow all prompts to install.
-  Default install destination is *C:\\Program Files (x86)\\ADRF6850_USB\\*
-  Run the executable either from a shortcut or by going to the location specified above and run the .exe file.

.. container:: centeralign

   \ |image2| *Figure 2. ADRF6850 Evaluation Software*\


Board Testing
~~~~~~~~~~~~~

-  Make sure that J21 is connected by default. Refer to Figure 3 below:

.. container:: centeralign

   \ |image3| *Figure 3. ADRF6850 Evaluation Setup*\


-  Attach the SDP-S board on the evaluation board then connect SDP-S to PC via USB. See Figure 1.
-  Connect J2 (IBBP RF OUT) to the input of a spectrum analyzer. Connect the 50Ω termination to J3. Set up the analyzer as follows:

   -  **Ref:** 0 dBm
   -  **Center Freq.:** 20 MHz
   -  **Freq. Span:** 5 MHz
   -  **RBW and VBW:** 100 KHz
   -  **Attn.:** 30 dB (adjust until noise floor like in Figure 4 is achieved)

-  Connect a high-frequency signal generator to J9 (RF IN). Set the signal generator output to **520 MHz and 0 dBm**, then enable the output.
-  Connect 3.3V 0.5A supply to VCC and GND test points then 0V VGAIN. Enable the supplies. The 3.3V supply should be sourcing current between 110 mA and 135 mA.
-  Run the evaluation software on PC. Refer to Figure 2.

   -  Click “Select SPI Mode” (top left).
   -  Click “Write Default Settings” (just to the right of above button). The +3.3V current should increase to between 310 mA and 380 mA.
   -  Set “LO Frequency” to 540MHz and click “Program LO Frequency”.

-  A tone at **20MHz** with a level of **-2 dBm to -4 dBm** should appear on the spectrum analyzer. The tone should be steady at a frequency of 20MHz. Refer to the screenshot in Figure 4.

.. container:: centeralign

   \ |image4| *Figure 4. IBBP Output Spectral Plot at IF = 20 MHz*\


Hardware Description
--------------------

Power Supplies
~~~~~~~~~~~~~~

An external +3.3 V supply (DUT + 3.3 V) powers each of the nine VCCx supplies on the ADRF6850 as well as the 13.5 MHz clock reference.

Recommended Decoupling for Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initially, the external +3.3 V supply is decoupled by a 10 μF capacitor and then further by a parallel combination of 100 nF and 56 pF capacitors that are placed as close to the DUT as possible for good local decoupling. The impedance of all these capacitors should be low and constant across a broad frequency range. Surface-mount multilayered ceramic chip (MLCC) Class II capacitors provide very low ESL and ESR, which assist in decoupling supply noise effectively. They also provide good temperature stability and good aging characteristics. Capacitance changes per the bias voltage that is applied. Larger case sizes have less capacitance change vs. applied bias voltage, and also lower ESR but higher ESL. A combination of 0402 size cases for the 56 pF capacitors and 0603 size cases for the 100 nF capacitors give a good compromise allowing the 56 pF capacitors to be placed as close as possible to the supply pins on the top side of the PCB with the 100 nF capacitors placed on the bottom side of the PCB quite close to the supply pins. X5R and X7R capacitors are examples of these types of capacitors and are recommended for decoupling.

Baseband Outputs and VOCM
~~~~~~~~~~~~~~~~~~~~~~~~~

The pair of I and Q baseband outputs are connected to the board by SMA connectors. They are ac-coupled to the output connectors. VOCM, which sets the common-mode output voltage, is grounded and the internal baseband (VOCM) reference is selected by Register CR29, Bit 6. If the external baseband (VOCM) reference is selected by setting this bit to a 0, then a voltage needs to be applied through the pair of VCOM and GND test points and R20 needs to be removed.

Loop Filter
~~~~~~~~~~~

A fourth-order loop filter is provided at the output of the charge pump and is required to adequately filter noise from the Σ-Δ modulator used in the N-divider. With the charge pump current set to a midscale value of 2.5 mA and using the on-chip VCO, the loop bandwidth is approximately 50 kHz, and the phase margin is 55°. C0G capacitors are recommended for use in the loop filter because they have low dielectric absorption, which is required for fast and accurate settling time. The use of non C0G capacitors may result in a long tail being introduced into the PLL settling time transient.

Reference Input
~~~~~~~~~~~~~~~

The reference input can be supplied by a 13.5 MHz Jauch clock generator or by an external clock through the use of Connector J7. The frequency range of the reference input is from 10 MHz to 300 MHz with the PFD frequency limited to a maximum of 30 MHz. Double the 13.5 MHz clock to 27 MHz by using the on-chip reference frequency doubler to optimize phase noise performance.

TESTLO Inputs
~~~~~~~~~~~~~

These pins are differential test inputs that allow a variety of debug options. On this board, the capability is provided to drive these pins with an external 4× LO signal that is then applied to an Anaren balun to provide a differential input signal.

When driving the TESTLO pins, the PLL can be bypassed, and the demodulator can be driven directly by this external LO signal. The frequency of the LO signal needs to be 4 times the operating frequency. These inputs also require a dc bias. A dc bias of 3.3 V is the default option used on the board.

LOMON Outputs
~~~~~~~~~~~~~

These pins are differential LO monitor outputs that provide a replica of the internal LO frequency at 1× LO. The single-ended power in a 50 Ω load can be programmed to −24 dBm, −18 dBm, −12 dBm, or −6 dBm. These open-collector outputs must be terminated to 3.3 V. Because both outputs must be terminated to 50 Ω, options are provided to terminate to 3.3 V using on-board 50 Ω resistors or by series inductors (or a ferrite bead), in which case the 50 Ω termination is provided by the measuring instrument.\\

CCOMPx Pins
~~~~~~~~~~~

The CCOMPx pins are internal compensation nodes that must be decoupled to ground with a 100 nF capacitor.

MUXOUT
~~~~~~

MUXOUT is a test output that allows different internal nodes to be monitored. It is a CMOS output stage that requires no termination.

Lock Detect (LDET)
~~~~~~~~~~~~~~~~~~

Lock detect is a CMOS output that indicates the state of the PLL. A high level indicates a locked condition, and a low level indicates a loss of lock condition.

RF Inputs (RFI, RFCM, /RFI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

RFI and /RFI are 50 Ω internally biased RF inputs. For single-ended operation as demonstrated on the evaluation board, RFI must be ac-coupled to the source and /RFI must be ac-coupled to the ground plane. RFCM is the RF input common-mode pin. It should be connected to /RFI when driving the input in single-ended mode. When driving the input differentially using a balun, connect this pin to the common terminal of the output coil of the balun.

VGAIN
~~~~~

The VGAIN pin sets the gain of the VGA. The VGAIN voltage range is from 0 V to 1.5 V. This allows the gain of the VGA to vary from 0 dB to +60 dB.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6850-evalz_setup_with_labels_v2.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6850_eval_software.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6850_j21_default_connection.png
   :width: 200px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/sdp/adrf6850_fft.png
   :width: 600px
