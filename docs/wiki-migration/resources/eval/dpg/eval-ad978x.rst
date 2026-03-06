EVALUATING THE AD9785/AD9787/AD9788 DIGITAL-TO-ANALOG CONVERTER
===============================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9785-DPG2-EBZ <eval-ad9785>`/:adi:`AD9787-DPG2-EBZ <eval-ad9787>`/:adi:`AD9788-DPG2-EBZ <eval-ad9788>` evaluation board to characterize :adi:`AD9785`/:adi:`AD9787`/:adi:`AD9788` 12-/14-/16-bit 800Msps high-speed digital-to-analog converter.

This guide shows how AD978x-DPG2-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG2 controller board.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. EVAL-AD9785/9787/9788 Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  `Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-evaluation_board_quick_start_guide.pdf>`__ for DPG2 users
-  Data Sheet :adi:`AD978x <static/imported-files/data_sheets/AD9785_9787_9788.pdf>`
-  IBIS Models: :adi:`AD9788 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9788.ibs>`, :adi:`AD9787 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9787.ibs>`, :adi:`AD9785 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9785.ibs>`
-  Schematics `AD9788-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-ebz_revd_schematic.pdf>`__
-  Bill of Materials `AD9788-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-ebz_revd_bom_customer.xls>`__
-  PCB Gerber files `AD9788-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-ebz_revd_gerber_files.zip>`__
-  PCB BRD file `AD9788-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-ebz_revd.zip>`__
-  PCB Layout PDF `AD9788-DPG2-EBZ RevD <https://wiki.analog.com/_media/resources/eval/dpg/ad9788-dpg2-ebz_revd_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9785-DPG2-EBZ`/:adi:`AD9787-DPG2-EBZ`/:adi:`AD9788-DPG2-EBZ` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12V 1A Wall Wart for SDP-H1
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  5V 2A Power Supply
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  (2) USB A to USB Mini Cables
-  (2) SMA Cables
-  (2) Banana Plug Cables

Quick Start Guide
-----------------

-  Make sure than on the evaluation board, JP1, JP2, JP3, and JP4 are configured such that IOUTxP and IOUTxN are connected to the corresponding baluns (T7, T8), and R8 and R9 are installed. Refer to Figure 5a.
-  Configure JP5 and JP6 to connect DAC clock inputs to the desired clock source. Refer to:

   -  Figure 6a for direct clocking or
   -  Figure 6b when using AD9516.

-  Attach the evaluation board to SDP-H1 FMC connector using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J2 (for direct clocking) or J1 (when using AD9516), and the DAC output from J4 or J8 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB and to a 5V 2A power supply via banana plug cables. Refer to Figure 1.
-  Connect SDP-H1 to PC via USB and to a 12V 1A power supply.
-  Set clock input to:

   -  400MHz and 3dBm for direct clocking, or
   -  100MHz and 3dBm when using AD9516.

-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9785/9787/9788 evaluation board.

.. container:: centeralign

   \ |image2|\ *Figure 2a. ACE Initial Configuration Wizard for Direct Clocking \| Figure 2b. ACE Initial Configuration Wizard when using AD9516*\


-  In ACE,

   -  when AD9516 is not in use, in the wizard under “AD78x DAC Setup,” change Data Format to “Binary” and Interpolation Factor to “8x”. Click “Apply". See Figure 2a.
   -  when using AD9516, check off the "Use AD9516" box. In the wizard under “AD78x DAC Setup,” change Data Format to “Binary” and Interpolation Factor to “8x”. Click “Apply". See Figure 2b.

-  Start DPG Lite or DPG Downloader. At the SDP-H1 part of the software, the device part number and DCO frequency of 50MHz should be displayed.
-  In DPG Lite or DPG Downloader, from the "Add Generator Waveforms" pulldown menu, select "Single Tone" and apply the settings as shown in Figure 3. Set data rate to 50MHz and desired frequency to 10MHz. Set DAC resolution to the DAC’s number of bits (16 for AD9788, 14 for AD9787, and 12 for AD9785). Check off the "Generate Complex Data (I & Q)" box.

.. container:: centeralign

   \ |image3|\ *Figure 3. DPG Lite session for EVAL-AD9788*\


-  Select the in-phase tone from the "I Data Vector" pulldown menu and the quadrature tone from the "Q Data Vector" pulldown menu.
-  Press the download arrow and then the play button. The FFT plot similar to Figure 4 should appear in the signal/spectrum analyzer.

.. container:: centeralign

   \ |image4|\ *Figure 4. EVAL-AD9788 FFT for Fdac=50MHz, Fout=10MHz*\


Reconfiguring the Evaluation Board
----------------------------------

Jumpers for Selecting DAC Output Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, jumpers JP1, JP2, JP3, and JP4 are configured such that the IDAC output can be observed at SMA J4, and QDAC output at J8. See Figure 5a.

To connect to the filters that feed ADL5375, the solder jumpers need to be repositioned as shown in Figure 5b. The output from the ADL5375 Modulator can be observed at SMA J6 RF out.

.. container:: centeralign

   \ |image5| *Figure 5a. DAC Outputs to Baluns (default) \| Figure 5b. DAC Outputs to ADL5375 Modulator*\


Jumpers for Selecting the Clock Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, JP5 and JP6 are configured such that DAC clock of the DUT is driven directly by an off-board clock source connected to J2. Refer to Figure 6a.

To test the performance i.e. ACLR with the clock multiplication, AD9516 is provided on board. In order to drive the DAC clock from AD9516, JP5 and JP6 needs to be changed as shown in Figure 6b. Connect the continuous wave generator to J1.

.. container:: centeralign

   \ |image6|\ *Figure 6a. Direct clocking configuration \| Figure 6b. DAC clock is driven by AD9516*\


Hardware Provisions for Power Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| There are 6 pin jumpers on the evaluation board corresponding to 6 supplies. They serve as ‘switches’ that determine if the on-board LDOs or external supplies are used for each individual supply. They are shunted by default, which means on-board LDOs are used. When an external supply is necessary, pull off the shunt from the corresponding supply and connect the external supply to the test points close to the jumper.
| |image7|

.. |image1| image:: https://wiki.analog.com/_media/ad9788_sdp-h1_setup_with_labels.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_ace_wizard.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_dpg_lite.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_fft.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_jumpers_for_output_config.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_jumpers_for_clock_source.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9788_table1.png
   :width: 600px
