No-OS SPI API
=============

Description
-----------

The no-OS framework provides a common application programming interface to initialize and use a SPI peripheral across various target :git-no-OS:`platforms <drivers/platform>`.

The SPI API documentation is available as `Doxygen documentation <http://analogdevicesinc.github.io/no-OS/no__os__spi_8h.html>`_.

SPI device initialization
~~~~~~~~~~~~~~~~~~~~~~~~~

The no-OS framework provides a way to create a SPI slave device descriptor starting from user specified initialization parameters (*init params*). The init params are generic, defined by no-OS and applicable to all platforms. However, a certain platform may require passing extra initialization parameters that are specific to that platform. The **extra** member of the init params allows the user to pass such specific init params. The extra init params are of the type **[platform]_spi_init_param** as defined in [platform]_spi.h header.

.. code:: C

   struct [platform]_spi_init_param slave_xip = {
       .specific_parameter = value,
   };

   struct no_os_spi_init_param slave_ip = {
       .device_id = 2,
       .max_speed_hz = 4000000,
       .mode = NO_OS_SPI_MODE_3,
       .chip_select = 1,
       .platform_ops = &[platform]_spi_ops,
       .extra = &slave_xip
   };

Creating/removing a SPI slave device descriptor with the above parameters can be achieved with:

.. code:: C

   int ret;
   struct no_os_spi_desc *slave_desc;
   ret = no_os_spi_init(&slave_desc, &slave_ip);
   // ...
   // ... spi transfers
   // ...
   ret = no_os_spi_remove(slave_desc);

Such a descriptor is needed for each slave because each slave may require different communication settings. When performing transfers, the SPI peripheral is reconfigured with the SPI settings of the particular slave being targeted.

In the above example, the max_speed_hz parameter given is 4 MHz. The no_os_spi_init() function will choose such a SPI peripheral prescaler so that SCLK is guaranteed to be the closest possible value to 4 MHz, provided a fixed input clock and the range of available prescalers. For example, if the SPI input clock is 24 MHz and available prescalers are 1, 2, 4, 8, 16, 32, the no_os_spi_init() will choose the prescaler value of 8 which results in an SCLK clock frequency of 24 / 8 = 3 MHz.

Transfers
~~~~~~~~~

using no_os_spi_write_and_read
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case of full duplex 4-wire SPI transfers, both MISO and MOSI lines are used to simultaneously shift in/out data. The way no_os_spi_write_and_read() works is by first shifting out data buffer on MOSI and then and then by replacing the data buffer content with data shifted in from MISO.

.. code:: C

   uint8_t data[2];
   data[0] = 0xAB;
   ret = no_os_spi_write_and_read(slave_desc, data, 1);
   if (ret < 0)
       ; // take action

   printf("Received on MISO: 0x%x\n", data[0]);

   data[0] = 0xBC;
   data[1] = 0xCD;
   ret = no_os_spi_write_and_read(slave_desc, data, 2);
   if (ret < 0)
       ; // take action

   printf("Received on MISO: 0x%x 0x%x\n", data[0], data[1]);

using no_os_spi_transfer
^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   no_os_spi_transfer() is not necessarily available on each no-OS platform! See drivers/platform/[platform]/[platform]_spi.c


An alternative way is using the no_os_spi_transfer() which splits a transfer sequence into basic transfers. A basic transfer contains transmit and receive buffers, the size of the transfer and the option to deassert the chip select signal after each basic transfer.

The following sequence can be broken down into two transfer phases (0x?? - don't care):

::

   MOSI: 0xAA 0x?? 0x??
   MISO: 0x?? 0xBB 0xCC

The two transfer phases are:

-  Transmit 1 byte (0xAA) on MOSI without deasserting the chip select
-  Receive 2 bytes (0xBB 0xCC) on MISO

.. code:: C

   struct no_os_spi_msg msgs[2] = { 0 };

   uint8_t tx[1] = {0xAA};
   uint8_t rx[2];

   msgs[0].bytes_number = 1;
   msgs[0].tx_buff = tx;
   msgs[0].cs_change = false;

   msgs[1].bytes_number = 2;
   msgs[1].rx_buff = rx;
   msgs[1].cs_change = true;

   ret = no_os_spi_transfer(slave_desc, msgs, NO_OS_ARRAY_SIZE(msgs));
   if (ret < 0)
       ; // take action

   // here, rx contains 2 bytes: {0xBB, 0xCC} received from slave
