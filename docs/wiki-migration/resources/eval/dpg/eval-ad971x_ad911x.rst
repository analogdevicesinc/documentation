EVALUATING THE AD9114/AD9115/AD9116/AD9117 AND THE AD9714/AD9715/AD9716/AD9717 DIGITAL-TO-ANALOG CONVERTERS
===========================================================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9114-DPG2-EBZ <eval-ad9114>`/:adi:`AD9115-DPG2-EBZ <eval-ad9115>`/:adi:`AD9116-DPG2-EBZ <eval-ad9116>`/:adi:`AD9117-DPG2-EBZ <eval-ad9117>` or :adi:`AD9714-DPG2-EBZ <eval-ad9714>`/:adi:`AD9715-DPG2-EBZ <eval-ad9715>`/:adi:`AD9716-DPG2-EBZ <eval-ad9716>`/:adi:`AD9717-DPG2-EBZ <eval-ad9717>` evaluation board to characterize :adi:`AD9114`/:adi:`AD9115`/:adi:`AD9116`/:adi:`AD9117` or :adi:`AD9714`/:adi:`AD9715`/:adi:`AD9716`/:adi:`AD9717` 8-/10-/12-/14-bit 125Msps low-power high-speed digital-to-analog converter.

This guide shows how AD911x-DPG2-EBZ/AD971x-DPG2-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG2 or DPG3 controller board.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. EVAL-AD911x / EVAL-AD971x Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  `UG-073 <https://wiki.analog.com/_media/resources/eval/dpg/ug-073.pdf>`__ for DPG2/DPG3 users and for reference on evaluation board jumper selection
-  Data Sheets: :adi:`AD971x <static/imported-files/data_sheets/AD9714_9715_9716_9717.pdf>`, :adi:`AD911x <static/imported-files/data_sheets/AD9114_9115_9116_9117.pdf>`
-  IBIS Models: :adi:`AD9717 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9717.ibs>`, :adi:`AD9716 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9716.ibs>`, :adi:`AD9715 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9715.ibs>`, :adi:`AD9714 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9714.ibs>`, :adi:`AD9117 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9117.ibs>`, :adi:`AD9116 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9116.ibs>`, :adi:`AD9115 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9115.ibs>`, :adi:`AD9114 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9114.ibs>`
-  Schematics `AD9717-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9717-dpg2-ebz_reva_schematic.pdf>`__ `AD9117-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9117-dpg2-ebz_reva_schematic.pdf>`__
-  Bill of Materials `AD9717-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9717-dpg2-ebz_reva_bom.xls>`__ `AD9117-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9117-dpg2-ebz_reva_bom.xls>`__
-  PCB Gerber files `AD9717-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9717-dpg2-ebz_reva_gerber_files.zip>`__ `AD9117-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9117-dpg2-ebz_reva_gerber_files.zip>`__
-  PCB BRD file `AD9717-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9717-dpg2-ebz_reva.zip>`__ `AD9117-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9117-dpg2-ebz_reva.zip>`__
-  PCB Layout PDF `AD9717-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9717-dpg2-ebz_reva_layout.pdf>`__ `AD9117-DPG2-EBZ RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9117-dpg2-ebz_reva_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (recommended; installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9114-DPG2-EBZ <eval-ad9114>`/:adi:`AD9115-DPG2-EBZ <eval-ad9115>`/:adi:`AD9116-DPG2-EBZ <eval-ad9116>`/:adi:`AD9117-DPG2-EBZ <eval-ad9117>` or :adi:`AD9714-DPG2-EBZ <eval-ad9714>`/:adi:`AD9715-DPG2-EBZ <eval-ad9715>`/:adi:`AD9716-DPG2-EBZ <eval-ad9716>`/:adi:`AD9717-DPG2-EBZ <eval-ad9717>` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12Vdc 1A Wall Wart for SDP-H1
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  (2) USB A to USB Mini Cables
-  (2) SMA Cables

Quick Start Guide
-----------------

-  Attach :adi:`AD9114-DPG2-EBZ`/:adi:`AD9115-DPG2-EBZ`/:adi:`AD9116-DPG2-EBZ`/:adi:`AD9117-DPG2-EBZ`/:adi:`AD9714-DPG2-EBZ`/:adi:`AD9715-DPG2-EBZ`/:adi:`AD9716-DPG2-EBZ`/:adi:`AD9717-DPG2-EBZ` to SDP-H1 FMC connector using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J10 and DAC output from S4 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB. Refer to Figure 1.
-  Connect SDP-H1 to PC via USB and to a 12Vdc 1A power supply.
-  Set clock input to 125MHz and 3dBm.
-  Press SW1 Button to reset the AD9114/AD9115/AD9116/AD9117/AD9714/AD9715/AD9716/AD9717.
-  Open ACE. The board will be automatically recognized by the software. Otherwise, install the plugin for Board.AD911x or Board.AD971x in ACE Plugin Manager Available packages.
-  Start DPG Lite or DPG Downloader. At the SDP-H1 part of the software, the device part number and clock frequency should be displayed.
-  In ACE, apply the values in the Initial Configuration wizard as shown in Figure 2.\ |image2|\

.. container:: centeralign

   
   *Figure 2. ACE Initial Configuration Wizard for EVAL-AD9717*\


-  In DPG Lite or DPG Downloader, from the Add Generator Waveforms pulldown menu select Single Tone and apply the settings as shown in Figure 3. Set the desired frequency to 15 MHz. Set DAC resolution to the DAC’s number of bits (14 for AD9717/9117, 12 for AD9716/9116, and so on). Check the Unsigned Data box.\ |image3|\

.. container:: centeralign

   
   *Figure 3. DPG Lite session for EVAL-AD9717*\


-  Select the tone from the Data Vector pulldown menu.
-  Press the download arrow and then the play button. The spectrum similar to Figure 4 should appear in the signal/spectrum analyzer.\ |image4|\

.. container:: centeralign

   
   *Figure 4. EVAL-AD9717 FFT for Fdac=125MHz, Fout=15MHz*\


Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. It also provides information on how to check for proper operation when using the modulator in the signal chain. If unexpected results occur

-  Reset the part (SW1) and rerun the SPI software.
-  Sync/reset the clock (SW2) when using the clock chip.
-  Check the voltage at TP30 (COREVDD), which should be 1.75 V.
-  Check the voltage at TP3 (VREF), which should be 1.0 V.
-  Probe S11 (DATACLK) to be sure that the DAC is properly receiving data and that a clock signal is present. This signal can also be probed at R64 near the part on-board (should be unsoldered from initial setup instructions).
-  When using the modulator, check to make sure the common-mode voltage is 0.5 V at the input of the modulator by probing at R24 or R61 for the I or Q channels, respectively.

If the common-mode voltage is not as expected, unplug the board and check the resistances at R13, R14, R52, and R53 for the correct values of the particular board. If a proper reading is not present, unsolder J13, J14, J19, and J23, which removes the resistors from the parallel connection with 1 kΩ/100 Ω at the input of the modulator to measure the individual resistances of those components. Check if the resistance values are still incorrect and if so, change out for the appropriate values listed above. If not, try resoldering the jumpers and test again to make sure there was not a problem with the previous connection.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/sdp-h1-set-up_withlabels.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9717.sdph1.ace_2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9717.sdph1.dpg-lite.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad717_sdph1_output_1.png
   :width: 600px
