Tutorial: Using MicroPython in Conjunction with Bare Metal Framework
====================================================================

MicroPython is only running on the ARM core, the code for the SHARC core needs to be built separately. This page discusses how to use the MicroPython in conjunction with SHARC Audio Module Bare Metal Framework to build a simple reverb effect processor and control the parameters from MicroPython.

This tutorial is based on the example from :doc:`Tutorial: Implementing a Basic Delay Effect </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/delay-effect-tutorial>`. This tutorial assumes you have read and understand that tutorial. However, the Audio Project Fin is not required to complete this tutorial.

Bare Metal Framework
--------------------

Normally, the bare metal framework runs on all three cores. If it needs to be used with MicroPython, some modification needs to be done to make it run on SHARC cores only.

SHARC only version
~~~~~~~~~~~~~~~~~~

In the current release of the SAM Bare Metal Framework (2.0.0), the SHARC only option does not exist. This page documents the process of modifying the framework to work on the SHARC core only.

This tutorial assumes:

-  The board being used is the SHARC Audio Module main board, either without any expansion fin, or with the Audio Project Fin.
-  CCES 2.8.0 or newer and SAM BM Framework 2.0.0 are installed.
-  An empty BM framework base project has been created using the Bare Metal Project Wizard in the CCES.
-  "core0", "core1", and "core2" refer to the 3 projects automatically generated. They usually have your own project name as prefix.
-  This tutorial contains many line number references that may be outdated.

Framework initialization
^^^^^^^^^^^^^^^^^^^^^^^^

Normally, codec initialization is done in the ARM core, now they need to be done by the SHARC core.

