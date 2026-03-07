EVALUATING THE AD9121/AD9122/AD9125 DIGITAL-TO-ANALOG CONVERTER
===============================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9121-M5372-EBZ/AD9121-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9121.html#eb-overview>` / :adi:`AD9122-M5372-EBZ/AD9122-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9122.html#eb-overview>` / :adi:`AD9125-M5372-EBZ/AD9125-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9125.html>` evaluation board to characterize :adi:`AD9121 <media/en/technical-documentation/data-sheets/AD9121.pdf>` 14-bit / :adi:`AD9122 <media/en/technical-documentation/data-sheets/AD9122.pdf>` 16-bit, Dual, 1.23GSPS, TxDAC+® digital-to-analog converter or :adi:`AD9125 <static/imported-files/data_sheets/AD9125.pdf>` 16-bit, Dual, 1GSPS, TxDAC+® digital-to-analog converter. This guide shows how AD9121-M5375-EBZ, AD9122-M5375-EBZ, and AD9125-M5375-EBZ works with ADS7-V2/SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG2 controller board.

This guide shows how AD9121 and AD9122 Evaluation boards works with ADS7-V2/SDP-H1 controller board and how AD9125 evaluation board works with SDP-H1 controller board

Typical Setup
-------------

.. container:: centeralign

   \ |image1|\ *Figure 1a. AD9121-M5372-EBZ/AD9121-M5375-EBZ/AD9122-M5372-EBZ/AD9122-M5375-EBZ/AD9125-M5375-EBZ with SDP-H1 Setup*\


.. container:: centeralign

   \ |image2|\ *Figure 1b. AD9121-M5372-EBZ/AD9121-M5375-EBZ/AD9122-M5372-EBZ/AD9122-M5375-EBZ with ADVS7-V2EBZ Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files:
--------------

-  `AD9121 User Guide / AD9122 User Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9122_userguide.pdf>`_ / `AD9125 User Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9125_evaluation_board_quick_start_guide.pdf>`_ for DPG2/3 users
-  Datasheet: :adi:`AD9121 <media/en/technical-documentation/data-sheets/AD9121.pdf>` / :adi:`AD9122 <media/en/technical-documentation/data-sheets/AD9122.pdf>` / :adi:`AD9125 <static/imported-files/data_sheets/AD9125.pdf>`
-  IBIS Model: :adi:`AD9121 / AD9122 <en/license/ibis-models?mediaPath=media/en/simulation-models/ibis-models/ad9122.ibs&modelType=ibis-models>` / :adi:`AD9125 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9125.ibs>`
-  Schematics: `AD9122-M5372-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_rev_a.pdf>`_ / `AD9122-M5372-EBZREV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_rev_b.pdf>`_ / `AD9122-M5375-EBZ REV E <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_rev_e.pdf>`_ / `AD9122-M5375-EBZ REV F <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_rev_f.pdf>`_ / `AD9125-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5372-ebz_revb_schematic.pdf>`_ / `AD9125-M5375-EBZ REV C <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5375-ebz_revc_schematic.pdf>`_
-  Bill of Materials: `AD9122-M5372-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_reva_bom_customer.xls>`_ / `AD9122-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_revb_bom_customer.xls>`_ / `AD9122-M5375-EBZ REV E <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_reve_bom_customer.xls>`_ / `AD9122-M5375-EBZ REV F <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_revf_bom_customer.xls>`_ / `AD9125-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5372-ebz_revb_bom_customer.xls>`_ / `AD9125-M5375-EBZ REV C <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5375-ebz_revc_bom_customer.xls>`_
-  PCB Gerber Files: `AD9122-M5372-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_reva_gerber_files.zip>`_ / `AD9122-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_revb_gerber_files.zip>`_ / `AD9122-M5375-EBZ REV E <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_reve_gerber_files.zip>`_ / `AD9122-M5375-EBZ REV F <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_revf_gerber_files.zip>`_ / `AD9125-M5375-EBZ REV C <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5375-ebz_revc_gerber_files.zip>`_
-  PCB Board Files: `AD9122-M5372-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_reva.zip>`_ / `AD9122-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_revb.zip>`_ / `AD9122-M5375-EBZ REV E <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_reve.zip>`_ / `AD9122-M5375-EBZ REV F <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_revf.zip>`_ / `AD9125-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5372-ebz_revb.zip>`_ / `AD9125-M5372-EBZ REV C <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5375-ebz_revc.zip>`_
-  PCB Layout: `AD9122-M5372-EBZ REV A <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_reva_layout.pdf>`_ / `AD9122-M5372-EBZ REV B <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5372-ebz_revb_layout.pdf>`_ / `AD9122-M5375-EBZ REV E <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_reve_layout.pdf>`_ / `AD9122-M5375-EBZ REV F <https://wiki.analog.com/_media/resources/eval/dpg/ad9122-m5375-ebz_revf_layout.pdf>`_ / `AD9125-M5375-EBZ REV C <https://wiki.analog.com/_media/resources/eval/dpg/ad9125-m5375-ebz_revc_layout.pdf>`_

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` (installed with ACE)

.. important::

   Do not install ACE on a computer with DAC Software Suite.


Hardware Needed:
----------------

-  :adi:`AD9121-M5372-EBZ/AD9121-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9121.html#eb-overview>` / :adi:`AD9122-M5372-EBZ/AD9122-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad9122.html#eb-overview>` / :adi:`AD9125-M5372-EBZ/AD9125-M5375-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9125.html>` Evaluation Board
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

