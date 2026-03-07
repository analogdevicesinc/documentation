:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

WAV Player
==========

The plug-in is located in the SigmaStudio+ Tree Toolbox window, as shown below. |WavPlayerToolbox.jpg|


|WavPlayerforSharc.jpg|

Description
-----------

| 
| The WAV Player module is designed to facilitate playback of audio files stored in external flash memory, interfaced with the ADSP-215xx/ADSP-SC5xx processor via the SPI (Serial Peripheral Interface). This module enables seamless reading of WAV files from flash and supports real-time pitch shifting, allowing dynamic adjustment of pitch during playback without affecting audio duration.

The module supports WAV files that include a standard WAV header and adhere to the little-endian byte format. It is compatible with audio sample resolutions of 8, 16, 24, or 32 bits per sample, using signed integer data types. The WAV Player module does not have any audio input pins. It features five control input pins, one audio output pin, and one control output pin. And also, it Includes pause and loopback functionality.

**Key Features:**

**SPI-Based WAV File Access:** Enables reading of WAV files stored in external flash through the SPI interface.

**Real-Time Pitch Shifting:** Supports pitch modification during playback for audio effects or tuning.

**WAV File Format Support:** Compatible with WAV files that include headers and use little-endian signed integer formats (8/16/24/32-bit samples).

**Channel Growth Capability:** Allows channel growth, where each growth instance supports the playback of one WAV file. The module supports up to five channels, enabling simultaneous playback of up to five different WAV files.

**Memory Offset Configuration:** Includes a control parameter that lets users specify the byte offset in flash memory, indicating where the WAV file begins. This feature provides flexibility in managing and accessing multiple audio files stored in flash.

**Limitations:**

-  Supports up to five .wav files. The Wav Player can support upto 5 growths.

-  Compatible with signed 16-bit little-endian .wav file format.

-  Allows pitch shifting with a factor of up to 10x.

Targets Supported
-----------------

========== =====================
Name       ADSP-215xx/ADSP-SC5xx
========== =====================
WAV Player Block
========== =====================

| 
| ===== Pins =====

Input
~~~~~

============= ======= ===============
Name          Type    Description
============= ======= ===============
Pitch Input   Control Input channel 0
Counter Input Control Input channel 1
Play/Stop     Control Input channel 2
Pause/Resume  Control Input channel 3
Loopback      Control Input channel 4
============= ======= ===============

Output
~~~~~~

========== ======= ================
Name       Type    Description
========== ======= ================
WavOutput  Analog  Output channel 0
CounterOut Control Output channel 1
========== ======= ================

Control Pins
------------

+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Range              | Data Type        | Function Description                                                                                                                                                                     |
+====================+====================+==================+==========================================================================================================================================================================================+
| Pitch Input        | 0.1 to 10x         | float            | This pin defines the pitch factor input for the module.                                                                                                                                  |
+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Counter Input      | 0 to 214,74,83,647 | Unsigned Integer | This pin specifies the number of times a wav player must read a wave file.                                                                                                               |
+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Play/Stop          | 1(on)/0(off)       | Boolean          | The value on the First Sample pin determines whether the WAV file playback should continue or stop. A value of ‘1’ indicates playback (Play), while a value of ‘0’ indicates stop (Stop) |
+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pause/Resume       | 1(on)/0(off)       | Boolean          | The value on the First Sample pin controls playback state. A value of ‘1’ pauses playback, while a value of ‘0’ resumes it.                                                              |
+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Loopback           | 1(on)/0(off)       | Boolean          | The value on the First Sample pin specifies the playback mode of the WAV Player: a value of ‘1’ enables Repeat mode, while a value of ‘0’ sets it to Counter mode.                       |
+--------------------+--------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range              | Function Description                                                                                                                                                                        |
+====================+===============+====================+=============================================================================================================================================================================================+
| WAV Offset         | 0             | 0 to 214,74,83,647 | This control can be used to set the WAV file offset in flash memory (bytes)                                                                                                                 |
+--------------------+---------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 5             | Number of input and output channels. For each channel, there are 5 input pins and 2 output pins. The overall number of input and output pins scales with the number of configured channels. |
+--------------------+---------------+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== Memory =====

========== ============ ============ =============
Processor  Code (Bytes) Coeff(Bytes) Data32(Bytes)
========== ============ ============ =============
ADSP-215xx 13356        4            400
========== ============ ============ =============

MIPS (Delay = Block size )
--------------------------

========== ============= ==============
Processor  Default(1 Ch) 2 Growth(2 Ch)
========== ============= ==============
ADSP-215xx 1.1           2.1
========== ============= ==============

