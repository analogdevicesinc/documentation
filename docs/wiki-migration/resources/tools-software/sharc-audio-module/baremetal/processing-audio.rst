Processing Audio
================

The bare metal framework supports numerous peripherals including audio codecs, A2B, and S/PDIF. The framework itself ensures that audio is properly sample-rate-converted (as necessary) and that audio arrives where it needs to get in time. The framework has been architected such that code which deals with the hardware is abstracted away.

Single-Core Audio Flow
----------------------

When using a single SHARC core for audio processing, audio is only routed through the first SHARC core. When a new set of audio buffers is ready to be presented, the audio callback function ``processaudio_callback`` is called (located in ``callback_audio_processing.cpp``).

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/single-core-config.png
   :alt: Single core audio flow

While the SHARC core is processing the current block of audio, the DMA system is simultaneously transmitting the last processed block of audio to the DACs (and other transmit devices / peripherals) and receiving the next block of audio to be processed from the ADCs (and other receive devices / peripherals). In this configuration, the system has a latency of AUDIO_BLOCK_SIZE x 2.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/single-core-latency.png
   :alt: Single core audio latency

Dual-Core Audio Flow
--------------------

When using both SHARC cores for audio processing, audio is sent first to Core 1 and then to Core 2. Audio from Core 2 is then sent back to Core 1 such that it can be routed to specific peripherals via the ``processaudio_output_routing()`` function. This function is only used when dual core processing is enabled.

Both cores rely on the same style of audio callback so audio processing code can be moved from one core to another without rewriting the code.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/dual-core-config.png
   :alt: Dual core audio flow

| As described above, the DMA system is moving audio data around in the background while both SHARC cores are processing blocks of audio.
| |Dual core audio latency|

Audio Callbacks
~~~~~~~~~~~~~~~

In both SHARC Core 1 and SHARC Core 2, there is a file called ``callback_audio_processing.cpp``. These files are where you can begin putting your audio processing functions. These files use the same naming conventions so it becomes pretty easy to move algorithms from one core to another.

These callback files are written in C but have the .cpp extension so existing C++ code can also be used with the framework and called from these callbacks.

These files contain a few key functions:

``processaudio_setup()`` : This is where any initialization code goes for your audio algorithms. This is where, for example, you might generate filter coefficients or allocate memory for a delay line. This function is called by the ``Startup_Code_Core.cpp`` file in each core once all of the DMAs have been set up but before everything is kicked off.

``processaudio_callback()`` : This is where your main audio processing goes. You’ll find a for loop in here that is set to the project-wide block size defined in ``audio_system_config.h``. Depending on the framework you’re using, there are a number of specific buffers that you can read and write to (e.g. ADAU1761 codec, SPDIF in and out, A2B bus, etc.). This function gets called everytime a new block of data is ready to be processed. All of the I/O buffers are single-precision floating point.

``processaudio_background_loop()`` : If your algorithm relies on any background processing (like gathering larger blocks of data and running an FFT, this is where you can do that. This function is called by the ``Startup_Code_Core.cpp`` file once the audio has been kicked off. You can put a while(1) loop within this processaudio_background_loop() and wait for pend on a flag that indicates you have enough audio buffered for an FFT, for example.

``processaudio_mips_overflow()`` : If the processaudio_callback() function takes too long to run and does not complete by the time the next audio block arrives, this callback function is called. There are also variables in the shared memory/multicore audio struct that contain telemetry data on the number of overflow events.

On SHARC Core 0, you’ll also notice that there is a function called ``processaudio_output_routing()`` that is only enabled when using both processors to process audio. This function allows you to route the audio that SHARC Core 2 just processed out to various buffers (e.g. ADAU1761 codec, SPDIF in and out, A2B bus, etc.).

Audio pointer aliases and audio buffers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you look in the main processing loop, ``processaudio_callback()``, you’ll see a set of non-descript buffers being used called ``audiochannel_0_left_in[]``, ``audiochannel_0_right_in[]``, ``audiochannel_0_left_out[]`` and ``audiochannel_0_right_out[]``. Depending on the framework and your hardware configuration, these buffers point to the most commonly used audio buffers (e.g. ADAU1761 codec, SPDIF in and out, A2B bus, etc.). For example, ``audiochannel_0_left_in[]`` and ``audiochannel_0_right_in[]`` typically point to the buffer that contains the stereo ADC data from the ADAU1761.

If you’re using only one core to process your audio, the corresponding ``audiochannel_0_left_out[]`` and ``audiochannel_0_right_out[]`` point to the buffer that contains stereo DAC data for the ADAU1761. However, if you’ve selected to use both cores, then these point to the buffers that get transferred to core 2 instead. The nice thing about this architecture is you can easily move between single and dual core processing without having to change much, and if you have an algorithm implemented on SHARC core 1 that uses these pointer aliases, you can move it to core 2 and it will work there too. On core 2, ``audiochannel_0_left_in[]`` and ``audiochannel_0_right_in[]`` point to the buffers used to receive audio from core 1, and ``audiochannel_0_left_out[]`` and ``audiochannel_0_right_out[]`` point to the buffers used to move audio back to core 1.

If you open up the header file that corresponds to the audio framework you are using, you will see all the various buffers available. If you want to explicitly write data to a certain peripheral, you can also write to that buffer directly instead of the generalized alias.

.. code:: c

       // Send a sine wave to the S/PDIF transmitter
       audiochannel_spdif_0_left_out[i]  = 0.5 * sinf(t);
       audiochannel_spdif_0_right_out[i] = 0.5 * sinf(t);

       // Send audio received from S/PDIF receiver to the DACs on the ADAU1761
       audiochannel_adau1761_0_left_out[i] = audiochannel_spdif_0_left_in[i];
       audiochannel_adau1761_0_right_out[i] = audiochannel_spdif_0_right_in[i];

       // Send audio from ADCs and SPDIF to SHARC Core 2
       // In our 8 channel framework, we have 8 channels we can use to move audio between the cores
       // In our 16 channel framework, we have 16 channels we can use to move audio between the cores
       audiochannel_to_sharc_core2_0_left[i] = audiochannel_spdif_0_left_in[i];
       audiochannel_to_sharc_core2_0_right[i] = audiochannel_spdif_0_right_in[i];
       audiochannel_to_sharc_core2_1_left[i] = audiochannel_adau1761_0_left_in[i];
       audiochannel_to_sharc_core2_1_right[i] = audiochannel_adau1761_0_right_in[i];

The audio framework then manages the flow of audio between the cores and the conversion between fixed / floating point. And when using a dual core framework, audio is passed from core 1 to core 2 and core 2 to core 1 at the block interrupts.

Audio Processing Capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The two SHARC cores provide a hefty amount of audio processing power. However, it is important to ensure that any audio processing code can run and complete within one frame of audio.

The total number of cycles available in the audio callback can be calculated as follows:

*total cycles = ( processor-clock-speed \* audio-block-size ) / audio-sample-rate*

For example, if the processor is running at 450MHz, the audio sampling rate is 48KHz and the audio block size is set to 32 words, the total number of processor cycles available in each callback is 300,000 cycles or 300,000/32 or 9,375 per sample of audio.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#configuring-the-framework
   :alt: Configuring the Framework#.|Bare Metal Framework#audio-frameworks|Selecting Between HW Platforms

.. |Dual core audio latency| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/dual-core-latency.png
