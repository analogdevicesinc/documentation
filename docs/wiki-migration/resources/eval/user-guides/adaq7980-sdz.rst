ADAQ7980 User Guide
===================

Overview
--------

The :adi:`ADAQ7980`/:adi:`ADAQ7988` are 16-bit analog-to-digital converter (ADC) subsystems that integrate four common signal processing and conditioning blocks into a system in package (SiP) design that supports a variety of applications. These devices contain the most critical passive components, eliminating many of the design challenges associated with traditional signal chains that use successive approximation register (SAR) ADCs. These passive components are crucial to achieving the specified device performance.

The :adi:`ADAQ7980`/:adi:`ADAQ7988` contain a high accuracy, low power, 16-bit SAR ADC, a low power, high bandwidth, high input impedance ADC driver, a low power, stable reference buffer, and an efficient power management block. Housed within a tiny, 5 mm × 4 mm LGA package, these systems simplify the design process for data acquisition systems. The level of system integration of the :adi:`ADAQ7980`/:adi:`ADAQ7988` solves many design challenges, while the devices still provide the flexibility of a configurable ADC driver feedback loop to allow gain and/or common-mode adjustments. A set of four device supplies provides optimal system performance; however, single-supply operation is possible with minimal impact on device operating specifications.

Using the SDI input, the SPI-compatible serial interface features the ability to daisy-chain multiple devices on a single, 3-wire bus and provides an optional busy indicator. The user interface is compatible with 1.8 V, 2.5 V, 3 V, or 5 V logic. Specified operation of these devices is from −55°C to +125°C.

Applications:

-  Automated test equipment (ATE)
-  Battery powered instrumentation
-  Communications
-  Data acquisition
-  Process control
-  Medical instruments

Supported Device
~~~~~~~~~~~~~~~~

-  :adi:`ADAQ7980`

Evaluation Boards
~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-ADAQ7980`

Supported carrier
~~~~~~~~~~~~~~~~~

-  `ZedBoard <https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html>`_

HDL Design Description
----------------------

In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design in general.

The reference design uses the standard :doc:`SPI Engine Framework </wiki-migration/resources/fpga/peripherals/spi_engine>` with an integrated pulse generator, which will provide the required conversion rate for the ADC.

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see :git-hdl:`Release notes <releases>`)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Set up the required sampling rate (see caption **Design Configuration**)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses an integrated pulse generator to synchronise the capture events during continuous conversion. The required sampling rate can be set in :git-hdl:`projects/adaq7980_sdz/zed/system_bd.tcl` file to the required values:

1) The targeted sampling rate:

::

   set adc_sampling_rate 1000000

No-OS Driver Description
------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------+------------------------+
| Function                                                                           | Description            |
+====================================================================================+========================+
| ``int32_t adaq7980_setup(adaq7980_dev **device, adaq7980_init_param init_param);`` | Initialize the device. |
+------------------------------------------------------------------------------------+------------------------+

Types Declarations
~~~~~~~~~~~~~~~~~~

+------------------------------------------+


| ``typedef struct {                       |

|     /* SPI */                            |
|     spi_device          spi_dev;         |
|     /* GPIO */                           |
|     gpio_device         gpio_dev;        |
|     int8_t              gpio_pd_ldo;     |
|     int8_t              gpio_ref_pd;     |
|     int8_t              gpio_rbuf_pd;    |
| } adaq7980_dev;                          |
|                                          |
| typedef struct {                         |
|     /* SPI */                            |
|     uint8_t             spi_chip_select; |
|     spi_mode            spi_mode;        |
|     spi_type            spi_type;        |
|     uint32_t            spi_device_id;   |
|     /* GPIO */                           |
|     gpio_type           gpio_type;       |
|     uint32_t            gpio_device_id;  |
|     int8_t              gpio_pd_ldo;     |
|     int8_t              gpio_ref_pd;     |
|     int8_t              gpio_rbuf_pd;    |
| } adaq7980_init_param;``                 |
+------------------------------------------+

Create the SDK Project
----------------------

To run the application the user has to create an **Empty Application Project** using Xilinx SDK, and have to copy all the :git-no-OS:`design sources <projects/adaq7980_sdz/src>` to the **sw** directory. (see :doc:`SDK Software Setup </wiki-migration/resources/fpga/xilinx/software_setup>` for more detailed instructions) Another option for building the no-OS is using the Makefile. (see `Build no-OS with GNU make <https://wiki.analog.com/resources/fpga/no-os_make/software_setup>`_)

HDL Downloads
-------------

.. admonition:: Download
   :class: download

   
   -


   
   |adaq7980-SDZ HDL Project.|

No-OS Downloads
---------------

.. admonition:: Download
   :class: download

   
   -


   
   |adaq7980-SDZ No-OS Project.|

.. |adaq7980-SDZ HDL Project.| image:: https://wiki.analog.com/_media/:git-hdl:`projects/adaq7980_sdz`
.. |adaq7980-SDZ No-OS Project.| image:: https://wiki.analog.com/_media/:git-no-OS:`projects/adaq7980_sdz`
