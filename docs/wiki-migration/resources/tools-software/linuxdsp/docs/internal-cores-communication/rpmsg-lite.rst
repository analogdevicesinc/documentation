RPMsg-Lite
==========

Introduction
------------

RPMsg is used to transfer messages between cores on ADSP devices. An implementation is available for ARM when running Linux and for bare metal applications a port of RPMsg-Lite is available for ARM and SHARC+ cores. It allows for transmitting a message to a specific endpoint on a different core via a dedicated transport link. Multiple endpoints can be registered against a single link.

This page describes how to use RPMsg-Lite for bare metal applications.

Additional information can be found here: https://github.com/analogdevicesinc/rpmsg-lite

Resources used
~~~~~~~~~~~~~~

In order to allow for message transmission between cores on ADSP-SC5xx devices RPMsg-Lite makes use of the following resources:

-  Shared memory for storing message buffers and vring buffers containing message descriptors
-  Interrupt on each core to indicate that a message has arrived
-  TRU triggers for raising an interrupt on a different core

.. note::

   These resources should not be used for other purposes when using RPMsg-Lite in your application.


The interrupts used are:

::

   TRGS_TRU0_IRQ3      /* ARM */
   TRGS_TRU0_IRQ7      /* SHARC0 */
   TRGS_TRU0_IRQ11     /* SHARC1 */

The TRU triggers allocated are:

::

   TRGM_SOFT3          /* Signal ARM */
   TRGM_SOFT4          /* Signal SHARC0 */
   TRGM_SOFT5          /* Signal SHARC1 */

The shared memory used is allocated by a single core and typically by the main core in an RPMsg-Lote context. In order for the remotes to know the physical addresses for the vring buffers in shared memory this information has to be passed from the main to the remote before the framework can be used. This is achieved by the main populating a resource table at a known address. The `examples <https://wiki.analog.com/rpmsg-lite>`_ utilise memory located at \_\__MCAPI_common_start. If using a different location for this make sure that the memory area used is uncached.

For the sake of compatibility the resource table used in the `examples <https://wiki.analog.com/rpmsg-lite>`_ has an identical structure to the one created by remoteproc in Linux which looks as follows:

::

   struct sharc_resource_table {
       struct resource_table table_hdr;
       unsigned int offset[1];
       struct fw_rsc_vdev rpmsg_vdev;
       struct fw_rsc_vdev_vring vring[2];
   };

   struct adi_resource_table {
       uint8_t tag[16];
       uint32_t version;
       uint32_t initialized;
       uint32_t reserved[8];
       struct sharc_resource_table tbl;
   };

.. note::

   Additional detail can be found at :git-rpmsg-lite:`release/yocto-2`.1.0/lib/include/remoteproc.h\


   | 

Using RPMsg-Lite on SC5xx
-------------------------

Allocate memory for vring buffers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The memory allocation for for the vring buffers should be done on a single core and the location of those buffers shared with the other cores via a resource table. To ensure that the cores pick up the data from the shared memory it is necessary to mark the memory as uncached on all cores using the buffers. Allocating memory and ensuring it is uncached is done differently on ARM and SHARC. If using RPMsg-Lite on the ARM it is recommended that the memory is allocated on the ARM as the SHARCs allow for simple run-time changes to caching via a set of registers.

Create an array for the vring buffers on the heap.

::

   uint8_t vring_buffer[ADI_VRING_BUFFER_SIZE];

|

Disable cache on ARM
^^^^^^^^^^^^^^^^^^^^

Disabling cache on the ARM for the vring buffers requires changes to the linker files.

Example for allocating 4MB of L3 memory as uncached memory on an SC594:

Modify apt.c:

Add a definition for an uncached block of memory and adjust the block of memory from which it is taken from

Change:

::

   { 0xA0000000u, 0xBFFFFFFFu, ADI_MMU_WB_CACHED           }, /* 512MB DDR-A */

To:

::

   { 0xA0000000u, 0xA03FFFFFu, ADI_MMU_RW_UNCACHED         }, /* 4MB DDR-A */
   { 0xA0400000u, 0xBFFFFFFFu, ADI_MMU_WB_CACHED           }, /* 508MB DDR-A */

