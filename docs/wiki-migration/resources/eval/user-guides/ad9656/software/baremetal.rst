AD9656 Bare Metal Quick Start Guide
===================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD9656 on the `ZCU102 <https://www.xilinx.com/ZCU102>`_ carrier board.

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  AD9656 Main Application - :git-no-OS:`projects/ad9656_fmc`
   -  Platform Drivers - :git-no-OS:`drivers/platform/xilinx`
   -  AD9656 Driver - :git-no-OS:`drivers/adc/ad9656`
   -  ADC Core Driver - :git-no-OS:`drivers/axi_core/axi_adc_core`
   -  DMA Core Driver - :git-no-OS:`drivers/axi_core/axi_dmac`
   -  Transceiver Core Driver - :git-no-OS:`drivers/axi_core/jesd204`
   -  Transceiver Modules Drivers -:git-no-OS:`drivers/axi_core/jesd204`
   -  JESD204B Core Driver - :git-no-OS:`drivers/axi_core/jesd204`
   

Make
----

.. include:: ../../../../no-os/build.rst

Software setup
--------------

.. note::

   See `resources/fpga/no-os_make/software_setup <https://wiki.analog.com/resources/fpga/no-os_make/software_setup>`_

GUI
---

.. include:: ../../../../fpga/xilinx/software_setup.rst

More information
----------------

-  :doc:`AD9656 HDL User Guide </wiki-migration/resources/eval/user-guides/ad9656/reference_hdl>`
-  :doc:`AD9656 Board User Guide </wiki-migration/resources/eval/ad9656-125ebz>`
