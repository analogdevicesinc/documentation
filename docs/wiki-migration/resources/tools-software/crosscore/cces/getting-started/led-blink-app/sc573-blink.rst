ADSP-SC573 LED Blink Example Application
========================================

To help get started using CCES, here are steps to create an example application to blink an LED on the ADSP-SC573 EZ-Kit. This step-by-step example assumes you are familiar with the C/C++ programming language and how to access CCES Online Help for information on the APIs.

To begin, follow the instructions in the :doc:`Creating Projects in CCES </wiki-migration/resources/tools-software/crosscore/cces/getting-started/create>` section of this guide to create the CCES_Example project for your ADSP-SC573 board. A project will appear for each core of the board, called **CCES_Example_Core0**, **CCES_Example_Core1**, and **CCES_Example_Core2**.

Open the <fc #4682b4>CCES_Example_Core0.c</fc>,<fc #4682b4> CCES_Example_Core1.c</fc>, and <fc #4682b4>CCES_Example_Core2.c</fc> files located in the src folder of each project (Figure 1). These are the main C files that we will be writing the example application in.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/led-blink-app/open_example_code.png
   :width: 400px

*Figure 1. Open Example Code*

The template code generated at project start-up by CCES includes auto-generated .c and .h files that take the project name. In the<fc #4682b4> CCES_Example_Core0.c</fc> file, there is a skeletal <fc #4682b4>main()</fc> function containing only three function calls. The <fc #4682b4>adi_initComponents()</fc> function is used to initialize drivers and services that were included using the system configuration utility. This is a necessary function in<fc #4682b4> main()</fc>, and all of your code that belongs in the <fc #4682b4>main()</fc> function should come after this call. Without this function call, the designated add-ins will not operate. The <fc #4682b4>adi_core_enable</fc> function tells the other processor cores to begin executing their code. The C files for the other cores contain only a call to <fc #4682b4>adi_initComponents()</fc>.

The CCES system services include a GPIO service, which is used in this example application. This service can be used to set direction, as well as read, set, toggle, and clear pins. There are also polling and interrupt methods available through the GPIO service. The GPIO Service Help information is located in Online Help under **CrossCore Embedded Studio 2.x.x → System Run-Time Documentation → System Services and Device Drivers → ADSP-SC57x (Cortex-A Core) API Reference → Modules → GPIO Service** and **CrossCore Embedded Studio 2.x.x → System Run-Time Documentation → System Services and Device Drivers → ADSP-SC57x (SHARC+ Core) API Reference → Modules → GPIO Service**.

Provided here is the code example for a multi-core LED blink application on the ADSP-SC573 EZ-Kit:

CCES_Example_Core0.c
--------------------

.. code:: c

   /*****************************************************************************
     * CCES_Example_Core0.c
    *****************************************************************************/

   #include <sys/platform.h>
   #include <sys/adi_core.h>
   #include "adi_initialize.h"
   #include "CCES_Example_Core0.h"
   #include <services/gpio/adi_gpio.h>

   int main()
   {
       /**
        * Initialize managed drivers and/or services that have been added to 
        * the project.
        * @return zero on success 
        */
       adi_initComponents();
       
       /* Begin adding your custom code here */

       ADI_GPIO_RESULT result;
       
       /* For all pins we are using, set direction to output */
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_E, ADI_GPIO_PIN_13, ADI_GPIO_DIRECTION_OUTPUT);
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_A, ADI_GPIO_PIN_9, ADI_GPIO_DIRECTION_OUTPUT);
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_C, ADI_GPIO_PIN_14, ADI_GPIO_DIRECTION_OUTPUT);
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_C, ADI_GPIO_PIN_4, ADI_GPIO_DIRECTION_OUTPUT);
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_D, ADI_GPIO_PIN_6, ADI_GPIO_DIRECTION_OUTPUT);
           result = adi_gpio_SetDirection(ADI_GPIO_PORT_E, ADI_GPIO_PIN_15, ADI_GPIO_DIRECTION_OUTPUT);

   /*
     * The default startup code does not include any functionality to allow
     * core 0 to enable core 1 and core 2. A convenient way to enable
     * core 1 and core 2 is to use the adi_core_enable function.
    */

   adi_core_enable(ADI_CORE_SHARC0);
   adi_core_enable(ADI_CORE_SHARC1);

   int x;
       while(1) {
           result = adi_gpio_Toggle(ADI_GPIO_PORT_E, ADI_GPIO_PIN_13);
           result = adi_gpio_Toggle(ADI_GPIO_PORT_A, ADI_GPIO_PIN_9);
           for (x = 0; x < 5000000; x++);
       }

       return 0;
   }

