No-OS Timer API
===============

Description
-----------

The timer driver initializes and offers APIs for hardware timers. No-OS platform uses hardware in two contexts:

-  to measure time intervals in order to perform time delays
-  to measure time intervals in order to perform time triggered interrupts.

Documentation
-------------

The timer generic driver documentation is generated using the Doxygen tool and it is available at:

-  `No-OS Timer Generic Driver <http://analogdevicesinc.github.io/no-OS/doxygen/no__os__timer_8h.html>`_

Timer Initial Parameters
------------------------

**struct no_os_timer_init_param** structure has to be filled in by the application and has to be given as a parameter when calling the initialization API.

Structure Definition
~~~~~~~~~~~~~~~~~~~~

.. code:: C

   struct no_os_timer_init_param {
       /** timer ID */
       uint16_t id;
       /** timer count frequency (Hz) */
       uint32_t freq_hz;
       /** the number of ticks the timer counts until it resets */
       uint32_t ticks_count;
       /** Timer platform operations */
       const struct no_os_timer_platform_ops *platform_ops;
       /** timer extra parameters (device specific) */
       void *extra;
   };

Parameters Description
~~~~~~~~~~~~~~~~~~~~~~

-  **id** - represents the unique identifier for a hardware timer to be used. the value is hardware dependent
-  **freq_hz** - represents the timer count frequency
-  **ticks_count** - represents the number of ticks the timer counts until it resets
-  **\*platform_ops** - is a pointer to timer APIs. the value is MCU platform specific
-  **\*extra** - is a pointer to extra timer initialization parameters, which are specific the the used MCU platform. The definition of the extra timer initialization parameters can be found under the name *platform*\ \_timer_init_param, where platform can be *aducm, max, pico, stm32, xil*.

Timer Descriptor
----------------

**struct no_os_timer_desc** structure is filled by the initialization API based on the given initialization parameters. It describes the initialized timer instance which has to be given as a parameter when using the other APIs.

.. _structure-definition-1:

Structure Definition
~~~~~~~~~~~~~~~~~~~~

.. code:: C

   struct no_os_timer_desc {
       /** timer ID */
       uint16_t id;
       /** timer count frequency (Hz) */
       uint32_t freq_hz;
       /** the number of ticks the timer counts until it resets */
       uint32_t ticks_count;
       /** Timer platform operations */
       const struct no_os_timer_platform_ops *platform_ops;
       /** timer extra parameters (device specific) */
       void *extra;
   };

.. _parameters-description-1:

Parameters Description
~~~~~~~~~~~~~~~~~~~~~~

-  **id** - represents the unique identifier given to the timer - equal to the id given in the initialization structure
-  **freq_hz** - represents the timer count frequency - equal to the freq_hz given in the initialization structure
-  **ticks_count** - represents the number of ticks the timer counts until it resets - equal to the ticks_count given in the initialization structure
-  **\*platform_ops** - is a pointer to timer APIs - equal to the platform_ops given in the initialization structure
-  **\*extra** - is a pointer to extra timer description parameters, which are specific the the used MCU platform. The definition of the extra timer descriptor can be found under the name *platform*\ \_timer_desc, where platform can be *aducm, max, pico, stm32, xil*.

Timer APIs
----------

The structure no_os_timer_platform_ops consists of pointers to timer APIs that point to platform specific functions. Each platform shall contain a specific implementation for each of these functions.

.. _structure-definition-2:

Structure Definition
~~~~~~~~~~~~~~~~~~~~

.. code:: C

   struct no_os_timer_platform_ops {
       /** timer initialization function pointer */
       int32_t (*init)(struct no_os_timer_desc **,
               const struct no_os_timer_init_param *);
       /** timer start function pointer */
       int32_t (*start)(struct no_os_timer_desc *);
       /** timer stop function pointer */
       int32_t (*stop)(struct no_os_timer_desc *);
       /** timer get counter function pointer */
       int32_t (*counter_get)(struct no_os_timer_desc *, uint32_t *counter);
       /** timer set counter function pointer */
       int32_t (*counter_set)(struct no_os_timer_desc *, uint32_t new_val);
       /** timer get clock frequency function pointer */
       int32_t (*count_clk_get)(struct no_os_timer_desc *, uint32_t *freq_hz);
       /** timer set clock frequency function pointer */
       int32_t (*count_clk_set)(struct no_os_timer_desc *, uint32_t freq_hz);
       /** timer get elapsed time in nsec */
       int32_t (*get_elapsed_time_nsec)(struct no_os_timer_desc *,
                        uint64_t *elapsed_time);
       /** timer remove function pointer */
       int32_t (*remove)(struct no_os_timer_desc *);
   };

