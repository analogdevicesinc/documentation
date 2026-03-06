EVALUATING THE AD9739A / AD9737A RF DIGITAL-TO-ANALOG CONVERTER
===============================================================

|

.. warning::

   \ **NOTE:**

   | Support for the eval-ad9739a is discontinued starting with 2022_R2 Kuiper Linux release and it will not be supported in future releases. Last release in which pre-build files can be found is 2021_r2. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases.


Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9739A-EBZ <eval-ad9739A>` evaluation board to characterize :adi:`AD9739A` 14-Bit, 2.5 GSPS, RF Digital-to-Analog Converter.

This guide shows how AD9739A-EBZ works with SDP-H1 or ADS7-V2 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG3 controller board.

Typical Setup
-------------

<fc #ff0000>\ |image1|\ </fc>

.. container:: centeralign

   \ *Figure 1a. EVAL-AD9739A Setup with SDP-H1*\


<fc #ff0000>\ |image2|\ </fc>

.. container:: centeralign

   \ *Figure 1b. EVAL-AD9739 Setup with ADS7-V2*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  Download the `AD9739A Evaluation Board Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_evaluation_board_quick_start_guide.pdf>`__\ for DPG3 users
-  Data Sheet: :adi:`AD9739 Data Sheet <static/imported-files/data_sheets/AD9739A.pdf>`
-  IBIS Model: :adi:`IBIS Model <en/license/ibis-models?mediaPath=media/en/simulation-models/ibis-models/ad9739.ibs&modelType=ibis-models>`
-  Schematic: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_schematic.pdf>`__ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_schematic.pdf>`__
-  Bill of Materials: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_bom_customer.xls>`__ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_bom_customer.xls>`__
-  PCB Gerber files:`ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_gerber_files.zip>`__ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_gerber_files.zip>`__
-  PCB BRD file:`ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva.zip>`__ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb.zip>`__
-  PCB Layout PDF: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_layout.pdf>`__ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9739A-EBZ <eval-ad9739a>` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) or :doc:`ADS7-V2EBZ </wiki-migration/resources/eval/ads7-v2>`
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
-  5Vdc 2A Power Supply
-  PC with ACE and DPG Lite Software Applications
-  High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  USB-A to USB-Mini Cable
-  (2) SMA Cables
-  The following are included in SDP-H1 Evaluation Kit:

   -  12Vdc 2.5A Wall Wart
   -  USB-A to USB-Mini Cable

-  The following are included in ADS7-V2 Evaluation Kit:

   -  12V 60W AC/DC Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

Quick Start Guide
-----------------

-  Attach the evaluation board to the FMC connector of SDP-H1 or ADS7-V2 using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J3, and the DAC output from J1 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB, a 5Vdc 2A power supply to P3 and ground to P4.Refer to Figures 1a and 1b.

   -  If using **SDP-H1**, set clock input to **300 MHz and 0 dBm**. Connect SDP-H1 to PC via USB and to a 12Vdc wall wart.
   -  If using **ADS7-V2**, set the clock input to **2 GHz and 0 dBm**. Connect ADS-V2 to PC via USB and to a 12V 60W AC/DC power supply. Switch the board ON using S1 beside the connector for 12V supply.

-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9739A evaluation board. From the AD9739A-EBZ tab, Click **“Run Example Startup Routine”**.

   -  If using **SDP-H1**, The MU Controller Locked indicator should light up as shown in figure 2a.
   -  If using **ADS7-V2**, The first three indicators should light up as shown in figure 2b.

.. container:: centeralign

   \ |image3|\ *Figure 2a. ACE Initial Board Configuration Wizard for SDP-H1*\


.. container:: centeralign

   \ |image4|\ *Figure 2a. ACE Initial Board Configuration Wizard for ADS7-V2*\


-  Double click the AD9739A Box to open chip view.

   -  If using **SDP-H1**, The DLL_LOCKED indicator should light up as shown in figure 3a.
   -  If using **ADS7-V2**, All three indicators should light up as shown in figure 3b.

.. container:: centeralign

   \ |image5|\ *Figure 3a. ACE Initial Board Configuration Wizard for SDP-H1*\


.. container:: centeralign

   \ |image6|\ *Figure 3b. ACE Initial Board Configuration Wizard for ADS7-V2*\


-  Start DPG Lite or DPG Downloader.

   -  At the **SDP-H1** settings, ensure that **Evaluation board** is equal to AD9739A and **DCO frequency** of around **75 MHz** should be displayed.
   -  At the **ADS7-V2** settings, ensure that **Evaluation board** is equal to AD9739A and **DCO frequency** of around **500 MHz** should be displayed.

-  In DPG Lite or DPG Downloader, from the **Add Generator Waveforms** pulldown menu, select **Single Tone** and apply the settings as shown in Figures 4a and 4b.

   -  When using **SDP-H1**, set **Data Rate** to 300 MHz and **Desired Frequency** to 20 MHz.
   -  When using **ADS-V2,** set **Data Rate** to 2 GHz and **Desired Frequency** to 180 MHz.

-  Continuing on setting up DPG Lite or DPG Downloader, set **DAC resolution** to 14 bits. Check off the **Unsigned Data** box.
-  Select the Single Tone from the **Data Vector** pulldown menu

.. container:: centeralign

   \ |image7|\ *Figure 4a. DPG Lite session for SDP-H1*\


.. container:: centeralign

   \ |image8|\ *Figure 4b. DPG Lite session for ADS7-V2*\


-  Press the download arrow and then the play button. The FFT plots similar to Figures 5a and 5b should appear in the signal/spectrum analyzer.

.. container:: centeralign

   {{ :resources:eval:dpg:ad9739a_sdp-h1_fft.png?nolink&600 \|\ |image9|\ *Figure 5a. EVAL-AD9739A FFT for Data Rate = 300 MHz, Fout = 20 MHz using SDP-H1*\


.. container:: centeralign

   \ |image10|\ *Figure 5b. EVAL-AD9739A FFT for Data Rate = 2 GHz, Fout = 180 MHz using AD7-V2*\


Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. If unexpected results occur:

-   Check if the Voltage supply test points of the evaluation board has the correct value.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board is lit up. Reconnect the board to the FMC connector of SDP-H1 if not lit up.
-  Check if the SDP-H1 is being supplied properly by 12Vdc adaptor. Some LEDs on the SDP-H1 should lit up.
-  Power cycle both the SDP-H1/ADS7-V2 and the AD9739A evaluation board.
-  Check on the Spectrum Analyzer if the DAC clock inputs are properly driven. For 300MHz clock using SDP-H1, the spectrum analyzer should detect a weak signal at 300MHz. For 2GHz clock using ADS7-V2, the spectrum analyzer should detect a weak signal at 2GHz. If not detected, check properly the clock source and connections.
-  Disconnect and reconnect the SDP-H1 /ADS7-V2 and AD9739A evaluation board. Reopen DPG Lite software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_setup_sdph1.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_setup_ads.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_ace_board_ads7.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_ace_board_ads7.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_ace_chip_sdp-h1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_ace_chip_ads7.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_sdp-h1_dpg.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_adsv7_dpg.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739_fout_sdp-h1.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_ads7_fft.jpg
   :width: 600px
