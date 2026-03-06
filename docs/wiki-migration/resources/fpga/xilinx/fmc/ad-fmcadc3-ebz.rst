ADI AD-FMCADC3-EBZ Boards & Xilinx Reference Design
===================================================

Introduction
------------

The :adi:`AD-FMCADC3-EBZ <EVAL-AD-FMCADC3-EBZ>` is a high speed data acquisition board featuring :adi:`AD9625` single channel ADC at 2500 MSPS and the ADA4961 :adi:`ADA4961` Low Distortion, 3.2 GHz, RF DGA driving the converter. The FMC form factor supports the JESD204B high speed serial interface. This board meets most of the FMC specifications in terms of mechanical size, mounting hole locations, and more. For that information, please refer to the FMC specification. Although this board does meet most of the FMC specifications, it is not meant as a `commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`__ (COTS) board. If you want a commercial, ready to integrate product, please refer to one of the many FMC manufacturers. This board is targeted to use the ADI reference designs that work with Xilinx development systems. ADI provides complete source (HDL and software) to re-create those projects (minus the IP provided by the FPGA vendors, which we use), but may not provide enough info to port this to your custom platform.

The reference design includes the device data capture via the JESD204B serial interface and the SPI interface. The samples are written to the external DDR-DRAM. It allows programming the device and monitoring it's internal registers via SPI.

Supported Devices
-----------------

-  :adi:`AD-FMCADC3-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCADC3-EBZ.html#eb-overview>`

Supported Carriers
------------------

-  `VC707 <https://www.xilinx.com/VC707>`__ HPC Slot
-  `ZC706 <https://www.xilinx.com/ZC706>`__ HPC Slot

Required Software
-----------------

-  We upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
-  A UART terminal (Tera Term/Hyperterminal), baud rate 115200.

Downloads
---------

The HDL Reference Designs and the no-OS Software can be downloaded from the Analog Devices github.

HDL Source
----------

.. admonition:: Download
   :class: download

   
   -  ZC706 HDL Reference design: :git-hdl:`projects/fmcadc2/zc706`
   -  VC707 HDL Reference design: :git-hdl:`projects/fmcadc2/vc707`
   


No-OS Software Source
---------------------

.. admonition:: Download
   :class: download

   
   -  AD-FMCADC2-EBZ Main project- :git-no-OS:`fmcadc2`
   

