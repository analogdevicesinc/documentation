Added Code to Users Main File
=============================

Includes
--------

Several different #include are inserted at the top of the users file, they are placed underneath the include "adi_initialize.h", since we know that this include will be available in all project created in CCES. All of the includes are required for the project to build, therefore removal of any of them may result in unexpected behavior.

The following image shows the changes that will be made to the users main file.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/freertos-addin-added-headers.png

A list of the includes that will be added can be found below

-  **#include <stdlib.h>** *- required for calls to* **abort()**\ *;*
-  **#include "FreeRTOSUserApplication.h"** *- required for access to* **userStartupTask**
-  **#include "FreeRTOSConfig.h"** *- required for access to FreeRTOS configuration Macros*
-  **#include "FreeRTOS.h"** *- required for call to* **vStartSchedular()** *and other main FreeRTOS functions*

--------------

Task Creation
-------------

The following task is added to the users main file as an example of how the FreeRTOS Add-In can be used It creates a basic task that will run in an infinite loop.

.. image:: https://wiki.analog.com/_media/resources/tools-software/freertos/freertos-addin/freertos-addin-added-code.png

We check want to error check the task, so if it does not have a value of pdPASS then we abort the compilation.

--------------

vTaskStartScheduler();
----------------------

.. note::

   Please do not add any hardware setup codes before the vTaskStartScheduler() function call


Most of the Hardware Setup is for the SSL/DD peripherals ( e.g. the TWI drivers and etc. ). Unlike the BareMetal code, only after the FreeRTOS scheduler has been started can timer tasks be created and executed.

Please refer to the FreeRTOS documentation on the FreeRTOS.org site to get a full description of what this function does https://www.freertos.org/a00132.html
