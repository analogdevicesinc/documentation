EVALUATING THE AD9135/AD9136 DIGITAL-TO-ANALOG CONVERTER
========================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9135-FMC-EBZ <EVAL-AD9135>`/:adi:`AD9136-FMC-EBZ <EVAL-AD9136>` evaluation board to characterize :adi:`AD9135`/:adi:`AD9136` 11-/16-bit 2.8Gsps dual JESD204B signal processing RF Digital to Analog Converter.

The :adi:`AD9135-FMC-EBZ <EVAL-AD9135>`/:adi:`AD9136-FMC-EBZ <EVAL-AD9136>` is an FMC mezzanine card and connects to an :adi:`ADS7-V2 <eval-ads7-v2>` or :adi:`ADS8-V1 <eval-ads8-v1ebz>` data pattern generator system. The ADS7-V2/ADS8-V1 automatically formats the data and sends it to the AD9135/AD9136 FMC card via its JESD204B lanes. +12V, +3.3V, and VADJ power supply rails are provided by the ADS7-V2/ADS8-V1 system via the FMC connector P1. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a GBTCLK clock used by the ADS7-V2/ADS8-V1. There is also an FMC standard I2C bus that is used by the ADS7-V2/ADS8-V1 to identify the AD9135/AD9136 FMC card. This I2C interface is implemented in software in the AD9135/AD9136 FMC card PIC processor (XU1). All ADS7-V2/ADS8-V1 to/from AD9135/AD9136 FMC card interface signals are connected via the FMC connector P1.

Typical Setup
-------------

.. container:: centeralign

   \ |image1|\ *Figure 1a. AD9135-FMC-EBZ Setup with ADS7-V2EBZ*\


.. container:: centeralign

   \ |image2|\ *Figure 1b. AD9135-FMC-EBZ Setup with ADS8-V1EBZ*\


.. container:: centeralign

   \ |image3|\ *Figure 2a. AD9136-FMC-EBZ Setup with ADS7-V2EBZ*\


.. container:: centeralign

   \ |image4|\ *Figure 2b. AD9136-FMC-EBZ Setup with ADS8-V1EBZ*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files/Links
-------------------

-  :doc:`AD9135-EBZ/AD9136-EBZ User Guide </wiki-migration/resources/eval/dpg/ad9136-ebz>` for non-FMC card users
-  :doc:`ADS7-V1/-V2 for High-Speed DAC Evaluation </wiki-migration/resources/eval/dpg/ads7>`
-  Datasheet: :adi:`AD9135/AD9136 <media/en/technical-documentation/data-sheets/AD9135_9136.pdf>`
-  IBIS Model: :adi:`AD9135 <media/en/package-pcb-model-library/ibis-models/ad9135bcpz>`,\ :adi:`AD9136 <media/en/package-pcb-model-library/ibis-models/ad9136bcpz>`
-  AMI Model: `AD9144/AD9152/AD9154/AD9135/AD9136 <https://form.analog.com/Form_Pages/securedownloads/designFilePackage.aspx?prodID=AD9144-9152-9154-9135-9136>`__
-  Simulink ADIsimDAC Model: `AD9136 <http://download.analog.com/behavioral-models/mathworks/ad9136_mathworks.zip>`__
-  Schematic: `AD9135-FMC-EBZ <https://wiki.analog.com/_media/resources/eval/dpg/ad9135-fmc-ebz_revb_schematic.pdf>`__, `AD9136-FMC-EBZ <https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_revb_schematic.pdf>`__
-  Bill of Materials: `AD9135-FMC-EBZ <https://wiki.analog.com/_media/resources/eval/dpg/ad9135-fmc-ebz_revb_bom_customer.xlsx>`__, `AD9136-FMC-EBZ <https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_revb_bom_customer.xls>`__
-  PCB Gerber Files: `RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9144-fmc-ebz_revb_gerber_files.zip>`__
-  PCB BRD File: `RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9144-fmc-ebz_revb.zip>`__
-  PCB Layout PDF: `RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9144-fmc-ebz_revb_layout.pdf>`__

