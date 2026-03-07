AD7616 User Guide
=================

Overview
--------

The :adi:`AD7616` is a 16-bit, data acquisition system (DAS) that supports dual simultaneous sampling of 16 channels. The :adi:`AD7616` operates from a single 5 V supply and can accommodate ±10 V, ±5 V, and ±2.5 V true bipolar input signals while sampling at throughput rates up to 1 MSPS per channel pair with 90 dB SNR. Higher SNR performance can be achieved with the on-chip oversampling mode; 92 dB for an oversampling ratio of 2.

The input clamp protection circuitry can tolerate voltages up to ±20 V. The :adi:`AD7616` has 1 MΩ analog input impedance regardless of sampling frequency. The single supply operation, on-chip filtering, and high input impedance eliminate the need for driver op-amps and external bipolar supplies.

Each device contains analog input clamp protection, a dual, 16-bit charge redistribution successive approximation analog-to-digital converter (ADC), a flexible digital filter, a 2.5 V reference and reference buffer, and high-speed serial and parallel interfaces.

Applications:

-  Powerline monitoring
-  Protective relays
-  Multiphase motor control
-  Instrumentation and control systems
-  Data acquisition systems (DAS)

Supported Devices
~~~~~~~~~~~~~~~~~

-  :adi:`AD7616`

Evaluation Boards
~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-AD7616`

Supported Carriers
~~~~~~~~~~~~~~~~~~

-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `ZedBoard <https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html>`_
-  :adi:`SDP-K1`

Other required hardware
~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`SDP-I-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-SDP-I-FMC.html>` when using Zedboard
-  `STLINK-V3 <https://www.st.com/en/development-tools/stlink-v3set.html>`_ when using SDP-K1

Zedboard setup
--------------

EVAL-AD7616 Jumper setup
~~~~~~~~~~~~~~~~~~~~~~~~

================== ========= ====================================
Jumper/Solder link Position  Description
================== ========= ====================================
SL1                Unmounted Channel Sequencer Enable
SL2                Unmounted RC Enable Input
SL3                Mounted   Selects 2 MISO mode
SL4                Unmounted Oversampling Ratio Selection OS2
SL5                Mounted   If mounted, selects serial interface
SL6                Unmounted Oversampling Ratio Selection OS1
SL7                Unmounted Oversampling Ratio Selection OS0
LK40               A         Onboard 5v0 power supply selected
LK41               A         Onboard 3v3 power supply selected
================== ========= ====================================

Block Diagrams
~~~~~~~~~~~~~~

-  AD7616_SDZ using the **SERIAL** interface

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7616_serial_hdl.svg
   :alt: AD7616_SDZ with Serial Interface
   :width: 800px

-  AD7616_SDZ using the **PARALLEL** interface

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7616_parallel_hdl.svg
   :alt: AD7616_SDZ with Parallel Interface
   :width: 800px

Required software
~~~~~~~~~~~~~~~~~

-  We're upgrading the Xilinx tools on every release. The supported version number can be found in our :git-hdl:`git repository <releases>`.
-  An UART terminal (Tera Term/Hyperterminal), baud rate set to 115200.

Using the HDL reference design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design in general.

In the :doc:`axi_ad7616's </wiki-migration/resources/fpga/docs/axi_ad7616>` wiki page, can be found a detailed description of the core.

The data path of the HDL design is simple as follows:

-  the parallel interface is controlled by the axi_ad7616 IP core
-  the serial interface is controlled by the SPI Engine Framework
-  data is written into memory by a DMA (axi_dmac core)
-  all the control pins of the device are driven by GPIO's

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Choose the required interface (see caption **Switching between interface types**)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

Switching between interface types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before the board power-up, the user has to choose the required device interface and setup. Depending on the required interface mode, some hardware modifications need to be done on the board and/or Tcl script:

In case of the **SERIAL** interface:

.. code:: c

   $ make SER_PAR_N=1

In case of the **PARALLEL** interface:

.. code:: c

   $ make SER_PAR_N=0

.. important::

   Because of the **SDP-I-FMC** the level of the **VADJ** in the carrier board needs to be set to **3.3V**.


CPU/Memory interconnects addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===================== ==========
Instance              Address
===================== ==========
axi_ad7616_dma        0x44a30000
ad7616_pwm_gen        0x44b00000
spi_ad7616_axi_regmap 0x44a00000
axi_ad7616            0x44a80000
===================== ==========

Note:

-   spi_ad7616 is instantiated only for SER_PAR_N=1
-   axi_ad7616 is instantiated only for SER_PAR_N=0

PL Interrupts
^^^^^^^^^^^^^

