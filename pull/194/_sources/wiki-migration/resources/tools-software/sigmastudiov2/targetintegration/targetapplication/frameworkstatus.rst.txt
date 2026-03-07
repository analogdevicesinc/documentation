| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =====Target Framework Status===== The SigmaStudio+ for SHARC (ADSP-SC5xx/ADSP-215xx) Target Framework has five states and these states are core agnostic, meaning, it is ensured that status of all the cores are considered for the overall Target status. For example, if core 2 reaches an erred state, then the overall target status reported by primary core is “error” even if its status is success. The states are explained below.
| 1. IDLE: The Target will be in this state upon hardware reset.
| 2. BOOTED: The Target reaches this state upon successful boot, system and IPC initialization.
| 3. INITED: The Target reaches this state upon successful initialization of connection, communication and Framework components.
| 4. PROCESSING: The Target reaches this state upon successful Framework initialization after SSn code and parameters have been downloaded.
| 5. ERROR: The Target ends up in error state if any of the APIs returns an error.
| =====LED Pattern for indicating Target Framework Status===== Six LEDs are used within the application to indicate the Target status. The LED pattern for the various states are described in the table below. The rest of the LED’s will be off. Note:
| 1. ADSP-SC589 EZ-Board does not have on board LED’s and hence Target Framework and processing errors are not indicated through LED’s.
| 2. LED 15 of ADSP-SC573 EZ-Board will always be turned ‘On’ when USBi is connected to ADSP-SC573 EZ-Board and cannot be used as the GPIO pin used for LED 15 and SPI 1 are same. Hence, LED 16 is used instead of LED 15 to indicate the Target Framework and processing errors for ADSP-SC573 EZ-Board.
| |image1|
|

.. note::

   ADSP-21593/ADSP-SC594/ADSP-SC598 EV-SOM with carrier boards follows the same LED pattern of ADSP-21569 for indicating target framework status. ADSP-SC589 MINI board follows the same LED pattern of ADSP-21569 for indicating target framework status, except that the LEDs 9, 10 and 7 are replaced with LED’s 10, 11 and 12 respectively.


| =====LED Pattern for indicating non-terminal processing error===== While processing, there can be non-terminal errors such as data clipping and NAN errors. These are indicated by the following LED patterns.
| |image2|
|

.. note::

   The Library Integration examples available in the package won't support LED status.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/led2156x.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/lednonterminal2156x.png
   :width: 600px
