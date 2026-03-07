Configuring the Framework
=========================

.. image:: https://wiki.analog.com/_media/youtube>W7md5m9Zq_o
   :alt: youtube>W7md5m9Zq_o

The framework options are configured via a single .h file that is shared between the three projects:

``src/common/audio_system_config.h``

This file is broken up into a number of short sections which describe how the framework will operate. Here are some examples of the types of things you can configure:

-  Presence of either the Audio Project or automotive Fin boards
-  The audio block size
-  The audio sample rate
-  Whether or not to use one or both cores for audio processing
-  Which audio framework to utilize
-  Whether or not to use A2B

   -  The role of the SHARC Audio Module board - A2B master or A2B slave
   -  The A2B network topology (if SHARC Audio Module is an A2B master)

-  Whether or not to use the Faust audio engine for synthesis and audio effects (more on this below)

The ``audio_system_config.h`` file includes several checks within the pre-processor logic at the bottom of the file to ensure that the combination of configurations is valid. If an invalid configuration is detected, the compiler will generate a pre-processor error when compiling this file.

.. important::

   Once you have made edits to ``audio_system_config.h``, it is recommended that you do a clean build across all three project folders.


1. Selecting a daughter board (aka "Fin")
-----------------------------------------

If either the Audio Project Fin or the Automotive Fin are connected to the SHARC Audio Module, set the corresponding line below to TRUE. Only one Fin can be attached at a time so if both are set to TRUE, the compiler will generate an error.

.. code:: c


   //*****************************************************************************
   // 1. Select which (if any) daughter boards are connected to the SHARC Audio Module
   //*****************************************************************************

   // Select any connected daughter boards

   // The Automotive audio daughter board is an 8-in / 16-out audio / A2B extender board 
   #define SAM_AUTOMOTIVE_AUDIO_BOARD_PRESENT              FALSE

   #if (SAM_AUTOMOTIVE_AUDIO_BOARD_PRESENT)
     /**
     * The automotive board includes an 1/8" input jack.  The audio from this jack can be
     * routed to channel 0 so you can use the framework as is.
     * Normally, audio from the 1/8" input jack shows up in stereo channel 2 due to the
     * structure of the TDM stream from the automotive board.
      */
     #define AUTOMOTIVE_MAP_JACKS_TO_CH_0_AND_1      TRUE
   #endif

   // The Audio Project Fin board contains 1/4" instrument jacks, MIDI In/Out/Thru, pots, buttons and proto area
   #define SAM_AUDIOPROJ_FIN_BOARD_PRESENT                       TRUE

   #if (SAM_AUDIOPROJ_FIN_BOARD_PRESENT)
       /*
     *  If you're using Audio Project Fin version 3.02, set this to true.  You can find the
     *  Audio Project Fin version right next to the POT associated with HADC2 on the Audio Project Fin.
        */
       #define SAM_AUDIOPROJ_FIN_BOARD_V3_02                     TRUE

   #endif

2. Setting the Audio Processing Parameters
------------------------------------------

The next section of the ``audio_system_config.h`` file deals with the audio processing configuration. ``AUDIO_BLOCK_SIZE`` is the number of audio samples per block of audio. In other words, the framework will buffer this many samples before generating an interrupt and calling the audio processing callback function. The ``AUDIO_BLOCK_SIZE`` is the number of samples per audio channel.

The ``AUDIO_SAMPLE_RATE`` is the desired system sample rate in Hz. The audio sample rate is typically determined by a single external audio component in the system, such as an audio codec or an A2B controller. This value will be used to configure the external audio component which is responsible for providing the master I2S/TDM audio signals. In the case of the SHARC audio module, the ADAU1761 serves as the timing master unless the SHARC audio module is configured to operate as an A2B slave in which case the A2B controller (AD2425W) provides the master I2S/TDM audio signals.

The ``USE_BOTH_CORES_TO_PROCESS_AUDIO`` variable determines if one SHARC core or both SHARC cores will be used to process audio.

If this value is set to FALSE, audio will not be sent to core 2 after it has been processed by core 1. When the framework is configured for single-core processing, the processing flow works as such:

``ADC`` -> ``SHARC Core 1`` -> ``DACs``

If this value is set to TRUE, audio will be sent to core 2 after it has been processed by core 1. When the framework is configure for dual-core processing, SHARC Core 1 still manages the flow of audio data to and from the ADCs and DACs.

``ADC`` -> ``SHARC Core 1 [processing]`` -> ``SHARC Core 2 [processing]`` -> ``SHARC Core 1 [final data transfer]`` -> ``DACs``

