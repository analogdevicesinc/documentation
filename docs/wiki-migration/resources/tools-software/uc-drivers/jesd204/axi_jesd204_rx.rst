ADI JESD204B/C Receive Peripheral No-OS Driver
==============================================

-  :doc:`ADI JESD204B/C Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>`

Description
-----------

The AXI JESD204B RX peripheral driver is a simple driver that supports the :doc:`ADI JESD204B Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>`. The driver reads JESD204B link configuration data from the initialization structure and configures the peripheral accordingly. After configuration has completed the JESD204B link is enabled. Link state can be monitored through using the \`axi_jesd204_rx_status_read\` function.

Initialization example
======================

.. code:: c

   struct jesd204_rx_init rx_jesd_init = {
       .name = "rx_jesd",
       .base = RX_JESD_BASEADDR,
       .octets_per_frame = 2,
       .frames_per_multiframe = 32,
       .subclass = 1,
       .device_clk_khz = 2500000 / 40, /* (lane_clk_khz / 40) */
       .lane_clk_khz = 2500000, /* LaneRate = (M/L)*NP*(10/8)*DataRate */
   };

   struct axi_jesd204_rx *rx_jesd;

   status = axi_jesd204_rx_init(&rx_jesd, &rx_jesd_init);
   if (status != 0) {
       printf("error: %s: axi_jesd204_rx_init() failed\n", rx_jesd_init.name);
       return status;
   }

   status = axi_jesd204_rx_lane_clk_enable(rx_jesd);
   if (status != 0) {
       printf("error: %s: axi_jesd204_rx_lane_clk_enable() failed\n", rx_jesd->name);
       return status;
   }

   status = axi_jesd204_rx_status_read(rx_jesd);
   if (status != 0) {
       printf("axi_jesd204_rx_status_read() error: %d\n", status);
   }

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `JESD204B/C Receive Peripheral Header file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__jesd204__rx_8h.html>`_
-  `JESD204B/C Receive Peripheral Source file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__jesd204__rx_8c.html>`_

Source Code
===========

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of JESD204B/C Receive Peripheral Driver.|

   -

   |Header of JESD204B/C Receive Peripheral Driver.|

.. |Implementation of JESD204B/C Receive Peripheral Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_jesd204_rx`.c
.. |Header of JESD204B/C Receive Peripheral Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/jesd204/axi_jesd204_rx`.h
