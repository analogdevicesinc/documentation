EVALUATING THE AD9139 DIGITAL-TO-ANALOG CONVERTER
=================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from AD9139-EBZ evaluation board to characterize AD9139 16-bit, 1.6GSPS, TxDAC+® digital-to-analog converter. This guide shows how ADS7-V2EBZ / SDP-H1 controller board automatically formats the data and sends it to the AD9139-EBZ developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG3 controller board.

Typical Setup
-------------

.. container:: centeralign

   \ |image1|\ *Figure 1a. AD9139-EBZ with ADVS7-V2EBZ Setup*\


.. container:: centeralign

   \ |image2|\ *Figure 1b. AD9139-EBZ with SDP-H1 Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  :doc:`AD9139-EBZ User Guide </wiki-migration/resources/eval/dpg/ad9139-ebz-dpg>` for DPG2/3 users
-  Datasheet: :adi:`AD9139 <media/en/technical-documentation/data-sheets/AD9139.pdf>`
-  IBIS Model: :adi:`AD9139 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9139.ibs>`
-  Schematics: `AD9139-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_reva_schematic.pdf>`_ / `AD9139-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_revb_schematic.pdf>`_
-  Bill of Materials: `AD9139-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_reva_bom.pdf>`_ / `AD9139-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_revb_bom.xls>`_
-  PCB Gerber Files: `AD9139-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_reva_gerber_files.zip>`_ / `AD9139-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_revb_gerber_files.zip>`_
-  PCB Board Files: `AD9139-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_reva.zip>`_ / `AD9139-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_revb.zip>`_
-  PCB Layout: `AD9139-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_reva_layout.pdf>`_ / `AD9139-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9139-ebz_revb_layout.pdf>`_

Software Needed:
----------------

-  `Analysis \| Control \| Evaluation (ACE) v1.25 Software <https://swdownloads.analog.com/ACE/ACEInstall_1.25.3217.1403.exe>`_
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (installed with ACE)

.. important::

   
   -  Do not install ACE on a computer with DAC Software Suite.
   -  Use **ACE version 1.25** to evaluate AD9139-EBZ.
   


Hardware Needed:
----------------

-  :adi:`AD9139-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9139.html>` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Evaluation Kit / :doc:`ADS7-V2EBZ </wiki-migration/resources/eval/ads7-v2>` Evaluation Kit
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  PC with ACE and DPG Lite Software Applications
-  5Vdc Power Supply
-  (2) Banana Plug Cables
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  USB-A to USB-Mini Cable
-  (2) SMA Cables
-  The following are included in SDP-H1 Evaluation Kit:

   -  12Vdc Wall Adapter
   -  USB-A to USB-Mini Cable

-  The following are included in ADS7-V2 Evaluation Kit:

   -  12Vdc Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

Quick Start Guide
-----------------

-  Follow evaluation setup in Figure 1a and 1b.

   -  Attach the AD9139-EBZ evaluation board to ADS7-V2EBZ/SDP-H1 connector using the AD-DAC-FMC-ADP adapter board.
   -  Connect continuous wave generator for clock input to J1 (AD9516_CLKIN).
   -  Connect output from J3 (DAC1 output) to a signal/spectrum analyzer.
   -  Connect the evaluation board to PC via USB and to a 5Vdc power supply via banana plug cables.
   -  Connect ADS7-V2EBZ/SDP-H1 to PC via USB and to a 12Vdc power supply.
   -  Set clock input to **500MHz** and **0dBm**.

-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9139 evaluation board. Double click this board then modify the configuration, refer to figure 2.:

   -  If ADS7-V2EBZ is used, set interpolation to **2**.
   -  If SDP-H1 is used, set interpolation to **1**.

.. container:: centeralign

   \ |image3|\ *Figure 2. ACE Initial Configuration Wizard when using ADS7-V2EBZ or SDP-H1*\


-  Open DPGDownloaderLite. The evaluation board, controller board and DCO Frequency will be automatically recognized by DPG.

   -  If ADS7-V2EBZ is used, a **DCO Frequency** of around **125 MHz** should be displayed.
   -  If SDPH1 is used, a **DCO Frequency** of around **250 MHz** should be displayed.

-  In DPGDownloaderLite, from the **Add Generator Waveforms** pulldown menu, select **Single Tone** and apply the settings as shown in Figures 3a and 3b. The data rate in DPG software should be equal to the data rate in ACE.

   -  If ADS7-V2EBZ is used, set **Data Rate** to 250 MHz and Desired Frequency to **22 MHz**.
   -  If SDPH1 is used, set **Data Rate** to 500 MHz and Desired Frequency to **22 MHz**.

-  Continuing on setting up DPGDownloaderLite, set **DAC Resolution** to 16 bits. Uncheck the **Generate Complex Data (I & Q)** box and **Unsigned Data** box.
-  Select the in-phase tone from the **I Data Vector** pulldown menu.

.. container:: centeralign

   \ |image4|\ *Figure 3a. DPGDownloaderLite Waveform Configuration for AD9139-EBZ with ADS7-V2EBZ*\


.. container:: centeralign

   \ |image5|\ *Figure 3b. DPGDownloaderLite Waveform Configuration for AD9139-EBZ with SDP-H1*\


-  Press the download arrow and then the play button. The spectrum similar to Figure 4 should appear in the signal/spectrum analyzer.

.. container:: centeralign

   \ |image6|\ *Figure 4. AD9139-EBZ FFT for Fdac=500MHz, Fout=22MHz*\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139_ads7.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9142a_sdph1_setup.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139_2_initial_config.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139_4_dpg.jpg
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139_4_dpg_sdp.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139_5_output.png
   :width: 600px
