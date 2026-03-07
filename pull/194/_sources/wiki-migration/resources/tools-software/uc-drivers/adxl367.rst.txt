ADXL367 No-OS Driver
====================

Supported Devices
-----------------

-  :adi:`ADXL367`

Overview
--------

The :adi:`ADXL367` is an ultralow power, 3-axis microelectromechanical systems (MEMS) accelerometer that consumes only 0.89 μA at a 100 Hz output data rate and 180 nA when in motion-triggered wake-up mode. Unlike accelerometers that use power duty cycling to achieve low power consumption, the :adi:`ADXL367` does not alias input signals by undersampling, but samples the full bandwidth of the sensor at all data rates.

The :adi:`ADXL367` always provides 14-bit output resolution. 8-bit formatted data is offered for more efficient single-byte transfers when a lower resolution is sufficient. 12-bit formatted data is also provided for ADXL362 design compatibility. Measurement ranges of ±2 g, ±4g, and ±8 g are available, with a resolution of 0.25 mg/LSB on the ±2 g range.

In addition to its ultralow power consumption, the :adi:`ADXL367` has many features to enable true system level power reduction. It includes a deep multimode output first in, first out (FIFO), a built-in micropower temperature sensor, an internal analog-to-digital converter (ADC) for synchronous conversion of an additional analog input with interrupt capability, single-tap and double-tap detection that can operate at any output data rate with only an added 35nA of current, and a state machine to prevent a false triggering. In addition, the :adi:`ADXL367` has provisions for external control of the sampling time and/or an external clock.

The :adi:`ADXL367` operates on a wide 1.1 V to 3.6 V supply range, and can interface, if necessary, to a host operating on a separate supply voltage. It is available in a 2.2 mm × 2.3 mm × 0.87mm package.

Applications
~~~~~~~~~~~~

-  24/7 sensing
-  Hearing aids
-  Vital signs monitoring devices
-  Motion-enabled power save switches
-  Motion-enabled metering devices
-  Smart watch with single-cell operation
-  Smart home

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/eval-adxl367-sdp-angle-web.gif
   :align: center
   :width: 400px

ADI No-OS
---------

The goal of ADI Microcontroller No-OS is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. ADI No-OS offers **generic drivers** which can be used as a base for any microcontroller platform and also **example projects** which are using these drivers on various microcontroller platforms.

For more information about ADI No-OS and supported microcontroller platforms see: :doc:`no-OS </wiki-migration/resources/no-os>`

ADXL367 ADI No-OS driver
------------------------

ADXL367 Driver Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for ADXL367 driver can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADXL367 Driver|

   -

   |Implementation of ADXL367 Driver|

The driver also uses the ADI util, delay and print_log libraries, so make sure you also add the necessary files in your project. The source code for the libraries can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADI util library|

   -

   |Implementation file of ADI util library|

   -

   |Header of ADI delay library|

   -

   |Implementation file of ADI delay library for Xilinx (use the one for the used platform)|

   -

   |Header of ADI print_log library|

In order to be able to use this driver you will have to provide the specific implementation for the communication APIs and the specific types they use. If the SPI communication is chosen, there are three functions which are called by the ADXL367 driver and have to be implemented:

-  no_os_spi_init() – initializes the communication peripheral.
-  no_os_spi_write_and_read() – writes and reads data to/from the device.
-  no_os_spi_remove() – deinitializes the communication peripheral.

And there are two data types that have to be defined:

-  no_os_spi_desc - structure holding the SPI descriptor
-  no_os_spi_init_param - structure holding the parameters for SPI initialization

If the I2C communication is chosen, there are four functions which are called by the ADXL367 driver:

-  i2c_init() – initializes the communication peripheral.
-  i2c_write() – writes data to the device.
-  i2c_read() – reads data from the device.
-  i2c_remove() – deinitializes the communication peripheral.

And there are two data types that have to be defined:

