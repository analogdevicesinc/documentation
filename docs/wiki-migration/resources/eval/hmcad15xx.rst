EVALUATING THE HMCAD1511/HMCAD1520 ANALOG-TO-DIGITAL CONVERTERS
===============================================================

Preface
-------

This user guide describes the :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` and :adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` evaluation boards, which provide the support circuitry required to operate the :adi:`HMCAD1520` and :adi:`HMCAD1511` in its various modes and configurations. The application software used to interface with the device is also described.

This guide shows how HMCAD15XX-EBZ works with the :adi:`SDP-H1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html#eb-overview>` (EVAL-SDP-CH1Z) controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the old evaluation system developed by Hittite which uses the Xilinx SP-601 controller board.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| //Figure 1. HMCAD15xx-EBZ (left) and EVAL-SDP-CH1Z (right) Setup //


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  `Previous User Guide <https://wiki.analog.com/_media/resources/eval/eval01-hmcad15xx_user_guide_analog_devices_wiki_.pdf>`__ for EVAL01-HMCAD15xx Evaluation Board
-  :adi:`HMCAD1520 <media/en/technical-documentation/data-sheets/hmcad1520.pdf>` and :adi:`HMCAD1511 <media/en/technical-documentation/data-sheets/hmcad1511.pdf>` Datasheet
-  `HMCAD15xx-EBZ Schematic <https://wiki.analog.com/_media/resources/eval/02-067426-01-d.pdf>`__
-  `HMCAD15xx-EBZ BOM <https://wiki.analog.com/_media/resources/eval/05-067426-01-d.xls>`__
-  `PCB Layout <https://wiki.analog.com/_media/resources/eval/08-067426-01-b.pdf>`__
-  `PCB Gerber Files <https://wiki.analog.com/_media/resources/eval/20-067426-01b_1_.zip>`__
-  `HMCAD15xx-EBZ Interleaving Spurs Calculator <https://wiki.analog.com/_media/resources/eval/hmcad15xx_interleaving_spur_calculator_rev1.xlsx>`__
-  `hmcad_sdph1_xxxdeg FPGA Images <https://wiki.analog.com/_media/resources/eval/hmcad_sdph1_xxxdeg.zip>`__
-  `HMCAD15xx SDP-H1 Phase DDR Slides <https://wiki.analog.com/_media/resources/eval/hmcad_sdph1_phase_ddr.pptx>`__

.. container:: hide

   \ `HMCAD15xx-EBZ Interleaving Spurs Calculator <https://wiki.analog.com/_media/resources/eval/hmcad15xx_interleaving_spur_calculator.xls>`__\


Software Needed:
----------------

-  :adi:`Analysis \| Control \| Evaluation (ACE) Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
-  :adi:`Visual Analog <en/design-center/interactive-design-tools/visualanalog.html>`

Hardware Needed:
----------------

-  :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>`/:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` Evaluation Board
-  :adi:`SDP-H1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-sdp-h1.html#eb-overview>` (EVAL-SDP-CH1Z) Board
-  12Vdc 1A Wall Adapter for SDP-H1
-  PC with ACE and Visual Analog Software Applications
-  (2) High-Frequency Continuous Wave Generator (Clock and Analog Input Source)
-  (2) SMA Cables
-  USB A to USB Mini Cables
-  Bandpass Filter

Evaluation Board Hardware
-------------------------

Analog Inputs
~~~~~~~~~~~~~

:adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` /:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` evaluation board has four input channels that supports single-ended to differential conversion with the use of a balun. By default, all input channels 1-4 (SMAs J3, J5, J6 and J7) are balun-coupled. Alternatively, input channel 1 (SMAs J3 and J4) can be configured to differential to differential conversion, and input channel 2 (SMA J5) can be configured to single-ended to differential conversion using the onboard :adi:`LTC6419 <en/products/ltc6419.html>` high-speed differential ADC driver. Moreover, results for optional amplifier configuration can be seen in :doc:`Optional Amplifier Configuration Results </wiki-migration/resources/eval/hmcad15xx>`.

Refer to the table below for the optional amplifier configuration.

+-----------------------------+--------------------------------------+-----------------------------+------------------------------+------------------------------+
| Analog Input Channel Number | Default Input Driver, AC/DC coupling | Signal type on Input/Output | Install                      | Uninstall                    |
+=============================+======================================+=============================+==============================+==============================+
| 1                           | LTC6419, DC coupling, Unity Gain     | Differential/Differential   | R41, R42, R44, R45, R60, R61 | C51, C52, R23, R24, R56, R57 |
+-----------------------------+--------------------------------------+-----------------------------+------------------------------+------------------------------+
| 2                           | LTC6419, DC coupling, Unity Gain     | Single-Ended/Differential   | R46, R58, R59                | C53, R54, R55, R23, R24      |
+-----------------------------+--------------------------------------+-----------------------------+------------------------------+------------------------------+

