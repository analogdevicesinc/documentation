Introduction to the "Audio Elements" and "Audio Effects"
========================================================

The **audio elements** are a collection of basic audio processing building blocks that can be combined to quickly build many types of audio effects and synthesizers.

The **audio effects** are full audio effects (e.g. tube distortion, stereo reverb, flanger, etc.) that have been created by connecting various **audio elements**.

List of audio elements
----------------------

-  ``allpass_filter.c/.h`` - An implementation of an all-pass filter structure that is commonly used in reverb algorithms. The allpass filter implemented here follows an allpass from two comb filter implementation. You find more information here: https://ccrma.stanford.edu/~jos/pasp/Allpass_Two_Combs.html.
-  ``amplitude_modulation.c/.h`` - An amplitude modulation effect which modulates the amplitude of an incoming signal using a second signal. Amplitude modulation is the main building block when implementing tremelo effects.
-  ``biquad_filter.c/.h`` - Provides a set of functions for defining, modifying and implementing a biquad (2nd order IIR) filter. This set of routines can be used to define low-pass, high-pass, band-pass, notch and shelving fiters. Once defined, a filter can also be safely dynamically modified for use in effects like wah pedals, envelope filters/auto-wah effects.
-  ``clickless_vol_ctrl.c/.h`` - Provides a basic gain / volume control function that can be changed on the fly in a "clickless" manner. This means that the volume is changed gradually enough such that no discontinuities are generated in the audio (result in clicks). This element can be used in basic input/output gain control but also effects like auto-swell effects.
-  ``clipper.c/.h`` - Provides a clipping function that relies on polynomial expansion. This function also supports optional upsampling / downsampling for tube-amp emulation to avoid audio artifacts that result in clipping without up/down sampling.
-  ``integer_delay_lpf.c/.h`` - Provides a single-tap digital delay. The feedback path can be optionally routed through a single-pole low-pass filter for a dampening effect. This function can be used to implement echo/delay effects, multi-channel looper effects, and reverbs. Because the SHARC Audio Module contains an abundance of DDR SDRAM, some really interesting effects can be created using long delay lines.
-  ``integer_delay_multitap.c/.h`` - Provides a multi-tap digital delay supporting up to 32 taps per delay line. Multi-tap delay lines are used in reverbs as well as novel digital delay/echo effects.
-  ``oscillators.c/.h`` - Provides fundamental oscillators such as sine, square, triangle, etc. These oscillators are used in a number of other elements
-  ``simple_synth.c/.h`` - Provides a set of basic synthesizer functionality built from the oscillators. Supports ADSR (Attach/Decay/Sustain/Release) envelopes, note volume, and note playing state. Notes can be triggered using MIDI note numbers (useful when building a MIDI synth) or frequencies (useful when building a guitar synth).
-  ``variable_delay.c/.h`` - Provides a variable delay line (frequency modulation). This is the basic building block of choruses, phases shifters, flangers and even tape-delay simulators.
-  ``zero_crossing_detector.c/.h`` - Detects zero crossing to roughly determine frequency of incoming signal from an instrument. This approaches doesn't work well for chords (FYI).

-  ``audio_utilities.c/.h`` - Provides a number of utility functions for copying and mixing audio buffers, measuring gain, etc.
-  ``audio_elements_common.h`` - Provides some constant values used across the audio elements.

List of audio effects
---------------------

-  ``effect_guitar_synth.c/.h`` - A multi-note guitar synth with envelope filter. This audio effect combines the zero_crossing_detector, biquad and simple_synth audio elements.
-  ``effect_stereo_reverb.c/.h`` - A stereo reverb based on the Freeverb architecture. This audio effect combines the allpass_filter and integer_delay_lpf audio elements.
-  ``effect_stereo_flanger.c/.h`` - A stereo flanger effect. This audio effect utilizes the variable_delay audio element
-  ``effect_tremelo.c/.h`` - A tremelo effect. This audio effect utilizes the amplitude_modulation audio element.
-  ``effect_tube_distortion.c/.h`` - A tube simulator distortion effect. This audio effect combines the biquad and clipper audio elements.

