Using a MATLAB Volume Control Function in the Framework
=======================================================

MATLAB gives users the ability to create powerful audio algorithms. This tutorial gives an overview of how to create a simple volume control function and then add it to the baremetal framework.

.. important::

   All MATLAB work was using version R2018b


Creating a Function in MATLAB
-----------------------------

From the **Home** tab choose **New::Function** and then overwrite all template contents with the following:

::

   function audio_out = volume_control( audio_in, vol_ctrl_factor )
   %increase/decrease the gain by using vol_ctrl_factor
   %   takes input channel and multiplies by a factor vol_ctrl_factor and stores in
   %   the output channel

   audio_out = audio_in * vol_ctrl_factor;

   end

This function takes an input audio channel, multiplies it by vol_ctrl_factor and stores the result in the output audio channel. It simply changes the volume. Notice that we don't use a for loop because MATLAB has built in implicit expansion for scalar \* vector multiplication. The file name should match the function name so name the file volume_control.

Testing the Newly Created Function in MATLAB
--------------------------------------------

In order for MATLAB Coder to know what the input variable types are and to verify the function is working properly, a test script needs to be created. From the **Home** tab choose **New::Script** and copy the following contents into the window:

::

   AUDIO_BLOCK_SIZE = int32(32);

   audio_in = ones(AUDIO_BLOCK_SIZE,1);

   vol_ctrl = single(0.5);

   volume_control(single(audio_in), vol_ctrl);

Generating C Code with MATLAB Coder
-----------------------------------

.. important::

   This page assumes that users have already gone through the :doc:`Getting Started and Support </wiki-migration/resources/tools-software/sharc-audio-module/gettingstarted>` and :doc:`Bare Metal Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` content.


Selecting the Function
~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/matlab_select_func.gif

-  From the **APPS** tab, choose MATLAB Coder.
-  In the Generate code for function section, choose the function that we created by either typing it in or clicking the "..." and searching for it.
-  Click Next

Defining the Input Types
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/matlab_define_type.gif

-  On the **Define Input Types** page, choose the test script that we created earlier
-  Click **Autodefine Input Types**, then click Next
-  Click **Check for Issues** to verify there are no issues
-  Click Next

Check for Run-Time Issues
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/matlab_runtime.gif

-  Now the code can be generated
-  **Build type** should be set to **Source Code**
-  **Language** should be **C plus plus**\ \*
-  Change **Hardware Board** to **None - Select device below**
-  **Device vendor** should be **Analog Devices**
-  **Device type** should be **SHARC**
-  Click **Generate**

Generate Code
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/matlab_generate_code.gif

Adding the Code to the Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we have our C++ function ready to add to the framework. There are multiple ways to do this but the easiest in this case is to just add the function to callback_audio_processing.cpp. Using the SHARC Audio Module Bare Metal Project wizard, users should choose all default options **with the addition of selecting the Audio Project Fin**.

-  Once the projects are created in CCES, open the callback_audio_processing.cpp file for core 1.
-  Copy the generated code from MATLAB Coder and paste it at the top of callback_audio_processing.cpp.

::

   /* Function Definitions */
   void volume_control(const float audio_in[32], float vol_ctrl_factor, float
                       audio_out[32])
   {
     int i;

     /* increase/decrease the gain by using vol_ctrl_factor */
     /*    takes input channel and multiplies by a factor vol_ctrl_factor and stores in */
     /*    the output channel */
     for (i = 0; i < 32; i++) {
       audio_out[i] = audio_in[i] * vol_ctrl_factor;
     }
   }

-  Remove or comment out all code currently in processaudio_callback(void) so that we can add our new code that will allow us to control the volume from HADC0 of the Audio Project Fin.
-  Copy the following code into processaudio_callback()

::

       float pot0_val = multicore_data->audioproj_fin_pot_hadc0;

       volume_control(audiochannel_0_left_in, pot0_val, audiochannel_0_left_out);
       volume_control(audiochannel_0_right_in, pot0_val, audiochannel_0_right_out);

The code will read the value of HADC0 and pass that into the volume_control() function created from MATLAB Coder to allow the volume to be adjusted.

Hardware Setup
^^^^^^^^^^^^^^

-  Attach the Audio Project Fin to the SHARC Audio Module main board
-  Connect a 1/8 inch stereo cable from an audio source to **LINE IN(J1)** of the SHARC Audio Module
-  Connect a 1/8 inch stereo cable from **LINE OUT(J2)** of the SHARC audio Module to some headphones or speakers
-  Attach the 12v power source to the SHARC Audio Module

Build and Run the Code in CCES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point it is assumed that users are familiar with using the framework in CCES. Build and run the code in CCES and notice that turning HADC0 will increase or decrease the volume.
