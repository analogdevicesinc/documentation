EVALUATING THE AD9709/AD9763/AD9765/AD9767 DIGITAL-TO-ANALOG CONVERTER
======================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9767-KIT-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9767.html#eb-relatedhardware>` to characterize :adi:`AD9709`/:adi:`AD9763`/:adi:`AD9765`/:adi:`AD9767` dual-port, high speed, 2-channel, 8-/10-/12-/14-bit CMOS DACs.

This guide shows how the AD9767-KIT-EBZ works with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have DPG2 and DPG3 controller boards.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. AD9767-KIT-EBZ Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  :adi:`User Guide <media/en/technical-documentation/application-notes/AN-555.pdf>` for DPG2/DPG3 users
-  Data Sheet: :adi:`AD9709 <media/en/technical-documentation/data-sheets/AD9709.pdf>`, :adi:`AD9763/65/67 <media/en/technical-documentation/data-sheets/AD9763_9765_9767.pdf>`
-  IBIS Models: :adi:`AD9709 <media/en/simulation-models/ibis-models/ad9709ast_3v.ibs>`, :adi:`AD9763/65/67 <media/en/simulation-models/ibis-models/ad9765ast.ibs>`
-  Schematics: `AD9709/63/65/67 Evaluation Board <https://wiki.analog.com/_media/resources/eval/dpg/ad9709_63_65_67-ebz_schematic.pdf>`_
-  Bill of Materials: `AD9709/63/65/67 Evaluation Board <https://wiki.analog.com/_media/resources/eval/dpg/ad9709_63_65_67-ebz_bom.xls>`_
-  PCB Gerber files: `AD9709/63/65/67 Evaluation Board <https://wiki.analog.com/_media/resources/eval/dpg/ad9709_63_65_67-ebz_gerber_files.zip>`_
-  PCB Layout PDF: Refer to :adi:`User Guide <media/en/technical-documentation/application-notes/AN-555.pdf>`

Software Needed:
----------------

-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

Hardware Needed:
----------------

-  :adi:`AD9767-KIT-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9767.html#eb-relatedhardware>` that includes:

   -  :adi:`AD9709/63/65/67 Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9767.html#eb-relatedhardware>`
   -  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adaptor Board
   -  CMOS-DAC/DPG2 Interface Board
   -  Ribbon Cables

-  :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) Board
-  12Vdc 1A Wall Adapter for SDP-H1
-  3Vdc power supply for the evaluation board.
-  PC with DPG Lite Software Application
-  High-Frequency Continuous Wave Generator (Clock Source)
-  Signal/Spectrum Analyzer
-  USB A to USB Mini Cables
-  (3) SMA Cables
-  SMA T-connector

Quick Start Guide
-----------------

-  To evaluate performance of lower resolution generics using :adi:`AD9767-EBZ <eval-ad9767>`, disconnect LSBs of :adi:`AD9767` from the data input connector, P1. Refer to Figure 4 in :doc:`Reconfiguring the Evaluation Board </wiki-migration/resources/eval/dpg/eval-ad976x>`.
-  Attach the :adi:`AD9709/63/65/67 Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9767.html#eb-relatedhardware>` to the SDP-H1 using the adaptor boards and cables. Refer to Figure 1.
-  Supply 3.3Vdc to the evaluation board and 12Vdc to the SDP-H1.
-  Using an SMA T-connector, split the output of a High-Frequency Clock Source (e.g. SMA100A) to SMA J701 on SDP-H1 and to SMA S1 on the evaluation board. Set to 100MHz, 16dBm output.
-  Connect the spectrum analyzer to SMA S6 on the evaluation board.
-  Open DPG Downloader Lite. On the **SDP-H1 Unit 1 Panel**, select **LVCMOS-3.3V** on the Port Configuration. Double check if the **DCO Frequency** detected is 100MHz.
-  Click on the **Add Generator Waveforms** pulldown menu select **Single Tone**. Set the **Data Rate** to 100MHz and **Desired Frequency** to 5MHz. Check the **Unsigned Data** box and the **Generate Complex Data (I & Q)**. Refer to Figure 2.
-  Select 16 bits **DAC Resolution** for all generics (AD9767, AD9765, AD9763, and AD9709). |image2|\

.. container:: centeralign

   
   //Figure 2. DPG Lite Session for AD9709/63/65/67 Evaluation Board] *


\* Select the I/Q tone from the* **I/Q Data Vector** *pulldown menu. \* Press the* **Download** *arrow and then the* **Play** *button. The spectrum similar to Figure 3 should appear in the signal/spectrum analyzer.\ \

.. container:: centeralign

   *\ Figure 3. Spectrum Output for AD9767; Fdac = 100MSPS, Fout = 5MHz //


=====Reconfiguring the Evaluation Board===== This section details how to configure the :adi:`AD9709/63/65/67 Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9767.html#eb-relatedhardware>` and allow user to evaluate AD9709, AD9763 and AD9765. Set up the board as shown in figure 4.

-  To evaluate AD9709, Remove RP6 for DAC channel 1 and RP8 for DAC channel 2.
-  To evaluate AD9763, Remove RP6 for DAC channel 1 and RP8 for DAC channel 2 and add 2 22ohm resistors.
-  To evaluate AD9765, Remove RP6 for DAC channel 1 and RP8 for DAC channel 2 and add 4 22ohm resistors.

|image3|

.. container:: centeralign

   *Figure 4. AD9709 \| AD9763 \| AD9765 LSB Configurations*\


Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. If unexpected results occur:

-  Check the supply voltage of the evaluation board. Voltage rail should be 3.3V.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board is lit up. Reconnect the board to the FMC connector of SDP-H1 if not lit up.
-  Check if the SDP-H1 is being supplied properly by 12Vdc adaptor. Some LEDs on the SDP-H1 should lit up.
-  Power cycle both the SDP-H1 and the AD9709/6x evaluation board.
-  Check on the Spectrum Analyzer if the DAC clock inputs are properly driven. For 100MHz clock, the spectrum analyzer should detect a weak signal at 100MHz. If not detected, check properly the clock source and connections.
-  Disconnect and reconnect the SDP-H1 and AD9709/6x evaluation board. Reopen DPG Lite software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9767_kit_setup.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/dpg_ad9767.jpg
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad976x_lower_resolution.png
   :width: 600px
