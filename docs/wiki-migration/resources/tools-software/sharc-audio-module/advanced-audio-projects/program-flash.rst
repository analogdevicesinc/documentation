====== Sharc Audio Module - Program Flash ====== *The following instructions detail how to flash the bootloader and application for the Audio Starter project.*

Bootloader Flash
================

**Only required for software that can be updated using the SAM Flasher (ADZS-SC589-MINI)! Skip this step otherwise.** :doc:`See Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`

*The bootloader allows for application reflash via the SAM Flash Tool depending on a pushbutton state. Note that this step requires you to identify which version of SAM hardware you have, as the script to use will change depending on the hardware version.*

**Follow the instructions below to flash the bootloader:**

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 1. Identify if you have the SAM hardware version v1.4 (or earlier) or v1.5 or greater. The version should be printed on the silkscreen on the back.                                                      | |image14| |image15| |image16| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 2. Prior to powering on the board, ensure that the JP1 jumper is set to position 1-2.                                                                                                                    | |image17| |image18|           |
| Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.                                                       |                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 3. Connect the USB cable for the :adi:`ICE-1000 or ICE-2000 <ice1000>` to the PC and to the ICE. If the device is powered on, a green light will appear.                                                 | |image19| |image20|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 4. Connect the 10-pin header to the ICE and to the Debug Header on the SAM (labeled *DEBUG*) - noting that the header is keyed.                                                                          | |image21|                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 5. Recall where you downloaded/cloned your bootloader software:                                                                                                                                          |                               |
| *See* :doc:`prerequisites#download_bootloader_software </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>`                                              |                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 6. Open the Git Bash application and navigate to *<BOOTLOADER_PROJECT_ROOT>/bootloader/prebuilt*                                                                                                         | |image22|                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 7. *Optional If using the ICE-1000*: Open with your preferred text editor:                                                                                                                               | |image23|                     |
| *boot0_hw_rev_1_4_cldp.bat* and *boot1_hw_rev_1_4_cldp.bat* if your hardware is v1.4 or earlier *or*                                                                                                     |                               |
| *boot0_hw_rev_1_5_cldp.bat* and *boot1_hw_rev_1_5_cldp.bat* if your hardware is v1.5 or greater and modify the *-emu 2000* option to *-emu 1000* to match the emulator in use. Save and close the files. |                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 8. At the command line, enter the command                                                                                                                                                                | |image24| |image25|           |
| *./boot0_hw_rev_1_4_cldp.bat* if your hardware is v1.4 or earlier *or*                                                                                                                                   |                               |
| *./boot0_hw_rev_1_5_cldp.bat* if your hardware is v1.5 or greater.                                                                                                                                       |                               |
| *Note that during program flash, the emulator LED will change from green to purple while the update is ongoing and will return to green once the update is completed.*                                   |                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 9. At the command line, enter the command                                                                                                                                                                | |image26|                     |
| *./boot1_hw_rev_1_4_cldp.bat* if your hardware is v1.4 or earlier *or*                                                                                                                                   |                               |
| *./boot1_hw_rev_1_5_cldp.bat* if your hardware is v1.5 or greater.                                                                                                                                       |                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+

--------------

CLD CDC USB Driver Setup
========================

**Only required for software that can be updated using the SAM Flasher (ADZS-SC589-MINI)! Skip this step otherwise.** :doc:`See Software Compatibility </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>` *Note that this only needs to be done once, but MUST be done after flashing the bootloader in the previous step!*

*The CLD CDC Driver is a driver that lives on the PC that acts as an interface between a serial terminal, such as* `TeraTerm <https://ttssh2.osdn.jp/index.html.en>`_\ *, or the SAM GUI Flash Tool. This driver is required for USB to Serial emulation and to be able to interact with the bootloader or application at run-time on the physical SAM hardware.*

**To install the CLD CDC Driver:**

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Recall where you downloaded/cloned your bootloader software (:doc:`prerequisites#download_bootloader_software </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>`) and open File explorer and navigate to *<BOOTLOADER_PROJECT_ROOT>/bootloader/prebuilt/driver* and unzip *driver.zip*            | |image30| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Right-click on the *.inf* file and select *install*.                                                                                                                                                                                                                                                                                                | |image31| |
|                                                                                                                                                                                                                                                                                                                                                        | |image32| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

Application Flash via SAM Flasher
=================================

