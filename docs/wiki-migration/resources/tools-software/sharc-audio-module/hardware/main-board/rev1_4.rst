SHARC Audio Module(Revision 1.4)
================================

The :adi:`SHARC Audio Module <sharcaudiomodule>` uses the :adi:`ADSP-SC589 <sc58x>` :adi:`sharc` processor along with an :adi:`ADAU1761 <en/products/audio-video/audio-codecs/adau1761.html>` SigmaDSP audio codec and an :adi:`AD2425W <en/products/ad2425w.html>` :adi:`a2b` transceiver in a compact form for audio development.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-main-board-top-1_4.png
   :width: 600px

**The SHARC Audio Module Main Board**

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/main-board-diagram.png
   :width: 600px

**Block Diagram of the SHARC Audio Module Main Board**

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   SHARC Audio Module Main Board Rev 1.4 Design and Integration Files

   
   -  `Schematics <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/a0939-2016.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/A0939-2016_BOM.xlsx>`__
   -  `Fabrication and Assembly Files <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/a0939-2016_1p4.zip>`__
   -  `Design Package <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/ADZS-SC589-MINI Archive R1.4.zip>`__
   


ADSP-SC589 SHARC DSP
--------------------

The SHARC Audio Module is powered by the Analog Devices, Inc. :adi:`ADSP-SC589 <sc58x>` SHARC DSP. The ADSP-SC589 contains an ARM Cortex-A5 and Dual SHARC+ cores running at 450 MHz.

DDR3 2x 2Gb
-----------

There are two DDR3 channels on the SHARC Audio Module, each with a 2Gbit DDR3 module. In the default SHARC Audio Module configuration, one DDR3 module is used for Linux and the other used by the SHARC+ cores for audio processing.

512Mb SPI Flash
---------------

A 512Mbit SPI Flash on the SHARC Audio Module that is ready to be programmed with a users desired audio application.

10/100/1000 Ethernet
--------------------

The SHARC Audio Module has a 10/100/1000 Ethernet module to provide network and internet access to the board. The default IP address for this board, while running the official SHARC Audio Module Linux OS is 192.168.1.9.

USB Type A Host Port and USB MicroAB Host/Device/OTG Port
---------------------------------------------------------

The USB Type A port is Host mode only, and is for USB WiFi, Bluetooth and USB memory devices.

The USB MicroAB can be a Host/Device or OTG connection. This interface can be used for USB Audio, along with the USBi Emulator.

Expansion Port P4
-----------------

============== ====== ====== ===============
+12v           ``1``  ``2``  +12v
GND            ``3``  ``4``  GND
TWI1_SCL       ``5``  ``6``  PB_00
TWI1_SDA       ``7``  ``8``  PB_01
GND            ``9``  ``10`` PB_02
DAI0_PIN13     ``11`` ``12`` PB_03
DAI0_PIN14     ``13`` ``14`` GND
DAI0_PIN15     ``15`` ``16`` PB_04
GND            ``17`` ``18`` PB_05
DAI0_PIN16     ``19`` ``20`` PD_14
DAI0_PIN17     ``21`` ``22`` PD_15
DAI0_PIN18     ``23`` ``24`` GND
+3.3v          ``25`` ``26`` PE_00
GND            ``27`` ``28`` PE_01
HADC0_VIN0     ``29`` ``30`` PE_02
HADC0_VIN1     ``31`` ``32`` PE_03
GND            ``33`` ``34`` GND
HADC0_VIN2     ``35`` ``36`` PE_04
HADCO_VIN3     ``37`` ``38`` PE_05
GND            ``39`` ``40`` PE_06
HADC0_VIN4     ``41`` ``42`` PE_07
HADC0_VIN5     ``43`` ``44`` PE_08
GND            ``45`` ``46`` GND
HADC0_VIN6     ``47`` ``48`` PE_09
HADC0_VIN7     ``49`` ``50`` PE_10
GND            ``51`` ``52`` PE_11/SPI1_SEL3
PD_12/UART2_TX ``53`` ``54`` PE_12/SPI1_SEL4
PD_13/UART2_RX ``55`` ``56`` PE_13/SPI1_CLK
TWI2_SCL       ``57`` ``58`` PE_14/SPI1_MISO
TWI2_SDA       ``49`` ``60`` PE_15/SPI1_MOSI
PB_11          ``61`` ``62`` PB_13
PB_12          ``63`` ``64`` PB_14
============== ====== ====== ===============