Modify app.ld:

Add a definition for an uncached block of memory and adjust the block of memory from which it is taken from matching the changes maed to apt.c

Change:

::

   /* ARM Core 0 L3, DMC0 */
   MEM_L3 : ORIGIN = 0xA0000000, LENGTH = 512M

To:

::

   /* ARM Core 0 L3, DMC0 */
   MEM_L3_UNCACHED : ORIGIN = 0xA0000000, LENGTH = 4M
   MEM_L3 : ORIGIN = 0xA0400000, LENGTH = 508M

Add an entry in the SECTIONS covering L3 memory:

::

   /* L3 Uncached Memory. No data placed here by default */
   .l3_uncached :
   {
     *(.l3_data_uncached)
   } >MEM_L3_UNCACHED = 0

To store the vring buffers previously declared in the uncached memory block use \__attribute\_\_ to specify the memory section it should be mapped to.

::

   __attribute__ ((section (".l3_data_uncached")))
   uint8_t vring_buffer[ADI_VRING_BUFFER_SIZE];

   | 

Disable cache on SHARC
^^^^^^^^^^^^^^^^^^^^^^

The SHARCs have a number of range registers allowing for sections of memory to be marked as uncached. We make use of these to mark the descriptor buffer range and the message buffer range as uncached like in the following example

::

       // Disable cache for the descriptors memory range
       status = adi_cache_set_range ((void *)vring_buffer,
                           (void *)(vring_buffer + ADI_VRING_BUFFER_SIZE),
                           adi_cache_rr6,
                           adi_cache_noncacheable_range);

If the SHARC is acting as an RPMsg-Lite remote the ranges to mark as uncached are retrieved from the resource table.

|

Create Resource Table
~~~~~~~~~~~~~~~~~~~~~

On the core on which the memory for the vring buffers was declared create the resource table used to provide information on the shared memory resources used for RPMsg-lite and instruct the linker to store it at a fixed location in L2 memory which is by default marked as uncached.

::

   RL_PACKED_BEGIN
   struct sharc_resource_table {
       struct resource_table table_hdr;
       unsigned int offset[1];
       struct fw_rsc_vdev rpmsg_vdev;
       struct fw_rsc_vdev_vring vring[2];
   }RL_PACKED_END;

   RL_PACKED_BEGIN
   struct adi_resource_table {
       uint8_t tag[16];
       uint32_t version;
       uint32_t initialized;
       uint32_t reserved[8];

       struct sharc_resource_table tbl;
   }RL_PACKED_END;

   const struct adi_resource_table rsc_tbl_local = {
           .tag = "AD-RESOURCE-TBL",
           .version = 1,
           .initialized = 0,
           .tbl.table_hdr = {
               /* resource table header */
               1,          /* version */
               1,          /* number of table entries */
               {0, 0,},    /* reserved fields */
           },
           .tbl.offset = {offsetof(struct sharc_resource_table, rpmsg_vdev),
           },
           .tbl.rpmsg_vdev = {RSC_VDEV, /* virtio dev type */
               7,              /* it's rpmsg virtio */
               1,              /* kick sharc0 */
               /* 1<<0 is VIRTIO_RPMSG_F_NS bit defined in virtio_rpmsg_bus.c */
               1<<0, 0, 0, 0,  /* dfeatures, gfeatures, config len, status */
               2,              /* num_of_vrings */
               {0, 0,},        /* reserved */
           },
           .tbl.vring = {
               {(uint32_t)-1, VRING_ALIGN, RL_BUFFER_COUNT, 1, 0}, /* da allocated by rpmsg_lite_master_init */
               {(uint32_t)-1, VRING_ALIGN, RL_BUFFER_COUNT, 1, 0}, /* da allocated by rpmsg_lite_master_init */
           },
   };

   /*
     * Declare the resource table used for sharing shmem vring details.
     * The ___MCAPI_common_start address is defined in app.ldf
    */
   extern struct adi_resource_table __MCAPI_common_start;
   volatile struct adi_resource_table *adi_resource_table;
   volatile struct sharc_resource_table *resource_table;

   | 

Adding an rpmsg-lite instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently the rpmsg-lite port for ADSP devices only supports static context instances.