============== ============= ===================
Instance       HDL interrupt Linux PsU interrupt
============== ============= ===================
---            0             89
---            1             90
---            2             91
---            3             92
---            4             93
---            5             94
---            6             95
---            7             96
---            8             104
---            9             105
axi_ad7616     10            106
---            11            107
spi_ad7616     12            108
axi_ad7616_dma 13            109
---            14            110
---            15            111
============== ============= ===================

Note:

-   spi_ad7616 is instantiated only for SER_PAR_N=1
-   axi_ad7616 is instantiated only for SER_PAR_N=0

GPIO signals
^^^^^^^^^^^^

Ps7 EMIO offset = 54

============= ===== ==============
GPIO Signal   GPIO  HDL GPIO EMIOn
============= ===== ==============
adc_reset_n   97    43
adc_hw_rngsel 96-95 42-41
adc_os        94-92 40-38
adc_seq_en    91    37
adc_burst     90    36
adc_chsel     89-87 35-33
adc_crcen     86    32
============= ===== ==============

Create the SDK Project
~~~~~~~~~~~~~~~~~~~~~~

To run the application the user has to create an **Empty Application Project** using Xilinx SDK, and have to copy all the :git-no-OS:`design sources <projects/ad7616-sdz/src>` to the **sw** directory. (see :doc:`SDK Software Setup </wiki-migration/resources/fpga/xilinx/software_setup>` for more detailed instructions). In order to build the No-OS project, refer to the :doc:`No-OS build guide </wiki-migration/resources/no-os/build>`.

HDL Downloads
~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -


   
   |AD7616-SDZ HDL Project.|

No-OS Downloads
~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -


   
   |AD7616-SDZ No-OS Project.|

SDP-K1 setup
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7616_sdp-k1_setup.jpg
   :align: center
   :width: 800px

:adi:`EVAL-AD7616` is connected to :adi:`SDP-K1` via fly-wire. In order to flash the SDP-K1, an `STLINK-V3 <https://www.st.com/en/development-tools/stlink-v3set.html>`_ is required

.. warning::

   Make sure to power both :adi:`EVAL-AD7616` and :adi:`SDP-K1` via the barrel jack connector


.. _eval-ad7616-jumper-setup-1:

EVAL-AD7616 Jumper setup
~~~~~~~~~~~~~~~~~~~~~~~~

================== ========= ====================================
Jumper/Solder link Position  Description
================== ========= ====================================
SL1                Unmounted Channel Sequencer Enable
SL2                Unmounted RC Enable Input
SL3                Unmounted Selects 1 MISO mode
SL4                Unmounted Oversampling Ratio Selection OS2
SL5                Mounted   If mounted, selects serial interface
SL6                Unmounted Oversampling Ratio Selection OS1
SL7                Unmounted Oversampling Ratio Selection OS0
LK40               A         Onboard 5v0 power supply selected
LK41               A         Onboard 3v3 power supply selected
================== ========= ====================================

Fly-wire connection
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------+
| :adi:`EVAL-AD7616`                                   | :adi:`SDP-K1` Arduino                              |
+------------------------------------------------------+----------------------------------------------------+
| SCLK                                                 | D13                                                |
+------------------------------------------------------+----------------------------------------------------+
| DB10/SDI                                             | D11                                                |
+------------------------------------------------------+----------------------------------------------------+
| DB12/SDOA                                            | D12                                                |
+------------------------------------------------------+----------------------------------------------------+
| CS                                                   | D10                                                |
+------------------------------------------------------+----------------------------------------------------+
| CONVST                                               | D5                                                 |
+------------------------------------------------------+----------------------------------------------------+
| RESET                                                | D7                                                 |
+------------------------------------------------------+----------------------------------------------------+
| BUSY                                                 | D6                                                 |
+------------------------------------------------------+----------------------------------------------------+

.. _no-os-downloads-1:

No-OS Downloads
~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -


   
   |AD7616-ST No-OS Project.|

No-OS project build
~~~~~~~~~~~~~~~~~~~

To build the project, just run:

.. code:: c

   $ make

To flash, run:

.. code:: c

   $ make run

