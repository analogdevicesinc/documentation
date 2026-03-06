EVAL-AD4113ARDZ User Guide
==========================

The :adi:`EVAL-AD4113ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4116.html>` is a full-featured evaluation board that can be used to evaluate all the features of the :adi:`AD4113 <en/products/ad4111.html>`. The AD4113 is a 16-bit, 31.25 kSPS analog-to-digital converter (ADC) with a ±10 V input voltage range with eight single-ended or four differential channels. All channels have on-board overvoltage and overcurrent protection.

The EVAL-AD4113ARDZ board includes voltage references and power and data insulation and can be connected to Analog Devices, Inc., :adi:`EVAL-SDP-CK1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`. The SDP board provides the connection to a PC via a universal serial bus (USB) port and can provide power for the EVAL-AD4113ARDZ board from the PC USB port. The ACE software configures the AD4113 device functionality and provides dc time domain analysis in the form of waveform graphs, histograms, and associated noise analysis for ADC performance evaluation. Full specifications for the AD4113 are available in the product datasheet, which must be consulted in conjunction with this user guide when working with this evaluation board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4113ardz/ad4113_evb_block_diagram.png
   :align: center

Features
--------

-  Full featured evaluation board for the AD4113
-  PC control in conjunction with the system demonstration platform (EVAL-SDP-CK1Z)
-  PC software for control and data analysis (time domain)
-  Standalone capability

Documents Needed
----------------

-  :adi:`AD4113 Data Sheet <media/en/technical-documentation/data-sheets/ad4111.pdf>`

Required Software
-----------------

-  :adi:`ACE Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>` (:doc:`Install guide </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`)(:doc:`ACE Software </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`)

Equipment Needed
----------------

-  :adi:`EVAL-AD4113ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4116.html>`
-  :adi:`EVAL-SDP-CK1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
-  DC signal source
-  USB cable
-  PC running Windows with USB 2.0 port

Quick Start Guide
=================

Recommended Quick Start Guide
-----------------------------

Use the following procedure to set up the evaluation board:

-   Disconnect the SDP (SDP-K1) board from the USB port of the PC. Install the ACE software. Restart the PC after installation.
-   Connect the SDP board to the EVAL-AD4111ARDZ board, as shown in Figure x.
-   Connect the SDP board to the PC via the USB cable. For Windows® XP, it may be necessary to search for the SDP drivers. Choose to automatically search for the drivers for the SDP board if prompted by the operating system.
-   Launch the **ACE software**.

Quick Start Measurement
-----------------------

Use the following procedure to capture data quickly:

-  Connect the dc signal source to the selected voltage input (for example, VIN0 and VIN1 for differential input)
-  Launch the ACE Software and select the AD4113 board.
-  Double click the AD4113 chip then click the **“Proceed to Waveform Analysis”**.
-  4. In the Waveform Analysis tab, the user can capture and measure the data by clicking **“Run Once”**.

The sample count in the top left area of the Waveform Analysis tab sets the number of samples collected in each batch.

|image1| **Figure 2. Evaluation Board Hardware Configuration**

Hardware Guide
==============

| :doc:`Visit the hardware guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad4111ardz/hardware_guide>`
| **Contents of the Hardware guide:**

-  :doc:`Description </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Set Up Procedures </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Block Diagram </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`On Board Connectors </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Power Supplies </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Serial Interface </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Analog Inputs </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Reference Options </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`
-  :doc:`Schematic, PCB Layout, BOM </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/hardware_guide>`

Software Guide
==============

| :doc:`Visit the software guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`
| **Contents of the Software guide:**

-  :doc:`ACE Software </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`

   -  :doc:`Install Guide </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`

      -  :doc:`Evaluation+ Windows </wiki-migration/resources/eval/user-guides/eval-ad4113ardz/software>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-003.png
   :width: 400px
