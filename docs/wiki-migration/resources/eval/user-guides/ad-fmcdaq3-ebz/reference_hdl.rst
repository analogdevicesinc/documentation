AD-FMCDAQ3-EBZ HDL Reference Design
===================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/daq3/index.html\


Functional Overview
-------------------

The reference design is a processor based (ARM, Nios II or Microblaze) embedded system. A functional block diagram of the system is given below. The devices interfaces are shared by the same set of transceivers followed by the individual JESD204B and ADC/DAC pcores. The cores are programmable through an AXI-lite interface. The data path consists of independent DMA interfaces for the transmit and receive paths.

AD-FMCDAQ3-EBZ block diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/ad-fmcdaq3-ebz.svg
   :alt: FMC HDL Block Diagram
   :width: 500px

Xilinx block diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/daq3_xilinx_2.svg
   :alt: Xilinx HDL Block Diagram
   :width: 800px

Intel block diagram
~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/daq3_intel_2.svg
   :alt: Intel HDL Block Diagram
   :width: 800px

Digital Interface
-----------------

The digital interface consists of 4 transmit and 4 receive lanes running at 12.33Gbps (default). The transceivers then interface to the cores at 128bits@308.25MHz. The data is sent or received based on the configuration (programmable) from separate transmit and receive chains.

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

Our recommended platforms are the Zynq based systems:

-  `ZC706 <https://www.xilinx.com/ZC706>`_

but it also works on the following fabric only systems:

-  `KCU105 <https://www.xilinx.com/KCU105>`_

We are in the process of adding Zynq Ultrascale support:

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_

For Altera systems:

-  `A10GX <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`_

Download
--------

.. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst

.. image:: https://wiki.analog.com/_media/navigation AD-FMCDAQ3-EBZ#Hardware#./
   :alt: User Guide#.:\|Software
