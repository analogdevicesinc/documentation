Sharc Audio Module - Ethernet Audio Example using MDNS/DHCP
===========================================================

*This section will take you through a few examples to set up and run ethernet audio using MDNS/DHCP (*\ :doc:`where applicable </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-a>`\ *), including using the shell terminal program to interface with the application.*

Hardware Setup
--------------

**Follow the instructions below to set up your specific hardware variant.**

ADZS-SC589-MINI
~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 1. Power on your SAM board and plug in the 12V Power Supply to the 12V connector. If the board is properly powered, the green LED9/PWR will light up.                     | |image5| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 2. Plug the USB Micro Type B (**labeled USB/OTG on v2.1 HW**) side to the SAM board USB connector and the USB Type A side to a USB connection on the PC.                  | |image6| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 3. **For VBAN->CODEC**                                                                                                                                                    | |image7| |
| Connect the Portable speaker to the *LINE OUT* connector on the SAM (ensure the speaker is turned on!).                                                                   |          |
| **For CODEC->VBAN**                                                                                                                                                       |          |
| Connect the 3.5MM Stereo Audio Cable to the *LINE IN* connector on the SAM.                                                                                               |          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 4. Connect one end of the ethernet cable to the ethernet port on the SAM labelled *J3* and the other end directly into an ethernet port on your PC. (No switch required). | |image8| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| 5. Proceed to the software setup instructions *(common for all hardware variants)*                                                                                        | NA       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

EV-SC594-SOM/EV-SC598-SOM + Carrier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Power on your SOM board by plugging in the 12V Power Supply to the 12V connector on the career board. If the board is properly powered, the green PWR LED on the SOM board will light up.  | |image13| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Plug the USB Micro side to the Carrier board labeled USB PHY and the USB Type A side to a USB connection on the PC.                                                                        | |image14| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. **For VBAN->CODEC**                                                                                                                                                                        | |image15| |
| Connect the Portable speaker ​to the *HEADPHONES* connector on the board (ensure the speaker is turned on!).                                                                                  |           |
| **For CODEC->VBAN**                                                                                                                                                                           |           |
| Connect the 3.5mm stereo audio cable to an audio source with audio jack support (such as a cell phone) and to the AN1/2 connector on the Carrier board.                                       |           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. Connect one end of the ethernet cable to the ethernet port on the SAM labelled *J13* and the other end directly into an ethernet port on your PC. (No switch required).                    | |image16| |
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

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 1. Open TeraTerm and connect to a new Serial Session, connecting to the Port labeled *SC5xx Communications Port*.                                                                                                                                                                                                                     | |image25| |image26| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 2. After connection, navigate to the *Serial Port* settings under *Setup* and change the Port settings to the following:                                                                                                                                                                                                              | |image27| |image28| |
| *Speed/Baud - 115200*                                                                                                                                                                                                                                                                                                                 |                     |
| *Data Bits - 8-bit*                                                                                                                                                                                                                                                                                                                   |                     |
| *Stop Bits - 1*                                                                                                                                                                                                                                                                                                                       |                     |
| *Parity - None*                                                                                                                                                                                                                                                                                                                       |                     |
| *Flow Control - None*                                                                                                                                                                                                                                                                                                                 |                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 3. With a successful connection, after reset, the terminal will display the name of the Audio Starter application with the version. Type *help* to list the available shell commands.                                                                                                                                                 | |image29| |image30| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 4. Using the shell command line, type :doc:`eth </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/network-commands>` to access the hardware's resolved hostname and IP Address. Note this hostname as *<hostname>* and IP Address as *<hardware_ip_addr>* as it will be used later. | |image31|           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| 5. Using your PC's command line, type *ipconfig* to get the resolved IPv4 DHCP address associated with the direct Ethernet connection to your PC. Note this IPv4 address as *<pc_ip_addr>* as it will be used later.                                                                                                                  | |image32|           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

Audio Connection Setup: VBAN->CODEC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass from ethernet input to analog output through your hardware. This setup allows us to play audio via a virtual VBAN soundcard established by Voicemeeter and output to a mini portable speaker.*

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Ensure that a valid ethernet connection can be established between the PC and the board by pinging it. Using the Windows command prompt run:                                                                                                                           | |image41| |
| *ping <hostname>*                                                                                                                                                                                                                                                         |           |
| A valid connection will respond with four replies. Note that the user's VPN and firewall can affect this connection so local traffic may need to be permitted by the firewall and/or VPN may need to be disabled to run this test.                                        |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Open Voicemeeter and after the *hardware out* option has finished initializing, set the PCs playback device to *Voicemeeter Input*                                                                                                                                     | |image42| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Press the VBAN button in the top right corner to configure VBAN ethernet audio.                                                                                                                                                                                        | |image43| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Under *Outgoing Streams* set the following parameters:                                                                                                                                                                                                                 | |image44| |
| *Source = Bus B*                                                                                                                                                                                                                                                          |           |
| *Stream Name = SAM*                                                                                                                                                                                                                                                       |           |
| *IP Address To = <hostname>*                                                                                                                                                                                                                                              |           |
| *SamplerRate = 48000Hz*                                                                                                                                                                                                                                                   |           |
| *Ch = 2*                                                                                                                                                                                                                                                                  |           |
| // Format = PCM 16 Bits//                                                                                                                                                                                                                                                 |           |
| *Net Quality = Optimal*                                                                                                                                                                                                                                                   |           |
| Press the *On* button to enable the source.                                                                                                                                                                                                                               |           |
| *Note that the clock domain mismatch will be much more pronounced when Net Quality = Optimal*                                                                                                                                                                             |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. In the shell terminal, type                                                                                                                                                                                                                                            | |image45| |
| *vban rx on <hardware_ip_addr> 6980 2 16*                                                                                                                                                                                                                                 |           |
| and                                                                                                                                                                                                                                                                       |           |
| *vban rx domain system*                                                                                                                                                                                                                                                   |           |
| This will prime the board to receive VBAN audio on port 6980 at ethernet address <hardware_ip_addr> with 2 channels of audio at 16-bits per channel. Type *vban* again to verify the proper settings.                                                                     |           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                                                    | |image46| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                                           | |image47| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. In the shell terminal, type *route 0 vban 0 codec 0 2 20* to add to route table index 0 the audio routing of vban audio to codec output with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly.                      | |image48| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 8. Finally, on your PC, enable audio through a preferred method, such as Youtube. You should now be able to hear the audio from your PC, through the VBAN virtual audio card, through the hardware and coming out of the speaker connected to *LINE OUT* or *HEADPHONES*. | NA        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

