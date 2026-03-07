Porting MATLAB Coder Pitch Shift to SHARC Audio Module
======================================================

Many customers utilize MATLAB to create custom audio effects and algorithms. This example will help customers go from concept to an actual product using the SHARC Audio Module. The PitchShifter Audio Plugin from MATLAB will be used for this example.

Tuning the Algorithm in MATLAB
------------------------------

First, start audioTestBench in the MATLAB command window

.. code:: c

   >> audioTestBench(audiopluginexample.PitchShifter) 

-  Choose the input audio file
-  Make sure to output to the correct output source such as PC speakers
-  Run the Audio Test Bench
-  Change the parameters to see how the algorithm performs

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/tuning.png
   :width: 600px

Creating the Function to Apply the Pitch Shift
----------------------------------------------

Although PitchShifter is one of the MATLAB Audio Plugin Examples, a function needs to be created that exercises the audiopluginexample.PitchShifter.

.. code:: c

   function y = applyPitchShift(PitchShift,Overlap,x)
       persistent h
       
       if isempty(h)    
           h = audiopluginexample.PitchShifter;  
       end
       
       % Exercise parameter tuning
       h.PitchShift = PitchShift;
       h.Overlap = Overlap; 

       % Exercise process function
       y = h(x);    
   end

Testing the Function in MATLAB
------------------------------

MATLAB will need a test for the function that was created to verify parameters.

.. code:: c


   AUDIO_BLOCK_SIZE = int32(32);
   audio_in = double(ones(AUDIO_BLOCK_SIZE,1));
   pitchShift = double(0);
   overLap = double(0);
   applyPitchShift(pitchShift, overLap, audio_in);   % PitchShift Audio

Using MATLAB Coder
------------------

MATLAB Coder will create code that can then be used in the SHARC Audio Module Bare Metal Framework

Select Function
~~~~~~~~~~~~~~~

Browse to where the Pitch Shift function is stored.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/select_func.png
   :width: 700px

Define Input Types
~~~~~~~~~~~~~~~~~~

Manually defining the input values can be done but pointing to the test function that was created already has them defined properly.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/define_input.png
   :width: 700px

Check For Issues
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/check_issues.png
   :width: 700px

Generate Code
~~~~~~~~~~~~~

-  Choose *Source Code* as the **Build Type**
-  Choose *C++* as the **Language**
-  Selecting **Hardware Board** *None* will give the ability to choose the *Analog Devices SHARC Device*
-  **More Settings** will be needed in this case

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/gen_code1.png
   :width: 700px

Adjust Settings
~~~~~~~~~~~~~~~

-  Choose **All Settings**
-  The bare metal framework processes the left and right channel separately so we need to make sure the function is re-entrant.
-  Make sure **Generate re-entrant code** is set to *yes*

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/gen_code2.png
   :width: 700px

.. _generate-code-1:

Generate Code
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/generate_code.png
   :width: 700px

--------------

Running the Pitch Shift Code in CrossCore Embedded Studio
---------------------------------------------------------

This section will describe all steps to run the pitch shift algorithm in CCES.

Create Project in CrossCore Embedded Studio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the Bare Metal Project Wizard to create a project that the MATLAB generated code can be integrated into. Using all the default settings in the wizard will create a working 3 core project.

.. tip::

   Reference the :doc:`Bare Metal Project Wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>` page for help creating a project.


Integrate MATLAB Code Into a Bare Metal Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Browse on the PC to ..\\MATLAB\\codegen\\lib to find the MATLAB project for the code being integrated
-  On the PC, create a matlab folder in the CCES pitchshifter project under **core 1**

   -  ..\\pitch_shifter\\pitch_shifter_core1\\src\\matlab
   -  CCES will automatically update to show this folder in its Project Explorer

-  Copy all files(excluding folders) from under applyPitchShift into the matlab folder

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/integrating_code.jpg
   :width: 800px

Updating callback_audio_processing.cpp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  All code changes will be in callback_audio_processing.cpp for core 1
-  Use main.cpp in the MATLAB generated code as reference code showing how to setup and call the pitch shift algorithm.

   -  .. \\MATLAB\\codegen\\lib\\applyPitchShift\\examples\\main.cpp

Adding includes to callback_audio_processing.cpp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

   #include "matlab/applyPitchShift.h"
   #include "matlab/applyPitchShift_initialize.h"

processaudio_setup(void) changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Reentrant memory structures will be needed for both left and right channels
-  Define static variables and then add the code to processaudio_setup()

