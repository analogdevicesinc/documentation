====== Sharc Audio Module - Environment Setup and Compilation ====== *The following instructions detail how to set up the rest of the PC environment and how to compile the program.*

PATH Setup
==========

*The system needs to know where it can access make, the compilers for the SHARC and ARM cores and other tools. These tools reside within the installation of the CrossCore Embedded Studio that was* :doc:`installed previously </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>`\ *.*

-  *If you already have CCES in your path by default, this section can be skipped.*
-  *These instructions need to be re-run every time a new instance of your command terminal is opened if CCES is not in your path by default.*
-  *If you have multiple versions of CCESS installed, pick either the latest or the version specific to your project. CCES is typically installed in C:\\Analog Devices\\CrossCore Embedded Studio <CCES VERSION>*

**To include a specific CCES Installation to PATH:**

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| 1. Open a file explorer and navigate to the root of the Audio Starter project within the cloned repository and open the *env.sh* file using a preferred text editor. | |image7|          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| 2. Modify the **CCES_VERSION** parameter of *env.sh* to match the version of CCES installed on your PC.                                                              | |image8| |image9| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| 3. Open the Git Bash application and navigate to the root of the Sam-Audio-Starter of the cloned repository                                                          | |image10|         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| 4. Run the command:                                                                                                                                                  | |image11|         |
| // source env.sh //                                                                                                                                                  |                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+
| 5. Verify that CCES has been added to your path by running the command *echo $PATH*                                                                                  | |image12|         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------+

--------------

SAM GUI Flash Tool Installation
===============================

**Only available for software that can be updated using the SAM Flasher!** :doc:`See Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`

*The SAM GUI Flash Tool is a standalone tool that allows for application reflash of the SAM once the bootloader is installed.*

**To install the GUI:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
| 1. Open a file explorer and navigate to *<BOOTLOADER_PROJECT_ROOT>/bootloader/prebuilt* and double-click *sam-flasher_v0.0.5_setup.exe* to run the installer. | |image20|                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
| 2. Follow the default setup instructions to install the tool.                                                                                                 | |image21| |image22| |image23| |image24| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+
| 3. Once installed, it can be searched for, or found under *SAM Flasher*.                                                                                      | |image25| |image26|                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------+

--------------

USB to UART Bridge Driver Setup
===============================

**Only required for ADZS-SC589-MINI v2.1 when the USB/UART interface is needed for UART Flashing. This driver and port will not be used during the audio example demonstrations.**

*The USB to UART Bridge Driver is a Windows library that is used to emulate a serial connection over USB to the USB/UART (type Micro) on the ADSZ-SC589-MINI v2.1 hardware.*

**To install the USB to UART Bridge Driver:**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. In a web browser, navigate to https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads                                                                                                                                 | |image36|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. Under *Software*, select *CP210x Universal Windows Driver* to download the latest driver.                                                                                                                                                    | |image37|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.                                                                                           | |image38|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. Plug the USB Micro Type B side to the SAM board USB/UART connector and the USB Type A side to a USB connection on the PC. *Note that the PC may say that the USB driver did not install or is not functioning properly. This is ok for now.* | |image39|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 5. On the PC, open up *Device Manager* and navigate to *Other Devices*. Here you will see the USB to UART Bridge Controller recognized but with no associated driver.                                                                           | |image40| |image41| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 6. Right click on *USB to UART Bridge Controller* and select *Update driver*.                                                                                                                                                                   | |image42|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 7. Select *Browse my computer for drivers* and navigate to the location which contains the unzipped *.inf* file (unzipped from the downloaded zip file)                                                                                         | |image43|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 8. Once the driver has finished installing, it will appear under *Ports* as *Silicon Labs CP210x USB to UART Bridge* or something similar.                                                                                                      | |image44|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

--------------

Application Compilation
=======================

*The following instructions are used to compile the application binaries.*

**To compile the application:**

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. In a Windows directory, navigate to //<project_root>/build //                                                                                               | |image48| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. On the command line, type *make -j4*                                                                                                                        | |image49| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. A successful compilation creates four binaries in the *build* folder, one for each core (For debugging) and one combined binary (for reflash). For example: | |image50| |
| *ARM Core (Debug): SAM-Audio-Starter-ARM.exe*                                                                                                                  |           |
| *SHARC0 Core (Debug): SAM-Audio-Starter-SHARC0.dxe*                                                                                                            |           |
| // SHARC1 Core (Debug): SAM-Audio-Starter-SHARC1.dxe//                                                                                                         |           |
| // Combined Flash File: SAM-Audio-Starter.ldr//                                                                                                                |           |
| *Note that the names of the DXEs and LDR may vary depending on the project.*                                                                                   |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Prerequisites#.|Advanced Audio Projects#.program-flash|Bootloader and Application Flash <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.prerequisites>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env4.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/path1.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sourceenv.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/path2.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env1.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env2.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/env4.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/path1.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sourceenv.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/path2.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam1.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam2.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam3.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam5.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam6.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam7.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam8.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam1.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam2.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam3.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam5.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam6.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam7.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam8.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart0.png
   :width: 200px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uartdriver.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart1.png
   :width: 200px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld4.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart2.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart3.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart4.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart5.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart0.png
   :width: 200px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uartdriver.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart1.png
   :width: 200px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld4.png
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart2.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart3.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart4.png
   :width: 400px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uart5.png
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile1.png
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile2.png
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile3.png
   :width: 400px
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile1.png
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile2.png
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/compile3.png
   :width: 400px
