:doc:`Click here to return to the Basic Modules page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Extended Serial Peripheral Interface(xSPI) Integration For Delay Line Buffer Read/Write Access
==============================================================================================

Description
-----------

| The octal Serial Peripheral Interface (xSPI0/HyperBus) port enables a wider external memory data bus, supporting up to eight parallel bits. For detailed information on xSPI, please consult the relevant hardware reference manual. A dedicated driver is required to configure the xSPI for read/write operations when used as a delay line buffer in SigmaStudio+ schematic delay blocks. If the system lacks DDR RAM support, this delay line buffer will be allocated in external RAM.
| ===== xSPI Integration Steps within the Target Application ===== **1)** Enable the xSPI peripheral using "Pin Multiplexing" option in "system.svc" settings.
| |xspipinmux.png|
| **2)** Add the xSPI driver library **"ADSP-21568_xSPI_Driver_Lib.dlb"** into CCES application using project settings. The xSPI driver library is available in SigmaStudio+ installation folder **"C:\\Analog Devices\\SigmaStudioPlus-Relx.x.x\\Target\\Lib-CCES"**.
|

.. note::

   The ADSP-21568 xSPI support for delay line buffer added from SigmaStudio+ version 2.4.0 onwards


| |xspidriverlibrary.png|
| **3)** A few global variables are used to manage external RAM memory addresses, enabling support for multiple instances of xSPI-based delay blocks. These variables can be integrated into the application as needed. SigmaStudio+ examples use the **XSPI_ENABLE** macro to group all xSPI-related configuration updates across both compiler and linker project settings.
| |xspicompilermacro.png|
| |xspilinkermacro.png|
| **Application code updates:**
| |xspicodeupdate1.png|
|

.. note::

   The ADSP-21568 xSPI memory mapping is 0x60000000 to 0x7FFFFFFF. The end address is depends on the size of the external RAM used in the target platform.


| |xspicodeupdate2.png|
| |xspicodeupdate3.png|
|

.. note::

   The **xSPI_RAM_Init** function is responsible for configuring the xSPI interface and initializing the external memory by setting its contents to zero. On the ADSP-21568 SOM EVAL board, which includes 32MB of external RAM, the size is defined as 0x02000000 bytes. This size should be adjusted to match the actual RAM capacity used on the target platform.


| |xspicodeupdate4.png|
|

.. note::

   The read and program functions are invoked from SigmaStudio+ schematic blocks. As a result, these symbols may be removed during a "Release" build. To ensure the xSPI delay blocks function correctly, these symbols must be placed in the preserve section. Otherwise, a schematic compilation error will occur.


| ===== ADSP-21568 Preload and Init application update for xSPI Speed =====
| The ADSP-21568 Preload and Init application is initially set to use an xSPI speed of 30 MHz by default. To enhance the performance of xSPI-based delay blocks in SigmaStudio+, it is recommended to increase this speed to 70 MHz.

You can build the preload application in **Release** mode. Once compiled, the resulting .dxe file can be used to launch the target application via CrossCore Embedded Studio (CCES).

The Preload CCES application is located at: **C:\\analog\\cces\\3.0.2\\SHARC\\ldr\\init_code\\2156x_Init\\21568w_preload**

| The **CFG0_BIT_CGU0_DIV_DSEL** value need to be changed to **14** for 70Mhz support. |image1|
| The Init application can be built in **Release** mode, and the resulting .dxe file can be used to generate the application loader (.ldr) file for flash boot(:doc:`Loader file Generation </wiki-migration/resources/tools-software/sigmastudiov2/gettingstarted/flash_the_loader_file>`).

| The Init CCES application can be found at: **C:\\analog\\cces\\3.0.2\\SHARC\\ldr\\init_code\\2156x_Init\\21568w_init**
|

.. note::

   The current version of the evaluation (Eval) board supports xSPI clock speeds up to 70 MHz. Future versions are expected to support speeds up to 160 MHz, which will enable maximum performance for this module.

   
   To support higher speeds, updates will be made to the xSPI driver library and the framework's xSPI initialization, including enabling auto command mode for memory clearing. Currently, since external RAM is cleared during the xSPI initialization process, this introduces additional delay during application boot-up. As a result, there is a wait time before the SigmaStudio+ schematic can be downloaded.
   
   | These limitations are expected to be addressed in upcoming Eval board revisions, leading to improved performance and reduced initialization delays.


| ====== Supported Processor ======

-  ADSP-21568

.. |xspipinmux.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspipinmux.png
.. |xspidriverlibrary.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspidriverlibrary.png
   :width: 1080px
.. |xspicompilermacro.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspicompilermacro.png
   :width: 1080px
.. |xspilinkermacro.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspilinkermacro.png
   :width: 1080px
.. |xspicodeupdate1.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspicodeupdate1.png
   :width: 1080px
.. |xspicodeupdate2.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspicodeupdate2.png
   :width: 1080px
.. |xspicodeupdate3.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspicodeupdate3.png
   :width: 1080px
.. |xspicodeupdate4.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/xspicodeupdate4.png
   :width: 1080px
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/speedsettings.png
