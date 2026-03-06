Tutorial: Audio Processing Basics with One or Two Cores
=======================================================

The baremetal audio framework is architected such that each time a new block of audio is available and ready to process, a callback function is called. This is described in more detail in the :doc:`Processing Audio </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/processing-audio>` section.

Within the ``processaudio_callback()`` function, we can either process individual samples of audio that are available in the various input buffers or we can call functions that operate on the entire block of audio.

For example, say we wanted to change the gain / volume by a factor of 0.5 on the incoming audio from the 1/8" audio in jack on the SHARC Audio Module, and send the output back to the 1/8" audio out jack. We'd do this by multiplying each of our input samples by 0.5, and then sending the result to our output buffer like so.

.. code:: c

   void processaudio_callback(void) {
       
       for (int i=0; i < AUDIO_BLOCK_SIZE; i++) {
           audiochannel_0_left_out[i]  = 0.5 * audiochannel_0_left_in[i];
           audiochannel_0_right_out[i] = 0.5 * audiochannel_0_right_in[i];
       }
   }

Or say we had written a function call ``volume_half( float * in, float * out, int samples)`` that performed this operation on a block of data. Since this function operates on a block of audio data, we can simply pass our input and output buffer pointers to this function and don't need the for loop.

.. code:: c

   void processaudio_callback(void) {
       
       volume_half(audiochannel_0_left_in, audiochannel_0_left_out, AUDIO_BLOCK_SIZE);
       volume_half(audiochannel_0_right_in, audiochannel_0_right_out, AUDIO_BLOCK_SIZE);
   }

As noted in the :doc:`Processing Audio </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/processing-audio>` section, we have callbacks on both SHARC cores. If both SHARC cores are configured to process audio (set in common/audio_system_config.h), the output buffers from core 1 are passed to core 2 and become input buffers. So the processing flow is input->core 1->core 2->output.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#troubleshooting
   :alt: Troubleshooting#.|Bare Metal Framework#tremelo-effect-tutorial|Implementing a Tremolo Effect
