Sharc Audio Module - Ethernet Audio Example using Static IP
===========================================================

*This section will take you through a few examples to set up and run ethernet audio, using a static IP address, including using the shell terminal program to interface with the application.*

Hardware Setup
--------------

Switch Setup
~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 1. Connect the 5V input to the 5V barrel connector on the back of the switch. Plug the other side into an available outlet. If the switch is properly powered, the green Power will light up.                                     | |image10| |image11|           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 2. Connect one end of the first ethernet cable to an ethernet port on your PC. Connect the other end to port 5 of the switch. If a network has been identified, the switch will display a green LED above the corresponding port. | |image12|                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 3. Connect one end of the second ethernet cable to port 1 on the ethernet switch.                                                                                                                                                 | |image13|                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 4. Navigate to your PC's Network & Internet Settings. Under Advanced network settings, select *Network and Sharing Center.*                                                                                                       | |image14| |image15| |image16| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 5. Select the Connections under *Unidentified network* to open the properties dialog                                                                                                                                              | |image17|                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+
| 6. Under properties, select *Internet Protocol Version 4 (TCP/IPv4)* and set IP address to use the an IP address in the same domain as the specific hardware in use.                                                              | |image18|                     |
| For example, if the hardware's IP address is *169.254.152.176*, the IPv4 address could be set to *169.254.152.1* assuming it is not in use.                                                                                       |                               |
| This will allow the Ethernet IP address of the Audio Starter project to be on the same domain as the switch.                                                                                                                      |                               |
| Note that once the system is up and running, the IP address and Subnet mask settings can also be retrieved by running the syslog command.                                                                                         |                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------+

**Follow the next set of instructions below to set up your specific hardware variant.**

ADZS-SC589-MINI
~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.    | |image23| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro Type B (**labeled USB/OTG on v2.1 HW**) side to the SAM board USB connector and the USB Type A side to a USB connection on the PC. | |image24| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. **For VBAN->CODEC**                                                                                                                                   | |image25| |
| Connect the Portable speaker to the *LINE OUT* connector on the SAM (ensure the speaker is turned on!).                                                  |           |
| **For CODEC->VBAN**                                                                                                                                      |           |
| Connect the 3.5MM Stereo Audio Cable to the *LINE IN* connector on the SAM.                                                                              |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Connect the other end of the second ethernet cable to the ethernet port on the SAM labelled *J3*                                                      | |image26| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                       | NA        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

ADZS-SC584-EZLITE
~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Power on your board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green PWR LED will light up.                                                | |image32|           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. Plug the USB Micro Type B side to the board USB OTG connector and the USB Type A side to a USB connection on the PC.                                                                         | |image33|           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. **For VBAN->CODEC**                                                                                                                                                                          | |image34| |image35| |
| Connect the Portable speaker ​to the *HEADPHONES* connector on the board (ensure the speaker is turned on!).                                                                                     |                     |
| **For CODEC->VBAN**                                                                                                                                                                              |                     |
| Connect the RCA Left and Right side connector to the INPUT/OUTPUT connector on the hardware and the 3.5mm stereo audio cable to an audio source with audio jack support (such as a cell phone).  |                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. Connect the other end of the second ethernet cable to the ethernet port on the hardware labelled *J4*                                                                                        | |image36|           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                                               | NA                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

EV-SC594-SOM/EV-SC598-SOM + Carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SOM board by plugging in the 12V Power Supply to the 12V connector on the career board. If the board is properly powered, the green PWR LED on the SOM board will light up. | |image41| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro side to the Carrier board labeled USB PHY and the USB Type A side to a USB connection on the PC.                                                                       | |image42| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. **For VBAN->CODEC**                                                                                                                                                                       | |image43| |
| Connect the Portable speaker ​to the *HEADPHONES* connector on the board (ensure the speaker is turned on!).                                                                                  |           |
| **For CODEC->VBAN**                                                                                                                                                                           |           |
| Connect the 3.5mm stereo audio cable to an audio source with audio jack support (such as a cell phone) and to the AN1/2 connector on the Carrier board.                                       |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Connect the other end of the second ethernet cable to the ethernet port on the hardware labelled *J13*                                                                                    | |image44| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                                            | NA        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

