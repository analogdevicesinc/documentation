Sharc Audio Module - A2B Audio Example
======================================

*This section will take you through a few examples to set up and run audio, including using the shell terminal program to interface with the application.*

Overview
--------

The Audio Starter can support a variety of A2B Network configurations via a shell command and an XML file. A *.xml* file describing a network can be exported from :doc:`SigmaStudio / SigmaStudio+ </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`. See :doc:`Exporting XML Files </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/exporting-a2b-xml-files>` for a basic guide to export your XML file. For a full list of supported A2B Shell Commands, see :doc:`A2B Shell Command Support. </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/a2b-commands>`

This example walks you through transferring an A2B network configuration file to your file system, discover the network and play A2B audio in both upstream and downstream configurations. This example uses the :adi:`EVAL-AD2428WB1BZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad2428wb1bz.html#eb-overview>` A2B evaluation board as a subordinate node.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example7.jpg
   :width: 400px

It contains 2 PDM Mics and TDM Audio connected to AUDIO IN/OUT (Analog) on the board. In this example, the network configuration is the following:

-  2 SAM->WBZ Downstream slots
-  4 WBZ->SAM Upstream slots

   -  Slots 0/1 PDM Mics
   -  Slots 2/3 Codec Audio

Hardware Setup
--------------

**Follow the instructions below to set up your specific hardware variant.**

ADZS-SC589-MINI
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.                                                                                                                                                                        | |image5| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 2. Plug the USB Micro Type B (**labeled USB/OTG on v2.1 HW**) side to the SAM board USB connector and the USB Type A side to a USB connection on the PC.                                                                                                                                                                     | |image6| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 3. **FOR UPSTREAM AUDIO**                                                                                                                                                                                                                                                                                                    | |image7| |
| Connect the Portable speaker to the *LINE OUT* connector on the SAM (ensure the speaker is turned on!). Connect the unshielded twisted pair cable from the "B" (labeled SLAVE) port on the SAM board to the "A" (labeled MSTR) port on the WBZ board.                                                                        |          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 4. **FOR DOWNSTREAM AUDIO**                                                                                                                                                                                                                                                                                                  | |image8| |
| Connect the Portable speaker to the *AUDIO OUT* connector on the WBZ (ensure the speaker is turned on!). Connect the 3.5mm stereo cable to the *LINE IN* connector on the SAM. Connect the unshielded twisted pair cable from the "B" (labeled SLAVE) port on the SAM board to the "A" (labeled MSTR) port on the WBZ board. |          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                                                                                                                                                                           | NA       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

