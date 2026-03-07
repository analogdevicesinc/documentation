ADXL372 - No-OS Driver
======================

Supported Devices
-----------------

-  :adi:`ADXL372`

Evaluation Boards
-----------------

-  :adi:`EVAL-ADXL372Z`

Overview
--------

The :adi:`ADXL372` is an ultralow power, 3-axis, ±200 g MEMS accelerometer that consumes 22 μA at a 3200 Hz output data rate (ODR). The :adi:`ADXL372`\ does not power cycle its front end to achieve its low power operation and therefore does not run the risk of aliasing the output of the sensor.

The :adi:`ADXL372` provides 12-bit output data at 100 mg/LSB scale factor. The user can access configuration and data registers via the serial peripheral interface (SPI) or limited I2C protocol. The :adi:`ADXL372` operates over a wide supply voltage range and is available in a 3 mm × 3.25 mm × 1.06 mm package.

In addition to its ultralow power consumption, the :adi:`ADXL372` has many features to enable impact detection while providing system level power reduction. The device includes a deep multimode output first in, first out (FIFO), several activity detection modes, and a method for capturing only the peak acceleration of over threshold events.

The :adi:`ADXL372` operates on a wide 1.6 V to 3.5 V supply range. :adi:`ADXL372` is available in a 3 mm × 3.25 mm × 1.06 mm package.

Applications
------------

-  Impact and shock detection
-  Asset health assessment
-  Portable Internet of Things (IoT) edge nodes
-  Concussion and head trauma detection

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/eval-adxl372z.png
   :align: center
   :width: 300px

No-OS Driver Description
------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Function                                                                                                                             | Description                                                                                                                     |
+======================================================================================================================================+=================================================================================================================================+
| ``int32_t adxl372_init(adxl372_dev **device, adxl372_init_param init_param)``                                                        | Initialize the device.                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_get_accel_data(adxl372_dev *dev, adxl372_xyz_accel_data *accel_data)``                                             | Retrieve 3-axis acceleration data.                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_get_highest_peak_data(adxl372_dev *dev, adxl372_xyz_accel_data *max_peak)``                                        | Retrieve the highest magnitude (x, y, z) sample recorded since the last read of the MAXPEAK registers.                          |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_get_fifo_xyz_data(adxl372_dev *dev, adxl372_xyz_accel_data *samples, uint16_t cnt)``                               | Get the data stored in FIFO.                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl_service_fifo_ev(adxl372_dev *dev, adxl372_xyz_accel_data *fifo_data, uint16_t *fifo_entries)``                        | Retrieve data stored in FIFO. Can be used in polling mode, but works best when interrupts are used.                             |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_configure_fifo(adxl372_dev *dev, adxl372_fifo_mode mode, adxl372_fifo_format format, uint16_t fifo_samples)``      | Configure the operating parameters for the FIFO.                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_reset(adxl372_dev *dev)``                                                                                          | Software reset.                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_get_status(adxl372_dev *dev, uint8_t *status1, uint8_t *status2, uint16_t *fifo_entries)``                         | Get the STATUS, STATUS2, FIFO_ENTRIES and FIFO_ENTRIES2 registers data.                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_interrupt_config(adxl372_dev *dev, adxl372_irq_config int1, adxl372_irq_config int2)``                             | Configure the INT1 and INT2 interrupt pins.                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_filter_settle(adxl372_dev *dev, adxl372_filter_settle mode)``                                                  | Set the filter settling period.                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_inactivity_time(adxl372_dev *dev, uint16_t time)``                                                             | Set the inactivity timer.                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_activity_time(adxl372_dev *dev, uint16_t time)``                                                               | Set the activity timer.                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_wakeup_rate(adxl372_dev *dev, adxl372_wakeup_rate wur)``                                                       | Set the Timer Rate for Wake-Up Mode.                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_instant_on_th(adxl372_dev *dev, adxl372_instant_on_th_mode mode)``                                             | Select instant on threshold.                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_odr(adxl372_dev *dev, adxl372_odr odr)``                                                                       | Set Output data rate.                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_act_proc_mode(adxl372_dev *dev, adxl372_act_proc_mode mode)``                                                  | Link/Loop Activity Processing.                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_bandwidth(adxl372_dev *dev, adxl372_bandwidth bw)``                                                            | Select the desired output signal bandwidth.                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_autosleep(adxl372_dev *dev, bool enable)``                                                                     | Autosleep. When set to 1, autosleep is enabled, and the device enters wake-up mode automatically upon detection of inactivity.  |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_op_mode(adxl372_dev *dev, adxl372_op_mode op_mode)``                                                           | Set the mode of operation.                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_set_activity_threshold(adxl372_dev *dev, adxl372_th_activity act, uint16_t thresh, bool referenced, bool enable)`` | Set the threshold for activity detection for all 3-axis                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_spi_write_mask(adxl372_dev *dev, uint8_t reg_addr, uint32_t mask, uint8_t data)``                                  | SPI write to device using a mask.                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_spi_reg_write(adxl372_dev *dev, uint8_t reg_addr, uint8_t reg_data)``                                              | Write to device.                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_spi_reg_read_multiple(adxl372_dev *dev, uint8_t reg_addr, uint8_t *reg_data, uint16_t count)``                     | Multibyte read from device. A register read begins with the address and autoincrements for each aditional byte in the transfer. |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``int32_t adxl372_spi_reg_read(adxl372_dev *dev, uint8_t reg_addr, uint8_t *reg_data)``                                              | Read from device.                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

