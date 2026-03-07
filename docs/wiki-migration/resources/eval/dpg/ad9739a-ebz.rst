AD9737A-EBZ/AD9739A-EBZ Quick Start Guide
=========================================

|

.. warning::

   \ **NOTE:**

   | Support for the eval-ad9739a is discontinued starting with 2022_R2 Kuiper Linux release and it will not be supported in future releases. Last release in which pre-build files can be found is 2021_r2. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases. The HDL project source code can still be found on :git-hdl:`hdl_2021_r2 <projects/ad9739a_fmc>` release branch.


Getting started with the AD9737A-EBZ/AD9739A-EBZ Evaluation Board
-----------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  AD9737A-EBZ or AD9739A-EBZ Evaluation Board
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment
~~~~~~~~~~~~~~~~~~~~~

-  Low Phase Noise Sinusoidal Signal Generator or ADF4350 Evaluation Board
-  Spectrum Analyzer
-  Data Pattern Generator Series 2 (DPG2)

Helpful Files
~~~~~~~~~~~~~

-  Download the `AD9739A Evaluation Board Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a_evaluation_board_quick_start_guide.pdf>`_\ for DPG3 users
-  Data Sheet: :adi:`AD9739 Data Sheet <static/imported-files/data_sheets/AD9739A.pdf>`
-  IBIS Model: :adi:`IBIS Model <en/license/ibis-models?mediaPath=media/en/simulation-models/ibis-models/ad9739.ibs&modelType=ibis-models>`
-  Schematic: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_schematic.pdf>`_ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_schematic.pdf>`_
-  Bill of Materials: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_bom_customer.xls>`_ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_bom_customer.xls>`_
-  PCB Gerber files:`ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_gerber_files.zip>`_ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_gerber_files.zip>`_
-  PCB BRD file:`ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva.zip>`_ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb.zip>`_
-  PCB Layout PDF: `ad9739a-ebz_rev a <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-ebz_reva_layout.pdf>`_ , `ad9739a-fmc-ebz_rev b <https://wiki.analog.com/_media/resources/eval/dpg/ad9739a-fmc-ebz_revb_layout.pdf>`_

Introduction
~~~~~~~~~~~~

The purpose of this document is to get the AD9737A/AD9739A evaluation board up and running as quickly as possible and provide guidance on how to optimize the controllers in the part to get the optimal performance out of the :adi:`AD9737A` or :adi:`AD9739A`.

Software
~~~~~~~~

The AD9737A-EBZ/AD9739A-EBZ is designed to receive data from a DPG2. The DAC Software Suite, plus the AD9739A Update, is required for evaluation. The DAC Software Suite is included on the Evaluation Board CD, or can be downloaded from the DPG web site at http://www.analog.com/dpg. This will install DPGDownloader (for loading vectors into the DPG2) and the legacy AD9739A SPI application. However, ACE, a newer evaluation software from ADI, is the preferred evaluation software over the SPI application. It can be downloaded from the ACE website at https://wiki.analog.com/resources/tools-software/ace. Also required is the ACE plug-in for the evaluation board, which is available for download on the AD9737A or AD9739A eval webpage in the software section at http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9739A.html#eb-relatedsoftware.

Hardware Setup
~~~~~~~~~~~~~~

To operate the board, a power supply capable of +5vdc, 2A should be connected to J17. A spectrum analyzer or an oscilloscope to view the DAC output should be connected to J1. The diagram in Figure 1 shows the location of each connection. A low jitter (< 0.5psec RMS) sine or square wave clock source should be connected to J3. The DC level of the clock is unimportant since the clock is AC-coupled on the evaluation board before the CLKP/N inputs. The included USB cable should be used to connect the Evaluation Board to a PC. Note that the software described above should be installed before connecting the USB cable.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9739-ebz_1.png
   :alt: ad9739-ebz_1.png
   :align: center
   :width: 300px

Getting Started
---------------