APIs description
~~~~~~~~~~~~~~~~

Init API
^^^^^^^^

Initializes the hardware timer peripheral, taking the initialization parameters and stores data in the timer descriptor.

Start API
^^^^^^^^^

Starts the hardware timer - at this point the timer shall begin counting with the given frequency either up to the ticks count value, starting from 0, either down to 0, starting from the given ticks count value. The descriptor of the timer is given as parameter. The timer has to be initialized before calling this API.

Stop API
^^^^^^^^

Stops the hardware timer which was previously started using the start API - at this point the timer shall stop counting. The descriptor of the timer is given as parameter. The timer has to be initialized before calling this API.

Get counter API
^^^^^^^^^^^^^^^

Reads the value of the count register of the hardware timer. The descriptor of the timer is given as parameter. The value of the count register will be stored at the address given by the counter pointer parameter. The timer has to be initialized before calling this API.

Set counter API
^^^^^^^^^^^^^^^

Sets the value of the count register of the hardware timer equal to the value given in the counter parameter. The descriptor of the timer is given as parameter. The timer has to be initialized before calling this API. This value has to be smaller than the ticks count value given in the initialization.

Get counter clock API
^^^^^^^^^^^^^^^^^^^^^

Reads the source clock frequency of the hardware timer. The descriptor of the timer is given as parameter. The value of the frequency (in Hertz) will be stored at the address given by the freq_hz pointer parameter. The timer has to be initialized before calling this API.

Set counter clock API
^^^^^^^^^^^^^^^^^^^^^

Sets the source clock frequency of the hardware timer equal to the value given in the freq_hz parameter (given in Hertz). The descriptor of the timer is given as parameter. The timer has to be initialized before calling this API.

Get elapsed time in nanoseconds API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reads the elapsed time in nanoseconds measured with the hardware timer. The descriptor of the timer is given as parameter. The value of elapsed time (in nanoseconds) will be stored at the address given by the elapsed_time pointer parameter. The timer has to be initialized before calling this API.

Timer Supported Platforms
-------------------------

ADUCM3029 Platform
~~~~~~~~~~~~~~~~~~

The timer driver documentation for ADUCM3029 platform can be found here:

-  `Header file for ADUCM3029 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/aducm3029__timer_8h.html>`_
-  `Source file for ADUCM3029 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/aducm3029__timer_8c.html>`_

The definition of the extra timer initialization parameters:

.. code:: C

   struct aducm_timer_init_param {
       /** Selected frequency for timer clock source */
       enum avail_freqs source_freq;
   };

The definition of the extra timer description parameters:

.. code:: C

   struct aducm_timer_desc {
       /** Used to compare with the driver internal count */
       uint64_t    old_time;
       /** 1 if the instance is counting, 0 otherwise */
       bool        started;
       /** Timer configuration for aducm3029 */
       ADI_TMR_CONFIG  tmr_conf;
   };

MAXIM Platform
~~~~~~~~~~~~~~

The timer driver documentation for each MAXIM family can be found here:

-  MAX32650:

   -  `Header file for MAX32650 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32650_2maxim__timer_8h.html>`_

      -  `Source file for MAX32650 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32650_2maxim__timer_8c.html>`_

-  MAX32655:

   -  `Header file for MAX32655 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32655_2maxim__timer_8h.html>`_

      -  `Source file for MAX32655 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32655_2maxim__timer_8c.html>`_

-  MAX32660:

   -  `Header file for MAX32660 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32660_2maxim__timer_8h.html>`_

      -  `Source file for MAX32660 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32660_2maxim__timer_8c.html>`_

-  MAX32665:

   -  `Header file for MAX32665 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32665_2maxim__timer_8h.html>`_

      -  `Source file for MAX32665 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max32665_2maxim__timer_8c.html>`_

-  MAX78000:

   -  `Header file for MAX78000 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max78000_2maxim__timer_8h.html>`_

      -  `Source file for MAX7800 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/max78000_2maxim__timer_8c.html>`_

There are no extra parameters needed for MAXIM platform.