Analog Input Vcm
~~~~~~~~~~~~~~~~

The :adi:`HMCAD1520 <media/en/technical-documentation/data-sheets/hmcad1520.pdf>`/:adi:`HMCAD1511 <media/en/technical-documentation/data-sheets/hmcad1511.pdf>` supplies the common-mode voltage at half-supply (0.9V) for all the analog input channels. No external supply is needed for the input Vcm.

Clocking
~~~~~~~~

The :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` evaluation board uses an external clock source on SMA J1 as default.

On the other hand, the :adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` evaluation board has an on-board 1GHz crystal for clocking the :adi:`HMCAD1511 <media/en/technical-documentation/data-sheets/hmcad1511.pdf>`. The user can also configure the board to use an external clock source for the :adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` board.

Refer to the table below for alternative clock configuration.

=================== ======= =========
Clock Configuration Install Uninstall
=================== ======= =========
Onboard             R13     R12
External            R12     R13
=================== ======= =========

Power Supply
~~~~~~~~~~~~

Both the :adi:`HMCAD1520` and :adi:`HMCAD1511` were being supplied by ADM7154 with 1.8V. The board can be modified to bypass the LDO so the :adi:`HMCAD1520` and :adi:`HMCAD1511` are directly supplied by the LTM8078 DC-DC regulator. To do this, change components **C3** to 100uF, **R6** to 200k, and install a ferrite bead to **R9**. Also, uninstall R8 and R10.

The supply rails for other components on the board (crystal, amplifier, etc) are isolated to the :adi:`HMCAD1520` and :adi:`HMCAD1511` supply rail. Refer to the board schematics for more info.

Quick Start Guide
-----------------

The following procedure below shows how to setup the evaluation board to capture 70MHz input signal at 1GSPS sampling rate:

-  Attach the :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>`/:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` evaluation board to the SDP-H1 FMC connector thru the P2 port. Refer to Figure 1.
-  Connect the SDP-H1 to PC via USB and to a 12V 1A power supply.
-  Open ACE, the evaluation board will automatically be recognized by the software. Otherwise, install the plugin for HMCAD1511/20 evaluation board.

   -  In ACE, go to Plug-in Manager.
   -  Under **Available Packages**, search **HMCAD1520** then click install.

-  Double click the **HMCAD1511/HMCAD1520 Board** and then double click the **HMCAD1511/HMCAD1520** blue chip. The onboard green LED should light up (DS1), indicating power is already supplied, and red LED (LED0) of SDP-H1 will start blinking.

.. container:: centeralign

   \ |image2|\ |image3|\ *Figure 2. HMCAD1511/20-EBZ ACE Board View Window*\


.. tip::

   Make sure that the state of the board is good (**State=Good**), check on the bottom-left corner.


-  Configure the initialization wizard settings shown in Figure 3. For :adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>`, select **External Clock** as clock source and input **1GHz** on the CLKIN.

.. container:: centeralign

   \ |image4|\ *Figure 3. HMCAD1511-EBZ Initialization Wizard Settings*\


-  Connect a continuous wave generator as an input signal on SMA **J7** with a frequency of **70MHz**.

.. important::

   Use a bandpass filter in between the signal source and the SMA connector.


