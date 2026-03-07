AD6676-EBZ Bare Metal Quick Start Guide
=======================================

Downloads
---------

.. admonition:: Download
   :class: download

   No-OS:

   
   -  AD6676-EBZ Main Driver - :git-no-OS:`projects/ad6676-ebz`
   -  Xilinx Platform Drivers - :git-no-OS:`legacy/common_drivers/platform_drivers`
   -  AD6676 Driver - :git-no-OS:`drivers/adc/ad6676`
   -  ADC Core Driver - :git-no-OS:`legacy/common_drivers/adc_core`
   -  DMAC Core Driver - :git-no-OS:`legacy/common_drivers/dmac_core`
   -  JESD204B Core Driver - :git-no-OS:`legacy/common_drivers/jesd_core`
   -  Transceiver Core Driver - :git-no-OS:`legacy/common_drivers/xcvr_core`
   -  Transceiver Modules Drivers - :git-no-OS:`legacy/common_drivers/xcvr_core/xcvr_modules`
   
   HDL project:
   
   -  AD6676EVB HDL project - :git-hdl:`projects/ad6676evb`
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

::

    * Open Xilinx Software Development Kit (XSDK) and provide the workspace location.

::

    * Create a new Application Project: go to **File -> New -> Application Project**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_app_project.png
   :alt: Creating a new application project
   :align: center
   :width: 650px

::

    * Create a new Hardware Platform: click **New** from the **Target Hardware** section

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_new_hardware.png
   :alt: Creating a new hardware platform
   :align: center
   :width: 450px

::

    * Specify the already generated Hardware Platform Specification File (more details about the generation: :doc:`/wiki-migration/resources/fpga/docs/build`): in the **Target Hardware Specification** section browse the desired file

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_hw_project.png
   :alt: Import hardware description file
   :align: center
   :width: 450px

::

    * Give a name to the project and to the board support package and click **Next**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_app_project.png
   :alt: Application project settings
   :align: center
   :width: 450px

::

    * Select the **Empty Application** templeta and click **Finish**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/project_templates.png
   :alt: Choose application template
   :align: center
   :width: 450px

::

    * The new **Empty Application project** should look like:


    |Empty application project|

.. important::

   Some applications (e.g. FMCOMMSx), when a Microblaze processor is used, requires an increased HEAP size for dynamic memory allocation. Make sure the HEAP size is at least **0x100000**.


   |image1|

::

    * Copy the source code files into the **src** directory
    * Make sure you uncomment the the required carrier vendor and CPU architecture from the **app_config.h** (or **config.h**) header file.

-  Example for choosing the Altera carrier in the **app_config.h** header file:

::

   //#define XILINX
   #define ALTERA

::

    * If there are multiple folders present in in the src one, include all the paths of the folders: go to the settings of the project and in the **C/C++ Build -> Settings -> Tool Settings -> gcc compiler -> Directories** section and add the paths of all the folders.

::

    * The SDK should automatically build the projects and the Console window will display the result of the build. If the build is not done automatically select the **Project -> Build Automatically** menu option.
     
    * At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system. You can program the FPGA by clicking on **Xilinx Tools -> Program FPGA** 

::

    * After the FPGA was programmed, we need to create a new Run configuration, by selecting **Run** -> **Run Configurations...**, in the Run Configuration windows select the Xilinx C/C++ application (System Debugger) and click at the **New Configuration** button at the upper left corner.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_run_configurations.png
   :alt: Create new run configuration
   :align: center
   :width: 650px

::

    * If your target carrier has a Zync SoC, make sure, that you specify the **Initialization file**, and select the **Run ps7_init** and **Run ps7_post_config** options.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/zynq_init_file.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

    * At the **Application** tab define your current project name and application executable. (.elf)

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/elf_app.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

       * The output of the example program can be viewed in the SDK console by enabling the Connect STDIO Console option and setting the baud rate of the UART port to 115200.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/stdio_config.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

       * As an alternative a UART terminal can be used to capture the output of the example program. The number of used UART port depends on the computer's configuration. The following settings must be used in the UART terminal:
       * **Baud Rate:** 115200bps
       * **Data:** 8 bit
       * **Parity:** None
       * **Stop bits:** 1 bit
       * **Flow Control:** none

::

     * When the run configuration is done, the software can be started by clicking the **Run** button.

::

     * Your new bare metal application should run  

.. |Empty application project| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/empty_project.png
   :width: 650px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/ad9361_no_os_microblaze_heap_size.png

