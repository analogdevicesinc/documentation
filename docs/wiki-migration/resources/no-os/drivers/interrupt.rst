No-OS Interrupts API
====================

Description
-----------

The IRQ framework provides a way to handle peripheral (external) interrupts when using the No-OS platform drivers.

Interface Documentation
-----------------------

The IRQ interface documentation is generated using the Doxygen tool and it is available at:

-  `No-OS IRQ API <http://analogdevicesinc.github.io/no-OS/no__os__irq_8h.html>`__

Initialization example
----------------------

There are 2 types of IRQ descriptors:

-  A GPIO interrupt controller descriptor, that handles interrupt configurations on individual GPIO pins.
-  A global interrupt controller, that handles all the other interrupt sources.

Global interrupt controller initialization
------------------------------------------

.. code:: C

   int ret;

   struct no_os_irq_ctrl_desc *global_desc;
   struct no_os_irq_init_param global_desc_param = {
           .irq_ctrl_id = 0,
           /** Global IRQ controller specific ops. This struct is platform dependent. */
           .platform_ops = &max_irq_ops,
           .extra = NULL
   };

   ret = no_os_irq_ctrl_init(&global_desc, &global_desc_param);
   if (ret)
           return ret;

The **irq_ctrl_id** and **extra** fields are not used by any of the IRQ API functions, so they can be given arbitrary values that may be useful to application code.

GPIO interrupt controller initialization
----------------------------------------

::

   int ret;

   struct no_os_irq_ctrl_desc *gpio_irq_desc;
   struct no_os_irq_init_param gpio_irq_desc_param = {
           /** GPIO port number */
           .irq_ctrl_id = 0,
           /** GPIO IRQ controller specific ops. This struct is platform dependent. * /
           .platform_ops = &max_gpio_irq_ops,
           .extra = NULL
   };

   ret = no_os_irq_ctrl_init(&gpio_irq_desc, &gpio_irq_desc_param);
   if (ret)
           return ret;

The **extra** field is not used by any of the IRQ API functions (it's simply stored in **gpio_irq_desc**'s **extra** field), so it can be given arbitrary values that may be useful to application code.

Usage examples
--------------

Global interrupt controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows how to register callbacks and enable/disable global interrupts. This assumes that the global interrupt controller descriptor has been initialized. As for the moment, all the interrupts have the same (0) priority level.

.. code:: C

   void uart_callback_fn(void *context)
   {
           // interrupt code
   }

.. code:: C

   int ret;

   struct no_os_callback_desc uart_cb = {
           /** Callback to be called when the event an event occurs. */
           .callback = uart_callback_fn,
           /** Parameter to be passed when the callback is called */
           .ctx = NULL,
           /** Event that triggers the calling of the callback. */
           .event = NO_OS_EVT_UART_RX_COMPLETE,
           /** Interrupt source peripheral specifier. */
           .peripheral = NO_OS_UART_IRQ,
           /** Platform specific HAL descriptor. This may be used to uniquely identify a registered callback */
           .handle = MXC_UART0
   };

   /** 
     * Register a new callback for an event/peripheral pair (in case there is already one registered, it will be overwritten).
     * In the case of the global interrupt controller, the irq_id refers to the interrupt vector entry number 
     * of the peripheral (this should be unique).
   */
   ret = no_os_irq_register_callback(global_desc, UART0_IRQn, &uart_cb);
   if (ret)
           return ret;

   /**
   * Set the priority level of an interrupt.
   */
   ret = no_os_irq_set_priority(global_desc, UART0_IRQn, 1);
   if (ret)
           return ret;
   /** 
     * Enable the handling of interrupts from a peripheral specified by **irq_id**.
     * Without this step, the interrupt routine won't be called.
   */
   ret = no_os_irq_enable(global_desc, UART0_IRQn);
   if (ret)
           return ret;

   /** 
     * The callback will now be triggered once a RX complete event occurs on UART0.
   */

   /** 
     * Registering a callback for a GPIO peripheral from the global interrupt controller will result in an error.
   */
   ret = no_os_irq_register_callback(global_desc, GPIO0_IRQn, &uart_cb);

   /**
     * Unregistering a callback is done in this way. 
   */
   ret = no_os_irq_unregister_callback(global_desc, UART0_IRQn, &uart_cb);
   if (ret)
           return ret;

   /**
     * The calllback will no longer be triggered.
   */

GPIO interrupt controller
~~~~~~~~~~~~~~~~~~~~~~~~~

The following example shows how to handle GPIO interrupts. This assumes that both a global interrupt controller and a GPIO interrupt controller have been initialized.

::

   void gpio_callback_fn(void *ctx)
   {
           // interrupt code
   }

.. code:: C

   int ret;

   struct no_os_callback_desc gpio_cb = {
           /** Callback to be called when the event an event occurs. */
           .callback = gpio_callback_fn,
           /** Parameter to be passed when the callback is called */
           .ctx = NULL,
           /** Event that triggers the calling of the callback. */
           .event = NO_OS_EVT_GPIO,
           /** Interrupt source peripheral specifier. */
           .peripheral = NO_OS_GPIO_IRQ,
           /** Not used in the case of a GPIO IRQ controller */
           .handle = NULL
   };

   /**
     * In the context of using the GPIO interrupt controller specific platform ops, the irq_id refers to the pin number.
     * The callback will be registered on pin 5 of the GPIO port 0 (the port is specified by the id field of the 
     * gpio_irq_desc).
   */
   ret = no_os_register_callback(gpio_irq_desc, 5, &gpio_cb);
   if (ret)
           return ret;

   /**
     * Set the trigger condition of the interrupt on pin 5 to rising edge.
   */
   ret = no_os_trigger_level_set(gpio_irq_desc, 5, NO_OS_IRQ_EDGE_RISING);
   if (ret)
           return ret;

   /**
   * This calls the interrupt priority set function of the parent controller.
   */
   ret = no_os_irq_set_priority(gpio_irq_desc, 5, 1);
   if (ret)
           return ret;

   /**
     * Enable interrupts on pin 5.
   */
   ret = no_os_irq_enable(gpio_irq_desc, 5);
   if (ret)
           return ret;
          
   ret = no_os_irq_enable(global_desc, GPIO0_IRQn);
   if (ret)
           return ret;
           
   /**
     * The callbacks on pin 5 (GPIO 0) now get triggered on rising edge.
   /* 

Platform specific fields
------------------------

The **handle** field of the **no_os_callback_desc** struct is platform specific and has the following values:

-  **STM32**: In the case that a global interrupt controller is used, the handle is a HandleTypeDef struct. For a GPIO controller, it's ignored.
-  **Maxim**: In the case that a global interrupt controller is used, the handle is a reference to a struct containing the peripheral's register state. These should be found in the Maxim's SDK (e.g MXC_TMR_GET_TMR(0) or MXC_TMR0. The naming for other peripherals is similar.). For a GPIO IRQ controller, this field can be ignored.
-  **RPi Pico**: In the case that a global interrupt controller is used, the handle is a struct containing peripheral register state (e.g uart0). For a GPIO IRQ controller, it's ignored.

Other platforms do not need to have the handle field set, as it's ignored.