*Only available for products that support SAM Flasher updates!*

**Follow the instructions below to flash the application via the SAM Flasher:**

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.                                                                            | |image42|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. Plug the USB Micro Type B side to the SAM board USB connector and the USB Type A side to a USB connection on the PC.                                                                                                          | |image43|           |
| **Note that on SAM v2.1 HW this is the connection on the board labeled USB OTG**                                                                                                                                                 |                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. On the SAM board, press and hold buttons PB1 and PB2. While still holding PB1 and PB2, press RESET.                                                                                                                           | |image44|           |
| *Note that you do not need to hold reset. Resetting the board while holding PB1 and PB2 down will tell the bootloader to stay in the bootloader and await instructions for application ​flash.*                                  |                     |
| *If this is successful, LED10 will blink, while LED11 and LED12 will remain off.*                                                                                                                                                |                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. Open the SAM Flasher Tool                                                                                                                                                                                                     | |image45|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 5. Select the *Comm Port* labelled *SC5xx Communications Port*.                                                                                                                                                                  | |image46|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 6. Select *Load* and navigate to the LDR that was :doc:`generated </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/environment_setup>` during compilation.                                   | |image47|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 7. Select *Update*. The program *Status* will specify that it is erasing flash. Once it has completed, the program *Status* will specify that it has completed. You can close the SAM Flasher Tool after this.                   | |image48| |image49| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 8. To enter the application, press the RESET button on the SAM again. If the application has properly loaded, LED10 will blink and LED11 will remain on. You will be able to additionally access the shell.                      | |image50|           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Application Flash via CLPD via Bootswitch
=========================================

*Only available for products that support CLPD updates via Bootswitch!*

**Follow the instructions below for products which support CLPD updates via Bootswitch:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 1. Set the bootswitch rotary switch to *0*. This tells the device to not automatically boot.                                                                                                                                                                                                                                                                  | |image58|\ |image59| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 2. Power on your board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green PWR LED will light up.                                                                                                                                                                                                              | |image60|            |
| *Location of LED will vary based on device.*                                                                                                                                                                                                                                                                                                                  |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 3. Plug the ICE-1000 or ICE-2000 JTAG header into board header labelled *DEBUG*. Ensure that the USB-A connector is plugged into a USB-A receptacle on the PC and ensure the status of the debugger shows a green LED.                                                                                                                                        | |image61| |image62|  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 4. Recall where you downloaded/cloned your application software (:doc:`prerequisites#clone_repositorydownload_application_software </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>`) and using Windows command prompt, navigate to *<​project_root>/​build* ​and run *flash.bat*                          | |image63|            |
| *Note that the update may take some time to complete.*                                                                                                                                                                                                                                                                                                        |                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| 5. Set the blue rotary switch back to 1 and reset the board to allow the software update to take effect.                                                                                                                                                                                                                                                      | |image64|            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

Application Flash via CrossCore Serial Flash Programmer
=======================================================

