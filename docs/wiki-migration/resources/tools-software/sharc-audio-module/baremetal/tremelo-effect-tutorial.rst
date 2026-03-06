Tutorial: Implementing a Tremolo Effect
=======================================

Bare Metal Project Wizard Setup
-------------------------------

Using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`:

-  Give the project a meaningful name, click Next
-  Choose the Audio Project Fin on the Expansion Fin Selection Page because it is required for part of the tutorial, click Finish

**No other options need to be changed.**

Tutorial Overview
-----------------

A tremolo is a classic audio effect whereby we modulate the volume, or amplitude, of our audio signal using an oscillator. Here's a nice explanation of how the tremolo effect works and its various parameters.

.. image:: https://wiki.analog.com/_media/youtube>oOCNB1izw8A
   :alt: youtube>oOCNB1izw8A

In this tutorial, we're going to start by building a basic tremolo effect. We'll then add a few additional bells and whistles.

Just like last time, we'll be working in the ``callback_audio_processing.cpp`` file. We can implement this code either on SHARC core 1 or SHARC core 2.

Basic Tremolo with Fixed Parameters
-----------------------------------

To begin, we'll build a tremolo effect that relies on fixed parameters just like we did with volume.

.. code:: c

   #pragma optimize_for_speed
   void processaudio_callback( ) {

       static float tremolo_rate = 0.5;  // the rate of our tremolo (0.0 to 1.0)
       static float tremolo_depth = 0.5; // the depth of our tremolo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float trem_factor = 1.0 - (tremolo_depth*(0.5*sinf(t)+0.5));
           
           // Update t based on rate and a scalar that gets maps our rate roughly between 1Hz and about 20Hz
           t += (tremolo_rate * 0.002);
           
           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // Multiply each incoming sample by our amplitude modulation value for this sample
           audiochannel_0_left_out[i]  = trem_factor * audiochannel_0_left_in[i];
           audiochannel_0_right_out[i] = trem_factor * audiochannel_0_right_in[i];
       }
   }

Controlling the Tremolo Parameters with Pots on the Audio Project Fin
---------------------------------------------------------------------

Now we will map the HADC0 pot to our rate parameter and the HADC1 pot to our depth parameter. We don't want our rate to drop down to 0.0 since we'd effectively be multiplying our audio by a constant value at some point along the sine wave we're using to modulate. So we'll map the HADC0 input from a value of 0.1 to 1.0 rather than 0.0 to 1.0.

.. code:: c

   #pragma optimize_for_speed
   void processaudio_callback( ) {

       float tremolo_rate  = 0.1 + 0.9*multicore_data->audioproj_fin_pot_hadc0;  // the rate of our tremolo (0.1 to 1.0)
       float tremolo_depth = multicore_data->audioproj_fin_pot_hadc1; // the depth of our tremolo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float tremolo_factor = 1.0 - (tremolo_depth*(0.5*sinf(t)+0.5));

           // Update t based on rate and a scalar that gets maps our rate roughly between 1Hz and about 20Hz
           t += (tremolo_rate * 0.002);

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // Multiply each incoming sample by our amplitude modulation value for this sample
           audiochannel_0_left_out[i]  = tremolo_factor * audiochannel_0_left_in[i];
           audiochannel_0_right_out[i] = tremolo_factor * audiochannel_0_right_in[i];
       }
   }

Enabling / Disabling the Tremolo with SW1 on the Audio Project Fin
------------------------------------------------------------------

We may not want the tremolo enabled all the time so let's use one of the buttons on the Audio Project Fin to enable / disable the tremolo effect. Each of the buttons on the Audio Project Fin is mapped to a default callback that can be found in ``Callback_Pushbuttons.cpp`` in the ARM core (``<PROJECT_NAME>_core0``). In these callbacks, the LED below each button is toggled by default and a field in the multicore memory structure is written to indicate that a button event has happened. The nice thing is that we don't need to change any of this default pushbutton callback behavior to use SW1 to enable / disable our effect.

In our audio callback, we'll add a new variable called ``tremolo_enabled`` which will be set to false initially. At the bottom of this callback, we'll check to see if SW1/PB_1 has been pressed and if so, we'll toggle the ``tremolo_enabled``. When it comes time to process the input buffers, we'll check to see if tremolo_enabled is true. If so, we'll apply the effect and if not, we'll just pass the audio through.

.. code:: c

   #pragma optimize_for_speed
   void processaudio_callback( ) {

       float tremolo_rate  = 0.1 + 0.9*multicore_data->audioproj_fin_pot_hadc0;  // the rate of our tremolo (0.1 to 1.0)
       float tremolo_depth = multicore_data->audioproj_fin_pot_hadc1; // the depth of our tremolo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       static bool tremolo_enabled = false;

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float tremolo_factor = 1.0 - (tremolo_depth*(0.5*sinf(t)+0.5));

           // Update t based on rate and a scalar that gets maps our rate roughly between 1Hz and about 20Hz
           t += (tremolo_rate * 0.002);

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // If tremolo is enabled, apply the effect
           if (tremolo_enabled) {
               // Multiply each incoming sample by our amplitude modulation value for this sample
               audiochannel_0_left_out[i]  = tremolo_factor * audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = tremolo_factor * audiochannel_0_right_in[i];

           // Otherwise, just pass the audio through
           } else {
               audiochannel_0_left_out[i]  = audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = audiochannel_0_right_in[i];
           }
       }

       // If a push button event was logged, clear the event and toggle our enable variable
       if (multicore_data->audioproj_fin_sw_1_core1_pressed) {
           multicore_data->audioproj_fin_sw_1_core1_pressed = false;
           tremolo_enabled = !tremolo_enabled;
       }
   }

Using SW2 on the Audio Project Fin to Set the Tremolo Rate
----------------------------------------------------------

Some more advanced tremolo pedals allow you to repeatedly tap a button at the desired tempo or rate of the effect. We'll use SW2 to allow the user to set the rate of the tremolo by tapping SW2 at the desired tempo.

To do this, we'll add some code to our background loop. This loop is called repeatedly when we're not in the processaudio_callback routine.

.. code:: c

   void processaudio_background_loop( ) {

       // *******************************************************************************
       // Add any custom background processing here
       // *******************************************************************************

       static uint64_t last_press_cyclecounter = 0;

       if (multicore_data->audioproj_fin_sw_2_core1_pressed) {
           multicore_data->audioproj_fin_sw_2_core1_pressed = false;

           // Use the SHARC cycle counter to measure the time between taps
           uint64_t current_cyclecounter = __builtin_emuclk();
           float delta_seconds = ((float) (current_cyclecounter - last_press_cyclecounter)) * (1.0/(float)CORE_CLOCK_FREQ_HZ);
           float delta_samples = delta_seconds * AUDIO_SAMPLE_RATE;

           // If the time between button taps is between 1/20th of a second and 5 seconds, update our tremolo rate
           if (delta_samples < AUDIO_SAMPLE_RATE * 5.0 && delta_samples > AUDIO_SAMPLE_RATE / 20.0) {
               tremolo_rate = 6.28318531/delta_samples;
           }

           // Update our cycle counter variable
           last_press_cyclecounter = current_cyclecounter;
       }
   }

We'll also need to make two small modifications to our callback. First, we're going to declare ``tremolo_rate`` as a global variable. And, we're going to update the line where we increment our ``t`` variable.

.. code:: c

   // declared as a global variable so we can modify from processaudio_background_loop()
   float tremolo_rate = 0.5;

   #pragma optimize_for_speed
   void processaudio_callback( ) {

       float tremolo_depth = multicore_data->audioproj_fin_pot_hadc1; // the depth of our tremolo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       static bool tremolo_enabled = false;

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float trem_factor = 1.0 - (tremolo_depth*(0.5*sinf(t)+0.5));

           // Update t based on rate and a scalar that gets maps our rate roughly between 1Hz and about 20Hz
           t += tremolo_rate;

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // If tremolo is enabled, apply the effect
           if (tremolo_enabled) {
               // Multiply each incoming sample by our amplitude modulation value for this sample
               audiochannel_0_left_out[i]  = trem_factor * audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = trem_factor * audiochannel_0_right_in[i];

           // Otherwise, just pass the audio through
           } else {
               audiochannel_0_left_out[i]  = audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = audiochannel_0_right_in[i];
           }
       }

       // If a push button event was logged, clear the event and toggle our enable variable
       if (multicore_data->audioproj_fin_sw_1_core1_pressed) {
           multicore_data->audioproj_fin_sw_1_core1_pressed = false;
           tremolo_enabled = !tremolo_enabled;
       }
   }

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#using-both-cores
   :alt: Audio Processing Basics#.|Bare Metal Framework#ring-modulator-effect-tutorial|Implementing a Ring Modulator Effect
