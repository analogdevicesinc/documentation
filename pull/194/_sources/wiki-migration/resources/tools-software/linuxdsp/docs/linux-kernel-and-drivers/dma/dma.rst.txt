DMA Operations
==============

Introduction
------------

The Direct Memory Access (DMA) controller in the ADSP-SC5xx processor allows automated data transfers with minimal overhead for the core. DMA transfers can occur between any of the DMA capable peripherals (such as the SPORT or PPI) and the memory in L2 SRAM or external DDR.

Linux DMA Framework
-------------------

There are two aspects of the Linux DMA framework.

-  The generic Linux DMA mapping API
-  The DMA API for the SC5xx onchip DMA controller

Linux DMA Mapping API
~~~~~~~~~~~~~~~~~~~~~

Document: linux-kernel/Documentation/DMA-API-HOWTO.txt, Linux Device Driver (3rd) - chapter 15. API definition: linux-kernel/include/linux/dma-mapping.h, linux-kernel/arch/arm/include/asm/dma-mapping.h DMA operations allocate a buffer and pass bus addresses to your device. A DMA mapping is a combination of allocating a DMA buffer and generating an address for that buffer that is accessible by the device.

DMA mappings must also address the issue of cache coherency. Modern processors keep copies of recently accessed memory areas in a fast, local cache. Without this cache, reasonable performance is not possible. If your device changes an area of main memory it is imperative that any processor caches covering that area be invalidated. Otherwise the processor may work with an incorrect image of main memory and data corruption may result. Similarly, when your device uses DMA to read data from main memory any changes to that memory residing in processor caches must be flushed out first.

On SC5xx, DMA mapping is done in the same way as other ARM processors. dma_alloc_coherent() can be called to allocate a DMA buffer in the drivers. A block of 256k bytes DDR pool is reserved for DMA atomic, coherent usage while the normal coherent DMA memory is reserved from DDR without a size limit. New VM areas and page table entries of the allocated page structures are created with the uncacheable page attribute before the area address pointer is returned.

If you are writing a portable device driver, make sure to use the generic DMA APIs (for a full list please refer to the documentation):

::

   void *dma_alloc_coherent(struct device *dev, size_t size, dma_addr_t *dma_handle, gfp_t gfp);
    
   void dma_free_coherent(struct device *dev, size_t size, void *vaddr, dma_addr_t dma_handle);
    
   dma_addr_t dma_map_single(struct device *dev, void *ptr, size_t size, enum dma_data_direction dir)
    
   dma_addr_t dma_map_page(struct device *dev, struct page *page, unsigned long offset, size_t size, enum dma_data_direction dir)
    
   int dma_map_sg(struct device *dev, struct scatterlist *sg, int nents, enum dma_data_direction dir);
    

What is a bus address
~~~~~~~~~~~~~~~~~~~~~

When the CPU (say with the MMU turned off) wants to access physical memory it puts that address on its output pins. This a physical Address.

When a peripheral device wants to access the same physical memory (as in a DMA function) it may have to use a different address to get to the same physical location. This is a bus address.

So a bus address is the address used by a peripheral to access a certain physical address.

Generic DMA mapping guide
~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to the Linux kernel document DMA API HOWTO for details.

DMA APIs for SC5xx
------------------

The SC5xx processor offers a wide array of DMA capabilities.

-  44 Different DMA channels
-  Memory to Memory and IO to Memory Channel transfers
-  Dual X and Y indexing Address counters
-  Register base configuration
-  Flexible Descriptor Based Configuration
-  Memory interface supporting 8, 16, 32, 64, 128 and 256 bit data transfers
-  Peripheral interface supports 8, 16 and 32 bit data transfers
-  Interrupt on each DMA packet completion
-  Flexible DMA Priority

Flow Types and Descriptor
~~~~~~~~~~~~~~~~~~~~~~~~~

There are 6 different ways the DMA controller can be set up. These are called Flow types

-  FLOW_STOP - Stop after the current job
-  FLOW_AUTO - Autobuffer, Repeat the current transfer until stopped
-  FLOW_LIST - Use a linked list of descriptors
-  FLOW_ARRAY - Use a sequential list of descriptors
-  FLOW_LIST_DEMAND - Use a linked list of descriptors and fetch the next only after the DMA channel detects an incoming trigger event
-  FLOW_ARRAY_DEMAND - Use a sequential list of descriptors and fetch next only after the DMA channel detects an incoming trigger event

The flow type can be defined in a CONFIG word in a descriptor so the modes can be mixed and the operation quite complex.

Descriptors are used to control the DMA channel and allow a complex stream of data packets to be assembled if required.

-  Array Descriptor - Simple Sequential array of descriptors in memory
-  List Descriptor - Descriptors chained via address word in memory

For descriptor list mode, at a minimum the DMA_DSCPTR_NXT register must be written prior to write to the DMA_CFG register, which is the special action required to start the DMA channel. For descriptor array mode, at a minimum the DMA_DSCPTR_CUR register must be written prior to writing to the DMA_CFG register, which is the special action required to start the DMA channel.

One other slight complexity in the descriptor is the fact the DMA controller does not have to read ALL of the words in the descriptor array. The NDSIZE part of the CONFIG Register contains the number of elements to read into the DMA controller for this operation.

Descriptor Memory Layout
~~~~~~~~~~~~~~~~~~~~~~~~

List Descriptor:

::

   struct dmasg {
           void *next_desc_addr;
           unsigned long start_addr;
           unsigned long cfg;
           unsigned long x_count;
           long x_modify;
           unsigned long y_count;
           long y_modify;
   } __packed;

Array Descriptor:

::

   struct dma_desc_array {
           unsigned long start_addr;
           unsigned long cfg;
           unsigned long x_count;
           long x_modify;
   } __packed;
   === 2-D DMA ===
   2-D DMA can be roughly viewed as:

   /* Correct me if the boundary check is wrong */
   for ( ; Y_COUNT > 1; Y_COUNT--)
   {
     for ( ; X_COUNT > 1; X_COUNT--)
       DMAx_CURR_ADDR += X_MODIFY;
     DMAx_CURR_ADDR += Y_MODIFY;
   }

In some video application, 2-D DMA is more convenient to use than 1-D DMA.

MDMA Copy Wrapper for Linux Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an altrenative to setting up MDMA by yourself there exist APIs to use MDMA. See API implementation in arch/arm/mach-sc58x/dma.c or arch/arm/mach-sc57x/dma.c .

::

   dma_addr_t dma_memcpy(dma_addr_t pdest, const dma_addr_t psrc, size_t size)
   dma_addr_t safe_dma_memcpy(dma_addr_t pdest, const dma_addr_t psrc, size_t size)

DMA Operation for Linux Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please refer to: arch/arm/mach-sc58x/include/mach/dma.h, and arch/arm/mach-sc58x/dma.c or arch/arm/mach-sc57x/include/mach/dma.h, and arch/arm/mach-sc57x/dma.c.

The DMA channel management API:

::

   int request_dma(unsigned int channel, const char *device_id)
   void free_dma(unsigned int channel)
   void enable_dma(int channel)
   void disable_dma(int channel)

The extended DMA manipulation API allows for increased flexibility in SC5xx:

::

   unsigned long gen_dma_config2(char direction, char flow_mode, char intr_mode, char dma_mode, char mem_width, char syncmode, char peri_width)
   unsigned long gen_dma_config(char direction, char flow_mode, char intr_mode, char dma_mode, char mem_width, char syncmode)
   void set_dma_start_addr(unsigned int channel, unsigned long addr) 
   void set_dma_next_desc_addr(unsigned int channel, unsigned long addr) 
   void set_dma_x_count(unsigned int channel, unsigned short x_count) 
   void set_dma_x_modify(unsigned int channel, short x_modify) 
   void set_dma_y_count(unsigned int channel, unsigned short y_count) 
   void set_dma_y_modify(unsigned int channel, short y_modify) 
   void set_dma_config(unsigned int channel, unsigned short config)
   unsigned short set_bfin_dma_config(char direction, char flow_mode, char intr_mode, char dma_mode, char width) 
   unsigned short get_dma_curr_irqstat(unsigned int channel) 
   unsigned short get_dma_curr_xcount(unsigned int channel) 
   unsigned short get_dma_curr_ycount(unsigned int channel) 
   void set_dma_sg(unsigned int channel, struct dmasg_t *sg, int nr_sg) 
   void dma_disable_irq(unsigned int channel) 
   void dma_disable_irq_nosync(unsigned int channel)
   void dma_enable_irq(unsigned int channel)
   void clear_dma_irqstat(unsigned int channel)
   int set_dma_callback(unsigned int channel, dma_interrupt_t callback, void *data)

DMA Example
-----------

This is a simple DMA example taken from the adsp-spidac.c driver. This is getting 8-bit data from the SPI device int mybuffer.

::

   #define SPI0_RX_DMA_CH 23
   #define BUF_SIZE 1024 * 32
   static usigned char mybuffer[BUF_SIZE];
    
   int mydmatest(struct device *dev)
   {
       int ret;
       dma_addr_t dma_addr;
    
       // Ask for the DMA channel
       ret = request_dma(SPI0_RX_DMA_CH,"SPI RX Test");
       if ( ret < 0 ) {
           printk(" Unable to get SPI0 RX DMA channel\n");
           return 1;
       }
    
       // Turn off the DMA channel
       disable_dma(SPI0_RX_DMA_CH);
    
       // Set the IRQ callback
       set_dma_callback(SPI0_RX_DMA_CH, myirq, mydata);
    
       // Map the memory for DMA device access
       dma_addr = dma_map_single(dev, mybuffer, BUF_SIZE, DMA_FROM_DEVICE);
       if (dma_mapping_error(dev, dma_handle)) {
           free_dma(SPI0_RX_DMA_CH);
           printk(" Unable to map DMA region\n");
           return 1;
       }
    
       // Set up the dma config
       // WNR We are going to write to memory
       // RESTART throw away any old data in the fifo
       // Enable Interrupts
       set_dma_config(SPI0_RX_DMA_CH, ( WNR | RESTART

       | DI_EN ));
    
       // Set address to drop data into
       set_dma_start_address(SPI0_RX_DMA_CH, dma_addr);
    
       // Set the transfer size in bytes
       set_dma_x_count(SPI0_RX_DMA_CH,size);
    
       // Set the X modify ( dont worry about Y for this one )
       set_dma_x_modify(SPI0_RX_DMA_CH,1);
    
       // Off we go
       enable_dma(SPI0_RX_DMA_CH);
   }

The IRQ routine could look like this. It simply clears the IRQ status.

::

   static irqreturn_t myirq( int irq, void *data)
   {
       unsigend short mystat;
       struct device *dev = (struct device*)data;
    
      mystat = get_dma_curr_irqstat(SPI0_RX_DMA_CH);
       clear_dma_irqstat(SPI0_RX_DMA_CH);
    
       // Unmap the DMA memory for processor access
       dma_unmap_single(dev, mybuffer, BUF_SIZE, DMA_TO_DEVICE);
       free_dma(SPI0_RX_DMA_CH);
     
       wake_up_interruptible(&mywaiting_task);
    
       return IRQ_HANDLED;
   }

|

| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
