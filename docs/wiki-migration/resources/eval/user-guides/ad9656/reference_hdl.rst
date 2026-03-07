AD9656 HDL Reference Design
===========================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/projects/ad9656_fmc/index.html\


Introduction
------------

The :adi:`AD9656` is a quad 16-bit, 125MSPS analog-to-digital converter (ADC) with an on-chip sample and hold circuit designed for low cost, low power, small size, and ease of use. The :adi:`AD9656EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9656.html#eb-overview>` board is build around the AD9656 chip and it pairs with a carrier board through a FMC connector. The ADC chip uses the JESD204B protocol to transfer the data to the carrier board. The SPI protocol is used by the carrier board to configure the parameters from the register file of the ADC and the two clock chips.

Supported Devices
-----------------

-  :adi:`AD9656EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9656.html#eb-overview>`

Supported Carriers
------------------

Until now our recommended plaform is the Zynq based system:

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_

Functional Overview
-------------------

The reference design is a processor based ARM embedded system. A functional block diagram of the system is given below for the Xilinx FPGAs. The cores are programmable through an AXI-lite interface. The data path consists of a DMA interface for the receive path.

AD9656 block diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9656-block_diagram.png
   :align: center
   :width: 600px

Xilinx block diagram
~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/xilinx_block_diagram.png
   :align: center
   :width: 600px

Digital Interface
-----------------

The digital interface consists of 4 receive lanes running at 2.5Gbps. The transceivers then interfaces to the cores at 128bits@62.5MHz. The data is received based on the configuration (programmable) from separate receive chains.

ADC Interface
-------------

The ADC data is sent to the DDR via DMA. The core also supports PN monitoring at the sample level. This is different from the JESD204B specific PN sequence.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI signals are controlled by a separate AXI based SPI core.

Building the HDL
----------------

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository. Then go to the /projects/ad9656_fmc/zcu102 location and run the make command by typing in your command prompt:

**Linux**

::

   dhotolea@analog:~$ cd hdl/projects/ad9656_fmc/zcu102
   dhotolea@analog:~/hdl/projects/ad9656_fmc/zcu102$ make

A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

More information
----------------

-  :doc:`AD9656 no-OS User Guide </wiki-migration/resources/eval/user-guides/ad9656/software/baremetal>`
-  :doc:`AD9656 Board User Guide </wiki-migration/resources/eval/ad9656-125ebz>`

Download
--------

.. include:: ../../../fpga/docs/hdl/downloads_insert.rst .. include:: ../../../fpga/docs/hdl/downloads_insert.rst