This quick-start will setup a single-tone output from the AD9737A or AD9739A to provide a brief introduction to the part, as well as a basic functionality test. This can be done using either the ACE software, the preferred evaluation method, or the SPI software. Each process for the software is given in the following sections.

A. ACE
~~~~~~

To begin, open ACE from the start window. It can be found by following the file path to the program or by searching in the Windows search bar for “ACE.” The |ace_icon_small.png| icon indicates the ACE software.

If the board is connected properly, ACE will detect it and display it on the Start page under *Attached Hardware*. Double click this board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_detected.png
   :alt: ad9739a_detected.png
   :align: center

Ensure that the |connection_icon.png| button in lower left corner of the subsystem image (located under the *System* tab) is green, meaning the board is connected. If not, click it, select the AD9737A or AD739A, and click *Acquire*.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_system.png
   :alt: ad9739a_system.png
   :align: center

Double click on the subsystem image to reach the board block diagram.


|ad9739a_chipview.png|

.. container:: centeralign

   Board block diagram


Set ACE Parameters
^^^^^^^^^^^^^^^^^^

*Poll Device* should be enabled on the top left of the ACE program. Click *Run Example Startup Routine* on the board diagram. The steps taken in this routine are available in the AD9737A/AD9739A datasheet. Double click on the AD9739A on the board diagram to view the chip diagram.


|ad9739a_clickview.png|

.. container:: centeralign

   Chip block diagram


Click *Read All* on the top left of the ACE program. On the chip diagram, DLL LOCKED, RCVR_LOCK, and RCVR_TRX_ON should all be enabled, as indicated with the green circles in the chip diagram. On the board diagram, the MU controller and data receiver should be locked and the DLL tracking should be established.

Load Pattern from the DPG2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open DPGDownloader (Start -> Programs -> Analog Devices -> DPG -> DPGDownloader). Ensure that “AD9739A” is selected in the *Evaluation Board* drop-down list. For this evaluation board, "LVDS" is the only valid *Port Configuration*, and will be selected automatically. *The Data Clock Frequency* display should read approximately 500MHz.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/dpgdownloader.png
   :alt: dpgdownloader.png
   :align: center

Click on *Add Generated Waveform*, and then *Single Tone*, as shown in Figure 3. A Single Tone panel will be added to the vector list. Start by entering the Clock Frequency (2GHz in this case). You can enter 2G in the box. Next, enter 180MHz (180M) as the desired frequency of the tone. The DAC Resolution should be set at 14 bits.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image007.png
   :alt: image007.png
   :align: center

Next, in the lower portion of the screen, select “1: Single Tone” as the Data Vector. The other options can be left at their default.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image008.png
   :alt: image008.png
   :align: center

After the DPG2 is correctly setup, click the Download button (|image009.png|) in the lower right, then the Play button (|image010.png|) to begin vector playback into the AD9739A. The resulting spectrum is shown in the *Result* section.

B. SPI Software
~~~~~~~~~~~~~~~

To begin, open the AD9739A SPI application (Start -> Programs -> Analog Devices -> AD9739A-EBZ -> AD9739A SPI). Connect a +5Vdc power supply to J17, and connect a 2GHz, 0dBm clock to J3.

Enable Mu Controller
^^^^^^^^^^^^^^^^^^^^

In order to optimize and lock the Mu Controller, it is only necessary to have the DAC clock running (no data needs to be presented). Click the MU_ENA button in the MU Controller section of the SPI application, as shown in Figure 2. Then run the SPI application by clicking on the Run button (|image004.png|) in the upper left of the screen.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image005.png
   :alt: image005.png
   :align: center
   :width: 300px

.. _load-pattern-from-the-dpg2-1:

