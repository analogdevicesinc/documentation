EVALUATING THE AD8195 HDMI/DVI BUFFER
=====================================

Preface
-------

The :adi:`AD8195` is an HDMI™/DVI buffer featuring equalized TMDS inputs and pre-emphasized TMDS outputs, ideal for systems with long cable runs. The AD8195 includes bidirectional buffering for the DDC bus and bidirectional buffering with integrated pull-up resistors for the CEC bus. The DDC and CEC buffers are powered independently of the TMDS buffers so that DDC/CEC functionality can be maintained when the system is powered off.

This user guide describes the setup needed to buffer an HDMI signal through the :adi:`AD8195-EVALZ <eval-ad8195>` evaluation board to characterize the AD8195 1:1 HDMI/DVI Buffer with Equalization.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1. AD8195-EVALZ Evaluation Board*\


.. container:: centeralign

   \ |image2| *Figure 2. AD8195 Evaluation Setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


.. container:: centeralign

   \ *Table 1. Jumper Functionality*\


+---------------------+------------+--------------------------------------------------+--------------------------------------------------------------+
| Function            | Designator | Functionality when jumper is installed           | Functionality when jumper is *not* installed                 |
+=====================+============+==================================================+==============================================================+
| Pre-Emphasis Enable | W1         | Pre-Emphasis Enabled, Output Boost = 6 dB        | Pre-Emphasis Disabled, Output Boost = 0 dB (factory default) |
+---------------------+------------+--------------------------------------------------+--------------------------------------------------------------+
| Tx Enable           | W2         | Tx Output Enabled                                | Tx Output Disabled                                           |
+---------------------+------------+--------------------------------------------------+--------------------------------------------------------------+
| +3.3V Enable        | W3         | +3.3V Regulator Supply Enabled (factory default) | +3.3V Regulator Supply Disabled                              |
+---------------------+------------+--------------------------------------------------+--------------------------------------------------------------+

.. container:: centeralign

   \ *Table 2. Switch Functionality*\


+---------------------------+------------+--------------------------------+--------------------------------+
| Function                  | Designator | Functionality when switch is 1 | Functionality when switch is 0 |
+===========================+============+================================+================================+
| VREF_IN reference select  | SW2        | AMUXVCC Selected               | VREF_IN Selected               |
+---------------------------+------------+--------------------------------+--------------------------------+
| VREF_OUT reference select | SW3        | AMUXVCC Selected               | VREF_OUT Selected              |
+---------------------------+------------+--------------------------------+--------------------------------+

Helpful Files
-------------

-  Datasheet: :adi:`AD8195 Datasheet <static/imported-files/data_sheets/AD8195.pdf>`
-  Schematic: `AD8195-EVALZ Rev D <https://wiki.analog.com/_media/resources/eval/ad8195-evalz_revd_schematic.pdf>`__
-  Bill of Materials: `AD8195-EVALZ Rev D <https://wiki.analog.com/_media/resources/eval/ad8195-evalz_revd_bom.xlsx>`__
-  PCB Gerber Files: `AD8195-EVALZ Rev C <https://wiki.analog.com/_media/resources/eval/ad8195-evalz_revc_gerberfiles.zip>`__
-  PCB BRD File: `AD8195-EVALZ Rev C <https://wiki.analog.com/_media/resources/eval/ad8195-evalz_revc_brd.zip>`__
-  PCB Layout PDF: `AD8195-EVALZ Rev C <https://wiki.analog.com/_media/resources/eval/ad8195-evalz_revc_layout.pdf>`__

Hardware Needed
---------------

-  AD8195-EVALZ Evaluation Board
-  9V 18W AC/DC Wall Mount Adapter (included in kit) or equivalent
-  Video and Audio Source with HDMI Port
-  Monitor Display with Sound Output and HDMI Port
-  Two (2) HDMI Cables
-  Voltmeter

Quick Start Guide
-----------------

-  Confirm that jumpers W2 and W3 are installed and jumper W1 is not installed.
-  Confirm that switches SW2 and SW3 are set to 1.
-  Connect the wall adapter DC plug to P1 of the evaluation board and the AC plug to a 90 ~ 264 VAC socket. Check that regulated +3.3V and +5V voltages can be observed at test points labeled “+3P3V” and “+5V_INTERNAL”, respectively.
-  Connect HDMI cable from the video and audio source to the evaluation board HDMI input connector P2.
-  Connect HDMI cable from the evaluation board HDMI output connector P4 to HDMI display (sink). Video and audio should be observed on the monitor.

Troubleshooting
---------------

This section lists items to check and practices to use when debugging any unexpected performance of a board. If unexpected results occur:

-  Check if each voltage supply test point of the evaluation board has the correct value.
-  Check if the jumpers are appropriately configured.
-  Check if the switches are set to the intended positions.
-  Power cycle the AD8195 evaluation board.
-  Disconnect and reconnect the source and sink from/to the AD8195 evaluation board.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ad8195-evalz_eval_board.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad8195-evalz_eval_setup.jpg
   :width: 600px
