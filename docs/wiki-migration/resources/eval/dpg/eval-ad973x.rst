EVALUATING THE AD9736/AD9735/AD9734 DIGITAL-TO-ANALOG CONVERTER
===============================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9736-DPG2-EBZ <eval-ad9736>` evaluation board to characterize :adi:`AD9736` 14-bit 1200 MSPS digital-to-analog converter.

This guide shows how AD9736-DPG2-EBZ works with SDP-H1 or ADS7-V2 controller board developed by Analog Devices. Documentation and software updates for using the <fc #ff0000>\ :adi:`AD9734`/:adi:`AD9735`/:adi:`AD9736`\ </fc> Evaluation Boards are included in a self-extracting update file. Documentation can also be downloaded individually below.

Typical Setup
-------------

|image1|

.. container:: centeralign

   \ *Figure 1a. EVAL-AD9736 Setup with SDP-H1*\


   |image2|

.. container:: centeralign

   \ *Figure 1b. EVAL-AD9736 Setup with ADS7-V2*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  Download the `AD9736 Update <https://wiki.analog.com/_media/resources/eval/dpg/hsdacupdate_ad9736_1.0.4686.25855.exe.zip>`__ for DPG3 users
-  Data Sheet: :adi:`AD973X Data Sheet <static/imported-files/data_sheets/AD9734_9735_9736.pdf>`
-  IBIS Model: :adi:`AD9736 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9736.ibs>`, :adi:`AD9735 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9735.ibs>`, :adi:`AD9734 </Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9734.ibs>`
-  `Schematic <https://wiki.analog.com/_media/resources/eval/dpg/ad9736-dpg2-ebz_revc_schematic.pdf>`__
-  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/dpg/ad9736-dpg2-ebz_revc_bom_customer.xls>`__
-  `PCB Gerber files <https://wiki.analog.com/_media/resources/eval/dpg/ad9736-dpg2-ebz_revc_gerber_files.zip>`__
-  `PCB BRD file <https://wiki.analog.com/_media/resources/eval/dpg/ad9736-dpg2-ebz_revc.zip>`__
-  `PCB Layout PDF <https://wiki.analog.com/_media/resources/eval/dpg/ad9736-dpg2-ebz_revc_layout.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

.. important::

   \ **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.


Hardware Needed:
----------------

-  :adi:`AD9736-DPG2-EBZ <eval-ad9736>` Evaluation Board
-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) or :doc:`ADS7-V2EBZ </wiki-migration/resources/eval/ads7-v2>` Evaluation Kit
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

-  Attach the evaluation board to the FMC connector of SDP-H1 or ADS7-V2 using the AD-DAC-FMC-ADP adapter board. Connect continuous wave generator for clock input to J1, and the DAC output from J2 to a signal/spectrum analyzer. Connect the evaluation board to PC via USB and to a 5Vdc 2A power supply via banana plug cables. Refer to Figures 1a and 1b.Set clock input to **500 MHz and 6 dBm**.

   -  If using **SDP-H1**, Connect to PC via USB and to a 12Vdc wall wart.
   -  If using **ADS7-V2**, Connect to PC via USB and to a 12V 60W AC/DC power supply. Switch the board ON using S1 beside the connector for 12V supply.

-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9736 evaluation board. Apply the configuration wizard settings shown in Figure 2.

.. container:: centeralign

   \ |image3|\ *Figure 2. ACE Chip View Initial Configuration Wizard*\


-  Start DPG Lite or DPG Downloader. At the SDP-H1 or ADS7-V2 settings, ensure that **Evaluation board** is equal to AD9736 and DCO frequency of around 250 MHz should be displayed.
-  In DPG Lite or DPG Downloader, from the **Add Generator Waveforms** pulldown menu, select **Single Tone** and apply the settings as shown in Figures 3a and 3b.Set **Data Rate** to 500 MHz and **Desired Frequency** to 50 MHz.
-  Continuing on setting up DPG Lite or DPG Downloader, set **DAC resolution** to 14 bits.

.. container:: centeralign

   \ |image4|\ *Figure 3a. DPG Lite session for SDP-H1*\


.. container:: centeralign

   \ |image5|\ *Figure 3b. DPG Lite session for ADS7-V2*\


-  Select the Single tone from the **Data Vector** pulldown menu
-  Press the download arrow and then the play button. The FFT plots similar to Figures 4 should appear in the signal/spectrum analyzer.

.. container:: centeralign

   \ |image6|\ *Figure 4. EVAL-AD9736 FFT for Data Rate = 500 MHz, Fout = 50 MHz*\


Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. If unexpected results occur:

-  Check the supply voltage of the evaluation board. Voltage rail should be 3.3V.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board is lit up. Reconnect the board to the FMC connector of SDP-H1 if not lit up.
-  Check if the SDP-H1 is being supplied properly by 12Vdc adaptor. Some LEDs on the SDP-H1 should lit up.
-  Power cycle both the SDP-H1/ADS7-V2 and the AD9736 evaluation board.
-  Check on the Spectrum Analyzer if the DAC clock inputs are properly driven. For 500MHz clock, the spectrum analyzer should detect a weak signal at 500MHz. If not detected, check properly the clock source and connections.
-  Disconnect and reconnect the SDP-H1 /ADS7-V2 and AD9736 evaluation board. Reopen DPG Lite software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736-sdph1.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736_ads7.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736_ace_chip_view.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736_dpglite_sdp-h1.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736_dpglite_ads7.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9736_output_fft.png
   :width: 600px
