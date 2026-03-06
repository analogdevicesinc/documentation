ADXL313 No-OS Driver
====================

Supported Devices
-----------------

-  :adi:`ADXL312`
-  :adi:`ADXL313`
-  :adi:`ADXL314`

Overview
--------

The :adi:`ADXL312` is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement up to ±12 g. More information about the device can be found :adi:`here <en/products/adxl312.html#product-overview>`.

The :adi:`ADXL313` is a small, thin, low power, 3-axis accelerometer with high resolution (13-bit) measurement up to ±4g. More information about the device can be found :adi:`here <en/products/adxl313.html#product-overview>`.

The :adi:`ADXL314` is a small, thin, 3-axis accelerometer that provides low power consumption and high-resolution measurement of ±200 g. More information about the device can be found :adi:`here <en/products/adxl313.html#product-overview>`.

Digital output data is formatted as 16-bit twos complement and is accessible through either a serial port interface (SPI) (3- or 4-wire) or I2C digital interface.

Applications
~~~~~~~~~~~~

-  Car alarm (ADXL312, ADXL313)
-  Black box (ADXL312, ADXL313)
-  Smart tire (ADXL314)
-  High force detection (ADXL314)

Breakout Board
~~~~~~~~~~~~~~

Each device is mounted on a simple breakout board that enables easy connection into an existing system.

-  :adi:`EVAL-ADXL312Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adxl312.html#eb-overview>`
-  :adi:`EVAL-ADXL313Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adxl313.html#eb-overview>`
-  :adi:`EVAL-ADXL314Z <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADXL314Z.html>`

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/adi/eval-adxl312zangle-web.png
   :alt: EVAL-ADXL312Z
   :align: center
   :width: 200px

ADI No-OS
---------

The goal of ADI Microcontroller No-OS is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. ADI No-OS offers **generic drivers** which can be used as a base for any microcontroller platform and also **example projects** which are using these drivers on various microcontroller platforms.

For more information about ADI No-OS and supported microcontroller platforms see: :doc:`no-OS </wiki-migration/resources/no-os>`.

ADXL313 ADI No-OS driver
------------------------

ADXL313 Driver Source Code
^^^^^^^^^^^^^^^^^^^^^^^^^^

The source code for the ADXL313 driver:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADXL313 Driver|

   -

   |Implementation of ADXL313 Driver|

The driver also uses the ADI util library, so make sure you also add the necessary files in your project. The source code for the util library:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADI util library|

   -

   |Implementation file of ADI util library|

In order to be able to use this driver you will have to provide the specific implementation for the communication APIs and the specific types they use. If the SPI communication is chosen, there are three functions which are called by the ADXL313 driver and have to be implemented:

-  no_os_spi_init() – initializes the communication peripheral,
-  no_os_spi_write_and_read() – writes and reads data to/from the device,
-  no_os_spi_remove() – deinitializes the communication peripheral.

And there are two data types that have to be defined:

-  no_os_spi_desc - structure holding the SPI descriptor,
-  no_os_spi_init_param - structure holding the parameters for SPI initialization.

If the I2C communication is chosen, there are four functions which are called by the ADXL313 driver:

-  i2c_init() – initializes the communication peripheral,
-  i2c_write() – writes data to the device,
-  i2c_read() – reads data from the device,
-  i2c_remove() – deinitializes the communication peripheral.

And there are two data types that have to be defined:

-  no_os_i2c_desc - structure holding the I2C descriptor,
-  no_os_i2c_init_param - structure holding the parameters for SPI initialization.

Example of a header file containing the prototypes of the functions which have to be implemented, along with some generic data types they are using:

.. admonition:: Download
   :class: download

   
   -


   
   |Generic header file for SPI Communication APIs|

   -

   |Generic header file for I2C Communication APIs|

ADXL313 Code Driver Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available at:

-  `ADXL313 Header file <http://analogdevicesinc.github.io/no-OS/adxl313_8h.html>`__,
-  `ADXL313 Source file <http://analogdevicesinc.github.io/no-OS/adxl313_8c.html>`__.

ADXL313 Device Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Driver Initialization
~~~~~~~~~~~~~~~~~~~~~

.. note::

   Some of the routines described below do not apply to all supported devices. In such cases, the text specifies to which device the instruction applies.


In order to be able to use the device, you will have to provide the support for the communication protocol (SPI or I2C) as mentioned above. The first API to be called is **adxl313_init**. Make sure that it returns 0, which means that the driver was initialized correctly.

After initialization, a soft reset can be performed (only for ADXL313), by calling **adxl313_soft_reset**, in order to reset the device. The driver reads the device settings saved in the device's registers in the initialization phase.