.. code:: c


   //*****************************************************************************
   // 2. Set audio processing parameters
   //*****************************************************************************

   // This should be a base 2 number from 8 to 128
   #define AUDIO_BLOCK_SIZE                                (32)

   // Set audio sample rate
   #define AUDIO_SAMPLE_RATE                               (48000)

   // Set to true to use both cores, set to false to just use SHARC Core 1
   #define USE_BOTH_CORES_TO_PROCESS_AUDIO                 TRUE

3. Selecting an Audio Processing Framework
------------------------------------------

The audio frameworks provide platform-specific code for different hardware configurations.

The ``FRAMEWORK_8CH_SINGLE_OR_DUAL_CORE_A2B`` framework provides support for the audio components (audio codec and A2B) on the SHARC Audio Module and the Audio Project Fin.

-  8 channels to/from the ADAU1761 audio codec (while the ADAU1761 contains a stereo codec, the SigmaDSP inside the ADAU1761 can be configured to provide additional audio processing - more information on this can be found in the Enhanced Driver section below)
-  8 channels to/from the AD2425W A2B controller
-  S/PDIF transmit and receive
-  8 channel audio bus between SHARC core 1 and SHARC core 2.

The ``FRAMEWORK_16CH_SINGLE_OR_DUAL_CORE_AUTOMOTIVE`` framework provides support for the audio components on the Automotive Fin which includes 16 DAC channels and 8 ADC channels.

-  16 channels to the DACs (ADAU1966)
-  8 channels from the ADCs (ADAU1977/ADAU1979)
-  16 channel audio bus between SHARC core 1 and SHARC core 2.

The ``FRAMEWORK_BYPASS_SC589_A2B`` framework directly connects the ADAU1761 audio codec to the AD2425W controller and is used to bypass the ADSP-SC589 processor all together. This configuration allows the SHARC Audio Module to behave as a simple CODEC slave node on an A2B bus where the ADAU1761 codec is directly connected to the AD2425W A2B controller. The flexible signal routing unit (SRU) on the ADSP-SC589 makes this possible as it enables us to dynamically route/re-route the I2S/TDM audio signals on the SHARC audio module.

If you'd like to use this framework on your own hardware configurations, you can create your own additional pre-processor variables here and select between the target hardware platform by simply setting one of these values to TRUE.

.. code:: c


   //*****************************************************************************
   // 3. Select an audio processing framework to use (only select one)
   //*****************************************************************************

   // Standard audio processing framework (SHARC Audio Module and SHARC Audio Module + Audio Project board)
   #define FRAMEWORK_8CH_SINGLE_OR_DUAL_CORE_A2B           TRUE

   // Audio processing framework for use with the automotive daughter board
   #define FRAMEWORK_16CH_SINGLE_OR_DUAL_CORE_AUTOMOTIVE   FALSE

   // Bypasses the ADSP-SC589 so I2S signals routed directly between ADAU1761 and A2B controller (GPIO4 = LED on this board)
   #define FRAMEWORK_BYPASS_SC589_A2B                      FALSE

4. Enabling and Configuring A2B Support
---------------------------------------

If you'd like the SHARC Audio Module to participate in an A2B bus, either as a master node or a slave node, set the ``ENABLE_A2B`` variable to ``TRUE``. If the SHARC Audio Module will be the A2B bus master (typical), ensure ``A2B_ROLE_MASTER`` is set to ``TRUE``. If the SHARC Audio Module will act as a slave node, set this variable to ``FALSE``.

If the SHARC Audio Module is the A2B bus master, there are a number of fixed network topologies that can be used. These network topologies are essentially A2B initialization sequences that will initialize the various I2C components on the slave nodes on the A2B bus. Only one A2B topology can be selected at a time.

If you'd like to create your own A2B topologies, see the :doc:`tutorial </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/driver-creation-tutorial>` on this topic.

.. code:: c


   //*****************************************************************************
   // 4. Select whether or not to enable A2B in the framework
   //*****************************************************************************

   #define ENABLE_A2B                                      FALSE

   #if (ENABLE_A2B)

       // If A2B is enabled, select the role that this SHARC Audio Module board will play
       // TRUE = master node, FALSE = slave node
       #define A2B_ROLE_MASTER                             TRUE

       // If this SHARC Audio Module board is a master, select an A2B topology to use for initialization (select only one)
       #if (A2B_ROLE_MASTER)

           // Note that these topologies are created in SigmaStudio and stored within drivers/a2b_simple/a2b_topologies
           // See documentation for a full description of these configurations
           // SET ONLY ONE TO TRUE
           #define A2B_TOPOLOGY_TDM8_SAM_to_SAM_2up_2down                       FALSE
           #define A2B_TOPOLOGY_TDM8_SAM_to_SAM_to_SAM_4up_4down                FALSE
           #define A2B_TOPOLOGY_TDM8_SAM_to_CLASSD_4down                        TRUE

           // Add your own pre-processor variables for custom A2B topologies here



       #endif  // A2B_ROLE_MASTER

   #endif  // ENABLE_A2B

5. Enabling the Enhanced ADAU1761 Driver
----------------------------------------

The ADAU1761 contains a stereo codec but it also contains a SigmaDSP processor, a light weight DSP engine. The ADSP-SC589 connects to the ADAU1761 via an 8 channel I2S/TDM interface. The first two of the eight TDM channels are used to move raw audio between the stereo ADCs and DACs on the ADAU1761. The remaining 6 channels are normally unused. The "enhanced" driver provides additional pre-processing and post-processing on the SigmaDSP core to using the remaining 6 channels.

The functionality implemented in the SigmaDSP is described in the comments below.

.. code:: c


   //*****************************************************************************
   // 5. Use enhanced ADAU1761 driver
   //*****************************************************************************

   #define USE_ENHANCED_ADAU1761_DRIVER                    FALSE

   /**
     * The ADAU1761 is a stereo codec but connects to the ADSP-SC589 via an 8 channel TDM link.
     * Because the ADAU1761 has a DSP core, we can use the remaining channels to provide
     * pre-processing and post-processing using the unused remaining channels.
    *
     * Below is the allocation of TDM channels
     * Output
     *  - First stereo pair : clean to DAC
     *  - Second stereo pair : loudness
     *  - Third stereo pair : "phat" stereo
     *  - Fourth stereo pair : Chorus
    *
     *  The outputs of all four channels are mixed together before sending to the DAC.
    *
     * Input
     *  - First stereo pair : clean from ADC
     *  - Second stereo pair : -6dB limiter
     *  - Third stereo pair : unused (zeros)
     *  - Fourth stereo pair : 440Hz (L) and 880Hz (R) sine waves
    */

6. Faust and MIDI support
-------------------------

Faust is an audio synthesis language that can be used to design audio effects and audio synthesizers. The bare metal framework supports Faust. To enable Faust in the bare metal framework, set the ``FAUST_INSTALLED`` variable to ``TRUE``. More information on Faust can be found in the Faust documentation.

MIDI messages from the UART can be send to either the ARM core or the first SHARC core. This will determine whether the MIDI callback on the ARM core or the SHARC core is called when a new byte arrives. Set either ``MIDI_UART_MANAGED_BY_ARM_CORE`` or ``MIDI_UART_MANAGED_BY_SHARC1_CORE`` depending on which core should handle MIDI notes. The Audio Project Fin contains a standard MIDI interface (5 pin DIN).

.. code:: c

   //*****************************************************************************
   // 6. Faust and MIDI configuration
   //*****************************************************************************

   #define FAUST_INSTALLED                                 FALSE

   #if (FAUST_INSTALLED && SAM_AUDIOPROJ_FIN_BOARD_PRESENT)
       /*
     * Select whether or not to use the Faust algorithm to generate synth sounds
     * and do audio processing.  Presently, a Audio Project Fin is required as the Faust
     * algorithm is configured to generate a synth sound based on MIDI notes.
     * Note: the Faust source code takes a few minutes to compile so you may
     * get a compiler warning that it's taking a long time to compile.  This is normal.
        */
       #define USE_FAUST_ALGORITHM_CORE1               TRUE
       #define USE_FAUST_ALGORITHM_CORE2               FALSE

       #define FAUST_AUDIO_CHANNELS                    2

   #endif

   #if (!FAUST_INSTALLED && SAM_AUDIOPROJ_FIN_BOARD_PRESENT)

     /*
     * If we're not using Faust (which owns MIDI), select which core MIDI events
     * should be handled by.  Only set one to TRUE.  This will enable the
     * MIDI callback function in Callback_MIDI_Message.cpp on that core.
      */

     #define   MIDI_UART_MANAGED_BY_ARM_CORE      FALSE
     #define   MIDI_UART_MANAGED_BY_SHARC1_CORE   TRUE

   #endif

7. Setting the clock frequencies
--------------------------------

The ``audio_system_config.h`` file can also be used to configure the system clocks. For now, the ADSP-SC589 only supports a 450MHz clock speed but this may change in the future.

.. code:: c

   //*****************************************************************************
   // 7. CPU clock speed
   //*****************************************************************************

   #define CORE_CLOCK_FREQ_HZ    (450000000)
   #define EXT_OSCILLATOR_FREQ_HZ  (25000000)

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#baremetal-framework-architecture
   :alt: Framework Architecture#.|Bare Metal Framework#processing-audio|Processing Audio within the Framework
