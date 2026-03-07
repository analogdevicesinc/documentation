Tutorial: Building a 2.1 Amplifier with the Class-D Module
==========================================================

The Class D Fin contains two stereo class D amplifiers providing four channels of output. In this tutorial, we will use the Class D board to implement a 2.1 or 2.2 audio amplifier. This will include 2 channels of standard audio and one channel for a subwoofer (LFE).

The SSM3582 has an option to combine a two channels into a single channel with more power. This requires some modifications to the configuration file and the Class D amp board. For this tutorial, we'll use one of the stereo channels as our sub channel. However, should you need even more power, the option is there to combine two channels. Refer to the SSM3582 datasheet for more information

We will send the incoming stereo audio from the 1/8" jacks to the first SSM3582 on the Class D board. We'll pass this audio along unaffected as our stereo channels. We'll then mix our incoming left and right channels together, run them through a low-pass filter, and send this to the second SSM3582 on the class board. This will be our sub channel.

Connect a set of standard speakers to the speaker terminals for the first stereo pair on the Class D board, and connect a sub-woofer to either of the speaker terminals for the second stereo pair on the Class D board.

Connect your Class D amp board via the A2B cable to the SHARC Audio Module. The SLAVE port of the SHARC Audio Module should be connected to the MASTER port of the Class D amp board.

Configure the baremetal framework to use A2B and select the SAM->Class D tutorial.

.. code:: c

   #define ENABLE_A2B                                         TRUE

   #if (ENABLE_A2B)
   /**
     * If A2B is enabled, select the role that this SHARC Audio Module board
     * will play (TRUE = master node, FALSE = slave node)
    */
       #define A2B_ROLE_MASTER                                TRUE


   /**
     * If this SHARC Audio Module board is a master, select an A2B topology
     * 
     * Note that these topologies are created in SigmaStudio and stored
     * within drivers/bm_a2b_driver/a2b_topologies. See documentation for a
     * full description of these configurations.
     * NOTE: SET ONLY ONE TO TRUE
    */
       #if (A2B_ROLE_MASTER)
           #define A2B_TOPOLOGY_TDM8_SAM_to_SAM_2up_2down                       FALSE
           #define A2B_TOPOLOGY_TDM8_SAM_to_SAM_to_SAM_4up_4down                FALSE
           #define A2B_TOPOLOGY_TDM8_SAM_to_CLASSD_4down                        TRUE

           // Add your own pre-processor variables for custom A2B topologies here

       #endif  // A2B_ROLE_MASTER

   #endif  // ENABLE_A2B

Setting up our Biquad filters
-----------------------------

We'll use a fourth order low-pass IIR filter with a cutoff frequency of 100Hz to remove the higher frequencies from our sub channel. The easiest way to do this is to cascade two 2nd order identical biquad filters.

First, we'll to declare two instances of BIQUAD_FILTER and allocate some pm memory for our coefficients at the top of callback_audio_processing.cpp.

.. code:: c

   BIQUAD_FILTER lpf_stage1, lpf_stage2;
   float pm coeffs_stage1[6], coeffs_stage2[6];

Next, we'll need to initialize these instances in ``void processaudio_setup(void)`` like so:

.. code:: c

       filter_setup(&lpf_stage1,
                   BIQUAD_TYPE_LPF,
                   BIQUAD_TRANS_MED,
                   coeffs_stage1,
                   100.0,
                   1.0,
                   1.0,
                   AUDIO_SAMPLE_RATE);
       filter_setup(&lpf_stage2,
                   BIQUAD_TYPE_LPF,
                   BIQUAD_TRANS_MED,
                   coeffs_stage2,
                   100.0,
                   1.0,
                   1.0,
                   AUDIO_SAMPLE_RATE);

Processing Audio and Sending to Class D Board via A2B
-----------------------------------------------------

Finally, in ``void processaudio_callback(void)``, we're going to filter our audio and route the audio to the Class D board over the A2B bus.

.. code:: c

   void processaudio_callback(void) {
       float filter_mixed[AUDIO_BLOCK_SIZE];
       
       // First we'll mix the L and R channels together 
       mix_2x1(audiochannel_0_left_in, audiochannel_0_right_in, filter_mixed);
       
       // Next, we'll apply the filters to this data in place
       filter_read(&lpf_stage1, filter_mixed, filter_mixed, AUDIO_BLOCK_SIZE);
       filter_read(&lpf_stage2, filter_mixed, filter_mixed, AUDIO_BLOCK_SIZE);
       
       // Finally, we'll copy our input buffers to the first two A2B channels, and our filtered data to our second two A2B channels.
       
       // Original stereo audio to our stereo speakers
       copy_buffer(audiochannel_0_left_in, audiochannel_a2b_0_left_out, AUDIO_BLOCK_SIZE);
       copy_buffer(audiochannel_0_right_in, audiochannel_a2b_0_right_out, AUDIO_BLOCK_SIZE);

       // Filtered audio to our sub speakers
       copy_buffer(filter_mixed, audiochannel_a2b_1_left_out, AUDIO_BLOCK_SIZE);
       copy_buffer(filter_mixed, audiochannel_a2b_1_right_out, AUDIO_BLOCK_SIZE);

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#chaining-audio-elements
   :alt: Chaining Audio Elements#.|Bare Metal Framework#simple-midi-synth|Simple MIDI Synthesizer