Load Pattern from the DPG2
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open DPGDownloader (Start -> Programs -> Analog Devices -> DPG -> DPGDownloader). Ensure that “AD9739A” is selected in the *Evaluation Board* drop-down list. For this evaluation board, "LVDS" is the only valid *Port Configuration*, and will be selected automatically. *The Data Clock Frequency* display should read approximately 500MHz.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/dpgdownloader.png
   :alt: dpgdownloader.png
   :align: center

Click on *Add Generated Waveform*, and then *Single Tone*, as shown in Figure 3. A Single Tone panel will be added to the vector list. Start by entering the Clock Frequency (2GHz in this case). You can enter 2G in the box. Next, enter 180MHz (180M) as the desired frequency of the tone. The DAC Resolution should be set at 14 bits.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image007.png
   :alt: image007.png
   :align: center

Next, in the lower portion of the screen, select “1: Single Tone” as the Data Vector. The other options can be left at their default.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image008.png
   :alt: image008.png
   :align: center

After the DPG2 is correctly setup, click the Download button (|image009.png|) in the lower right, then the Play button (|image010.png|) to begin vector playback into the AD9739A.

Enable LVDS Controller
^^^^^^^^^^^^^^^^^^^^^^

Once the pattern is loaded into the DPG2 and running, the final step is to enable the LVDS Controller. In the AD9739A SPI application, enable the RCV_LOOP and RCV_ENA buttons. Click the Run button (|image1|). Once the run is complete, the RCVR LCK and RCVR TRX ON indicators should be green, as shown in Figure 9.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image011.png
   :alt: image011.png
   :align: center
   :width: 500px

|image012.png|\ Another way to verify that the controller is in the correct spot (and not on the edge) is to check the status of the four status bits which sample the rising edge of the DCI at four different phases. DCI PHS1 should always be high, and DCI PHS3 should always be low. The other bits will toggle as the LVDS controller searches for the correct timing. The ideal case is shown in Figure 10. Increasing the value of the FINE_DEL_SKEW allows for a wider search around the DCI edge, and should reduce the toggling on PHS0 and PHS2. This is usually required when the DCI signal has a lot of jitter.

Result
~~~~~~

The final result of this setup should be as shown below. Note the RF Attenuation of 20dB to accurately measure harmonics.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/image013.gif
   :alt: image013.gif
   :align: center
   :width: 600px

AD9739A USB SPI Software
~~~~~~~~~~~~~~~~~~~~~~~~

The SPI software is broken up into numerous sections. Several of them are described here, as they pertain to the evaluation board. For complete descriptions of each SPI register, see the AD9737A/AD9739A datasheet. In the interest of continuous quality improvements, the images below may not exactly match your version of the software.

SPI Settings and Powerdown/Reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image014.png|\ These bits (shown in Figure 12) control the operation of the SPI port on the AD9737A and the AD9739A, as well as the master reset and individual power-down bits. Changing the SDIO DIR or DATADIR bits will cause the SPI application to stop functioning correctly. Do not change these bits. The Reset button is “sticky”, that is, the part will stay in reset for as long as the button is enabled. To reset the part, set this bit, run the SPI application, then unset this bit and run the application again.

Controller Clock Controls and Analog FS controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image015.png|\ The Controller Clock controls enable the Mu Controller and LVDS controllers. For normal operation, both of these should be enabled. The Clock GEN PD switch powers down the clocking structure, and should be left disabled for normal use.

The DAC current ouput has an adjustable full-scale value. The FSC Set option allows for this adjustment. After running the SPI application, the full-scale current in miliamps will be displayed here.

*Mu Controller Clock Enable: Register 0x02 Bit 0 LVDS Controller Clock Enable: Register 0x02 Bit 1 Analog Full-Scale Setting (10 bit Gain DAC 10-30mA adjustment): Register 0x06 bit 0:8, Register 0x07 bits 0,1*

Decoder Controller and IRQ Controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decoder Mode: Register 0x08 Bits 0,1 0x0 – Normal Mode 0x1 – Return to zero (RZ) Mode 0x2 – Mix Mode

Cross Control
^^^^^^^^^^^^^

