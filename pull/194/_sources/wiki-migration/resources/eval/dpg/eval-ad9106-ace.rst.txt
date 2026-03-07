Evaluating the AD9106/AD9102 Waveform Generator Digital-to-Analog Converter using ACE
=====================================================================================

Navigation
----------

You can return to Homepage here: :doc:`AD9106 & AD9102 Evaluation Boards </wiki-migration/resources/eval/dpg/eval-ad9106>`

Preface
-------

This user guide describes how to acquire data capture from :adi:`AD9106-ARDZ-EBZ <eval-ad9106>`/:adi:`AD9102-ARDZ-EBZ <eval-ad9102>` evaluation board to characterize :adi:`AD9106`/:adi:`AD9102` high-speed digital-to-analog converter. It focuses on how the evaluation board works with :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` controller board and :doc:`Analysis Control Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>` both developed by Analog Devices.

The evaluation setup can be powered by USB only and does not require a high-frequency waveform generator for clock input. The evaluation board has an on-board 156.25 MHz crystal oscillator. To fit the evaluation system in a small form factor and manage power consumption within USB specifications, AD9106 and AD9102 supply voltages AVDD, DVDD and CLKVDD are limited to 3.3V only.

Software Needed
---------------

-  :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`
-  :adi:`AD9106/02 ACE Plugin <plugins/ace/board.ad9106.1.2022.43200.acezip>`

.. important::

   
   -  Do not install ACE on a computer with DAC Software Suite.
   -  **Known Issue:** ACE may fail to detect HS-DAC boards, details :doc:`here </wiki-migration/resources/tools-software/ace/knownissues>`.
   


Quick Start Guide
-----------------

-  Attach AD9106-ARDZ-EBZ / AD9102-ARDZ-EBZ evaluation board to SDP-K1. Make sure SDP-K1 VIO is set to 3.3V through the P14 jumper by placing the shunt on the center and 3.3V pins, refer to Figure 1.

.. container:: centeralign

   \ |image1| *Figure 1. SDP-K1 VIO Configuration*\


.. important::

   Note: If the VIO is set to 1.8V, 0xFFFF data will be read to all registers in the memory map and can't apply data changes to all registers.


-  Connect SDP-K1 to PC over USB. DS1 and DS2 on SDP-K1 and DS1 on the evaluation board should light up. If DAC outputs are connected to the on-board amplifiers, connect a 7V to 12V 30W wall wart to SDP-K1 DC Jack or to P15 on the evaluation board.
-  Connect the outputs of the evaluation board to an oscilloscope using SMA to BNC cables. Apply the oscilloscope settings shown in the waveform captures of the example patterns in Figures 5a and 5b.
-  Open ACE. The board will automatically be recognized by the software. Otherwise, install the plugin for AD9106/AD9102 evaluation board by following the steps in this page: :doc:`Quickstart - ACE Quickstart and Plug-in Installation </wiki-migration/resources/tools-software/ace/userguide/quickstart>`.
-  In ACE, select the settings enumerated below and shown in Figure 2a or 2b. Click **Apply**.

   -  Clock Input: **On-board Oscillator (Xtal = 156.25MHz)**
   -  DAC Output Setting: **RF Balun Transformer**

.. container:: centeralign

   \ |image2| *Figure 2a. EVAL-AD9106 Default Board Configuration*\


.. container:: centeralign

   \ |image3|//Figure 2b. EVAL-AD9102 Default Board Configuration *


\* Click the AD9106 / AD9102 Chip to proceed to chip view. Apply the chip settings enumerated below and shown in Figure 3. \* DDS Output Frequency:* **10MHz**\ *\* Waveform Selector Dropdown Menus:* **Prestored**\ *\* Prestored Waveform Selector Dropdown Menus:* **DDSx output**\ *\* DAC1 Dig Gain:* **1**\ *\* DAC2 Dig Gain:* **0.75**\ *\* DAC3 Dig Gain:* **0.5**\ *\* DAC4 Dig Gain:* **0.25** *

.. container:: centeralign

   \ *\ Figure 3a. AD9106 Chip View\ *


.. container:: centeralign

   \ *\ Figure 3b. AD9102 Chip View\ *


\* Click* **Apply Changes** *to update SPI register values.

.. container:: centeralign

   \ *\ Figure 4. AD910x Apply Changes Button in Chip View//


-  Click **Trigger** to generate output waveforms. Waveform captures are shown in Figures 5a and 5b.

+------------------------------------------------------------------------+---------------------------------------------+
| |ad9106_50.jpg|                                                        | |ad9106_50.jpg|                             |
+------------------------------------------------------------------------+---------------------------------------------+
| *Figure 5a. EVAL-AD9106 10MHz DDS Sinewave with Digital Gain Settings* | *Figure 5b. EVAL-AD9102 10MHz DDS Sinewave* |
+------------------------------------------------------------------------+---------------------------------------------+

Loading Sample Waveforms
------------------------

There are six available sample waveform settings that can be loaded from the plugin to the device.

::

   -From chip view, click **Load Sample Waveforms** at lower left side of the window.
   -Select an option from the sample waveforms shown in Figures 6a and 6b. Resulting waveforms are shown under  [[/resources/eval/dpg/eval-ad9106|Sample waveforms out of RF transformer and Onboard Amplifier]].

