EVAL-AD4116ASDZ User Guide
==========================

The :adi:`EVAL-AD4116ASDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4116.html>` is a full-featured evaluation board that can be used to evaluate all the features of the :adi:`AD4116 <en/products/ad4116.html>`. The AD4116 is a 24-bit, sigma-delta analog-to-digital converter (ADC) with 6 differential/11 single-ended, high impedance (≥10 MΩ) bipolar, ±10 V voltage inputs, and 2 differential/4 single-ended/pseudo differential direct ADC inputs. All channels have onboard overvoltage and overcurrent protection.

The EVAL-AD4116ASDZ board includes voltage references and power and data insulation and can be connected to the Analog Devices, Inc., :adi:`EVAL-SDP-CB1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-b.html>`. The SDP board provides the connection to a PC via a universal serial bus (USB) port and can provide power for the EVAL-AD4116ASDZ board from the PC USB port. The AD411X Eval+ evaluation software configures the AD4116 device functionality and provides dc time domain analysis in the form of waveform graphs, histograms, and associated noise analysis for ADC performance evaluation. Full specifications for the AD4116 are available in the product datasheet, which must be consulted in conjunction with this user guide when working with this evaluation board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4116_block_diagram_with_fig.png
   :align: center

Features
--------

-  Full featured evaluation board for the AD4116
-  PC control in conjunction with the system demonstration platform (EVAL-SDP-CB1Z)
-  PC software for control and data analysis (time domain)
-  Standalone capability

Documents Needed
----------------

-  :adi:`AD4116 Data Sheet <media/en/technical-documentation/data-sheets/ad4116.pdf>`

Required Software
-----------------

-  :adi:`AD411x Evaluation Software <media/en/evaluation-boards-kits/evaluation-software/ad411x-eval-installer.zip>` (:doc:`Install guide </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`)(:doc:`Eval+ Description </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`)

Equipment Needed
----------------

-  :adi:`EVAL-AD4116ASDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4116.html>`
-  :adi:`EVAL-SDP-CB1Z system demonstration platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-b.html>`
-  DC signal source
-  USB cable
-  PC running Windows with USB 2.0 port

Quick Start Guide
=================

Recommended Quick Start Guide
-----------------------------

Use the following procedure to set up the evaluation board:

-   Disconnect the SDP (SDP-B) board from the USB port of the PC. Install the **AD411X Eval+** software. Restart the PC after installation.
-   Connect the SDP board to the EVAL-AD4116ASDZ board, as shown in Figure 3.
-   Fasten the two boards together with the enclosed plastic screw washer set.
-   Connect the SDP board to the PC via the USB cable. For Windows® XP, it may be necessary to search for the SDP drivers. Choose to automatically search for the drivers for the SDP board if prompted by the operating system.
-   Launch the **AD411X Eval+** software from the **Analog Devices** subfolder in the **Programs** menu.

Quick Start Measurement
-----------------------

Use the following procedure to capture data quickly:

-  Connect the dc signal source to the selected voltage input (for example, VIN0 and VIN1 for differential input).
-  Launch the **AD411X Eval+** software and select **QuickStart**.
-  In the **Configuration** tab, under **Demo Mode**, click **All Single-Ended**, and then click **Sample** (see Figure 16).
-  In the **Voltage Waveform tab**, the user can evaluate the measured data.

The **Samples** box in the top right corner of the main window sets the number of samples collected in each batch.

|image1| **Figure 2. Evaluation Board Hardware Configuration**

Hardware Guide
==============

| :doc:`Visit the hardware guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
| **Contents of the Hardware guide:**

-  :doc:`Description </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Set Up Procedures </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Block Diagram </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Hardware Link Options </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`On Board Connectors </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Power Supplies </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Serial Interface </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Analog Inputs </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Reference Options </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
-  :doc:`Schematic, PCB Layout, BOM </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`

Software Guide
==============

| :doc:`Visit the software guide chapter here </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`
| **Contents of the Software guide:**

-  :doc:`Evaluation+ Software </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`

   -  :doc:`Install Guide </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`

      -  :doc:`Evaluation+ Windows </wiki-migration/resources/eval/user-guides/eval-ad4116asdz/software>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-003.png
   :width: 400px
