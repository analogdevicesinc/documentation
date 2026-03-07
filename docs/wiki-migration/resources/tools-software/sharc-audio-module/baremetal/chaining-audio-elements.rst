Tutorial: Chaining Audio Elements and Audio Effects
===================================================

The power of the audio elements is how they can be combined in novel ways to create audio effects. In this tutorial, we'll implement a bank of band-pass filters that feed into a set of different delay lines set to different delay lengths.

To do this, we'll first need to declare instances of the biquad and integer_delay_lpf audio elements at the top of ``src/callback_audio_processing.cpp`` on the first SHARC core.

.. code:: c

   // Declarations for struct/instances for filters 
   BIQUAD_FILTER filt_300Hz, filt_900Hz;
   float pm filt_300Hz_coeffs[4]; 
   float pm filt_900Hz_coeffs[4];

   // Declaration of delay element structs and buffers for delay lines
   DELAY_LPF     delay_1, delay_2;
   float    section("seg_sdram") delay_buffer_1[AUDIO_SAMPLE_RATE\*2];
   float    section("seg_sdram") delay_buffer_2[AUDIO_SAMPLE_RATE\*2];

Next, we'll set up the instances in the processaudio_setup() function in ``src/callback_audio_processing.cpp`` on the first SHARC core.

.. code:: c

   void processaudio_setup(void) {

       // *******************************************************************************
       // Add any custom setup code here
       // *******************************************************************************

       // Set up filters
       filter_setup(&filt_300Hz,
                    BIQUAD_TYPE_BPF,
                    BIQUAD_TRANS_MED,
                    filt_300Hz_coeffs,
                    300.0,  // Center frequency
                    4.0,    // Q
                    1.0,    // Gain (db)
                    AUDIO_SAMPLE_RATE);
       filter_setup(&filt_900Hz,
                    BIQUAD_TYPE_BPF,
                    BIQUAD_TRANS_MED,
                    filt_900Hz_coeffs,
                    900.0,  // Center frequency
                    4.0,    // Q
                    1.0,    // Gain (db)
                    AUDIO_SAMPLE_RATE);   
                                                   
       // Set up delay lines
       delay_setup(&delay_1,
                   delay_buffer_1,
                   AUDIO_SAMPLE_RATE\*2,
                   AUDIO_SAMPLE_RATE\*0.25, // set delay line initially to 0.25 seconds
                   0.8,  // Feedthrough
                   0.6,  // Feedback
                   0.0); // Dampening coefficient (0=no dampening)
    
       delay_setup(&delay_2,
                   delay_buffer_2,
                   AUDIO_SAMPLE_RATE\*2,
                   AUDIO_SAMPLE_RATE\*0.5, // set delay line initially to 0.5 seconds
                   0.8,  // Feedthrough
                   0.6,  // Feedback
                   0.0); // Dampening coefficient (0=no dampening)               
                   
   }

Finally, we'll process audio in ``void processaudio_callback(void)``. First, we will run the biquads on the incoming left and right audio channels and save the outputs to a pair of buffers called 'audio_temp_1' and 'audio_temp_2'. We'll then use these buffers as the inputs to our delay functions. Finally, we'll send the outputs of the delay function to the left channel and right channel outputs.

.. code:: c

   void processaudio_callback(void) {

       float audio_temp_1[AUDIO_BLOCK_SIZE];
       float audio_temp_2[AUDIO_BLOCK_SIZE];
       
       // Run filters on incoming L/R input audio
       filter_read(&filt_300Hz, audiochannel_0_left_in, audio_temp_1, AUDIO_BLOCK_SIZE);
       filter_read(&filt_900Hz, audiochannel_0_right_in, audio_temp_2, AUDIO_BLOCK_SIZE);

       // Run filtered audio through delay lines and send to L/R/ output audio
       delay_read(&delay_1, audio_temp_1, audiochannel_0_left_out, AUDIO_BLOCK_SIZE);
       delay_read(&delay_2, audio_temp_2, audiochannel_0_right_out, AUDIO_BLOCK_SIZE);

   }

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#volume-control-tutorial
   :alt: Programming a Volume Control#.|Bare Metal Framework#class-d-2-1-amp|Building a 2.1 Amplifier
