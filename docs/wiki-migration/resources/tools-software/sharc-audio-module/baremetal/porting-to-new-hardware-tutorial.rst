Porting the Bare Metal Framework to a New Hardware Platform
===========================================================

This tutorial covers how to port the Bare Metal Framework to a custom hardware platform. The Bare Metal Framework is designed to be portable. As discussed in the :doc:`Selecting Between Different Hardware Platforms </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/audio-frameworks>` section, all of the hardware platform specific code resides in a .c/.h file pair on each core.

-  Create new audio framework files (.c/.h file pair for each core) and add the framework to audio_system_config.h

   -  On the pair of files for the ARM core

      -  Add any external ADC, DAC, CODEC initialization code

         -  Configure any GPIO

            -  Configure the Signal Routing Unit (SRU) to connect the external components to the

      -  On the first SHARC core, configure the DMA(s)

Step 1: Creating new framework files for your hardware platform
---------------------------------------------------------------

It's likely going to be easiest to clone one of the existing frameworks and use this as a starting point.

Presently, there are two audio frameworks that ship with the Bare Metal Framework. The first is called ``audio_frameworks/audio_framework_8ch_sam_and_audioproj_fin`` and this provides support for the hardware components on the SHARC Audio Module. The second is called ``audio_frameworks/audio_framework_16ch_sam_and_automotive_fin`` and this provides support for audio components on the 16-channel automotive Fin (but provide support for the audio components on the SHARC Audio Module).

One notable distinction between the two is the number of general purpose audio channels that are available to pass audio data between the L1 memory of the two SHARC cores. With ``audio_framework_8ch_sam_and_audioproj_fin``, 8 channels of audio are available for moving audio between SHARC Core 1 and SHARC Core 2. With ``audio_framework_16ch_sam_and_automotive_fin``, 16 channels of audio are available for moving audio between SHARC Core 1 and SHARC Core 2. Audio data is moved between cores via background DMA so there isn't more processing overhead when using 16 channels. However, we do need to allocate L1 memory for these channels on each core.

We'll start by cloning one of these two file pairs on each core and providing our new files with a unique name. Let's call it "Hardware Platform One". In total, we'll create 6 new files (2 for each core) and each will be a copy of the corresponding ``audio_framework_8ch_sam_and_audioproj_fin`` .c or .h file on each core.

In the ARM core project (sam_baremetal_framework_core0 in CCES): ``audio_frameworks/audio_framework_hardware_platform_one_arm.c`` ``audio_frameworks/audio_framework_hardware_platform_one_arm.h``

In the SHARC core 1 project (sam_baremetal_framework_core1 in CCES): ``audio_frameworks/audio_framework_hardware_platform_one_core1.c`` ``audio_frameworks/audio_framework_hardware_platform_one_core1.h``

In the SHARC core 2 project (sam_baremetal_framework_core2 in CCES): ``audio_frameworks/audio_framework_hardware_platform_one_core2.c`` ``audio_frameworks/audio_framework_hardware_platform_one_core2.h``

Step 2: Create a new preprocessor variable for the new audio framework
----------------------------------------------------------------------

One nice feature of the Bare Metal framework is we can switch between hardware platforms by changing a single field in the audio_system_config.h file. This is managed with preprocessor variables that are used to selectively include the audio framework files associated with each platform.

The first thing we'll do is create a new definition in ``audio_system_config.h`` for our framework as shown below. Ensure that only one audio framework is set to TRUE.

.. code:: c

   //*****************************************************************************
   // 3. Select an audio processing framework to use (only select one)
   //*****************************************************************************

   // Standard audio processing framework (SHARC Audio Module and SHARC Audio Module + DIY board)
   #define FRAMEWORK_8CH_SINGLE_OR_DUAL_CORE_A2B           FALSE

   // Audio processing framework for use with the automotive daughter board
   #define FRAMEWORK_16CH_SINGLE_OR_DUAL_CORE_AUTOMOTIVE   FALSE

   // Bypasses the ADSP-SC589 so I2S signals routed directly between ADAU1761 and A2B controller (GPIO4 = LED on this board)
   #define FRAMEWORK_BYPASS_SC589_A2B                      FALSE

   // Our first custom hardware platform
   #define FRAMEWORK_HARDWARE_PLATFORM_ONE                 TRUE