.. container:: centeralign

   {{ :resources:eval:dpg:ad910x_samplewaveforms.png?800 |}}


.. container:: centeralign

   //Figure 6a. AD9106 Sample Waveform  | Figure 6b. AD9102 Sample Waveform //


.. note::

   To modify sample waveform, either

   
   -  click **Back to AD910x** then modify the settings from the chip view; or
   -  open **Memory Map** then change register values.
   
   | Click **Apply Changes** then **Trigger**.


| ===== Extracting power up sequence and SPI registers ===== When transitioning from an evaluation platform to custom designed hardware it is often necessary to understand the state of the hardware settings or interactions occurring during an evaluation session. ACE provides the option to :doc:`Export Interaction With Hardware </wiki-migration/resources/tools-software/ace/exporting>`.

Using ACE Macro Tool
~~~~~~~~~~~~~~~~~~~~

.. container:: centeralign

   \ |ad910x_ace_macro.png|\


.. container:: centeralign

   \ *Figure 7. AD9106 ACE Macro Tool*\


-  Expand **Tools** and select **Macro Tools** from the left side pane of ACE. This should open the **Macro Tool** at the right side pane.
-  Click **Record** button.
-  Apply settings as needed. After completing some interactions with the GUI, press the stop icon.

.. tip::

   The macro can be edited by choosing steps to skip or adding comments. It macro can be exported to be used as a reference for the interactions that happened in the session, or to replay in a different session


Using Memory Map
~~~~~~~~~~~~~~~~

The user can also opt to use Memory Map to Extract SPI Register Settings at the time of waveform generation.

-  From Chip View, click **Proceed to Memory Map**.
-  Click **Read All** and **Export**.
-  Save the Export file.

===== Modifying SRAM Vectors ===== The AD910x ACE plugin includes an **SRAM Control** feature that can be used to Generate Waveform and Load waveform into SRAM. This is accessible from the chip view by clicking **Proceed to SRAM Control**.

ACE includes a :doc:`vector generation tool </wiki-migration/resources/tools-software/ace/vector-generation>` accessible from the left side menu. ==== Loading SRAM Vector ====

.. container:: centeralign

   \ |ad9106_sram_control_tab\_.jpg|\ |ad9102_sram_control.jpg|\


.. container:: centeralign

   \ *Figure 8a. AD9106 SRAM Control \| Figure 8b. AD9102 SRAM Control*\


From the SRAM Control Tab, select the vector file path in the Vector file text box.

-  Click **Write SRAM Data** to write the data in the AD910x SRAM Addresses.
-  To read SRAM data, click the **Read SRAM Data**.

.. note::

   SRAM registers are left justified. Data written to memory map are automatically shifted to the left by **4 bits** for AD9106 and **2 bits** for AD9102.


==== Using the Vector Generator ==== The plugin also includes a :doc:`vector generation tool </wiki-migration/resources/tools-software/ace/vector-generation>` also accessible in the **SRAM Control Tab**\ |ad9106_vector_generator.jpg|\ |ad9102_vector_generator_tab.jpg|\

.. container:: centeralign

   \ *Figure 9a. AD9106 Vector Generator \| Figure 9b. AD9102 Vector Generator*\


To Generate a Vector
^^^^^^^^^^^^^^^^^^^^

-  From the SRAM Control tab, Click **Generate Vector** button. This will prompt user to VectorGenerator Tab.
-  From ADD wizard, choose from the available common vectors then click **(+)**.
-  From GENERATE wizard, set the desired vector characteristics.
-  Click **Preview** to generate a preview of the waveform.
-  Click **Export**. This will generate a text file.
-  Save file to a known folder.

.. note::

   Ensure that vector characteristics is similar to Figure 17 or that:

   
   -  Data Rate is **similar** to DAC Clock.
   -  Record length is **4096**.
   -  Resolution is **12 bits** for AD9106 and **14 bits** for AD9102.
   -  Amplitude control should be in **dB**.
   


To Preview a Vector file
^^^^^^^^^^^^^^^^^^^^^^^^

-  From ADD Wizard under File, select **Txt file** vector. This will add a vector to GENERATE wizard.
-  From GENERATE wizard, Select **Real Vector** and correct file path for your vector file.
-  Select correct resolution used and Data Rate.
-  Click **Preview**.

.. note::

   There are sample vector text file in the default Vector File Path that can be used as reference.


| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/sdp-k1_vio_config.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9106.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9102.png
   :width: 600px
.. |ad9106_50.jpg| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9106_50.jpg
.. |ad910x_ace_macro.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad910x_ace_macro.png
   :width: 600px
.. |ad9106_sram_control_tab\_.jpg| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9106_sram_control_tab_.jpg
   :width: 390px
.. |ad9102_sram_control.jpg| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9102_sram_control.jpg
   :width: 390px
.. |ad9106_vector_generator.jpg| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9106_vector_generator.jpg
   :width: 390px
.. |ad9102_vector_generator_tab.jpg| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9102_vector_generator_tab.jpg
   :width: 390px