-  no_os_i2c_desc - structure holding the I2C descriptor
-  no_os_i2c_init_param - structure holding the parameters for I2C initialization

An example of a header file containing the prototypes of the functions which have to be implemented, along with some generic data types they are using can be found below:

.. admonition:: Download
   :class: download

   
   -


   
   |Generic header file for SPI Communication APIs|

   -

   |Generic header file for I2C Communication APIs|

ADXL367 Code Driver Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:

-  `ADXL367 Header file <http://analogdevicesinc.github.io/no-OS/adxl367_8h.html>`_
-  `ADXL367 Source file <http://analogdevicesinc.github.io/no-OS/adxl367_8c.html>`_

ADXL367 Device Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Driver Initialization
~~~~~~~~~~~~~~~~~~~~~

In order to be able to use the device, you will have to provide the support for the communication protocol (SPI or I2C) as mentioned above. The first API to be called is **adxl367_init**. Make sure that it returns 0, which means that the driver was initialized correctly.

Range Configuration
~~~~~~~~~~~~~~~~~~~

By default, the device uses +/- 2g range configuration. You may modify this value to +/- 4g or +/- 8g by using **adxl367_set_range** API.

Axis Calibration Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may set an offset for each axis for calibration purposes by using **adxl367_set_offset**. The offset is disabled by default. The data provided in **adxl367_set_offset** will be in two's complement format. The offset is added after all other signal processing is taking place.

FIFO Configuration
~~~~~~~~~~~~~~~~~~

There are 513 locations in the FIFO. Each location contains an acceleration data point on an axis. In case you want to use the FIFO, you are able to modify the number of FIFO samples to be stored in the FIFO. The default and maximum value is 513, but can be modified using **adxl367_set_fifo_sample_sets_nb** API. A full set-up for FIFO can be done using **adxl367_fifo_setup** API.

Activity Detection Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to use the activity detection algorithm, you can enable this feature on any axis using **adxl367_setup_activity_detection** API. By default the activity detection feature is disabled. You will have to specify a threshold for the activity detection and a number of consecutive measurements above the threshold which would trigger the detection of an activity.

Inactivity Detection Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to use the inactivity detection algorithm, you can enable this feature on any axis using **adxl367_setup_inactivity_detection** API. By default the activity detection feature is disabled. You will have to specify a threshold for the inactivity detection and a number of consecutive measurements below the threshold which would trigger the detection of an inactivity.

Interrupts Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

The device allows the usage of interrupts which can be mapped to INT1 or INT2 pins. In case you want to use interrupts, make sure you configure the interrupt map by using **adxl367_int_map** API.

The following events can be mapped to the interrupt pins:

-  DATA READY interrupt - it is triggered when new acceleration data is available to the interface and it is cleared on a read of data register, using **adxl367_read_raw_temp** API.
-  FIFO WATERMARK interrupt - it is triggered when the entries in the FIFO are equal to the setting made when calling **adxl367_set_fifo_sample_sets_nb** API. It is cleared when the number of entries in the FIFO is less than the number of samples set by **adxl367_set_fifo_sample_sets_nb** API.
-  FIFO OVERRUN interrupt - it is triggered when the FIFO is so far overrange that data is lost. The specified side of the FIFO is 513 locations. The interrupt is triggered only when there is an attempt to write past this 513-location limit.
-  FIFO READY interrupt - it is set if there is at least one sample available in the FIFO output buffer.
-  ACTIVITY interrupt - it is set when the measured acceleration on any axis is above the set threshold, using **adxl367_setup_activity_detection** API. A read of the status register clears the interrupt, but this interrupt is triggered again at the end of the next measurement if the activity conditions are still satisfied.
-  INACTIVITY interrupt - it is set when the measured acceleration on any axis is below the set threshold, using **adxl367_setup_inactivity_detection** API. A read of the status register clears the interrupt, but this interrupt is triggered again at the end of the next measurement if the inactivity conditions are still satisfied.
-  AWAKE interrupt - it is set if the accelerometer is in an active state (AWAKE = 1)

