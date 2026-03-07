EVAL-AD7173-8ARDZ User Guide
============================

The :adi:`EVAL-AD7173-8ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7173-8.html>` evaluation board features the :adi:`AD7173-8 <en/products/ad7173-8.html>`, a 24-bit, 31.25 kSPS analog-to-digital converter (ADC) with integrated analog input buffers, on-board power supply regulation, and an external amplifier section for amplifier evaluation. A 5V USB is regulated to 5 V and 3.3 V; this supplies the :adi:`AD7173-8 <en/products/ad7173-8.html>` and support components. The evaluation board connects to a USB port via the system demonstration platform (SDP) controller board :adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` (:adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`).

The AD717x Eval+ software fully configures the :adi:`AD7173-8 <en/products/ad7173-8.html>` device functionality via a user accessible register interface and provides dc time domain analysis in the form of waveform graphs, histograms, and associated noise analysis for ADC performance evaluation. Full specifications on the :adi:`AD7173-8 <en/products/ad7173-8.html>` are available in the product data sheet, which should be consulted in conjunction with this user guide when working with the evaluation board. Full details for the SDP-K1 controller board are available on the Analog Devices website.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7173-8/ebal_board_block_diagram.png
   :width: 800px

**Figure 1. Evaluation Board Block Diagram**

Features
--------

-  Full featured evaluation board for the AD7173-8
-  PC control in conjunction with the Analog Devices, Inc., SDP-K1 board (EVAL-SDP-CK1Z)
-  PC software for control and data analysis (time domain)
-  Standalone capability

Documents Needed
----------------

-  :adi:`AD7173-8 Data Sheet <media/en/technical-documentation/data-sheets/ad7173-8.pdf>`

Required Software
-----------------

-  :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>` (:doc:`Installation guide </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`)(:doc:`ACE Software </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`)

Equipment Needed
----------------

-  :adi:`EVAL-AD7173-8ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7173-8.html>`
-  :adi:`EVAL-SDP-CK1Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
-  DC signal source
-  USB cable
-  PC running Windows with USB 2.0 port

Quick Start Guide
=================

Recommended Quick Start Guide
-----------------------------

Use the following procedure to set up the evaluation board:

-   With the SDP-K1 board disconnected from the USB port of the PC, install the ACE software (can be downloaded online). Restart the PC after the software installation is complete (for complete software installation instructions, see the Evaluation Software section).
-   Connect the SDP-K1 board to the EVAL-AD7173-8ARDZ board, as shown in Figure x.
-   Connect the SDP-K1 board to the PC via the USB cable. For Windows® XP, it may be necessary to search for the SDP drivers. Choose to automatically search for the drivers for the SDP board if prompted by the operating system.
-   Launch the **ACE software**.

Quick Start Measurement
-----------------------

Use the following procedure to capture data quickly:

-  Connect the dc signal source to the selected voltage input (for example, AIN0 and AIN1 for differential input)
-  Launch the ACE Software and select the **AD7173-8 Board**.
-  Double click the AD7173-8 chip then click the **“Proceed to Waveform Analysis”**.
-  In the Waveform Analysis tab, the user can capture and measure the data by clicking **“Run Once”**.

The sample count in the top left area of the Waveform Analysis tab sets the number of samples collected in each batch.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7173-8/65008_2.jpg
   :width: 800px

**Figure 2. Evaluation Board Hardware Configuration**

Hardware Guide
==============

| :doc:`Visit the hardware guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
| **Contents of the Hardware guide:**

-  :doc:`Description </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Set Up Procedures </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Block Diagram </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`On Board Connectors </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Power Supplies </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Serial Interface </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Analog Inputs </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Reference Options </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
-  :doc:`Schematic, PCB Layout, BOM </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`

Software Guide
==============

| :doc:`Visit the software guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`
| **Contents of the Software guide:**

-  :doc:`ACE Software </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`

   -  :doc:`Installation Guide </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`

      -  :doc:`Evaluation+ Windows </wiki-migration/resources/eval/user-guides/eval-ad7173-8ardz/software>`
