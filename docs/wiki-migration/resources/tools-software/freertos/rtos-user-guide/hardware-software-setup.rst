Hardware and software set up
============================

To run the FreeRTOS examples, this section would guide users how to get the hardware and software ready, including get the FreeRTOS source code and set up running environment.

--------------

Get the hardware ready
----------------------

The Analog Devices FreeRTOS product supports reference development board from Analog Devices for the SHARC+ and Blackfin BF70x processor families.

Below is a list of the hardware involved.

\*\* ADI reference board: \*\*

+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Evaluation Board  | Link                                                                                                                                            |
+===================+=================================================================================================================================================+
| ADSP-BF707 EZ-kit | :adi:`eval-bf707.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-bf707.html>`                               |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-SC573 EZ-kit | :adi:`SC573EZKIT.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/SC573EZKIT.html>`                               |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-SC584 EZ-kit | :adi:`EVAL-ADSP-SC584.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC584.html>`                     |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-SC589 EZ-kit | :adi:`EVAL-ADSP-SC589.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADSP-SC589.html>`                     |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-21569 EZ-kit | :adi:`ev-21569-ezkit.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-21569-ezkit.html>`                       |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-SC594 EZ-kit | :adi:`ev-SC594-ezkit.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ev-SC594-ezkit.html>`                       |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ADSP-SC598 EZ-Kit | :adi:`EV-SC598-EZKIT.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EV-SC598-EZKIT.html>`                       |
+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

\*\* Jtag debugger: \*\*

-  ICE1000/2000: :adi:`emulators.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/emulators.html>`

\*\* PC: \*\*

A Windows 8.1 or 10 PC is required. Verify that your PC has these minimum requirements:

-  2 GHz single core processor; 3.3GHz dual core or better recommended
-  4 GB RAM; 8GB or more recommended
-  3 GB available disk space
-  1 USB port for ICE
-  1 USB port for UART (required for I/O on Cortex-A5 cores)

--------------

Get the source code ready
-------------------------

Latest versions
~~~~~~~~~~~~~~~

For ADI FreeRTOS version 2.0.0 and later, combined sources are available from GitHub: :git-freertos:`FreeRTOSv10.4.x`

The latest sources are automatically downloaded and configured via the FreeRTOS Add-In for CCES, more details can be found at :doc:`freertos-addin </wiki-migration/resources/tools-software/freertos/freertos-addin>`

Previous versions
~~~~~~~~~~~~~~~~~

For details on finding legacy versions of FreeRTOS, see :doc:`legacy-versions </wiki-migration/resources/tools-software/freertos/legacy-versions>`

--------------

CrossCore Embedded Studio
-------------------------

CrossCore Embedded Studio is available from :adi:`adswt-cces.html <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`

FreeRTOS is supported from CrossCore Embedded Studio version 2.8.0. The FreeRTOS Add-In is supported from CrossCore Embedded Studio version 2.10.1.

System Resources Used By FreeRTOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Details of the system resources used by FreeRTOS can be found :doc:`here </wiki-migration/resources/tools-software/freertos/rtos-user-guide/system-resources-used-by-freertos>`.
