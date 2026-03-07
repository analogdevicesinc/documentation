A2B Class-D Amplifier Module for SHARC Audio Module
===================================================

The :doc:`SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module>` A\ :sup:`2`\ B Class-D Amplifier Module is an :adi:`a2b` connected board that contains two Class-D :adi:`SSM3582 <en/products/audio-video/audio-amplifiers/class-d-audio-amplifiers/ssm3582.html>` amplifier ICs, providing 4 channels of audio output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/sam-class-d-top.png
   :width: 500px

**The A\ 2\ B Class-D Amplifier Module**

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/class-d-diagram.png
   :width: 500px

**Block Diagram of the A\ 2\ B Class-D Amplifier Module**

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   SHARC Audio Module A\ :sup:`2`\ B Class-D Amplifier Module Design and Integration Files

   
   -  `Schematics <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/a0974-2017.pdf>`_
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/a0974-2017_bom_hlm.xlsx>`_
   -  `Fabrication and Assembly Files <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/hardware/adzs-audioa2bamp_design_files.zip>`_
   


Automotive Audio Bus (A2B) Interface Duraclick (P4, P5)
-------------------------------------------------------

The A\ :sup:`2`\ B bus uses crossover cables to connect nodes to each other. ``P4`` connects to upstream towards the Master Node in the network and ``P5`` connects downstream to the next slave in the network.

The A\ :sup:`2`\ B Class-D Amplifier Module uses the :adi:`AD2428W <en/products/audio-video/automotive-audio-bus/ad2428w.html>` IC.

SSM3582 Class-D Amplifier
-------------------------

There are two ADI :adi:`SSM3582 <en/products/audio-video/audio-amplifiers/class-d-audio-amplifiers/ssm3582.html>` Class-D amplifiers on the A\ :sup:`2`\ B Class-D Amplifier Module. Each is two channels.

At 16V, the max power per channel is ~24w of power.

**P11 AMP1 Left Channel Output**

===== ========
``1`` Positive
``2`` Negative
===== ========

**P12 AMP1 Right Channel Output/MONO**

===== ========
``1`` Positive
``2`` Negative
===== ========

**P13 AMP2 Left Channel Output**

===== ========
``1`` Positive
``2`` Negative
===== ========

**P14 AMP2 Right Channel Output/MONO**

===== ========
``1`` Positive
``2`` Negative
===== ========

Populate ``JP6`` & ``JP7`` to configure AMP1 into MONO Output on ``P12``. Populate ``JP8`` & ``JP9`` to configure AMP2 into MONO Output on ``P14``.

USBi Connector for SigmaStudio (P1)
-----------------------------------

The USBi Connector on the :adi:`SHARC Audio Module <sharcaudiomodule>` allows for the use of the USBi adapter for :adi:`sigmastudio` and bare metal programming.

+12v Input Power Jack (P3)
--------------------------

The A\ :sup:`2`\ B Class-D Amplifier Module is designed to run off a 12v to 16v supply. A 12v 2A DC power supply is included in the kit. The barrel connector on the A\ :sup:`2`\ B Class-D Amplifier Module can handle up to 3A current.

.. note::

   **The Class-D Amplifier Module is shipped with a US power supply. Here is a universal option:** https://www.digikey.com/products/en?keywords=102-3580-ND\


Power Supply Input (P10)
------------------------

``P10`` is a power supply input jack to connect up to 16v @ 8A MAX. There is an 8A fuse on the Positive input of the P10 connector.

Pushbuttons (PB1, PB2)
----------------------

Two GPIO pushbuttons are provided on the A\ :sup:`2`\ B Class-D Amplifier Module. They are connected as follows:

-  ``PB1`` is connected to ``IO1`` on AD2428W
-  ``PB2`` is connected to ``IO2`` on AD2428W

GPIO LEDs (LED1, LED2)
----------------------

There are two GPIO-controlled LEDs on the A\ :sup:`2`\ B Class-D Amplifier Module. They are connected as follows:

-  ``LED1`` is connected to IO0 on the ``AD2428W``
-  ``LED2`` is connected to IO7 on the ``AD2428W``

PDM/TDM Connectors
------------------

**JP5 PDM MIC**

==== ===== ===== ===
3.3v ``1`` ``2`` GND
DRX0 ``3`` ``4`` GND
DRX1 ``5`` ``6`` GND
BLCK ``7`` ``8`` GND
==== ===== ===== ===

\*\* P2 Buffered TDM Signals \*\*

======= ====== ====== ===
B_DTX0  ``1``  ``2``  GND
B_DTX1  ``3``  ``4``  GND
B_DRX0  ``5``  ``6``  GND
B_DRX1  ``7``  ``8``  GND
B_FSYNC ``9``  ``10`` GND
B_BLCK  ``11`` ``12`` GND
======= ====== ====== ===

\*\* P15 Unbuffered TDM Signals \*\*

===== ====== ====== ===
DTX0  ``1``  ``2``  GND
DTX1  ``3``  ``4``  GND
DRX0  ``5``  ``6``  GND
DRX1  ``7``  ``8``  GND
FSYNC ``9``  ``10`` GND
BLCK  ``11`` ``12`` GND
===== ====== ====== ===

EEPROM
------

The A\ :sup:`2`\ B Class-D Amplifier Module has a TWI 256k EEPROM for configuration data. The EEPROM used is the `24FC256I/MS <http://www.microchip.com/wwwproducts/en/24FC256>`_.

--------------

`Audio Project Fin#..hardware|Hardware Reference#..faust|Faust and the SHARC Audio Module <https://wiki.analog.com/_media/navigation SHARC Audio Module#.audioproj-fin>`_
