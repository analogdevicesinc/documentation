Generic platform driver description
===================================

The **Generic Platform Driver** is where the specific communication functions for the desired type of processor and communication protocol have to be implemented. This driver implements the communication with the device and hides the actual details of the communication protocol to the specific device or family driver.

The **Generic Platform Driver** has a standard interface, so the device driver can be used exactly as it is provided. This standard interface includes the **I2C** and **SPI** communications, functions for managing **GPIOs** and a **miliseconds delay** function.

The **milisecond delay** functions is:

=============================== ===========================
Function                        Description
=============================== ===========================
``void mdelay(uint32_t msecs)`` Generate miliseconds delay.
=============================== ===========================

I2C interface
-------------

The **I2C** interface has the following functions:

+----------------------------------------------------------------------------------+----------------------------------------------+
| Function                                                                         | Description                                  |
+==================================================================================+==============================================+
| ``int32_t i2c_init(struct i2c_desc **desc, const struct i2c_init_param *param)`` | Initialize the I2C communication peripheral. |
+----------------------------------------------------------------------------------+----------------------------------------------+
| ``int32_t i2c_remove(struct i2c_desc *desc)``                                    | Free the resources allocated by i2c_init().  |
+----------------------------------------------------------------------------------+----------------------------------------------+
| ``int32_t i2c_write(struct i2c_desc *desc, uint8_t *data,                        | Write data to a slave device.                |
|     uint8_t bytes_number, uint8_t stop_bit)``                                    |                                              |
+----------------------------------------------------------------------------------+----------------------------------------------+
| ``int32_t i2c_read(struct i2c_desc *desc, uint8_t *data,                         | Read data from a slave device.               |
|     uint8_t bytes_number, uint8_t stop_bit)``                                    |                                              |
+----------------------------------------------------------------------------------+----------------------------------------------+

The following structs and enums are used for the **I2C** interface:

.. code:: c

   typedef enum i2c_type {
       GENERIC_I2C
   } i2c_type;

   typedef struct i2c_init_param {
       enum i2c_type   type;
       uint32_t    id;
       uint32_t    max_speed_hz;
       uint8_t     slave_address;
   } i2c_init_param;

   typedef struct i2c_desc {
       enum i2c_type   type;
       uint32_t    id;
       uint32_t    max_speed_hz;
       uint8_t     slave_address;
   } i2c_desc;

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/i2c_driver_architecture.png
   :align: center

SPI interface
-------------

The **SPI** interface has the following functions:

+----------------------------------------------------------------------------------+----------------------------------------------+
| Function                                                                         | Description                                  |
+==================================================================================+==============================================+
| ``int32_t spi_init(struct spi_desc **desc, const struct spi_init_param *param)`` | Initialize the SPI communication peripheral. |
+----------------------------------------------------------------------------------+----------------------------------------------+
| ``int32_t spi_remove(struct spi_desc *desc)``                                    | Free the resources allocated by spi_init().  |
+----------------------------------------------------------------------------------+----------------------------------------------+
| ``int32_t spi_write_and_read(struct spi_desc *desc, uint8_t *data,               | Write and read data to/from SPI.             |
|     uint8_t bytes_number)``                                                      |                                              |
+----------------------------------------------------------------------------------+----------------------------------------------+

The following structs and enums are used for the **SPI** interface:

.. code:: c

   typedef enum spi_type {
       GENERIC_SPI
   } spi_type;

   typedef enum spi_mode {
       SPI_MODE_0 = (0 | 0),
       SPI_MODE_1 = (0 | SPI_CPHA),
       SPI_MODE_2 = (SPI_CPOL | 0),
       SPI_MODE_3 = (SPI_CPOL | SPI_CPHA)
   } spi_mode;

   typedef struct spi_init_param {
       enum spi_type   type;
       uint32_t    id;
       uint32_t    max_speed_hz;
       enum spi_mode   mode;
       uint8_t     chip_select;
   } spi_init_param;

   typedef struct spi_desc {
       enum spi_type   type;
       uint32_t    id;
       uint32_t    max_speed_hz;
       enum spi_mode   mode;
       uint8_t     chip_select;
   } spi_desc;

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/spi_driver_architecture.png
   :align: center

GPIO interface
--------------

The **GPIO** interface has the following functions:

+----------------------------------------------------------------------------+----------------------------------------------------+
| Function                                                                   | Description                                        |
+============================================================================+====================================================+
| ``int32_t gpio_get(struct gpio_desc **desc, uint8_t gpio_number)``         | Obtain the GPIO decriptor.                         |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_remove(struct gpio_desc *desc)``                            | Free the resources allocated by gpio_get().        |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_direction_input(struct gpio_desc *desc)``                   | Enable the input direction of the specified GPIO.  |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_direction_output(struct gpio_desc *desc, uint8_t value)``   | Enable the output direction of the specified GPIO. |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_get_direction(struct gpio_desc *desc, uint8_t *direction)`` | Get the direction of the specified GPIO.           |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_set_value(struct gpio_desc *desc, uint8_t value)``          | Set the value of the specified GPIO.               |
+----------------------------------------------------------------------------+----------------------------------------------------+
| ``int32_t gpio_get_value(struct gpio_desc *desc, uint8_t *value)``         | Get the value of the specified GPIO.               |
+----------------------------------------------------------------------------+----------------------------------------------------+

The following structs and enums are used for the **GPIO** interface:

.. code:: c

   typedef enum gpio_type {
       GENERIC_GPIO
   } gpio_type;

   typedef struct gpio_desc {
       enum gpio_type  type;
       uint32_t    id;
       uint8_t     number;
   } gpio_desc;

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers-all/gpio_driver_architecture.png
   :align: center