Range Configuration
~~~~~~~~~~~~~~~~~~~

By default, the device uses the minimum range configuration (valid for ADXL312 and ADXL313; ADXL314 has fixed range). You may modify this value by using **adxl313_set_range** API.

Axis Calibration Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may set an offset for each axis for calibration purposes by using **adxl313_set_offset**. The offset is set to 0 by default. The data provided in **adxl313_set_offset** is in twos complement format, with a scale factor depending on device. The value stored in the offset registers is automatically added to the acceleration data, and the resulting value is stored in the output data registers.

FIFO Configuration
~~~~~~~~~~~~~~~~~~

The devices contain patent pending technology for an embedded memory management system with a 32-level :adi:`FIFO <media/cn/technical-documentation/application-notes/AN-1025.pdf?doc=ADXL375.pdf>` that can be used to minimize host processor burden. This buffer has four modes: bypass, FIFO, stream, and trigger. Each mode is selected by the using the **adxl313_set_fifo_mode** function.

In case you want to use the FIFO, you can to modify the number of FIFO samples to be stored in the FIFO. The default and maximum value is 32 samples (3 values per sample, one for each axis), but can be modified using the **adxl313_set_fifo_samples** API.

Activity/Inactivity Detection Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you want to use the activity / inactivity detection algorithm, you can enable this feature on any axis using the **adxl313_set_activity_detection** / **adxl313_set_inactivity_detection** API.

Interrupts Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

The device allows the usage of interrupts which can be mapped to INT1 or INT2 pins. In case you want to use interrupts, make sure you configure the interrupt pin by using **adxl313_interrupt_int_map** API, where **interrupt** is replaced with the desired interrupt (**data_ready**, **activity**, **inactivity**, **watermark**, **overrun**). You may also configure the polarity of the interrupt, whether is active high or active low, by using **adxl313_set_int_pol** API.

ADXL313 Device Measurements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Operation Mode Setting
~~~~~~~~~~~~~~~~~~~~~~

It is recommended that the device be configured in standby mode before measurement mode is enabled. The setting of the operation mode is performed through the use of the **adxl313_set_op_mode** function.

Acceleration Data
~~~~~~~~~~~~~~~~~

Single Data Set
"""""""""""""""

If you want to obtain a single data set, you may use the **adxl313_get_xyz** API to obtain the data converted to g, or the **adxl313_get_raw_xyz** API to obtain the raw data. The raw data is in two's complement format and it does not have the scaling applied.

FIFO Data
"""""""""

If you want to read from the :adi:`FIFO <media/cn/technical-documentation/application-notes/AN-1025.pdf?doc=ADXL375.pdf>`, you may use the **adxl313_get_fifo_data** API to obtain the data converted to g or the **adxl313_get_raw_fifo_data** API to obtain the raw data. The raw data is in two's complement format and it does not have the scaling applied. The parameter **fifo_entries** shows the number of valid measurements in the FIFO which were read.

ADXL313 Driver Initialization Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPI Communication Example
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: C

   struct adxl313_dev *adxl313;
   /* Particular SPI configuration */
   struct no_os_spi_init_param sip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_MAX_HZ,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_0,
       .extra = &xsip,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
   };

   struct adxl313_init_param adxl313_user_init = {
       .dev_type = ID_ADXL313,
       .comm_type = ADXL313_SPI_COMM,
   };

   /* Initialize component. */
   ret = adxl313_init(&adxl313, adxl313_user_init);
   if (ret)
       goto error;

   /* Perform device self-test. */
   ret = adxl313_self_test(adxl313);
   if (ret)
       goto error;

   /* Set Standby mode, required for performing setup. */
   ret = adxl313_set_op_mode(adxl313, ADXL313_STDBY);
   if (ret)
       goto error;

   /* Set output data rate. */
   ret = adxl313_set_odr(adxl313, ADXL313_ODR_800HZ);
   if (ret)
       goto error;

   /* Put device in Measure mode after setup. */
   ret = adxl313_set_op_mode(adxl313, ADXL313_MEAS);
   if (ret)
       goto error;

   /* Read single accel data */
   struct adxl313_frac_repr x;
   struct adxl313_frac_repr y;
   struct adxl313_frac_repr z;

   ret = adxl313_get_xyz(adxl313,&x, &y, &z);
   if (ret < 0)
       goto error;

   /* Read FIFO accel data */
   struct adxl313_frac_repr x[32] = {0};
   struct adxl313_frac_repr y[32] = {0};
   struct adxl313_frac_repr z[32] = {0};
   uint8_t fifo_entries = 0;
   ret = adxl313_get_fifo_data(adxl313, &fifo_entries, &x[0], &y[0], &z[0]);
   if (ret < 0)
       goto error;

