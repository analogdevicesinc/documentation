AD6676-EBZ Bare Metal Quick Start Guide
=======================================

Downloads
---------

.. admonition:: Download
   :class: download

   No-OS:

   
   -  AD6676-EBZ Main Driver - :git-no-OS:`no-OS/tree/main/projects/ad6676-ebz <projects/ad6676-ebz>`
   -  Xilinx Platform Drivers - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/platform_drivers <legacy/common_drivers/platform_drivers>`
   -  AD6676 Driver - :git-no-OS:`no-OS/tree/main/drivers/adc/ad6676 <drivers/adc/ad6676>`
   -  ADC Core Driver - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/adc_core <legacy/common_drivers/adc_core>`
   -  DMAC Core Driver - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/dmac_core <legacy/common_drivers/dmac_core>`
   -  JESD204B Core Driver - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/jesd_core <legacy/common_drivers/jesd_core>`
   -  Transceiver Core Driver - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/xcvr_core <legacy/common_drivers/xcvr_core>`
   -  Transceiver Modules Drivers - :git-no-OS:`no-OS/tree/main/legacy/common_drivers/xcvr_core/xcvr_modules <legacy/common_drivers/xcvr_core/xcvr_modules>`
   
   HDL project:
   
   -  AD6676EVB HDL project - :git-hdl:`hdl/tree/main/projects/ad6676evb <projects/ad6676evb>`
   -  AD6676EVB HDL project documentation - https://analogdevicesinc.github.io/hdl/projects/ad6676evb/index.html
   

AD6676 Driver Description
-------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Function                                                                                                | Description                                                                                                            |
+=========================================================================================================+========================================================================================================================+
| ``int32_t ad6676_spi_read(struct ad6676_dev *dev, uint16_t reg_addr, uint8_t *reg_data);``              | SPI read from device.                                                                                                  |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_spi_write(struct ad6676_dev *dev, uint16_t reg_addr, uint8_t reg_data);``              | SPI write to device.                                                                                                   |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_splitreg(struct ad6676_dev *dev, uint32_t reg, uint32_t val);``             | SPI write a 16 bit register as two consecutive registers, LSB first.                                                   |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static inline int32_t ad6676_get_splitreg(struct ad6676_dev *dev, uint32_t reg, uint32_t *val);``     | SPI read from a 16 bit register as two consecutive registers, LSB first.                                               |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_fadc(struct ad6676_dev *dev, uint32_t val);``                               | Set ADC clock frequency.                                                                                               |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static inline uint32_t ad6676_get_fadc(struct ad6676_dev *dev);``                                     | Get the ADC clock frequency.                                                                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_set_fif(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``               | Set the target IF frequency.                                                                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``uint64_t ad6676_get_fif(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``              | Get the target IF frequency.                                                                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_bw(struct ad6676_dev *dev, uint32_t val);``                                 | Set the target BW frequency.                                                                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static inline uint32_t ad6676_get_bw(struct ad6676_dev *dev);``                                       | Get the target BW frequency.                                                                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_decimation(struct ad6676_dev *dev, struct ad6676_init_param *init_param);`` | Set decimation factor in the decimation mode register.                                                                 |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_clk_synth(struct ad6676_dev *dev, uint32_t refin_Hz, uint32_t freq);``      | Set the clock synthesizer to generate a specific frequency using a given refrence clock and do VCO and CP calibration. |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_set_extclk_cntl(struct ad6676_dev *dev, uint32_t freq);``                       | Enable external clock for the ADC.                                                                                     |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_jesd_setup(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``     | Setup JESD204 link parameters.                                                                                         |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_shuffle_setup(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``         | Setup shuffling rate and threshold for the adaptive shuffler.                                                          |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_calibrate(struct ad6676_dev *dev, uint32_t cal);``                              | Do internal calibration of JESD, ADC or flash.                                                                         |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_reset(struct ad6676_dev *dev, uint8_t spi3wire);``                              | Software reset all SPI registers to default value.                                                                     |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``static int32_t ad6676_outputmode_set(struct ad6676_dev *dev, uint32_t mode);``                        | Set output mode as twos complement or straight binary.                                                                 |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_set_attenuation(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``       | Set attenuation in decibels or disable attenuator.                                                                     |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_setup(struct ad6676_dev **device, struct ad6676_init_param init_param);``              | Initialize the device.                                                                                                 |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_update(struct ad6676_dev *dev, struct ad6676_init_param *init_param);``                | Reconfigure device for other target frequency and bandwidth and recalibrate.                                           |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``int32_t ad6676_test(struct ad6676_dev *dev, uint32_t test_mode);``                                    | Perform an interface test.                                                                                             |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

Make
----

.. note::

   See `resources/fpga/no-os_make/software_setup <https://wiki.analog.com/resources/fpga/no-os_make/software_setup>`_

GUI
---

.. include:: ../../../../fpga/xilinx/software_setup.rst
