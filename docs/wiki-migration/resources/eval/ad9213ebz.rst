EVALUATING THE AD9213 ANALOG-TO-DIGITAL CONVERTER
=================================================

Preface
=======

This user guide describes the :adi:`AD9213-10GEBZ <AD9213>` and :adi:`AD9213-6GEBZ <AD9213>` evaluation boards which provide all of the support circuitry required to operate the ADC in its various modes and configurations. This guide entails both the hardware and software setup needed to acquire data capture from the evaluation board. The\ :adi:`ADS8-V1 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS8-V1>` FPGA based data capture board can be used to configure and capture data from the :adi:`AD9213-10GEBZ <AD9213>` and :adi:`AD9213-6GEBZ <AD9213>` evaluation boards. The user guide for the :adi:`ADS8-V1 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS8-V1>` provides additional information available for consultation during usage. Documents and software tools, where available, can be found at the :adi:`HS-ADC Eval Board homepage <hsadcevalboard>`.

For additional information or questions, post a question on :ez:`Engineer Zone <community/data_converters>`, or send an email to **highspeed.converters@analog.com**.

This user guide wiki applies to the following evaluation boards:<WRAP> </WRAP>

+--------------------------------+------------------------------------------------------+-----------------------------+
| Evaluation Board Part Number   | Description                                          | Board Revision              |
+================================+======================================================+=============================+
| <fc #9400d3>AD9213-10GEBZ</fc> | <fc #9400d3>Evaluation board for AD9213XBPZ-10G</fc> | <fc #9400d3>20 044860c</fc> |
+--------------------------------+------------------------------------------------------+-----------------------------+
| <fc #9400d3>AD9213-6GEBZ</fc>  | <fc #9400d3>Evaluation board for AD9213XBPZ-6G</fc>  | <fc #9400d3>20 044860c</fc> |
+--------------------------------+------------------------------------------------------+-----------------------------+

Typical Setup
=============

|image1|\

.. container:: centeralign

   *Figure 1a.* :adi:`AD9208-3000EBZ <AD9208>` */* :adi:`AD9689-2600EBZ <AD9689>` */* :adi:`AD9689-2000EBZ <AD9689>`\ *\ (Left) and* :doc:`ADS7-V2 </wiki-migration/resources/eval/ads7-v2>` *(Right)*\


|image2|\

.. container:: centeralign

   *Figure 1b.* :adi:`AD9208-3000EBZ <AD9208>` */* :adi:`AD9689-2600EBZ <AD9689>` */* :adi:`AD9689-2000EBZ <AD9689>`\ *\ (Left) and* :adi:`ADS8-V1 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS8-V1>` *(Right)*\


|image3|\

.. container:: centeralign

   *Figure 2. Top-side of* :adi:`AD9208-3000EBZ <AD9208>` */* :adi:`AD9689-2600EBZ <AD9689>` */* :adi:`AD9689-2000EBZ <AD9689>` *Board*\


|image4|\

.. container:: centeralign

   *Figure 3. Bottom-side of* :adi:`AD9208-3000EBZ <AD9208>` */* :adi:`AD9689-2600EBZ <AD9689>` */* :adi:`AD9689-2000EBZ <AD9689>` *Board*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Features
========

-  Full featured evaluation board for the :adi:`AD9208-3000EBZ <AD9208>` / :adi:`AD9689-2600EBZ <AD9689>` / :adi:`AD9689-2000EBZ <AD9689>`.
-  JESD204B coded serial digital outputs with support for lane rates up to 16Gbps/lane.
-  Wide full power bandwidth supports IF sampling of signals up to 9GHz (-3dB point).
-  Four Integrated wide-band decimation filter and NCO blocks supporting multi-band receivers.
-  Fast NCO switching enabled through GPIO pins.
-  Flexible SPI interface controls various product features and functions to meet specific system requirements.
-  Programmable fast over range detection and signal monitoring.
-  On-chip temperature diode for system thermal management.

Helpful Documents
=================

-  :adi:`AD9208` / :adi:`AD9689` Data Sheet
-  `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__ Data Sheet
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  `ADI SPI Application Note </>resources/technical-guides/adispi>>`__ // ADI Serial Control Interface Standard//
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Needed
===============

-  `ACE </>resources/tools-software/ace>>`__ (Analysis \| Control \| Evaluation)

Design and Integration Files
============================

-  `Schematic, Gerber layout and BOM <https://wiki.analog.com/_media/resources/eval/ad9208_3000ebz_files.zip>`__