ADXL367 Device Measurements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Operation Mode Setting
~~~~~~~~~~~~~~~~~~~~~~

After the specific configuration was performed as mentioned above, you can set the device in the desired measurement mode, using **adxl367_set_power_mode** API. The available operation modes for measurement are as follows:

-  ADXL367_OP_MEASURE - measurement mode
-  ADXL367_OP_STANDBY - stand-by mode, mode in which the configuration of the device should be done

Temperature Data
~~~~~~~~~~~~~~~~

By using **adxl367_temp_read_en**, temperature data can be enabled. Data can be obtained by calling **adxl367_read_temperature** API. The temperature is Celsius degrees, with scaling already applied.

If you want to obtain the raw temperature data without any scaling applies, simply call **adxl367_read_raw_temp** API.

Acceleration Data
~~~~~~~~~~~~~~~~~

Single Data Set
^^^^^^^^^^^^^^^

If you want to obtain a single data set, you may use **adxl367_get_g_xyz** API to obtain the data converted to g, or **adxl367_get_raw_xyz** API to obtain the raw data. The raw data is in two's complement format and it does not have the scaling applied.

FIFO Data
^^^^^^^^^

If you want to read from the FIFO, you may use **adxl367_read_converted_fifo** API to obtain the data converted to g and Celsius degrees for temperature, or **adxl367_read_raw_fifo** api to obtain the raw data. The raw data is in two's complement format and it does not have the scaling applied. The parameter **entries** shows the number of valid measurements in the FIFO which were read.

ADXL367 Driver Initialization Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPI Communication Example
~~~~~~~~~~~~~~~~~~~~~~~~~

::

   // Particular SPI configuration
   struct no_os_spi_init_param spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = 100000,
       .mode = NO_OS_SPI_MODE_0,
       .chip_select = 0U,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .platform_ops = SPI_OPS,
       .extra = &spi_extra
   };

   struct adxl367_init_param init_param = {
       .spi_init = spi_ip,
       .comm_type = ADXL367_SPI_COMM
   };
   // Device descriptor
   struct adxl367_dev *dev;

   adxl367_init(&dev, init_param);

   adxl367_self_test(dev);

   adxl367_temp_read_en(dev, 1);

   adxl367_set_output_rate(dev, ADXL367_ODR_200HZ);

   adxl367_fifo_setup(dev, ADXL367_OLDEST_SAVED, ADXL367_FIFO_FORMAT_XYZT, 50);

   //be sure to make all configs before switching to measure mode
   adxl367_set_power_mode(dev, ADXL367_OP_MEASURE);

   uint16_t entries;
   struct adxl367_fractional_val x[128], y[128], z[128], temp[128];

   adxl367_read_converted_fifo(dev, x, y, z, temp, &entries);

   pr_info("Number of read entries from the FIFO %d \n", entries);

   for (uint8_t i = 0; i < entries / 4; i ++) {
       pr_info("x=%d"".%09u m/s^2\n", (int)x[i].integer, (abs)(x[i].fractional));
       pr_info("y=%d"".%09u m/s^2\n", (int)y[i].integer, (abs)(y[i].fractional));
       pr_info("z=%d"".%09u m/s^2\n", (int)z[i].integer, (abs)(z[i].fractional));
       pr_info("temp=%d"".%09u C\n", (int)temp[i].integer, (abs)(temp[i].fractional));
       pr_info("\n");
   }

ADI IIO No-OS
-------------

ADXL367 IIO No-OS driver
------------------------

The ADXL367 IIO driver comes on top of ADXL367 driver and offers support for interfacing IIO clients through IIO lib.

ADXL367 IIO Device Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Device Attributes
~~~~~~~~~~~~~~~~~

ADXL367 IIO device does not have any device specific attributes.

Device Channels
~~~~~~~~~~~~~~~

ADXL367 IIO device has 0 input channels and 4 output channels: 3 acceleration channels and 1 temperature channel.