ADXL313 Driver Application Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Application Example Projects for ADXL313 driver: :doc:`Evaluating the ADXL313 </wiki-migration/resources/eval/user-guides/eval-adxl313z/no-os-setup>`.

ADI IIO No-OS
-------------

More on :doc:`no-OS IIO </wiki-migration/resources/tools-software/no-os-software/iio>`.

ADXL313 IIO No-OS driver
^^^^^^^^^^^^^^^^^^^^^^^^

The ADXL313 IIO driver comes on top of ADXL313 driver and offers support for interfacing IIO clients through IIO lib.

ADXL313 IIO Driver Source Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Source code for ADXL313 driver:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADXL313 IIO Driver|

   -

   |Implementation of ADXL313 IIO Driver|

ADXL313 IIO Code Driver Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Source code documentation for the IIO driver is automatically generated using the Doxygen tool and it is available at:

-  `ADXL313 IIO Header file <http://analogdevicesinc.github.io/no-OS/iio__adxl313_8h.html>`__
-  `ADXL313 IIO Source file <http://analogdevicesinc.github.io/no-OS/iio__adxl313_8c.html>`__

ADXL313 IIO Device Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Device Attributes
~~~~~~~~~~~~~~~~~

The ADXL313 IIO device does not have any device specific attributes.

Device Channels
~~~~~~~~~~~~~~~

The ADXL313 IIO device has 0 input channels and 3 output channels, corresponding to the acceleration on the three axes.

The acceleration channels are:

-  Channel 0: accel_x,
-  Channel 1: accel_y,
-  Channel 2: accel_z.

Each acceleration channel has 8 attributes. 6 of these attributes are shared in value with the other acceleration channels and 2 of these attributes can have different values for each channel.

The attributes are:

-  calibbias - offset added to the corresponding axis. It will be applied as an offset to the raw value bits;
-  raw - raw acceleration value read from the device;
-  sampling_frequency (shared) - sampling frequency for acceleration data;
-  sampling_frequency_available (shared) - list of available sampling frequency values;
-  range (shared) - selected range (applicable for ADXL312 and ADXL313);
-  range_available (shared) - list of available ranges for selected device;
-  scale (shared) - is the scale that has to be applied to the raw value in order to obtain the converted real value in m/s^2 (depends on device and on the currently selected range);
-  scale_available (shared) - list of available scales for current range.

ADXL314 IIO Driver Initialization Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: C

   struct adxl313_iio_dev *adxl313_iio_desc;
   struct adxl313_iio_dev_init_param adxl313_init_par;

   struct no_os_spi_init_param sip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_MAX_HZ,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_0,
       .extra = &xsip,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
   };

   struct adxl313_init_param adxl313_user_init = {
       .dev_type = ID_ADXL313,
       .comm_type = ADXL313_SPI_COMM,
   };

   adxl313_init_par.adxl313_dev_init = &adxl313_user_init;
   ret = adxl313_iio_init(&adxl313_iio_desc, &adxl313_init_par);
   if (ret)
       return ret;

   switch(adxl313_iio_desc->adxl313_dev->dev_type) {
   case ID_ADXL312:
       dev_name = "ADXL312";
       break;
   case ID_ADXL313:
       dev_name = "ADXL313";
       break;
   case ID_ADXL314:
       dev_name = "ADXL314";
       break;
   default:
       return -ENODEV;
   }

   struct iio_app_device iio_devices[] = {
       {
           .name = dev_name,
           .dev = adxl313_iio_desc,
           .dev_descriptor = adxl313_iio_desc->iio_dev,
       }
   };

   return iio_app_run(iio_devices, NO_OS_ARRAY_SIZE(iio_devices));

ADXL313 IIO Driver Application Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Application Example Project for the ADXL313 IIO driver: :doc:`Evaluating the ADXL313 </wiki-migration/resources/eval/user-guides/eval-adxl313z/no-os-setup>`.

.. |Header file of ADXL313 Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl313/adxl313`.h
.. |Implementation of ADXL313 Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl313/adxl313`.c
.. |Header file of ADI util library| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_util`.h
.. |Implementation file of ADI util library| image:: https://wiki.analog.com/_media/:git-no-OS:`util/no_os_util`.c
.. |Generic header file for SPI Communication APIs| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_spi`.h
.. |Generic header file for I2C Communication APIs| image:: https://wiki.analog.com/_media/:git-no-OS:`include/no_os_i2c`.h
.. |Header file of ADXL313 IIO Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl313/iio_adxl313`.h
.. |Implementation of ADXL313 IIO Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/accel/adxl313/iio_adxl313`.c
