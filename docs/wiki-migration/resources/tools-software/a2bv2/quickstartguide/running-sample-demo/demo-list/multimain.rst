:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

Running Sample Demo Multi-main
==============================

PC (Host) + ADSP-21569 SOM + SOM-CRR ez-kit
-------------------------------------------

This demo uses either two ADZS-2435MINI or two ADZS-2433MINI. The following steps are applicable for both the A2B evaluation board pairs.

-  Perform the hardware setup as per :doc:`ADZS2435-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`ADZS2435-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2435WJ3LZ Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`ADZS2433-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` , :doc:`ADZS2433-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2433WB1BZ Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` . Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals
-  Launch SigmaStudio+ x.y.z
-  Click on file -> open project. Browse to C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC and select the file adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj for 2433 transceiver or adi_a2b_ADZS2435MINI_ADSP21569_Multi_Main.ssprj for 2435 transceiver.
-  Follow the procedure given in :doc:`Flashing ADSP-21569 SOM </wiki-migration/resources/tools-software/a2bv2/quickstartguide/adsp-21569_ez-kit>` to flash the file C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\LDR\\SS_App_21569_Multi_Main.ldr onto the SOM board.
-  Turn OFF power to the SOM-CRR board and set boot-mode to 1 on the SOM.
-  Make all the connections described in sections :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` .
-  Connect the USB-Type A cable of USBi device to the PC.
-  Turn ON power to the SOM-CRR and A2B Main nodes.
-  Confirm that LEDs 8 (green) and 9 (amber) are lit on the SOM-CRR. These are just behind the A2B connector (also shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`).
-  Provide audio sinks and sources as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` .
-  On SS+ toolbar, click on the Action -> “Link Compile Download”.
-  The schematic will download and Audio out’s as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>` will be heard.
-  **Note :**

   -  To re-download the schematic, the SOM-CRR must be reset by pushing the reset button.
   -  If the message “Target execution could not be verified” is displayed. Perform a re-download of the schematic by following point ‘a’ above.

-  This demo example has an audio-in at sub-node 1 of main-node 0 chain and an audio-out on sub-node 1 of main-node 1 chain (as per section :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Audio In/out for ADSP-21569 and PC as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2433-with-som-carrier-ez-kit>`). A cross fade can be performed between this audio-in and a 500 Hz sine-tone which is generated on the ADSP-21569.

   -  In the system tab of the schematic, double-click the custom platform and then double-click the ADSP-2156x shape.
   -  A schematic as shown in below Figure will open.
   -  Click once on the “On/Off switch” to put it to “ON” state and observe that the song will fade into a sine tone
   -  Click on the same switch again to get back the audio.
   -  Volume can be adjusted by operating the slider on the right end of the schematic near the outputs
   -  The frequency, gain and on/off state can be changed for each of the two sine tones by interacting with the “Sine Tone” block.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main-dsp.png
   :align: center

.. container:: centeralign

   \ **Figure:** Multi-main DSP schematic


SC594 (Host) + SOM-CRR ez kit
-----------------------------

This demo uses SC594 as a host and it uses two ADZS-2435MINI’s. The following steps shows how to run this sample demo.

-  Perform the hardware setup as per :doc:`ADZS2435-MINI Hardware modifications </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`EVAL-AD2435WJ3LZ ADZS2435-MINI Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` , :doc:`Jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` . Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals.
-  Open CCES v2.11.0 and click on File -> Import -> ‘Existing projects into work space’
-  Browse to the folder C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\multimaster and select a2b-adsp-sc59x
-  Build the project using Project -> Build Project option.
-  Turn OFF power to the SOM-CRR board and set boot-mode to 0 on the SOM.
-  Make all the connections described in section :doc:`connections </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>`.
-  Turn ON power to the SOM-CRR and A2B Main nodes.
-  Connect the JTAG to PC.
   **Note:** If Emulator is used the first time: Create a new debug configuration using Run- >Debug Configurations, create new session, select ADSP-SC594 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP-SC594 via ICE1000) and click NEXT, then click FINISH.
-  Select a debug configuration and press F5 to run the project.
-  There are three audio configurations for this multi-main setup described in above Figures and section :doc:`Audio In/out for ADSP-SC594 as a host – multi-main </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad2435-with-som-carrier-ez-kit>` . Provide the audio sources and sinks as per these.