MBED Platform
~~~~~~~~~~~~~

The timer driver documentation for MBED platform can be found here:

-  `Header file for MBED timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/mbed__timer_8h.html>`_

The definition of the extra timer description parameters:

.. code:: C

   struct mbed_timer_desc {
       void *timer;        // Object to the mbed Timer class
   };

Pico Platform
~~~~~~~~~~~~~

The timer driver documentation for Pico platform can be found here:

-  `Header file for Pico timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/pico__timer_8h.html>`_
-  `Source file for Pico timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/pico__timer_8c.html>`_

STM32 Platform
~~~~~~~~~~~~~~

The timer driver documentation for STM32 platform can be found here:

-  `Header file for STM32 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/stm32__timer_8h.html>`_
-  `Source file for STM32 timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/stm32__timer_8c.html>`_

The definition of the extra timer initialization parameters:

.. code:: C

   typedef struct stm32_timer_init_param {
       TIM_HandleTypeDef *htimer;
   } stm32_timer_init_param;

The definition of the extra timer description parameters:

.. code:: C

   typedef struct stm32_timer_desc {
       TIM_HandleTypeDef *htimer;
   } stm32_timer_desc;

Where htimer parameter is a pointer to the address holding the hardware timer handle data, specific to STM32 HAL.

Xilinx Platform
~~~~~~~~~~~~~~~

The timer driver documentation for Xilinx platform can be found here:

-  `Header file for Xilinx timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/xilinx_2timer__extra_8h.html>`_
-  `Source file for Xilinx timer driver <http://analogdevicesinc.github.io/no-OS/doxygen/platform_2xilinx_2no__os__timer_8c.html>`_

The definition of the extra timer initialization parameters:

.. code:: C

   struct xil_timer_init_param {
       /** Timer used from the PL 3-timer core */
       uint8_t active_tmr;
       /** Platform selection parameter */
       enum xil_timer_type type;
   };

The definition of the extra timer description parameters:

.. code:: C

   struct xil_timer_desc {
       /** Pointer to the BSP driver handler */
       void *instance;
       /** Pointer to the BSP driver configuration handler */
       void *config;
       /** Timer used from the PL 3-timer core */
       uint8_t active_tmr;
       /** Platform selection parameter */
       enum xil_timer_type type;
   };

Timer Examples
--------------

Delays with hardware timers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may obtain delays using a hardware timer. Below you may find an example.

