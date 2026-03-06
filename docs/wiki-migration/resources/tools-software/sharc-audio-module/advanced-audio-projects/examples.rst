Sharc Audio Module - Analog Audio Example
=========================================

*This section will take you through a few examples to set up and run audio, including using the shell terminal program to interface with the application.*

Serial Terminal Setup
---------------------

*This tutorial uses TeraTerm as the serial interface to the SAM.*

**Follow the instructions below to set up a connection to the SAM:**

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.           | |image9|            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. Plug the USB Micro Type B side to the SAM board USB connector and the USB Type A side to a USB connection on the PC.                                         | |image10|           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port*.                                               | |image11| |image12| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                        | |image13| |image14| |
| *Speed/Baud - 115200*                                                                                                                                           |                     |
| *Data Bits - 8-bit*                                                                                                                                             |                     |
| *Stop Bits - 1*                                                                                                                                                 |                     |
| *Parity - None*                                                                                                                                                 |                     |
| *Flow Control - None*                                                                                                                                           |                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 5. With a successful connection, after reset, the terminal will display *SAM Audio Starter* with the version. Type *help* to list the available shell commands. | |image15| |image16| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Audio Connection Setup
----------------------

*This setup will allow audio to pass from input to output through the SAM by using both an analog input source and an analog output source. This setup allows us to play audio via an Audio Jack from a phone and output to a mini portable speaker.*

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example7.png
   :align: center
   :width: 400px

**Follow the instructions below to set up the audio path:**

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 1. Connect the 3.5mm stereo audio cable to an audio source with audio jack support (such as a cell phone) and to the *LINE IN* connector on the SAM.                                                                     | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 2. Connect the Portable speaker to the *LINE OUT* connector on the SAM (ensure the speaker is turned on!).                                                                                                               | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 3. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                   | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 4. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                          | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 5. In the shell terminal, type *route 0 codec 0 codec 0 2* to add to route table index 0 the audio routing of codec input to codec output with 2 channels. Type *route* again to ensure that table was updated properly. | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+
| 6. Finally, on your analog input device, enable audio. You should now be able to hear the audio from the input device coming out of the speaker connected to *LINE OUT*.                                                 | TODO |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------+

--------------

`Bootloader and Application Flash#.|Advanced Audio Projects#.|Application Examples <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.program-flash>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