Next, we'll then add this same new preprocessor definition / variable to a file called ``src/audio_framework_selector.h`` on core 0/ARM core, ``src/audio_framework_selector.h`` on core 1/SHARC core 1, ``audio_framework_selector.h`` on core 2/SHARC core 2.

.. code:: c

   #ifndef _AUDIO_FRAMEWORK_ARM_H_
   #define _AUDIO_FRAMEWORK_ARM_H_

   // Set audio system parameters in this file
   #include "common/audio_system_config.h"

   #if defined(FRAMEWORK_8CH_SINGLE_OR_DUAL_CORE_A2B) && FRAMEWORK_8CH_SINGLE_OR_DUAL_CORE_A2B
   #include "audio_frameworks/audio_framework_8ch_sam_and_audioproj_fin_arm.h"

   #elif defined(FRAMEWORK_16CH_SINGLE_OR_DUAL_CORE_AUTOMOTIVE) && FRAMEWORK_16CH_SINGLE_OR_DUAL_CORE_AUTOMOTIVE
   #include "audio_frameworks/audio_framework_16ch_sam_and_automotive_fin_arm.h"

   #elif defined(FRAMEWORK_BYPASS_SC589_A2B) && FRAMEWORK_BYPASS_SC589_A2B
   #include "audio_frameworks/audio_framework_a2b_bypass_sc589_arm.h"

   // Support for our first custom hardware platform
   #elif defined(FRAMEWORK_HARDWARE_PLATFORM_ONE) && FRAMEWORK_HARDWARE_PLATFORM_ONE
   #include "audio_frameworks/audio_framework_hardware_platform_one_arm.h"

   #endif // Audio frameworks

   #endif // _AUDIO_FRAMEWORK_ARM_H_

Make the same modification to the audio_framework\_ file on each core and be sure to point to the new local .h file you cloned in the step prior.

At the top of your cloned audio framework .c files on each core, add the same pre-processor variable to the top of the file. This will ensure only the audio framework files we have selected in audio_system_config.h is compiled.

.. code:: c

   // Define your audio system parameters in this file
   #include "common/audio_system_config.h"

   #if defined(FRAMEWORK_HARDWARE_PLATFORM_ONE) && FRAMEWORK_HARDWARE_PLATFORM_ONE

   #include "audio_framework_hardware_platform_one_arm.h"

Finally, at the very bottom of your cloned audio framework .c files on each core, you'll find an integer declaration. This is here only to prevent compiler warnings when the current framework is not selected but this file is compiled. Change this to a unique name at the end of each of these files so we don't end up with a linker error like so:

.. code:: c

   int audio_framework_hardware_platform_one = 1;

In summary, add a new preprocessor variable to audio_system_config.h for your new audio framework. Add this variable to ``audio_framework_hardware_platform_one_arm.h``, ``audio_framework_hardware_platform_one_core1.h`` and ``audio_framework_hardware_platform_one_core2.h``. And finally, add this variable to the top of our three new, cloned .c files for our new audio framework (one on each core).

To confirm that everything is configured properly, do a clean build and ensure everything compiles and links properly. At this point, we've just selected a cloned version of the 8 channel SHARC Audio Module framework.

Step 3: On the ARM Core, Configure System Initialization Code
-------------------------------------------------------------

Open up ``audio_frameworks/audio_framework_hardware_platform_one_arm.c`` on the ARM core and locate the function, ``audioframework_initialize()``. This function is called by ``src/startup_core_core0.c`` and is initializes the following components in our system:

-  The Signal Routing Unit (SRU) which routes I2S/TDM audio signals from the pins of the processor to the SPORTs (synchronous serial ports used for audio) and other audio peripherals such as the Sample Rate Converters (SRUs).
-  GPIO pin configuruation
-  External ADC, DAC, CODEC initialization via I2C or SPI

The first thing we'll do is configure the Signal Routing Unit (SRU).

The **Signal Routing Unit (SRU)** is a very powerful and useful peripheral. This tutorial won't go into great depth about how to use this peripheral but in short, it allows us to dynamically "wire" signals to/from the pins of the ADSP-SC589 and/or to/from various internal peripherals.

