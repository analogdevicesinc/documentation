ADI AD-FMCADC2-EBZ Boards & Xilinx Reference Design
===================================================

|

.. warning::

   \ **NOTE:**

   | Support for the ad-fmcadc2-ebz was discontinued starting with 2022_R2 Kuiper Linux release and it is not supported in later releases. Last release in which pre-build files can be found is **2021_r2**. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases. The HDL project source code can still be found on :git-hdl:`hdl_2021_r2 <projects/fmcadc2>` release branch.


.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/fmcadc2/index.html\


Introduction
------------

The :doc:`AD-FMCADC2-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcadc2-ebz>` is a high speed data acquisition (1 ADC channel at 2500 MSPS), in an FMC form factor, which has one high speed JESD204B Analog to Digital converters (:adi:`AD9625`) on it. The AD9625 is a 12-bit monolithic sampling analog-to-digital converter (ADC) that operates at conversion rates of up to 2.5 giga samples per second (GSPS). This product is designed for sampling wide bandwidth analog signals up to the second Nyquist zone. The combination of wide input bandwidth, high sampling rate, and excellent linearity of the AD9625 is ideally suited for spectrum analyzers, data acquisition systems, and a wide assortment of military electronics applications, such as radar and jamming/antijamming measures.

The card is mechanically (width/depth, but not height) and electrically compliant to the FMC standard (ANSI/VITA 57.1).

The reference design includes the device data capture via the JESD204B serial interface and the SPI interface. The samples are written to the external DDR-DRAM. It allows programming the device and monitoring it's internal registers via SPI.

Supported Devices
-----------------

-  :adi:`AD-FMCADC2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCADC2-EBZ.html#eb-overview>`

Supported Carriers
------------------

-  `VC707 <https://www.xilinx.com/VC707>`__ HPC Slot
-  `ZC706 <https://www.xilinx.com/ZC706>`__ HPC Slot

Required Software
-----------------

-  We're upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
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

   
   -  AD-FMCADC2-EBZ Project - :git-no-OS:`fmcadc2`
   

