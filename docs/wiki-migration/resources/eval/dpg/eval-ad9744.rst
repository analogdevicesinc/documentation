EVALUATING THE AD9740/AD9742/AD9744/AD9748 DIGITAL-TO-ANALOG CONVERTERS
=======================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9740-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9740.html>`/:adi:`AD9742-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9742.html>`/:adi:`AD9744-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9744.html>`/:adi:`AD9748-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9748.html>` evaluation boards to characterize the :adi:`AD9748` 8-bit, :adi:`AD9740` 10-bit, :adi:`AD9742` 12-bit, and :adi:`AD9744` 14-bit, 210 MSPS TxDAC+® digital-to-analog converters.

The evaluation boards have an FMC form-factor with FMC connector that is compatible to the Vita 57.1 standard. The boards provide provision for on-board clocking (using ACE software for control) or external direct clocking. The :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` controller board automatically formats the data and sends it to the evaluation board, which simplifies the evaluation of the device. The evaluation board receives power from the :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` power supply.

This guide shows how AD9748-FMC-EBZ, AD9740-FMC-EBZ, AD9742-FMC-EBZ, and AD9744-FMC-EBZ, work with SDP-H1 controller board developed by Analog Devices. Link to the previous user guide document is provided for customers who still have the DPG2 controller board.

Typical Setup
-------------

|image1|

.. container:: centeralign

   *Figure 1. AD9744-FMC-EBZ Evaluation Board with SDP-H1*


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  `User Guide <https://wiki.analog.com/_media/ad974xacp-pcbz_ug-1650.pdf>`__ for the previous evaluation board
-  Data Sheet: :adi:`AD9740 <media/en/technical-documentation/data-sheets/AD9740.pdf>`, :adi:`AD9742 <media/en/technical-documentation/data-sheets/AD9742.pdf>`, :adi:`AD9744 <media/en/technical-documentation/data-sheets/AD9744.pdf>`, :adi:`AD9748 <media/en/technical-documentation/data-sheets/AD9748.pdf>`
-  IBIS Models: :adi:`AD9740 <media/en/simulation-models/ibis-models/ad9740ar.ibs>`, :adi:`AD9742 <media/en/simulation-models/ibis-models/ad9742ar.ibs>`, :adi:`AD9744 <media/en/simulation-models/ibis-models/ad9744ar.ibs>`, :adi:`AD9748 <media/en/simulation-models/ibis-models/ad9748cp.ibs>`
-  Schematic: `AD9744-FMC-EBZ Rev B <https://wiki.analog.com/_media/resources/eval/dpg/02-064131-01-b.pdf>`__
-  Bill of Materials: `AD9744-FMC-EBZ Rev B <https://wiki.analog.com/_media/resources/eval/dpg/ad9744-fmc-ebz_bom.xlsx>`__
-  PCB Gerber Files: `AD9744-FMC-EBZ Rev B <https://wiki.analog.com/_media/resources/eval/dpg/ad9744-fmc-ebz_gerber_files.zip>`__
-  PCB BRD File: `AD9744-FMC-EBZ Rev B <https://wiki.analog.com/_media/resources/eval/dpg/ad9744-fmc-ebz.zip>`__
-  PCB Layout: `AD9744-FMC-EBZ Rev B <https://wiki.analog.com/_media/resources/eval/dpg/ad9744-fmc-ebz.pdf>`__

Software Needed:
----------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` or :doc:`DPG Downloader </wiki-migration/resources/eval/dpg/dpgdownloader>`

Hardware Needed
---------------

-  System demonstration platform :doc:`SDP-H1 </wiki-migration/resources/eval/dpg/hsdac-sdp-h1>` controller board (EVAL-SDP-CH1Z)
-  :adi:`AD9740-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9740.html>`/:adi:`AD9742-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9742.html>`/:adi:`AD9744-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9744.html>`/:adi:`AD9748-FMC-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9748.html>` evaluation board
-  Spectrum analyzer
-  PC with ACE and DPGLite Software
-  12Vdc 1A Wall Adapter for SDP-H1
-  (1) USB A to USB Mini Cable
-  (1) SMA Cable

Quick Start Guide
-----------------

Reconfiguring the Evaluation Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section details the quick start procedures for setting up the AD9740-FMC-EBZ/AD9742-FMC-EBZ/AD9744-FMC-EBZ/ AD9748-FMC-EBZ evaluation board. Refer to the table below to configure the clock and output option of the evaluation board.

| 
| ===Clock Configuration=== The evaluation board has a provision for on-board or external clocking configuration.

.. container:: centeralign

   |image2|\


.. container:: centeralign

   Table 1. Clock Options


-  The **on-board clocking configuration** is implemented by **default**.
-  For external clocking configuration, split the output of a High-Frequency Clock Source (e.g. SMA100A) using an SMA T-adapter and connect to J3 and J4 of the evaluation board. Set SMA to desired clock frequency and 16dBm output.

Output Configuration
^^^^^^^^^^^^^^^^^^^^

The evaluation board has a provision for single-ended or differential output. The **single-ended configuration** is implemented by **default**.

.. container:: centeralign

   |image3|\


.. container:: centeralign

   Table 2. Output Options


Board Jumpers Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A 0402, 0-ohm resistor are installed on the jumpers. Move these 0-ohm resistors accordingly to the required configuration as shown in table 3.

.. container:: centeralign

   |image4|\


.. container:: centeralign

   Table 3. Jumper Names


Software Installation
^^^^^^^^^^^^^^^^^^^^^

The ACE software and DPGDownloader Lite are needed to configure the device. ACE is the software that is used to load the registers in the ADF4351 while DPGDownloader Lite is used to load the vector into the evaluation board. Install ACE from this link :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`. During installation, expand the High-Speed DAC Components list and select the **DPG Lite** and **HSDAC eval boards support through SDP drivers** checkboxes. The plugins for this board can be downloaded from the plugin manager in the ACE software.