*Note : The AD9208-3000EBZ, AD9689-2600EBZ and the AD9689-2000EBZ use the same design files. The only difference is in the ADC choice*

Equipment Needed
================

-  PC running Windows®
-  USB 2.0 port and USB 2.0 High-speed A to B Cable
-  :adi:`AD9208-3000EBZ <AD9208>` / :adi:`AD9689-2600EBZ <AD9689>` / :adi:`AD9689-2000EBZ <AD9689>` evaluation board
-  `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__ FPGA-based data capture kit
-  12V, 6.5A switching power supply (such as the SL POWER CENB1080A1251F01 supplied with `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__)
-  Low phase noise analog input source and antialiasing filter
-  Low phase noise sample clock source
-  Reference clock source

Getting Started
===============

This section provides quick start procedures for using the AD9208 evaluation board.

Connector Layout
----------------

|image5|

.. container:: centeralign

   \ *Figure 4.* :doc:`ADS7-V2 </wiki-migration/resources/eval/ads7-v2>` *Connector Layout*\


   |image6|

.. container:: centeralign

   \ *Figure 5.* :adi:`AD9208-3000EBZ <AD9208>` */* :adi:`AD9689-2600EBZ <AD9689>` *Connector Layout*\


.. tip::

   Tip: For more information on Sysref and Global Clock (J3, J4, J200, J202), see the :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`.


.. warning::

   \ **Warning: The AD9208-3000EBZ/AD9689-2600EBZ is electrostatic discharge (ESD) sensitive. Handle the device with care, and employ conducting wrist straps or antistatic bags when handling the board.**\


Configuring the Board
---------------------

|image7|

.. container:: centeralign

   \ *Figure 6. Jumper connections on* :adi:`AD9208-3000EBZ <AD9208>`\ */*\ :adi:`AD9689-2600EBZ <AD9689>`\


Before using the software for testing, configure the evaluation boards as follows:

-  Before connecting the AD9208/AD9689 evaluation board to the ADS7-V2, jump the following pins: **P304, P305, P307, P308, P309, P311,** and **P312.** Do not jump **P7** (Temperature Sensor Enable) or **P100** (Power Down / Standby). Jump **P401** towards the inside of the board, to power the board via FMC. See Figure 6 for all jumper connections.
-  Ensure that the data capture board is switched to “OFF.” (**S1** on the data capture board) Connect the evaluation board to the data capture board via the FMC connector found on the underside of the board, as shown in Figure 1. Connect the power supply and USB cable to the data capture board.
-  Turn on the `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__.
-  The `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__ should appear in the Device Manager as shown in Figure 7.<WRAP>\ |image8|\ </WRAP>

.. container:: centeralign

   \ *Figure 7. Device Manager showing* `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__\


-  If the Device Manager does not show the `ADS7-V2EBZ <https://wiki.analog.com/ads7-v2>`__ listed as shown in Figure 7, unplug all USB devices from the PC, uninstall and re-install ACE and restart the hardware setup from step 1.
-  On the AD9208 evaluation board, provide a clean, low jitter clock source to connector **J201** (preferably via a shielded RG-58 50 Ω coaxial cable) and set the amplitude to 10 dBm. This is the ADC Sample Clock. Set the sample clock frequency to the rated value of 3GHz for the AD9208 and 2.6GHz for the AD9689.
-  On the ADS7-V2, provide a clean, low jitter clock source to connector **J3** and set the amplitude to 10 dBm. This is the Reference Clock for the gigabit transceivers in the FPGA. The REFCLK frequency can be calculated using the following empirical formulae:

.. container:: centeralign

   :math:`\displaystyle LaneLineRate=M \times Nprime \times (\frac{10}{8}) \times f_{out}/L` bps/lane, where


.. container:: centeralign

   :math:`f_{out} = f_{ADC SAMPLE CLOCK}/DecimationRatio`


.. container:: centeralign

   :math:`Nprime=8 or 16`


.. container:: centeralign

   :math:`REFCLK = LaneLineRate/20`


.. container:: centeralign

   :sub:`(Default Nprime = 16; DCM = Chip Decimation Ratio (DCM = 1 for Full Bandwidth Mode); M = Virtual Converters; L = Lanes)`


-  On the AD9208/AD9689 evaluation board, connect a clean signal generator with low phase noise to **J101** or **J104** via coaxial cable for channels A and B respectively. It is recommended to use a narrow-band, band-pass filter with 50 Ω terminations and an appropriate center frequency.

ACE Setup
---------

