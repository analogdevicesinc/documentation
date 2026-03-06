Tutorial: Implementing a Ring Modulator Effect
==============================================

Bare Metal Project Wizard Setup
-------------------------------

Using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`:

-  Give the project a meaningful name, click Next
-  Choose the Audio Project Fin on the Expansion Fin Selection Page because it is required for part of the tutorial, click Finish

**No other options need to be changed.**

Tutorial Overview
-----------------

A ring modulator is a wild audio effect that generates some very interesting sounds. In this effect, we multiply the incoming audio signal using an oscillator. Here's a nice explanation of how the ring modular effect works and its various parameters.

.. image:: https://wiki.analog.com/_media/youtube>vI0VKNkv0n0
   :alt: youtube>vI0VKNkv0n0

In this tutorial, we're going to start by building a basic ring modulator effect. We'll then add a few additional bells and whistles. Before you begin this tutorial, it's recommended to quickly go through :doc:`Tutorial: Tremolo Effect </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/tremelo-effect-tutorial>`.

Just like last time, we'll be working in the ``callback_audio_processing.cpp`` file. We can implement this code either on SHARC core 1 or SHARC core 2.

Basic Ring Modulator with Fixed Parameters
------------------------------------------

Just like in the tremelo tutorial, we'll start with some fixed parameters. ``ringmod_rate`` will set the frequency of the sine wave we're using to modulate the signal. ``ringmod_blend`` will set the mix of clean and modulated audio.

.. code:: c

   void processaudio_callback( ) {

       static float ringmod_rate = 0.5;  // the rate of our ring modulator (0.0 to 1.0)
       static float ringmod_blend = 0.5; // the blend or mix of our tremelo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       // Otherwise, perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float ring_factor = sinf(t);

           // Update t based on rate and a scalar to map into a nice range
           t += (ringmod_rate * 0.02);

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // Multiply each incoming sample by our amplitude modulation value for this sample
           audiochannel_0_left_out[i]  = (1.0-ringmod_blend)*audiochannel_0_left_in[i] + ringmod_blend*ring_factor*audiochannel_0_left_in[i];
           audiochannel_0_right_out[i] = (1.0-ringmod_blend)*audiochannel_0_right_in[i] + ringmod_blend*ring_factor*audiochannel_0_right_in[i];
       }
   }

Controlling the Ring Modulator Parameters with Pots on the Audio Project Fin
----------------------------------------------------------------------------

Now we will map the HADC0 pot to our rate parameter and the HADC1 pot to our blend / mix parameter. In the case, we're mapping HADC0 to a set of values between 2.0 and 6.0 which gives us a nice wide range of frequencies.

.. code:: c

   void processaudio_callback( ) {

       float ringmod_rate  = 2.0 + 4.0*multicore_data->audioproj_fin_pot_hadc0; // frequency scaler of our ring modulator (2 to 6.0)
       float ringmod_blend = multicore_data->audioproj_fin_pot_hadc1; // the blend or mix of our tremelo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       // Perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample
           float ring_factor = sinf(t);

           // Update t based on rate and a scalar to map into a nice range
           t += (ringmod_rate * 0.02);

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // Multiply each incoming sample by our amplitude modulation value for this sample
           audiochannel_0_left_out[i]  = (1.0-ringmod_blend)*audiochannel_0_left_in[i] + ringmod_blend*ring_factor*audiochannel_0_left_in[i];
           audiochannel_0_right_out[i] = (1.0-ringmod_blend)*audiochannel_0_right_in[i] + ringmod_blend*ring_factor*audiochannel_0_right_in[i];
       }
   }

Using Different Waveforms to Modulate the Signal (Selectable with SW2)
----------------------------------------------------------------------

Some ring modulator pedals allow the user to select between different waveforms to use to modulate the original signal. In this version, we'll use SW2 to select between a sine wave, a triangle wave and a square wave. And SW1 will be used to toggle the effect on and off.

.. code:: c

   float square_wave( float t ) {

       float x = sinf(t);
       if (x >= 0.0) return 1.0;
       else return -1.0;
   }

   float triangle_wave( float t ) {

       return asinf(cosf(t))/1.57079633;

   }

   #pragma optimize_for_speed
   void processaudio_callback( ) {

       float ringmod_rate  = 2.0 + 4.0*multicore_data->audioproj_fin_pot_hadc0; // frequency scaler of our ring modulator (2 to 6.0)
       float ringmod_blend = multicore_data->audioproj_fin_pot_hadc1; // the blend or mix of our tremelo (0.0 to 1.0)
       static float t = 0.0;     // current value of t for sine calculations

       static uint8_t current_modulator = 0;
       static bool ringmod_enabled = false;

       // Perform our C-based block processing here!
       for (int i=0;i<AUDIO_BLOCK_SIZE;i++) {

           // Calculate our modulation factor for this sample depending on which modulator is selected
           float ring_factor;
           if (current_modulator == 0) {
               ring_factor = sinf(t);
           }
           else if (current_modulator == 1) {
               ring_factor = triangle_wave(t);
           }
           else if (current_modulator == 2) {
               ring_factor = square_wave(t);
           }
           // Update t based on rate and a scalar to map into a nice range
           t += (ringmod_rate * 0.02);

           // Wrap t if necessary
           if (t > 6.28318531) t -= 6.28318531;

           // If ringmod enabled, apply the effect
           if (ringmod_enabled) {
               // Multiply each incoming sample by our amplitude modulation value for this sample
               audiochannel_0_left_out[i]  = (1.0-ringmod_blend)*audiochannel_0_left_in[i] + ringmod_blend*ring_factor*audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = (1.0-ringmod_blend)*audiochannel_0_right_in[i] + ringmod_blend*ring_factor*audiochannel_0_right_in[i];

               // Otherwise, just pass the audio through
           } else {
               audiochannel_0_left_out[i]  = audiochannel_0_left_in[i];
               audiochannel_0_right_out[i] = audiochannel_0_right_in[i];
           }
       }

       // Use SW1 / PB_1 to toggle the effect
       if (multicore_data->audioproj_fin_sw_1_core1_pressed) {
           multicore_data->audioproj_fin_sw_1_core1_pressed = false;
           ringmod_enabled = !ringmod_enabled;
       }

       // Use SW2 / PB_2 to cycle through the modulating waveforms
       if (multicore_data->audioproj_fin_sw_2_core1_pressed) {
           multicore_data->audioproj_fin_sw_2_core1_pressed = false;
           current_modulator += 1;

           if (current_modulator >= 3) {
               current_modulator = 0;
           }
       }
   }

When we press SW2, the LED next to the push button toggles. To disable this behavior, open ``Callback_Pushbuttons.cpp`` in the ``<PROJECT_NAME>_core0`` project. Locate the callback for PB2 (SW2) on the Audio Project Fin and comment out the code to toggle the LED:

.. code:: c

   // Call back for PB2 on SHARC Audio Module Audio Project Fin
   void pushbutton_callback_external_2( void  * data_object ) {

   /*
       static bool sw2_state = false;

       // Toggle the LED below the button to indicate state

       sw2_state = !sw2_state;
       if (sw2_state) {
           gpio_write(GPIO_AUDIOPROJ_FIN_LED_SW2, GPIO_HIGH);
       } else {
           gpio_write(GPIO_AUDIOPROJ_FIN_LED_SW2, GPIO_LOW);
       }
   */
       // Update our multicore structure to let the SHARCs know that a PB has been pressed
       multicore_data->audioproj_fin_sw_2_core1_pressed = true;
       multicore_data->audioproj_fin_sw_2_core2_pressed = true;

       // Add custom code here

   }

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#tremelo-effect-tutorial
   :alt: Implementing a Tremolo Effect#.|Bare Metal Framework#delay-effect-tutorial|Implementing a Delay Effect
