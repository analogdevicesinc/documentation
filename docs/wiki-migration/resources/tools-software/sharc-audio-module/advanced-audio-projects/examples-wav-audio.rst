Sharc Audio Module - WAV Audio Example
======================================

*This section will take you through a few examples to set up and run audio, including using the shell terminal program to interface with the application and stream audio via a .wav file.*

Hardware Setup
--------------

**Follow the instructions below to set up your specific hardware variant.**

ADZS-SC589-MINI
~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.    | |image4| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 2. Plug the USB Micro Type B (**labeled USB/OTG on v2.1 HW**) side to the SAM board USB connector and the USB Type A side to a USB connection on the PC. | |image5| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 3. Connect a Portable speaker or headphones to the *LINE OUT* connector on the SAM (ensure the speaker is turned on!).                                   | |image6| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 4. Proceed to the software setup instructions *(common for all hardware variants)*                                                                       | NA       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

ADZS-SC584-EZLITE
~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green PWR LED will light up. | |image10| |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro Type B side to the board USB OTG connector and the USB Type A side to a USB connection on the PC.                          | |image11| |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Connect the Portable speaker to the *HEADPHONES* connector on the board (ensure the speaker is turned on!).                                   | |image12| |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Proceed to the software setup instructions *(common for all hardware variants)*                                                               | NA        |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

EV-SC594-SOM/EV-SC598-SOM + Carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SOM board by plugging in the 12V Power Supply to the 12V connector on the career board. If the board is properly powered, the green PWR LED on the SOM board will light up. | |image16| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro side to the Carrier board labeled USB PHY and the USB Type A side to a USB connection on the PC.                                                                       | |image17| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Connect the Portable speaker to the HEADPHONES connector on the Carrier board (ensure the speaker is turned on!).                                                                         | |image18| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                                           | NA        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

Software Setup
--------------

**Follow the instructions below to set up the software.**

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

*This tutorial uses TeraTerm as the serial interface to your hardware.*

**Follow the instructions below to set up a connection to your hardware:**

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port*.                                               | |image25| |image26| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                        | |image27| |image28| |
| *Speed/Baud - 115200*                                                                                                                                           |                     |
| *Data Bits - 8-bit*                                                                                                                                             |                     |
| *Stop Bits - 1*                                                                                                                                                 |                     |
| *Parity - None*                                                                                                                                                 |                     |
| *Flow Control - None*                                                                                                                                           |                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. With a successful connection, after reset, the terminal will display *SAM Audio Starter* with the version. Type *help* to list the available shell commands. | |image29| |image30| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Transferring a WAV File
~~~~~~~~~~~~~~~~~~~~~~~

*This section will instruct the user how to transfer a WAV file to the SHARC Audio platform over XMODEM. The example will use TeraTerm to send the WAV file. On systems with SD Card support, the SD Card filesystem will be the default file system. This example makes use of the default filesystem. If you are not sure which filesystems are available, you can use the* :doc:`drive </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` *command to see which filesystems are available, noting that the SD Card may not be mounted if one is not inserted (where applicable).*

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Ensure the file system on your device is formatted and mounted correctly. To check to see if your file system needs to be formatted, you can use the :doc:`fsck </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` command. If your file system is not formatted properly, you can run :doc:`format </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` in the shell to format all drives, then reset your hardware to mount the filesystem.                     | |image35| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Call *recv <filename.wav>* to prepare the SHARC platform to receive a WAV audio file over an XMODEM connection. See :doc:`recv </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` for more details on usage.                                                                                                                                                                                                                                                                                                                           | |image36| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. In TeraTerm, select **File->Transfer->XMODEM->Send...** and select your .wav file from the PC's filesystem. Ensure the test .wav file uses a sample rate of 48000 Hz.                                                                                                                                                                                                                                                                                                                                                                                                                                         | |image37| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Check that you have transferred the file by checking the result of the *recv* command, and then call *ls* to observe the new file in your storage media.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | |image38| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Audio Connection Setup
~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass from input to output through your hardware by using both an analog input source and an analog output source. This setup allows us to play audio via an Audio Jack from a phone and output to a mini portable speaker.*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                                                                                                                                                                    | |image43| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                                                                                                                                                           | |image44| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. In the shell terminal, type *route 0 wav 0 codec 0 2 20* to add to route table index 0 the audio routing of WAV file to codec output with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly.                                                                                                                                         | |image45| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. In the shell terminal, type *wav src on <filename.wav>* to enable the wav file audio source stream. Note that the number of channels and bits per channel is automatically detected on a WAV source. See the :doc:`wav </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>` shell command for details.                 | |image46| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. You should now be able to hear the audio from the input device coming out of the speaker connected to *LINE OUT* or *HEADPHONES*.                                                                                                                                                                                                                                                      | NA        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Application Examples - USB Audio#.|Advanced Audio Projects#.examples-ethernet-audio|Application Examples - Ethernet Audio Static IP <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.examples-usb-audio>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_usb.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogout.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_usb.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogout.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_analogoutjpg.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_analogoutjpg.jpg
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/format_cmd.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/recv_command.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/xmodem_send.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wav_received.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/format_cmd.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/recv_command.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/xmodem_send.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wav_received.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image41| image:: https://wiki.analog.com/_media/{{/resources/tools-software/sharc-audio-module/advanced-audio-projects/wav_routing.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/enable_wav_src.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image45| image:: https://wiki.analog.com/_media/{{/resources/tools-software/sharc-audio-module/advanced-audio-projects/wav_routing.png
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/enable_wav_src.png
   :width: 400px
