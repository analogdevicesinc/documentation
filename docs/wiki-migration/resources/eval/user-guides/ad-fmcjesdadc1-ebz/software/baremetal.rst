AD-FMCJESDADC1-EBZ Bare Metal Quick Start Guide
===============================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD-FMCJESDADC1-EBZ on either:

-  `KC705 <https://www.xilinx.com/KC705>`_
-  `VC707 <https://www.xilinx.com/VC707>`_
-  `ZC706 <https://www.xilinx.com/ZC706>`_

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  AD-FMCJESDADC1-EBZ Main, AD9250, AD9517 Drivers - :git-no-OS:`ad-fmcjesdadc1-ebz`
   -  Platform Drivers - :git-no-OS:`common_drivers/platform_drivers`
   -  ADC Core Driver - :git-no-OS:`common_drivers/adc_core`
   -  XCVR Driver - :git-no-OS:`common_drivers/xcvr_core`
   -  JESD204B Driver - :git-no-OS:`common_drivers/jesd_core`
   


Required Software
~~~~~~~~~~~~~~~~~

-  We upgrade the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <tree/master>`.
-  A :doc:`UART </wiki-migration/resources/fpga/uart_setup>` terminal (Tera Term/Hyperterminal), baud rate 115200.

Software Setup
~~~~~~~~~~~~~~

-  With every release, we add new features, check the generic build process:

   -  `make <https://wiki.analog.com/resources/fpga/no-os_make/software_setup>`_
   -  :doc:`GUI </wiki-migration/resources/fpga/xilinx/software_setup>` (manual)