Acceleration channels
^^^^^^^^^^^^^^^^^^^^^

The acceleration channels are:

-  Channel 0: X axis
-  Channel 1: Y axis
-  Channel 2: Z axis

Each acceleration channel has 6 attributes. 4 of these attributes are shared in value with the other acceleration channels and 2 of these attributes can have different values for each channel.

The attributes are:

-  calibbias - offset added to the axis after all other signal processing. The calibbias value will be applied as an offset to the raw value bits.
-  raw - is the raw acceleration value read from the device.
-  sampling_frequency (shared) - is the sampling frequency for acceleration data. This value is common for all three acceleration channels and for temperature, too.
-  sampling_frequency_available (shared) - is the list of available sampling frequency values. This list is common for all three acceleration channels.
-  scale (shared) - is the scale that has to be applied to the raw value in order to obtain the converted real value in m/s^2.
-  scale_available (shared) - lists the available scale options (in this way device's range can be modified)

::

   converted_accel [m/s^2] = (raw + calibbias) * scale 

Temperature channel
^^^^^^^^^^^^^^^^^^^

The temperature channel is:

-  Channel 4: temp

The channel has 3 attributes, as follows:

-  offset - is the offset that has to be applied to the raw value in order to obtain the converted real value in degrees Celsius.
-  raw - is the raw temperature value read from the device.
-  scale - is the scale that has to be applied to the raw value in order to obtain the converted real value in degrees Celsius.

::

   converted_temp [degrees Celsius] = (raw + offset) * scale 

Device buffers
~~~~~~~~~~~~~~

The ADXL367 IIO devices driver supports the usage of a data buffer for reading purposes.

ADXL367 IIO Driver Initialization Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   #define DATA_BUFFER_SIZE 400
   uint8_t iio_data_buffer[DATA_BUFFER_SIZE\*4*sizeof(int16_t)];

   struct adxl367_iio_dev *adxl367_iio_desc;
   struct adxl367_iio_init_param adxl367_init_par;

   // Particular SPI configuration
   struct no_os_spi_init_param spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = 100000,
       .mode = NO_OS_SPI_MODE_0,
       .chip_select = 0U,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .platform_ops = SPI_OPS,
       .extra = &spi_extra
   };

   struct adxl367_init_param init_param = {
       .spi_init = spi_ip,
       .comm_type = ADXL367_SPI_COMM
   };

   struct iio_data_buffer accel_buff = {
       .buff = (void *)iio_data_buffer,
       .size = DATA_BUFFER_SIZE\*4*sizeof(int16_t)
   };

   adxl367_iio_ip.adxl367_initial_param = &init_param;
   adxl367_iio_init(&adxl367_iio_desc, &adxl367_iio_ip);

   struct iio_app_device iio_devices[] = {
       {
           .name = "adxl367",
           .dev = adxl367_iio_desc,
           .dev_descriptor = adxl367_iio_desc->iio_dev,
           .read_buff = &accel_buff,
       }
   };

   return iio_app_run(iio_devices, NO_OS_ARRAY_SIZE(iio_devices));

.. |Header file of ADXL367 Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl367/adxl367`.h
.. |Implementation of ADXL367 Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl367/adxl367`.c
.. |Header file of ADI util library| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_util`.h
.. |Implementation file of ADI util library| image:: https://wiki.analog.com/_media/:git-no-OS:`util/no_os_util`.c
.. |Header of ADI delay library| image:: https://wiki.analog.com/_media/:git-no-OS:`util/no_os_delay`.h
.. |Implementation file of ADI delay library for Xilinx (use the one for the used platform)| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/platform/xilinx/delay`.c
.. |Header of ADI print_log library| image:: https://wiki.analog.com/_media/:git-no-OS:`util/no_os_print_log`.h
.. |Generic header file for SPI Communication APIs| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_spi`.h
.. |Generic header file for I2C Communication APIs| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_i2c`.h
