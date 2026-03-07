Tutorial: Basic Volume Control
==============================

Bare Metal Project Wizard Setup
-------------------------------

Using the :doc:`bare metal project wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`:

-  Give the project a meaningful name, click Next
-  Choose the Audio Project Fin on the Expansion Fin Selection Page because it is required for part of the tutorial, click Finish

**No other options need to be changed.**

Tutorial Overview
-----------------

In this tutorial, we will implement a basic volume control effect.

Changing the volume or amplitude of the audio signal passing through the SHARC Audio Module requires us to simply multiply each sample by a constant value. If that value is between 0.0 and 1.0, the volume will be decreased, or "attenuated". If the value is greater than 1.0, the volume will be increased, or "amplified".

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/volume_control_effect.png
   :align: center
   :width: 400px

Attenuating an Audio Signal using POTs on the Audio Project Fin
---------------------------------------------------------------

In this tutorial, we'll implement a stereo volume control function that will use the POTs on the Audio Project fin to control the left and right gain of the audio arriving at the 1/8" audio input jack on the SHARC Audio Module and the 1/4" audio input jack on the Audio Project fin. The output will be passed to the 1/8" output jack on the SHARC Audio Module, the 1/4" audio output jack on the Audio Project fin, and S/PDIF out.

For this tutorial, we'll use an audio element called the "clickless volume control" which can be found in ``src/audio_processing/audio_elements/clickless_vol_ctrl.c/.h``. This element will change the gain of an incoming audio signal by an arbitrary value. It also supports "clickless" gain adjustment. This means that if the gain is changed to a new value, the function will slew the gain over the course of several samples to the new value. You can change the slew rate of the volume using the ``VOLUME_CTRL_TRANSITION_SPEED`` constants defined in ``clickless_vol_ctrl.h``. This is an argument in the ``volume_control_set_gain()`` function as shown below.

Open up the file ``src/callback_audio_processing.cpp`` in the ``<PROJECT_NAME>_core1`` project and locate the ``processaudio_setup()`` and ``processaudio_callback()`` functions. The setup function is called when the system is initialized and is where we'll set up our volume control function. And the processaudio_callback is called each time a new block of audio is ready for us to process. This is where we'll apply the volume control.

Prior to the setup function, we'll need to declare two instances of the clickless volume control (one for left channel and one for right channel). And in ``processaudio_setup()``, we'll initialize the two instances using the current POT values as their initial gain values.

.. code:: c


   // Instances of the clickless audio volume control
   VOLUME_CTRL     vol_ctrl_l, vol_ctrl_r;

   /*
     * Place any initialization code here for the audio processing
    */
   void processaudio_setup(void) {

       // *******************************************************************************
       // Add any custom setup code here
       // *******************************************************************************
       volume_control_setup(&vol_ctrl_l, multicore_data->audioproj_fin_pot_hadc0);
       volume_control_setup(&vol_ctrl_r, multicore_data->audioproj_fin_pot_hadc1);

   }

Then, we'll replace the contents of the ``processaudio_callback()`` function with the following code:

.. code:: c

       // Apply gain control effect to incoming left and right audio streams
       volume_control_read(&vol_ctrl_l,
                           audiochannel_0_left_in,
                           audiochannel_0_left_out,
                           AUDIO_BLOCK_SIZE);
       volume_control_read(&vol_ctrl_r,
                           audiochannel_0_right_in,
                           audiochannel_0_right_out,
                           AUDIO_BLOCK_SIZE);

       // Update the gain values based on the current values of the Pots
       volume_control_set_gain(&vol_ctrl_l, multicore_data->audioproj_fin_pot_hadc0, VOLUME_TRANSITION_FAST);
       volume_control_set_gain(&vol_ctrl_r, multicore_data->audioproj_fin_pot_hadc1, VOLUME_TRANSITION_FAST);

Attenuating and Amplifying Audio using POTs on the Audio Project Fin
--------------------------------------------------------------------

Thus far, we have only attenuated the audio. However, in this example, we'll have the gain be set to 1.0 when the pots are in the middle position. And when the pots are turned all the way to the right, we'll set the gain to 2.0. And when the pots are turned all the way to the left, we'll set the gain to zero.

The pots values range from 0.0 (full left) to 1.0 (full right) so in essence we just need to multiply the pot values by 2.0.

In our setup code, we'll multiply the value of the current pots by 2.0...

.. code:: c


   // Instances of the clickless audio volume control
   VOLUME_CTRL     vol_ctrl_l, vol_ctrl_r;

   /*
     * Place any initialization code here for the audio processing
    */
   void processaudio_setup(void) {

       // *******************************************************************************
       // Add any custom setup code here
       // *******************************************************************************


       volume_control_setup(&vol_ctrl_l, multicore_data->audioproj_fin_pot_hadc0 * 2.0);
       volume_control_setup(&vol_ctrl_r, multicore_data->audioproj_fin_pot_hadc1 * 2.0);

   }

And we'll make the same modification to our audio callback...

.. code:: c

       // Apply gain control effect to incoming left and right audio streams
       volume_control_read(&vol_ctrl_l,
                           audiochannel_0_left_in,
                           audiochannel_0_left_out,
                           AUDIO_BLOCK_SIZE);
       volume_control_read(&vol_ctrl_r,
                           audiochannel_0_right_in,
                           audiochannel_0_right_out,
                           AUDIO_BLOCK_SIZE);

       // Update the gain values based on the current values of the Pots
       volume_control_set_gain(&vol_ctrl_l, multicore_data->audioproj_fin_pot_hadc0 * 2.0, VOLUME_TRANSITION_FAST);
       volume_control_set_gain(&vol_ctrl_r, multicore_data->audioproj_fin_pot_hadc1 * 2.0, VOLUME_TRANSITION_FAST);

Other Fun Things to Try
-----------------------

-  Move the audio processing to the second SHARC core by making the changes to the same file in the ``<PROJECT_NAME>_core2`` project rather than the ``<PROJECT_NAME>_core1`` project.
-  Use a third pot to control the left-right balance of the signal
-  Create a phase shift effect on one channel by multiplying it by a negated value of volume_level

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#audio-elements
   :alt: "Audio Elements" and "Audio Effects"#.|Bare Metal Framework#chaining-audio-elements|Chaining Elements and Effects
