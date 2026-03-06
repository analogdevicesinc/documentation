AD9144-EBZ Evaluation Board Quick Start Guide Using ACE (Analysis \| Control \| Evaluate) Software
==================================================================================================

Getting Started with the AD9144-EBZ Evaluation Board and Software
-----------------------------------------------------------------

What's in the Box
~~~~~~~~~~~~~~~~~

-  :adi:`AD9144-EBZ` Evaluation Board
-  Evaluation Board CD
-  Mini-USB Cable

Recommended Equipment List
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  +5Vdc, Power Supply
-  Sinusoidal Clock Sources
-  Spectrum Analyzer
-  Data Pattern Generator Series 3 (DPG3)

Introduction
------------

The AD9144-EBZ connects to a DPG3 for quick evaluation of the :adi:`AD9144`, a high-speed, signal processing Digital to Analog Converter. The DPG3 automatically formats the data and sends it to the AD9144-EBZ, simplifying evaluation of the device. The Evaluation Board (EVB) runs from a +5V supply. A clock distribution chip AD9516 is included on this EVB as a clock fan-out and frequency divider for the DACCLK, REFCLK and DPG3 input clock. Figure 2 is an image of the top side of the AD9144-EBZ.

AD9144 Evaluation Software
--------------------------

The AD9144 Evaluation Board software runs on the easy-to-use ACE (Analysis|Control|Evaluate) graphical user interface (GUI). It is included on the Evaluation Board CD. Registers on the AD9144 and AD9516 products are programmed via a USB cable connecting the user’s PC to the AD9144-EBZ XP2 connector. Software in the AD9144-EBZ PIC processor (XU1) provides the interface between the USB bus and the SPI busses of the AD9144 and AD9516.

Hardware Setup
--------------

Connect +5.0V to P5, GND to P6. A low phase noise high frequency clock source should be connected to the SMA connector, J1. This is the DACCLK input. The spectrum analyzer should be connected to the SMA connector, J4. A +1.0V power supply must be connected to the VTT probe point near SMA connector J9, along with a GND connection to the GND probe point next to it. The evaluation board connects to the DPG3 through the connectors P4. The PC should be connected to the EVB using the mini-USB connector XP2 after installation of the Evaluation Board software. Figure 1 shows the block diagram of the set-up.

.. container:: center

   
   +--------------------------------------------------------+----------------------------------+
   | |image3|                                               | |image4|                         |
   +--------------------------------------------------------+----------------------------------+
   | Figure 1. Block diagram of the AD9144 lab bench set-up | Figure 2. Top view of AD9144-EBZ |
   +--------------------------------------------------------+----------------------------------+
   


Single-Tone Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~

| These settings configure the AD9144 to output a sine wave using the DPG3 and allow the user to view the single-tone performance at the DAC output, under the condition: Fdata = 750MHz, 2X interpolation, IF = 112MHz.
| === Single Tone Demo Lab Bench Configuration Procedure:=== These settings configure the AD9144 to output a 112MHz -1dbFS sine wave using the DPG3 on all four AD9144 DACs.

- Configure the hardware according to the hardware set-up instructions given in the Hardware Setup section above. Set the frequency of the DAC clock signal generator to 1500MHz, and the output level to 3dBm. The spectrum analyzer can be configured as shown in Figure 8 with a resolution bandwidth of 100kHz. Choose an Input Attenuation of 24dB.

| - On your lab computer, open the ACE application (Start > All Programs > Analog Devices > ACE). You will see the GUI shown in Figure 5 come up.

Single Tone Demo Hardware and Software Start Up Procedure:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. Open DPG Downloader. It will say AD9144 as shown in Figure 3
|

.. container:: center


|image5|

   +----------------------------------------+

   | Figure 3. Initial DPG Downloader Panel |

   +----------------------------------------+

   | 2. To load the proper panel, select the Port Configuration option for "QBF 1x8 85G 425M" for single link (for dual link cases choose "QBF 2x4 85G 425M"). Select the JESD Mode drop-down to Mode 0 and Subclass to 0. Create a single-tone vector with a Data Rate of 750MHz, Desired Frequency of 112MHz, Amplitude of -1dBFS, uncheck the Unsigned Data checkbox and check the Generate Complex I & Q Data box. Select the I and Q vectors for each of the 4 DAC vector input options, as shown in Figure 4.
|

.. container:: center


|image6|

   +-----------------------------------------+

   | Figure 4. Configured DPG Downloader GUI |

   +-----------------------------------------+

   |


3. Open ACE. It should recognize the AD9144-EBZ in the attached hardware section when the application startup screen displays, as shown in Figure 5. Double-click on the AD9144-EBZ icon to navigate to the board view.
|

.. container:: center


|image7|

   +-------------------------------------------------------------+

   | Figure 5. Initial ACE Startup Window with Attached Hardware |

   +-------------------------------------------------------------+

   |


4. In the Setup Wizard, select single link, JESD Mode 0, Interpolation 2 and FDAC 1.5GHz, as shown in Figure 6. Hit "Apply" and the wizard will execute a startup routine to configure the AD9516 and AD9144. // // Once complete, the SERDES PLL lock indicator on the board will turn green if it locked and the display will look like Figure 7.
|

.. container:: center


|image8|

   +-------------------------------------+

   | Figure 6. Configured ACE Wizard GUI |

   +-------------------------------------+
   


.. container:: center

   


|image9|

   +-----------------------------------------------------+

   | Figure 7. ACE Wizard Executed and SERDES PLL Locked |

   +-----------------------------------------------------+
   


| 5. Return to DPGDownloader and note the Serial Line Rate readback should read 7.5Gbps indicating that the clocks going to the FPGA are configured properly for this setup. 6. Click Download (|9154_down_arrow.png|) and Play (|9154_right_green_arrow.png|). The 'Sync Status' checkmark should turn green indicating that the SYNCOUTb level is high and the link is up, as shown in Figure 7. The spectrum in Figure 8 will appear on all 4 DAC outputs (J17, J4, J5, and J14).
|

.. container:: center


|image10|

   +---------------------------------------+

   | Figure 7. Executed DPG Downloader GUI |

   +---------------------------------------+
   


8. Figure 8 shows what you will see at the output of the DACs on the Spectrum Analyzer.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_8_ad9144_fmc_ebz_spectrum_capture_1.png

+------------------------------------------------+


| Figure 8. DAC Output Spectrum Analyzer Display |

+------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_1.png
   :width: 440px
   :height: 260px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144_ebz_photo.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/figure_1.png
   :width: 440px
   :height: 260px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/ad9144_ebz_photo.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_DPGStartup.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_DPGSetup.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_ACEStartup.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_ACESetup.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_ACEWizRan.png
   :width: 900px
.. |9154_down_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_down_arrow.png
.. |9154_right_green_arrow.png| image:: https://wiki.analog.com/_media/resources/eval/dpg/9154_right_green_arrow.png
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9144/AD9144-EBZ_DPGDwnld.png
   :width: 900px
