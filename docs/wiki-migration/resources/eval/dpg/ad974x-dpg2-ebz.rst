EVALUATING THE AD9743/AD9745/AD9746/AD9747 DIGITAL-TO-ANALOG CONVERTER
======================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9743-DPG2-EBZ`/:adi:`AD9745-DPG2-EBZ`/:adi:`AD9746-DPG2-EBZ`/:adi:`AD9747-DPG2-EBZ` evaluation board to characterize :adi:`AD9743`/:adi:`AD9745`/:adi:`AD9746`/:adi:`AD9747` 10-/12-/14-/16-bit 250Msps high-speed digital-to-analog converter.

This guide shows how AD974x-DPG2-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the old user guide document is provided for customers who still have DPG2 and DPG3 controller boards.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. EVAL-AD9743/45/46/47 Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  Previous `User Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9747_evaluation_board_quick_start_guide.pdf>`__ as reference on evaluation board jumper selection
-  :adi:`AD9743_45_46_47 Data Sheet <static/imported-files/data_sheets/AD9743_9745_9746_9747.pdf>`
-  IBIS Models: :adi:`AD9747 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9747.ibs>`,\ :adi:`AD9746 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9746.ibs>`,\ :adi:`AD9745 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9745.ibs>`,\ :adi:`AD9743 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9743.ibs>`
-  `Schematic <https://wiki.analog.com/_media/resources/eval/dpg/ad9747-dpg2-ebz_revb_schematic.pdf>`__
-  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/dpg/ad9747-dpg2-ebz_revb_bom_customer.xls>`__
-  `PCB Gerber files <https://wiki.analog.com/_media/resources/eval/dpg/ad9747-dpg2-ebz_revb_gerber_files.zip>`__
-  `PCB BRD file <https://wiki.analog.com/_media/resources/eval/dpg/ad9747-dpg2-ebz_revb.zip>`__
-  `PCB Layout PDF <https://wiki.analog.com/_media/resources/eval/dpg/ad9747-dpg2-ebz_revb_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9743-DPG2-EBZ`/:adi:`AD9745-DPG2-EBZ`/:adi:`AD9746-DPG2-EBZ`/:adi:`AD9747-DPG2-EBZ` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12V 1A Wall Adapter for SDP-H1
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  5V 1A Power Supply
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  (2) USB A to USB Mini Cables
-  (2) SMA Cables
-  (2) Banana Plug Cables

Quick Start Guide
-----------------

-  Make sure than on AD9743-DPG2-EBZ/AD9745-DPG2-EBZ/AD9746-DPG2-EBZ/AD9747-DPG2-EBZ, JP4, JP5, JP6, and JP7 are configured such that IOUTxP and IOUTxN are connected to the corresponding baluns (T7, T8), and R39 and R40 are installed. Refer to Figure 5a.
-  Attach the evaluation board to SDP-H1 FMC connector using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J1 and DAC output from J8 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB and to a 5V 1A power supply via banana plug cables. Refer to Figure 1.
-  Connect SDP-H1 to PC via USB and to a 12V 1A power supply.
-  Set clock input to 100MHz and 2dBm.
-  Open ACE. The board will be automatically recognized by the software. Otherwise, install the plugin for AD9747.
-  Start DPG Lite or DPG Downloader. At the SDP-H1 part of the software, the device part number and clock frequency should be displayed.
-  In ACE, apply the default values in the Initial Configuration wizard as shown in Figure 2.\ |image2|\

.. container:: centeralign

   
   *Figure 2. ACE Initial Configuration Wizard for EVAL-AD9747*\


-  In DPG Lite or DPG Downloader, from the Add Generator Waveforms pulldown menu select Single Tone and apply the settings as shown in Figure 3. Set the desired frequency to 17 MHz. Set DAC resolution to the DAC’s number of bits (16 for AD9747, 14 for AD9746, and so on). Check the Generate Complex Data (I & Q) box.\ |image3|\

.. container:: centeralign

   
   *Figure 3. DPG Lite session for EVAL-AD9747*\


-  Select the in-phase tone from the I Data Vector pulldown menu and the quadrature tone from the Q Date Vector pulldown menu.
-  Press the download arrow and then the play button. The spectrum similar to Figure 4 should appear in the signal/spectrum analyzer.\ |image4|\

.. container:: centeralign

   
   *Figure 4. EVAL-AD9747 FFT for Fdac=100MHz, Fout=17MHz*\


Reconfiguring the Evaluation Board
----------------------------------

Jumpers for Selecting DAC Output Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each pair of differential DAC outputs can be connected to a balun or both differential pairs can be connected to the ADL5373 modulator. Refer to the jumper settings below.

.. container:: centeralign

   \ |image5| *Figure 5a. DAC Outputs to Baluns \| Figure 5b. DAC Outputs to ADL5373 Modulator*\


The modulator output can be observed thru the SMA connector J6 (MODULATED OUTPUT). The modulator LO input can be sourced thru SMA connector J10 (LOCAL OSC INPUT). The clock level into the modulator should be set to about 3dBm.

Jumpers for Power Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 6 pin jumpers on the evaluation board corresponding to the 6 supplies on the board. They serve as ‘switches’ that determine if the on board LDOs or external supplies are used for each individual supply. They are shunted by default, which means on board LDOs are used. When an external supply is necessary, pull off the shunt from the corresponding supply and connect the external supply to the SMA test points close to the jumper.


|image6|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747_sdp-h1_hardware_set-up.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747_ace_boardview.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747_dpg-lite_sdp-h1.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747_output_sdp-h1_.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747-10.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9747-11.png
   :width: 600px