.. code:: c

   /* Variable Definitions */
   static applyPitchShiftStackData applyPitchShiftStackDataGlobal1;
   static applyPitchShiftPersistentData c_applyPitchShiftPersistentData1;
   static applyPitchShiftStackData applyPitchShiftStackDataGlobal2;
   static applyPitchShiftPersistentData c_applyPitchShiftPersistentData2;

.. code:: c

   void processaudio_setup(void) {
       // Initialize the audio effects in the audio_processing/ folder
       audio_effects_setup_core1();
       // ******************************************************************
       // Add any custom setup code here
       // ******************************************************************
       /* Initialize reentrant memory structures */
       applyPitchShiftStackDataGlobal1.pd = &c_applyPitchShiftPersistentData1;
       /* Initialize the application.
          You do not need to do this more than one time. */
       applyPitchShift_initialize(&applyPitchShiftStackDataGlobal1);
       /* Initialize reentrant memory structures */
       applyPitchShiftStackDataGlobal2.pd = &c_applyPitchShiftPersistentData2;
       /* Initialize the application.
          You do not need to do this more than one time. */
       applyPitchShift_initialize(&applyPitchShiftStackDataGlobal2);
   }

processaudio_callback(void) changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update processaudio_callback() for core 1 to apply the pitch shift

-  Delete the current contents of the callback on core 1
-  Replace the contents with the code below

.. code:: c

   void processaudio_callback(void) {
       double pitch_shift = 3;
       double overlap = 0.2;
       double temp_right_in[AUDIO_BLOCK_SIZE];
       double temp_left_in[AUDIO_BLOCK_SIZE];
       double temp_right_out[AUDIO_BLOCK_SIZE];
       double temp_left_out[AUDIO_BLOCK_SIZE];
       int i = 0;

       // applyPitchShift expects a double[] so create temporary buffers to hold doubles
       for (i = 0; i < AUDIO_BLOCK_SIZE; i+=1) {
           temp_right_in[i] = (double)audiochannel_0_right_in[i];
           temp_left_in[i] = (double)audiochannel_0_left_in[i];
       }

       applyPitchShift(&applyPitchShiftStackDataGlobal1, pitch_shift, overlap, temp_right_in, temp_right_out);
       applyPitchShift(&applyPitchShiftStackDataGlobal2, pitch_shift, overlap, temp_left_in, temp_left_out);

       // applyPitchShift expects a double[] so convert back to float
       for (i = 0; i < AUDIO_BLOCK_SIZE; i+=1) {
           audiochannel_0_right_out[i] = (float)temp_right_out[i];
           audiochannel_0_left_out[i] = (float)temp_left_out[i];
       }
   }

Hardware Connections
~~~~~~~~~~~~~~~~~~~~

Before executing the application in CCES, the hardware should be setup as shown below in order for correct execution of the application.

.. tip::

   Revision 1.5 and greater of the SHARC Audio Module board does not use the FTDI cable. The circuit has been added to the board. A USB cable should be plugged into USB/UART(P6) instead of the FTDI cable connection shown.


.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/hw_setup.png
   :width: 800px

Executing the Code in CCES
~~~~~~~~~~~~~~~~~~~~~~~~~~

|

.. tip::

   Some knowledge of CrossCore Embedded Studio(CCES) is assumed here. If unfamiliar with CCES, please go through the :doc:`CCES Getting Started Guide </wiki-migration/resources/tools-software/crosscore/cces/getting-started>` prior to working in CCES.


   |image1|

-  Build all 3 core projects
-  Create the debug configuration to load all 3 cores using the ICE-1000
-  After creating the debug configuration, click Debug
-  Core 0 needs to run first to release the 2 SHARC cores so that they run to main
-  Once the SHARC cores are at main, run both cores
-  Be sure you have audio input to the board
-  You should hear audio a few octaves higher than expected


--------------

Optimizing the Pitch Shift Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| By default the optimizer in CCES is not enabled for the new matlab code.
|

.. container:: left

   \ |image2|\


-  Right click on the matlab folder.
-  Go to Properties::C/C+ + Build::Settings.
-  Under the Compiler section in the Tools Settings tab, select General.
-  Check Enable optimization
-  Rebuild and run the application


--------------

Verifying Optimization with Logging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the FTDI cable(Rev 1.4 boards) or a USB cable(Rev 1.5 boards), logging output can be seen when running the bare metal framework. Opening a console application, such as PuTTY, with the following serial settings should show the logging information.

Serial Settings
"""""""""""""""

-  115200 baud
-  8 Data bits
-  1 Stop bits
-  No parity
-  XON/XOFF flow control

| 

============= =========
Non-Optimized Optimized
============= =========
|image3|      |image4|
============= =========

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/debug_config.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/optimize_folder.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/debug_not_optimized.png
   :width: 700px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/debug_optimized.png
   :width: 700px