Software Setup
--------------

**Follow the instructions below to set up the software.**

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

*This tutorial uses TeraTerm as the serial interface to your hardware.*

**Follow the instructions below to set up a connection to your hardware:**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port*.                                                                         | |image52| |image53| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                                                  | |image54| |image55| |
| *Speed/Baud - 115200*                                                                                                                                                                     |                     |
| *Data Bits - 8-bit*                                                                                                                                                                       |                     |
| *Stop Bits - 1*                                                                                                                                                                           |                     |
| *Parity - None*                                                                                                                                                                           |                     |
| *Flow Control - None*                                                                                                                                                                     |                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. With a successful connection, after reset, the terminal will display the name of the Audio Starter application with the version. Type *help* to list the available shell commands.     | |image56| |image57| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. Using the command line, type *syslog* to access the hardware's specific IP address and Netmask. Note this IP address as *<hardware_ip_addr>* and *<netmask>* as it will be used later. | |image58|           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Audio Connection Setup: VBAN->CODEC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass from ethernet input to analog output through your hardware. This setup allows us to play audio via a virtual VBAN soundcard established by Voicemeeter and output to a mini portable speaker.*

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Ensure that a valid ethernet connection can be established between the PC and the board by pinging it. Using the Windows command prompt run:                                                                                                                           | |image67| |
| *ping <hardware_ip_addr>*                                                                                                                                                                                                                                                 |           |
| A valid connection will respond with four replies. Note that the user's VPN and firewall can affect this connection so local traffic may need to be permitted by the firewall and/or VPN may need to be disabled to run this test.                                        |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Open Voicemeeter and after the *hardware out* option has finished initializing, set the PCs playback device to *Voicemeeter Input*                                                                                                                                     | |image68| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Press the VBAN button in the top right corner to configure VBAN ethernet audio.                                                                                                                                                                                        | |image69| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Under *Outgoing Streams* set the following parameters:                                                                                                                                                                                                                 | |image70| |
| *Source = Bus B*                                                                                                                                                                                                                                                          |           |
| *Stream Name = SAM*                                                                                                                                                                                                                                                       |           |
| *IP Address To = <hardware_ip_addr>*                                                                                                                                                                                                                                      |           |
| *SamplerRate = 48000Hz*                                                                                                                                                                                                                                                   |           |
| *Ch = 2*                                                                                                                                                                                                                                                                  |           |
| // Format = PCM 16 Bits//                                                                                                                                                                                                                                                 |           |
| *Net Quality = Slow*                                                                                                                                                                                                                                                      |           |
| Press the *On* button to enable the source.                                                                                                                                                                                                                               |           |
| *Note that the clock domain mismatch will be much more pronounced when Net Quality = Optimal*                                                                                                                                                                             |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. In the shell terminal, type                                                                                                                                                                                                                                            | |image71| |
| *vban rx on <hardware_ip_addr> 6980 2 16*                                                                                                                                                                                                                                 |           |
| and                                                                                                                                                                                                                                                                       |           |
| *vban rx domain system*                                                                                                                                                                                                                                                   |           |
| This will prime the board to receive VBAN audio on port 6980 at ethernet address <hardware_ip_addr> with 2 channels of audio at 16-bits per channel. Type *vban* again to verify the proper settings.                                                                     |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                                                    | |image72| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                                           | |image73| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. In the shell terminal, type *route 0 vban 0 codec 0 2 20* to add to route table index 0 the audio routing of vban audio to codec output with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly.                      | |image74| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 8. Finally, on your PC, enable audio through a preferred method, such as Youtube. You should now be able to hear the audio from your PC, through the VBAN virtual audio card, through the hardware and coming out of the speaker connected to *LINE OUT* or *HEADPHONES*. | NA        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

.. important::

   There are no ASRCS currently implemented for a VBAN to DAC clocking domain at this time. As a result, the output may underrun eventually. This is a very basic example just to show ethernet audio. VBAN to VBAN audio should be used to keep clock domains aligned. Clock domain mismatch means that the audio may pop/click/drop samples, etc. ASRCS may be implemented in the future.