-  For :adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>`, connect another continuous wave generator as the ADC clock. Set the clock frequency to **1GHz** and **10dBm** output level.
-  Going back to ACE Software, click **Proceed to Analysis** button and click on the **FFT** tab. Click **Run Once** button under **Capture** wizard to capture an FFT plot.
-  Observe the fundamental frequency and power. Adjust the signal source until fundamental power obtains approximately -1dBFS at 70MHz.

.. container:: centeralign

   \ |image5|\ *Figure 4. HMCAD1511-EBZ Fundamental Frequency and Power*\


-  If fundamental power achieved, click **Zoom to Fit** (|hmcad1511_zoomtofit.jpg|) to show graph at Fs/2, then click **Show Annotations** (|hmcad1511_annotations.jpg|) to show all the spurs' annotation within the plot. Refer to Figure 5.

.. container:: centeralign

   \ |image6|\ *Figure 5. HMCAD1511-EBZ (8-bit, single channel, Fs=1GHz, Fin=70MHz) FFT Analysis Results*\


-  To save the **Data Set**, click **Export** button on the **Results** wizard. Also, you click **Import** button to review the saved data set with a file format of "*.acesamples*".

.. container:: centeralign

   \ |image7|\ *Table 3. HMCAD1511-EBZ (8-bit, single channel, Fs=1GHz, Fin=70MHz) Results Comparison.*\


.. note::

   Note: SDP-H1 is limited to operate **Fin<375MHz**.


.. tip::

   
   -  If Spur_x is equal to Harm_x, then harmonic spectral power is **removed** and is set to -300dBc.
   -  If the result is a little bit poor due to calculation rounding-off, increase at least 2 bins at harmonic bins settings.
   


Interleaving Spurs Calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  You can download the

.. admonition:: Download
   :class: download

   \ **HMCAD15xx-EBZ Interleaving Spurs Calculator**\


in the :doc:`Helpful Files </wiki-migration/resources/eval/hmcad15xx>`, and input both the sampling and input frequencies on the yellow boxes provided. The calculator will provide the spur frequencies depending on the selected number of channels. In figure 6, the analog input signal is around **70MHz** with different sampling rate.

.. container:: centeralign

   \ |image8|\ *Figure 6. HMCAD1511-EBZ ACE vs Interleaving Spurs Calculator*\


Optional Amplifier Configuration Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section is intended to provide evaluation board characterization results on Differential-to-Differential configuration in Channel 1 using the LTC6419 amplifier as shown in Figure 7, and on Single-to-Differential configuration in Channel 2 using the said amplifier as shown in Figure 8.

.. container:: centeralign

   \ |image9|\ *Figure 7. Amplifier Path for Differential-to-Differential Configuration in CH1*\


.. container:: centeralign

   \ |image10|\ *Figure 8. Amplifier Path for Single-to-Differential Configuration in CH2*\


Troubleshooting Tips
--------------------

If the FFT window remains blank after Running Once in ACE, do the following:

-  Make sure there is a clock signal going to the ADC.
-  Check the 1.8V supply rails of the ADC. The onboard yellow LED indicates 12V is being supplied to the board.
-  Check if there's no error messages in ACE. If there is any, power cycle the board and restart the ACE software.
-  Make sure the SDP-H1 board is powered up and connected to the PC via USB.

If the FFT plot appears abnormal, do the following:

-  Make sure that the input signal is not overdriving the ADC. Limit the fundamental frequency to -1dBFS.
-  Check for the Vcm at the analog input path. The Vcm should be around 0.9V.
-  Make sure that the correct encoding is set in ACE. The default setting is Twos complement.
-  Check for any loose connections between the input SMA and the signal source. Same with the clock source if using an external clock.
-  If using the LTC6419 as the ADC driver, check the 5V supply rail and the 0.9V common mode voltage.
-  Make sure the correct resolution and channel configuration are set correctly on ACE.

If the FFT plot still appears distorted or does not produce a capture after following the steps above, do the following steps below:

-  Check the path **C:\\ProgramData\\Analog Devices\\ACE\\Plugins\\Board.HMCAD1520.1.2022...\\content\\FpgaImages** if this exists.
-  If yes, check if there is hmcad_sdph1.bit file inside the FPGA Images folder and if so, exclude the bit file inside.
-  Look for an appropriate FPGA image **hmcad_sdph1_xxxdeg** folder in the :doc:`Helpful Files </wiki-migration/resources/eval/hmcad15xx>`, copy it into the FPGA Images folder in the path, and rename it to **hmcad_sdph1.bit**.
-  Run the ACE software and proceed with the analysis. If running the FPGA image and still will not produce a good data capture, repeat the steps above until selected FPGA image will produce a good data capture. You may refer to the **HMCAD15xx SDP-H1 Phase DDR** pptx slides in the :doc:`Helpful Files </wiki-migration/resources/eval/hmcad15xx>`.
-  If after running all the FPGA images and still not produce a good data capture, contact the responsible applications engineer.

If the FFT plot appears normal but performance is poor, do the following:

-  Make sure that an appropriate analog filter is used on the input signal.
-  Make sure that the fundamental frequency is set to -1dBFS.
-  Make sure that the signal generators for the clock and the analog input are clean (low phase noise).
-  Make sure the correct resolution and channel configuration are set correctly on ACE.

If the ACE cannot detect the board or prompts an error message during data capture, do the following:

-  Make sure the SDP-H1 is powered correctly and connected to the PC via USB.
-  Make sure that the :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` /:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` is attached properly on the P1 port of the SDP-H1.
-  Make sure that the yellow LED on the :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` /:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` evalboard is lit up.
-  Power cycle both the :adi:`HMCAD1520-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1520.html>` /:adi:`HMCAD1511-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-HMCAD1511.html>` and the SDP-H1, and restart the ACE software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/hmcad1520_sdp_top.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511_boardview.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/hmcad1520_boardview.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/hmcad-8bit-1g-70m-single-config.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511_fundpower_-1dbfs.jpg
   :width: 400px
.. |hmcad1511_zoomtofit.jpg| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511_zoomtofit.jpg
.. |hmcad1511_annotations.jpg| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511_annotations.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/hmcad-8bit-1g-70m-single-fft.jpg
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/hmcad-result-table.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511_interleavingspurs.jpg
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/hmcad1511-8bit-quad-250mhz-70mhz-opamp-channel_1-12.61dbm.jpg
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/hmcad1520-8bit-quad-250mhz-70mhz-opamp-channel_2-10.53dbm.jpg
   :width: 600px
