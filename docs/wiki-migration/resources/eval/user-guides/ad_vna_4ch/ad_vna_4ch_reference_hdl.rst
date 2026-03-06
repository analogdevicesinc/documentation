AD VNA 4CH FMC Card HDL Reference Design
========================================

Overview
--------

4x Vector Network Analyzer(VNA) HDL reference design

The :adi:`AD9083` is a 16-bit, 16 channel with 125 MHz bandwidth per channel (2 GSPS total) analog-to-digital converter (ADC) featuring an on-chip programmable, single-pole antialiasing filter and termination resistor that is designed for low power, small size, and ease of use.

In the VNA design we will use decimation filters inside the AD9083 resulting in a 15.625, 7.8125 or 3.90625 MSPS bandwidth for each channel(32 virtual channels).

The :adi:`AD9173` is a high performance, dual, 16-bit digital-to-analog converter (DAC) that supports DAC sample rates to 12.6 GSPS. The AD9173 features three complex data input channels. The device supports up to a 1.54 GSPS complex data rate per input channel and is capable of aggregating multiple complex input data streams up to a maximum complex data rate of 1.54 GSPS. The device will be used in mode 4(L=4, M=4, F=2, S=1, NP=16, N=16, K=32)

AD4858 - is a precision ADC with 8 channels from which 4 are used.

All cores from the receive chain are programmable through an AXI-Lite interface.

Supported Devices
-----------------

-  :adi:`AD9083`

https://wiki.analog.com/resources/eval/ad_vna_4ch

Supported Carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`__ - HPC0 Slot

Block Diagram
~~~~~~~~~~~~~

The data path and clock domains are depicted on the below diagram:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad_vna_4ch/adi_vna_4x_wiki2.svg
   :align: center

AD9083(ADC)
~~~~~~~~~~~

The design has one JESD receive chain with 1 lanes at rate of 10Gbps. The JESD receive chain consists of a physical layer represented by an XCVR module, a link layer represented by an RX JESD LINK module and transport layer represented by a RX JESD TPL module. The links operate in Subclass 0 since it is not using the SYSREF signal.

Deframer paramaters: L=1, M=32, F=64, S=1, N’=16

| GTREFCLK – 500MHz
| LINKCLK(Lane Rate/40) – 250MHz
| DEVICECLK - 15.625 MHz depending on the chosen dtb
| JESD204B Lane Rate – 10Gbps
| Because of the F=64 parameter the JESD Link IP will have different input and output frequencies and bus widths. Data will enter the IP on 1 32bit wide channel at 250MHz (link clock) and will exit on a 512bit interface clocked at 15.625MHz (device clock). The transport layer component presents on its output 512 bits at once on every clock cycle, representing 1 sample per converter(32). The receive chain is then transferred to the DDR using a DMA.

AD9173(DAC)
~~~~~~~~~~~

Deframer paramaters(Mode 4): L=4, M=4, F=1, S=1, N’=16

| GTREFCLK – 500 MHz
| LINKCLK(Lane Rate/40) – 312,5 MHz
| DEVICECLK - --- MHz depending on the chosen dtb
| JESD204B Lane Rate – 12.5Gbps
| SPI connections

==================== ============= =========== =============== ===
SPI manager instance Alias         SPI address SPI subordinate CSn
==================== ============= =========== =============== ===
psu spi 0            spi_fpga      0xFF040000  AD9083          0
psu spi 1            spi ad        0xFF050000  AD4858          0
:::                  :::           :::         AD4696          1
axi_spi_bus0         spi_bus_0     0x88000000  AD4372          0
:::                  :::           :::         AD9528          2
axi_spi_bus1         spi_bus_1     0x88100000  ADRF5720 D1     0
:::                  :::           :::         ADRF5720 D2     1
axi_spi_adl5960_1    spi_adl5960_1 0x88200000  ADL5960 A       0
:::                  :::           :::         ADL5960 B       1
:::                  :::           :::         ADL5960 C       2
:::                  :::           :::         ADL5960 D       3
axi_spi_fmcdac       spi_fmcdac    0x88300000  AD9173          0
axi_spi_busf         spi_busf      0x88400000  ADMV8818        0
==================== ============= =========== =============== ===

Building the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository. Then go to the /projects/ad_vna_4ch/zcu102 location and run the make command by typing in your command prompt:

PL Interrupts
^^^^^^^^^^^^^

==================== ============= ===================
Instance             HDL interrupt Linux PsU interrupt
==================== ============= ===================
---                  0             89
---                  1             90
---                  2             91
axi_spi_fmcdac       3             92
axi_dac_jesd204_link 4             93
axi_dac_dma          5             94
axi_ad4858_dma       6             95
---                  7             96
axi_spi_adl5960_1    8             104
axi_spi_busf         9             105
axi_spi_bus1         10            106
axi_spi_bus0         11            107
axi_ad9083_rx_jesd   12            108
axi_ad9083_rx_dma    13            109
---                  14            110
---                  15            111
==================== ============= ===================

GPIO signals(schematic)
^^^^^^^^^^^^^^^^^^^^^^^

Ps8 EMIO offset = 78

================= ==== ==============
GPIO Signal       GPIO HDL GPIO EMIOn
================= ==== ==============
adcpd             130  52
adcmon_rstn       129  51
fpga_busf_sfl     128  50
fpga_hlsel        127  49
gpio_sw_pg        126  48
gpio_mix2en       121  43
gpio_sw3_v2       120  42
gpio_sw4_v2       119  41
gpio_sw4_v1       118  40
gpio_sw3_v1       117  39
gpio_sw2          116  38
gpio_sw1_v2       115  37
gpio_sw1_v1       114  36
adl5960x_sync1    113  35
fpga_adclk_refsel 112  34
fmc_rstb          111  33
fmc_pd            110  32
================= ==== ==============

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad_vna_4ch/zcu102
   user@analog:~/hdl/projects/ad_vna_4ch/zcu102$ make

A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |AD VNA 4 channels HDL Project|

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

.. |AD VNA 4 channels HDL Project| image:: https://wiki.analog.com/_media/:git-hdl:`projects/ad_vna_4ch`
.. |Linux Driver| image:: https://github.com/analogdevicesinc/linux
