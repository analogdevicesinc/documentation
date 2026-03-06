Software environment set up for CrossCore Embedded Studio
=========================================================

This part shows the software environment setup for CrossCore Embedded Studio on the below five kinds of boards:

-  ``ADSP-BF707 EzKit``
-  ``ADSP-21569 EzKit``
-  ``ADSP-SC573 EzKit`` (``Cortex-A5`` and ``SHARC``)
-  ``ADSP-SC584 EzKit`` (``Cortex-A5`` and ``SHARC``)
-  ``ADSP-SC589 EzKit`` (``Cortex-A5`` and ``SHARC``)

--------------

Common Software
---------------

**CCES**

Analog Devices :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>` version ``2.9.1`` or later.

**FreeRTOS-Addin**

Analog Devices :doc:`FreeRTOS-Addin product </wiki-migration/resources/tools-software/freertos/freertos-addin>` version ``1.0.0`` or later.

**FreeRTOS-Addin Examples**

Git Usage for downloading FreeRTOS-Addin Examples version ``1.0.0`` from github

.. code:: bash

   git clone https://bitbucket.analog.com/scm/dte/freertos-addin-examples.git

   cd freertos-addin-examples

   git branch -a 

   git checkout -b develop/freertosaddin-1.0.0 remotes/origin/develop/freertosaddin-1.0.0

   git pull

--------------

ADSP-BF7XX EZ-Kit
-----------------

-  Analog Devices CrossCore Embedded Studio version 2.9.1 or later
-  Analog Devices FreeRTOS-Addin product version 1.0.0 or later.
-  Analog Devices FreeRTOS-Addin Examples version 1.0.0

No other software needed to run the examples in CCES on ADSP-BF707 board.

--------------

ADSP-2156X EZ-Kit
-----------------

-  Analog Devices CrossCore Embedded Studio version 2.9.1 or later
-  Analog Devices FreeRTOS-Addin product version 1.0.0 or later.
-  Analog Devices FreeRTOS-Addin Examples version 1.0.0

No other software needed to run the examples in CCES on ADSP-2156X board.

--------------

ADSP-SC589/ADSP-SC584/ADSP-SC573
--------------------------------

-  Analog Devices CrossCore Embedded Studio version 2.9.1 or later
-  Analog Devices FreeRTOS-Addin product version 1.0.0 or later
-  Analog Devices FreeRTOS-Addin Examples version 1.0.0
-  For the users who want to try LwIP, install :adi:`TCP/IP Stack for CrossCore Embedded Studio Rev. 2.6.0 <en/design-center/processors-and-dsp/evaluation-and-development-software/adswp-lwip.html#dsp-relatedsoftware>` for CCES and please refer to the linked page :ez:`add the LwIP patch with CCES V2.9.0 or later <dsp/software-and-development-tools/freertos/w/documents/15283/how-to-use-the-lwip-dnsclient-freertos-example-with-the-cces-v2-9-0-or-later>` configure the LwIP support configuration

--------------