*CLKP Offset Setting: Register 0x24 Bits 0-3 CLKP Direction Bit: Register 0x24 Bit 4 CLKP Offset Setting: Register 0x25 Bits 0-3 CLKP Direction Bit: Register 0x25 Bit 4 Damp: Register 0x25 Bits 7*

Mu Controller
^^^^^^^^^^^^^

::

     Mu Controller Enable: Register 0x26 Bit 0 (Set to 1 to enable the controller)

Mu Controller Gain: Register 0x26 Bits 1,2 (Optimal Setting is a Gain of 1) MU Desired Phase: Desired Phase Value for Phase to Voltage Converter to Optimize Mu Controller. The optimal setting is negative 6 (max of 16) . Register 0x27 bits 0-4 Slope: Slope the mu contoller will lock onto Register 0x26 bit 6 (Optimal setting is Negative slope set bit to 0) MU_DEL_Manual: Register 0x28 bits 0-7 and 0x27 bits 6,7: Sets the point where the Mu Controller begins to search. It is best to set it to the middle of the delay line . The maximum Mu delay is 432, so set these bits to approximately 220. Mode: Register: 0x26 Bits 4, 5 Sets the Mode in which the Controller searches:

::

         0x00 – Search and Track (Optimal Setting)
         0x01 – Track Only
         0x10 – Search Only
         0x11 – Invalid

Search Mode: 0x27 – Bits 5, 6 Sets the Mode in which the search for the optimal phase is performed

::

         0x00 – Down
         0x01 – Up
         0x10 – Up/Down (Optimal Setting)
         0x11 – Invalid

Search GB: sets a GB from the beginning and end of the Mu Delay line in which the Mu controller will not enter into unless it does not find a valid phase outside the GB. Register 0x29 bits 0-4. Optimal value is Decimal 11. Tolerance: Sets the Tolerance of the phase search. Register 0x29 bit 7

::

         0 – Not Exact. Can find a phase within 2 phases of the desired phase
         1- Exact. Finds the exact phase you are targeting (Optimal Setting)

ContRST: Controls whether the controller will reset or continue if it does not find the desired phase

::

         0 – Continue (Optimal Setting)
         1 – Reset

Phase Detector Enable: Register 0x24 bit 5. Enables the Phase Detector (Set to 1 to enable the Phase Detector) Phase Detector Comparator Boost: Optimizes the bias to the Phase Detector (Set to 1 to enable) Bias: Register 0x24 Bits 0-3: Manual Control of the bias if the Boost control is not enabled Duty Cycle Fix: Register 0x25 Bit 7 Enables the duty cycle correction in the Mu Controller. Recommended to always enable (Set to 1 to enable) Direction: Register 0x25 Bit 6 Sets the direction that the duty cycle will be corrected

::

         0 – Negative (Optimal Setting)
         1 - Positive 

Offset: Register Register 0x25 Bit 0-5 Sets the Duty Cycle Correction manually if Fix is not enabled

The status read back bits for the mu controller are as follows: MU_LCK: Register 0x2A bit 0 (value of 1 means the controller is locked) LST_LCK: Register 0x2A bit 1 (Value of 1 means the control lost lock)

In order to read back the present MU Delay and phase value, it is necessary to set the Read bit high and then low before the values can be read back: Read: Register 0x26 Bit 3 Mu Delay Readback: Register 0x28 bits 0-7 and 0x27 bits 6,7 (Total of 9 bits in the read back the maximum Mu delay value is d432 or x1B0) MUD_PH_Readback: Register 0x27 bits 0-4 – Phase the controller locked to. In order to use the Mu controller in manual mode the following bits are utilized:

::

     Mu Controller Enable: Register 0x26 Bit 0 (Set to 0 to disable the controller)

MU_DEL_Manual: Register 0x28 bits 0-7 and 0x27 bits 7,8. (Total of 9 bits the maximum Mu delay value is d432 or x1B0)

