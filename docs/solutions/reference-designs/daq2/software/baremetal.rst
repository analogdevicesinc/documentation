AD-FMCDAQ2-EBZ Bare Metal Quick Start Guide
===========================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD-FMCDAQ2-EBZ
on either:

-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `KC705 <https://www.xilinx.com/KC705>`_
-  `KCU105 <https://www.xilinx.com/KCU105>`_
-  `VC707 <https://www.xilinx.com/VC707>`_

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  FMCDAQ2 Main Driver - :git-no-OS:`fmcdaq2`
   -  Platform Drivers - :git-no-OS:`common_drivers/platform_drivers`
   -  AD9144 Driver - :git-no-OS:`drivers/dac/ad9144`
   -  AD9523 Driver - :git-no-OS:`drivers/frequency/ad9523`
   -  AD9680 Driver - :git-no-OS:`drivers/adc/ad9680`
   -  ADC Core Driver - :git-no-OS:`common_drivers/adc_core`
   -  DAC Core Driver - :git-no-OS:`common_drivers/dac_core`
   -  DAC Buffer Drivers - :git-no-OS:`common_drivers/dac_buffer`
   -  DMA Core Driver - :git-no-OS:`common_drivers/dmac_core`
   -  Transceiver Core Driver - :git-no-OS:`common_drivers/xcvr_core`
   -  Transceiver Modules Drivers - :git-no-OS:`common_drivers/xcvr_core/xcvr_modules`
   -  JESD204B Core Driver - :git-no-OS:`common_drivers/jesd_core`
   

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