EV-SC594-SOM/EV-SC598-SOM + Carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SOM board by plugging in the 12V Power Supply to the 12V connector on the career board. If the board is properly powered, the green PWR LED on the SOM board will light up.                                                                                                                                                                                                                            | |image13| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro side to the Carrier board labeled USB PHY and the USB Type A side to a USB connection on the PC.                                                                                                                                                                                                                                                                                                  | |image14| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. **FOR UPSTREAM AUDIO**                                                                                                                                                                                                                                                                                                                                                                                               | |image15| |
| Connect the Portable speaker to the *HEADPHONES* connector on the Carrier (ensure the speaker is turned on!). Connect the ADZS-2428MINI adapter to the J10 connector on the Carrier board. Connect the unshielded twisted pair cable from the "B" (labeled *P10* port on the ADZS-2428MINI board to "A" (labeled MSTR) port on the WBZ board.                                                                           |           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. **FOR DOWNSTREAM AUDIO**                                                                                                                                                                                                                                                                                                                                                                                             | |image16| |
| Connect the Portable speaker to the *AUDIO OUT* connector on the WBZ (ensure the speaker is turned on!). Connect the 3.5mm stereo cable to the *AIN1/2* connector on the Carrier board. Connect the ADZS-2428MINI adapter to the J10 connector on the Carrier board. Connect the unshielded twisted pair cable from the "B" (labeled *P10* port on the ADZS-2428MINI board to "A" (labeled MSTR) port on the WBZ board. |           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                                                                                                                                                                                                                                                                      | NA        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

Software Setup
--------------

**Follow the instructions below to set up the software.**

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

*This tutorial uses TeraTerm as the serial interface to your hardware.*

**Follow the instructions below to set up a connection to your hardware:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port* or *FTDI COMxx Port*.                                                | |image24| |image25| OR |image26| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                                              | |image27| |image28|              |
| *Speed/Baud - 115200*                                                                                                                                                                 |                                  |
| *Data Bits - 8-bit*                                                                                                                                                                   |                                  |
| *Stop Bits - 1*                                                                                                                                                                       |                                  |
| *Parity - None*                                                                                                                                                                       |                                  |
| *Flow Control - None*                                                                                                                                                                 |                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| 3. With a successful connection, after reset, the terminal will display the name of the Audio Starter application with the version. Type *help* to list the available shell commands. | |image29| |image30|              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

Transferring an A2B Sigma Studio XML File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This section will instruct the user how to transfer an A2B XML SigmaStudio file to the SHARC Audio platform over XMODEM. The example will use TeraTerm to send the XML file.*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. An existing A2B Network XML has been provided as part of the Audio Starter collateral for the SAM with hardware v2.1. It will be located in the following path:                               | |image36| |
| *<project_root>/collateral/a2b/SAM_V2_1_AD2428_WB1BZ/xml*                                                                                                                                        |           |
| or                                                                                                                                                                                               |           |
| *<project_root>/collateral/a2b/AD2428_WB1BZ/xml*                                                                                                                                                 |           |
| With the following name:                                                                                                                                                                         |           |
| *sam-wbz-codec2Dwn2Up-mics2Up.xml*.                                                                                                                                                              |           |
| Take note of this file's location on your PC.                                                                                                                                                    |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Ensure the file system on your device is formatted and mounted correctly. To do this, you can run *format* in the shell to format all drives, then reset the device to mount each filesystem. | |image37| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Call *recv <filename.xml>* to prepare the SHARC platform to receive the A2B XML file over an XMODEM connection.                                                                               | |image38| |
| Note that the A2B XML filename does NOT need to match the name on the PC. In this example, we are naming it *sam-wbz-mics-codec.xml*                                                             |           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. In TeraTerm, select **File->Transfer->XMODEM->Send...** and select your .xml file from the PC's filesystem.                                                                                   | |image39| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Check that you have transferred the file by checking the result of the *recv* command, and then call *ls* to observe the new file in your storage media.                                      | |image40| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Performing A2B Network Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This section will instruct the user how discovery an A2B Network using the XML file that was just transferred to the Audio Starter's file system.*

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Once the XML file has been verified as residing on the file system, use the :doc:`discover </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/a2b-commands>` command to discover the A2B Network. To do this, type:       | |image45|           |
| *discover sam-wbz-mics-codec.xml*                                                                                                                                                                                                                                                                          |                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. A successful discovery will display **SUCCESS** with one node discovered. Additionally, LED3 on the WBZ board will be illuminated.                                                                                                                                                                      | |image46| |image47| |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. A common setup problem for Network discovery is an incorrect A2B link (i.e. plugged into the wrong port on the SAM or on the WBZ board. In this case you might see **WRONG PORT** displayed. When this happens, double check that the hardware setup matches the picture in the Hardware Setup section. | |image48|           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Audio Connection Setup: Upstream Audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass from the configured A2B upstream audio slots (PDM mics and Codec) to output through your Audio Starter hardware analog output source. Ensure your hardware is set up according to the Upstream Audio configuration.*

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                                      | |image56| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                             | |image57| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. In the shell terminal, type *route 0 a2b 0 codec 0 2 20* to add to route table index 0 the audio routing of A2B PDM Mics input to codec output with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly. | |image58| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Gently tap on the two PDM microphones located near the top left corner of the board. You should now be able to hear the audio from the input device coming out of the speaker connected to *LINE OUT*                                                    | |image59| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Now plug in a 3.5mm stereo cable into the *AUDIO IN* connector of the WBZ board and the other side into an analog audio source such as a PC or a phone.                                                                                                  | |image60| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. In the shell terminal, type *route 0 a2b 2 codec 0 2 20* to add to route table index 0 the audio routing of A2B AUDIO IN input to codec output with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly. | |image61| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. Enable the analog audio source connected to the 3.5mm stereo cable. Audio should now be heard from the *LINE OUT* on the SAM board, sourced from *AUDIO IN* on the WBZ board.                                                                            |           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 8. Type *route clear* to clear the routing table for the next exercise.                                                                                                                                                                                     | |image62| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Audio Connection Setup: Downstream Audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

//This setup will allow audio to pass from the *LINE IN* on the SAM to the configured A2B downstream audio slots (Codec). Ensure your hardware is set up according to the Downstream Audio configuration.//

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                                                                        | |image66| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                                                               | |image67| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. In the shell terminal, type *route 0 codec 0 a2b 0 2 20* to add to route table index 0 the audio routing of the codec input on the SAM to the 2 downstream A2B slots (AUDIO OUT) with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly. | |image68| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Enable the analog audio source connected to the 3.5mm stereo cable. Audio should now be heard from the *AUDIO OUT* on the WBZ board, sourced from *LIN IN* on the SAM board.                                                                                                               |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Application Examples - Ethernet Audio MDNS#.|Advanced Audio Projects#.examples-signal-generator|Application Examples - Signal Generator <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.examples-ethernet-audio-mdns>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_setup.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example12.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_setup.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example12.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example15.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example16.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example15.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example16.jpg
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_serial.jpg
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example.jpg
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/format_cmd.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example1.jpg
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/xmodem_send.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example2.jpg
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example.jpg
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/format_cmd.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example1.jpg
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/xmodem_send.png
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example2.jpg
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example3.jpg
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example4.jpg
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example6.jpg
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example5.jpg
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example3.jpg
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example4.jpg
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example6.jpg
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example5.jpg
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example9.jpg
   :width: 400px
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example8.jpg
   :width: 400px
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example10.jpg
   :width: 400px
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example11.jpg
   :width: 400px
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example13.jpg
   :width: 400px
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example9.jpg
   :width: 400px
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example8.jpg
   :width: 400px
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example10.jpg
   :width: 400px
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example11.jpg
   :width: 400px
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example13.jpg
   :width: 400px
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image64| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image65| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example14.jpg
   :width: 400px
.. |image66| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image67| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image68| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b_example14.jpg
   :width: 400px