The file ``drivers/sru_simple/sru_simple.c`` contains a number of configurations that you can use as a starting point. You can either create a new function in this driver or add the SRU config code directly to ``audioframework_initialize()``.

There are two existing SRU configuration calls in ``audioframework_initialize()`` that you can remove and replace with your own configuration code. You can use the contents of these functions as a rough template as you're wiring up the peripherals in your system.

.. code:: c

       // Configure the DAI / SRU to use the ADAU1761 as an I2S clock/FS master to SPORT 0 and A2B to SPORT 1
       sru_config_sharc_sam_a2b_master();

       // Configure SPDIF to connect to SPORT2.  Divide the fs.
       sru_config_spdif(4);

The next thing we'll do is configure our GPIO pins. There is a function called ``gpio_initialize()`` that contains the initialization routines for the GPIO pins. These routines use the bare metal gpio driver located at ``drivers/bm_gpio_driver/bm _gpio.h`` which makes it easy to configure various GPIO pins as inputs and outputs and optionally attach interrupt callbacks to the input pins.

Finally, we'll add any initialization code for our external components such as ADCs, DACs and CODECs. The existing ``audio_framework_hardware_platform_one_arm.c`` file will have the initialization code for the ADAU1761 which we can replace. You can either perform I2C or SPI reads and writes to your external components here directly (using twi_simple and spi_simple drivers). If you're using an Analog Devices audio ADC, DAC or CODEC, you may be able to use SigmaStudio to generate the initialization code for you. See :doc:`Tutorial: Creating Drivers for Audio Components </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/driver-creation-tutorial>` for more information on how to use SigmaStudio to generate initialization code.

Below is an example of what a new version of the audioframework_initialize() could look like. In this example, we have a fictional audio codec that we can configure over I2C/TWI with an I2C address of 0x40. The I2S/TDM signals from this component connect to the DAI0 pins 1-4 on the ADSP-SC589. Note the additional include files at the top of this snippet which need to be added too.

.. code:: c


   // Add some additional headers so we can access SRU and TWI
   #include "drivers/bm_twi_driver/bm_twi.h"
   #include <srusc589.h>

   /**
     * @brief      ARM audio framework initialization function
    *
     * This function initializes any external components, selects the right
     * SRU / DAI configuration, and sets the sample rate.
    *
    */
   void audioframework_initialize() {

       /**
     * Set system-wide audio parameters in our shared memory structure between cores.
     * While sample rate is set initially via pre-processor variables, there may be
     * situations where they are modified on the fly.
        */

       multiCoreAudioCtrl->audio_sample_rate = AUDIO_SAMPLE_RATE;
       multiCoreAudioCtrl->audio_block_size = AUDIO_BLOCK_SIZE;
       multiCoreAudioCtrl->core_clock_frequency = CORE_CLOCK_FREQ_HZ;

       // Initialize GPIO
       gpio_initialize();

       // Set to false while we initialize the external audio components in our system
       multiCoreAudioCtrl->ARM_Audio_Peripheral_Initialization_Complete = false;

       // Initialize state variables and pointers for the audio framework
       multiCoreAudioCtrl->SHARC_Core1_Ready_For_Audio = false;
       multiCoreAudioCtrl->SHARC_Core2_Ready_For_Audio = false;

       // Configure the SRU to route I2S/TDM signals from DAI0 pins 1-4 to SPORT0
       SRU(HIGH, DAI0_PBEN01_I);       // DAC data is an output
       SRU(LOW,  DAI0_PBEN02_I);       // ADC data is an input
       SRU(LOW,  DAI0_PBEN03_I);       // CLK is an input
       SRU(LOW,  DAI0_PBEN04_I);       // FS is an input

       SRU(DAI0_PB03_O, SPT0_ACLK_I);  // route BCLK output to SPORT0A clock input
       SRU(DAI0_PB03_O, SPT0_BCLK_I);  // route also to SPORT0B clock input

       SRU(DAI0_PB04_O, SPT0_AFS_I);   // route FS output to SPORT0A frame sync
       SRU(DAI0_PB04_O, SPT0_BFS_I);   // route FS output to SPORT0B frame sync

       SRU(DAI0_PB02_O, SPT0_BD0_I);   // route ADC pin to SPT0 BD0 input
       SRU(SPT0_AD0_O,  DAI0_PB01_I);  // route SPT0A AD0 output to DAC pin

       // Initialize some I2C audio codec at I2C address 0x40 connected to TWI0 pins
       BM_TWI    codec_twi;

       if (twi_initialize( &codec_twi, 0x40, TWI_TYPICAL_SCLK0_FREQ, TWI0) !=  TWI_SIMPLE_SUCCESS) {
           // handle I2C init error here
           return;
       }

       // Write a value of 0x80 to codec to start it
       twi_write( &codec_twi, 0x80)

       // The ARM is all ready to go!
       multicore_data->arm_audio_peripheral_initialization_complete = true;

   }