Software Needed
---------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`
-  ACE Plugin for Specific Device: :adi:`AD9135 <plugins/ace/board.ad9135.1.2020.12100.acezip>`, :adi:`AD9136 <plugins/ace/board.ad9136.1.2020.12100.acezip>`

.. important::

   
   -  Do not install ACE on a computer with DAC Software Suite.
   -  **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.
   


Hardware Needed
---------------

-  :adi:`AD9135-FMC-EBZ <EVAL-AD9135>`/:adi:`AD9136-FMC-EBZ <EVAL-AD9136>` Evaluation Board which comes with:

   -  USB-A to USB-Mini Cable

-  :doc:`ADS7-V2EBZ </wiki-migration/resources/eval/ads7-v2>` or :doc:`ADS8-V1EBZ </wiki-migration/resources/eval/ads8-v1>` Evaluation Kit which includes:

   -  12V 60W AC/DC Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

-  PC with ACE and DPG Lite Software Applications
-  Low Phase Noise High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer and/or Wide Bandwidth Oscilloscope
-  (3) SMA Cables

Quick Start Guide
-----------------

-  Attach AD9135-FMC-EBZ/AD9136-FMC-EBZ onto the FMC connector of ADS7-V2 or ADS8-V1 controller board. Connect the evaluation board to PC via USB, the continuous waveform generator output to J1, the DAC output at J17 to a signal/spectrum analyzer, and, if desired, the other DAC output at J5 to an oscilloscope. Connect ADS7-V2/ADS8-V1 to PC via USB and to a 12V 60W AC/DC power supply, then switch the board ON using S1 beside the connector for 12V supply. Refer to :doc:`Typical Setup </wiki-migration/resources/eval/dpg/ad9136-fmc-ebz>` section for pictures of actual evaluation setup.
-  Set the frequency of the continuous waveform generator output to **2.0 GHz** and the output level to **+3 dBm**. Enable the output.

.. container:: centeralign

   \ |image5|\ *Figure 3. ADS7-V2 and AD9136 detected in DPG Software*\


-  Start DPG Lite or DPG Downloader. A panel named after the detected controller board should appear at the bottom of the DPG window. The device on the evaluation board and the data interface should also be automatically detected by the software and shown at **Evaluation Board** and **Port Configuration**, respectively.

.. container:: centeralign

   \ |image6|\ *Figure 4. AD9136-FMC-EBZ detected in ACE*\


-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9135/AD9136 evaluation board by following the steps in this page: :doc:`Quickstart - ACE Quickstart and Plug-in Installation </wiki-migration/resources/tools-software/ace/userguide/quickstart>`.

.. container:: centeralign

   \ |image7|\ *Figure 5. ACE Initial Configuration Wizard*\


.. container:: centeralign

   \ |image8|\ *Figure 6. ACE AD9136 Chipview Tab*\


-  In ACE, apply the configuration wizard settings enumerated below and shown in Figure 5. JESD204B PLL should lock and the indicator should turn green.

   -  **Links:** Dual Link

      -  **JESD Mode:** 8
      -  **Subclass1:** True
      -  **Interpolation:** 1
      -  **DAC PLL:** False
      -  **FDAC:** 2 GHz

.. container:: centeralign

   \ |image9|\ *Figure 7. Single Tone and ADS7-V2 Configuration Panels in DPG*\


-  In DPG Lite or DPG Downloader, configure generation of two single tone waveforms. From the **Add Generator Waveforms** pulldown menu, select **Single Tone**. Do this two times then configure the panels as follows:

   -  **Data Rate** = 2 GHz, **Amplitude** = -1dBFS, **Unsigned Data** is unchecked for both panels.

      -  **Desired Frequency = 112 MHz** in one panel while **Desired Frequency = 221 MHz** in the other.
      -  If using AD9135, set **DAC Resolution** to **11 bits**. Otherwise, leave as is (16 bits).

-  In the ADS7-V2 or ADS8-V1 panel in the DPG window, configure **Data Playback** by selecting tone2 for DAC0 and tone1 for DAC1. Set **JESD Mode** to Mode 8, **Links** to Dual, and **Subclass** to 1.

.. container:: centeralign

   |image10|\ *Figure 8. DAC0 Output Spectrum Analyzer Display*


.. container:: centeralign

   |image11|\ *Figure 9. DAC1 Output Scope Display*


-  Press the download arrow (|9154_down_arrow.png|) then the play button (|9154_right_green_arrow.png|). **Serial Line Rate** should appear as 10 Gbps and **Sync Status** should have two check marks. Refer to FFT plot of the DAC0 output in Figure 8 and the oscilloscope capture of DAC1 output in Figure 9.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9135-fmc-ebz_setup_with_label.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9135-fmc-ebz_setup2_with_labels.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_setup_with_labels.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_setup2_with_labels.jpg
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_dpg_board_detect.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_ace_board_detect.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_ace_configuration_wizard.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_ace_chipview.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136-fmc-ebz_dpg_output_generation.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/ad9136-35_dac0_sa_output.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9136/ad9136-35_dac1_scope_output.png
   :width: 600px
.. |9154_down_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_down_arrow.png
.. |9154_right_green_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_right_green_arrow.png