*This section will explain how to flash an application with the CrossCore Serial Flash Programmer, ccsfp.exe.*

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Set the bootswitch to the position for "UART boot". For example, on the SC584-EZLITE, set the rotary boot switch to position "7" for UART boot. On SC598-EZKIT and SC594-EZKIT, set it to position "3". For detailed info on boot switch positions, consult the schematic for your target board.                                                                                                                    | |image78| |
| *If using the SC589-MINI, place the "BOOT MODE" jumper (JP1) to position 2-3.*                                                                                                                                                                                                                                                                                                                                         |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                                                                                                                                                                                                                                                                                                                                                                                                                        | |image79| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Power on your board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green PWR LED will light up.                                                                                                                                                                                                                                                                       | |image80| |
| *Location of LED will vary based on device.*                                                                                                                                                                                                                                                                                                                                                                           |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Plug a micro-USB cable from your PC into the USB/UART port on your evaluation kit. For SC594 and SC598, plug it to USB type C port on the SOM.                                                                                                                                                                                                                                                                      | |image81| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                                                                                                                                                                                                                                                                                                                                                                                                                        | |image82| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Open the "CrossCore Serial Flash Programmer" program included in the :adi:`CrossCore Utilities <en/design-center/evaluation-hardware-and-software/software/crosscore-utilities.html>` package. This can be done either through the Windows Start Menu or by finding the executable at "C:\\Analog Devices\\CrossCoreUtilities-Rel1.7.1\\bin\\ccsfp.exe", assuming a standard installation path.                     | |image83| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Select the Target board, Serial Port, and Baudrate to connect to your ADSP platform. The standard baud rate is 115200. Then select the .ldr file to flash to your target platform.                                                                                                                                                                                                                                  | |image84| |
| *SC589-MINI users should select the "SHARC Audio Module" for the target. Serial Port will differ for each individual kit, but should be the USB/UART connector on most kits. The correct COM port will show up as "Silicon Labs CP210x USB to UART Bridge". For SC594-EZKIT, select ADSP-SC594 SOM and for the SC598-EZKIT, select ADSP-SC598 SOM*                                                                     | |image85| |
|                                                                                                                                                                                                                                                                                                                                                                                                                        | |image86| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. Hit "Start" and verify a successful flashing process by viewing the status log.                                                                                                                                                                                                                                                                                                                                     | |image87| |
| //If you receive a message like "No autobaud response", please verify that you are plugged into the "USB/UART" port of your evaluation board, and that you have set your device up for the proper Boot Mode. If not, reconfigure the Boot Mode and reset the power to your board to reboot. //                                                                                                                         |           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                                                                                                                                                                                                                                                                                                                                                                                                                        | |image88| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. Set your boot mode back to the default on your target platform, then reset the power to your board to verify the application firmware starts correctly. On most platforms, boot mode is "1". On SC594 or SC598 EZKIT, plug the USB Micro Type B side to the EZKIT board USB PHY port and the USB Type A side to a USB connection on the PC.                                                                         | |image89| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
|                                                                                                                                                                                                                                                                                                                                                                                                                        | |image90| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Environment Setup and Compilation#.|Advanced Audio Projects#.examples-analog-audio|Application Examples - Analog Audio <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.environment_setup>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot11.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot10.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot12.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0jp1.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot1.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot2.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/prebuiltloc.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot6.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot7.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot9.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot8.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot11.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot10.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot12.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0jp1.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot1.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot2.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/prebuiltloc.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot6.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot7.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot9.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot8.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld1.png
   :width: 600px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld_updated.jpg
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld_updated2.jpg
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld1.png
   :width: 600px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld_updated.jpg
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld_updated2.jpg
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app2.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam7.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app3.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app4.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app5.png
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app6.png
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app7.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app2.png
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sam7.png
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app3.png
   :width: 400px
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app4.png
   :width: 400px
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app5.png
   :width: 400px
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app6.png
   :width: 400px
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/app7.png
   :width: 400px
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch1.png
   :width: 400px
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch2.png
   :width: 400px
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot2.png
   :width: 400px
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0.png
   :width: 400px
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clpd_flash.png
   :width: 600px
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch3.png
   :width: 600px
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch1.png
   :width: 400px
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch2.png
   :width: 400px
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot2.png
   :width: 400px
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/boot0.png
   :width: 400px
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/clpd_flash.png
   :width: 600px
.. |image64| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/bootswitch3.png
   :width: 600px
.. |image65| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_uart_bootswitch.jpg
   :width: 400px
.. |image66| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
.. |image67| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image68| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_uart_usb.jpg
   :width: 400px
.. |image69| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
.. |image70| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step4.png
   :width: 400px
.. |image71| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ccsfp_sam.png
   :width: 400px
.. |image72| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uartflash_sc594.jpg
   :width: 400px
.. |image73| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598.png
   :width: 400px
.. |image74| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ccsfp_sam_flashing.png
   :width: 400px
.. |image75| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_complete.png
   :width: 400px
.. |image76| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_running.jpg
   :width: 400px
.. |image77| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
.. |image78| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_uart_bootswitch.jpg
   :width: 400px
.. |image79| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
.. |image80| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image81| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_uart_usb.jpg
   :width: 400px
.. |image82| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
.. |image83| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/step4.png
   :width: 400px
.. |image84| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ccsfp_sam.png
   :width: 400px
.. |image85| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/uartflash_sc594.jpg
   :width: 400px
.. |image86| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598.png
   :width: 400px
.. |image87| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ccsfp_sam_flashing.png
   :width: 400px
.. |image88| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc598_complete.png
   :width: 400px
.. |image89| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589_running.jpg
   :width: 400px
.. |image90| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/somcrr-ezkit.jpg
   :width: 400px
