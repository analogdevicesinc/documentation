IAR Board Support Package
=========================

A modular software framework is provided for quick application prototyping.

.. important::

   Please make sure you install IAR Embedded Workbench before installing the pack


The Cog software development kit

-  `BSP - Board Support Package for EZ-KIT-ADuCM3029 <http://download.analog.com/tools/EZBoards/CM302x/Releases/Release_2.0.0/ADuCM3029_Software-Rel2.0.0.exe>`__ - This is a bare minimum pack required to enable working with ADuCM3029 on IAR. This helps to develop,

   -  simple applications using the on-chip drivers.

      -  simple applications using the on-board drivers.

.. important::

   The application examples found in the pack are developed for EVAL-ADuCM3029-Ez-Kit and will require small changes to make it work for EV-COG-AD3029LZ


**As an example "LED_button_callback" is considered and the changes required is briefly explained.**

\**Here, the changes are made only with respect to the GPIOs and only on the application source file. \*\*

-  Install the IAR BSP from the above link.
-  Open the "LED_button_callback.c" source code in the editor of your choice and make the below changes:

::

     * PATH: C:\Analog Devices\ADuCM302x\ADuCM302x_EZ_Kit\examples\gpio\LED_button_callback\LED_button_callback.c
       * Macro definition changes under "defined(__ADUCM302x__)":
         * #define PB1_PORT_NUM        ADI_GPIO_PORT1
         * #define PB1_PIN_NUM         ADI_GPIO_PIN_0
         * 
         * #define PB2_PORT_NUM        ADI_GPIO_PORT0
         * #define PB2_PIN_NUM         ADI_GPIO_PIN_9
         * 
         * #define LED1_PORT_NUM       ADI_GPIO_PORT2
         * #define LED1_PIN_NUM        ADI_GPIO_PIN_2
         * 
         * #define LED2_PORT_NUM       ADI_GPIO_PORT2
         * #define LED2_PIN_NUM        ADI_GPIO_PIN_10

::

         * Application code changes:
         * Before changes:
         * /* set GPIO output LED 4 and 5 */
         * if(ADI_GPIO_SUCCESS != (eResult = adi_gpio_OutputEnable(ADI_GPIO_PORT1, (ADI_GPIO_PIN_12 | ADI_GPIO_PIN_13), true)))
         * {
         * DEBUG_MESSAGE("adi_gpio_SetDirection failed\n");
         * break;
         * }
         * ...........
         * After changes:
         * /* set GPIO output LED 4 and 5 */
         * if(ADI_GPIO_SUCCESS != (eResult = adi_gpio_OutputEnable(LED1_PORT_NUM , LED1_PIN_NUM, true)))
         * {
         * DEBUG_MESSAGE("adi_gpio_SetDirection failed\n");
         * break;
         * }
         * if(ADI_GPIO_SUCCESS != (eResult = adi_gpio_OutputEnable(LED2_PORT_NUM, LED2_PIN_NUM , true)))
         * {
         * DEBUG_MESSAGE("adi_gpio_SetDirection failed\n");
         * break;
         * }
         * ...........
         * save the changes and close the source file.

-  Now open the application in IAR embedded workbench.

PATH:C:\\AnalogDevices\\ADuCM302x\\ADuCM302x_EZ_Kit\\examples\\gpio\\LED_button_callback\\ADuCM302x\\iar\\LED_button_callback.eww

-  Press Alt+F7 to open the project options.
-  Under category select Debugger.
-  In setup, under Driver select CMSIS DAP.
-  In Download, uncheck the verify download option.
-  Under category select CMSIS DAP.
-  In Interface, under Interface select SWD.
-  Press "OK" to save and close the options window.
-  Press Cltr+D to initiate download and debug.
