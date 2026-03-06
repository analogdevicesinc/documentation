Tutorial: A Simple MIDI Synthesizer
===================================

Bare Metal Project Wizard Setup
-------------------------------

Using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`:

-  Give the project a meaningful name, click Next
-  Choose the Audio Project Fin on the Expansion Fin Selection Page because it is required for part of the tutorial, click Finish

**No other options need to be changed.**

Tutorial Overview
-----------------

In this tutorial, we will develop a basic MIDI synthesizer using the SHARC Audio Module and the Audio Project Fin.

The synthesizer will support a handful of oscillators (sine, square, triangle, etc.) as well as ADSR (Attack-Decay-Sustain-Release) envelope control. Here's a nice `tutorial on ADSR <https://www.wikiaudio.org/adsr-envelope/>`__. In this tutorial, we'll trigger the synthesizer from the MIDI interface.

Ensuring MIDI is Set Up Properly
--------------------------------

Open up ``/common/audio_system_config.h`` and be sure that Faust is not enabled and that MIDI notes will be sent to the SHARC Core 1 and not the ARM core.

.. code:: c

   //*****************************************************************************
   // 6. Faust and MIDI configuration
   //*****************************************************************************
   #define FAUST_INSTALLED                                 FALSE

...and a bit below...

.. code:: c

     #define   MIDI_UART_MANAGED_BY_ARM_CORE      FALSE
     #define   MIDI_UART_MANAGED_BY_SHARC1_CORE   TRUE

Setting up the Audio Synthesis
------------------------------

Up until now, we've been working in ``callback_audio_processing.cpp``. In this tutorial, we'll also be working on ``Callback_MIDI_Message.cpp``.

To begin, let's get the audio processing in place. At the top of ``callback_audio_processing.cpp`` include our synth audio element and our audio utilities with the other include files like so:

.. code:: c

   // Simple Synth Engine
   #include "audio_processing/audio_elements/audio_elements_common.h"
   #include "audio_processing/audio_elements/audio_utilities.h"
   #include "audio_processing/audio_elements/simple_synth.h"

Locate the function called ``processaudio_setup()``. Right above this function, we'll declare an array of our new synth struct. Each instance of the simple synth can support a single note. However, if we want to support chords, we'll need more than one instance of the synth so we'll declare an array of the synth structs with 16 elements. This basically means we're building a synth than can generate up to 16 notes at once (16 not polyphony).

.. code:: c

   // Create a synth with up to 16 voices
   SIMPLE_SYNTH synth_voices[16];

And in ``processaudio_setup()``, we'll initialize each "voice" of our synthesizer. The first parameter we pass is a pointer to the struct instance. The next four parameters are the attack, decay, sustain and release parameters in *samples*. So if want to create an instrument with an attach that is 1 second long, and our sample rate is 48KHz, we'd use a value of 48000. The next argument is the type of oscillator we want to use in our synth. If you look at ``audio_processing/audio_elements/simple_synth.h``, you'll find a few options include sine wave, square wave, triangle wave and a pulse train. Lastly, we'll pass along a few parameters related to our audio system setup.

.. code:: c

   /*
     * Place any initialization code here for the audio processing
    */
   void processaudio_setup( void ) {

       // *******************************************************************************
       // Add any custom setup code here
       // *******************************************************************************

       int i;
       for (i=0;i<16;i++) {
            synth_setup(   &synth_voices[i],
                           2000,
                           2000,
                           28000,
                           20000,
                           SYNTH_TRIANGLE,
                           (float) AUDIO_SAMPLE_RATE );
       }
   }

At this point, we've initialized all 16 voices of our synth engine. Now, we'll add the synth_read() function to our ``processaudio_callback()``. We're going to run the synth_read() function on all 16 voices. If one of those voices is playing a note, it's going to generate a waveform in the output buffer. If it's not playing a note, it will fill the output buffer with zeros.

