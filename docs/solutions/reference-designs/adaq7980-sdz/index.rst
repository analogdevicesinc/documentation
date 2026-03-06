.. imported from: https://wiki.analog.com/resources/eval/user-guides/adaq7980-sdz

.. _adaq7980-sdz:

ADAQ7980-SDZ User Guide
========================

Introduction
------------

The :adi:`ADAQ7980` / :adi:`ADAQ7988` are 16-bit analog-to-digital converter
(ADC) subsystems that integrate four common signal processing and conditioning
blocks into a system in package (SiP) design that supports a variety of
applications. These devices contain the most critical passive components,
eliminating many of the design challenges associated with traditional signal
chains that use successive approximation register (SAR) ADCs. These passive
components are crucial to achieving the specified device performance.

The ADAQ7980 / ADAQ7988 contain:

- A high accuracy, low power, 16-bit SAR ADC
- A low power, high bandwidth, high input impedance ADC driver
- A low power, stable reference buffer
- An efficient power management block

Housed within a 5 mm x 4 mm LGA package, the ADAQ7980 simplifies the design
process for data acquisition systems while providing the flexibility of a
configurable ADC driver feedback loop to allow gain and/or common-mode
adjustments. A set of four device supplies provides optimal system performance;
however, single-supply operation is possible with minimal impact on device
operating specifications.

Using the SDI input, the SPI-compatible serial interface features the ability to
daisy-chain multiple devices on a single, 3-wire bus and provides an optional
busy indicator. The user interface is compatible with 1.8 V, 2.5 V, 3 V, or
5 V logic. Specified operation of these devices is from -55 degrees C to
+125 degrees C.

Applications:

- Automated test equipment (ATE)
- Battery powered instrumentation
- Communications
- Data acquisition
- Process control
- Medical instruments

Supported Devices
-----------------

- :adi:`ADAQ7980`
- :adi:`ADAQ7988`

Evaluation Boards
~~~~~~~~~~~~~~~~~

- :adi:`EVAL-ADAQ7980`

Supported Carriers
------------------

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

HDL Reference Design
--------------------

The reference design uses the standard SPI Engine Framework with an integrated
pulse generator, which provides the required conversion rate for the ADC.

In order to build the HDL design, follow these steps:

#. Confirm that you have the right tools (see
   `HDL releases <https://github.com/analogdevicesinc/hdl/releases>`__)
#. Clone the
   `HDL GitHub repository <https://github.com/analogdevicesinc/hdl>`__
#. Set up the required sampling rate (see **Design Configuration** below)
#. Build the project (see
   `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__)

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses an integrated pulse generator to synchronize the
capture events during continuous conversion. The required sampling rate can be
set in the ``system_bd.tcl`` file:

.. code-block:: tcl

   set adc_sampling_rate 1000000

HDL Source Code
~~~~~~~~~~~~~~~

- :git-hdl:`projects/adaq7980_sdz`

Software Support
----------------

No-OS Project
~~~~~~~~~~~~~

- :git-no-OS:`projects/adaq7980_sdz`

No-OS Driver
~~~~~~~~~~~~

The driver provides the following API:

.. list-table:: No-OS Driver Functions
   :header-rows: 1
   :widths: 40 60

   * - Function
     - Description
   * - ``adaq7980_setup()``
     - Initialize the device.

The driver uses the following device and initialization structures:

.. code-block:: c

   typedef struct {
       /* SPI */
       spi_device      spi_dev;
       /* GPIO */
       gpio_device     gpio_dev;
       int8_t          gpio_pd_ldo;
       int8_t          gpio_ref_pd;
       int8_t          gpio_rbuf_pd;
   } adaq7980_dev;

   typedef struct {
       /* SPI */
       uint8_t         spi_chip_select;
       spi_mode        spi_mode;
       spi_type        spi_type;
       uint32_t        spi_device_id;
       /* GPIO */
       gpio_type       gpio_type;
       uint32_t        gpio_device_id;
       int8_t          gpio_pd_ldo;
       int8_t          gpio_ref_pd;
       int8_t          gpio_rbuf_pd;
   } adaq7980_init_param;

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`FPGA Reference Designs Forum <fpga>`.