|image5|

.. container:: centeralign

   *Figure 2. DPG Lite Installation*


To configure the evaluation board to output a 5.0MHz sine wave at 210MSPS with DPGDownloader Lite and ACE software, take the following steps:

| 
| === Configuring the EVB using ACE === Follow the steps to set-up and configure the clocking of the eval board.

-  From the initial ACE screen, click the AD9744-FMC-EBZ.
-  On the Clocking Setup Tab, select Onboard clock (ADF4351) on the clock source drop-down menu, and enter 210MHz on the DAC clock field. Refer to the Figure 3.
-  Click Apply and a summary window will pop up. Confirm if the entered details are correct.

|image6|

.. container:: centeralign

   *Figure 3. AD9744 Plugin Board Wizard*


| 
| === Loading a vector using DPGDownloader Lite === Follow the steps to generate and download a vector into the eval board.

-  Confirm first if the DCO frequency detected is the same as the clock frequency set on ACE (210MHz). Repeat the ACE process if frequencies don't match.
-  In the DPGDownloader Lite window (see Figure 4), click the Add Generated Waveform dropdown menu and select Single Tone as the vector type.
-  Refer to Figure 4 for the appropriate frequency values and default settings.

.. important::

   \ **Note:** Select 14 bits DAC Resolution for all generics (AD9744, AD9740, AD9742 & AD9748).The NC pins are disconnected in the corresponding evaluation board.


.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   Table 4. Data bit pins connection


-  In the Data Playback panel, select the 1I: Single Tone - 5.01 MHz; 0.0 dB; 0.0° (In-Phase) option from the I Data Vector dropdown menu.
-  Select the 1Q: Single Tone - 5.01 MHz; 0.0 dB; 0.0° (Quadrature) option from the Q Data Vector dropdown menu.
-  Click the Download button in the lower right of the Data Playback panel.
-  Click the Play button, located to the left of the Download button, to begin vector playback.
-  The signal frequency output then appears on the spectrum analyzer.

|image8|

.. container:: centeralign

   *Figure 4. DPG Lite Panel*


Verification
------------

Figure 5 shows the output window that appears on the Spectrum Analyzer hardware. Ensure that the following options are set:

-  Connect Spectrum Analyzer to SMA J1.
-  Set the Stop frequency to 105.0MHz.
-  Set the Ref level to 0 dBm.
-  Set the #Res BW to 220 Hz.
-  Set the VBW to 220 Hz.
-  Check that the DAC output, the top right Mrkr1, is approximately 5.0000 MHz and check that the amplitude is approximately 0 dBm.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_output.png
   :align: center
   :width: 600px

.. container:: centeralign

   *Figure 5. AD9744 Output Spectrum*


Troubleshooting
---------------

On-Board LEDs
^^^^^^^^^^^^^

There are two LEDs on the evaluation board, which are the 3.3V power supply LED, and the ADF4351 lock detect LED. These LEDs are shown in Figure 6. These two LEDs will light up when 3.3V is supplied to the board, and when the ADF4351 clock chip is working properly.


|image9|

.. container:: centeralign

   *Figure 6. AD9744-FMC-EBZ Evaluation Board LEDs*


| 
| === DPGDownloader Lite Does Not Recognize the Evaluation Board === There may be cases where the DPGDownloader Lite does not recognize the evaluation board. If this occurs, open the DPGDownloader Lite and unplug then replug the USB cable. If DPGDownloader Lite still does not recognize the evaluation board, there is a chance that the firmware of the board is not updated and the evaluation board must be reprogrammed with the new firmware. Contact a local Analog Devices salesperson or distributor to arrange for this reprogramming to be done.

| 

ACE Does Not Recognize the Evaluation Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| There may be cases where the AD9744 icon does not appear on the Attached Hardware tab of ACE, or the icon is there but once clicked, will indicate an Unavailable status on the bottom as shown in Figure 7. These errors can occur if the ACE software is started before powering up and connecting the evaluation board to the PC, or if the evaluation board is power cycled and ACE is not restarted. The most basic remedy for this issue is to close ACE and reopen it (restart). As long as the evaluation board is powered up and connected to the PC, ACE recognizes the evaluation board and will work again. |image10|

.. container:: centeralign

   *Figure 7. Unavailable state error in ACE*


DCO Frequency is not correct or not detected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Check if the proper resistors are installed indicated in Table 1. If using the Onboard clock, check if DS2 LED lights up. If not, restart ACE and then reprogram the board with the desired clock frequency. If using an external clock source, increase the output power level to 20dBm. Make sure the resistors installed are properly soldered.
| === DAC Output Frequency is not correct === Check if the DCO Frequency detected on the DPG Panel matches the Data Rate field. These two should match for proper vector generation and playing to the DAC.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_sdp_h1.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_table1.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_table2.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_table3.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_ace_install.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_ace1.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad974x_databits.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_dpg.png
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_led.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9744_ace_error1.png
   :width: 600px
