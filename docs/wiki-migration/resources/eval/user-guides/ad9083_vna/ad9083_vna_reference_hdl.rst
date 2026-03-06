AD9083 VNA FMC Card HDL Reference Design
========================================

Overview
--------

8x Vector Network Analyzer(VNA) HDL reference design

The AD9083 is a 16-bit, 16 channel with 125 MHz bandwidth per channel (2 GSPS total) analog-to-digital converter (ADC) featuring an on-chip programmable, single-pole antialiasing filter and termination resistor that is designed for low power, small size, and ease of use.

In the VNA design we will use decimation filters inside the AD9083 resulting in a 15.625, 7.8125 or 3.90625 MSPS bandwidth for each channel(32 virtual channels).

All cores from the receive chain are programmable through an AXI-Lite interface.

Supported Devices
-----------------

-  :adi:`AD9083`

https://wiki.analog.com/resources/eval/ad9083_vna

Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__ - HPC0 Slot

Block Diagram
~~~~~~~~~~~~~

The data path and clock domains are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/reference_designs/adi_vna_8x.svg
   :align: center

The design has one JESD receive chain with 1 lanes at rate of 10Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The links operate in Subclass 0 since it is not using the SYSREF signal.

Both links are set for full bandwidth mode and operate with the following parameters:

Deframer paramaters: L=1, M=32, F=64, S=1, N’=16

| GTREFCLK – 500MHz
| LINKCLK(Lane Rate/40) – 250MHz
| DEVICECLK - 15.625 MHz depending on the chosen dtb
| JESD204B Lane Rate – 10Gbps
| Because of the F=64 parameter the JESD Link IP will have different input and output frequencies and bus widths. Data will enter the IP on 1 32bit wide channel at 250MHz (link clock) and will exit on a 512bit interface clocked at 15.625MHz (device clock). The transport layer component presents on its output 512 bits at once on every clock cycle, representing 1 sample per converter(32). The receive chain is then transferred to the DDR using a DMA.

SPI connections

==================== =========== =========== =============== ===
SPI manager instance Alias       SPI address SPI subordinate CSn
==================== =========== =========== =============== ===
psu spi 0            spi_fpga    0xFF040000  AD9083          0
psu spi 1            spiad       0xFF050000  AD4696          0
axi_spi_bus0         spi_bus_0   0x48000000  ADF4372         0
:::                  :::         :::         AD9528          1
axi_spi_bus1         spi_bus_1   0x48100000  ADF4372 D2      0
:::                  :::         :::         ADF4372 D1      1
:::                  :::         :::         MAX7301ATL+     2
axi_spi_adl5960      spi_adl5960 0x48200000  ADL5960 A       0
:::                  :::         :::         ADL5960 B       1
:::                  :::         :::         ADL5960 C       2
:::                  :::         :::         ADL5960 D       3
:::                  :::         :::         ADL5960 E       4
:::                  :::         :::         ADL5960 F       5
:::                  :::         :::         ADL5960 G       6
:::                  :::         :::         ADL5960 H       7
axi_spi_fmcdac       spi_fmcdac  0x48300000  AD9173          0
axi_spi_busf         spi_busf    0x48400000  ADMV8812SCCZ    0
axi_spim             spim        0x48500000  ADRF6780SC SIG  0
:::                  :::         :::         ADRF6780SC LO   1
axi_spi_ndac         spi_ndac    0x48600000  AD5664          0
==================== =========== =========== =============== ===

PL Interrupts
^^^^^^^^^^^^^

================== ============= ===================
Instance           HDL interrupt Linux PsU interrupt
================== ============= ===================
axi_spi_fmcdac     3             92
dac_jesd204_link   4             93
dac_dma            5             94
axi_spi_ndac       6             95
axi_spi_adl5960    8             104
axi_spi_fpga_busf  9             105
axi_spi_bus1       10            106
axi_spi_bus0       11            107
axi_ad9083_rx_jesd 12            108
axi_ad9083_rx_dma  13            109
axi_spim           15            111
================== ============= ===================

GPIO signals(schematic)
^^^^^^^^^^^^^^^^^^^^^^^

Ps8 EMIO offset = 78

============== ==== =============
GPIO Signal    GPIO HDL EMIO GPIO
============== ==== =============
fpga_busf_sfl  128  50
spare_gpiox    127  49
---            ---  ---
adcmon_rstn    119  41
smix_rstn      118  40
---            ---  ---
lmix_rstn      114  36
adl5960x_sync1 113  35
---            ---  ---
fmc_rstb       111  33
fmc_pd         110  32
============== ==== =============

Building the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository. Then go to the /projects/ad9083_vna/zcu102 location and run the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad9083_vna/zcu102
   user@analog:~/hdl/projects/ad9083_vna/zcu102$ make

A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |AD9083 HDL Project|

Software sources
----------------

.. admonition:: Download
   :class: download

   
   -


   
   |Linux Driver|

More Information
~~~~~~~~~~~~~~~~

-  :doc:`AD9083 Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9083>`
-  :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`
-  :doc:`JESD204B High-Speed Serial Interface Support </wiki-migration/resources/fpga/peripherals/jesd204>`

Support
-------

Analog Devices will provide limited online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone <community/fpga>`.

.. |AD9083 HDL Project| image:: https://wiki.analog.com/_media/:git-hdl:`projects/ad9083_vna`
.. |Linux Driver| image:: https://github.com/analogdevicesinc/linux
