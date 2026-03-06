Sharc Audio Module - Signal Generator Example (UNRELEASED)
==========================================================

//This section will take you through a few examples to set up and run audio, including using the shell terminal program to interface with the signal generator source. //

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

EV-SC594-SOM/EV-SC598-SOM + Carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SOM board by plugging in the 12V Power Supply to the 12V connector on the career board. If the board is properly powered, the green PWR LED on the SOM board will light up. | |image10| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro side to the Carrier board labeled USB PHY and the USB Type A side to a USB connection on the PC.                                                                       | |image11| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Connect the Portable speaker to the HEADPHONES connector on the Carrier board (ensure the speaker is turned on!).                                                                         | |image12| |
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

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port* or *FTDI COMxx Port*.                                                | |image20| |image21| OR |image22| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                                              | |image23| |image24|              |
| *Speed/Baud - 115200*                                                                                                                                                                 |                                  |
| *Data Bits - 8-bit*                                                                                                                                                                   |                                  |
| *Stop Bits - 1*                                                                                                                                                                       |                                  |
| *Parity - None*                                                                                                                                                                       |                                  |
| *Flow Control - None*                                                                                                                                                                 |                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 3. With a successful connection, after reset, the terminal will display the name of the Audio Starter application with the version. Type *help* to list the available shell commands. | |image25| |image26|              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

Signal Generator
~~~~~~~~~~~~~~~~

// The following steps illustrate how to generate different audio signals and how they can be routed and mixed together. //

+----------------------------------------------------------------------------------------------------------+-----------+
| 1. In the shell terminal, type *help signal*. The shell will display the usage for the *signal* command. | |image31| |
+----------------------------------------------------------------------------------------------------------+-----------+
| 2. In the shell terminal, type *signal*. The shell will display the signal generator table.              | |image32| |
+----------------------------------------------------------------------------------------------------------+-----------+
| 3. Type *signal 0 sine 440* to generate a 440 Hz sine wave with 0.5 amplitude.                           |           |
+----------------------------------------------------------------------------------------------------------+-----------+
| 4. Type *signal 1 white* to generate a white noise signal with 0.5 amplitude.                            |           |
+----------------------------------------------------------------------------------------------------------+-----------+
| 5. Type the following route commands:                                                                    | |image33| |
| - *route 0 signal0 0 codec 0 1 0*                                                                        |           |
| - *route 1 signal1 0 codec 1 1 0*                                                                        |           |
| This will route the sine wave to the left channel and white noise to the right channel.                  |           |
+----------------------------------------------------------------------------------------------------------+-----------+
| 6. Type *route clear* to reset the routing table.                                                        |           |
+----------------------------------------------------------------------------------------------------------+-----------+
| 7. Type the following route commands:                                                                    | |image34| |
| - *route 0 signal0 0 codec 0 1 6*                                                                        |           |
| - *route 1 signal0 0 codec 1 1 6*                                                                        |           |
| - *route 2 signal1 0 codec 0 1 6 mix*                                                                    |           |
| - *route 3 signal1 0 codec 1 1 6 mix*                                                                    |           |
| This will route the mix of both generator to both left and right channels.                               |           |
| **Note:** Signals are attenuated 6 dB's to avoid clipping during mixing.                                 |           |
+----------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Application Examples - A2B Audio#.|Advanced Audio Projects#.shell-commands|Shell Commands <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.examples-a2b-audio>`__

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
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_analogoutjpg.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_analogoutjpg.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/help-signal.jpg
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/signal-status.jpg
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/signal-1.jpg
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/signal-2.jpg
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/help-signal.jpg
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/signal-status.jpg
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/signal-1.jpg
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/signal-2.jpg
   :width: 400px
