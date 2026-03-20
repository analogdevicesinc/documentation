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

.. note::

   See `Build <https://wiki.analog.com/resources/no-os/build>`_.

Software setup
--------------

.. note::

   See `resources/fpga/no-os_make/software_setup <https://wiki.analog.com/resources/fpga/no-os_make/software_setup>`_

GUI
---

.. note::

   See `Software Setup <https://wiki.analog.com/resources/fpga/xilinx/software_setup>`_.

More information
----------------

-  :doc:`AD9656 HDL User Guide </solutions/reference-designs/ad9656/reference_hdl>`
-  `AD9656 Board User Guide <https://wiki.analog.com/resources/eval/ad9656-125ebz>`_