Create a header file named "rpmsg_config.h" and define RL_USE_STATIC_API. RPMsg-Lite will attempt to include this header file during build.

::

   #define RL_USE_STATIC_API (1)

Create the static RPMsg-Lite instance.

::

   struct rpmsg_lite_instance rpmsg_SHARC_channel;

The instance makes use of a Link ID to determine which core the instance should connect to.

::

   /* Link IDs to use on ARM core */
   #define RL_PLATFORM_ARM_SHARC0_LINK_ID (0U)  /* Link between ARM and SHARC0 */
   #define RL_PLATFORM_ARM_SHARC1_LINK_ID (1U)  /* Link between ARM and SHARC1 */

   /* Link IDs to use on a SHARC core */
   #define RL_PLATFORM_SHARC_ARM_LINK_ID (0U)   /* Link between SHARC and ARM */
   #define RL_PLATFORM_SHARC_SHARC_LINK_ID (1U) /* Link between SHARC and SHARC */

Initialize the RPMsg-Lite instance on the main core.

::

   rpmsg_instance = rpmsg_lite_master_init(
           (void*)vring_buffer,
           ADI_VRING_BUFFER_SIZE,
           RL_PLATFORM_ARM_SHARC0_LINK_ID,
           RL_SHM_VDEV,
           &rpmsg_SHARC_channel);

Populate the resource table with the addresses of the vrings created by rpmsg_lite_master_init and signal the remote core that the resource table has been initialised

::

   adi_resource_table = (struct adi_resource_table *)
       ((uint32_t)&__MCAPI_common_start);
   memcpy((void*)adi_resource_table, (const void*)&rsc_tbl_local, sizeof(struct adi_resource_table));

   resource_table = &adi_resource_table->tbl;
   resource_table->vring[0].da = (uint32_t) rpmsg_instance->rvq->vq_ring_mem;
   resource_table->vring[1].da = (uint32_t) rpmsg_instance->tvq->vq_ring_mem;
   resource_table->rpmsg_vdev.status = 7;

On the remote side the instance is initialized as follows

::

   rpmsg_instance = rpmsg_lite_remote_init(
           (void*)&resource_table_arm->rpmsg_vdev,
           RL_PLATFORM_SHARC_ARM_LINK_ID,
           RL_SHM_VDEV,
           &rpmsg_ARM_channel);

|

Adding an endpoint
^^^^^^^^^^^^^^^^^^

A unique endpoint is determined by a uint32 address.

Create the static context for the endpoint.

::

   struct rpmsg_lite_ept_static_context sharc_ping_endpoint_context;

Create a callback function for handling messages received for the endpoint

::

   int32_t sharc_ping_call_back(void *payload, uint32_t payload_len, uint32_t src, void *priv) {
       printf("Received a ping from SHARC0\n");
       return RL_RELEASE;
   }

Create an endpoint

::

   uint32_t addr = ARM_EP_ADDR;

   rpmsg_ept = rpmsg_lite_create_ept(
           &rpmsg_SHARC_channel,
           addr,
           &sharc_ping_call_back,
           NULL,
           &sharc_ping_endpoint_context);

           | 

Sending a message
^^^^^^^^^^^^^^^^^

In order to send a message the recipient endpoint address must be known.

::

   uint32_t remote_addr = SHARC0_EP_ADDR;
   char msg[] = "ping";
   uint32_t len = 4;

   return rpmsg_lite_send(
           &rpmsg_SHARC_channel,
           &sharc_ping_endpoint_context.ept,
           remote_addr,
           msg, len, 0);

|

Additional information
----------------------

https://github.com/analogdevicesinc/rpmsg-lite

Downloads
~~~~~~~~~

RPMsg-Lite for ADSP devices is available for Bare-Metal applications running on SHARC+, ARM A5 and ARM A55 here: https://github.com/analogdevicesinc/rpmsg-lite. To guarantee compatibility use the same version of RPMsg-Lite on all cores. If running Linux on the ARM use the RPMsg-Lite version matching the Yocto Linux release version running on the ARM.

Examples
~~~~~~~~

https://github.com/analogdevicesinc/lnxdsp-examples