-  Copy the file ``audio_framework_8ch_sam_and_audioproj_fin_arm.c`` from ``core0/src/audio_frameworks`` to ``core1/src/audio_frameworks``. This file should show up in the core1 project in the CCES window. If not, try refreshing the project (F12).
-  Open the the file that has just been copied. Make sure you open the copy in the core1 project.
-  On line 28, change include file to ``#include "audio_framework_8ch_sam_and_audioproj_fin_core1.h"``
-  On line 197, delete or comment out the call to event logging function as it no longer exists in core 1.
-  On line 207, change the function name to ``void audioframework_initialize_core0(void)`` to avoid conflict.
-  On line 243, delete or comment out the function that sets the 1ms callback to avoid conflict.
-  Open the file ``audio_framework_8ch_sam_and_audioproj_fin_core1.h`` (in core1 project).
-  From ``audio_framework_8ch_sam_and_audioproj_fin_arm.h`` (in core0 project), copy contents from line 53 to line 72 (HADC definitions). Paste them to line 59 (before the ``#endif for _AUDIOPROJ_DAUGHTER_BOARD_``)
-  At line 193 of ``audio_framework_8ch_sam_and_audioproj_fin_core1.h`` (near the end of file, before ``#ifdef __cplusplus``), add the function prototype for timer tick callback function: ``void ms_tick_event_callback(void);``
-  Right after the previous definition, add the function prototype for initialization function: ``void audioframework_initialize_core0(void);``

MIDI callback
^^^^^^^^^^^^^

MIDI is by default managed by the SHARC core (as in line 179-180 of ``common/audio_system_config.h``). However, the pinmux of UART1 (used by MIDI) is normally done by ARM. Now it should be done by SHARC.

Open ``callback_midi_message.cpp`` in core 1 project, add below to line 25 (after the last #include):

.. code:: c

   #define UART1_RX_PORTB_MUX ((uint16_t) ((uint16_t) 1<<6))
   #define UART1_TX_PORTB_MUX ((uint16_t) ((uint16_t) 1<<4))

   #define UART1_RX_PORTB_FER ((uint16_t) ((uint16_t) 1<<3))
   #define UART1_TX_PORTB_FER ((uint16_t) ((uint16_t) 1<<2))

In midi_setup_sharc1 function, add below to the beginning of function:

.. code:: c

   *pREG_PORTB_MUX = UART1_RX_PORTB_MUX | UART1_TX_PORTB_MUX;
   *pREG_PORTB_FER = UART1_RX_PORTB_FER | UART1_TX_PORTB_FER;

Now the MIDI should work fine.

Push button callback
^^^^^^^^^^^^^^^^^^^^

Push button callback is normally handled by the ARM core, and need to be moved to the SHARC core. (Note this might not be necessary if user want to use the push button on the ARM side, outside of the BM framework.)

To move it to the sharc core, simply copy ``callback_pushbuttons.cpp`` and ``callback_pushbuttons.h`` from core0/src to core1/src. Make sure the CCES detected the new file.

Disable logging support
^^^^^^^^^^^^^^^^^^^^^^^

Since ARM will have the control of the UART0, logging via UART will no longer be possible. Logging support need to be disabled.

In the ``drivers/bm_event_logging_driver.c``, comment out (or delete) content inside log_event function(line 549), ``event_logging_initialize_sharc_core`` function (line 586), and ``event_logging_process_queue_sharc_core`` function (line 611). Codes that are specific to ARM core doesn't need to be touched, as they will not be compiled.

Add missing driver to Core1
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normally, only a selection of BM drivers are included in core1 the source tree. Interface drivers like TWI has been omitted. They need to be added back.

-  Remove the drivers folder inside the src folder in the core1 project: right click on the drivers folder, select "Delete" in the popup menu. Click OK to confirm. (It will warning the files will be deleted from the file system, it is fine as it is an empty folder in the file system.)
-  Add the link to the real drivers folder into the src folder: right click on the src folder, select "New → Folder."
-  In the popup window, click "Advanced >>"
-  Select "Link to alternate location (Linked Folder)", and type in ``PROJECT_LOC/../drivers``, the "Folder name" should be automatically filled with "drivers"
-  Click finish

This should add all available drivers to the core1 project. This need to be done for core 1 only.

Core1 start-up process
^^^^^^^^^^^^^^^^^^^^^^

Now everything should be moved to core1, some modification to the core 1 startup process is required.

-  Open ``startup_code_core1.cpp``
-  Change both falsies in line 87 and 88 to true. (Now, core 1 will initialize the system clocks and control the HADC.)
-  Between line 107 and 108, insert a call to ``audioframework_initialize_core0()``, before the original call to initialize function.
-  In ``timer_tick_callback`` function (line 47), add a call to ``ms_tick_event_callback()``, this function handles the HADC reading.

Remove things in the ARM core code (optional, for debugging with emulator)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SHARC cores need to be enabled by the ARM core to run. If one want to debug the SHARC only application with emulator, the ARM core code is still required to just enable the SHARC cores. Open the ``startup_code_core0.c`` file in the core0 project, find the main function, delete everything except calling the adi_initComponents and enabling the cores. It should look like this:

.. code:: c

   int main(int argc, const char *argv[]) {
       adi_initComponents();
       adi_core_enable(ADI_CORE_SHARC0);
       adi_core_enable(ADI_CORE_SHARC1);
       while (1);
   }

Optionally, remove all unrelated files.

Configure the IDE to generate LDR file only for SHARC cores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   You would need to build the project at least once before continue on.


-  Right click on the core1 project, select Properties.
-  Navigate to "C/C++ Build → Settings"
-  In the "Build Artifact" tab, set "Artifact Type" to be "Loader File"
-  In the "Tools Settings" tab, go to "CrossCore SHARC Loader → Executable Files", set executable file for Core1 and Core2, leave executable blank for Core0. Check "Append core input without introducing a FINAL block" for Core 1, uncheck for other two.
-  Go to "CrossCore SHARC Loader → General", set "Boot format" to be "Binary", set "Boot code" to be 0x1.
-  You may want to also set ``-MaxBlockSize 2048`` in "CrossCore SHARC Loader → Additional Options".
-  Rebuild and the loader file should be ready.

Building the demo
~~~~~~~~~~~~~~~~~

After making the changes, follow the tutorial at :doc:`Tutorial: Implementing a Basic Delay Effect </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/delay-effect-tutorial>` to create a reverb effect in the SHARC only version of framework.

.. note::

   It's a good idea to test if the effect is working or not using the debugger first.


Export variables
~~~~~~~~~~~~~~~~

In the tutorial, all the parameters for the reverb effect is controlled using keys and potentiometers. In this tutorial, they would be instead controller from the MicroPython. So they need to be exported to somewhere the ARM core can access. In the BM framework, the multicore_data variable is designed to do this, and it is located inside ``common/multicore_shared_memory.c`` and its header file.

The reverb effect is controlled by 3 parameters: mix ratio, delay feedback, and length. Start by defining these three variables in ``the multicore_shared_memory.h``:

Add these three lines after ``float *sharc_core2_audio_out;`` (line 105) and before ``uint32_t sharc_core_new_message_ready;`` (line 108):

.. code:: c

   float delay_mix;
   float delay_feedback;
   float delay_length;

Unfortunately, as this file would not be seen by the Python, the Python would have no idea where each variable will be located exactly. So it is necessary to count the offset address of these three variables and write them in the Python environment later. (Though it should not be hard to write a Python script to actually parse this file.) All float and uint32_t variable occupy 4 bytes, and the first variable starts at offset 0. So for example, in the code below:

.. code:: c

   typedef struct
   {

       // Status of system initialization
       uint32_t arm_audio_peripheral_initialization_complete;
       uint32_t sharc_core1_ready_for_audio;
       uint32_t sharc_core1_processing_audio;

These three variable will have offset of 0, 4, and 8 bytes respectively.

Currently, if you are using the Rel 2.0.0 version of SDK and put the variable at the exact place described before, variables that control the reverb effect should be at offset 172, 176, and 180 respectively. Note this should not change whether the audio project fin support is enabled or not.

Next step would be modify the audio callback function to make it read the parameters from the shared variable, rather than potentiometer.

Open ``callback_audio_processing.cpp``, add the following code to the end of ``void processaudio_callback(void)`` function:

.. code:: c

       if (abs(multicore_data->delay_length - delay_len_seconds) > 0.04) {
           delay_len_seconds = multicore_data->delay_length;
           delay_len_samples = (uint32_t)(delay_len_seconds * (float)AUDIO_SAMPLE_RATE);
       }

       delay_wet_mix = multicore_data->delay_mix;
       delay_dry_mix = 1.0 - multicore_data->delay_mix;
       delay_feedback = multicore_data->delay_feedback;

Now build the project into a binary LDR file. (refer to the SHARC only version section) Put the LDR file on a SD card formatted to FAT or FAT32 filesystem.

Python side
-----------

At the Python side, we need to first load the LDR file, use that to bootstrap the SHARC core, and second setting up the environment to allow read and write shared variables.

Assume the LDR file is called reverb.ldr and is in the SD card's root directory, write a Python script with the content below:

.. code:: python

   import sharc

   # load the sharc program to run
   f = open('delay.ldr', 'rb')
   stream = f.read()
   sharc.boot(stream)
   f.close()

   print("Delay effect is loaded and running.")

These code would open the loader file and bootstrap the SHARC core.

Then we need to tell the Python where is the shared variables. Add the code blow to the script:

.. code:: python

   import uctypes

   # initialize the parameters
   sharc_data_struct = {
       "core1_load": uctypes.FLOAT32 | 36,
       "core1_load_peak": uctypes.FLOAT32 | 40,
       "core2_load": uctypes.FLOAT32 | 44,
       "core2_load_peak": uctypes.FLOAT32 | 48,
       "delay_mix": uctypes.FLOAT32 | 172,
       "delay_feedback": uctypes.FLOAT32 | 176,
       "delay_length": uctypes.FLOAT32 | 180
   }

   sharc_data = uctypes.struct(0x20080000, sharc_data_struct)

   sharc_data.delay_mix = 0.5
   sharc_data.delay_feedback = 0.5
   sharc_data.delay_length = 0.25

   print("Use \'sharc_data.delay_mix\', \'sharc_data.delay_feedback\', and\'sharc_data.delay_length\' to adjust the parameters.")

Note how the offset we counted before is defined here. For more information, please read MicroPython's documentation about uctypes: https://docs.micropython.org/en/latest/library/uctypes.html

Save the script as delay_setup.py, and put it at the root directory of the SD card.

Inside the MicroPython REPL (console), type in:

.. code:: python

   execfile('delay.py')

It should boot up the SHARC core and setup the variable mapping. Try use ``print(sharc_data.core1_load)`` to view the load, and use ``sharc_data.delay_mix = 0.8`` to change the parameters.

It is also easy to write a simple user interface to control the parameter with arrow keys within python like this example:

.. code:: python

   import sys

   current_selection = 0
   options = ["Mix      ", "Feedback ", "Length   "]
   values = [0.5, 0.5, 0.5]

   def print_ui():
       print("\033c")
       for i in range(3):
           if (i == current_selection):
               print(" >", end =" ")
           else:
               print("  ", end =" ")
           print(options[i], end =": ")
           print("%.2f" % abs(values[i])) # abs to avoid -0.00

   def update_changes():
       sharc_data.delay_mix = values[0]
       sharc_data.delay_feedback = values[1]
       sharc_data.delay_length = values[2]

   # main function start here
   while True:
       print_ui()
       k = sys.stdin.read(3)
       if k=='\x1b[A':
           # up
           if current_selection > 0:
               current_selection = current_selection - 1
       elif k=='\x1b[B':
           if current_selection < 2:
               current_selection = current_selection + 1
       elif k=='\x1b[C':
           if values[current_selection] < 0.96:
               values[current_selection] = values[current_selection] + 0.05
               update_changes()
       elif k=='\x1b[D':
           if values[current_selection] > 0.04:
               values[current_selection] = values[current_selection] - 0.05
               update_changes()
       else:
           break

Save the code inside the SD card, and run the code using ``execfile`` as before. You should be able to control the effect from the console.

--------------

`Using Hardware Peripherals#..micropython|MicroPython Overview#.building|Building MicroPython with CCES <https://wiki.analog.com/_media/navigation SHARC Audio Module#.peripherals>`_
