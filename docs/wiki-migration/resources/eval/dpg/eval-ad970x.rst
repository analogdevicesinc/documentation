EVALUATING THE AD9704/AD9705/AD9706/AD9707 DIGITAL-TO-ANALOG CONVERTER
======================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9704-DPG2-EBZ <eval-ad9704>`/:adi:`AD9705-DPG2-EBZ <eval-ad9705>`/:adi:`AD9706-DPG2-EBZ <eval-ad9706>`/:adi:`AD9707-DPG2-EBZ <eval-ad9707>` evaluation board to characterize :adi:`AD9704`/:adi:`AD9705`/:adi:`AD9706`/:adi:`AD9707` 8-/10-/12-/14-bit 175Msps high-speed digital-to-analog converter.

This guide shows how AD970x-DPG2-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG2 or DPG3 controller board.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. EVAL-AD970x Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  `Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2_evaluation_board_quick_start_guide.pdf>`__ for DPG2/DPG3 users
-  :adi:`AD970x Data Sheet <static/imported-files/data_sheets/AD9704_9705_9706_9707.pdf>`
-  IBIS Models: :adi:`AD9707 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9707.ibs>`,\ :adi:`AD9706 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9706.ibs>`,\ :adi:`AD9705 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9705.ibs>`,\ :adi:`AD9704 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9704.ibs>`
-  `Schematic <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2-ebz_revb_schematic.pdf>`__
-  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2-ebz_revb_bom.xls>`__
-  `PCB Gerber files <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2-ebz_revb_gerber_files.zip>`__
-  `PCB BRD file <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2-ebz_revb.zip>`__
-  `PCB Layout PDF <https://wiki.analog.com/_media/resources/eval/dpg/ad9707-dpg2-ebz_revb_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9704-DPG2-EBZ`/:adi:`AD9705-DPG2-EBZ`/:adi:`AD9706-DPG2-EBZ`/:adi:`AD9707-DPG2-EBZ` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12Vdc 1A Wall Adapter for SDP-H1
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  (2) USB A to USB Mini Cables
-  (2) SMA Cables

Quick Start Guide
-----------------

-  Attach AD9704-DPG2-EBZ/AD9705-DPG2-EBZ/AD9706-DPG2-EBZ/AD9707-DPG2-EBZ to SDP-H1 FMC connector using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J10 and DAC output from S4 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB. Refer to Figure 1.
-  Connect SDP-H1 to PC via USB and to a 12Vdc 1A power supply.
-  Set clock input to 175MHz and 3dBm.
-  Press SW1 Button to reset the AD9704/AD9705/AD9706/AD9707.
-  Open ACE. The board will be automatically recognized by the software. Otherwise, install the plugin for AD9704/05/06/07 evaluation board.
-  In ACE, apply the default values in the Initial Configuration wizard as shown in Figure 2.\ |image2|\

.. container:: centeralign

   
   *Figure 2. ACE Initial Configuration Wizard for EVAL-AD9707*\


-  Start DPG Lite or DPG Downloader. At the SDP-H1 part of the software, the device part number and data clock frequency of 175MHz should be displayed.
-  In DPG Lite or DPG Downloader, from the "Add Generator Waveforms" pulldown menu select "Single Tone" and apply the settings as shown in Figure 3. Set data rate to 175MHz and desired frequency to 20MHz. Set DAC resolution to the DAC’s number of bits (14 for AD9707, 12 for AD9706, and so on). Check off the "Unsigned Data" box.\ |image3|\

.. container:: centeralign

   
   *Figure 3. DPG Lite session for EVAL-AD9707*\


-  Select the tone from the "Data Vector" pulldown menu.
-  Press the download arrow and then the play button. The FFT similar to Figure 4 should appear in the signal/spectrum analyzer.\ |image4|\

.. container:: centeralign

   
   *Figure 4. EVAL-AD9707 FFT for Fdac=175MHz, Fout=20MHz*\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad970x-sdp-h1-set-up_edited.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/board.ad9707.acesession.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/board.ad9707.dpglite.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9707_sdph1_output_2.png
   :width: 600px
