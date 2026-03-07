Version history for the FreeRTOS Add-In. Trivial changes have been omitted.

1.1.0
=====

-  Introduced support for

   -  ADSP-SC83x (SHARC-FX and Cortex-M33 cores)

-  Configuration options that are not available for a processor are hidden rather than disabled.

Known Issues

-  'Generate Run-Time Statistics' doesn't have the prerequisite portGET_RUN_TIME_COUNTER_VALUE or portCONFIGURE_TIMER_FOR_RUN_TIME_STATS functionality.

.. _section-1:

1.0.1
=====

-  Fixed a bug where if the previous git hash wasn't found we didn't update the new hash.
-  Fixed a bug where the configUSE_QUEUE_SETS value wasn't being saved.

.. _section-2:

1.0.0
=====

Initial release providing support for:

-  ADSP-BF70x
-  ADSP-SC5xx (SHARC+, Cortex-A5 and Cortex-A55 cores)
-  ADSP-215xx
