AD9139-DUAL-EBZ Evaluation Board Quick Start Guide
==================================================

Getting Started with the AD9139-DUAL-EBZ Evaluation Board and Software
----------------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  AD9139-DUAL-EBZ Evaluation Board
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5Vdc, Power Supply
-  2 Sinusoidal Clock Sources
-  Spectrum Analyzer
-  Data Pattern Generator Series 3 (DPG3)

Introduction
^^^^^^^^^^^^

The AD9139-DUAL-EBZ connects to a DPG3 for quick evaluation of the AD9139, a high-speed, signal processing Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9139-DUAL-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK, Frame, and DPG3 input clock. Also included is a quadrature modulator ADL5375 for quick DAC+IQMOD evaluation. Since AD9139 is a single channel converter, dual AD9139s are used on the board to work as I and Q, which typically applies to the case of wideband applications. Figure 2 is an image of the top side of the AD9139-DUAL-EBZ.

AD9139 DUAL Evaluation Software
-------------------------------

The AD9139 DUAL Evaluation Board software has an easy-to-use graphical user interface (GUI). It is included on the Evaluation Board CD, or can be downloaded from the DPG website at http://www.analog.com/dpg. This will install DPGDownloader (for generating and loading vectors into the DPG3) and AD9139 DUAL SPI software.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. One low phase noise high frequency clock source should be connected to the SMA connector, J1 (AD9516_CLKIN). The other low phase noise high frequency clock source should be connected to the SMA connector, J15 (LO_IN), and the spectrum analyzer should be connected to the SMA connector, J6. The evaluation board connects to the DPG3 through the connectors P1 and P2. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +--------------------------------------------------------+---------------------------------------+
   | |image3|                                               | |image4|                              |
   +--------------------------------------------------------+---------------------------------------+
   | Figure 1. Block diagram of the AD9139 lab bench set-up | Figure 2. Top view of AD9139-DUAL-EBZ |
   +--------------------------------------------------------+---------------------------------------+
   


Getting Started
---------------

The PC software comes on the included Evaluation Board CD, but may also be downloaded from the DPG Web site at http://www.analog.com/dpg. The installation will include the DPG Downloader software as well as all the necessary AD9139 files including schematic, board layout, datasheet, AD9139 DUAL SPI, and other files.

Initial Set-Up
~~~~~~~~~~~~~~

| 1. Install the DPG Downloader and AD9139 DUAL SPI software and support files on your PC. Follow the instructions in the installation wizard and use the default (recommended) installation settings.
| 2. Use a USB cable to connect the EVB to your PC and connect the lab equipment to the EVB.
| 3. Connect the DGP3 unit to your PC and turn on the unit.

Single-Tone Test
~~~~~~~~~~~~~~~~

| These settings configure the dual AD9139s to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the IQMOD output, under the condition: Fdata = 515MHz, 1X interpolation, IF = 71MHz, LO = 2000MHz, RF = 2071MHz.
| 1. To begin, open the AD9139 DUAL SPI application (Start > All Programs > Analog Devices > AD9139 > AD9139 DUAL SPI). The screen should look similar to Figure 3. Each AD9139 should be set respectively.
|

.. container:: center

   
   +-------------------------------------------------------+
   | |image5|                                              |
   +-------------------------------------------------------+

   | Figure 3 Entry Screen of the AD9139 DUAL SPI software |

   +-------------------------------------------------------+
   


| 2. Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1150MHz, and the output level to 6dBm. Set the frequency of the LO clock signal generator to 2000MHz, and the output level to 6dBm.The spectrum analyzer can be configured with Center Frequency = 2000 MHz, Span = 200 MHz, and Resolution Bandwidth of 30 kHz. Choose Input Attenuation to be 24dB. This can be adjusted later if indications are that the analyzer is causing degradations.
| 3. Follow the sequence below to configure the AD9139s/AD9516 SPI registers and DPG downloader.
| a. Click “Reset DAC” button on the “Quick Start” and “Quick Start2” tab.
| b. Set AD9516 as Figure 4 shows below before click “AD9516 Update” button.
|

.. container:: center

   
   +--------------------------+
   | |image6|                 |
   +--------------------------+

   | Figure 4 AD9516 settings |

   +--------------------------+
   