LVDS Receiver Controls
^^^^^^^^^^^^^^^^^^^^^^

ACE Software
~~~~~~~~~~~~

The ACE software is organized to allow the user to evaluate and control the AD9122A evaluation board. The “Initial Configuration” wizard, which is only available for certain boards, controls the DAC and PLL setups. Block diagram views of the board and chip contain elements that can be used to vary parameters like ref current and data format. These parameters can be changed using check boxes, drop down menus, and input boxes. Some parameters do not have settings shown in the diagram. Double click on the parameter to view the available settings, seen with the NCO settings below.


|ad9122_nco.png|

.. container:: centeralign

   NCO settings for the AD9122


In addition, some parameters can be enabled or disabled. This feature is evident by the color of the block parameter. For example, if the block parameter is dark blue, the parameter is enabled. If it is light grey, it is disabled. To enable or disable a parameter, click on it.

.. container:: column


   ..

|ad9739a_on.png|

.. container:: column


   ..

|ad9739a_off.png|

.. container:: column

   
   .. container:: centeralign

      Enabled parameter

   


.. container:: column

   
   .. container:: centeralign

      Disabled parameter

   



More direct changes to registers and bit fields can be made in the memory map, which is linked from the chip block diagram through the “Proceed to Memory Map” button. In this view, names, addresses, and data can be manually altered by the user.


   



|ad9122_memmap.png|

.. container:: centeralign

   Bench Set-Up


ACE also contains the Macro Tool, which can be used to record register reads and writes. This is executed in the memory map view or with the initialization wizard. To use, check the “Record Sub-Commands” checkbox and press the record button. Changes in the memory map, which are bolded until they are applied to the part, are recorded as UI commands by the macro tool once the changes are made. Changed register write commands for the controls are also recorded. Hit “Apply Changes” to execute the commands and make changes in the memory map. To stop recording, click the “Stop Recording” button. A macro tool page with the command steps will be created. The macro can be saved using the “Save Macro” button so that it may be loaded for future use.



|ad9122_macrocommands.png|

.. container:: centeralign

   Macro tool in ACE. The *Stop Recording*, *Record*, and *Save Macro* commands are located at the top of the macro tool.


The raw macro file will be saved using ACE syntax, which is not easily readable. To remedy this, the ACE software download includes the Macro to Hex Conversion Tool. The user can choose to include or exclude register write, reads, and/or comments in the conversion. The file pathways for the source and save paths should be the same, except that one should be an .acemacro file and the other should be a .txt file. The “Convert” button converts and opens the converted text file, which is easier to read. The conversion tool can also convert back to an .acemacro file if desired.

.. container:: column


   ..

|ad9122_m2hconvert_5.png|

.. container:: column


   ..

|ad9122_m2hconvert_4.png|

.. container:: column

   
   .. container:: centeralign

      Conversion set-up for macro to hex

   


.. container:: column

   
   .. container:: centeralign

      Converted text file

   



For more information about ACE and its features, visit https://wiki.analog.com/resources/tools-software/ace.

.. |ace_icon_small.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ace_icon_small.png
.. |connection_icon.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/connection_icon.png
.. |ad9739a_chipview.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_chipview.png
.. |ad9739a_clickview.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_clickview.png
.. |image009.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image010.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image004.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image004.png
   :width: 15px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/image004.png
.. |image012.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image012.png
   :width: 200px
.. |image014.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image014.png
   :width: 100px
.. |image015.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/image015.png
   :width: 100px
.. |ad9122_nco.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_nco.png
.. |ad9739a_on.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_on.png
.. |ad9739a_off.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9739a_off.png
.. |ad9122_memmap.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_memmap.png
.. |ad9122_macrocommands.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_macrocommands.png
.. |ad9122_m2hconvert_5.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_5.png
.. |ad9122_m2hconvert_4.png| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9122_m2hconvert_4.png
