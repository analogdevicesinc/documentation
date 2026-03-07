ADI JESD204B/C Transmit Peripheral No-OS Driver
===============================================

Supported Devices
-----------------

-  :doc:`ADI JESD204B/C Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>`

Description
-----------

The AXI JESD204B TX peripheral driver is a simple driver that supports the :doc:`ADI JESD204B Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>`. The driver reads JESD204B link configuration data from the initialization structure and configures the peripheral accordingly. After configuration has completed the JESD204B link is enabled. Link state can be monitored through using the \`axi_jesd204_tx_status_read\` function.

Initialization example
======================

.. code:: c

   struct jesd204_tx_init tx_jesd_init = {
       .name = "tx_jesd",
       .base = TX_JESD_BASEADDR,
       .octets_per_frame = 2,
       .frames_per_multiframe = 32,
       .converters_per_device = 4,
       .converter_resolution = 16,
       .bits_per_sample = 16,
       .high_density = false,
       .control_bits_per_sample = 0,
       .subclass = 1,
       .device_clk_khz = 184320,   /* (lane_clk_khz / 40) */
       .lane_clk_khz = 7372800,    /* LaneRate = ( M/L)*NP*(10/8)*DataRate */
   };
   struct axi_jesd204_tx *tx_jesd;

   status = axi_jesd204_tx_init(&tx_jesd, &tx_jesd_init);
   if (status != 0) {
       printf("error: %s: axi_jesd204_tx_init() failed\n", tx_jesd_init.name);
       return status;
   }

   status = axi_jesd204_tx_lane_clk_enable(tx_jesd);
   if (status != 0) {
       printf("error: %s: axi_jesd204_tx_lane_clk_enable() failed\n", tx_jesd->name);
       return status;
   }

   status = axi_jesd204_tx_status_read(tx_jesd);
   if (status != 0) {
       printf("axi_jesd204_tx_status_read() error: %d\n", status);
   }

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `JESD204B/C Transmit Peripheral Header file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__jesd204__tx_8h.html>`_
-  `JESD204B/C Transmit Peripheral Source file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__jesd204__tx_8c.html>`_

Source Code
===========

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of JESD204B/C Transmit Peripheral Driver.|

   -

   |Header of JESD204B/C Transmit Peripheral Driver.|

.. |Implementation of JESD204B/C Transmit Peripheral Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_jesd204_tx`.c
.. |Header of JESD204B/C Transmit Peripheral Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_jesd204_tx`.h