| c. Click “Restore Registers from File” and select the configuration file “AD9139Dual_1x_Sync.csv”. This will configure the registers of both AD9139s with correct values under the condition we are testing.
| d. There may be a few registers highlighted in red. The red highlights mean mismatches between the SPI read and write values in the software. Clicking “Read All Registers” reads back all the current values in the registers, which should resolve the highlights.
| e. Open DPG Downloader if you have not done so. (Start > All Programs > Analog Devices > DPG > DPGDownloader). Ensure that the program detects the AD9139-Dual, as indicated in the “Evaluation Board” drop-down list, and select it. For this evaluation board, LVDS is the only valid Port Configuration, and it will be selected automatically. The “DCO Frequency” window should show the correct data rate (575 MHz). The actual detected frequency may not be exactly 575 MHz but it should be stable and very close to it as shown in Figure 5.
|

.. container:: center

   
   +-------------------------------+
   | |image7|                      |
   +-------------------------------+

   | Figure 5 DPG Downloader Panel |

   +-------------------------------+

   | f. Click on “Add Generated Waveform”, and then “Single Tone”. As shown in Figure 6, A Single Tone panel will be added to the vector list. Enter the sample rate, in this case 575 MHz and the desired frequency, 71MHz. Enter the digital amplitude. In this case we use -14dBFS. Check the “Generate Complex Data (I & Q)” box and uncheck the “Unsigned Data” box. Select the In-Phase data vector in the “I Data Vector” drop down menu and the Quadrature data vector in the “Q Data Vector”.
|

.. container:: center

   
   +-----------------------------------------+
   | |image8|                                |
   +-----------------------------------------+

   | Figure 6 DPG Downloader sinewave vector |

   +-----------------------------------------+
   


| g. Click Download (|image9|) and Play (|image10|).
| h. The AD9139 DUAL SPI software should look like Figure 7 (for 1st AD9139) and Figure 8 (for 2nd AD9139) respectively.
|

.. container:: center

   
   +---------------------------------------------------+
   | |image11|                                         |
   +---------------------------------------------------+

   | Figure 7 Configured Quick Start Tab of 1st AD9139 |

   +---------------------------------------------------+
   


.. container:: center

   
   +---------------------------------------------------+
   | |image12|                                         |
   +---------------------------------------------------+

   | Figure 8 Configured Quick Start Tab of 2nd AD9139 |

   +---------------------------------------------------+

   | h. The Spectrum Analyzer should look like Figure 9.
|

.. container:: center

   
   +-------------------------------------------------+
   | |image13|                                       |
   +-------------------------------------------------+

   | Figure 9 AD9139 DUAL Eval Board output Spectrum |

   +-------------------------------------------------+
   


| 4. The current on the 5V supply should read about 1383mA.

SPI SOFTWARE
------------

| The AD9139 DUAL SPI software is conveniently organized in a series of tabs that groups registers according to their functions. In this way, all registers associated with the digital functions, for example, are on the “Digital Functions” tab. All registers associated with the PLL are on the “PLL” tab, and so on. Since there are dual AD9139s on the board, two sets of settings appear on the panel accordingly. For example, “Digital Functions2” tab is for 2nd AD9139 on the board. Normally the “Quick Start” tab is sufficient for a quick evaluation. The most frequently used register controls are included on this tab. A full description of each register and its settings is given in the AD9139 data sheet. Some of the registers and their functions are described here as they pertain to the AD9139 DUAL evaluation board. Please note that some of the screen images in this document may not match exactly with the latest revision of the software, due to ongoing improvements and enhancements to the software.
| The full screen layout is shown in Figure 3. The tabs can be seen across the top of the work area, and four function buttons in the menu area. “Save Registers to File” and “Restore Registers from File” allow the user to save the current register settings into a file for later uses. A register is immediately updated when the value in the control is changed. Switching between tabs does not update register values. “Read All Registers” can be used to monitor a resister with changing readback values. “ Record Sequence” allows the user to record a series of SPI writes in a particular order and to play back the sequence later. A short description of the register is shown in the status bar on the bottom of the work area when the mouse curser hovers over the control. Some of the tabs are discussed below.

