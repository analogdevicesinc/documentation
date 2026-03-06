Calibration Board
=================

Splitter/Combiner, Calibration, Power Analyzer
----------------------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/adquadmxfe-calangle-web.gif
   :align: center

Features
--------

-  Mates to Quad-MxFE Digitizing Card & VCU118 PMOD Interface (Cable Included)
-  MATLAB Control Enables System-Level Calibration Algorithm Development
-  Provides Both Individual Adjacent Channel Loopback and Combined Channel Loopback Options
-  Combined Tx Channels Out Via SMA Option
-  Combined Rx Channels In Via SMA Option
-  On-Board Log Power Detectors With AD5592R Output To VCU118 Over PMOD
-  On-Board Power Regulation from Single 12V Power Adapter (Included)

Below is the full integrated system including the Xilinx `VCU118 <https://www.xilinx.com/VCU118>`__, ADQUADMXFE1EBZ, and :doc:`ADQUADMXFE-CAL </wiki-migration/resources/eval/user-guides/quadmxfe/calboard>` in full operation. For LED identification please see :doc:`Calibration Broad LED Information </wiki-migration/resources/eval/user-guides/quadmxfe/calboard>`, or `Quad MxFE LED Information <https://wiki.analog.com/resources/eval/user-guides/quadmxfe/>`__


|image1|

--------------

General Description
-------------------

This page serves to inform system engineers and software developers about the calibration board addition kit that pairs with the :adi:`Quad-MxFE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`. This board directly aligns with the 16 Rx and 16 Tx ports on the output of the Quad MxFE and includes power detectors and loopback configurations for the system-level calibration of the Quad MxFE. The board contains a PMOD 2A interface that connects the `VCU118 <https://www.xilinx.com/VCU118>`__ Evaluation Board from Xilinx®. A DIP switch and multi-channel ADC/DAC,\ :adi:`AD5592R`, are also included for additional control and power readings. The goal of this kit is to enable users to demonstrate combined-channel dynamic range, spurious, and phase noise improvements, develop system-level calibration algorithms, and demonstrate immediate phase determinism.

High Level Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/blckdiagram_edit.png
   :align: center
   :width: 600px

Key Component Location
~~~~~~~~~~~~~~~~~~~~~~

|image2| |image3|

LED Identification
~~~~~~~~~~~~~~~~~~

+-----------------------+


| LED Status Indicators |

+=======================+

| LED Ref Des           |

+-----------------------+

| DS601                 |

+-----------------------+

| DS602                 |

+-----------------------+

| DS603                 |

+-----------------------+

Equipment Needed
----------------

-  PMOD Cable

   -  `Cable Assembly <https://www.samtec.com/products/idsd-06-d-15.00>`__

-  12V (150W) Wall Supply

   -  `Power Brick Assembly <https://www.digikey.com/TE150A1251F01>`__

-  2x SMA Cables (50 Ω)
-  MMCX to SMA cables
-  MMCX to MMCX cables

   -  `Cable Assembly <https://www.samtec.com/products/rf316-03sp1-03sp1-0100>`__

-  Board Standoffs

   -  `Standoff Assembly <https://www.mcmaster.com/catalog/127/3467/>`__

-  Static Shielding Bag
-  Packaging (Box, Foam)
-  Startup Documentation
-  VCU118 FPGA Board (optional)

   -  `VCU118 <https://www.xilinx.com/VCU118>`__

-  Quad MxFE Board (optional)

   -  :adi:`Quad MxFE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`

--------------

Control Interfaces
------------------

The calibration board can be controlled in multiple ways including a DIP Switch and 2A PMOD Interface. The board can be controlled with 4 main signals: 5045 V1 and 5045 V2 which control an ADRF5045 which switches the transmit path between combined loopback, low frequency path, high frequency path, and power detection path, CTLR IND which turns off and on adjacent individual loopback for each Rx and Tx channel, and CTRL RX COMB which turns off and on the combined receive loopback path. The DIP Switch controls 4 signals: 5045 V1, 5045 V2, CTRL IND, and CTRL RX COMB. The PMOD Interface has 8 signals: 5045 V1, 5045 V2, CTRL IND, CTRL RX COMB, and 4 SPI Communications signals. The AD5592R is an 8 channel GPIO/ADC/DAC and it is connected the same control signals as the DIP switch as well as the three power detectors (:adi:`AD8318 </en/products/ad8318.html>`, :adi:`HMC948 </en/products/hmc948.html>`, :adi:`LTC5596 </en/products/ltc5596.html>`), plus a temperature sensor on the AD8318. Below is a tabular representation of these control signals.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/capture.png
   :width: 400px

Software Needed
---------------

The following link contains the MATLAB driver for controlling the 16 Tx / 16 Rx Calibration board via the VCU118 PMOD interface. The driver may be used to configure the Quad MxFE platform in a Combined Loopback, Individual Loopback, Combined Tx to SMA, Combined Rx from SMA, Combined Tx Power reading, and Power readings from the :adi:`AD5592R </en/products/ad5592r.html>` and subsequent (:adi:`AD8318 </en/products/ad8318.html>`, :adi:`HMC948 </en/products/hmc948.html>`, :adi:`LTC5596 </en/products/ltc5596.html>`).

-  :doc:`Cal Board VCU118 PMOD </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`

Related Documents
-----------------

Related Parts Pages
~~~~~~~~~~~~~~~~~~~

-  :adi:`ad5592r` 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip Reference, SPI interface
-  :adi:`hmc948` 54 dB Logarithmic Detector SMT, 1 - 23 GHz
-  :adi:`LTM5596 <ltc5596>` 100MHz to 40GHz Linear-in-dB RMS Power Detector with 35dB Dynamic Range
-  :adi:`ad8318` 1 MHz TO 8 GHz, 70 dB Logarithmic Detector/Controller
-  :adi:`adp5020` Power Management Unit for Imaging Modules
-  :adi:`ad5045` Fully Accurate 14-Bit VOUT nanoDAC® SPI Interface 4.5 V to 5.5 V in a TSSOP

Schematic
~~~~~~~~~

-  `ADQUADMXFE-CAL <https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/02-064888-01-b_2_.pdf>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadfull_edit.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/cal_brd_labels.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/quadmxfe/cal_brd_labels2.png