Audio Connection Setup: CODEC->VBAN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass the codec input (LINE IN) to the ethernet port via the VBAN protocol. This setup allows us to play audio to a virtual VBAN soundcard established by Voicemeeter.*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Ensure that a valid ethernet connection can be established between the PC and the board by pinging it. Using the Windows command prompt run:                                                                                                    | |image83| |
| *ping <hardware_ip_addr>*                                                                                                                                                                                                                          |           |
| A valid connection will respond with four replies. Note that the user's VPN and firewall can affect this connection so local traffic may need to be permitted by the firewall and/or VPN may need to be disabled to run this test.                 |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Open Voicemeeter and after the *hardware out* option has finished initializing, set the PCs playback device to *Speakers (Realtek)*                                                                                                             | |image84| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Press the VBAN button in the top right corner to configure VBAN ethernet audio.                                                                                                                                                                 | |image85| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Under *Incoming Streams* set the following parameters:                                                                                                                                                                                          | |image86| |
| *Stream Name = SAM*                                                                                                                                                                                                                                |           |
| *IP Address To = <hardware_ip_addr>*                                                                                                                                                                                                               |           |
| *SamplerRate = 48000Hz*                                                                                                                                                                                                                            |           |
| *Ch = 2*                                                                                                                                                                                                                                           |           |
| *Format = PCM 16 Bits*                                                                                                                                                                                                                             |           |
| *Net Quality = Fast*                                                                                                                                                                                                                               |           |
| *Destination = In #1*                                                                                                                                                                                                                              |           |
| Press the *On* button to enable the stream.                                                                                                                                                                                                        |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. In the shell terminal, type                                                                                                                                                                                                                     | |image87| |
| *vban tx on <switch_ip_addr> 6980 2 16*                                                                                                                                                                                                            |           |
| This will prime the PC to receive VBAN audio on port 6980 at ethernet address <switch_ip_addr> with 2 channels of audio at 16-bits per channel from the input codec. Type *vban* again to verify the proper settings.                              |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                             | |image88| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                    | |image89| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 8. In the shell terminal, type *route 0 codec 0 vban 0 2 20* to add to route table index 0 the audio routing of codec audio to vban with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly.      | |image90| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 9. Finally, on your PC, Phone, or other analog source, enable audio through a preferred method, such as Youtube. You should now be able to hear the audio from your analog source, input to the codec, and out through the Ethernet port via VBAN. | NA        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Application Examples - Wave Audio#.|Advanced Audio Projects#.examples-ethernet-audio-mdns|Application Examples - Ethernet Audio MDNS <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.examples-wav-audio>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch0.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch1.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch2.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch3.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet0.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet1.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet2.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet3.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample2.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch0.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch1.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch2.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/switch3.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet0.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet1.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet2.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet3.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample2.jpg
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet5.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet5.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_usb.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogout.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogin.png
   :width: 600px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet6.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/alternatepower.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_usb.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogout.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc584_analogin.png
   :width: 600px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet6.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_aud.jpg
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethsc594.jpg
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_aud.jpg
   :width: 400px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethsc594.jpg
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample.jpg
   :width: 400px
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample.jpg
   :width: 400px
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/EthernetPing.JPG
   :width: 600px
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanVoicemeter.JPG
   :width: 800px
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanNew.JPG
   :width: 600px
.. |image64| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image65| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image66| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter4.png
   :width: 600px
.. |image67| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/EthernetPing.JPG
   :width: 600px
.. |image68| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image69| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image70| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanVoicemeter.JPG
   :width: 800px
.. |image71| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanNew.JPG
   :width: 600px
.. |image72| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image73| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image74| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter4.png
   :width: 600px
.. |image75| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/EthernetPing.JPG
   :width: 600px
.. |image76| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanPC.JPG
   :width: 600px
.. |image77| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image78| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/codecvban.png
   :width: 600px
.. |image79| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantx.png
   :width: 600px
.. |image80| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image81| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image82| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantxroute.png
   :width: 600px
.. |image83| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/EthernetPing.JPG
   :width: 600px
.. |image84| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/VbanPC.JPG
   :width: 600px
.. |image85| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image86| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/codecvban.png
   :width: 600px
.. |image87| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantx.png
   :width: 600px
.. |image88| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image89| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image90| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantxroute.png
   :width: 600px
