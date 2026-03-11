AD7768-1 User Guide
===================

Overview
--------

The :adi:`AD7768-1` is a low power, high performance, Σ-Δ analog-to-digital converter (ADC), with a Σ-Δ modulator and digital filter for precision conversion of both ac and dc signals. The :adi:`AD7768-1` is a single channel version of the AD7768, an 8-channel, simultaneously sampling, Σ-Δ ADC. The :adi:`AD7768-1` provides a single configurable and reusable data acquisition footprint, which establishes a new industry standard in combined ac and dc performance and enables instrumentation and industrial system designers to design across multiple measurement variants for both isolated and nonisolated applications.

The :adi:`AD7768-1` achieves a 108.5 dB dynamic range when using the low ripple, finite impulse response (FIR) digital filter at 256 kSPS, giving 110.8 kHz input bandwidth (BW), combined with ±1.1 ppm integral nonlinearity (INL), ±30 µV offset error, and ±30 ppm gain error.

Wider bandwidth, up to 500 kHz Nyquist, 204 kHz, −3 dB, is available using the sinc5 filter, enabling a view of signals over an extended range.

The :adi:`AD7768-1` offers the user the flexibility to configure and optimize for input BW vs. output data rate (ODR) and vs. power dissipation. The flexibility of the :adi:`AD7768-1` allows for dynamic analysis of a changing input signal, making it particularly useful in general-purpose data acquisition systems. The selection of one of three available power modes allows the designer to achieve required noise targets while minimizing power consumption. The design of the :adi:`AD7768-1` is unique in that it becomes a reusable and flexible platform for low power dc and high performance ac measurement modules.

The :adi:`AD7768-1` achieves the optimum balance of dc and ac performance with excellent power efficiency. The following three operating modes allow the user to tailor the input BW vs. power budgets:

-  Fast mode offers both a sinc filter with up to 256 kSPS and 52.2 kHz of bandwidth, and 26.4 mW of power consumption, or a FIR filter with up to 256 kSPS, 110.8 kHz of bandwidth, and 36.8 mW of power consumption

-  Median mode offers a FIR filter with up to 128 kSPS, 55.4 kHz of bandwidth, and 19.7 mW of power consumption

-  Low power mode offers a FIR filter with up to 32 kSPS, 13.85 kHz of bandwidth, and 6.75 mW of power consumption

The :adi:`AD7768-1` offers extensive digital filtering capabilities that can meet a wide range of system requirements. The filter options allow configuration for frequency domain measurements with tight gain error over frequency, linear phase response requirements (brick wall filter), a lower latency path (sinc5 or sinc3) for use in control loop applications, and measuring dc inputs with the ability to configure the sinc3 filter to reject the line frequency of either 50 Hz or 60 Hz. All filters offer programmable decimation.

A 1.024 MHz sinc5 filter path exists for users seeking an even higher output data rate. This path is quantization noise limited; therefore, it is best suited for customers requiring minimum latency for control loops or implementing custom digital filtering on an external field programmable gate array (FPGA) or digital signal processor (DSP).

Filter options include the following:

-  A low ripple FIR filter with a ±0.005 dB pass-band ripple to 102.4 kHz

-  A low latency sinc5 filter with up to a 1.024 MHz data rate to maximize control loop responsiveness

-  A low latency sinc3 filter that is fully programmable, with 50 Hz/60 Hz rejection capabilities

When using the :adi:`AD7768-1`, embedded analog functionality within the :adi:`AD7768-1` greatly reduces the design burden over the entire application range. The precharge buffer on each analog input decreases analog input current compared to competitive offerings, simplifying the task of an external amplifier to drive the analog input.

A full buffer input on the reference vastly reduces the input current, providing a high impedance input for the external reference device or in buffering any reference sense resistor scenarios used in ratiometric measurements.

The device operates with a 5.0 V AVDD1 − AVSS supply, a 2.0 V to 5.0 V AVDD2 − AVSS supply, and a 1.8 V to 3.3 V IOVDD − DGND supply.

In low power mode, the AVDD1, AVDD2, and IOVDD supplies can run from a single 3.3 V rail.

The device requires an external reference; the absolute input reference (REFIN) voltage range is 1 V to AVDD1 − AVSS.

The specified operating temperature range is −40°C to +125°C. The device is housed in a 4 mm × 5 mm, 28-lead LFCSP.

Supported devices
~~~~~~~~~~~~~~~~~

-  :adi:`AD7768-1`

Evaluation board
~~~~~~~~~~~~~~~~

-  :adi:`EVAL-AD7768-1`

Supported FPGA carrier
~~~~~~~~~~~~~~~~~~~~~~

-  `ZedBoard <https://www.xilinx.com/products/boards-and-kits/1-8dyf-11.html>`_

HDL Design Description
----------------------

In the :doc:`ADI Reference Designs HDL User Guide </wiki-migration/resources/fpga/docs/hdl>` can be found an in-depth presentation and instructions about the HDL design in general.

The reference design uses the standard :doc:`SPI Engine Framework </wiki-migration/resources/fpga/peripherals/spi_engine>`, the offload module is triggered by the DRDY (data ready) signal of the device. Because the board has two AD7768-1, the data path consists of two separate SPI interface and GPIOs, and two DMAs for data stream capture.

In order to build the HDL design the user has to go through the following steps:

-  Confirm that you have the right tools (see `Release notes <https://github.com/analogdevicesinc/hdl/releases>`_)
-  Clone the HDL GitHub repository (see :doc:`/wiki-migration/resources/fpga/docs/git`)
-  Build the project (see :doc:`/wiki-migration/resources/fpga/docs/build`)

No-OS Driver Description
------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Function                                                                                                                                  | Description                                                                              |
+===========================================================================================================================================+==========================================================================================+
| ``int32_t ad77681_setup(ad77681_dev **device, ad77681_init_param init_param);``                                                           | Initialize the device.                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_soft_reset(ad77681_dev *dev);``                                                                                         | Device reset over SPI.                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_status_bit(ad77681_dev *dev, bool status_bit);``                                                                    | Enables Status bits output.                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_crc_sel(ad77681_dev *dev, ad77681_crc_sel crc_sel);``                                                               | Activates CRC on all SPI transactions and Selects CRC method as XOR or 8-bit polynomial. |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_convlen(ad77681_dev *dev, ad77681_conv_len conv_len);``                                                             | Set the Conversion Result Output Length.                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_conv_mode(ad77681_dev *dev, ad77681_conv_mode conv_mode, ad77681_conv_diag_mux diag_mux_sel, bool conv_diag_sel);`` | Conversion mode and source select.                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_mclk_div(ad77681_dev *dev, ad77681_mclk_div clk_div);``                                                             | Set the MCLK divider.                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_set_power_mode(ad77681_dev *dev, ad77681_power_mode mode);``                                                            | Set the power consumption mode of the ADC core.                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_spi_read_adc_data(ad77681_dev *dev, uint8_t *adc_data);``                                                               | Read conversion result from device.                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_spi_write_mask(ad77681_dev *dev, uint8_t reg_addr, uint8_t mask, uint8_t data);``                                       | SPI write to device using a mask.                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_spi_read_mask(ad77681_dev *dev, uint8_t reg_addr, uint8_t mask, uint8_t *data);``                                       | SPI read from device using a mask.                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_spi_reg_read(ad77681_dev *dev, uint8_t reg_addr, uint8_t *reg_data);``                                                  | Read from device.                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_compute_xor(uint8_t *data, uint8_t data_size);``                                                                        | Compute XOR checksum.                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``int32_t ad77681_compute_crc8(uint8_t *data, uint8_t data_size);``                                                                       | Compute CRC8 checksum.                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

Types Declarations
~~~~~~~~~~~~~~~~~~

.. code-block:: c

::

    typedef enum {
     AD77681_ECO = 0,
     AD77681_MEDIAN = 2,
     AD77681_FAST = 3,
    } ad77681_power_mode;

::

    typedef enum {
     AD77681_MCLK_DIV_16 = 0,
     AD77681_MCLK_DIV_8 = 1,
     AD77681_MCLK_DIV_4 = 2,
     AD77681_MCLK_DIV_2 = 3
    } ad77681_mclk_div;

::

    typedef enum {
     AD77681_CONV_CONTINUOUS = 0,
     AD77681_CONV_ONE_SHOT = 1,
     AD77681_CONV_SINGLE = 2,
     AD77681_CONV_PERIODIC = 3
    } ad77681_conv_mode;

::

    typedef enum {
     AD77681_CONV_24BIT = 0,
     AD77681_CONV_16BIT = 1
    } ad77681_conv_len;

::

    typedef enum {
     AD77681_RDY_DOUT_EN,
     AD77681_RDY_DOUT_DIS
    } ad77681_rdy_dout;

::

    typedef enum {
     AD77681_TEMP_SENSOR = 0x0,
     AD77681_AIN_SHORT= 0x8,
     AD77681_POSITIVE_FS = 0x9,
     AD77681_NEGATIVE_FS = 0xA
    } ad77681_conv_diag_mux;

::

    typedef enum {
     AD77681_CRC,
     AD77681_XOR,
     AD77681_NO_CRC
    } ad77681_crc_sel;

::

    typedef struct {
     /* SPI */
     spi_dev                 *spi_eng_dev;
     /* Configuration */
     ad77681_power_mode      power_mode;
     ad77681_mclk_div        mclk_div;
     ad77681_conv_mode       conv_mode;
     ad77681_conv_diag_mux   diag_mux_sel;
     bool                    conv_diag_sel;
     ad77681_conv_len        conv_len;
     ad77681_crc_sel         crc_sel;
     uint8_t                 status_bit;
    } ad77681_dev;

::

    typedef struct {
     /* SPI */
     spi_init_param          *spi_eng_dev_init;
     /* Configuration */
     ad77681_power_mode      power_mode;
     ad77681_mclk_div        mclk_div;
     ad77681_conv_mode       conv_mode;
     ad77681_conv_diag_mux   diag_mux_sel;
     bool                    conv_diag_sel;
     ad77681_conv_len        conv_len;
     ad77681_crc_sel         crc_sel;
     uint8_t                 status_bit;
    } ad77681_init_param;

HDL Downloads
-------------

.. admonition:: Download
   :class: download


   -  :git-hdl:`ad77681evb HDL Project. <projects/ad77681evb>`



No-OS Downloads
---------------

.. admonition:: Download
   :class: download


   -  `ad7768-1fmcz <https://github.com/analogdevicesinc/no-OS/tree/ad7768_1/ad7768-1fmcz>`_
