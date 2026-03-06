EVALUATING THE AD8369 EVAL BOARD
================================

FEATURES
--------

-  Full featured evaluation board for the or AD8369
-  SPI control via SDP-S board
-  5.0 V supply operation

EVALUATION KIT CONTENTS
-----------------------

-  AD8369-ACE-EVALZ evaluation board

ADDITIONAL HARDWARE REQUIRED
----------------------------

-  Analog signal generator
-  Analog signal analyzer
-  Power supplies (5 V/1 A)
-  PC with Windows XP, Windows 7, or Windows 10 operating system
-  USB 2.0 port, recommended (USB 1.1-compatible)
-  SDP-S controller board

ADDITIONAL SOFTWARE REQUIRED
----------------------------

-  Analysis \| Control \| Evaluation (ACE) software
-  AD8369 ACE Plug-in

.. image:: https://wiki.analog.com/_media/resources/eval/ad8369_ace_evalz.png
   :align: center

EVALUATION BOARD SOFTWARE
~~~~~~~~~~~~~~~~~~~~~~~~~

ACE SOFTWARE REQUIREMENTS AND INSTALLATION
------------------------------------------

Installing the ACE Software Suite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the ACE software suite, take the following steps:

-  Download the latest ACE software from the ACE product page.
-  Open the downloaded file to begin the installation process. The default installation path is C:\\Program Files (x86)\\Analog Devices\\ACE.

If desired, the user can create a desktop icon for the ACE software. Otherwise, the ACE executable can be found by clicking Start > Analog Devices > ACE.

Installing the AD8369 Plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Double-click the AD8369.acezip file to install the evaluation board plugins.
-  Ensure that the board.ad8369 and chip.ad8369 folders are located inside the C:\\ProgramData\\Analog Devices\\ACE\\Plugins folder.

EVALUATION BOARD HARDWARE
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/ad8369_ace_evalz_testbench.png
   :align: center

EVALUATION PROCEDURES
~~~~~~~~~~~~~~~~~~~~~

TESTING AD8369 EVALUATION BOARD
-------------------------------

-  Connect the DC supply.
-  Connect the RFIN_HI to signal source.
-  Connect the RFOUT_LO to signal analyzer.
-  Plug USB cable to PC.
-  Open the ACE software. The software automatically detects the AD8369-EVALZ evaluation board.

.. image:: https://wiki.analog.com/_media/resources/eval/ad8369_ace_overall.png
   :align: center

-  Double-click the AD8369 Board icon on the top, as shown in Figure above.

.. image:: https://wiki.analog.com/_media/resources/eval/ad8369_ace_boardicon.png
   :align: center
   :width: 200px

-  Double-click the chip on the ACE chip view on Figure above.

TEST SEQUENCE
-------------

-  Power up (enable DC power supply) the AD8369 EVALZ evaluation board.
-  Set the signal generator frequency to 70 MHz, and amplitude to -33 dBm. Enable RF output.

.. image:: https://wiki.analog.com/_media/resources/eval/ad8369_ace_chip.png
   :align: center

-  Select Gain Code to 15 on Label A as shown in Figure above.
-  Click Apply Changes on the top-left.
-  Check: The Voltage and Current on +5V Power. You should see ~34 mA
-  Check signal level in Spectrum analyzer. You should see ~0.3 dBm
