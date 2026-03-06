No-OS DMA API
=============

Description
-----------

TBD

Documentation
-------------

TBD

DMA Initial Parameters
----------------------

TBD

Structure Definition
~~~~~~~~~~~~~~~~~~~~

TBD

Parameters Description
~~~~~~~~~~~~~~~~~~~~~~

TBD

DMA Descriptor
--------------

.. _structure-definition-1:

Structure Definition
~~~~~~~~~~~~~~~~~~~~

TBD

.. _parameters-description-1:

Parameters Description
~~~~~~~~~~~~~~~~~~~~~~

TBD

DMA APIs
--------

TBD

.. _structure-definition-2:

Structure Definition
~~~~~~~~~~~~~~~~~~~~

TBD

APIs description
~~~~~~~~~~~~~~~~

TBD

DMA Supported Platforms
-----------------------

MAXIM Platform
~~~~~~~~~~~~~~

TBD

STM32 Platform
~~~~~~~~~~~~~~

The timer driver documentation for STM32 platform can be found here:

-  `Header file for STM32 DMA driver <http://analogdevicesinc.github.io/no-OS/doxygen/stm32__dma_8h.html>`__

-  `Source file for STM32 DMA driver <http://analogdevicesinc.github.io/no-OS/doxygen/stm32__dma_8c.html>`__

The definition of the extra DMA initialization parameters:

.. code:: C

   struct stm32_dma_init_param {
       /* DMA Channel descriptor */
       struct stm32_dma_channel *chn;
   };

Where chn is the channel specific descriptor

The defintion for the channel specific DMA initialization parameters:

.. code:: C

   struct stm32_dma_channel {
       /* DMA Handle */
       DMA_HandleTypeDef *hdma;
       /* Channel Number */
       uint32_t ch_num;
       /* Memory Increment */
       bool mem_increment;
       /* Peripheral Increment */
       bool per_increment;
       /* Memory Data Alignment */
       enum stm32_dma_data_alignment mem_data_alignment;
       /* Peripheral Data Alignment */
       enum stm32_dma_data_alignment per_data_alignment;
       /* DMA Mode */
       enum stm32_dma_mode dma_mode;
       /* Source Address for the data */
       uint8_t* src;
       /* Destination Address for the data */
       uint8_t* dst;
       /* Transfer length in Bytes */
       uint32_t length;
   };

Where

hdma is the channel specific DMA handle

ch_num is the channel number

mem_increment and per_increment are boolean values, that allows the user to configure the memory increment status

mem_data_alignment and per_data_alignment decide the direction of data flow for the channel of interest

dma_mode is the data buffer mode- circular or linear

src, dst are the source and destination addresses for the channel

length is the number of bytes per transfer

DMA Examples
------------

TBD
