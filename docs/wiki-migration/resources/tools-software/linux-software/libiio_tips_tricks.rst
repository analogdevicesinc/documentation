IIO System Considerations Tips & Tricks
=======================================

IIO context timeout (libiio)
----------------------------

-  May be triggered by low sample rates and large buffers
-  Long blocking calls (some calibration, profile load, etc.)

.. tip::

   Increase **iio_context_set_timeout()** timeout parameter or set to 0 to disables the timeout


Buffer handling, sizes and counts
---------------------------------

Typically set to a frame or chunk size suitable for signal processing (e.g. N x FFT_size)

-  Small buffers -> less latency but more overhead
-  Large buffers -> less overhead but more latency

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/internals/libiio_highspeed_interface.png
   :align: center
   :width: 400px

|

.. tip::

   \ **Number of discrete buffers are configurable, default is 4.**


   | Can change this using **iio_device_set_kernel_buffers_count()**\


|

.. tip::

   \ **Capturing starts as soon as the buffer is created!**

   | *iio_device_create_buffer()*\


.. tip::

   \ **FIFO like behavior new data is dropped in case it's not consumed fast enough!**\


IIO buffer DMA max block size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Max buffer size is limited by the max_block_size parameter

-  Default 16M
-  Can be adjusted

There are two ways to adjust the max block size

sysfs
^^^^^

Set via **/sys/module/industrialio_buffer_dma/parameters/max_block_size** in bytes

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      root@analog:~# **echo 67108864 > /sys/module/industrialio_buffer_dma/parameters/max_block_size**
      root@analog:~# **cat /sys/module/industrialio_buffer_dma/parameters/max_block_size**
      67108864
      root@analog:~# 
   


Kernel command line
^^^^^^^^^^^^^^^^^^^

Append the following to your kernel command line

-  **industrialio_buffer_dma.max_block_size=size_in_bytes**

Linux Contiguous Memory Allocator (or CMA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Allocation of big, physically-contiguous memory blocks
-  Reserve memory early at boot time
-  Kconfig menu "Device Drivers" -> "Generic Driver Options"-> "Contiguous Memory Allocator"
-  Kernel command line option cma=size_in_bytes
-  PlutoSDR default 256M

.. tip::

   Depending on your **IIO buffer DMA max block size** and **number of kernel buffer count** you may need to **CMA size**\


Capturing large contiguous buffers
----------------------------------

-  Set kernel buffer count to 1
-  Increase **IIO buffer DMA max block size** parameter to at least the size of your desired contiguous buffer
-  Make sure your CMA size is significantly bigger (CMA is used by various other DMA capable devices in your Linux system)
-  AXI_DMAC controller limits length of the transfers to 2**DMA_LENGTH_WIDTH. The default is 24 so your max transfer size is 16777216 bytes. You may need to increase that and rebuild your design. Please see here: :doc:`Synthesis Configuration Parameters </wiki-migration/resources/fpga/docs/axi_dmac>`
