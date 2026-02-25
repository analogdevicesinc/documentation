HDL Reference Design
====================

The HDL reference design is built around the Zynq UltraScale+ quad
Cortex-A53 MPCore processors. The PS provides SDIO, UART, Ethernet, SPI,
USB 3.0, QSPI, and DisplayPort control modules.

The two ADRV9009 digital interfaces are handled by the JESD204B physical,
data link, and transport layer IPs. The JESD204B lanes are shared among the
8 transmit, 4 receive, and 4 observation/sniffer receive data paths. The
cores are programmable through an AXI-Lite interface.

Two PL DDR4 (32-bit @ 1200 MHz) modules can be used as offload FIFOs.
Additional transceiver lanes are available to implement PCIe Gen3 x8, 10 Gb
Ethernet, and 40 Gb Ethernet simultaneously. A full FMC HPC connector
enables extending the system with another two ADRV9009 devices.

Digital Interface
-----------------

The digital interface consists of 8 transmit, 4 receive, and 4
observation/sniffer lanes running up to 9.8 Gbps. The transceivers interface
to the cores at 256 bits @ 245 MHz in the transmit path and 128 bits @
245 MHz for the receive and observation paths.

TX Interface
~~~~~~~~~~~~

DAC data may be sourced from an internal data generator (DDS or pattern) or
from external DDR via DMA. The internal DDS phase and frequency are
programmable. The UNPACK IP (util_upack) allows transferring data from the
DMA to a reduced number of channels at a higher rate. The optional offload
FIFO uses one of the PL DDRs to capture data at maximum rate.

RX Interface
~~~~~~~~~~~~

ADC data is sent to DDR via DMA. The PACK IP (util_cpack) allows capturing
only a subset of channels. The optional offload FIFO uses one of the PL DDRs
to capture data at maximum rate.

OBS Interface
~~~~~~~~~~~~~

Observation data is sent to DDR via DMA with similar PACK IP support and
optional offload FIFO capability.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module.
The SPI signals are controlled by a single PS8 SPI core.

Block Diagrams
--------------

.. figure:: adrv9009_zu11eg_hdl.svg
   :align: center

   ADRV9009-ZU11EG system block diagram

.. figure:: adrv9009_zu11eg_datapath.svg
   :align: center

   ADRV9009-ZU11EG data path diagram

HDL Source Code
---------------

- :git-hdl:`projects/adrv9009zu11eg`