.. important::

   There are no ASRCS currently implemented for a VBAN to DAC clocking domain at this time. As a result, the output may underrun eventually. This is a very basic example just to show ethernet audio. VBAN to VBAN audio should be used to keep clock domains aligned. Clock domain mismatch means that the audio may pop/click/drop samples, etc. ASRCS may be implemented in the future.


Audio Connection Setup: CODEC->VBAN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*This setup will allow audio to pass the codec input (LINE IN) to the ethernet port via the VBAN protocol. This setup allows us to play audio to a virtual VBAN soundcard established by Voicemeeter.*

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Ensure that a valid ethernet connection can be established between the PC and the board by pinging it. Using the Windows command prompt run:                                                                                                    | |image57| |
| *ping <hostname>*                                                                                                                                                                                                                                  |           |
| A valid connection will respond with four replies. Note that the user's VPN and firewall can affect this connection so local traffic may need to be permitted by the firewall and/or VPN may need to be disabled to run this test.                 |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Open Voicemeeter and after the *hardware out* option has finished initializing, set the PCs playback device to *Voicemeeter Input*                                                                                                              | |image58| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Press the VBAN button in the top right corner to configure VBAN ethernet audio.                                                                                                                                                                 | |image59| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Under *Incoming Streams* set the following parameters:                                                                                                                                                                                          | |image60| |
| *Stream Name = SAM*                                                                                                                                                                                                                                |           |
| *IP Address To = <hostname>*                                                                                                                                                                                                                       |           |
| *SamplerRate = 48000Hz*                                                                                                                                                                                                                            |           |
| *Ch = 2*                                                                                                                                                                                                                                           |           |
| *Format = PCM 16 Bits*                                                                                                                                                                                                                             |           |
| *Net Quality = Medium*                                                                                                                                                                                                                             |           |
| *Destination = Virtual Input*                                                                                                                                                                                                                      |           |
| Press the *On* button to enable the stream.                                                                                                                                                                                                        |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. In the shell terminal, type                                                                                                                                                                                                                     | |image61| |
| *vban tx on <pc_ip_addr> 6980 2 16*                                                                                                                                                                                                                |           |
| This will prime the PC to receive VBAN audio on port 6980 at ethernet address <pc_ip_addr> with 2 channels of audio at 16-bits per channel from the input codec. Type *vban* again to verify the proper settings.                                  |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 5. In the shell terminal, type *help route*. The shell will display the usage for the *route* command.                                                                                                                                             | |image62| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 6. In the shell terminal, type *route*. The shell will display the current audio routing table.                                                                                                                                                    | |image63| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 7. In the shell terminal, type *route 0 codec 0 vban 0 2 20* to add to route table index 0 the audio routing of codec audio to vban with 2 channels and an attenuation of 20dB. Type *route* again to ensure that table was updated properly.      | |image64| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 8. Finally, on your PC, Phone, or other analog source, enable audio through a preferred method, such as Youtube. You should now be able to hear the audio from your analog source, input to the codec, and out through the Ethernet port via VBAN. | NA        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

--------------

.. important::

   Having trouble? Check out our list of :doc:`common issues </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-b>`!


--------------

`Application Examples - Ethernet Audio Static IP#.|Advanced Audio Projects#.examples-a2b-audio|Application Examples - A2B Audio <https://wiki.analog.com/_media/navigation Advanced Audio Projects#.examples-ethernet-audio>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet5.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld2.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cld3.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc589analogreal.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethernet5.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_aud.jpg
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethsc594.jpg
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_pwr.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sc594_usb_phy.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/som_aud.jpg
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethsc594.jpg
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example1.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example2.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example4.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example3.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example5.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/example6.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample3.jpg
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/dhcp_ipaddress.jpg
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
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ethexample3.jpg
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/dhcp_ipaddress.jpg
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/pingmdns.jpg
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns.jpg
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns1.jpg
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter4.png
   :width: 600px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/pingmdns.jpg
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 600px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns.jpg
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns1.jpg
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image48| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter4.png
   :width: 600px
.. |image49| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/pingmdns.jpg
   :width: 400px
.. |image50| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image51| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 400px
.. |image52| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns2.jpg
   :width: 400px
.. |image53| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns3.jpg
   :width: 400px
.. |image54| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image55| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image56| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantxroute.png
   :width: 600px
.. |image57| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/pingmdns.jpg
   :width: 400px
.. |image58| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter0.png
   :width: 600px
.. |image59| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/voicemeter1.png
   :width: 400px
.. |image60| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns2.jpg
   :width: 400px
.. |image61| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban_mdns3.jpg
   :width: 400px
.. |image62| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route0.png
   :width: 600px
.. |image63| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route1.png
   :width: 600px
.. |image64| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vbantxroute.png
   :width: 600px
