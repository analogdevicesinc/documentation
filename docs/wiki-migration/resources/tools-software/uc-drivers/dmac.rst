AXI DMAC No-OS Driver
=====================

Description
-----------

The AXI DMAC (DMA Controller) IP Core driver is the driver for :doc:`High-Speed DMA Controller Peripheral </wiki-migration/resources/fpga/docs/axi_dmac>` which is used on various FPGA designs. The register map of the DMA Controller can be found here: :doc:`Base register map (common to all cores) </wiki-migration/resources/fpga/docs/hdl/regmap>`.

Initialization example
----------------------

.. code:: c

   struct axi_dmac_init rx_dmac_init = {
       /* Instance name */
       .name = "rx_dmac",
       /* Base address */
       .base = CF_AD9361_RX_DMA_BASEADDR,
       /* Flag indicating whether IRQs are enabled */
       .use_irq = IRQ_ENABLED
   };

   /* Initialize the DAMC core */
   status = axi_dmac_init(&rx_dmac, &rx_dmac_init);
   if (status) {
       printf("axi_dmac_init rx init error: %"PRIi32"\n", status);
       return status;
   }

DMA Transfer
------------

A structure that specifies the DMA transfer characteristics is required for sending/receiving data.

.. code:: c

   struct axi_dma_transfer {
       /* Transfer size */
       uint32_t size;
       /* Flag indicating transfer status */
       volatile bool transfer_done;
       /* Flag indicating whether data is sent cyclically */
       enum cyclic_transfer cyclic;
       /* The address of the data source */
       uint32_t src_addr;
       /* The address of the data destination */   
       uint32_t dest_addr;
   };

The following examples show the three types of DMA transfers possible: memory to device (e.g., DAC), device (e.g., ADC) to memory, and memory to memory.

Memory to device transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below transfers in a loop an array named ``sine_lut_iq``, witten at address ``dac_buffer``, to a DAC.

.. code:: c

   struct axi_dma_transfer transfer = {
       // Number of bytes to write/read
       .size = sizeof(sine_lut_iq),
       // Transfer done flag
       .transfer_done = 0,
       // Signal transfer mode
       .cyclic = CYCLIC,
       // Address of data source
       .src_addr = (uintptr_t)dac_buffer,
       // Address of data destination
       .dest_addr = 0
   };

   /* Transfer the data. */
   axi_dmac_transfer_start(tx_dmac, &transfer);

Note
^^^^

-  After each DMA transfer, the program has to invalidate the cache for the associated data.

.. code:: c

   /* Invalidate cache data. Example for a Xilinx platform. */
   Xil_DCacheInvalidateRange((uintptr_t)dac_buffer, sizeof(sine_lut_iq));

-  Only a memory to device transfer can be CYCLIC.
-  A CYCLIC transfer uses the hardware feature of the DMAC IP Core that automatically disables interrupts for the corresponding instance and cyclically sends the data if this does not exceed the maximum transfer size specified in the HDL. If the CYCLIC flag is set and the transfer exceeds the maximum size for one transmission, then the cyclic sending of the data is solved by the driver through the use of interrupts.

Device to memory transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below transfers ``sizeof(adc_buffer)`` bytes of data from an ADC to the memory at address ``adc_buffer``.

.. code:: c

   struct axi_dma_transfer read_transfer = {
       // Number of bytes to write/read
       .size = sizeof(adc_buffer),
       // Transfer done flag
       .transfer_done = 0,
       // Signal transfer mode
       .cyclic = NO,
       // Address of data source
       .src_addr = 0,
       // Address of data destination
       .dest_addr = (uintptr_t)adc_buffer
   };

   /* Read the data from the ADC DMA. */
   axi_dmac_transfer_start(rx_dmac, &read_transfer);

   /* Wait until transfer finishes */
   status = axi_dmac_transfer_wait_completion(rx_dmac, timeout);
   if(status)
       return status;

.. _note-1:

Note
^^^^

-  After each DMA transfer, the program has to invalidate the cache for the associated data.

.. code:: c

   /* Invalidate cache data. Example for a Xilinx platform. */
   Xil_DCacheInvalidateRange((uintptr_t)adc_buffer, sizeof(adc_buffer));

-  If the size exceeds the maximum transfer size specified in the HDL and if interrupts are enabled for the DMAC instance, then all the data is retrieved. If interrupts are disabled, only a transfer with the maximum size is performed and the application has to manage the reading of the entire amount of data.

Memory to memory transfer
~~~~~~~~~~~~~~~~~~~~~~~~~

A memory to memory transfer sends the specified amount of data from the source address to the destination.

.. code:: c

   struct axi_dma_transfer mem_transfer = {
       // Number of bytes to write/read
       no_of_bytes,
       // Transfer done flag
       0,
       // Signal transfer mode
       NO,
       // Address of data source
       (uintptr_t)src_address_mem,
       // Address of data destination
       (uintptr_t)dest_address_mem,
       // Address of data destination
   };

   /* Transfer the data. */
   axi_dmac_transfer_start(mem_dmac, &mem_transfer);

   /* Wait until transfer finishes */
   status = axi_dmac_transfer_wait_completion(mem_dmac, timeout);
   if(status)
       return status;

.. _note-2:

Note
^^^^

-  After each DMA transfer, the program has to invalidate the cache for the associated data.

.. code:: c

   /* Invalidate cache data. Example for a Xilinx platform. */
   Xil_DCacheInvalidateRange((uintptr_t)dest_address_mem, no_of_bytes);

Code Documentation
------------------

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `AXI DMAC IP Core Header file <http://analogdevicesinc.github.io/no-OS/axi__dmac_8h.html>`_
-  `AXI DMAC IP Core Source file <http://analogdevicesinc.github.io/no-OS/axi__dmac_8c.html>`_

Source Code
-----------

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of AXI DMAC IP Core Driver.|

   -  |\|Header of the AXI DMAC IP Core Driver.|
   


.. |Implementation of AXI DMAC IP Core Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/axi_core/axi_dmac/axi_dmac`.c
.. |\|Header of the AXI DMAC IP Core Driver.| image:: :git-no-OS:`drivers/axi_core/axi_dmac/axi_dmac`.h