Types Declarations
~~~~~~~~~~~~~~~~~~

+------------------------------------------------+


| ``typedef enum {                               |

|     ADXL372_X_AXIS,                            |
|     ADXL372_Y_AXIS,                            |
|     ADXL372_Z_AXIS                             |
| } adxl372_axis;                                |
|                                                |
| typedef enum {                                 |
|     ADXL372_STANDBY,                           |
|     ADXL372_WAKE_UP,                           |
|     ADXL372_INSTANT_ON,                        |
|     ADXL372_FULL_BW_MEASUREMENT                |
| } adxl372_op_mode;                             |
|                                                |
| typedef enum {                                 |
|     ADXL372_BW_200HZ,                          |
|     ADXL372_BW_400HZ,                          |
|     ADXL372_BW_800HZ,                          |
|     ADXL372_BW_1600HZ,                         |
|     ADXL372_BW_3200HZ                          |
| } adxl372_bandwidth;                           |
|                                                |
| typedef enum {                                 |
|     ADXL372_DEFAULT,                           |
|     ADXL372_LINKED,                            |
|     ADXL372_LOOPED                             |
| } adxl372_act_proc_mode;                       |
|                                                |
| typedef enum {                                 |
|     ADXL372_ODR_400HZ,                         |
|     ADXL372_ODR_800HZ,                         |
|     ADXL372_ODR_1600HZ,                        |
|     ADXL372_ODR_3200HZ,                        |
|     ADXL372_ODR_6400HZ                         |
| } adxl372_odr;                                 |
|                                                |
| typedef enum {                                 |
|     ADXL372_INSTANT_ON_LOW_TH,                 |
|     ADXL372_INSTANT_ON_HIGH_TH                 |
| } adxl372_instant_on_th_mode;                  |
|                                                |
| typedef enum {                                 |
|     ADXL372_WUR_52ms,                          |
|     ADXL372_WUR_104ms,                         |
|     ADXL372_WUR_208ms,                         |
|     ADXL372_WUR_512ms,                         |
|     ADXL372_WUR_2048ms,                        |
|     ADXL372_WUR_4096ms,                        |
|     ADXL372_WUR_8192ms,                        |
|     ADXL372_WUR_24576ms                        |
| } adxl372_wakeup_rate;                         |
|                                                |
| typedef enum {                                 |
|     ADXL372_ACTIVITY,                          |
|     ADXL372_ACTIVITY2,                         |
|     ADXL372_INACTIVITY                         |
| } adxl372_th_activity;                         |
|                                                |
| typedef enum {                                 |
|     ADXL372_FILTER_SETTLE_370,                 |
|     ADXL372_FILTER_SETTLE_16                   |
| } adxl372_filter_settle;                       |
|                                                |
| typedef enum {                                 |
|     ADXL372_XYZ_FIFO,                          |
|     ADXL372_X_FIFO,                            |
|     ADXL372_Y_FIFO,                            |
|     ADXL372_XY_FIFO,                           |
|     ADXL372_Z_FIFO,                            |
|     ADXL372_XZ_FIFO,                           |
|     ADXL372_YZ_FIFO,                           |
|     ADXL372_XYZ_PEAK_FIFO,                     |
| } adxl372_fifo_format;                         |
|                                                |
| typedef enum {                                 |
|     ADXL372_FIFO_BYPASSED,                     |
|     ADXL372_FIFO_STREAMED,                     |
|     ADXL372_FIFO_TRIGGERED,                    |
|     ADXL372_FIFO_OLD_SAVED                     |
| } adxl372_fifo_mode;                           |
|                                                |
| typedef struct {                               |
|     adxl372_fifo_mode fifo_mode;               |
|     adxl372_fifo_format fifo_format;           |
|     uint16_t fifo_samples;                     |
| } adxl372_fifo_config;                         |
|                                                |
| typedef struct {                               |
|     uint16_t thresh;                           |
|     bool referenced;                           |
|     bool enable;                               |
| } adxl372_activity_threshold;                  |
|                                                |
| typedef struct {                               |
|     uint16_t x;                                |
|     uint16_t y;                                |
|     uint16_t z;                                |
| } adxl372_xyz_accel_data;                      |
|                                                |
| typedef struct {                               |
|     bool data_rdy;                             |
|     bool fifo_rdy;                             |
|     bool fifo_full;                            |
|     bool fifo_ovr;                             |
|     bool inactivity;                           |
|     bool activity;                             |
|     bool awake;                                |
|     bool low_operation;                        |
| } adxl372_irq_config;                          |
|                                                |
| typedef struct {                               |
|     /* SPI */                                  |
|     spi_desc            *spi_desc;             |
|     /* GPIO */                                 |
|     gpio_desc           *gpio_int1;            |
|     gpio_desc           *gpio_int2;            |
|     /* Device Settings */                      |
|     adxl372_bandwidth       bw;                |
|     adxl372_odr         odr;                   |
|     adxl372_wakeup_rate     wur;               |
|     adxl372_act_proc_mode       act_proc_mode; |
|     adxl372_instant_on_th_mode  th_mode;       |
|     adxl372_fifo_config     fifo_config;       |
| } adxl372_dev;                                 |
|                                                |
| typedef struct {                               |
|     /* SPI */                                  |
|     spi_init_param          spi_init;          |
|     /* GPIO */                                 |
|     int8_t              gpio_int1;             |
|     int8_t              gpio_int2;             |
|     /* Device Settings */                      |
|     adxl372_bandwidth       bw;                |
|     adxl372_odr         odr;                   |
|     adxl372_wakeup_rate     wur;               |
|     adxl372_act_proc_mode       act_proc_mode; |
|     adxl372_instant_on_th_mode  th_mode;       |
|     adxl372_activity_threshold  activity_th;   |
|     adxl372_activity_threshold  activity2_th;  |
|     adxl372_activity_threshold  inactivity_th; |
|     uint8_t             activity_time;         |
|     uint16_t            inactivity_time;       |
|     adxl372_filter_settle       filter_settle; |
|     adxl372_fifo_config     fifo_config;       |
|     adxl372_irq_config      int1_config;       |
|     adxl372_irq_config      int2_config;       |
|     adxl372_op_mode         op_mode;           |
| } adxl372_init_param;``                        |
+------------------------------------------------+

No-OS Downloads
---------------

.. admonition:: Download
   :class: download

   
   -


   
   |adxl372 source and header files.|

.. |adxl372 source and header files.| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl372`
