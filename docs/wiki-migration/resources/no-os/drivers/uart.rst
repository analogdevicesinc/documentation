No-OS UART API
==============

Description
-----------

The no-OS framework provides a common application programming interface to initialize and use an UART across various target :git-no-OS:`platforms <drivers/platform>`.

Interface documentation
-----------------------

The UART interface documentation is generated using the Doxygen tool and it is available at:

-  `No-OS UART API <http://analogdevicesinc.github.io/no-OS/no__os__uart_8h.html>`_

Interface usage
---------------

UART device initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~

The no-OS framework provides a way to create a UART device driver starting from user specified initialization parameters (*init params*). The init params are generic, defined by no-OS and applicable to all platforms. However, a certain platform may require passing extra initialization parameters that are specific to that platform. The **extra** member of the init params allows the user to pass such specific init params. The extra init params are of the type **[platform]_uart_init_param**.

.. code:: C

   struct [platform]_uart_init_param xuip = {
       .specific_param = value,
   };
   struct no_os_uart_init_param uip = {
       .device_id = 1,
       .baud_rate = 115200,
       .size = NO_OS_UART_CS_8,
       .parity = NO_OS_UART_PAR_NO,
       .stop = NO_OS_UART_STOP_1_BIT,
       .extra = &xuip,
   };

Creating/removing a UART device descriptor with the above parameters can be achieved with:

.. code:: C

   int ret;
   struct no_os_uart_desc *ud;
   ret = no_os_uart_init(&ud, &uip);
   // ...
   // ... transmit / receive
   // ...
   ret = no_os_uart_remove(ud);

The above code calls platform specific initialization routines that configure the physical UART instance (in this example UART1) with the provided settings (in this example 115200 baudrate, 8 data bits, no parity bit, 1 stop bit).

Transmitting and receiving
~~~~~~~~~~~~~~~~~~~~~~~~~~

You may then use the created UART device descriptor **ud** to transmit or receive data over the UART.

Blocking
^^^^^^^^

.. code:: C

   char *string = "Hello!\n";
   ret = no_os_uart_write(ud, string, strlen(string));
   // ... blocking call, when execution returns from the function, the data was sent over UART

.. code:: C

   char string[10];
   ret = no_os_uart_read(ud, string, 10);
   // ... blocking call, returns from function when all 10 characters were received

Nonblocking
^^^^^^^^^^^

Some applications require listening on the UART Rx continuously for incoming characters. The characters may come at an arbitrary time and the number of characters may also be arbitrary. For this scenario, no_os_uart_read can be configured in nonblocking mode by the use of the following init params:

.. code:: C

   struct no_os_uart_init_param uip = {
       // ...
       .asynchronous_rx = true,
       .irq_id = 2,
   };

If asynchronous_rx is enabled, it is mandatory to fill the irq_id field as well. The UART is configured in such a way that after each received character, the provided interrupt (irq_id) is triggered, and the received character is copied into a software buffer. Therefore, the no_os_uart_read function simply reads characters from this software buffer instead of reading characters from the UART peripheral.
