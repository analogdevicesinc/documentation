Go back to :doc:`Home Page </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>`

Network_Configuration
=====================

This xml element contains sub elements with attributes as below:


|image1|

-  Discovery_Mode – Simple/Modified/Optimized - Discovery mode selection.
-  Discovery_StartDelay_ms – PLL lock time. To wait after software reset and before starting Discovery.
-  Line_Diagnostics – Enable/Disable Line Diagnostic post discovery.
-  Auto_Rediscovery_upon_Critical_Fault – Enable/Disable automatic rediscovery upon critical fault during discovery process.
-  Number_of_Discovery_Attempts_on_Critical_Fault – No. of automatic discovery attempts.
-  Auto_Rediscovery_upon_Post_Discovery_Fault – Enable/Disable automatic rediscovery for post discovery fault.
-  Rediscovery_Interval_ms – Time between rediscovery attempts.
-  Partial_Discovery_Upon_Post_Discovery_Fault – Enable/Disable Partial discovery upon line faults.
-  Current_Interface – I2C/SPI
-  Redisc_WaitTime - Rediscovery wait time
-  Number_of_Peripheral_Devices – No. of peripheral devices connected to the Target Processor.
-   Network_Peripheral_x_Config – Each element Contains attributes like :doc:`Peripheral_x_Config </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml/masterslavechain>` in sub node element.

Each attribute is of “String” Data type.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/image33.png
