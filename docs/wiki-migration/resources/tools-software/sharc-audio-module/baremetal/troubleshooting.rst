Troubleshooting
===============

This section provides some solutions to common problems encountered with the SHARC Audio Module, CCES 2.8.0 and the bare metal framework.

Below are a few steps to make troubleshooting a bit easier:

-  Rev 1.4 and older

   -  To get a better sense of how the framework is working, it is also recommended to connect a ``USB-UART`` device to connector P8 on the SHARC Audio Module via the :doc:`Event Logging </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/event-logging>` output. A 3.3V ``USB-UART`` adapter can be purchased on Amazon for $10-20 such as this one: https://www.amazon.com/Converter-Terminated-Galileo-BeagleBone-Minnowboard/dp/B06ZYPLFNB/ref=sr_1_10?ie=UTF8&qid=1531502798&sr=8-10&keywords=FTDI+3.3V.

-  Rev 1.5 and newer

   -   To get a better sense of how the framework is working, it is also recommended to connect a USB cable to connector P6(USB/UART) on the SHARC Audio Module via the :doc:`Event Logging </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/event-logging>` output.

-  Remove the boot jumper (JP1) and power cycle the SHARC Audio Module. When this jumper is in place, the ADSP-SC589 will boot and run an application from local flash memory. If there was an existing application flashed into memory on the SHARC Audio Module, the ADSP-SC589 will boot this application at power up. Depending on the application, it may create configuration issues when attempting to reinitialize the various hardware components on the board. When this jumper is removed, the SHARC won't boot (it will be waiting for the emulator to connect and download/run code via CCES). All of the hardware components on the SHARC Audio Module will be waiting to be initialized. It's best to keep this jumper removed until you decide to flash your own application (to run at boot without using an emulator).

No audio is coming from the LINE OUT jack on the SHARC Audio Module
-------------------------------------------------------------------

There are generally five sources of issues that can result in no audio coming from the SHARC Audio Module LINE OUT jack when an audio source is connected to the LINE IN jack:

-  The code in the audio callbacks has an error or is reading and writing from the wrong buffers
-  The framework is not configured properly
-  Aspects of the framework are not functioning properly (e.g. SPORT initialization, DMA configuration and management, interrupts)
-  An external audio device hasn't been properly initialized
-  The SRU (Signal Routing Unit) isn't configured to properly route the I2S/TDM signals to the right processor pins and internal SPORTs.

Sources #3-5 may be encountered when modifying the framework itself (beyond the callbacks) such as when porting the framework to a new hardware platform. If you're working within the audio callbacks, these are unlikely the source of the issue. The following steps are designed to help identify the source of the issue.

\**Step 1: Confirm that the cables, audio source device and audio output device are working as expected \*\*

The best place to start is to confirm that the cables connected to the SHARC Audio Module are working, that there is line-level audio coming from your audio source (e.g., smartphone, PC, etc.) connected to the SHARC Audio Module, and that whatever audio output device (e.g., amplifier, headphones, etc.) the SHARC Audio Module is connected to is working as expected. A simple test is to connect the audio source directly to the audio output device to ensure that all of the hardware and cabling connected to the SHARC Audio Module is working as expected.

**Step 2: Confirm that audio is flowing through the unmodified framework**

If the issue still persists, the next step is to ensure that the unmodified Bare Metal Framework is properly passing audio from the input 1/8" jack (LINE IN) to the output 1/8" jack (LINE OUT). The framework is configured to pass audio from LINE IN to LINE OUT by default. Download and run the unmodified Bare Metal Framework on the SHARC Audio Module via CCES. Once all three cores are running, all three LEDs (LED10-LED12) on the SHARC Audio Module should be strobing about once per second (if the LEDs are strobing rapidly, scroll down to the "rapid LED strobing" issue). If one of the three LEDs is not strobing, it means that core is not yet running. Make sure to click "Run->Resume" for each core via the Debug window in the CCES IDE.

If no audio is coming from the SHARC Audio Module but all three LEDs are toggling once per second, it may mean that the SHARC Audio Module is damaged.

\*\* Step 3: Confirm you're accessing the right buffers \*\*

The Bare Metal Framework provides a number of floating point input and output buffers that you can access directly to read audio from various input sources (e,g., S/PDIF In, ADCs on the ADAU1761, A2B, Faust engine, etc.) and send audio to various output sinks (e.g. S/PDIF out, DACs on the ADAU1761, A2B, Faust engine, etc.). However, the framework also provides some aliased buffers to the default audio path.

When in doubt, use AudioChannel_0_Left_In and AudioChannel_0_Right_In as your input buffers and AudioChannel_0_Left_Out and AudioChannel_0_Right_Out as your output buffers. These "aliases" are pointers which point to the right set of input and output buffers on each core to essentially route the stereo ADCs from the ADAU1761 to Core 1, the output of SHARC Core 1 is sent to SHARC Core 2, and the output from core 2 is sent to the stereo DACs on the ADAU1761.

\*\* Step 4: Generate a simple sine wave on Core 1 to confirm that the output path is working \*\*

Try generating a simple sine wave to the output buffers.

In ``Callback_Audio_Processing.cpp`` on SHARC Core 1, change processaudio_callback() as follows which will generate a simple sine tone out of the left and right DAC channels.

