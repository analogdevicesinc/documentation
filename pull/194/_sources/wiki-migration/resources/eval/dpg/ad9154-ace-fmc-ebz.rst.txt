EVALUATING THE AD9154 DIGITAL-TO-ANALOG CONVERTER
=================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9154-FMC-EBZ <EVAL-AD9154>` evaluation board to characterize :adi:`AD9154` 16-bit 2.4Gsps quad JESD204B signal processing RF Digital to Analog Converter.

The :adi:`AD9154-FMC-EBZ <EVAL-AD9154>` is an FMC mezzanine card and connects to an :adi:`ADS7-V2 <eval-ads7-v2>` data pattern generator system. The ADS7-V2 automatically formats the data and sends it to the AD9154-FMC-EBZ via its JESD204B lanes. +12V, +3.3V, and VADJ power supply rails are provided by the ADS7-V2 system via the FMC connector P1. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a GBTCLK clock used by the ADS7-V2. There is also an FMC standard I2C bus that is used by the ADS7-V2 to identify the AD9154-FMC-EBZ. This I2C interface is implemented in software in the AD9154-FMC-EBZ PIC processor (XU1). All ADS7-V2 to/from AD9154-FMC-EBZ interface signals are connected via the FMC connector P1.

Typical Setup
-------------

.. container:: centeralign

   |image1|\ *Figure 1. AD9154-FMC-EBZ Setup with ADS7-V2EBZ*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files/Links
-------------------

-  User Guides for non-FMC card users:

   -  :doc:`AD9154-EBZ </wiki-migration/resources/eval/dpg/ad9154-ace-ebz>`
   -  :doc:`AD9154-ADRF6720-EBZ </wiki-migration/resources/eval/dpg/ad9154-adrf6720-ebz>`

-  :doc:`ADS7-V1/-V2 for High-Speed DAC Evaluation </wiki-migration/resources/eval/dpg/ads7>`
-  Datasheet: :adi:`AD9154 <media/en/technical-documentation/data-sheets/AD9154.pdf>`
-  IBIS Model: :adi:`AD9154 <media/en/package-pcb-model-library/ibis-models/ad9154bcpz>`
-  AMI Model: `AD9144/AD9152/AD9154/AD9135/AD9136 <https://form.analog.com/Form_Pages/securedownloads/designFilePackage.aspx?prodID=AD9144-9152-9154-9135-9136>`_
-  Schematic: `RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_reva_schematic.pdf>`_
-  Bill of Materials: `RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_reva_bom.xls>`_
-  PCB Gerber Files: `RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_reva_gerber_files.zip>`_
-  PCB BRD File: `RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_reva.zip>`_
-  PCB Layout PDF: `RevA <https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_reva_layout.pdf>`_

Software Needed
---------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`
-  :adi:`AD9154 ACE Plugin <plugins/ace/board.ad9154.1.2020.4400.acezip>`

.. important::

   
   -  Do not install ACE on a computer with DAC Software Suite.
   -  **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.
   


Hardware Needed
---------------

-  :adi:`AD9154-FMC-EBZ <EVAL-AD9154>` Evaluation Board which comes with:

   -  USB-A to USB-Mini Cable

-  :doc:`ADS7-V2EBZ </wiki-migration/resources/eval/ads7-v2>` Evaluation Kit which includes:

   -  12V 60W AC/DC Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

-  PC with ACE and DPG Lite Software Applications
-  Low Phase Noise High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer and/or Wide Bandwidth Oscilloscope
-  2 to 5 SMA Cables

Quick Start Guide
-----------------

-  Attach AD9154-FMC-EBZ onto the FMC connector of ADS7-V2 controller board. Connect the evaluation board to PC via USB, the continuous waveform generator output to J1, one of the DAC outputs to a spectrum/signal analyzer and the rest to an oscilloscope. Connect ADS7-V2 to PC via USB and to a 12V 60W AC/DC power supply, then switch the board ON using S1 beside the connector for 12V supply. Refer to Typical Setup section for pictures of actual evaluation setup.
-  Set the frequency of the continuous waveform generator output to **1.5 GHz** and the output level to **+3 dBm**. Enable the output.

.. container:: centeralign

   \ |image2|\ *Figure 2. ADS7-V2 and AD9154 detected in DPG Software*\


-  Start DPG Lite or DPG Downloader. A panel named after the detected controller board should appear at the bottom of the DPG window. The device on the evaluation board and the data interface should also be automatically detected by the software and shown at **Evaluation Board** and **Port Configuration**, respectively. See Figure 2.

.. container:: centeralign

   \ |image3|\ *Figure 3. AD9154-FMC-EBZ detected in ACE*\


-  Open ACE. The board will automatically be recognized by the software as shown in Figure 3. Otherwise, install the plugin for AD9154 evaluation board by following the steps in this page: :doc:`Quickstart - ACE Quickstart and Plug-in Installation </wiki-migration/resources/tools-software/ace/userguide/quickstart>`.

.. container:: centeralign

   \ |image4|\ *Figure 4. ACE Initial Configuration Wizard*\


.. container:: centeralign

   \ |image5|\ *Figure 5. ACE AD9154 Chipview Tab*\


-  In ACE, apply the configuration wizard settings enumerated below and shown in Figure 4. JESD204B PLL should lock and the indicator should turn green.

   -  **Links:** Single Link
   -  **JESD Mode:** 0
   -  **Subclass1:** False
   -  **Interpolation:** 2
   -  **DAC PLL:** False
   -  **FDAC:** 1.5 GHz

.. container:: centeralign

   \ |image6|\ *Figure 6. Single Tone and ADS7-V2 Configuration Panels in DPG*\


-  In DPG Lite or DPG Downloader, configure single tone waveform generation. From the **Add Generator Waveforms** pulldown menu, select **Single Tone**. Apply the following settings:

   -  **Data Rate:** 750 MHz
   -  **Desired Frequency:** 180 MHz
   -  **DAC Resolution:** 16 bits
   -  **Amplitude:** 0 dB
   -  **Unsigned Data:** unchecked
   -  **Generate Complex Data (I & Q):** checked

-  In the ADS7-V2 panel in the DPG window, configure **Data Playback** by selecting tones for the DAC outputs from each dropdown menu. Set **JESD Mode** to Mode 0, **Links** to Single, and **Subclass** to 0.

.. container:: centeralign

   \ |image7|\ *Figure 7. AD9154 DAC Output FFT for Data Rate = 750 MHz, FOUT = 180 MHz*\


.. container:: centeralign

   \ |image8|\ *Figure 8. Oscilloscope Capture of Other DAC Outputs*\


-  Press the download arrow (|9154_down_arrow.png|) then the play button (|9154_right_green_arrow.png|). As in Figure 6, **Serial Line Rate** should appear as 7.5 Gbps and **Sync Status** should have a check mark. FFT plot of one of the DAC outputs is shown in Figure 7 while the oscilloscope capture of the other outputs is Figure 8.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_setup_with_labels.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_dpg_board_detect_ads7.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_ace_board_detect_ads7.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_ace_configuration_wizard_ads7.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_ace_chipview_ads7.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9154-fmc-ebz_dpg_generate_output.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ace_ad9154_fmc_180msa.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_fmcfigure_8_scope.png
   :width: 600px
.. |9154_down_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_down_arrow.png
.. |9154_right_green_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_right_green_arrow.png