Step 4: On the SHARC Core 1, Configure the Audio DMA
----------------------------------------------------

SHARC Core 1 is primarily responsible for routing audio between the two SHARC cores and the SPORTs which connect to various audio devices and peripherals.

The current framework which we cloned is design to route audio to and from three different sources/sinks: the ADAU1761 (8 channels), the A2B bus (8 channels) and S/PDIF (2 channels).

For the sake of example, let's say that our new audio hardware platform has a single 8 channel codec and this is the only audio component that we'll communicate with in our new hardware platform.

The first thing we'll do is update the various memory buffers. There are two types of memory buffers that the framework uses. The first are fixed point buffers which contain the raw, fixed point audio data that is coming from, going to the various audio components in our system. The second are floating point buffers which contain the audio data that we'll be processing within the callbacks. SHARC core 1 handles the movement of data and floating-point<->fixed-point conversion between these two types of buffers.

At the top of ``audio_frameworks/audio_framework_hardware_platform_one_core1.c`` are the fixed point buffers declarations used for DMA. There are two buffers for each direction as the DMA is capable of automatically ping-ponging between buffers. When we're processing one set of buffers, the DMA engine is transmitting/receiving the other set. As you can see below, we have one pair of buffers for transmit and one pair for receive. Data from each audio channel be stacked in each buffer is the (total number of channels from that device) x (system wide audio block size). The DMA engine takes care of de-interleaving the data so each channel of audio is grouped together / stacked. The ``section()`` directive places these buffers in L1 memory to ensure highest computational performance.

.. code:: c


   // Fixed-point (raw ADC/DAC data) DMA buffers for ping-pong / double-buffered DMA
   int section("seg_dmda_nw") sport0_dma_rx_0_buffer[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};
   int section("seg_dmda_nw") sport0_dma_rx_1_buffer[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};
   int section("seg_dmda_nw") sport0_dma_tx_0_buffer[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};
   int section("seg_dmda_nw") sport0_dma_tx_1_buffer[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};

Below the fixed-point DMA buffer declarations, we see the floating-point buffer declarations. We'll reduce this to a single input and output buffer for our CODEC. Having all of our 8 audio channels packed into one long contiguous buffer allows us more efficiently perform the fixed/floating point conversion.

Below our input and output buffers for our codec, we'll also preserve the second set of buffers which is used to move 8 channels of audio data to the second SHARC core if we're using both cores to process audio.

.. code:: c


   // Floating-point buffers that we will process / operate on
   // These are aligned to 32-byte boundaries so we can use fast DMAs to move them around
   #pragma align 32
   float codec_audiochannels_out[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};    // Audio to DACs
   #pragma align 32
   float codec_audiochannels_in[AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE] = {0};     // Audio from ADCs

   #if (USE_BOTH_CORES_TO_PROCESS_AUDIO)
   #pragma align 32
   float audiochannels_from_sharc_core2[AUDIO_CHANNELS * AUDIO_BLOCK_SIZE] = {0};      // Audio from SHARC Core 2
   #pragma align 32
   float audiochannels_to_sharc_core2[AUDIO_CHANNELS * AUDIO_BLOCK_SIZE] = {0};        // Audio from SHARC Core 2
   #endif

Now we'll create points into our input and output buffers that will allow us to access each audio channel from our audio callbacks. We'll also preserve the code we're using to set up the audio buffers going to and from SHARC core 2.

.. code:: c


   // 8 input channels from the codec
   float * audiochannel_codec_0_left_In  = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_codec_0_right_In = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_codec_1_left_In  = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_codec_1_right_In = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_codec_2_left_In  = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_codec_2_right_In = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_codec_3_left_In  = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_codec_3_right_In = codec_audiochannels_In + AUDIO_BLOCK_SIZE\*7;

   // 8 output channels to the codec
   float * audiochannel_codec_0_left_Out  = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_codec_0_right_Out = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_codec_1_left_Out  = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_codec_1_right_Out = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_codec_2_left_Out  = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_codec_2_right_Out = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_codec_3_left_Out  = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_codec_3_right_Out = codec_audiochannels_Out + AUDIO_BLOCK_SIZE\*7;

   #if (USE_BOTH_CORES_TO_PROCESS_AUDIO)

   // Processed audio data from SHARC Core
   float * audiochannel_from_sharc_core2_0_left  = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_from_sharc_core2_0_right = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_from_sharc_core2_1_left  = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_from_sharc_core2_1_right = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_from_sharc_core2_2_left  = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_from_sharc_core2_2_right = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_from_sharc_core2_3_left  = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_from_sharc_core2_3_right = audiochannels_from_sharc_core2 + AUDIO_BLOCK_SIZE\*7;

   float * audiochannel_to_sharc_core2_0_left  = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_to_sharc_core2_0_right = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_to_sharc_core2_1_left  = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_to_sharc_core2_1_right = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_to_sharc_core2_2_left  = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_to_sharc_core2_2_right = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_to_sharc_core2_3_left  = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_to_sharc_core2_3_right = audiochannels_to_sharc_core2 + AUDIO_BLOCK_SIZE\*7;

   #endif

Next, we'll update our buffer aliases. This allows us to always read and write from a standard set of buffer names in our audio callback regardless of whether we're using one core or both cores. In our callback, when write to the ``AudioChannel_0_Left_Out[]`` buffer, we're either writing to the buffer heading to core 2 when we're using both cores or we're writing to the buffer that will be transmitted to our codec when using just one core. This way, we can flip between single core processing and dual core processing (via ``audio_system_config.h``) without having to re-write any of our audio processing code in the audio processing callback.

::


   // Define alias pointers for inputs
   float * audiochannel_0_left_in  = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_0_right_in = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_1_left_in  = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_1_right_in = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_2_left_in  = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_2_right_in = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_3_left_in  = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_3_right_in = codec_audiochannels_in + AUDIO_BLOCK_SIZE\*7;

   #if (USE_BOTH_CORES_TO_PROCESS_AUDIO)

   // If we're in dual core, point our alias to the buffers heading to SHARC 2.
   float * audiochannel_0_left_out  = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_0_right_out = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_1_left_out  = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_1_right_out = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_2_left_out  = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_2_right_out = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_3_left_out  = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_3_right_out = audiochannels_To_sharc_core2 + AUDIO_BLOCK_SIZE\*7;

   #else
   // Otherwise, point our alias buffers back out to the codec
   float * audiochannel_0_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*0;
   float * audiochannel_0_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*1;
   float * audiochannel_1_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*2;
   float * audiochannel_1_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*3;
   float * audiochannel_2_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*4;
   float * audiochannel_2_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*5;
   float * audiochannel_3_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*6;
   float * audiochannel_3_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*7;
   #endif

   // Declare buffers to write directly to codec output
   float * codec_0_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*0;
   float * codec_0_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*1;
   float * codec_1_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*2;
   float * codec_1_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*3;
   float * codec_2_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*4;
   float * codec_2_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*5;
   float * codec_3_left_out  = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*6;
   float * codec_3_right_out = codec_audiochannels_out + AUDIO_BLOCK_SIZE\*7;

Update ``audio_frameworks/audio_framework_hardware_platform_one_core1.h`` to ensure these variables you've created are present in the header file too.

At this point, our various memory buffers and pointers are all ready.

Next, we need to configure the DMA and our serial ports (SPORTs). The ``drivers/bm_audio_flow_driver/`` driver has a utility function for configuring both the DMA and the SPORT for each of our audio devices. Since the existing framework has three different audio sources/sinks, you'll find three such struct definitions in ``audio_frameworks/audio_framework_hardware_platform_one_core1.c``. We can remove all but the definition for SPORT0.

The C struct definition is shown below. Here we provide information about the number of channels and audio block size, the audio buffers that the DMA engine will read from/write to, the SPORT configuration, and whether or not we want this DMA to generate an interrupt each time it transfers an audio frame (channels x block size). The code below shows an example of the DMA configuration for our 8 channel audio codec.

.. code:: c

   // DMA & SPORT Configuration for SPORT 0 (CODEC connection)
   SPORT_DMA_CONFIG   SPR0_CODEC_8CH_Config = {

       .sport_number         = SPORT0,

       .dma_audio_channels   = AUDIO_CHANNELS,
       .dma_audio_block_size = AUDIO_BLOCK_SIZE,

       .dma_tx_buffer_0    = sport0_dma_tx_0_buffer,
       .dma_tx_buffer_1    = sport0_dma_tx_1_buffer,
       .dma_rx_buffer_0    = sport0_dma_rx_0_buffer,
       .dma_rx_buffer_1    = sport0_dma_rx_1_buffer,

       // SPORT Transmit
       .pREG_SPORT_CTL_A   = (0x1 << BITP_SPORT_CTL_A_DTYPE) |     // Right justify, sign extend
                             (0x1F << BITP_SPORT_CTL_A_SLEN) |     // 32-bit transfers
                             BITM_SPORT_CTL_A_CKRE  |              // Sample on rising edge
                             BITM_SPORT_CTL_A_FSR |                // Frame sync required
                             BITM_SPORT_CTL_A_DIFS |               // Data independent FS
                             BITM_SPORT_CTL_A_LFS |                // Active low FS / LR CLK
                             BITM_SPORT_CTL_A_SPTRAN |             // SPORT is transmitter
                             0,

       .pREG_SPORT_MCTL_A  = BITM_SPORT_MCTL_A_MCE |               // Multi-channel enable
                             (0x1 << BITP_SPORT_MCTL_A_MFD) |      // Frame delay = 1
                             ((8-1) << BITP_SPORT_MCTL_A_WSIZE) |  // 8 words / frame
                             0,

       .pREG_SPORT_CS0_A   = AUDIO_CHANNELS_MASK,   // 8 channels

       // SPORT Receive
       .pREG_SPORT_CTL_B   = (0x1 << BITP_SPORT_CTL_B_DTYPE) |     // Right justify, sign extend
                             (0x1F << BITP_SPORT_CTL_B_SLEN) |     // 32-bit transfers
                             BITM_SPORT_CTL_A_CKRE  |              // Sample on rising edge
                             BITM_SPORT_CTL_B_FSR |                // Frame sync required
                             BITM_SPORT_CTL_B_DIFS |               // Data independent FS
                             BITM_SPORT_CTL_B_LFS |                // Active low FS / LR CLK
                             0,

       .pREG_SPORT_MCTL_B  = BITM_SPORT_MCTL_B_MCE |               // Multi-channel enable
                             (0x1 << BITP_SPORT_MCTL_B_MFD) |      // Frame delay = 1
                             ((8-1) << BITP_SPORT_MCTL_B_WSIZE) |  // 8 words / frame
                             0,

       .pREG_SPORT_CS0_B   = AUDIO_CHANNELS_MASK,   // 8 channels

       .generates_interrupts = true,
       .dma_interrupt_routine = audioframework_dma_handler

   };

The interrupt handler can be mostly left as is. There are only two small changes:

1) Remove the fixed-float processing for the second and third set of audio buffers in the original framework.

.. code:: c


       if( (uint32_t) sport_dma_cfg->DMA_Descriptor_RX_0_LIST.Next_Desc !=
            (*sport_dma_cfg->pREG_DMA_RX_DSCPTR_NXT)
         )
       {
           audioflow_float_to_fixed(codec_audiochannels_out, sport0_dma_tx_0_buffer, AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE);
           audioflow_fixed_to_float(sport0_dma_rx_0_buffer, codec_audiochannels_in,  AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE);
       }
       else
       {
           audioflow_float_to_fixed(codec_audiochannels_out, sport0_dma_tx_1_buffer, AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE);
           audioflow_fixed_to_float(sport0_dma_rx_1_buffer, codec_audiochannels_in,  AUDIO_CHANNELS\*AUDIO_BLOCK_SIZE);
       }

2) Update the code to zero output buffers in the case of a MIPS overflow

.. code:: c

       // Detect and handle the "frame dropped" event
       if (!last_audio_frame_completed) {

           // Make a call to the callback
           processaudio_mips_overflow();

           // Zero output buffers so we get silence instead of repeated audio
           for (i = 0; i < AUDIO_CHANNELS * AUDIO_BLOCK_SIZE; i++) {
           #if (USE_BOTH_CORES_TO_PROCESS_AUDIO)
                   audiochannels_to_sharc_core2[i] = 0;
               #endif
               codec_audiochannels_out[i] = 0;   // <-- Update this line with the codec buffer
           }

           // Update dropped audio frame counter
           multicore_data->sharc_core1_dropped_audio_frames++;

           // Don't trigger the software interrupt for audio processing on this block
           return;
       }

And similarly, in ``audioframework_initialize()``, we to call audioflow_init_sport_dma() for our single audio periperhal (remove the others).

::

     // Initialize peripherals and DMA to configure audio data I/O flow
     audioflow_init_sport_dma( &SPR0_CODEC_8CH_Config );

The last step is reducing the DMA and SPORT enable code to enable just SPORT0 (and its corresponding DMAs).

.. code:: c

   void audioframework_start() {

       // Enable RX and TX DMAs for SPORT0 
       SPORT_DMA_ENABLE(0,1);
       SPORT_DMA_ENABLE(1,1);
       
       // Enable SPORT0 
       SPORT_ENABLE(0,A,0,1);
       SPORT_ENABLE(0,B,0,1);

   }

Step 5: On the SHARC Core 1, Update the Audio Callback
------------------------------------------------------

The last thing we need to do is to update the ``processaudio_output_routing()`` routing function in callback_audio_processing.cpp on SHARC Core 1. As described in the comments, this function routes audio from SHARC Core 2 to the output buffers associated with the various peripherals we have connected to the SHARC.

.. code:: c

   #if (USE_BOTH_CORES_TO_PROCESS_AUDIO)

   /*
     * When using a dual core configuration, SHARC Core 1 is responsible for routing the
     * processed audio from SHARC Core 2 to the various output buffers for the
     * devices connected to the SC589.  For example, in a dual core framework, SHARC Core 1
     * may pass 8 channels of audio to Core 2, and then receive 8 channels of processed audio
     * back from Core 2.  It is this routine where we route these channels to the ADAU1761,
     * the A2B bus, SPDIF, etc.
    */
   #pragma optimize_for_speed
   void processaudio_output_routing(void) {

       for (int i = 0; i < AUDIO_BLOCK_SIZE; i++) {

           // Send all 8 channels from SHARC core 2 to our codec 
           codec_0_left_out[i]  = audiochannel_from_sharc_core2_0_left[i];
           codec_0_right_out[i] = audiochannel_from_sharc_core2_0_right[i];
           codec_1_left_out[i]  = audiochannel_from_sharc_core2_1_left[i];
           codec_1_right_out[i] = audiochannel_from_sharc_core2_1_right[i];
           codec_2_left_out[i]  = audiochannel_from_sharc_core2_2_left[i];
           codec_2_right_out[i] = audiochannel_from_sharc_core2_2_right[i];
           codec_3_left_out[i]  = audiochannel_from_sharc_core2_3_left[i];
           codec_3_right_out[i] = audiochannel_from_sharc_core2_3_right[i];
       }
   }
   #endif

There are no modifications necessary for SHARC core 2.

Further Changes
---------------

Depending on your hardware configuration, the ports assignments of the peripherals you're using may have changed. In this case, open up the system.svc (at the bottom of the project file tree in the ARM core in CCES). The window that opens will have a number of tabs at the bottom. Click Pin Multiplexing and here you'll be able to map the peripherals you're using to the corresponding I/O pins on the processor.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#driver-creation-tutorial
   :alt: Creating Drivers for New Audio Components#.|Bare Metal Framework#flashing|Programming BM Framework to Flash