.. code:: c

   #pragma optimize_for_speed
   void processaudio_callback( ) {

           static float t = 0;

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // *******************************************************************************
           // Replace the pass-through code below with your custom audio processing code here
           // *******************************************************************************
    
                           float sine_val = 0.5*sinf(t);
                           t += 0.05;
                           if (t > 6.2831853072) t -= 6.2831853072;
                           
               // Generate a sine output
               AudioChannel_0_Left_Out[i]  = sine_val;
               AudioChannel_0_Right_Out[i] = sine_val;
           }
   }

Do a Project->Clean across all three cores followed by a rebuild. Download and run the code and confirm that you're hearing a sine wave in the LINE OUT jack. If you are hearing a sine wave, the good news is that the output audio is making it from the SHARC Core 1 all the DACs.

If there is no audio, the SHARC Audio Module may be damaged.

\*\* Step 5: Try your code on just one core \*\*

If the unmodified framework is passing audio from the LINE IN to the LINE OUT jack, start by configuring the Bare Metal Framework to operating using just one SHARC Core. This can be accomplished by opening ``shared/audio_system_config.h`` and changing ``USE_BOTH_CORES_TO_PROCESS_AUDIO`` to ``FALSE``.

.. code:: c

   //*****************************************************************************
   // 2. Set audio processing parameters
   //*****************************************************************************

   // This should be a base 2 number from 8 to 128
   #define AUDIO_BLOCK_SIZE                                (32)

   // Set audio sample rate
   #define AUDIO_SAMPLE_RATE                               (48000)

   // Set to true to use both cores, set to false to just use SHARC Core 1
   #define USE_BOTH_CORES_TO_PROCESS_AUDIO                 FALSE

Do a Project->Clean across all three cores followed by a rebuild. Download and run the code and confirm that you're hearing a sine wave in the LINE OUT jack.

The audio coming from the SHARC Audio Module is noisy or distorted
------------------------------------------------------------------

The SHARC Audio Module was tested with an Audio Precision and generally has very good noise and distortion characteristics.

If you're hearing background noise (a persistent hiss or buzz), this often due to either a damaged cable or a ground loop. If the characteristics of the noise change when you move the input and output cables connected to the LINE IN and LINE OUT jacks, this is usually indicative of a damaged or pool quality cable. If not, this may be a ground issue. Try plugging the source audio device and audio output device into the same outlet that the SHARC Audio Module is plugged into. You may also try connecting the SHARC Audio Module to a smartphone (LINE IN) which is not charging and headphones (LINE OUT).

If you're hearing periodic noise, it may be due to an issue with your audio processing algorithm. If your algorithm is consuming too many MIPS on one of the SHARC cores, the :doc:`event logging </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/event-logging>` system will report this. If you're not using event logging, you can halt one of the three cores and inspect the multicore memory structure. This has a counter for each SHARC core measuring the number of MIPS overflow events.

On the ARM core, you can monitor the number of dropped audio frames due to overflows like so:

.. code:: c

   if ((multiCoreAudioCtrl->SHARC_Core1_Dropped_Audio_Frames > 0) || 
       (multiCoreAudioCtrl->SHARC_Core2_Dropped_Audio_Frames > 0)
   {
     // Add some code to let you know that one of the SHARC cores has dropped an audio frame
   }

LEDs on the SHARC Audio Module are strobing rapidly (multiple times per second)
-------------------------------------------------------------------------------

When the three LEDs are blinking rapidly (multiple times per second), this means the framework has run into an error. The best way to see the source of the error is to use the event logging system. However, you can also inspect the event log history via the ``Event_Logger_State`` variable on the ARM core. Open up an expressions window in the IDE for the ARM core and add this. You can scroll the various events and determine the one that generated either an ERROR or FATAL level event.

IDE generating error when downloading code to the SHARC Audio Module
--------------------------------------------------------------------

If CCES generates an error when downloading binaries to the SHARC Audio Module, try power cycling the SHARC Audio Module with the boot jumper removed and power cycling the emulator.

Audio Bleeding Through From Main Board to Audio Project Fin
-----------------------------------------------------------

In revisions 1.4 and older of the SHARC Audio Module, users may notice audio bleeding through to the Audio Project Fin. In order to fix this issue resistors R44 and R45 should be removed.

Generally unexpected behavior
-----------------------------

**Different build profiles across each core** : Each project has a build profile (typically "Debug" or "Release"). It's possible to have one of the three projects set to one profile and the other two projects set to the other. For example, the ARM and SHARC Core 1 can be set for Debug while SHARC Core 2 is set to Release. In this case, the binary files generated by the linker will go into the respective /Debug and /Release folders within each project. The emulator "Debug Configuration" in the IDE is typically configured to use files from either the /Debug directories on each core or the /Release directories (but not a mix of the two). So when SHARC Core 2 is set to "Release" build and the emulator configuration is loading the binary files from the /Debug directories, the changes made with each compile on SHARC Core 2 aren't being downloaded. The IDE is loading an older binary from the /Debug directory for SHARC Core 2. Thus it's important to ensure all three projects are set to the same build profile AND to ensure the emulator "Debug Configuration" is also pulling from those same folders.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#flashing
   :alt: Programming BM Framework to Flash#.|Bare Metal Framework#using-both-cores|Audio Processing Basics