-  Download and install `ACE </>resources/tools-software/ace>>`__ if it is not already installed.
-  The AD9208 / AD9689 ACE plug-in can be found under the :adi:`9208 Evaluation Board Software Section <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9208.html#eb-relatedsoftware>`, :adi:`9689 Evaluation Board Software Section <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9689.html#eb-relatedsoftware>` or through ACE's Plug-In Manager (Tools -> Manage Plug-Ins).<WRAP>

.. tip::

   Tip: Some browsers (Such as Internet Explorer) may save the file as a .zip file instead of an .acezip file. If this happens, simply download and rename the file with an .acezip file extension.


</WRAP>

-  Once the .acezip file has been downloaded from the Analog Devices website, right click on it and install the plug-in, or double click to install.
-  Click Start -> All Programs -> Analog Devices -> ACE -> ACE
-  The AD9208/AD9689 plug-in should appear as in Figure 8 if successfully installed.
-  If the AD9208/AD9689 plug-in does not appear, or no board is detected, make sure the ADS7-V2 is powered on and the evaluation board is properly connected. Make sure that ACE has been updated to the most recent version and the necessary plug-ins have been installed.<WRAP>\ |image9|\ |image10|\ </WRAP>

.. container:: centeralign

   \ *Figure 8. ACE's AD9208 / AD9689 Plug-in*\


<WRAP>

.. note::

   Note: Differences may occur between ACE plug-in versions, including the version number seen in Figure 8 above or components in any of the other images below - however, these will not affect the performance of the part nor the fundamental features described in this user guide.


</WRAP>

-  Click on the plug-in to open it. This will open the AD9208/AD9689 Board View. Click the "**Program FPGA Image**" button to program the ADS7-V2's FPGA for communicating with the AD9208-3000EBZ/AD9689-2600EBZ. Once it is done programming, double click on the blue AD9208 / AD9689 chip (in the middle of the board) to open up the Chip View.<WRAP>

.. warning::

   \ **Warning: Programming the FPGA will power the AD9208 evaluation board via the FMC connector. Removing any of the board's power jumpers (as seen in Figure 6) while the board is on or in operation may cause damage to the board, board components, and/or the chip. Removing the board while it is being powered via the FMC connector may also cause damage to the board.**\


</WRAP>

<WRAP>\ |image11|\ |image12|\ </WRAP>

.. container:: centeralign

   \ *Figure 9. ACE's AD9208 / AD9689 Board View*

   *<fc #ff00ff>Note: The plugin might display some warnings/errors. These can be ignored for now</fc>*\


<WRAP>\ |image13|\ </WRAP>

.. container:: centeralign

   \ *Figure 10. AD9208 Chip View*

   *<fc #ff00ff>The AD9689 Chip view is similar to the AD9208 chip view</fc>*\


Obtaining a Full Bandwidth Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Under Initial Configuration, change the number of Virtual Converters to 1. Click Apply to apply the chip settings. Set the reference clock to the appropriate frequency as recommended by the ACE plugin.<WRAP>\ |image14|\ |image15|\ </WRAP>

.. container:: centeralign

   \ *Figure 11. Chip Settings, AD9208-3000 on top, AD9689-2600 on bottom*\


<WRAP>\ |image16|\ </WRAP>

.. container:: centeralign

   \ *Figure 12. Apply Settings*\


-  The chip view will update to reflect the changes made to the board. If any changes are made, the chip can be read by clicking the Read All button.<WRAP>\ |image17|\ </WRAP>

.. container:: centeralign

   \ *Figure 13. Read All*\


-  Issue a data path reset to the AD9208 by clicking its checkbox and clicking Apply Changes. The data path reset bit will automatically self clear.<WRAP>\ |image18|\ </WRAP>

.. container:: centeralign

   \ *Figure 14. Data path reset*\


<WRAP>\ |image19|\ </WRAP>

.. container:: centeralign

   \ *Figure 15. Apply Changes*\


-   If the PLL Lock Lost indicator lights up, you can reset it by powering down the JESD link using the Link Control dropdown box, and clicking Apply Changes.<WRAP>\ |image20|\ </WRAP>

.. container:: centeralign

   \ *Figure 16. PLL Lock Lost*\


<WRAP>\ |image21|\ </WRAP>

.. container:: centeralign

   \ *Figure 17. Link Power Down*\


-  Enable the link again and Apply Changes.<WRAP>\ |image22|\ </WRAP>

.. container:: centeralign

   \ *Figure 18. Link Enable*\


