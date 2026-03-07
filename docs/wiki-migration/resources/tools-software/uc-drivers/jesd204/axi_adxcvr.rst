ADI JESD204B/C AXI_ADXCVR Highspeed Transceivers No-OS Driver
=============================================================

Supported Devices
-----------------

-  :doc:`AXI_ADXCVR Physical Layer Highspeed Transceivers HDL Core </wiki-migration/resources/fpga/docs/axi_adxcvr>`

Description
-----------

The JESD204B/C AXI_ADXCVR Highspeed Transceivers peripheral driver is a simple driver that supports the :doc:`AXI_ADXCVR Physical Layer Highspeed Transceivers HDL Core </wiki-migration/resources/fpga/docs/axi_adxcvr>`. The driver reads some configuration from the initialization structure and configures the peripheral accordingly. After configuration has completed the JESD204 link is enabled, this driver also supports PHY layer `PRBS <https://en.wikipedia.org/wiki/PRBS>`_ generation and checking.

Initialization example
======================

.. code:: c

   struct adxcvr_init axi_xcvr_param = {
       .name = "axi_xcvr",
       .base = RX_XCVR_BASEADDR,
       .sys_clk_sel = ADXCVR_SYS_CLK_CPLL,
       .out_clk_sel = ADXCVR_REFCLK_DIV2,
       .lpm_enable = 0,
       .ref_rate_khz = 625000,
       .lane_rate_khz = 6250000,
           .export_no_os_clk = true
   };
   struct adxcvr *axi_xcvr;

   status = adxcvr_init(&axi_xcvr, &axi_xcvr_param);
   if (status != 0) {
       printf("error: %s: adxcvr_init() failed\n", axi_xcvr->name);
       return status;
   }

   status = adxcvr_clk_enable(axi_xcvr);
   if (status != 0) {
       printf("error: %s: adxcvr_clk_enable() failed\n", axi_xcvr->name);
       return status;
   }

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `AXI_ADXCVR Highspeed Transceivers Header file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__adxcvr_8h.html>`_
-  `AXI_ADXCVR Highspeed Transceivers Source file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__adxcvr_8c.html>`_

Source Code
===========

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of AXI_ADXCVR Highspeed Transceivers Driver.|

   -

   |Header of AXI_ADXCVR Highspeed Transceivers Driver.|

.. |Implementation of AXI_ADXCVR Highspeed Transceivers Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_adxcvr`.c
.. |Header of AXI_ADXCVR Highspeed Transceivers Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_adxcvr`.h