.. code:: C

   #include "no_os_timer.h"
   #include "no_os_irq.h"
   #include "parameters.h"

   /* Each tick takes 1/10000 seconds = 0.1 ms)
   #define TIMER_FREQ_HZ 10000
   /* The counter of the timer will reset when it reached value 1000 */
   #define TIMER_TICKS_COUNT 1000

   /* We need 100 ticks in order to obtain a 10ms period */
   #define TIMER_DELAY_10MS 100

   int main ()
   {
       int ret;
       uint32_t count;
    
       /* Timer initialization parameter */
       struct no_os_timer_init_param timer_ip = {
           .id = TIMER_DEVICE_ID, // platform specific
           .freq_hz = TIMER_FREQ_HZ,
           .ticks_count = TIMER_TICKS_COUNT,
           .platform_ops = TIMER_OPS, // platform specific
           .extra = TIMER_EXTRA, // platform specific
       };

           /* Timer descriptor. */
       struct no_os_timer_desc *timer_desc;

       /* Initialize timer */
       ret = no_os_timer_init(&timer_desc, &timer_irq_ip);
       if (ret)
           return ret;

       /* Set counter to 0 */
       ret = no_os_timer_counter_set(timer_desc,0);
       if (ret)
           return ret;

       /* Start timer */
       ret = no_os_timer_start(timer_desc);
       if (ret)
           return ret;

       /* Wait until the timer counter is equal to the desired value */
       do {
           ret = no_os_timer_counter_get(timer_desc, &count);
           if (ret)
               return ret;
       } while (count < TIMER_DELAY_10MS);

       /* Stop the timer */
       ret = no_os_timer_stop(timer_desc);
       if (ret)
           return ret;

       ...

Below you may find the platform specific definitions for each platform:

.. _aducm3029-platform-1:

Aducm3029 platform
^^^^^^^^^^^^^^^^^^

Aducm3029 parameters.h:

.. code:: C

   #include "aducm3029_timer.h"

   #define TIMER_DEVICE_ID 1 // only 1 allowed, instace 0 is used for time delays
   #define TIMER_OPS &aducm3029_timer_ops
   extern struct aducm_timer_init_param timer_extra_ip;
   #define TIMER_EXTRA &timer_extra_ip

Aducm3029 parameters.c:

.. code:: C

   #include "parameters.h"
   struct aducm_timer_init_param timer_extra_ip = {
       .source_freq = PCLK_DIV256,
   };

.. important::

   For Aducm3029 platform TIMER_FREQ_HZ value is not used (initialization parameter freq_hz) because it cannot be set freely. The value of the source clock frequency is given in the extra parameter in the source_freq field. In this example the clock source frequency for the timer will be equal to the PCLK frequency divided by 256.


.. _maxim-platform-1:

Maxim platform
^^^^^^^^^^^^^^

Maxim parameters.h:

.. code:: C

   #include "timer_extra.h"

   #define TIMER_DEVICE_ID 0
   #define TIMER_OPS &max_timer_ops
   #define TIMER_EXTRA NULL // Not used for Maxim platform

.. _mbed-platform-1:

MBED Platform
^^^^^^^^^^^^^

MBED parameters.h:

.. code:: C

   #include "mbed_timer.h"

   #define TIMER_DEVICE_ID 0 // Not used for MBED platform
   #define TIMER_OPS NULL // Not used for MBED platform
   #define TIMER_EXTRA NULL // Not used for MBED platform

.. _pico-platform-1:

Pico Platform
^^^^^^^^^^^^^

Pico parameters.h:

.. code:: C

   #include "pico_timer.h"

   #define TIMER_DEVICE_ID 0 // For alarm0 instance
   #define TIMER_OPS &pico_timer_ops
   #define TIMER_EXTRA NULL // Not used for pico platform

.. _stm32-platform-1:

STM32 platform
^^^^^^^^^^^^^^

STM32 parameters.h:

.. code:: C

   #include "stm32_timer.h"

   #define TIMER_DEVICE_ID 0
   #define TIMER_OPS &stm32_timer_ops
   extern stm32_timer_init_param timer_xtip;
   #define TIMER_EXTRA &timer_xtip

STM32 parameters.c:

.. code:: C

   #include "parameters.h"
   /* htim13 is defined in the STM32 generated code after selecting the timer in the STMCubeMx application */
   extern TIM_HandleTypeDef htim13;
   struct stm32_timer_init_param timer_xtip = {
       .htimer = &htim13,
   };

.. important::

   For HAL configuration the .ioc file is used. Make sure your .ioc file contains the timer instantiation.

   
   Some settings used in STMCubeMx will be overwritten by No-OS code such that the period of the timer meets the settings given in the initialization parameters \*/


The image below show that TIM13 is activated in STMCubeMx:



|STMCubeMx TIM13 activated|

.. _xilinx-platform-1:

Xilinx Platform
^^^^^^^^^^^^^^^

Xilinx parameters.h:

.. code:: C

   #include "timer_extra.h"

   #define TIMER_DEVICE_ID 0 // Not used for Xilinx platform
   #define TIMER_OPS NULL // Not used for Xilinx platform
   extern struct xil_timer_init_param timer_xtip;
   #define TIMER_EXTRA &timer_xtip

Xilinx parameters.c:

.. code:: C

   #include "parameters.h"
   struct xil_timer_init_param timer_xtip = {
       .active_tmr = 0,
       .type = TIMER_PS;
   };

Although you may use the hardware timers to perform delays, with No-OS platform we advise you to use the already implemented APIs from no_os_delay.h: no_os_udelay(uint32_t usecs) to perform a delay in microseconds and no_os_mdelay(uint32_t msecs) to perform a delay in milliseconds. Using the no_os_delay APIs you will have one extra hardware timer resource available, to be used in the application as deemed fit.

Time triggered interrupts with hardware timers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On No-OS platform, the time triggered interrupts are primarily used for IIO hardware triggers, but they can be used by the application as seen fit.

Time triggered interrupts generic example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to be able to used time triggered interrupts you will have two perform initialization for the timer peripheral (with no_os_timer_init API) and for the interrupt controller (with no_os_irq_ctrl_init API). Additionally you may specify the the interrupt priority (with no_os_irq_set_priority API). If the initialization is successful, now you may register your callback function (with no_os_irq_register_callback API) which is going to be called from the interrupt context. Finally, you should enable the timer interrupt (with no_os_irq_enable API) and you should start the timer (with no_os_timer_start API).

Below you may find a code snippet, containing the needed steps to be able to use time triggered interrupts:

.. code:: C

   #include "no_os_timer.h"
   #include "no_os_irq.h"
   #include "parameters.h"

   /* Values for 100 ms interrupt period */
   #define TIMER_FREQ_HZ 10000
   #define TIMER_TICKS_COUNT 1000

   void timer_callback(void *context)
   {
       /* Application specific implementation */
   }


   int main ()
   {
       int ret;

       /* Timer initialization parameter */
       struct no_os_timer_init_param timer_ip = {
           .id = TIMER_DEVICE_ID, // platform specific
           .freq_hz = TIMER_FREQ_HZ,
           .ticks_count = TIMER_TICKS_COUNT,
           .platform_ops = TIMER_OPS, // platform specific
           .extra = TIMER_EXTRA, // platform specific
       };

       /* Timer irq initialization parameter */
       struct no_os_irq_init_param timer_irq_ip = {
           .irq_ctrl_id = 0, // specific to NVIC IRQ controller
           .platform_ops = TIMER_IRQ_OPS, // platform specific
           .extra = TIMER_IRQ_EXTRA, // platform specific
       };

       struct no_os_callback_desc irq_cb = {
           .callback = timer_callback,
           .ctx = CALLBACK_PARAMETERS,
           .event = NO_OS_EVT_TIM_ELAPSED,
           .peripheral = NO_OS_TIM_IRQ,
           .handle = TIMER_CB_HANDLE, // platform specific
       };

       /* Timer descriptor. */
       struct no_os_timer_desc *timer_desc;

       /* Irq descriptor */
       struct no_os_irq_ctrl_desc *irq_desc;

       /* Initialize timer */
       ret = no_os_timer_init(&timer_desc, &timer_irq_ip);
       if (ret)
           return ret;

       /* Initialize timer IRQ controller */
       ret = no_os_irq_ctrl_init(&irq_desc, &timer_irq_ip);
       if (ret)
           return ret;

       /* Set timer IRQ priority */
       ret = no_os_irq_set_priority(irq_desc, TIMER_IRQ_ID, TIMER_IRQ_PRIORITY);
       if (ret)
           return ret;

       /* Register callback for timer IRQ */
       ret = no_os_irq_register_callback(irq_desc, TIMER_IRQ_ID, &irq_cb);
       if (ret)
           return ret;

       /* Enable timer IRQ */
       ret = no_os_irq_enable(irq_desc, TIMER_IRQ_ID);
       if (ret)
           return ret;
       /* Start timer */    
       ret = no_os_timer_start(timer_desc);​
       if (ret)     
           return ret; 
    
       ...
   }

Below you may find the platform specific definitions for each platform:

.. _aducm3029-platform-2:

Aducm3029 platform
""""""""""""""""""

Aducm3029 parameters.h:

.. code:: C

   #include "aducm3029_timer.h"
   #include "aducm3029_irq.h"

   #define TIMER_DEVICE_ID 1 // only 1 allowed, instace 0 is used for time delays
   #define TIMER_OPS &aducm3029_timer_ops
   extern struct aducm_timer_init_param timer_extra_ip;
   #define TIMER_EXTRA &timer_extra_ip

   #define TIMER_IRQ_ID 0 // not used for Aducm3029 platform
   #define TIMER_IRQ_OPS &aducm3029_irq_ops
   #define TIMER_IRQ_EXTRA NULL // not used for Aducm3029 platform

   #define CALLBACK_PARAMETERS NULL //application specific - can track the context from which the callback was registered
   #define TIMER_CB_HANDLE NULL // not used for Aducm3029 platform

Aducm3029 parameters.c:

.. code:: C

   #include "parameters.h"
   struct aducm_timer_init_param timer_extra_ip = {
       .source_freq = PCLK_DIV256,
   };

.. important::

   For Aducm3029 platform TIMER_FREQ_HZ value is not used (initialization parameter freq_hz) because it cannot be set freely. The value of the source clock frequency is given in the extra parameter in the source_freq field. In this example the clock source frequency for the timer will be equal to the PCLK frequency divided by 256.


.. _maxim-platform-2:

Maxim platform
""""""""""""""

Maxim parameters.h:

.. code:: C

   #include "maxim_timer.h"
   #include "maxim_irq.h"

   #define TIMER_DEVICE_ID 0
   #define TIMER_OPS &max_timer_ops
   #define TIMER_EXTRA NULL // Not used for Maxim platform

   #define TIMER_IRQ_ID TMR0_IRQn
   #define TIMER_IRQ_OPS &max_irq_ops
   #define TIMER_IRQ_EXTRA NULL // Not used for Maxim platform

   #define CALLBACK_PARAMETERS NULL //application specific - can track the context from which the callback was registered
   #define TIMER_CB_HANDLE MXC_TMR0

.. _mbed-platform-2:

MBED Platform
"""""""""""""

MBED platform does not offer timer interrupts support currently.

.. _pico-platform-2:

Pico Platform
"""""""""""""

Pico parameters.h:

.. code:: C

   #include "pico_timer.h"
   #include "pico_irq.h"

   #define TIMER_DEVICE_ID 0 // For alarm0 instance
   #define TIMER_OPS &pico_timer_ops
   #define TIMER_EXTRA NULL // Not used for pico platform

   #define TIMER_IRQ_ID 0 // For alarm0 IRQ
   #define TIMER_IRQ_OPS &pico_irq_ops
   #define TIMER_IRQ_EXTRA NULL // not used for pico platform

   #define CALLBACK_PARAMETERS NULL //application specific - can track the context from which the callback was registered
   extern uint8_t timer_cb_handle;
   #define TIMER_CB_HANDLE &timer_cb_handle

Pico parameters.c:

.. code:: C

   #include "parameters.h"
   uint8_t timer_cb_handle = 0; // for alarm0

.. _stm32-platform-2:

STM32 platform
""""""""""""""

STM32 parameters.h:

.. code:: C

   #include "stm32_timer.h"
   #include "stm32_irq.h"

   #define TIMER_DEVICE_ID 0
   #define TIMER_OPS &stm32_timer_ops
   extern stm32_timer_init_param timer_xtip;
   #define TIMER_EXTRA &timer_xtip

   #define TIMER_IRQ_ID TIM8_UP_TIM13_IRQn
   #define TIMER_IRQ_OPS &stm32_irq_ops
   #define TIMER_IRQ_EXTRA NULL // not used in STM32 platform

   #define CALLBACK_PARAMETERS NULL //application specific - can track the context from which the callback was registered
   #define TIMER_CB_HANDLE &htim13

STM32 parameters.c:

.. code:: C

   #include "parameters.h"
   /* htim13 is defined in the STM32 generated code after selecting the timer in the STMCubeMx application */
   extern TIM_HandleTypeDef htim13;
   struct stm32_timer_init_param timer_xtip = {
       .htimer = &htim13,
   };

.. important::

   For HAL configuration the .ioc file is used. Make sure your .ioc file contains the timer instantiation and make sure you are enabling interrupts for the selected timer.

   
   Some settings used in STMCubeMx will be overwritten by No-OS code such that the period of the timer meets the settings given in the initialization parameters \*/


The images below show that TIM13 is activated and that the according interrupts are enabled in STMCubeMx:



|STMCubeMx TIM13 activated|

.. image:: https://wiki.analog.com/_media/resources/no-os/drivers/nvic_timer_stm32.png
   :alt: STMCubeMx TIMER13 IRQ activated
   :align: center

.. _xilinx-platform-2:

Xilinx Platform
"""""""""""""""

Xilinx platform does not offer timer interrupts support currently.

Time triggered interrupt with IIO triggers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As mentioned previously, on No-OS platform, the time triggered interrupts are primarily used for IIO hardware triggers.

When an interrupt takes place, a trigger callback will be activated, which will lead to performing a reading or a writing from/to the IIO device. The interrupt callback is registered in iio_trigger.c file in iio_hw_trig_init API. The context is the trigger descriptor, which is needed for handling the correct IIO device.

In :git-no-OS:`projects/iio_demo` project you may find a timer interrupt example with IIO triggers for STM32 platform.

In :git-no-OS:`projects/adxrs290-pmdz` project you may find timer interrupt examples with IIO triggers for Aducm3029 and Pico platform.

.. |STMCubeMx TIM13 activated| image:: https://wiki.analog.com/_media/resources/no-os/drivers/parameters_timer_stm32.png
