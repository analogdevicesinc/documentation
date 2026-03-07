AXI DAC No-OS Driver
====================

Description
-----------

The AXI DAC DDS HDL driver is the driver for various HDL interface cores which are used on different FPGA designs. The driver is implemented as an no-OS driver. It's register map can be found here: :doc:`Base register map (common to all cores) </wiki-migration/resources/fpga/docs/hdl/regmap>`

This driver is independent from the physical layer. So it's being used with CMOS or LVDS type interfaces or the :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>`.

Sometimes there is a common HDL/FPGA transport layer core, which handles both RX/TX or ADC/DMA. This single physical core is then handled by two independent IIO drivers each for one transport data direction. It’s physical address register space is then also split or divided, typically spaced by 0x4000. A good example for this case is the :doc:`AXI_AD9361 </wiki-migration/resources/fpga/docs/axi_ad9361>` HDL core.

The HDL/FPGA transport layer capture core driver portion implements a polyphase dual tone DDS core per channel together with an DMA based waveform buffer mechanism. The buffer can be filled by arbitrary data, which is then typically cyclically repeated or used in a streaming fashion.

Initialization example
======================

.. code:: c

   struct axi_dac_init tx_dac_init = {
       .name = "tx_dac",
       .base = TX_CORE_BASEADDR,
       .num_channels = 2,
           .rate = 3
   };

   struct axi_dac *tx_dac;

   /* Initialize the DAC DDS */
   status = axi_dac_init(&tx_dac, &tx_dac_init);
   if (status != 0) {
       printf("axi_dac_init() error: %"PRIi32"\n", status);
       return status;
   }

   status = axi_dac_set_datasel(tx_dac, -1, AXI_DAC_DATA_SEL_DMA);
   if (status != 0) {
       printf("axi_dac_set_datasel() error: %"PRIi32"\n", status);
       return status;
   }

   status = axi_dac_load_custom_data(tx_dac, sine_lut_iq,
                     NO_OS_ARRAY_SIZE(sine_lut_iq),
                     (uintptr_t)dac_buffer);
   if (status != 0) {
       printf("axi_dac_load_custom_data() error: %"PRIi32"\n", status);
       return status;
   }

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `AXI DAC Core Header file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__dac__core_8h.html>`_
-  `AXI DAC Core Source file <http://analogdevicesinc.github.io/no-OS/doxygen/axi__dac__core_8c.html>`_

Source Code
===========

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of AXI DAC Core Driver.|

   -

   |Header of AXI DAC Core Driver.|

.. |Implementation of AXI DAC Core Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/axi_dac_core/axi_dac_core`.c
.. |Header of AXI DAC Core Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/axi_dac_core/axi_dac_core`.h