.. code:: c

   void processaudio_callback( ) {

       float temp_audio[AUDIO_BLOCK_SIZE], temp_audio_accum[AUDIO_BLOCK_SIZE];

       // Quick way to zero audiochannel_0_left_out
       clear_buffer(temp_audio_accum, AUDIO_BLOCK_SIZE);

       // Scan remaining channels and synthesize when playing
       for (int i=0;i<16;i++) {
           synth_read(&synth_voices[i], temp_audio, AUDIO_BLOCK_SIZE );
           
           // Mix this synth voice with our accumulated audio
           mix_2x1(temp_audio, temp_audio_accum, temp_audio_accum, AUDIO_BLOCK_SIZE);
       }

       // Scale and copy the synthesized audio to our output buffers
       gain_buffer(audiochannel_0_left_out, 0.25, AUDIO_BLOCK_SIZE);
       gain_buffer(audiochannel_0_right_out, 0.25, AUDIO_BLOCK_SIZE);
       
   }

Setting up the MIDI Control
---------------------------

At this point, we're all ready to begin synthesizing audio. We just need to connect our synthesizer to something that can generate note information for us - MIDI!. Here's a nice `reference on MIDI messages <https://www.midi.org/specifications-old/item/table-1-summary-of-midi-message>`__.

Open up ``Callback_MIDI_Message.cpp``\ in SHARC Core 1 and at the top, we'll both include our ``simple_synth.h`` header file and also create an extern declaration for our array of structs we declared in the audio callback so we can reference it in this file too.

.. code:: c

   #include "audio_processing/audio_elements/simple_synth.h"
   extern SIMPLE_SYNTH synth_voices[];

Now we're going to update the MIDI callback which is called each time we have a new byte from the MIDI interface that's ready to parse.

Replace the contents of ``midi_rx_callback_sharc1()`` with the code below. This code is implements a very primitive MIDI parser that will look for *MIDI note on* and *MIDI note off* events. When a *note on* event is detected, this code will iterate through our 16 structs (each corresponding to a voice of our synthesizer). As soon as it finds one that is not playing, it will play the MIDI note on this voice via the ``synth_start_note()`` function. Similarly, when a *note off* event is detected, the code will iterate through the 16 voices and look for one that has the same note value as the note that should be turned off. Once this is found, the ``synth_stop_note()`` function is called on this voice.

.. code:: c

   void midi_rx_callback_sharc1( void ) {

       uint8_t val;
       int i;

       static uint32_t midi_state = 0;
       static bool midi_note_start = false;
       static bool midi_note_stop = false;

       static uint32_t midi_note = 0;
       static uint32_t midi_vol = 0;

       // Keep reading bytes from MIDI FIFO until we have processed all of them
       while (uart_available(&MIDI_UART_SHARC1)) {

         // Read the new byte
         uart_read_byte(&MIDI_UART_SHARC1, &val);

         // Look for note on event on midi channel 0
         if (midi_state == 0 && val == 0x90) {
             midi_state = 1;
             midi_note_start = true;
             return;
         }

         // Look for a note off event on midi channel 0
         if (midi_state == 0 && val == 0x80) {
             midi_state = 1;
             midi_note_stop = true;
             return;
         }

         if (midi_state == 1) {
             midi_note = val;
             midi_state = 2;
             return;
         }
         if (midi_state == 2) {
             midi_vol = val;
             midi_state = 0;

             if (midi_note_start) {
                 // Look for an unused synth element to play this note on
                 bool found = false;
                 int indx = 0;
                 do {
                     if (!synth_voices[indx].playing) {
                         synth_play_note( &synth_voices[indx], midi_note, ((float) midi_vol)*(1.0/128.0) );
                         found = true;
                     }
                     indx++;
                 } while (!found && indx < 16);
                 midi_note_start = false;

                 return;
             }

             if (midi_note_stop) {

                 // Look for a playing synth with this note
                 bool found = false;
                 int indx = 0;
                 do {
                     if (synth_voices[indx].playing && synth_voices[indx].note == midi_note ) {
                         synth_stop_note( &synth_voices[indx] );
                         found = true;
                     }
                     indx++;
                 } while (!found && indx < 16);
                 midi_note_stop = false;

                 return;
             }
          }
       }
   }

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#class-d-2-1-amp
   :alt: Building a 2.1 Amp#.|Bare Metal Framework#..hardware|Hardware Reference
