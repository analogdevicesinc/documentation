Evaluating the AD8283 and AD8285 Evaluation Boards
==================================================

Introduction
============

The AD8283CP-EBZ and AD8285CP-EBZ are designed to aid in the evaluation of AD8283 and AD8285 radar receive path ICs. The boards connects to the high speed ADC FIFO evaluation board for ready data capture. They also provides flexible options for clock settings, voltage references, and provides easy interfaces for input signals. The AD8283 or AD8285 datasheets should be consulted when using the evaluation board.

Features
========

-  SPI interface for setup and control
-  On-board clock driver for optional external clock inputs
-  On-board optional external voltage reference

Helpful Documents
=================

-  :adi:`AD8283` or :adi:`AD8285` data sheet
-  :adi:`HSC-ADC-EVALC <media/en/technical-documentation/data-sheets/HSC-ADC-EVALB.pdf>`, *High Speed ADC FIFO Evaluation kit C*
-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AD8283 and AD8285 Evaluation Board Page <EVAL-AD8283>`, *Schematic, Layout and Configuration Files, see Software section*

Equipment Needed
================

-  (2) 6.0V, 2.0A switching power source, provided
-  PC running Windows
-  USB 2.0 port
-  AD8283CP-EBZ or AD8285CP-EBZ board
-  HSC-ADC-EVALCZ FPGA-based data capture kit

Getting Started
===============

This section provides quick start procedures for using the AD8283CP-EBZ, or AD8285CP-EBZ board.

Jumper Configurations
---------------------

Set the jumper settings/link options on the evaluation board for the required operating modes before powering on the board. The functions of the jumpers are described in Table 1. Figure 1 shows the default jumper settings.

+--------+----------------------------------------------------------------------------------------+
| Jumper | Description                                                                            |
+========+========================================================================================+
| P302   | PWDN. Short jumper to power down the device                                            |
+--------+----------------------------------------------------------------------------------------+
| P303   | MUXA. Short jumper to force multiplexer to Channel A                                   |
|        | Note: Activating MUXA will render the FIFO unable to acquire data                      |
+--------+----------------------------------------------------------------------------------------+
| P304   | AUX. Short jumper to force multiplexer to AUX channels (INADC+ and INADC-)             |
+--------+----------------------------------------------------------------------------------------+
| P305   | ZSEL. Short jumper to force input impedance to 200kohm                                 |
+--------+----------------------------------------------------------------------------------------+
| J403   | Tristate control for the on board oscillator                                           |
|        | Place in position 1 to disable the oscillator                                          |
|        | Place in position 2 to enable the oscillator                                           |
+--------+----------------------------------------------------------------------------------------+
| J601   | SPI lines. All jumpers must be shorted to enable connection to the data capture board. |
+--------+----------------------------------------------------------------------------------------+

|image1|

.. container:: centeralign

   \ *Figure 1. Evaluation Board with Default Jumper Settings*\


Configuring the Board
---------------------

Before using the software for testing, configure the evaluation board as follows:

1. Connect the evaluation board to the data capture board, as shown in Figure 2.


|image2|

.. container:: centeralign

   \ *Figure 2. Interfacing the evaluation board to the data capture board*\


| 2. Connect one 6V, 2A switching power supply to the evaluation board, and another 6V, 2A switching power supply to the data capture board. Power up both boards.
| 3. Connect the data capture board to the PC using a USB cable. Make sure that all the jumpers on J601 are connected.
| 4. Open VisualAnalog on the connected PC. The board should automatically be detected. Configure the board as instructed in AN-905. Select the preferred template to begin.

|image3|

.. container:: centeralign

   \ *Figure 3. VisualAnalog Startup Window*\


Click Yes when the dialog box below appears to configure the part.



|image4|

.. container:: centeralign

   \ *Figure 4. VisualAnalog Program Configuration*\


5. After properly configuring the VisualAnalog software, open SPI controller. Configure the software as in AN-878 by loading the appropriate Cfg and Cal files. Click the Read button on the CHIP ID(1) box to check whether the correct configuration files have been loaded.



|image5|

.. container:: centeralign

   \ *Figure 5. SPI Controller Configuration*\


Configure the part registers on the ADCBase0 tab. Individual registers may also be written or read to on the Eng 0 tab.



|image6|

.. container:: centeralign

   \ *Figure 6. ADCBase0 Tab on SPI Controller*\


6. When the registers have been properly configured, click Update on VisualAnalog to run the canvas.



|image7|

.. container:: centeralign

   \ *Figure 7. Updating the VisualAnalog Canvas*\


Evaluation Board Circuitry
--------------------------

Power
~~~~~

The AD8283 and AD8285 require 3.3V and 1.8V supplies for both analog (AVDD) and digital (DVDD) power. The evaluation boards have on-board regulators, specifically the ADP3339, to supply this power. U705 and U706 provide the 3.3V digital and analog supply, respectively. U707 and U704, on the other hand, provide the 1.8V digital and analog supply.

Input Signals
~~~~~~~~~~~~~

Each input is configured with SMA ports and terminated with 50ohms for easy interfacing to source equipment. Each input is connected with a diode array for overcurrent protection. The inputs are AC-coupled to the AD8283/5. Use P10x to connect any of the positive input pins to ground. Use P11x to short any of the negative inputs to ground. Use P12x to short any two differential lines together.

Output Signals
~~~~~~~~~~~~~~

The AD8283CP-EBZ and AD8285CP-EBZ use the Analog Devices high speed converter evaluation platform (HSC-ADC-EVALCZ) for capturing data. The digital outputs D0 to D11 are directly mapped to connector P702. For more information on the data capture board and its settings, visit www.analog.com/hsadcevalboard.

Clock
~~~~~

The AD8283CP-EBZ and AD8285CP-EBZ have default 72MHz oscillators on-board. This clock signal is coupled via a transformer to the CLK+ and CLK- pins of the AD8283/5. This oscillator can be controlled using J403. Placing the jumper at position 1 disables the oscillator, while placing it in position 2 enables the oscillator.

The clock may also be driven externally through the SMA connectors J401 and J402. J403 should be placed in position 2 to disable the onboard oscillator.

It is recommended that then AD8283/5 be driven with a clock source that has low jitter and low phase noise. The board is configured with the AD9515 clock distribution IC, which may be used to improve the jitter and phase noise performance of the clock. To use the AD9515, connect 0ohm resistors to R406 and R407 and remove resistors R415 and R416. Capacitors with a value of 0.1uF should also be connected to C405 and C406. The part is hardware programmable through resistors R424 to R445. The AD9515 LVPECL output is mapped directly to the CLK+ and CLK- pins of the AD8283/5.

Reference
~~~~~~~~~

The AD8283/5 may be configured to derive its reference voltage internally or externally. The board comes installed with the ADR130, which is configured to provide a 1V reference. A 0ohm resistor must be connected at R311 in order to use this reference. Make sure internal register 0x18 is configured appropriately before applying the external reference.

RBias
~~~~~

Rbias has a default 10kohm resistor installed to ground and is used to set the ADC core bias current. Note that using a resistor with a value other than 10kohm, 1% may degrade the performance of the device.

How to Use the Software for Testing
===================================

Setting Up an FFT
-----------------

In order to obtain an FFT plot, follow steps 1 to 5 on the Getting Started section, choosing the FFT canvas on the VisualAnalog window. The part and the data capture board must then be configured for proper operation, as detailed in the sections below.

Enabling the Active Input Channels Using SPI Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Register 0x0C on the SPI controller, depending on the number of channels to be enabled. The correct register settings can be found in the Register Map section of the AD8283/5 datasheet.

To do this, on the Eng0 tab of the SPI controller, enter the address in the appropriate field, then enter the data to be written to the register. These values can be written in binary, hex, or decimal notations. In the figure below, writing 1010b or 0x0A to the register indicates that all channels are active.

Click Write.

.. image:: https://wiki.analog.com/_media/ad8283/writetoreg0cedit.png
   :align: center
   :width: 200px

Configuring the Sample Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample rate of the data capture board must be configured to run at the effective sample rate of the part for proper operation. Note that the effective sample rate is given by

.. image:: https://wiki.analog.com/_media/ad8283/sr_equation.png
   :align: center
   :width: 200px

To do this, on the VisualAnalog canvas, click on the Settings button of the ADC Data Capture Block.

.. image:: https://wiki.analog.com/_media/ad8283/datacapturesettings.png
   :align: center
   :width: 200px

Enter the effective sample rate in the Clock Frequency option. The figure below shows the settings for the AD8283 with all 6 channels active.

.. image:: https://wiki.analog.com/_media/ad8283/samplerate12.png
   :align: center
   :width: 400px

Adding or Removing Output Data Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add channels from the data capture board, choose the desired channel by selecting it from the drop-down list as shown in the Figure below.

.. image:: https://wiki.analog.com/_media/ad8283/dropdownchannelsadd.png
   :align: center
   :width: 400px

After selecting the data, click Add. It should now show up on the Output Data Box.

.. image:: https://wiki.analog.com/_media/ad8283/channeladded.png
   :align: center
   :width: 400px

To remove a channel, click the channel, and click Remove.

.. image:: https://wiki.analog.com/_media/ad8283/removechannels.png
   :align: center
   :width: 400px

Running the FFT
---------------

| Once all registers and settings have been configured, the FFT can now be run.
| 1. Connect a signal source to the SMA inputs of the evaluation board.
| 2. Click update on the VisualAnalog window.
| |image8|

.. |image1| image:: https://wiki.analog.com/_media/ad8283/ad8283_eval_bd_z_1_of_1_edlow.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/ad8283/ad8283-hsc-adc_1_of_1_edlow.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/ad8283/vanalog_startup.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/ad8283/vanalog_program8283.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/ad8283/spicontroller_chipid_zoom.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/ad8283/spicontroller_adcbase_zoom.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/ad8283/vanalog_play.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/ad8283/chana_40mhz_100mvpp_reg0cdat00h.png