Jumpers for Selecting the DAC Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jumpers JP4, JP5, JP6, and JP17 select the output configuration. By default, the DAC output connected to the LPF and the ADL537x analog quadrature modulator. For selecting DAC output configuration, refer to Table 1 and Figure 2.

<WRAP >\ *Table 1. Jumper Configurations for Viewing DAC Output and Modulator Output*\ </WRAP>

+----------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Output Viewed              | SMA Output                 | Jumper Configuration                                                                                                                                                              |
+============================+============================+===================================================================================================================================================================================+
| DAC Output                 | J3 (DAC1_P) or J8 (DAC2_P) | <WRAP>JP4 and JP5 Pin 2 to Pin 3 (outer pads), JP6 and JP17 Pin 2 to Pin 3 (outer pads)</WRAP>

JP20 and JP19 Pin 2 to Pin 3 (inner pads), JP18 and JP7 Pin 2 to Pin 3 (inner pads) |
+----------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modulator Output (Default) | J6 (MOD_OUT)               | JP4 and JP5 Pin 1 to Pin 2 (inner pads), JP6 and JP17 Pin 1 to Pin 2 (inner pads)                                                                                                 |
+----------------------------+----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

================================ ==============================
|ad9122_dac_output_config_2.png| |image3|
DAC Output Configuration         Modulator Output Configuration
================================ ==============================

.. container:: centeralign

   \ *Figure 2. AD9121-M5375-EBZ/AD9122-M5375-EBZ/AD9125-M5375-EBZ Output Configuration*\


Jumper for Selecting Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board has a provision for on board or external power supply configuration.

Internal Power Supply
^^^^^^^^^^^^^^^^^^^^^

On board power supply is implemented by default using LDO. **JP1** selects the supply voltage level for IOVDD. Refer to Figure 3.

-  When Pin 1 and Pin 2 are connected, IOVDD = 3.3 V (Default)
-  When Pin 2 and Pin 3 are connected, IOVDD = 1.8 V

.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ *Figure 3. AD9122-M5375-EBZ IOVDD*\


External Power Supply
^^^^^^^^^^^^^^^^^^^^^

To implement external supply configuration, remove the header shunt of six pin jumpers, as shown in Figure 4. Refer to Table 2 for external supply jumper connection.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ *Figure 4. AD9122-M5375-EBZ Pin Jumpers*\


<WRAP >\ *Table 2. Jumper Configurations for External Power Supply*\ </WRAP>

=========== ==================== =====================
Supply Rail Remove Jx Pin Jumper Apply External Supply
=========== ==================== =====================
CVDD18      JP2                  J4
DVDD18      JP3                  J11
IOVDD       JP12                 J12
AVDD33      JP8                  J13
XCVDD33     JP9                  J10
AVDD5       JP11                 TP11(+5V), TP12 (GND)
=========== ==================== =====================

