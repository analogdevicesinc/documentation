FPGA Peripherals
================

-  CN0363 - Cores used by the :doc:`EVAL-CN0363-PMDZ HDL reference design </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz>`

   -  :doc:`CN0363 Phase Data Sync </wiki-migration/resources/fpga/peripherals/cn0363/phase_data_sync>` - Align ADC conversion result data and phase information
   -  :doc:`CN0363 DMA Sequencer </wiki-migration/resources/fpga/peripherals/cn0363/sequencer>` - Sequence data channels to the DMA

-  :doc:`SPI Engine </wiki-migration/resources/fpga/peripherals/spi_engine>` - SPI-Engine framework

   -  :doc:`Execution Module </wiki-migration/resources/fpga/peripherals/spi_engine/engine>` - Main module which processes a SPI engine command stream and implements the SPI bus interface logic
   -  :doc:`AXI Interface Module </wiki-migration/resources/fpga/peripherals/spi_engine/axi>` - Memory mapped software accessible interface to a SPI Engine command stream and/or offload cores
   -  :doc:`Offload Module </wiki-migration/resources/fpga/peripherals/spi_engine/offload>` - Stores a SPI Engine command stream, execution is triggered by an external event
   -  :doc:`Interconnect Module </wiki-migration/resources/fpga/peripherals/spi_engine/interconnect>` - Connects multiple SPI Engine command streams to a SPI Engine execution module

-  :doc:`Sigma-Delta SPI Util </wiki-migration/resources/fpga/peripherals/util_sigma_delta_spi>` - Helper module for interfacing ADCs from the Analog Devices Sigma-Delta family