CCES_Example_Core1.c
--------------------

.. code:: c

   /*****************************************************************************
     * CCES_Example_Core1.c
    *****************************************************************************/

   #include <sys/platform.h>
   #include <sys/adi_core.h>
   #include "adi_initialize.h"
   #include "CCES_Example_Core1.h"
   #include <services/gpio/adi_gpio.h>

   int main()
   {
       /**
        * Initialize managed drivers and/or services that have been added to 
        * the project.
        * @return zero on success 
        */
       adi_initComponents();
       
       /* Begin adding your custom code here */

       ADI_GPIO_RESULT result;

           int x;
       while(1) {
           result = adi_gpio_Toggle(ADI_GPIO_PORT_C, ADI_GPIO_PIN_14);
           result = adi_gpio_Toggle(ADI_GPIO_PORT_C, ADI_GPIO_PIN_4);
           for (x = 0; x < 5000000; x++);
       }
   }

CCES_Example_Core2.c
--------------------

.. code:: c

   /*****************************************************************************
     * CCES_Example_Core2.c
    *****************************************************************************/

   #include <sys/platform.h>
   #include <sys/adi_core.h>
   #include "adi_initialize.h"
   #include "CCES_Example_Core2.h"
   #include <services/gpio/adi_gpio.h>

   int main()
   {
       /**
        * Initialize managed drivers and/or services that have been added to 
        * the project.
        * @return zero on success 
        */
       adi_initComponents();
       
       /* Begin adding your custom code here */

       ADI_GPIO_RESULT result;

           int x;
       while(1) {
           result = adi_gpio_Toggle(ADI_GPIO_PORT_D, ADI_GPIO_PIN_6);
           result = adi_gpio_Toggle(ADI_GPIO_PORT_E, ADI_GPIO_PIN_15);
           for (x = 0; x < 5000000; x++);
       }
   }

*Figure 2. LED Blink Application for the ADSP-SC573 EZ-Kit*

The first step in writing this LED Blink example is to include the header for the GPIO service in each source file:

<fc #4682b4>#include <services/gpio/adi_gpio.h></fc>

Each of the system services contains header files located in the \\services sub-directory in your CCES installation. We then need to declare a variable for the return values from the system service and device driver APIs:

<fc #4682b4>ADI_GPIO_RESULT result;</fc>

Next, we set the direction of the I/O pins connected to the LEDs to be outputs via the <fc #4682b4>adi_gpio_SetDirection()</fc> function. The APIs have return values that indicate success or failure and can provide valuable debugging information, and this example uses result for each of the API calls to the GPIO service.

Finally, to actually blink the LED, the <fc #4682b4>adi_gpio_Toggle()</fc> GPIO toggle API is called from within an infinite loop, buffered on each iteration by a delay loop to space out toggling of the GPIO state.

Note that, if we were registering GPIO callbacks, we would need to allocate memory to hold callback information and then initialize the GPIO service by calling <fc #4682b4>adi_gpio_Init()</fc>.

Now you are ready to :doc:`Debug </wiki-migration/resources/tools-software/crosscore/cces/getting-started/debug>` your application.

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#bf707-blink
   :alt: Single-Core LED Blink Application#.|LED Blink Application#..app|Creating Bootable Applications