Jumper for Selecting Clock Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9121-M5372-EBZ/AD9121-M5375-EBZ/AD9122-M5372-EBZ/AD9122-M5375-EBZ/AD9125-M5375-EBZ evaluates both the DAC outputs as well as the AQM outputs. Refer to Table 3 for clock configuration.

<WRAP >\ *Table 3. Clock Configuration*\ </WRAP>

========================== =========== ======================
Output Viewed              Clock Input Local Oscillator Input
========================== =========== ======================
DAC Output                 J1 (CLKIN)  
Modulator Output (Default) J1 (CLKIN)  J9 (LO_IN)
========================== =========== ======================

The modulator LO input can be sourced through SMA connector J9 (LO_IN) with clock level at **3dBm**.

Evaluation Guide
~~~~~~~~~~~~~~~~

-  Make sure that on AD9121-M5375-EBZ/AD9122-M5375-EBZ/AD9125-M5375-EBZ, JP4, JP5, JP6, and JP17 are configured such that DAC output are connected with J3 (DAC1_P) or J8 (DAC2_P). Refer to Figure 2.
-  Follow evaluation setup in Figure 1a and 1b. **AD9121/AD9122** are both compatible with **ADS7/V2EBZ** and **SDP-H1** controller board while **AD9125** is only compatible with **SDP-H1** controller board.

   -  Attach the evaluation board to SDP-H1/ADS7-V2EBZ connector using the AD-DAC-FMC-ADP adapter board.
   -  Connect continuous wave generator for clock input to J1.
   -  Connect the DAC output from J3 (DAC1_P) or J8 (DAC2_P) to a signal/spectrum analyzer.
   -  Connect the evaluation board to PC via USB and to a 5Vdc power supply via banana plug cables.
   -  Connect SDP-H1/ADS7-V2EBZ to PC via USB and to a 12Vdc power supply.
   -  Set clock input/continuous wave generator to **500MHz** and **2dBm**.

-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9121/AD9122/AD9125 evaluation board. Double click this board then modify the configuration, as shown in Figure 5, and click "Apply".

.. container:: centeralign

   \ |image6|\ *Figure 5. ACE Initial Configuration Wizard when using SDP-H1/ADS7-V2EBZ*\


-  Open the DPGDownloaderLite. The evaluation board, controller board and DCO Frequency of around **250MHz** will be automatically recognized by DPG.

   -  If using AD9121 / AD9122 with **SDP-H1**, select **LVDS** as port configuration.
   -  If using AD9125 with **SDP-H1**, select **LVCMOS-1.8V**\ as port configuration.
   -  If using AD9121 / AD9122 with **ADS7-V2EBZ**, use default configuration.

.. container:: centeralign

   \ |image7|\ *Figure 6. AD9121/AD9122 SDP-H1 Port Configuration / AD9125 SDP-H1 Port Configuration*\


-  In DPGDownloaderLite, **Add Generator Waveforms** pulldown menu select Single Tone and apply the settings as shown in Figure 7. Set the **Data Rate** to 250MHz and **Desired Frequency** to 29 MHz. Set **DAC Resolution** to the DAC’s number of bits to: **14 bits** for AD9121; **16 bits** for AD9122/AD9125. Check the “Generate Complex Data (I & Q)” box and “Unsigned Data” box.
-  Select the in-phase tone from the **I Data Vector** pulldown menu and the quadrature tone from the **Q Data Vector** pulldown menu.

.. container:: centeralign

   \ |image8|\ *Figure 7. DPGDownloader Waveform Configuration for AD9122-M5375-EBZ*\


-  Press the download arrow and then the play button. The spectrum similar to Figure 8 should appear in the signal/spectrum analyzer.

.. container:: centeralign

   \ |image9|\ *Figure 8. AD9122-M5375-EBZ FFT for Fdac=500MHz,2x Interpolation Fout=29MHz*\


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_sdp.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_ads.jpg
   :width: 600px
.. |ad9122_dac_output_config_2.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_dac_output_config_2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_modulator_output_config.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_iovdd.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_7_jumpers_-_copy_2_.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_2_initial_config.jpg
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/sph_port_configuration.jpg
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_4_dpg.jpg
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9122_5_output.png
   :width: 600px