The project provides an iio device over the serial interface. The baudrate used is 230400. You can use the :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>` to view the captured data.

For further details, refer to the :doc:`No-OS build guide </wiki-migration/resources/no-os/build>`.

No-OS Driver Description
------------------------

Each setup have its own project but they there one common :git-no-OS:`driver <drivers/adc/ad7616>`

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Function                                                                                                                              | Description                                                       |
+=======================================================================================================================================+===================================================================+
| ``int32_t ad7616_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data);``                                                       | SPI read from device.                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data);``                                                       | SPI write to device.                                              |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_read_mask(ad7616_dev *dev, uint8_t reg_addr, uint16_t mask, uint16_t *data);``                                       | SPI read from device using a mask.                                |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_write_mask(ad7616_dev *dev, uint8_t reg_addr, uint16_t mask, uint16_t data);``                                       | SPI write to device using a mask.                                 |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_spi_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data);``                                                   | SPI read from device.                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_spi_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data);``                                                   | SPI write to device.                                              |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_par_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data);``                                                   | PAR read from device.                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_par_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data);``                                                   | PAR write to device.                                              |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_reset(ad7616_dev *dev);``                                                                                            | Perform a full reset of the device.                               |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_set_range(ad7616_dev *dev, ad7616_ch ch, ad7616_range range);``                                                      | Set the analog input range for the selected analog input channel. |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_set_mode(ad7616_dev *dev, ad7616_mode mode);``                                                                       | Set the operation mode (software or hardware).                    |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_set_oversampling_ratio(ad7616_dev *dev, ad7616_osr osr);``                                                           | Set the oversampling ratio.                                       |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_read_data_serial(struct ad7616_dev *dev, struct ad7616_conversion_result *results, uint32_t samples);``              | Read data in serial mode.                                         |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_setup(ad7616_dev **device, adc_core *core, ad7616_init_param init_param);``                                          | Initialize the device.                                            |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_read_channel_source(struct ad7616_dev *dev, enum ad7616_ch *ch_a, enum ad7616_ch *ch_b);``                           | Read currently selected channel input sources.                    |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_select_channel_source(struct ad7616_dev *dev, enum ad7616_ch ch);``                                                  | Select the input source for a channel.                            |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_setup_sequencer(struct ad7616_dev *dev, struct ad7616_sequencer_layer *layers, uint32_t layers_nb, uint8_t burst);`` | Setup sequencer with given layers.                                |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| ``int32_t ad7616_disable_sequencer(struct ad7616_dev *dev);``                                                                         | Disable the sequencer.                                            |
+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Types Declarations
~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------+


| ``enum ad7616_mode {                                                         |

|     AD7616_SW,                                                               |
|     AD7616_HW,                                                               |
| };                                                                           |
|                                                                              |
| enum ad7616_interface {                                                      |
|     AD7616_SERIAL,                                                           |
|     AD7616_PARALLEL,                                                         |
| };                                                                           |
|                                                                              |
| enum ad7616_ch {                                                             |
|     AD7616_VA0,                                                              |
|     AD7616_VA1,                                                              |
|     AD7616_VA2,                                                              |
|     AD7616_VA3,                                                              |
|     AD7616_VA4,                                                              |
|     AD7616_VA5,                                                              |
|     AD7616_VA6,                                                              |
|     AD7616_VA7,                                                              |
|     AD7616_VA_VCC,                                                           |
|     AD7616_VA_ALDO,                                                          |
|     AD7616_VA_RESERVED1,                                                     |
|     AD7616_VA_SELF_TEST,                                                     |
|     AD7616_VA_RESERVED2,                                                     |
|     AD7616_VB0,                                                              |
|     AD7616_VB1,                                                              |
|     AD7616_VB2,                                                              |
|     AD7616_VB3,                                                              |
|     AD7616_VB4,                                                              |
|     AD7616_VB5,                                                              |
|     AD7616_VB6,                                                              |
|     AD7616_VB7,                                                              |
|     AD7616_VB_VCC,                                                           |
|     AD7616_VB_ALDO,                                                          |
|     AD7616_VB_RESERVED1,                                                     |
|     AD7616_VB_SELF_TEST,                                                     |
|     AD7616_VB_RESERVED2,                                                     |
| };                                                                           |
|                                                                              |
| enum ad7616_range {                                                          |
|     AD7616_2V5 = 1,                                                          |
|     AD7616_5V  = 2,                                                          |
|     AD7616_10V = 3,                                                          |
| };                                                                           |
|                                                                              |
| enum ad7616_osr {                                                            |
|     AD7616_OSR_0,                                                            |
|     AD7616_OSR_2,                                                            |
|     AD7616_OSR_4,                                                            |
|     AD7616_OSR_8,                                                            |
|     AD7616_OSR_16,                                                           |
|     AD7616_OSR_32,                                                           |
|     AD7616_OSR_64,                                                           |
|     AD7616_OSR_128,                                                          |
| };                                                                           |
|                                                                              |
| struct ad7616_dev {                                                          |
|     /* SPI */                                                                |
|     struct no_os_spi_desc       *spi_desc;                                   |
|     struct spi_engine_offload_init_param *offload_init_param;                |
|     uint32_t reg_access_speed;                                               |
|     uint8_t crc;                                                             |
|     /* GPIO */                                                               |
|     struct no_os_gpio_desc  *gpio_hw_rngsel0;                                |
|     struct no_os_gpio_desc  *gpio_hw_rngsel1;                                |
|     struct no_os_gpio_desc  *gpio_reset;                                     |
|     struct no_os_gpio_desc  *gpio_os0;                                       |
|     struct no_os_gpio_desc  *gpio_os1;                                       |
|     struct no_os_gpio_desc  *gpio_os2;                                       |
|     struct no_os_gpio_desc  *gpio_convst;                                    |
|     struct no_os_gpio_desc  *gpio_busy;                                      |
|     /* AXI Core */                                                           |
|     uint32_t core_baseaddr;                                                  |
|     /* Device Settings */                                                    |
|     enum ad7616_interface   interface;                                       |
|     enum ad7616_mode            mode;                                        |
|     enum ad7616_range       va[8];                                           |
|     enum ad7616_range       vb[8];                                           |
|     enum ad7616_osr         osr;                                             |
|     void (*dcache_invalidate_range)(uint32_t address, uint32_t bytes_count); |
|     /* Sequencer and burst mode */                                           |
|     uint8_t layers_nb;                                                       |
| };                                                                           |
|                                                                              |
| struct ad7616_init_param {                                                   |
|     /* SPI */                                                                |
|     struct no_os_spi_init_param     *spi_param;                              |
|     struct spi_engine_offload_init_param *offload_init_param;                |
|     uint32_t reg_access_speed;                                               |
|     uint8_t crc;                                                             |
|     /* GPIO */                                                               |
|     struct no_os_gpio_init_param        *gpio_hw_rngsel0_param;              |
|     struct no_os_gpio_init_param        *gpio_hw_rngsel1_param;              |
|     struct no_os_gpio_init_param        *gpio_reset_param;                   |
|     struct no_os_gpio_init_param        *gpio_os0_param;                     |
|     struct no_os_gpio_init_param        *gpio_os1_param;                     |
|     struct no_os_gpio_init_param        *gpio_os2_param;                     |
|     struct no_os_gpio_init_param        *gpio_convst_param;                  |
|     struct no_os_gpio_init_param        *gpio_busy_param;                    |
|     /* Core */                                                               |
|     uint32_t            core_baseaddr;                                       |
|     /* Device Settings */                                                    |
|     enum ad7616_mode            mode;                                        |
|     enum ad7616_range       va[8];                                           |
|     enum ad7616_range       vb[8];                                           |
|     enum ad7616_osr         osr;                                             |
|     void (*dcache_invalidate_range)(uint32_t address, uint32_t bytes_count); |
| };                                                                           |
|                                                                              |
| struct ad7616_conversion_result {                                            |
|     uint16_t channel_a;                                                      |
|     uint16_t channel_b;                                                      |
| };                                                                           |
|                                                                              |
| struct ad7616_sequencer_layer {                                              |
|     enum ad7616_ch ch_a;                                                     |
|     enum ad7616_ch ch_b;                                                     |
| };``                                                                         |
+------------------------------------------------------------------------------+

No-OS IIO Driver Description
----------------------------

.. _functions-declarations-1:

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------+---------------------------------------+
| Function                                                                                    | Description                           |
+=============================================================================================+=======================================+
| ``int ad7616_iio_init(struct ad7616_iio_dev **dev, struct ad7616_init_param *init_param);`` | Initialize AD7616 for IIO interfacing |
+---------------------------------------------------------------------------------------------+---------------------------------------+
| ``int ad7616_iio_remove(struct ad7616_iio_dev *dev);``                                      | Remove AD7616                         |
+---------------------------------------------------------------------------------------------+---------------------------------------+

.. _types-declarations-1:

Types Declarations
~~~~~~~~~~~~~~~~~~

.. code:: c

   struct ad7616_iio_dev {
       struct ad7616_dev *ad7616_dev;
       struct iio_device *iio_dev;
   };

Support
-------

.. hint::

   **Questions?** Feel free to ask your questions in EngineerZone support forums.

   
   -  :ez:`FPGA Reference Design <community/fpga>`
   -  :ez:`Microcontroller no-OS Drivers <community/linux-device-drivers/microcontroller-no-os-drivers>`.
   


.. |AD7616-SDZ HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/ad7616_sdz`
.. |AD7616-SDZ No-OS Project.| image:: https://wiki.analog.com/_media/:git-no-OS:`projects/ad7616-sdz`
.. |AD7616-ST No-OS Project.| image:: https://wiki.analog.com/_media/:git-no-OS:`projects/ad7616-st`
