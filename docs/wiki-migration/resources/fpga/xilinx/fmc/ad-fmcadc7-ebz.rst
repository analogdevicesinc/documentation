AD-FMCADC7-EBZ HDL Reference Design
===================================

.. important::

   This HDL project is obsolete, and is no longer supported. The source code can be found in the last release where it was present, :git-hdl:`hdl_2021_r2 <releases/tag/2021_R2>`.


Functional Overview
-------------------

The FMCADC7 reference design is a processor based (ARM, NIOS-II or Microblaze) embedded system. The device interfaces to the FPGA transceivers followed by the individual JESD204B and ADC cores. The cores are programmable through an AXI-lite interface. The samples are passed to the system memory (DDR).

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI signals are controlled by a separate AXI based SPI core.

Download
--------

.. include:: ../../docs/hdl/downloads_insert.rst .. include:: ../../docs/hdl/downloads_insert.rst
