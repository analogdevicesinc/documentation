EVALUATING THE ADUM141E1S QUAD CHANNEL ISOLATOR
===============================================

Preface
-------

| The :adi:`EVAL-ADUM141E1S` supports the ADUM141E1S quad-channel digital isolator based on Analog Devices, Inc., iCoupler® technology. Combining high speed CMOS and monolithic air core transformer technology, the :adi:`ADUM141E1S <ADuM141ES>` provideds outstanding performance characteristics superior to alternatives such as optocoupler devices and other integrated couplers. The :adi:`ADUM141E1S <ADuM141ES>` offers low propagation delay and low pulse width distortion as well a tight channel matching. The :adi:`ADUM141E1S <ADuM141ES>` features two different fail-safe options by which the outputs transition to a pre-determined state when the input power supply is not applied or the inputs are disabled.
| Complete specifications for the :adi:`ADUM141E1S <ADuM141ES>` are provided in the :adi:`ADUM141E1S <ADuM141ES>` data sheet available from Analog Devices, Inc., and should be consulted in conjunction with this Wiki user guide when using the evaluation board.
| ===== Overview ===== The :adi:`EVAL-ADUM141E1S <ADuM141ES>` board, shown in Figure 1, can be used to evaluate the performance and data sheet specifications of the :adi:`ADUM141E1S <ADuM141ES>`. Figure 2 shows the schematic of the :adi:`EVAL-ADUM141E1S <ADuM141ES>` circuit which can be used to test the accuracy of the :adi:`ADUM141E1S <ADuM141ES>` and perform other tests. The :adi:`EVAL-ADUM141E1S` is a 4-layer PC board, complete with ground and power layers as shown in the Evaluation Board Schematics and Artwork section.

Helpful Documents
-----------------

-  :adi:`ADUM141E1S <ADuM141ES>` military data sheet
-  :adi:`ADUM141E` data sheet
-  :adi:`AN-1478 Application Note <media/en/technical-documentation/application-notes/an-1478.pdf>`, *Isolated SPI Bus for Distinct System Requirements*
-  :adi:`CN-0385 Circuit Note <cn0385>`, *Isolated, Multichannel Data Acquisition System with PGIA for Single-Ended and Differential Industrial Level Signals*
-  :adi:`Analog Dialogue, Volume 50, Number 4 <analog-dialogue/articles/plc-dcs-analog-input-module-breaks-barriers-in-isolation11.html>`, "PLC DCS Analog Input Module Design Breaks Barriers in Channel-to-Channel Isolation and High Density".
-  :adi:`Analog Devices Webcast <education/education-library/webcasts/using-on-off-keying-digital-isolators-harsh-environments.html>`, "Using On-Off Keying, Digital Isolators in Harsh Environments".

Evaluation Board Files
----------------------

The evaluation board layout, BOM, and schematic files for the :adi:`EVAL-ADUM141E1S` board can be downloaded from the links below.

| **DISCLAIMER: The footprint used for layout on the evaluation board is provided for general reference only. The exact footprint required for mounting this device onto a printed circuit board will depend on the device lead forming and may differ from what is provided herein. It is recommended to generate specific footprint information from the users lead forming specifications when placing this device on the application printed circuit board.**
| ==== Artwork: ==== `09-047807-01A.zip <https://wiki.analog.com/_media/resources/eval/09-047807-01A.zip>`_
| ==== BOM: ==== `05-047807-01-a1.zip <https://wiki.analog.com/_media/resources/eval/05-047807-01-a1.zip>`_
| ==== Schematic: ==== `02_047807a_top_0926.pdf <https://wiki.analog.com/_media/resources/eval/02_047807a_top_0926.pdf>`_

Evaluation Board
----------------

|image1|\

.. container:: centeralign

   \ *Figure 1. ADUM141E1S Evaluation board—*\ :adi:`EVAL-ADUM141E1S`\


Evaluation Board Schematic
--------------------------

|image2|\

.. container:: centeralign

   \ *Figure 2. ADUM141E1S Evaluation Board Schematic—*\ :adi:`EVAL-ADUM141E1S`\


Figure 2 shows the :adi:`ADUM141E1S <ADuM141ES>` schematic of the :adi:`EVAL-ADUM141E1S` evaluation board. U1 is the :adi:`ADUM141E1S <ADuM141ES>` in the center of the board and Pin 1 is the top-left pad with respect to the notch in the silkscreen’s package outline.

Equipment Required
~~~~~~~~~~~~~~~~~~

-  Agilent B1110A Pulse generator or equivalent (capable of supplying 75 MHz square wave with at leave 4 V amplitude and 50% duty cycle
-  MSOX6004A Keysight Oscilloscope (1 GHz - 6 GHz, 20 GSa/s) with N2796 active probe (2 GHz BW, 1 MΩ, <1 pF) or equivalent
-  Keysight (Agilent) E3631A Triple Output Power Supply or equivalent
-  SMA to BNC coaxial cable
-  50Ω SMD resistors
-  15 pF capacitors
-  Cables for power supply connections

Power Input
~~~~~~~~~~~

Each side of the :adi:`ADUM141E1S <ADuM141ES>` requires an off-board power source. The power source must be independent if common-mode voltages are applied across the isolation barrier or damage may occure to the power supply.

Example Test Procedure
~~~~~~~~~~~~~~~~~~~~~~

-  Install the 50Ω input resistors (R6 and R16).
-  Install the 15 pF load capacitors (C8, C9, C10, and C11).
-  Connect the evaluation board to the test equipment. See Figure 2 below. Note: Make sure the pulse generator and power supply outputs are disabled.\ |image3|\

.. container:: centeralign

   \ *Figure 2. ADUM141E1S Example Test Configuration—*\ :adi:`EVAL-ADUM141E1S`\


-  Once the connections have been made in Step 3 (Figure 2) set both output of the power supply to 5V. Enable the outputs.
-  Configure the pulse generator to produce a 0V – 5V step, 75MHz Square Wave with an offset value of 2.5V. (If using the Agilent B1110A the max amplitude at 75MHz will be 4 V) Enable the pulse generator output. Note: This provides an input to the A Channel (VIA, J1) of the evaluation board.
-  Set the oscilloscope to the following settings: CH1 = 750 mV/div, Time Base = 2 ns/div.
-  Select the following measurements for CH1: Amplitude, Rise Time, Fall Time, and Frequency.
-  Use the N2796A active probe to capture the A Channel Output (VOA) at connector J5 (a 75 MHz square with an amplitude of approximately 5 V should be visible). An example plot is shown below in Figure 3.\ |image4|\

.. container:: centeralign

   \ *Figure 3. ADUM141E1S Example Output Waveforem—*\ :adi:`EVAL-ADUM141E1S`\


-  Check the supply current on both outputs of the power supply to ensure that IDD1 and IDD2 does not exceed 25 mA.
-  Repeat steps 6 and 7 for any of the remaining channels desired for test (B, C and/or D) by connecting the pulse generator to the appropriate input channel and the oscilloscope to its corresponding output. Refer to the table below for connections:|image5|\

.. container:: centeralign

   \ *Table 2. ADUM141E1S Evaluation Board Connection Table—*\ :adi:`EVAL-ADUM141E1S`\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ADUM141E1S_eval_board.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ADUM141E1S_eval_board_schematic.png
   :width: 1600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ADUM141E1S_eval_board_connections.jpg
   :width: 1600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/adum141e1s_example_output_waveform.png
   :width: 1600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/adum141e1s_connection_table.png
   :width: 600px
