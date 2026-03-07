ADRV9371 HDL Reference Design
=============================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/adrv9371x/index.html\


Functional Overview
-------------------

The HDL reference design is an embedded system built around a processor core either ARM, NIOS-II or Microblaze. A functional block diagram of the system is shown below. The device digital interface is handled by the transceiver IP followed by the JESD204B and device specific cores. The JESD204B lanes are shared among the 4 transmit, 4 receive and 2 observation/sniffer receive data paths by the same set of transceivers within the IP. The cores are programmable through an AXI-lite interface. The delineated data is then passed on to independent DMA cores for the transmit, receive and observation/sniffer paths.

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/adrv9371_3.svg
   :alt: adrv9371_3.svg
   :align: center

Digital Interface
-----------------

The digital interface consists of 4 transmit, 2 receive and 2 observation/sniffer lanes running up to 6Gbps (default is 4Gbps). The transceivers then interfaces to the cores at 128bits@122MHz in the transmit and 64bits@122MHz for the receive channels. The sniffer/observation rates depends on the mode selected. The data is sent or received based on the configuration (programmable) from separate transmit and receive chains.

DAC Interface
-------------

The DAC data may be sourced from an internal data generator (DDS, pattern or PRBS) or from the external DDR via DMA. The internal DDS phase and frequency are programmable.

ADC Interface
-------------

The ADC data is sent to the DDR via DMA.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI signals are controlled by a separate AXI based SPI core.

Download
--------

The HDL repository, list of supported carriers and the list of required IP cores can be found here:

.. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst
