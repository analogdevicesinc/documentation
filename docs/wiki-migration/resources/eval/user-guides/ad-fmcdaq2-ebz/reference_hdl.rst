AD-FMCDAQ2-EBZ HDL Reference Design
===================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/daq2/index.html\


Functional Overview
-------------------

The reference design is a processor based (ARM or Microblaze/Nios2) embedded system. A functional block diagram of the system is given below for both Xilinx and Altera FPGAs. The device interfaces are shared by the same set of transceivers followed by the individual JESD204B and ADC/DAC pcores. The cores are programmable through an AXI-lite interface. The data path consists of independent DMA interfaces for the transmit and receive paths.

AD-FMCDAQ2-EBZ block diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/AD-FMCDAQ2-EBZ_1.svg
   :alt: Xilinx HDL Block Diagram
   :width: 600px

Xilinx block diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/daq2_xilinx_2.svg
   :alt: Xilinx HDL Block Diagram
   :width: 800px

Altera block diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/daq2_intel.svg
   :alt: Altera HDL Block Diagram
   :width: 800px

Digital Interface
-----------------

The digital interface consists of 4 transmit and 4 receive lanes running at 10Gbps (default). The transceivers then interfaces to the cores at 128bits@250MHz. The data is sent or received based on the configuration (programmable) from separate transmit and receive chains.

Altera specific
~~~~~~~~~~~~~~~

When using Qsys, implementing JESD204B protocol requires several IPs. AVL_XCVR is a wrapper which instantiates all the required IPs and configures them according to the desired data rate. One AVL_XCVR must be instantiated for the transmit path and one for the receive path. It adds clock bridges, PLL and reconfiguration IP, proper reset, lane PLL for the transmit path, a JESD204B IP instantiating the JESD204B base and a JESD204B IP for each lane instantiating the PHY.

AXI_XCVR allows resetting and monitoring the transceiver path.

One important aspect for AD-FMCDAQ2-EBZ is that the reference clock needed for the FPGA transceiver calibration is generated only after the AD9523-1 clock generator is configured. The programming is done only after the FPGA is configured and software is running. Because of this, the software needs to perform a transceiver re-calibration after the transceiver reference clock is stable and before taking AXI_XCVR cores out of reset.

DAC Interface
-------------

The DAC data may be sourced from an internal data generator (DDS, pattern or PRBS) or from the external DDR via DMA. The internal DDS phase and frequency are programmable.

ADC Interface
-------------

The ADC data is sent to the DDR via DMA. The core also supports PN monitoring at the sample level. This is different from the JESD204B specific PN sequence (though they both claim to be from the same equation).

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI signals are controlled by a separate AXI based SPI core.

Supported Carriers
------------------

These are the supported carriers for the HDL - not the complete package (software and HDL). Typically the software lags behind the HDL, so if you don't see the these listed on the main project page - it is not yet done.

Our recommended plaforms are the Zynq based systems:

-  `ZC706 <https://www.xilinx.com/ZC706>`_

but it also works on the following fabric only systems:

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

For Altera systems:

-  `Arria 10 SoC Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_
-  `Arria 10 GX FPGA Development Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`_

Download
--------

.. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst

.. image:: https://wiki.analog.com/_media/navigation AD-FMCDAQ2-EBZ#Hardware#./
   :alt: Reference HDL Design#Software
