EVALUATING THE AD9776A/AD9778A/AD9779A DIGITAL-TO-ANALOG CONVERTERS
===================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9776A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9776A.html>`/:adi:`AD9778A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9778A.html>`/:adi:`AD9779A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9779A.html#eb-overview>` evaluation board to characterize :adi:`AD9776A`/:adi:`AD9778A`/:adi:`AD9779A` 12-/14-/16- bit 1GSPS high-speed digital-to-analog converter.

This guide shows how AD977xA-DPG2-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have DPG2 and DPG3 controller boards.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. EVAL-AD977xA Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  `Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2_evaluation_board_quick_start_guide.pdf>`_ for DPG2/DPG3 USERS
-  Data Sheet: :adi:`AD977xA <static/imported-files/data_sheets/AD9776A_AD9778A_AD9779A.pdf>`
-  IBIS Models: :adi:`AD9779A <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9779a.ibs>`, :adi:`AD9778A <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9778a.ibs>`, :adi:`AD9776A <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9776a.ibs>`
-  Schematics: `AD9779A-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2-ebz_revd_schematic.pdf>`_
-  Bill of Materials: `AD9779A-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2-ebz_revd_bom_customer.xls>`_
-  PCB Gerber files: `AD9779A-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2-ebz_revd_gerber_files.zip>`_
-  PCB BRD file: `AD9779A-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2-ebz_revd.zip>`_
-  PCB Layout PDF: `AD9779A-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9779a-dpg2-ebz_revd_layout.pdf>`_

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9776A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9776A.html>`/:adi:`AD9778A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9778A.html>`/:adi:`AD9779A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9779A.html#eb-overview>` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12Vdc 1A Wall Adapter for SDP-H1
-  5Vdc 1A power supply (banana plug) for the evaluation board.
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  High-Frequency Continuous Wave Generator (Clock Source)
-  Signal/Spectrum Analyzer
-  (2) USB A to USB Mini Cables
-  (2) SMA Cables

Quick Start Guide
-----------------

-  Attach :adi:`AD9776A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9776A.html>`/:adi:`AD9778A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9778A.html>`/:adi:`AD9779A-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9779A.html#eb-overview>` to SDP-H1 FMC connector using the AD-DAC-FMC-ADP adapter board.
-  Connect SDP-H1 to PC via USB and to a 12V 1A power supply.
-  Connect the evaluation board to PC via USB and to a 5Vdc 1A power supply on P4 and P5. Refer to Figure 1.
-  Connect continuous wave generator for clock input to SMA J2 DAC_CLK/DAC_CLK_P and DAC output from SMA J4 (IOUT1P) or SMA J8 (IOUT2P) to a signal/spectrum analyzer.
-  Set clock input to 400MHz, 3dBm.
-  Open ACE. The board will be automatically recognized by the software. Click the plugin. Otherwise, install the :adi:`ACE plugin <plugins/ace/Board.AD9779A.1.2020.3200.acezip>` for AD977xA. |image2|\

.. container:: centeralign

   
   //Figure 2. AD9779A Plugin *


\* To change the settings of the AD977xA chip, double click on the AD977xA block on the board view to access the chip. The default values for the register is displayed and set. The values can be changed on the Chip View GUI, or on the* **Memory Map** *for registers not available in the GUI. For more info on the memory map, refer to* :adi:`AD977XA <static/imported-files/data_sheets/AD9776A_AD9778A_AD9779A.pdf>` *datasheet. Once the desired values are set, Click* **Apply Changes** *and then* **Read All** *on the upper right window. \

.. container:: centeralign

   *\ Figure 3. Apply Changes and Read All button *


\* Apply the values in the* **Initial Configuration** *wizard as shown in Figure 4. \

.. container:: centeralign

   *\ Figure 4. AD9779A Initial Configuration Window\ *


\* Start DPG Downloader Lite. At the SDP-H1 part of the software, the device part number and clock frequency should be displayed. \

.. container:: centeralign

   *\ Figure 5. DPG Lite Session for EVAL-AD9779A *


\* In DPG Downloader Lite, from the* **Add Generator Waveforms** *pulldown menu select* **Single Tone** *and apply the settings as shown in Figure 5. Set the* **Data Rate** *to 100MHz and Desired Frequency to 10.2MHz. Uncheck the* **Unsigned Data** *box and Check the* **Generate Complex Data (I & Q)**\ *. \* Select the I/Q tone from the* **I/Q Data Vector** *pulldown menu. \* Press the download arrow and then the play button. The spectrum similar to Figure 6 should appear in the signal/spectrum analyzer.\ \

.. container:: centeralign

   *\ Figure 6. Spectrum Output for AD9779A; Fdac = 100MSPS, Fout = 10.2MHz//


Using the AD9516 as clock source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, solder jumpers JP5 and JP6 are configured to drive the AD977xA clock inputs directly by SMA J2. This jumper setting is shown on Figure 7a. The AD9516 is included so the user can test the performance (e.g. ACLR) with the AD9516 clock multiplication.

-  To use the AD9616 to drive the clock inputs, the solder jumpers should be reconfigured as shown in Figure 7b. Connect continuous wave generator for clock input to SMA J1 (REF_CLK_IN). Set to 100MHz, 3dBm output. |image3|\

.. container:: centeralign

   
   *Figure 7a (left). Direct Clock Configuration; Figure 7b (right) AD9516 Clock Configuration*\


-  On the ACE Initial Configuration window, apply the following values shown on Figure 8. |image4|\

.. container:: centeralign

   
   *Figure 8. Settings for using AD9516 as clock source*\


-  Make sure that the PLL Lock LED on the ACE GUI and the LD LED on the evaluation board are lit up.\ |image5|\

.. container:: centeralign

   
   *Figure 9. LD and PLL Lock LED*\


-  Proceed with the DPG Lite procedure above.

Using the ADL5375 Modulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, solder jumpers JP1, JP2, JP3, and JP4 are configured to route the DAC outputs to SMA J4 (IOUT1P) and to J8 (IOUT2P). This jumper setting is shown on Figure 10a. To connect the DAC output to the filter that feeds into the ADL5375, the solder jumpers should be reconfigured as shown in Figure 7b. Source the desired LO of the modulator (e.g. 900 or 1800MHz, 3dBm) on SMA J19 (LO IN). The ADL5375 Modulator output can be observed on SMA J6 (RF OUT). |image6|\

.. container:: centeralign

   *Figure 10a (left). DAC Output Configuration; Figure 10b (right) Modulator Output Configuration*\


Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. If unexpected results occur:

-  Check the voltage rails of the evaluation board. P4, P5, and TP4 should be 5V; TP6, TP8, and TP16 should be 3.3V; TP1 and TP3 should be 1.8V.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board is lit up. Reconnect the board to the FMC connector of SDP-H1 if not lit up.
-  Check if the SDP-H1 is being supplied properly by 12Vdc adaptor. Some LEDs on the SDP-H1 should lit up.
-  Perform a chip reset by pressing S2 on the AD977xA evaluation board.
-  Power cycle both the SDP-H1 and the AD977xA evaluation board.
-  Probe C76 and C78 to make sure a clock signal is being sent into the DAC.
-  Check if XD1 is lit up on the evaluation board. Reconnect/replace the USB cable connection to the evaluation board if it's not lit up.
-  Disconnect and reconnect the SDP-H1 and AD977xA evaluation board. Reopen ACE and DPG Lite software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9779a_setup.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ace_startw.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9516_enables.jpg
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9516_config.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ld_led.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/modulator_output_config.jpg
   :width: 800px
