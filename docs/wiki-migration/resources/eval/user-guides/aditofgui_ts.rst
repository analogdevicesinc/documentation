Troubleshooting Guide
=====================

EVAL-ADTF3175D-NXZ
------------------

Known Issues
~~~~~~~~~~~~

-  AB Shift - As the user switches from MP to QMP the AB image shifts alongside the x axis to the right

Troubleshooting
~~~~~~~~~~~~~~~

-  The GUI cannot find the camera

   -  If LEDs on NXP are on :

      -  Do you get a reply if you run "ping 10.42.0.1" command from cmd?

         -  No:

            -  Ensure no apps on pc are connected to the camera
            -  Disconnect from any VPNs
            -  Try different USB-C port
            -  Change USB-C cable
            -  Try connecting a USB-C hub in between camera and PC

         -  Yes:

            -  Ensure that the NXP SD card image is the one downloaded from the GUI installer

               -  :doc:`eval-adsd3100-nxz-software-installation </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`

   -  If LEDs on NXP are off :

      -  Try different USB-C port
      -  Change USB-C Cable
      -  Use HUB with external power

-  Result of a missing *tofi_processor.obj*.

::

       ~/Analog Devices/TOF_Evaluation_ADTF3175D-Rel3.2.0/bin$ ./ADIToFGUI 
       Conn established
       Connection Closed
       Conn established
       Failed to load the compute engine
       Failed to initialize OpenCL config
       Failed to initialize TOFI Processor Config
       Segmentation fault (core dumped)

EVAL-ADSD3100-NXZ or EVAL-ADTF3175-NXZ
--------------------------------------

.. _known-issues-1:

Known Issues
~~~~~~~~~~~~

-  Green light on NXP platform turns on, camera is not detected by GUI

   -  Reconnect the kit to the pc, this can take multiple tries (3-5 times)

-  GUI crashes, last line on log (stored in 'log' folder) says: "successfully requested frame!"

   -  Restart GUI without reconnecting the camera, stream should start

-  Some PCs/Laptops might fail PD negotiation. User can connect to camera, however GUI is fails to get frames

   -  Known laptops that fail

      -  DELL Precision 5540
      -  DELL Precision 5560

   -  Workarounds

      -  Connect USB-C hub between camera and NXP kit
      -  Use NXP Image with PD disabled : LINK

.. _troubleshooting-1:

Troubleshooting
~~~~~~~~~~~~~~~

-  GUI unable to find camera

   -  Log message : 'Failed to write the length of the request string. Error: -2147024463'
   -  Reconnect camera

-  GUI can capture qmp frames only, fps is very slow (<3-5fps)

   -  Change power mode on laptop to 'Best performance'
   -  Connect power supply to laptop
   -  Connect a USB-C Hub with external power supply

-  Camera not showing up on drop down menu

   -  Click 'Refresh Devices' to get updated list
   -  Disconnect the camera and quit GUI
   -  Connect the camera and ensure it shows up on Device Manager as UVC Camera
   -  Start GUI

-  GUI stuck

   -  Typically occurs when mode switching fails. Restart GUI and power cycle camera
   -  Ensure that camera playback is stopped before switching modes

-  GUI Crashes on Play (Windows)

   -  Use :git-ToF:`releases/tag/v3.2.0` or newer
   -  If above step doesn't work, install OpenCL GPU binaries : :doc:`Instructions </wiki-migration/resources/eval/user-guides/eval-adtf3175d-depth-compute-libs>`

      -  Copy the contents from TOF_DepthComputeEngine_Windows-Rel3.0.0\\prebuilt_binary\\ to TOF_Evaluation_ADTF3175D-Rel3.2.0.1\\bin\\ folder

-  Data_collect failed to capture frames

   -  Check if config.json is pointing to correct RawToDepthAdsd3500_xxxxx.INI files.
   -  Check the content of RawToDepthAdsd3500_xxxxx.INI files.

      -  For MP, lr-native, sr-native in respective RawToDepth.INI files

         -  inputFormat should be **"mipiRaw12_8"**
         -  bitsInAB should be **"16"**

   -  Check if the config.json and RawToDepthAdsd3500.ini files are in proper format for respective operating systems. If not convert the file to specific operating system format and re-run the command.

-  Unexpectedly low frame rate:

   -  Source can be:

      -  A USB 2.0 cable - USB 3.0 Type C to Type C is strongly recommended.
      -  A USB port that is being used by other devices
      -  Inappropriate MTU size on the host - An MTU size of 10,000 is recommended.

   -  The tool iPerf3 can be used to measure network bandwdith over USB. iPerf3 can be installed on Linux and Windows. An appropriate bandwidth is above 1Gbps.
   -  On some Linux system it may be necessary to increase the MTU size to 10000.