Expansion Port P5
-----------------

=============== ====== ====== =============
DAI1_PIN01      ``1``  ``2``  DAI1_PIN11
DAI1_PIN02      ``3``  ``4``  DAI1_PIN12
DAI1_PIN03      ``5``  ``6``  DAI1_PIN13
GND             ``7``  ``8``  GND
DAI1_PIN04      ``9``  ``10`` DAI1_PIN14
DAI1_PIN05      ``11`` ``12`` DAI1_PIN15
DAI1_PIN06      ``13`` ``14`` DAI1_PIN16
GND             ``15`` ``16`` GND
DAI1_PIN07      ``17`` ``18`` DAI1_PINI17
DAI1_PIN08      ``19`` ``20`` DAI1_PIN18
DAI1_PIN09      ``21`` ``22`` DAI1_PIN19
DAI1_PIN10      ``23`` ``24`` DAI1_PIN20
GND             ``25`` ``26`` GND
PD_04           ``27`` ``28`` PD_06
PD_05           ``29`` ``30`` PD_07
PC_07/CAN0_RX   ``31`` ``32`` PB_09/CAN1_TX
PC_08/CAN0_TX   ``33`` ``34`` PB_10/CAN1_RX
PC_09/SPI0_CLK  ``35`` ``36`` PC_00
PC_10/SPI0_MISO ``37`` ``38`` PB_15
PC_11/SPI1_MOSI ``39`` ``40`` GND
PC_12/SPI1_SEL3 ``41`` ``42`` +3.3v
PG_00           ``43`` ``44`` PF_14
PG_01           ``45`` ``46`` PF_15
PG_02           ``47`` ``48`` PG_03
TWI0_SCL        ``49`` ``50`` PG_04
TWI0_SDA        ``51`` ``52`` PG_05
GND             ``53`` ``54`` GND
ADAU1761_RAUX   ``55`` ``56`` ADAU1761_RHP
GND             ``57`` ``58`` GND
ADAU1761_LAUX   ``49`` ``60`` ADAU1761_LHP
PD_08           ``61`` ``62`` PD_10
PD_09           ``63`` ``64`` PD_11
=============== ====== ====== =============

FTDI Header (P8)
----------------

This connector is compatible with most FTDI 3.3v UART to USB adapters.

===== ===============
``1`` GND
``2`` PD_00/UART0_CTS
``3`` N/C
``4`` PC_14/UART0_RX
``5`` PC_13/UART0_TX
``6`` PC_15/UART0_RTS
===== ===============

Automotive Audio Bus (A2B) Interface Duraclick (P6, P7)
-------------------------------------------------------

The A2B bus uses crossover cables to connect nodes to each other. ``P6`` connects to upstream towards the Master Node in the network and ``P7`` connects downstream to the next slave in the network. The SHARC Audio Module uses the :adi:`AD2425W <en/products/audio-video/automotive-audio-bus/ad2425w.html>` IC.

-  ``BLCK`` is connected to ``DAI0_PIN07``
-  ``SYNC`` is connected to ``DAI0_PIN08``
-  ``DTX0`` is connected to ``DAI0_PIN09``
-  ``DTX1`` is connected to ``DAI0_PIN10``
-  ``DRX0`` is connected to ``DAI0_PIN11``
-  ``DRX1`` is connected to ``DAI0_PIN12``

SigmaDSP ADAU1761 Audio Codec
-----------------------------

The :adi:`ADAU1761 <en/products/audio-video/audio-codecs/adau1761.html>` is a low power, stereo audio codec with integrated digital audio processing that supports stereo 48 kHz record and playback. The stereo audio ADCs and DACs support sample rates from 8 kHz to 96 kHz as well as a digital volume control.

