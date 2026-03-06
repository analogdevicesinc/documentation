Evaluating the MAX14815 Octal 5-level Pulser with T/R Switch and Embedded Beamforming
=====================================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire output waveforms from :adi:`MAX14815EVKIT# <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max14815evkit.html>` to characterize :adi:`MAX14815 <en/products/max14815.html>` octal 5-level pulser with T/R switch and embedded beamforming. An example sequence is detailed step by step in the Quickstart Guide section.

Typical Setup
-------------

.. container:: centeralign

   \ |image1|\ *Figure 1. MAX14815 evaluation setup*\


.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


Helpful Files
-------------

-  MAX14815 Datasheet
-  `MAX14815 EV Kit PDF User Guide <https://wiki.analog.com/_media/resources/eval/max14815evkit.pdf>`__

Software Files and Installation Procedure
-----------------------------------------

-  Download then run `SetupMAX14815_EvKit_1.0.0.0.exe <https://confluence.analog.com/download/attachments/722382012/SetupMAX14815_EvKit_1.0.0.0.exe?version=1&modificationDate=1681475589240&api=v2>`__.

.. container:: centeralign

   \ |image2|\ *Figure 2. Software License Agreement page*\


-  Review then accept the License Agreement. Click **Next**.

.. container:: centeralign

   \ |image3|\ *Figure 3. Software installation directory selection window*\


-  Setup the directory where the software will be installed. Click **Next**.

.. container:: centeralign

   \ |image4|\ *Figure 4. Shortcut installation directory selection window*\


-  Choose the directory where the software shortcut will be installed. Click **Next**.
-  In the following page, click **Install**.

.. container:: centeralign

   \ |image5|\ *Figure 5. Installation completion window*\


-  When the installation is finished, do either of the following:

   -  Connect the evaluation board to PC via USB cable. Tick the Launch MAX14815 EvKit checkbox to open the software right after clicking the Finish button.
   -  Leave Launch MAX14815 EvKit checkbox unchecked then click Finish. Connect the evaluation board to PC via USB cable then re-launch the software by double-clicking the shortcut icon or the application file in the directory where the software was installed.

Hardware Needed
---------------

-  MAX14815EVKIT# which includes

   -  MAX14815 evaluation board
   -  USB cable (type A male to type B male)
   -  3.5mm scope probe jacks for high-voltage outputs

-  Pattern generator to drive INNx, INPx control signals (optional)
-  +5V DC, 1A power supply for VCC_EXT
-  -5V DC, 100mA power supply for VEE_EXT (optional if the on-board LDO is used)
-  +3.3V DC, 100mA power supply for VIO_EXT (optional if the on-board LDO for is used)
-  +5V to +100V DC, 30mA (+100V) to 600mA (+5V) power supply for VPPA_VPPB
-  -5V to -100V DC, -30mA (-100V) to -600mA (-5V) power supply VNNA_VNNB
-  Optional for 5 levels configuration:

   -  Additional +5V to +100V DC, 30mA (+100V) to 600mA (+5V) power supply
   -  Additional -5V to -100V DC, -30mA (-100V) to -600mA (-5V) power supply

-  Oscilloscope
-  Windows XP®/7/8.1/10 PC

Quick Start Guide
-----------------

-  Mount scope probe jacks to HVOUTx connector footprints on the evaluation board.
-  Configure jumpers on the evaluation board such that on-board LDOs are used for VEE_EXT, VIO_EXT, on-board USB-to-SPI converter and the on-board clock generator. Check that the jumper shunt positions are as listed below. Connect a +5V DC, 1A power supply output across VCC_EXT and GND test pins. Enable the power supply.

   -  VCC_REG: 1-2
   -  VEE_SEL: 2-3
   -  VIO_SEL: 2-3
   -  JU21: 1-2

.. container:: centeralign

   \ |image6|\ *Figure 6. EV Kit software showing "Hardware Connected" status*\


-  Connect the evaluation board to PC with the USB cable. Launch the EV kit software by double-clicking the shortcut icon or the application file in the directory where it was installed. The board will automatically be recognized by the software and at the lower right portion of the window, **"MAX14815 EV Kit Hardware Connected"** should be indicated. Otherwise, from the **Device** menu, select **Connect Hardware**. Verify that the status bar indicates the EV Kit hardware is **Connected**. Refer to Figure 6.
-  On the evaluation board, to produce five-level outputs, remove the shunts from VPPA-VPPB and VNNA-VNNB jumpers. Connect the following power supplies to the corresponding test pins as listed below. If only 3-level outputs are desired, keep the shunts on the jumpers and connect power supplies either to VPPA, GND, VNNA, GND test pins only or to VPPB, GND, VNNB, GND pins only. Enable the power supplies.

   -  +10V DC 250mA across VPPA and GND
   -  -10V DC 250mA across VNNA and GND
   -  +5V DC 500mA across VPPB and GND
   -  -5V DC 500mA across VNNB and GND

-  On the EV kit GUI, prepare to output a pattern by following the sequence below:

   -  Press Reset RAMs button to clear the Pulse Wave Table, Line Number Table, and Line Type Table.
   -  Press Reset Registers button to the content of any registers and possible errors.
   -  Press the Initialize button to pre-fill the configuration tab with default values. All Channel Enable and Channel TX Enable checkboxes will be enabled. Checkboxes for CH2 to CH8 can be unchecked.

-  To output a pattern, follow the steps below:

   -  Go to Pulse Wave Tables tab then copy the pattern shown in Figure 7 for CH1. Press the Write button then the Read button.
   -  Enable the on-board high-speed clock by ticking the Power-On checkbox in the Clock/Trigger Control panel.
   -  Finally, tick the Trigger checkbox. The pulser will then output the programmed pattern at the desired frequency and pulse repetition frequency (PRF). Figure 8 shows the captured waveform corresponding to the programmed pattern in Figure 7.

-  To stop the pattern, deselect the Trigger checkbox.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/max14815_setup_with_labels.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/max14815_software_setup_license.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/max14815_software_setup_installation_directory.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/max14815_software_setup_shortcut_directory.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/max14815_software_setup_finish.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/max14815_sw_hardware_connected.png
   :width: 600px
