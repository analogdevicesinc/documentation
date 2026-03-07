ADPD410X No-OS Driver
=====================

Supported Devices
-----------------

-  :adi:`ADPD4100`
-  :adi:`ADPD4101`

Overview
--------

The :adi:`ADPD4100`/:adi:`ADPD4101` operate as a complete multimodal sensor front end, stimulating up to eight light emitting diodes (LEDs) and measuring the return signal on up to eight separate current inputs. Twelve time slots are available, enabling 12 separate measurements per sampling period. The data output and functional configuration utilize an I2C interface on the :adi:`ADPD4101` or a serial port interface (SPI) on the :adi:`ADPD4100`. The control circuitry includes flexible LED signaling and synchronous detection. The devices use a 1.8 V analog core and 1.8 V/3.3 V compatible digital input/output (I/O).

Applications:

-  Wearable health and fitness monitors: heart rate monitors (HRMs), heart rate variability (HRV), stress, blood pressure estimation, SpO2, hydration, body composition
-  Industrial monitoring: CO, CO2, smoke, and aerosol detection
-  Home patient monitoring

Driver Description
------------------

The driver contains two parts:

-  The driver for the :adi:`ADPD4100`/:adi:`ADPD4101` part, which may be used, without modifications, with any microcontroller.
-  The Communication Drivers, where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the ADI driver.

The Communication Driver has a standard interface, so the :adi:`ADPD4100`/:adi:`ADPD4101` driver can be used exactly as it is provided.

The Communication Drivers must include two things: I2C transmission methods for :adi:`ADPD4101` and SPI transmission methods for :adi:`ADPD4100` and GPIO control methods. For the I2C method, the driver calls four functions:

-  i2c_init() – initializes the I2C communication peripheral.
-  i2c_remove() – frees memory allocated by the I2C communication driver.
-  i2c_write() – writes data to the device.
-  i2c_read() – reads data from the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/i2c_driver_architecture.png
   :align: center

For the SPI method, the driver calls three functions:

-  spi_init() - initializes the SPI communication peripheral.
-  spi_remove() – frees memory allocated by the SPI communication driver.
-  spi_write_and_read() – conduct information transfer with the device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_driver_architecture.png
   :align: center

For the GPIO control methods, the driver calls three functions:

-  gpio_get() - initialize GPIO peripheral and allocate memory for one GPIO control.
-  gpio_remove() - frees memory allocated by the GPIO control driver.
-  gpio_direction_output() - set GPIO as input.
-  gpio_set_value() - set logic state of the GPIO.

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| Function                                                        | Description                                                                        |
+=================================================================+====================================================================================+
| ``int32_t adpd410x_setup(struct adpd410x_dev **device,          | Setup the device and the driver.                                                   |
|         struct adpd410x_init_param *init_param);``              |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_remove(struct adpd410x_dev *dev);``          | Free memory allocated by adpd410x_setup().                                         |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_reg_read(struct adpd410x_dev *dev,           | Read device register.                                                              |
|         uint16_t address,                                       |                                                                                    |
|         uint16_t *data);``                                      |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_reg_write(struct adpd410x_dev *dev,          | Write device register.                                                             |
|         uint16_t address,                                       |                                                                                    |
|         uint16_t data);``                                       |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_reg_write_mask(struct adpd410x_dev *dev,     | Do a read and write of a register to update only part of a register.               |
|         uint16_t address,                                       |                                                                                    |
|         uint16_t data,                                          |                                                                                    |
|         uint16_t mask);``                                       |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_reset(struct adpd410x_dev *dev);``           | Do a software reset.                                                               |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_set_opmode(struct adpd410x_dev *dev,         | Set operation mode.                                                                |
|         enum adpd410x_opmode mode);``                           |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_set_last_timeslot(struct adpd410x_dev *dev,  | Set number of active time slots.                                                   |
|         enum adpd410x_timeslots timeslot_no);``                 |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_set_sampling_freq(struct adpd410x_dev *dev,  | Set device sampling frequency.                                                     |
|         uint32_t sampling_freq);``                              |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_timeslot_setup(struct adpd410x_dev *dev,     | Setup an active time slot.                                                         |
|         enum adpd410x_timeslots timeslot_no,                    |                                                                                    |
|         struct adpd410x_timeslot_init *init);``                 |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_get_fifo_bytecount(struct adpd410x_dev *dev, | Get number of bytes in the device FIFO.                                            |
|         uint16_t *bytes);``                                     |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``int32_t adpd410x_get_data(struct adpd410x_dev *dev,           | Get a full data packet from the device containing data from all active time slots. |
|         uint32_t *data);``                                      |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+