The SigmaDSP® core features 28-bit processing (56-bit double precision). The processor allows system designers to compensate for the real-world limitations of microphones, speakers, amplifiers, and listening environments, resulting in a dramatic improvement in the perceived audio quality through equalization, multiband compression, limiting, and third-party branded algorithms.

The ADAU1761 is connected to the DAI ports on the ADSP-SC589 as follows:

-  ``DAC_SDATA`` is connected to ``DAI0_PIN01``
-  ``ADC_SDATA`` is connected to ``DAI0_PIN02``
-  ``BCLK`` is connected to ``DAI0_PIN03``
-  ``LRCLK`` is connected to ``DAI0_PIN04``

3.5mm Audio In/Out Jacks (J1, J2)
---------------------------------

The 3.5mm Audio In/Out jacks are connected to the ADAU1761 SigmaDSP.

The impedance of the 3.5mm signals is 16 ohms. The HP output pins to the expansion connectors are also 16 ohms.

SPDIF In/Out Jacks (J4, J5)
---------------------------

The SPDIF jacks are connected to the DAI ports on the ADSP-SC589.

-  SPDIF Input is connected to ``DAI0_PIN19``.
-  SPDIF Output is connected to ``DAI0_PIN20``.

USBi Connector (P2)
-------------------

The USBi Connector on the SHARC Audio module allows for the use of the USBi adapter for bare metal programming.

+12v Input Power Jack (P3)
--------------------------

The SHARC Audio Module was design for a 12V DC input, but can operated from 10v to 20v input to the barrel jack. A 12v 1.5A DC power supply is recommended. The barrel connector on the SHARC Audio Module can handle up to 3A current.

.. note::

   **The SHARC Audio Module is shipped with a US power supply. Here is a universal option:** https://www.digikey.com/products/en?keywords=102-3580-ND\


MicroSD Card Slot (J6)
----------------------

The MicroSD card slot on the SHARC Audio Module can be used to store the Linux OS as well as other data.

JTAG Interface (P1)
-------------------

The JTAG interface allows for programming and debugging of the ADSP-SC589 using an :adi:`ICE-1000 <ice1000>` or an :adi:`ICE-2000 <ice2000>` emulator and :adi:`CrossCore Embedded Studio <cces>`.

Boot Mode Jumper (JP1)
----------------------

The ADSP-SC589 has multiple boots modes. This jumper allows for three of the supported boot modes on the DSP, depending on jumper setting.

============== =============
Jumper on Pins Boot Mode
============== =============
1-2            ``SPI Boot``
2-3            ``UART Boot``
None           ``No Boot``
============== =============

.. important::

   **SHARC Audio Module revisions 1.4 or older incorrectly use link port boot rather than UART boot**\


Pushbuttons (PB1, PB2)
----------------------

Two GPIO pushbuttons are provided on the SHARC Audio Model. They are connected as follows:

-  ``PB1`` is connected to ``PF_00``
-  ``PB2`` is connected to ``PF_01``

Reset Button (RESET)
--------------------

The Reset button resets all the hardware on the SHARC Audio Module. It will not reset anything on connected to the expansion connectors.

GPIO LEDs (LED10, LED11, LED12)
-------------------------------

There are three GPIO controlled LEDs on the SHARC Audio Module. They are connected as follows:

-  ``LED10`` is connected to ``PD_01``
-  ``LED11`` is connected to ``PD_02``
-  ``LED12`` is connected to ``PD_03``

TWI Switch
----------

The SHARC Audio Module has a TWI switch the can connect TWI0 or TWI1 on the ADSP-SC589 to the A2B and ADAU1761 on the board. This allows either the ARM core or the SHARC+ cores to access the A2B and ADAU1761 TWI control lines. ``PB_08`` controls the switch.

===== ==========
PB_08 Connection
===== ==========
Low   ``TWI0``
High  ``TWI1``
===== ==========

--------------

`Hardware Reference#..|Hardware Reference#..audioproj-fin|Audio Project Fin <https://wiki.analog.com/_media/navigation SHARC Audio Module#..>`__
