:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/executeexampleproject>`

Loader File Generation
======================

|

.. note::

   The path of elfloader.exe and initcode .exe should be updated based on the CCES version number and path of installation. The below commands by default will have the CCES version recommended for the given release and the default installation path


   | ===ADSP-SC598 EV-SOM=== Use the following command to generate the loader file for ADSP-SC598 EV-SOM with Carrier board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-SC598 -core0=SS_App_Core0 -init
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkitSC598W_initcode_core0" -core1=SS_App_Core1.dxe 
   -core2=SS_App_Core2.dxe -NoFinalTag=SS_App_Core0 -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 
   0x1 -verbose -o SS_App_SC598.ldr

--------------

ADSP-SC594 EV-SOM
-----------------

Use the following command to generate the loader file for ADSP-SC594 EV-SOM with Carrier board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-SC594 -core0=SS_App_Core0 -init 
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkitSC594_initcode_core0" -core1=SS_App_Core1.dxe
   -core2=SS_App_Core2.dxe -NoFinalTag=SS_App_Core0 -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode
   0x1 -verbose -o SS_App_SC594.ldr

--------------

ADSP-21593 EV-SOM
-----------------

Use the following command to generate the loader file for ADSP-21593 EV-SOM with Carrier board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-21593 -core1=SS_App_Core1.dxe -init
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkit21593_initcode_core1.dxe" -core2=SS_App_Core2.dxe 
   -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_21593.ldr

--------------

ADSP-SC584 EZ-Board
-------------------

Use the following command to generate the loader file for ADSP-SC584 EZ-Board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-SC584 -core0=SS_App_Core0 -init
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkitSC584_initcode_core0_v10" -core1=SS_App_Core1.dxe 
    -core2=SS_App_Core2.dxe -NoFinalTag=SS_App_Core0 -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 
    0x1 -verbose -o SS_App_SC584.ldr

--------------

ADSP-SC589 EZ-Board
-------------------

Use the following command to generate the loader file for ADSP-SC589 EZ-Board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-SC589 -core0=SS_App_Core0 -init 
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkitSC589_initcode_core0_v10" -core1=SS_App_Core1.dxe 
   -core2=SS_App_Core2.dxe -NoFinalTag=SS_App_Core0 -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 
   0x1 -verbose -o SS_App_SC589.ldr

--------------

ADSP-SC573 EZ-Board
-------------------

Use the following command to generate the loader file for ADSP-SC573 EZ-Board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-SC573 -core0=SS_App_Core0 -init 
   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\ezkitSC573_initcode_core0" -core1=SS_App_Core1.dxe 
   -core2=SS_App_Core2.dxe -NoFinalTag=SS_App_Core0 -NoFinalTag=SS_App_Core1.dxe -b SPI -f BINARY -Width 8 -bcode 
   0x1 -verbose -o SS_App_SC573.ldr

--------------

ADSP-21568 SOM
--------------

Use the following command to generate the loader file for ADSP-21568 SOM with Carrier EZ-Lite board.

::

   "C:\analog\cces\3.0.1\elfloader.exe" -proc ADSP-21568 SS_App_Core1 -init ezkit21568W_initcode.dxe -b SPI 
   -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_21568.ldr

.. note::

   The ADSP-21568 processor is supported in CCES 3.0.1.


**Note :** The default ADSP-21568 target application in CrossCore Embedded Studio includes the loader example.

--------------

ADSP-21569 EV-SOM
-----------------

Use the following command to generate the loader file for **ADSP-21569 EV-SOM** with Carrier board and EZ-Board.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-21569 SS_App_Core1 -init 
   ezkit21569_initcode.dxe -b SPI -f BINARY -Width 8 -bcode 0x1 -verbose -o SS_App_21569.ldr

.. note::

   The default ADSP-21569 target application supported for EV-21569-SOM with CRR board and to make the same application to work with ADSP-21569 EZ-KIT, please remove the "ADSP_21569_SOM" macro from the CCES project compiler preprocessor properties.


--------------

ADSP-21489
----------

Use the following command to generate the loader file for ADSP-21489 or the example application CCES project itself generate the SS_App_21489.ldr loader file.

::

   "C:\Analog Devices\CrossCore Embedded Studio 2.11.1\elfloader.exe" -proc ADSP-21489 -si-revision any -bspi -fbinary
   -hostwidth 8 -l"C:\Analog Devices\CrossCore Embedded Studio 2.11.1\SHARC\ldr\489_spi.dxe" -o "./SS_App_21489.ldr"
   "./SS_App_21489.dxe"

Programming the Flash
=====================

|

| Batch files for programming the flash are provided under '**SigmaStudioPlus-Relx.y.z\\Target\\Utilities\\FlashProgrammer**' folder and pre-built loader files (LDR) are provided under '**SigmaStudioPlus-Relx.y.z\\Target\\Examples\\LDR**' folder.
|

.. note::

   The path of cldp.exe inside the batch files should be updated based on the CCES version number and path of installation. The batch file by default will have the CCES version recommended for the given release and the default installation path


--------------

Use the following command to program the flash on **ADSP-SC598 EV-SOM** with Carrier using the pre-built SS_App_SC598.ldr loader file.

::

   Flash_ADSPSC59x.bat SC598 XXXX “<Package folder>\Target\Examples\LDR\SS_App_SC598.ldr”

--------------

Use the following command to program the flash on **ADSP-SC594 EV-SOM** with Carrier Board using the pre-built SS_App_SC594.ldr loader file.

::

   Flash_ADSPSC59x.bat SC594 XXXX “<Package folder>\Target\Examples\LDR\SS_App_SC594.ldr”

--------------

Use the following command to program the flash on **ADSP-21593 EV-SOM** with Carrier Board using the pre-built SS_App_21593.ldr loader file.

::

   Flash_ADSP2159x.bat 21593 XXXX “<Package folder>\Target\Examples\LDR\SS_App_21593.ldr”

--------------

Use the following command to program the flash on **ADSP-SC584 EZ-Board** using the pre-built SS_App_SC584.ldr loader file.

::

   Flash_ADSPSC5xx.bat SC584 XXXX “<Package folder>\Target\Examples\LDR\SS_App_SC584.ldr”

--------------

Use the following command to program the flash on **ADSP-SC589 EZ-Board** using the pre-built SS_App_SC589.ldr loader file.

::

   Flash_ADSPSC5xx.bat SC589 XXXX “<Package folder>\Target\Examples\LDR\SS_App_SC589.ldr”

--------------

Use the following command to program the flash on **ADSP-SC573 EZ-Board** using the pre-built SS_App_SC573.ldr loader file.

::

   Flash_ADSPSC5xx.bat SC573 XXXX “<Package folder>\Target\Examples\LDR\SS_App_SC573.ldr”

--------------

Use the following command to program the flash on **ADSP-21568 SOM** with Carrier EZ-Lite board using the pre-built SS_App_21568.ldr loader file.

::

   Flash_ADSP2156x.bat 21568 XXXX “<Package folder>\Target\Examples\LDR\SS_App_21568.ldr”

--------------

Use the following command to program the flash on **ADSP-21569 EZ-Board** using the pre-built SS_App_21569.ldr loader file.

::

   Flash_ADSP2156x.bat 21569 XXXX “<Package folder>\Target\Examples\LDR\SS_App_21569.ldr”

--------------

Use the following command to program the flash on **ADSP-21489 EZ-Board** using the pre-built SS_App_21489.ldr loader file.

::

   Flash_ADSP214xx.bat 21469 XXXX “<Package folder>\Target\Examples\LDR\SS_App_21469.ldr”

--------------

**XXXX** stands for **KIT** or **1000** or **2000** based on the emulator (KIT Onboard Debug Agent or ICE-1000 or ICE-2000) used for flashing.

.. note::

   The boot switch should be set to ‘1’ and a hard reset of the EZ-Board is required to run the application.


.. note::

   The ADSP-21568 flash boot position should be set to ‘6’ and a hard reset of the EZ-Board is required to run the application.


.. note::

   The evaluation board can be reset to boot application from flash. Once application booted the SigmaStudio plus schematic can be downloaded to target by selecting target processor and SHARC core DXE's in schematic project settings. The "Link Compile Download" step not required if the schematic application source files included into the application that is DemouC application. Just use "Link Compile Connect" option in "Action" tab to connect with target for tuning the schematic application.