Quick Start
~~~~~~~~~~~

The “Quick Start/Quick Start2” tab has selections that apply to the general configuration of the DAC. Reset DAC is recommended every time when the DAC is powered on or reset. Interpolation Rate allows the user to select among the 2 interpolation modes (1X and 2X). When sync is disabled, FIFO SPI Reset Request sets the FIFO with the requested value through a SPI command. The FIFO Level Read Back should reflect the actual FIFO level after the FIFO SPI Reset Request. Note loading/reloading a vector in the DPG Downloader may generate glitches on the DCI so it is also recommended to reload configuration file to dual AD9139. DCI Clk Div Ratio changes the divide ratio of the AD9516 input clock frequency over DCI frequency. In word mode, this ratio should be two times the interpolation rate. In byte mode, it should be the same as interpolation rate. For example, if the interpolation ratio is 1x, the DCI divide ratio should be 2x. The AD9516 registers in this SPI software are not immediately updated after a user changes the value in a control. AD9516 Update loads the changes in the AD9516 settings.

.. container:: center

   
   +-------------------------------------------+
   | |image14|                                 |
   +-------------------------------------------+

   | Figure 10 AD9139 DUAL SPI Quick Start tab |

   +-------------------------------------------+
   


PLL
~~~

| The “PLL/PLL2” tab includes all the PLL control registers. Both PLLs should be set respectively. The recommended settings for the best performance is PLL Charge Pump Current = 7 and PLL LOOP BW = 7. The user needs to follow the sequence below to enable the PLL. 1. Choose the desired divide ratios in the Loop Divider and the VCO Divider.
| 2. Set PLL Charge Pump Current and PLL Loop BW settings to 7.
| 3. Set the PLL Mode to Manual.
| 4. Turn on PLL Enable.
| 5. Set the PLL Mode to Auto.
|

.. container:: center

   
   +-----------------------------------+
   | |image15|                         |
   +-----------------------------------+

   | Figure 11 AD9139 DUAL SPI PLL Tab |

   +-----------------------------------+
   


EVB Jumper Configurations
-------------------------

| This evaluation board allows evaluation of both the DAC IF outputs as well as the modulator RF outputs. By default, the solder jumpers are configured to look at the modulator RF outputs. Below is a table listing the jumper configurations and SMA connector connections needed to view either output on a spectrum analyzer.
|

.. container:: center

   
   +-------------------+-------------------+------------------------------------------+
   | Output Viewed     | SMA Connector     | Jumper Configurations                    |
   +===================+===================+==========================================+
   | I DAC Output      | J3("DAC1 Output") | JP4 & JP5 Pins 1-2 (outer pads)          |
   +-------------------+-------------------+------------------------------------------+
   | Q DAC Output      | J4("DAC2 Output") | JP6 & JP7 Pins 1-2 (outer pads)          |
   +-------------------+-------------------+------------------------------------------+
   | ADL5375 RF Output | J6("MOD_OUT")     | JP4, JP5, JP6, JP7 Pins 2-3 (inner pads) |
   +-------------------+-------------------+------------------------------------------+
   


Note: When viewing the modulator output, a local oscillator (LO) must be connected to J15 (”LO_IN”) to properly modulate the signals.

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/AD9139-DUAL-EBZ?&v=RevB>`__ to receive all these great benefits and more!


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/AD9139_M5375_bench_setup.png
   :width: 473px
   :height: 324px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/AD9139_M5375_ebz_eval_top.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/AD9139_M5375_bench_setup.png
   :width: 473px
   :height: 324px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/AD9139_M5375_ebz_eval_top.png
   :width: 200px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/screen_of_AD9139_DUAL_SPI_software.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/screen_of_AD9139_DUAL_SPI_AD9516_settings.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139_dual_dpg_downloader_entry_screen.png
   :width: 650px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139_dpg_downloader_sinewave.png
   :width: 650px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/image009.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/image010.png
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139-dual_spi_software_entry_screen_work_dac1.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139-dual_spi_software_entry_screen_work_dac2.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139-dual_evb_mod_output.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139-dual_spi_software_entry_screen_work_dac1.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9139/ad9139_spi_software_pll.png
   :width: 600px