Package Information
-------------------

| Please find the attached package containing the necessary resources for running the WavPlayer module using ADSP-21569 and SC584 Eval boards:
| `WAV Player Supported Files <https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/WavPlayerSupportedPackage.zip>`_
| The package includes the following folders:
| **Flash_Files:** A batch file along with the required WAV files for flashing onto the hardware.

**SourceFiles:** Contains the necessary .c and .h files for integrating or modifying the target application.

| **SchematicFiles:** Reference SigmaStudio+ schematic files for various channel configurations (ADSP-21569).
| ===== Flashing Example WAV Files ===== Follow the steps below to flash the example WAV files to the external flash memory connected to the ADSP-215xx/ADSP-SC5xx EZ-KIT:

**Connect the Emulator:** Attach the ICE-1000 or ICE-2000 emulator to the EZ-KIT board.

**Install Development Tools:** Ensure that CrossCore Embedded Studio (CCES) version 3.0.3 is installed on your system.

**Locate Flash Script:** Navigate to the Package directory and locate the **Flash_ADSPSC584.bat** or **Flash_2156x.bat** file (based on the processor).

**Run Flash Script:** Execute the .bat file corresponding to your EZ-KIT platform. This will launch a command line interface displaying the flashing progress for each WAV file, as shown in the below image.


|FlashFileStatus.jpg|

**Flashing Custom WAV Files:**

\* To flash custom WAV files at different flash memory offsets, modify the filename and offset value within the batch script.

\* Ensure the custom WAV files are placed in the same directory as the batch file before execution.

Steps to run the Wav Player using Demo Application
--------------------------------------------------

The following changes must be made to the ADSP-SC5xx/ADSP-215xxSigmaStudio demo application to ensure the correct functioning of the WAV Player module on the EZ-Kits. These changes configure the flash, SPI and cache as required by the WAV Player module.

**Import the CCES demo projects for ADSP-SC5xx/ADSP-215xx**

|ImportDemoApplication.jpg| **Demo application changes for ADSP SC58x/2158x/SC57x/2157x processors**

**Pin multiplexing**

1. Add the Pin multiplexing Add-in to Sharc Core 0 project. Upon successful addition the plugin must appear in the installed Add-in view

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/AddPinMuxing.jpg
   :alt: AddPinMuxing.jpg

2. Enable SPI2 in the Pin multiplexing and select MISO, MOSI, CLK, SEL1, D2, D3 as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/enablespi2.jpg
   :alt: enablespi2.jpg

**Software switch configuration**

Ensure the SPI2FLASH_CS_EN is enabled in adi_ss_softconfig_SC5xx.c file. |SoftConfiguration.jpg| \**Configuring Flash \*\*

Add the callback function **wavplayerSetupFlash()** to **adi_ss_app_sh0.c** file and set the following flash configuration parameters:

::

          1. Flash start address 
          2. Flash end address 
          3. Flash quad read command opcode 
          4. Address size 
          5. Address pins  
          6. Dummy size 

This call back function is called during initialization of the WAV player module. The flash configuration parameters for the ADSP-SC5xx EZ-KIT flash is as shown below.


|WavPlayerSetupFlash.jpg|

Include the file adi_initSPIMode.c in the Sharc Core0 application. This file has the function definition for InitializeSPIMode() and which sets up the SPI in memory mapped read mode. Invoke this function within the wavplayerSetupFlash() function after configuring the flash properties.

Include the file platform_flash_config.c in the Sharc Core0 application. This file has the function definition for SetFlashMode() and which sets the quad enable bit in the ADSP-SC5xx EZ-KIT flash to allow quad SPI memory mapped reads.

Within adi_ss_app_sh0.c file, add the call to functionSetFlashMode() in the main() function just after the call to ConfigSoftSwitches() function, as shown below

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/ConfigureSoftSwitch_2156x_1.jpg
   :alt: ConfigureSoftSwitch_2156x_1.jpg

Include the header “adi_wavplayer.h" in the adi_ss_app_sh0.c file and include this header file in the Sharc Core0 application project.

In the Sharc Core 0app.ldf file add KEEP (wavplayerSetupFlash.) and KEEP(InitializeSPIMMode.) to retain the symbol.

|ldfChanges.jpg| **Cache configuration**

Enable cache 16KB andset\*pREG_SHL1C0_CFG = ENABLE_I_D_CACHE in adi_ss_config_I_D_cache(void) in file adi_ss_cache_config.c.


|CacheConfiguration.jpg|

