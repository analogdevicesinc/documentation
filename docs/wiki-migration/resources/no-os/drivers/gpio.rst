No-OS GPIO API
==============

Description
-----------

The GPIO framework provides a way to handle General-Purpose Input/Output (GPIO) pins when using the No-OS platform drivers.

Interface Documentation
-----------------------

The GPIO interface documentation is generated using the Doxygen tool and it is available at:

-  `No-OS GPIO API <http://analogdevicesinc.github.io/no-OS/no__os__gpio_8h.html>`__

Initialization example
----------------------

GPIO initialization
~~~~~~~~~~~~~~~~~~~

.. code:: C


   /* GPIO Description declaration */
   struct no_os_gpio_desc *gpio_desc;

   /* GPIO Initialization Parameters */
   struct no_os_gpio_init_param gpio_param = {
       /** Port number */
       .port = 0,
       /** Pull up/down resistor configuration */
       .pull = NO_OS_PULL_NONE,
       /** GPIO Number */
       .number = GPIO_1,
       /** GPIO platform specific functions (Xilinx Platform in this particular example) */
       .platform_ops = &xil_gpio_ops,
       /** GPIO extra parameters (device specific) */
       .extra = &xil_gpio_param
   };

   /* Obtain the GPIO decriptor. */
   ret = no_os_gpio_get(&gpio_desc, &gpio_param);
   if (ret)
       return -1;

   /* Free the resources allocated by no_os_gpio_get(). */
   ret = no_os_gpio_remove(gpio_desc);
   if (ret)
       return -1;

Alternatively, if the a specific gpio is optional, the \`no_os_gpio_get_optional\` function can be used instead of \`no_os_gpio_get\`.

GPIO Usage
~~~~~~~~~~

.. code:: C

   /* Enable the input direction of the specified GPIO. */
   ret = no_os_gpio_direction_input(gpio_desc);
   if (ret)
       return -1;

   /* Enable the output direction of the specified GPIO with logic level high. */
   ret = no_os_gpio_direction_output(gpio_desc, NO_OS_GPIO_HIGH);
   if (ret)
       return -1;

   /* Enable the output direction of the specified GPIO with logic level low. */
   ret = no_os_gpio_direction_output(gpio_desc, NO_OS_GPIO_LOW);
   if (ret)
       return -1;

   /* Get the direction of the specified GPIO. */
   uint8_t dir;
   ret = no_os_gpio_get_direction(gpio_desc, &dir);
   if (ret)
       return -1;

   /* Set the value of the specified GPIO with logic level high. */
   ret = no_os_gpio_set_value(gpio_desc, NO_OS_GPIO_HIGH);
   if (ret)
       return -1;

   /* Set the value of the specified GPIO with logic level low. */
   ret = no_os_gpio_set_value(gpio_desc, NO_OS_GPIO_LOW);
   if (ret)
       return -1;

   /* Get the value of the specified GPIO. */
   enum no_os_gpio_values val;
   ret = no_os_gpio_get_value(gpio_desc, &val);
   if (ret)
       return -1;
