ADI AD-FMCADC4-EBZ Boards & Xilinx Reference Design (OBSOLETE)
==============================================================

Introduction
------------

.. important::

   Support for AD-FMCADC4-EBZ project on this website only for legacy purposes. The support for this project has been discontinued, latest tested release being 2018_r2.


The :adi:`AD-FMCADC4-EBZ <EVAL-AD-FMCADC4-EBZ>` is a high speed 4 channel data acquisition board featuring two :adi:`AD9680` dual channel ADC at 1000 MSPS and four ADA4961 :adi:`ADA4961` low distortion, 3.2 GHz, RF DGA driving each converter. The FMC form factor supports the JESD204B high speed serial interface. All clocking and channel synchronization is support on-board using the AD9528 :adi:`AD9528` clock generator. This board meets most of the FMC specifications in terms of mechanical size, mounting hole locations, and more. For that information, please refer to the FMC specification. Although this board does meet most of the FMC specifications, it is not meant as a `commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`__ (COTS) board. If a commercial, ready to go integrate product is required, please refer to one of the many FMC manufacturers. This board is targeted for the use of ADI reference designs that work with Xilinx development systems. ADI provides a complete source (HDL and software) to re-create these projects (minus the IP provided by the FPGA vendors).

The reference design includes the device data capture via the JESD204B serial interface and the SPI interface. The samples are written to the external DDR-DRAM. It allows programming the device and monitoring it's internal registers via SPI.

Supported Devices
-----------------

-  :adi:`AD-FMCADC4-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCADC4-EBZ.html#eb-overview>`

Supported Carriers
------------------

-  `ZC706 <https://www.xilinx.com/ZC706>`__ HPC Slot

Required Software
-----------------

-  We're upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <projects/scripts/adi_project.tcl#L10>`.
-  A UART terminal (Tera Term/Hyperterminal), baud rate 115200.

Downloads
---------

The HDL Reference Designs and the no-OS Software can be downloaded from the Analog Devices github.

HDL Source
----------

.. admonition:: Download
   :class: download

   
   -  ZC706 HDL Reference design: :git-hdl:`projects/fmcadc4/zc706`
   


No-OS Software Source
---------------------

.. admonition:: Download
   :class: download

   
   -  AD-FMCADC4-EBZ No-OS - :git-no-OS:`fmcadc4`
   