Finally, there is a set of functions that perform audio effect selection in a file called ``audio_effects_selector.cpp``. This provides a basic framework for switching between various effects on the fly similar to what you'd find in a multi-effects unit.

Installing the Audio Elements and Audio Effects
===============================================

.. important::

   This section can be skipped if you have installed the SHARC Audio Module Bare Metal SDK version 2.1.0 or greater.


Prior to the SHARC Audio Module Bare Metal SDK 2.1.0, the audio elements and audio effects are not part of the standard baremetal framework install. After you've created a new project with the New Project Wizard, follow the steps below to install and use these libraries:

-  Download the `audio_processing.zip <https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/audio_processing.zip>`_ and extract it into the project you just created with the New Project Wizard. You should now have a folder called ``audio_processing/`` in your project.

   -  Files from the zip ``common``' folder go into the ``common`` folder of your new project
   -  Files from the zip ``core0\src`` folder go into the ``<PROJECT_NAME>_core0\src`` folder of your new project
   -  Files from the zip ``core1\src`` folder go into the ``<PROJECT_NAME>_core1\src`` folder of your new project
   -  Files from the zip ``core2\src`` folder go into the ``<PROJECT_NAME>_core2\src`` folder of your new project

-  In each SHARC core in your CCES project, right click on the src/ directory in the project tree, and select New->Folder. Expand the Advanced options at the bottom of the New Folder dialog and select the third radio option, Link to an alternative location. In the text box immediately to the right, add ``PROJECT_LOC\..\audio_processing``. Do the same for SHARC Core 2. You should now have an audio_processing/ folder in each of your projects.

.. important::

   If you have copied all files over from the zip file attached then you do not need to do the rest of this section. If you would rather hand edit the files then the steps below detail how to do that.


-  Open up ``callback_audio_processing.cpp`` in each SHARC project and make the following modifications.

   -  In the include files at the top, add ``#include "audio_processing/audio_effects_selector.h"``.
   -  In the ``processaudio_setup()`` function add ``audio_effects_setup_core1();`` in core 1 and ``audio_effects_setup_core2();`` in core 2. The audio effect selector selects a different set of effects for each core. (Or, copy the file from the earlier referenced archive file to this directory)
   -  In the ``processaudio_callback(void)`` function, add the code block below to the top. This will optionally apply the selected effects at the front fo the audio callback on each core. Be sure to change ``audio_effects_process_audio_core1()`` to ``audio_effects_process_audio_core2()`` when you add this code to SHARC core 2. (Or, copy the file from the earlier referenced archive file to this directory)

.. code:: c

       if (true) {

           // Copy incoming audio buffers to the effects input buffers
           copy_buffer(audiochannel_0_left_in,  audio_effects_left_in, AUDIO_BLOCK_SIZE);
           copy_buffer(audiochannel_0_right_in, audio_effects_right_in, AUDIO_BLOCK_SIZE);

           // Process audio effects
           audio_effects_process_audio_core1();

           // Copy processed audio back to input buffers
           copy_buffer(audio_effects_left_out, audiochannel_0_left_in, AUDIO_BLOCK_SIZE);
           copy_buffer(audio_effects_right_out, audiochannel_0_right_in, AUDIO_BLOCK_SIZE);
       }

-  Next, open up ``src/common/multicore_shared_memory.h`` and add the following code anywhere in the C struct that is declared there. This will allow the ARM core, which current reads push button events, manage the effect preset we're on for each core. (Or, copy the file from the earlier referenced archive file to this directory)

.. code:: c

    // Effects processing presets
       uint32_t    effects_preset;
       uint32_t    reverb_preset;
       uint32_t    total_effects_presets;

-  On the ARM Core (core 0), open up ``src/startup_code_core0.cpp`` and add the following code after ``audio_framework_initialize()`` in ``main()`` to initialize the multicore presets. (Or, copy the file from the earlier referenced archive file to this directory)

