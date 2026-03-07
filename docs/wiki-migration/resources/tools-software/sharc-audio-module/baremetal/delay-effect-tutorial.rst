Tutorial: Implementing a Basic Delay Effect
===========================================

In this tutorial, we’ll use the bare metal framework to implement a basic echo / delay effect.

Bare Metal Project Wizard Setup
-------------------------------

Using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`:

-  Give the project a meaningful name, click Next
-  Choose the Audio Project Fin on the Expansion Fin Selection Page because it is required for part of the tutorial, click Finish

**No other options need to be changed.**

Echo Effect Basics
------------------

An echo effect is based on a delay line, a number of adders, and gain elements as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/echo_structure.gif
   :alt: Basic echo effect

The light blue elements in the figure represent the typical adjustable parameters on an delay processor, namely:

-  *Feedback*: determines how much of the delayed signal is added back into the original signal. This effects how long the echo lasts.
-  *Delay*: determines the time between the original signal and the time-delayed signal, as a number of audio samples. A high value may sound like you’re in the mountains (hello hello hello hello) while a smaller value will sound more like a dry room or underneath a bridge.
-  *Dry Mix*: amount of original signal mixed through to the output.
-  *Wet Mix*: amount of echoed signal that is mixed through to the output.

Let’s get to work!

Step 1: open up our audio processing callback
---------------------------------------------

All of our code will be placed in ``src/callback_audio_processing.cpp`` of the SHARC Core 1 project. This file provides all of the hooks you’ll need for your audio processing. It can be found here in the bare metal framework:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/audio-callback-location.png
   :alt: Project location

Step 2: declare the required global variables, including the delay lines
------------------------------------------------------------------------

We’re going to build a stereo echo which means that we’ll process the left and right channel independently, each through an echo effect of its own.

The SHARC Audio Module board has a very large amount of DDR SDRAM that is perfect to implement long delay lines.

First, let's declare two large floating point buffers (a stereo pair) and instruct the linker to place them in SDRAM. We will declare buffers large enough to hold 5 seconds of audio. The following formula can help us establish how big that is:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/delay_formula.gif
   :alt: Delay formula

For a maximum delay of 5 seconds between echos, in a project where the sampling rate is set to 48KHz, our delay lines must have a size of: **48,000 Hz x 5 s = 240,000 samples**.

Place the following declarations immediately before the ``processaudio_setup()`` function in ``callback_audio_processing.cpp``

.. code:: c

   #define  MAX_DELAY_SECONDS  (5)
   #define  DELAY_LINE_SIZE    (AUDIO_SAMPLE_RATE * MAX_DELAY_SECONDS)

   #pragma section("seg_sdram")
   volatile float delay_line_left[DELAY_LINE_SIZE];
   #pragma section("seg_sdram")
   volatile float delay_line_right[DELAY_LINE_SIZE];

Next, still above ``processaudio_setup()``, let's declare global variables that will serve as parameters to the delay line:

.. code:: c

   // length of delay in seconds
   float    delay_len_seconds = 1.0;

   // length of delay in samples
   uint32_t  delay_len_samples = (uint32_t) delay_len_seconds * AUDIO_SAMPLE_RATE;

   // wet mix (from delay line)
   float    delay_wet_mix = 0.5;

   // dry mix (original audio)
   float    delay_dry_mix = 0.5;

   // delay feedback
   float    delay_feedback = 0.3;

Note that we declared a parameter to hold the delay length, in seconds, and *initially set it to 1*. Although we have allocated enough memory to support 5 second delay lines, we can limit our memory accesses to a subset of this area, defined with this variable. This can provide a real time control of the delay line length that is more efficient than reallocating memory dynamically every time our delay parameter changes.

Finally, let's declare an index to access distinct samples in our delay lines:

.. code:: c

   uint32_t    delay_line_index = 0;

Step 3: zero the delay lines
----------------------------

The ``processaudio_setup()`` function gets called at startup and is a good place to initialize variables (filter coefficients, e.g.). It’s good practice to zero the delay lines, so write the following code in the ``processaudio_setup()`` function:

.. code:: c

   /*
     * Place any initialization code here for the audio processing
    */
   void processaudio_setup( void ) {
       int i;

       // zero delay lines used for echo effect
       for (i=0;i<DELAY_LINE_SIZE;i++) {
           delay_line_left[i] = 0.0;
           delay_line_right[i] = 0.0;
       }
   }

Step 4: implement the echo effect
---------------------------------

The ``processaudio_callback()`` function gets called each time a new block of audio is ready to be processed. The original version of this function contains a number of example audio routing code snippets.

Audio input data, from the ADCs, can be read from ``audiochannel_0_left_in`` and ``audiochannel_0_right_in``. Similarly, output audio data (e.g. post-processing) can be written to ``audiochannel_0_left_out`` and ``audiochannel_0_right_out``. If single-core audio processing is selected, these output buffers are sent to the DACs. If dual-core audio processing is selected, these buffers are passed along to SHARC Core 2. This way, it is possible to enable/disable dual core processing without touching the audio processing code written for SHARC Core 1.

Let's write the audio processing code implementing the echo effect itself in this function. First remove or disable the audio routing example snippets – for instance by surrounding them with a pre-processor ``#if 0`` condition – to ensure the audio buffers written by the echo code are not immediately overwritten. Then write the following signal processing routine in ``processaudio_callback``:

.. code:: c

   void processaudio_callback( void ) {

       // Otherwise perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Read last audio sample in each delay line
           float delayed_left  = delay_line_left[delay_line_index];
           float delayed_right = delay_line_right[delay_line_index];

           // Mix the above with current audio and write the results back to output
           audiochannel_0_left_out[i] = (audiochannel_0_left_in[i] * delay_dry_mix) +
                                        (delayed_left * delay_wet_mix);
           audiochannel_0_right_out[i] = (audiochannel_0_right_in[i] * delay_dry_mix) +
                                         (delayed_right * delay_wet_mix);

           // Update each delay line
           delay_line_left[delay_line_index]  = delay_feedback * (delayed_left + audiochannel_0_left_in[i]);
           delay_line_right[delay_line_index] = delay_feedback * (delayed_right + audiochannel_0_right_in[i]);

           // Finally, update the delay line index
           if (delay_line_index++ >= delay_len_samples) {
               delay_line_index = 0;
           }
       }
   }

Now compile, upload and run your code.

Note that when running your code as part of a debug session, the IDDE will pause the execution automatically upon entering a core's ``main()`` function. Press the Resume button (see below) for all three cores to allow them to run in order to hear audio.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/debugcores.png
   :width: 800px

Additional Things To Try
------------------------

Routing audio to / from other peripherals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can route audio to/from other peripherals by simply utilizing different buffers. For example, the following code snippet routes the output audio data to the S/PDIF transmitter instead of the DACs on the ADAU1761:

.. code:: c

   audiochannel_spdif_0_left_out[i] = (audiochannel_0_left_in[i] * delay_dry_mix) +
                                      (delayed_left * delay_wet_mix);
   audiochannel_spdif_0_right_out[i] = (audiochannel_0_right_in[i] * delay_dry_mix) +
                                       (delayed_right * delay_wet_mix);

See the product documentation for a full list of audio buffers available.

Check CPUs loading
~~~~~~~~~~~~~~~~~~

Halt Core 0 (ARM core) and open up an Expressions window in CCES. Add the variable ``multicore_data`` to the Expressions window and expand it. You’ll see a set of variables that record peak and current CPU loading for each core. This value is expressed in MHz so the maximum is 450.0 by default. As you can see, the delay line plus the audio framework consumes about 15MHz which is a mere 3% of the available processing power on just one core!

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/mips-loading.png
   :alt: MIPS Loading

Have an Audio Project Fin? Wire in the POTs to control the effect in real time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Audio Project Fin is an expansion board that has 1/4" instrument jacks, 3 pots, push-buttons and a MIDI interface.

The multicore memory structure contains the current value of each pot. We can overwrite the fixed delay length, feedback, and dry/wet values with values sensed dynamically from these pots.

First, let's create two extra global variables to hold the new delay length:

.. code:: c

   float    new_delay_len_seconds;
   uint32_t new_delay_len_samples;

Second, let's sense the pot values to refresh our delay line each time we enter ``processaudio_callback()``. Add the following code in ``processaudio_callback()`` before the audio processing loop written at step three:

.. code:: c

   // Use the first pot to control our feedback.  The pot values are floats between 0.0 and 1.0
   delay_feedback = multicore_data->audioproj_fin_pot_hadc0;

   // Use the second pot to control our wet mix.  The pot values are floats between 0.0 and 1.0
   delay_wet_mix = multicore_data->audioproj_fin_pot_hadc1;

   // Use the third pot to control delay length.
   new_delay_len_seconds = multicore_data->audioproj_fin_pot_hadc2 * MAX_DELAY_SECONDS;

   // Calculate the new delay length based on the pot value sensed
   new_delay_len_samples = (uint32_t) (new_delay_len_seconds * AUDIO_SAMPLE_RATE);

Notice that as it stands, the new delay length has no effect. Relics in the delay line will cause audible artifacts when we increase the delay length, so we must take care to zero them. However, this can represent a significant amount of processing given the size of the delay line arrays and we must also take care not to overload ``processaudio_callback()``.

This is a situation where we should take advantage of the ``processAudio_BackgroundLoop()`` function, which runs in the background without interrupting the audio processing callback. Add the following code to that function:

.. code:: c

   // If we're expanding our delay line, zero audio from the new part to remove old relics,
   // note that SDRAM is a much faster if we write to it linearly so we write a distinct
   // loop for each delay line
   uint32_t j;
   for (j=delay_len_samples; j < new_delay_len_samples; j++) {
       delay_line_left[j] = 0.0;
   }
   for (j=delay_len_samples; j < new_delay_len_samples; j++) {
       delay_line_right[j] = 0.0;
   }
   delay_len_samples = new_delay_len_samples;

Note that the delay length will only increase *after* the zeroing of both delay line expansion areas so it is quite safe. Now compile, upload and run your code again. You can turn the pots on the Audio Project Fin to control the delay parameters in real time.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#ring-modulator-effect-tutorial
   :alt: Implementing a Ring Modulator Effect#.|Bare Metal Framework#audio-elements\|"Audio Elements" and "Audio Effects"