Types Declarations
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+


| ``/**                                                                           |

|   * @union phy_comm_dev                                                         |
|   * @brief Contains physical communication handler                              |
|  */                                                                             |
| union phy_comm_dev {                                                            |
|     /** SPI handler */                                                          |
|     struct spi_desc *spi_phy_dev;                                               |
|     /** I2C handler */                                                          |
|     struct i2c_desc *i2c_phy_dev;                                               |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @union phy_comm_init_param                                                  |
|   * @brief Contains physical communication initialization structure             |
|  */                                                                             |
| union phy_comm_init_param {                                                     |
|     /** SPI initialization structure */                                         |
|     struct spi_init_param spi_phy_init;                                         |
|     /** I2C initialization structure */                                         |
|     struct i2c_init_param i2c_phy_init;                                         |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_supported_dev                                                |
|   * @brief Devices supported by the driver                                      |
|  */                                                                             |
| enum adpd410x_supported_dev {                                                   |
|     ADPD4100,                                                                   |
|     ADPD4101                                                                    |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_opmode                                                       |
|   * @brief Operation modes of the device                                        |
|  */                                                                             |
| enum adpd410x_opmode {                                                          |
|     /** Standby mode, used for programming */                                   |
|     ADPD410X_STANDBY,                                                           |
|     /** Active mode, used for sampling data */                                  |
|     ADPD410X_GOMODE                                                             |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_ts_input_pair                                                |
|   * @brief List of input pairs options for time slots                           |
|  */                                                                             |
| enum adpd410x_ts_input_pair {                                                   |
|     /** Use input pair 1 and 2 */                                               |
|     ADPD410X_INP12,                                                             |
|     /** Use input pair 3 and 4 */                                               |
|     ADPD410X_INP34,                                                             |
|     /** Use input pair 5 and 6 */                                               |
|     ADPD410X_INP56,                                                             |
|     /** Use input pair 7 and 8 */                                               |
|     ADPD410X_INP78                                                              |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_ts_input_opt                                                 |
|   * @brief List of input configurations for time slot                           |
|  */                                                                             |
| enum adpd410x_ts_input_opt {                                                    |
|     /** Both inputs disconnected */                                             |
|     ADPD410X_INaDIS_INbDIS,                                                     |
|     /** First input connected to channel 1 */                                   |
|     ADPD410X_INaCH1_INbDIS,                                                     |
|     /** First input connected to channel 2 */                                   |
|     ADPD410X_INaCH2_INbDIS,                                                     |
|     /** Second input connected to channel 1 */                                  |
|     ADPD410X_INaDIS_INbCH1,                                                     |
|     /** Second input connected to channel 2 */                                  |
|     ADPD410X_INaDIS_INbCH2,                                                     |
|     /** First input -> channel 1, second input -> channel 2 */                  |
|     ADPD410X_INaCH1_INbCH2,                                                     |
|     /** First input -> channel 2, second input -> channel 1 */                  |
|     ADPD410X_INaCH2_INbCH1,                                                     |
|     /** First input + Second input -> channel 1 */                              |
|     ADPD410X_INaCH1_INbCH1,                                                     |
|     /** First input + Second input -> channel 2 */                              |
|     ADPD410X_INaCH2_INbCH2                                                      |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @struct adpd410x_ts_inputs                                                  |
|   * @brief Structure holding time slot input configuration                      |
|  */                                                                             |
| struct adpd410x_ts_inputs {                                                     |
|     /** Input pair option */                                                    |
|     enum adpd410x_ts_input_pair pair;                                           |
|     /** Input pair t channel connection option */                               |
|     enum adpd410x_ts_input_opt option;                                          |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_precon_opt                                                   |
|   * @brief Time slot input precondition options                                 |
|  */                                                                             |
| enum adpd410x_precon_opt {                                                      |
|     /** Float inputs */                                                         |
|     ADPD410X_FLOAT_INS,                                                         |
|     /** Precondition inputs to VC1 */                                           |
|     ADPD410X_VC1,                                                               |
|     /** Precondition inputs to VC2 */                                           |
|     ADPD410X_VC2,                                                               |
|     /** Precondition inputs to VICM */                                          |
|     ADPD410X_VICM,                                                              |
|     /** Precondition inputs to TIA input */                                     |
|     ADPD410X_TIA_IN,                                                            |
|     /** Precondition inputs to TIA reference voltage */                         |
|     ADPD410X_TIA_VREF,                                                          |
|     /** Precondition inputs by shorting the differential pair */                |
|     ADPD410X_SHORT_INS                                                          |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_tia_vref_volt                                                |
|   * @brief TIA reference voltage options                                        |
|  */                                                                             |
| enum adpd410x_tia_vref_volt {                                                   |
|     /** 1,1385 V */                                                             |
|     ADPD410X_TIA_VREF_1V1385,                                                   |
|     /** 1,012 V */                                                              |
|     ADPD410X_TIA_VREF_1V012,                                                    |
|     /** 0,8855 V */                                                             |
|     ADPD410X_TIA_VREF_0V8855,                                                   |
|     /** 1,256 V */                                                              |
|     ADPD410X_TIA_VREF_1V256                                                     |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_tia_vref_ref                                                 |
|   * @brief TIA resistor gain setting                                            |
|  */                                                                             |
| enum adpd410x_tia_vref_ref {                                                    |
|     /** 200 kOhm */                                                             |
|     ADPD410X_TIA_VREF_200K,                                                     |
|     /** 100 kOhm */                                                             |
|     ADPD410X_TIA_VREF_100K,                                                     |
|     /** 50 kOhm */                                                              |
|     ADPD410X_TIA_VREF_50K,                                                      |
|     /** 25 kOhm */                                                              |
|     ADPD410X_TIA_VREF_25K,                                                      |
|     /** 12,5 kOhm */                                                            |
|     ADPD410X_TIA_VREF_12K5                                                      |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_led_output_opt                                               |
|   * @brief LED output option                                                    |
|  */                                                                             |
| enum adpd410x_led_output_opt {                                                  |
|     /** Option A */                                                             |
|     ADPD410X_OUTPUT_A,                                                          |
|     /** Option B */                                                             |
|     ADPD410X_OUTPUT_B                                                           |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @struct _adpd410x_led_control                                               |
|   * @brief Structure mapping LED output option and LED strength to one byte     |
|  */                                                                             |
| struct _adpd410x_led_control {                                                  |
|     /** LED output strength */                                                  |
|     uint8_t let_current_select : 7;                                             |
|     /** LED option */                                                           |
|     enum adpd410x_led_output_opt led_output_select : 1;                         |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @union adpd410x_led_control                                                 |
|   * @brief Union of the LED mapping and value so they can be accessed both ways |
|  */                                                                             |
| union adpd410x_led_control {                                                    |
|     /** LED control mapping */                                                  |
|     struct _adpd410x_led_control fields;                                        |
|     /** LED control value */                                                    |
|     uint8_t value;                                                              |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_timeslots                                                    |
|   * @brief Available Time slots                                                 |
|  */                                                                             |
| enum adpd410x_timeslots {                                                       |
|     /** Time slot A */                                                          |
|     ADPD410X_TS_A,                                                              |
|     /** Time slot B */                                                          |
|     ADPD410X_TS_B,                                                              |
|     /** Time slot C */                                                          |
|     ADPD410X_TS_C,                                                              |
|     /** Time slot D */                                                          |
|     ADPD410X_TS_D,                                                              |
|     /** Time slot E */                                                          |
|     ADPD410X_TS_E,                                                              |
|     /** Time slot F */                                                          |
|     ADPD410X_TS_F,                                                              |
|     /** Time slot G */                                                          |
|     ADPD410X_TS_G,                                                              |
|     /** Time slot H */                                                          |
|     ADPD410X_TS_H,                                                              |
|     /** Time slot I */                                                          |
|     ADPD410X_TS_I,                                                              |
|     /** Time slot J */                                                          |
|     ADPD410X_TS_J,                                                              |
|     /** Time slot K */                                                          |
|     ADPD410X_TS_K,                                                              |
|     /** Time slot L */                                                          |
|     ADPD410X_TS_L                                                               |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @struct adpd410x_timeslot_init                                              |
|   * @brief Initialization structure for time slots                              |
|  */                                                                             |
| struct adpd410x_timeslot_init {                                                 |
|     /** Enable ADC channel 2 for a time slot */                                 |
|     bool enable_ch2;                                                            |
|     /** Time slot input configuration */                                        |
|     struct adpd410x_ts_inputs ts_inputs;                                        |
|     /** Time slot input precondition option */                                  |
|     enum adpd410x_precon_opt precon_option;                                     |
|     /** TIA reference voltage */                                                |
|     enum adpd410x_tia_vref_volt afe_trim_opt;                                   |
|     /** TIA alternative reference voltage for pulsing property */               |
|     enum adpd410x_tia_vref_volt vref_pulse_opt;                                 |
|     /** TIA resistor gain setting for channel 1 */                              |
|     enum adpd410x_tia_vref_ref chan1;                                           |
|     /** TIA resistor gain setting for channel 2 */                              |
|     enum adpd410x_tia_vref_ref chan2;                                           |
|     /** LED pulse reverse pattern */                                            |
|     uint8_t pulse4_reverse;                                                     |
|     /** LED pulse subtracion pattern */                                         |
|     uint8_t pulse4_subtract;                                                    |
|     /** Bytes number for time slot */                                           |
|     uint8_t byte_no;                                                            |
|     /** Decimate factor - 1 */                                                  |
|     uint8_t dec_factor;                                                         |
|     /** LED 2 output and current control */                                     |
|     union adpd410x_led_control led2;                                            |
|     /** LED 1 output and current control */                                     |
|     union adpd410x_led_control led1;                                            |
|     /** LED 4 output and current control */                                     |
|     union adpd410x_led_control led4;                                            |
|     /** LED 3 output and current control */                                     |
|     union adpd410x_led_control led3;                                            |
|     /** ADC integration cycles per conversion */                                |
|     uint8_t adc_cycles;                                                         |
|     /** ADC number of LED pulses per cycle */                                   |
|     uint8_t repeats_no;                                                         |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @enum adpd410x_clk_opt                                                      |
|   * @brief External clock options                                               |
|  */                                                                             |
| enum adpd410x_clk_opt {                                                         |
|     /** Use internal low frequency and high frequency oscillators */            |
|     ADPD410X_INTLFO_INTHFO,                                                     |
|     /** Use external low frequency and internal high frequency oscillator */    |
|     ADPD410X_EXTLFO_INTHFO,                                                     |
|     /** Use internal low frequency and external high frequency oscillator */    |
|     ADPD410X_INTLFO_EXTHFO,                                                     |
|     /** Use external high frequency oscillator and generate low frequency       |
|      *  using it */                                                             |
|     ADPD410X_GENLFO_EXTHFO                                                      |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @struct adpd410x_init_param                                                 |
|   * @brief Device driver initialization structure                               |
|  */                                                                             |
| struct adpd410x_init_param {                                                    |
|     /** Physical communication */                                               |
|     union phy_comm_init_param dev_ops_init;                                     |
|     /** Device option */                                                        |
|     enum adpd410x_supported_dev dev_type;                                       |
|     /** Device clock option */                                                  |
|     enum adpd410x_clk_opt clk_opt;                                              |
|     /** GPIO 0 initialization */                                                |
|     struct gpio_init_param gpio0;                                               |
|     /** GPIO 1 initialization */                                                |
|     struct gpio_init_param gpio1;                                               |
|     /** GPIO 2 initialization */                                                |
|     struct gpio_init_param gpio2;                                               |
|     /** GPIO 3 initialization */                                                |
|     struct gpio_init_param gpio3;                                               |
|     /** External low frequency oscillator frequency, if applicable */           |
|     uint32_t ext_lfo_freq;                                                      |
| };                                                                              |
|                                                                                 |
| /**                                                                             |
|   * @struct adpd410x_dev                                                        |
|   * @brief Device driver handler                                                |
|  */                                                                             |
| struct adpd410x_dev {                                                           |
|     /** Physical communication */                                               |
|     union phy_comm_dev dev_ops;                                                 |
|     /** Device option */                                                        |
|     enum adpd410x_supported_dev dev_type;                                       |
|     /** Device clock option */                                                  |
|     enum adpd410x_clk_opt clk_opt;                                              |
|     /** GPIO 0 handler */                                                       |
|     struct gpio_desc *gpio0;                                                    |
|     /** GPIO 1 handler */                                                       |
|     struct gpio_desc *gpio1;                                                    |
|     /** GPIO 2 handler */                                                       |
|     struct gpio_desc *gpio2;                                                    |
|     /** GPIO 3 handler */                                                       |
|     struct gpio_desc *gpio3;                                                    |
|     /** External low frequency oscillator frequency, if applicable */           |
|     uint32_t ext_lfo_freq;                                                      |
| };``                                                                            |
+---------------------------------------------------------------------------------+

Initialization example
~~~~~~~~~~~~~~~~~~~~~~

:adi:`CN0503 Liquid Analysis Platform <cn0503>`

Downloads
---------

.. admonition:: Download
   :class: download

   
   -


   
   |Implementation of ADPD410X Driver.|

   -

   |Header file of ADPD410X Driver.|

.. |Implementation of ADPD410X Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/photo-electronic/adpd410x/adpd410x`.c
.. |Header file of ADPD410X Driver.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/photo-electronic/adpd410x/adpd410x`.h