.. code:: c

       // Initialize the effects presets
       multicore_data->total_effects_presets = 10;
       multicore_data->effects_preset = 0;
       multicore_data->reverb_preset = 0;

-  On the ARM Core (core 0), open up ``src/callback_pushbuttons.cpp``, Here we will modify the preset values when the buttons on the AUDIO_PROJECT fin are pressed. (Or, copy the file from the earlier referenced archive file to this directory)

In ``pushbutton_callback_external_1()`` add:

.. code:: c

       // Decrement our reverb effect
       multicore_data->reverb_preset--;
       if (multicore_data->reverb_preset >= multicore_data->total_effects_presets) {
           multicore_data->reverb_preset = multicore_data->total_effects_presets - 1;
       }

In ``pushbutton_callback_external_2()`` add:

.. code:: c

       // Increment our reverb effect
       multicore_data->reverb_preset++;
       if (multicore_data->reverb_preset >= multicore_data->total_effects_presets) {
           multicore_data->reverb_preset = 0;
       }

In ``pushbutton_callback_external_3()`` add:

.. code:: c

       // Decrement our current effect
       multicore_data->effects_preset--;
       if (multicore_data->effects_preset >= multicore_data->total_effects_presets) {
           multicore_data->effects_preset = multicore_data->total_effects_presets - 1;
       }

In ``pushbutton_callback_external_4()`` add:

.. code:: c

       // Increment our current effect
       multicore_data->effects_preset++;
       if (multicore_data->effects_preset >= multicore_data->total_effects_presets) {
           multicore_data->effects_preset = 0;
       }

Selecting Effects
=================

Once installed, the push buttons on the AUDIO PROJECT fin can be used to increment and decrement the audio effect running on core 1 and the reverb preset running on core 2. The pots on the AUDIO PROJECT fin control parameters for each effect. See ``src/audio_processing/audio_effects_selector.cpp`` for information on which pot control which parameter.

The first preset is bypass so when you run the code, initially, you will hear just clean, unprocessed audio. Press the switches to toggle between the various effects. Below is the list of effects implemented on core 1 that the push buttons will cycle through:

+------------------------+---------------------------------------------------------+
| PB Index (SW3 and SW4) | Effect                                                  |
+========================+=========================================================+
| 0                      | ``bypass``                                              |
+------------------------+---------------------------------------------------------+
| 1                      | ``digital delay``                                       |
+------------------------+---------------------------------------------------------+
| 2                      | ``multi-tap delay``                                     |
+------------------------+---------------------------------------------------------+
| 3                      | ``tube distortion emulation``                           |
+------------------------+---------------------------------------------------------+
| 4                      | ``multiband compressor``                                |
+------------------------+---------------------------------------------------------+
| 5                      | ``flanger``                                             |
+------------------------+---------------------------------------------------------+
| 6                      | ``guitar synth``                                        |
+------------------------+---------------------------------------------------------+
| 7                      | ``autowah``                                             |
+------------------------+---------------------------------------------------------+
| 8                      | ``simple multi-fx example (tube distortion + tremolo)`` |
+------------------------+---------------------------------------------------------+
| 9                      | ``ring modulator``                                      |
+------------------------+---------------------------------------------------------+

Programming with the Audio Elements and Audio Effects
=====================================================

The audio elements and audio effects are each implemented in a .c/.h file pair that can be called from C or C++. State information is stored in a C struct so you can instantiate as many instances as memory and processing power can support.

Each .c/.h file contains the following routines:

-  A **setup** routine to initialize an instance of the audio effect or audio element
-  One or more **modify** routines to change parameters of the audio effect or audio element
-  A **read** routine to process a block of data for the audio effect or audio element

A C struct holds the configuration and state information for each instance of the audio effect or audio element. Thus if you want to run the effect on two channels, you'd declare two instances of the struct.

See the tutorials that follow for examples of building and chaining various audio elements and audio effects.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#delay-effect-tutorial
   :alt: Delay Effect from Scratch#.|Bare Metal Framework#volume-control-tutorial|Programming a Volume Control
