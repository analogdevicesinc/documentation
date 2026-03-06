ADRV9009-ZU11EG HDL Reference Design
====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/adrv9009zu11eg/index.html\


Functional Overview
-------------------

The HDL reference design is built around the Zynq® Ultrascale+ four Cortex™-A536 MPCore processors. A functional block diagram of the system is shown below.

The PS8 provides a SDIO, UART, Ethernet, SPI, USB 3.0, QSPI and a Display Port control modules.

The two ADRV9009's digital interface is handled by the JESD20B physical, data link and transport layer IPs. The JESD204B lanes are shared among the 8 transmit, 4 receive and 4 observation/sniffer receive data paths by the same set of transceivers within the IP. The cores are programmable through an AXI-lite interface.

There are 2 PL DDR4 32 bit@1200MHz which can be used as OFFLOAD FIFOs in the system.

There are additional transceiver lanes available that can be used to implement PCIe Gen3 x8, 10Gb ethernet and 40Gb ethernet at the same time. On top of those, another 10 transceiver lanes can be used to implement a full FMC HPC connector, through which to extend the system with another two ADRV9009s.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/adrv9009_zu11eg_hdl.svg
   :alt: adrv9009_zu11eg_hdl.svg
   :align: center
   :width: 700px

Digital Interface
-----------------

The digital interface consists of 8 transmit, 4 receive and 4 observation/sniffer lanes running up to 9.8Gbps. The transceivers then interface to the cores at 256bits@245MHz in the transmit and 128bits@245MHz for the receive and sniffer/observation rates. The data is sent or received based on the configuration (programmable) from separate transmit, receive and observation chains.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009-zu11eg/adrv9009_zu11eg_datapath.svg
   :alt: adrv9009_zu11eg_datapath.svg
   :align: center
   :width: 700px

TX Interface
------------

The DAC data may be sourced from an internal data generator (DDS or pattern) or from the external DDR via DMA. The internal DDS phase and frequency are programmable. The UNPACK IP (util_upack) allows transfering data from the DMA to a reduced number of channels, at a higher rate. The optional OFFLOAD FIFO uses one of the PL DDRs to capture data at maximum rate.

RX Interface
------------

The RX data is sent to the DDR via DMA. The PACK IP (util_cpack) allows capturing only part of the channels. The optional OFFLOAD FIFO uses one of the PL DDRs to capture data at maximum rate.

OBS Interface
-------------

The OBS data is sent to the DDR via DMA. The PACK IP (util_cpack) allows capturing only part of the channels. The optional OFFLOAD FIFO uses one of the PL DDRs to capture data at maximum rate.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI signals are controlled by a single PS8 SPI core.

Project Location
----------------

The project is available at https://github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009zu11eg

More Information
----------------

-  :doc:`ADI HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI JESD204B Interface Framework User Guide </wiki-migration/resources/fpga/peripherals/jesd204>`