-  Click Proceed to Analysis. This is ACE's Analysis tool for data from the ADC, displaying both sample plots and FFTs. Click on FFT and run one capture.<WRAP>\ |image23|\ </WRAP>

.. container:: centeralign

   \ *Figure 19. Analysis Tool*\


<WRAP>\ |image24|\ </WRAP>

.. container:: centeralign

   \ *Figure 20. Display FFTs*\


<WRAP>\ |image25|\ </WRAP>

.. container:: centeralign

   \ *Figure 21. Run one capture*\


<WRAP>

.. important::

   Tip: Capturing data using another program (e.g. VisualAnalog, proprietary code, etc.) while using ACE concurrently may cause errors in ACE's data capture. If this occurs, the best solution is to restart the evaluation boards and work solely via ACE, or to setup the part in ACE then capture solely in the other program.


</WRAP>

-  A successful capture is shown below, with a filtered 255 MHz signal input to Channel A. <WRAP>\ |image26|\ </WRAP>

.. container:: centeralign

   \ *Figure 22. AD9208-3000 FFT at 255MHz Analog Input to Channel A*\


-  In order to get a capture from Channel B, use the Register Debugger within ACE and write 0x01 to register 0x0564. Click the **Read All** button. Repeat Step 6. <WRAP>\ |image27|\ |image28|\ </WRAP>

.. container:: centeralign

   \ *Figure 23. ACE Register Debugger*\


Obtaining a DDC Capture
~~~~~~~~~~~~~~~~~~~~~~~

The procedure to obtain a FFT using DDC is the same between AD9208 and AD9689. The steps below use the AD9208 as the example, but the same can be done to the AD9689 plugin with the sample rate set to 2.6GSPS.

-  This section explains the steps needed to setup the AD9208-3000EBZ in a DDC (Decimal Down Converter) setup as shown in Figure 24. <WRAP>\ |image29|\ </WRAP>

.. container:: centeralign

   \ *Figure 24. AD9208 DDC setup block diagram*\


-  Under Initial Configuration, set the Chip Operating Mode for two DDCs. The DDC settings will become available, and automatically set up for Decimate-by-4 mode. For the decimation, select "HB1_HB2_HB3 Complex" - three half-band filters, i.e. Decimate-by-8. Set the number of lanes to 4, the number of converters to 4, and the number of Octets per Frame to 2. Apply the settings. <WRAP>\ |image30|\ </WRAP>

.. container:: centeralign

   \ *Figure 25. DDC Chip Settings*\


-  The chip view will update to reflect the changes. Click on the NCO block to change the Numerically Controlled Oscillator's frequency to 1300 MHz. Enable the 6dB gain for the DDC from the dropdown menu. Click Apply Changes to apply both.<WRAP>\ |image31|\ </WRAP>

.. container:: centeralign

   \ *Figure 26. NCO Frequency Setting*\


<WRAP>\ |image32|\ </WRAP>

.. container:: centeralign

   \ *Figure 27. DDC Gain*\


-  Navigate to the second DDC (DDC1) and make the same changes.<WRAP>\ |image33|\ </WRAP>

.. container:: centeralign

   \ *Figure 28. DDC Selection*\


-  In Analysis, run a capture. DDC0 can be selected from Channel A and DDC1 can be selected from Channel B.<WRAP>\ |image34|\ </WRAP>

.. container:: centeralign

   \ *Figure 29. DDC Selection*\


-  A successful capture is shown below, with a filtered 1305 MHz signal input to Channel A / DDC0.<WRAP>\ |image35|\ </WRAP>

.. container:: centeralign

   \ *Figure 30. AD9208-3000 DDC FFT at 1305MHz Analog Input to Channel A; NCO tuning frequency = 1300MHz*\


Troubleshooting Tips
====================

EVALUATION BOARD ISN'T FUNCTIONING PROPERLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  It is possible that a board component has been rendered inoperable by ESD, removing a jumper during powered operation, accidental shorting while probing, etc. Try checking the supply domain voltages of the board while it is powered. They should be as follows:

======= ====== ========== ===============
Domain  Jumper Test Point Approx. Voltage
======= ====== ========== ===============
AVDD_1  P307   TP303      0.975 V
AVDD_2  P308   TP304      1.90 V
AVDD_3  P309   TP305      2.50 V
DRVDD_1 P304   TP301      0.975 V
DRVDD_2 P311   TP306      1.90 V
DVDD    P305   TP302      0.975 V
SPI_VDD P312   TP307      1.90 V
======= ====== ========== ===============