Cache configuration and modification in adi_ss_cache_config.c

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/CacheConfiguration_1.jpg
   :alt: CacheConfiguration_1.jpg

After making the above changes, rebuild the projects to create the application dxes.

**Demo application changes for ADSP-2156x processors**

The following changes are required for the SigmaStudio Demo application on ADSP-2156x processor located in “C:\\Analog Devices\\SigmaStudioPlus-Relx.x.0\\Target\\Examples\\Demo\\ADSP-2156x\\ADSP-21569\\SS_App_Core1” folder.

NOTE: CrossCore Embedded Studio (CCES) v3.0.3 shall be used for building the above mentioned ADSP-21569 application.

**Pin multiplexing**

1. Add the Pin multiplexing Add-in to Sharc Core 0 project. Upon successful addition the plugin must appear in the installed Add-in view as below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/AddPinMuxing2156x.jpg
   :alt: AddPinMuxing2156x.jpg

2. Enable SPI2 in the Pin multiplexing and select MISO, MOSI, CLK, SEL1, D2, D3 as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/SPI22156x.jpg
   :alt: SPI22156x.jpg

**Software switch configuration**

Ensure the SPI2FLASH_CS_EN and SPI2D2_D3_EN is enabled in *adi_ss_softconfig_21569.c* file and *adi_ss_sys.c*

|SwitchConfiguration2156x.jpg| |SwitchConfig_2_2156x.jpg|

**Configuring Flash**

Add the callback function wavplayerSetupFlash() to adi_ss_app_sh0.c file and set the following flash configuration parameters: 1. Flash start address

2. Flash end address

3. Flash quad read command opcode

4. Address size

5. Address pins

6. Dummy size

This call back function is called during initialization of the WAV player module. The flash configuration parameters for the ADSP-21569 EZ-KIT flash is as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/WavPlayersetupFlash_2156x.jpg
   :alt: WavPlayersetupFlash_2156x.jpg

Include the file adi_initSPIMode.c in the Sharc Core0 application. This file has the function definition for InitializeSPIMode(), which sets up the SPI in memory mapped read mode. . Invoke this function within the wavplayerSetupFlash() function after configuring the flash properties.

Include the file platform_flash_config.c in the Sharc Core0 application. This file has the function definition for SetFlashMode() which sets the quad enable bit in the ADSP-21569 EZ-KIT flash to allow quad SPI memory mapped reads.

Within adi_ss_app_sh0.c file, add the call to functionSetFlashMode() in the main() function just after the call to ConfigSoftSwitches() function, as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/ConfigureSoftSwitch_2156x_1.jpg
   :alt: ConfigureSoftSwitch_2156x_1.jpg

Include the header “adi_wavplayer.h" in the adi_ss_app_sh0.c file and add the link to the Sharc Core0 application project properties.

In the Sharc Core 0app.ldf file add KEEP (wavplayerSetupFlash.) and KEEP(InitializeSPIMMode.) to retain the symbols.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/APP_2156x.ldf.jpg
   :alt: APP_2156x.ldf.jpg

**Cache configuration and other changes to the project**

Enable 16KB cache and set \*pREG_SHL1C0_CFG = ENABLE_I_D_CACHE in function adi_ss_config_I_D_cache() in file adi_ss_cache_config.c.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/CacheConfiguration_2156x.jpg
   :alt: CacheConfiguration_2156x.jpg

In the compiler preprocessor section of the project properties, add the following preprocessor definition: “ADI_SPORT_BLOCKING_MODE=1”

Click on system.svc and from the overview tab, add OSPI driver add-in to the project as shown below

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/OSPIDriverAdd.jpg
   :alt: OSPIDriverAdd.jpg

After making the above changes, rebuild the project to create the application dxe that can be used with the wav player SigmaStudio plugin.

.. |WavPlayerToolbox.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/WavPlayerToolbox.jpg
.. |WavPlayerforSharc.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/WavPlayerforSharc.jpg
.. |FlashFileStatus.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/FlashFileStatus.jpg
.. |ImportDemoApplication.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/ImportDemoApplication.jpg
.. |SoftConfiguration.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/SoftConfiguration.jpg
.. |WavPlayerSetupFlash.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/WavPlayerSetupFlash.jpg
.. |ldfChanges.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/ldfChanges.jpg
.. |CacheConfiguration.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/CacheConfiguration.jpg
.. |SwitchConfiguration2156x.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/SwitchConfiguration2156x.jpg
.. |SwitchConfig_2_2156x.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/SwitchConfig_2_2156x.jpg
