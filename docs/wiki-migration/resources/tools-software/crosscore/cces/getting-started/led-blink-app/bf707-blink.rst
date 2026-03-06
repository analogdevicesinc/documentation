ADSP-BF707 LED Blink Example
============================

To help get started using CCES, here are steps to create an example application to blink an LED on the ADSP-BF707 EZ-Kit. This step-by-step example assumes familiarity with the C/C++ programming language and how to access CCES Online Help for information on the APIs.

If not done already, follow the instructions in the :doc:`Creating Projects in CCES </wiki-migration/resources/tools-software/crosscore/cces/getting-started/create>` section of this guide to create the **CCES_Example** project for your ADSP-BF707 board. Switch the Editor view to the *CCES_Example.c* tab, as shown in Figure 1.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/led-blink-app/cces_editor.png
   :width: 600px

*Figure 1. CCES Example.c*

The template code generated at project start-up by CCES includes auto-generated .c and .h files that take the project name. In the *CCES Example.c* file, there is a skeletal <fc #4682b4>main()</fc> function containing only a call to the <fc #4682b4>adi_initComponents()</fc> function. The <fc #4682b4>adi_initComponents()</fc> function is used to initialize drivers and services that were included using the system configuration utility. This is a necessary function in<fc #4682b4> main()</fc> and must be executed before any custom code. Without this function call, the designated add-ins will not operate.

The CCES system services include a GPIO service, which is used in this example application. This service can be used to set the direction of the GPIO pins, as well as read, set, toggle, and clear the states of each pin. Polling of pin states and interrupt methods are available through the GPIO service as well, which is documented in Online Help under **CrossCore Embedded Studio 2.x.x → System Run-Time Documentation → System Services and Device Drivers → ADSP-BF70x API Reference → Modules → GPIO Service**.

Provided here is the full code example needed to blink the LED on the ADSP-BF707 EZ-Kit, and a description of the code follows:

.. code:: c

   /*****************************************************************************
     * CCES Example.c
    *****************************************************************************/

   #include "adi_initialize.h"
   #include "CCES Example.h"
   #include <services/gpio/adi_gpio.h>

   #define GPIO_MEMORY_SIZE (ADI_GPIO_CALLBACK_MEM_SIZE*2)

   static uint8_t gpioMemory[GPIO_MEMORY_SIZE];

   int main(void)
   {
       /**
        * Initialize managed drivers and/or services that have been added to 
        * the project.
        * @return zero on success 
        */
       adi_initComponents();
       
       /* Begin adding your custom code here */

       ADI_GPIO_RESULT result;
       uint32_t gpioMaxCallbacks;
       /* initialize the GPIO service */
       result = adi_gpio_Init((void*)gpioMemory, GPIO_MEMORY_SIZE, &gpioMaxCallbacks);

       result = adi_gpio_SetDirection(ADI_GPIO_PORT_A, ADI_GPIO_PIN_0, ADI_GPIO_DIRECTION_OUTPUT);

       while(1)
       {
           result = adi_gpio_Toggle(ADI_GPIO_PORT_A, ADI_GPIO_PIN_0);
           for(int x = 0; x<5000000; x++);
       }

       return 0;
   }

Each of the system services has a dedicated header file located in the **\\services** sub-directory under the CCES root directory, and the first step in writing this LED Blink example is to include the header for the GPIO service after the default headers are included:

<fc #4682b4>\ **#include** "adi_initialize.h"</fc> ← Automatically included

<fc #4682b4>\ **#include** "CCES Example.h"</fc> ← Automatically included

<fc #4682b4> **#include** <services/gpio/adi_gpio.h></fc> ← Must Be Added

The next step is to define the object array which will contain the GPIO service data. This array will be used during the initialization of the GPIO service, and the macro definitions utilized can be found in the <fc #4682b4>adi_gpio.h</fc> file added above.

<fc #4682b4>\ **#define** GPIO_MEMORY_SIZE (ADI_GPIO_CALLBACK_MEM_SIZE*2)

static uint8_t gpioMemory[GPIO_MEMORY_SIZE];</fc>

A variable is then required for the return values from the system service and device driver APIs:

<fc #4682b4>ADI_GPIO_RESULT result;</fc>

Since the goal of this example is to build a simple blink application, the GPIO service needs to be initialized with the call to the<fc #4682b4> adi_gpio_Init()</fc> function, and the direction of the I/O pin connected to the LED must be set as an output pin via the <fc #4682b4>adi_gpio_SetDirection()</fc> function. The APIs have return values that indicate success or failure, which can provide valuable debug information, and this example uses result for each of the API calls to the GPIO service. Because of the simple nature of this example (i.e., only one pin is used, and only one service is being initialized), there is no error-checking implemented. A more complex system should utilize error-checking to ensure that the device drivers and system services are all being initialized and used properly.

Finally, to actually blink the LED, the <fc #4682b4>adi_gpio_Toggle()</fc> GPIO toggle API is called from within an infinite <fc #4682b4>while(1)</fc> loop, buffered on each iteration by the <fc #4682b4>for(int x = 0; x<5000000; x++)</fc> delay loop to space out toggling of the GPIO state.

Now you are ready to :doc:`Debug </wiki-migration/resources/tools-software/crosscore/cces/getting-started/debug>` your application.

--------------

`LED Blink Application#.|LED Blink Application#sc573-blink|Multi-Core LED Blink Example Application <https://wiki.analog.com/_media/navigation CCES Getting Started#.>`__