-  If a short is detected between any of the supply domains and ground, or an open is detected across fuse chip F401 (next to P401), a component may have been damaged. This may have occurred from jumper or board removal while being actively powered (See the warning in the :doc:`ACE Setup section </wiki-migration/resources/eval/ad9208-3000ebz>`). See the :doc:`Design Integration Files section </wiki-migration/resources/eval/ad9208-3000ebz>` for the schematic and/or bill of materials for the relevant components to test and/or replace.

EVALUATION BOARD IS NOT COMMUNICATING WITH THE ADS7-V2 / NO SPI COMMUNICATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Make sure that the FPGA on the ADS7-V2 has been programmed - a lit LED DS15 (FPGA_DONE) on the top of the ADS7-V2 and a powered fan are good indicators of the FPGA being programmed.
-  Check the common mode voltage on the JESD204B traces. On the evaluation board, the common mode voltage should be roughly two-thirds of DRVDD_1. On the ADS7-V2, the common mode voltage should be around 1.2 volts.
-  Check Test Point 307 - test point for the SPI_VDD supply domain, jumper P312 - and make sure it is around 1.9 volts.
-  To test SPI operation, attempt to both read and write to register 0x000A using ACE's Register Debugger (see Figure 23). This register is an open register available for testing memory reads and writes. If the register reads back the same value written to it, SPI is operational.
-  All registers reading back as either all ones or all zeros (i.e., 0xFF or 0x00) may indicate no SPI communication.
-  Register 0x0000 (SPI Configuration A) reading back 0x81 in ACE may indicate no SPI communication as a result of the FPGA on the ADS7-V2 not being programmed.

EVALUATION BOARD FAILS TO CAPTURE DATA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Ensure that the board is functioning properly and that SPI communication is successful - see previous troubleshooting tips.
-  Check the Clock Detect register 0x011B to see if the sample clock is being detected. 0x01 indicates detection, 0x00 indicates no clock detected. Check the signal generator input on connector J201. Try checking the common mode voltage on the clock pins, which should be roughly two-thirds of AVDD_1. Try placing a differential oscilloscope probe on the clock pins to see if the clock signal is reaching the chip.
-  Check the PLL Locked indicator (see Figure 16) or register 0x056F (PLL Status). If the light in the plugin chip view is green / if the register reads back 0x80, the PLL is locked. If it is not locked:

   -  Check the clock being input to connector J201 (in this guide, 3 GHz or 2.6GHz depending on the part).
   -  Check the JESD204B settings under the Initial Configuration. Reference the :adi:`AD9208` / :adi:`AD9689` datasheet for supported lane options.
   -  Check the reference clock and make sure it matches your JESD settings.
   -  Make sure P100 (Power Down / Standby Jumper, see Figure 6) is not jumped.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/ce02b_fpga_connnections.png
   :width: 620px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ADS8-V1EBZ-AD9208 Typ Setup.png
   :width: 620px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/topofboard.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/bottomofboard.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/fpgapinlabeling.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/pinlabeling.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/topofboardjumpers.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/0.png
   :width: 300px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/1.png
   :width: 200px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ace_ad9689-2600_start.png
   :width: 200px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/a1.png
   :width: 300px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ace_ad9689-2600_board_view.png
   :width: 200px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/2.png
   :width: 500px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/3.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ace_ad9689-2600_summary.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/4.png
   :width: 200px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/5.png
   :width: 100px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/6.png
   :width: 250px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/7.png
   :width: 100px
.. |image20| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/8.png
   :width: 100px
.. |image21| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/9.png
   :width: 500px
.. |image22| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/11.png
   :width: 500px
.. |image23| image:: https://wiki.analog.com/_media/resources/eval/screen_shot_01-04-18_at_04.37_pm.png
   :width: 500px
.. |image24| image:: https://wiki.analog.com/_media/resources/eval/screen_shot_01-04-18_at_04.36_pm.png
   :width: 200px
.. |image25| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/14.png
   :width: 150px
.. |image26| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/15.png
   :width: 500px
.. |image27| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/15p0.png
   :width: 200px
.. |image28| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/5.png
   :width: 100px
.. |image29| image:: https://wiki.analog.com/_media/resources/eval/lmfs_4421_generic.png
.. |image30| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/16.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/17.png
   :width: 200px
.. |image32| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/18.png
   :width: 200px
.. |image33| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/19.png
   :width: 200px
.. |image34| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/23.png
   :width: 200px
.. |image35| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9208/stepbystep/22.png
   :width: 600px
