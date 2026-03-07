Sharing Data Between Cores / System Telemetry
=============================================

.. image:: https://wiki.analog.com/_media/youtube>srVoSbo7zB4
   :alt: youtube>srVoSbo7zB4

All three processors have access to a block of shared L2 memory. The default Linker Description File (LDF) allocates a number of section for MCAPI but as the Bare Metal Framework does not rely on this heavier form of intra-core message passing, we can reuse this shared memory. There is one segment that all three cores are, by default, able to read from and write to which is located at address 0x20080000.

The Bare Metal Framework uses a C struct that is placed in this shared block of L2 memory which is declared in ``common/multicore_shared_memory.c`` and ``common/multicore_shared_memory.h``. The .h file contains the struct declaration and the .c file places this in the L2 segment that all three cores can access.

The memory segment containing the C struct is 4Kbytes so we can't store large buffers of audio. However, it is perfect for quickly and easily sharing parameters and telemetry data that all three cores can access from C.

the C struct declared in ``common/multicore_shared_memory.h`` is comprised predominantly of 32-bit data types. This is important to help guarantee proper atomic accesses between cores.

You can customize the structure and add additional variables. The example below shows how to read a value from the shared memory structure and how to write into the structure.

.. code:: c

       // Read from the shared memory structure
       uint32_t x = multicore_data->my_var_1;

       // Write to the shared memory structure
       multicore_data->my_var_2 = sinf(t);

There are a number of existing fields within this structure that are helpful as you develop and benchmark your audio algorithms.

\*\* Peak and current MHz loading for each core \*\*

Each SHARC core measures the current loading in MHz of the audio processing algorithms and the framework itself. These values are in MHz. If you audio processing is consuming 45.0MHz on SHARC Core 1, you're using roughly 10% of the processing available on that core.

Additionally, each SHARC core keeps track of how many audio frames it has dropped due to the audio callback consuming too many processor cycles. Note that this information is also sent to the event logging system.

.. code:: c

       // Examine these variables to understand MHz loading for each core
       float           sharc_core1_cpuload_mhz;
       float           sharc_core1_cpuload_mhz_peak;
       float           sharc_core2_cpuload_mhz;
       float           sharc_core2_cpuload_mhz_peak;
       
       uint32_t        sharc_core1_dropped_audio_frames;
       uint32_t        sharc_core2_dropped_audio_frames;    

All cores can read these fields. To read the current MHz loading of SHARC Core 2 on the ARM core, you can do something like this:

.. code:: c

    float core2_loading = multicore_data->sharc_core2_cpuload_mhz;

\*\* Access push buttons and Pots values (from Audio Project Fin) \*\*

The Audio Project Fin has 3 Pots and a number of additional push buttons. These can be accessed from both SHARC cores. There is a flag for each pushbutton for each SHARC core. This prevents one core from acknowledging a button event before the other core sees it.

.. code:: c


        **/
       #ifdef SAM_AUDIOPROJ_FIN_BOARD_PRESENT
           uint32_t audioproj_fin_sw_1_core1_pressed;
           uint32_t audioproj_fin_sw_2_core1_pressed;
           uint32_t audioproj_fin_sw_3_core1_pressed;
           uint32_t audioproj_fin_sw_4_core1_pressed;
           uint32_t audioproj_fin_sw_1_core2_pressed;
           uint32_t audioproj_fin_sw_2_core2_pressed;
           uint32_t audioproj_fin_sw_3_core2_pressed;
           uint32_t audioproj_fin_sw_4_core2_pressed;

           // These are the POTS on the Audio Project Fin
           float audioproj_fin_pot_hadc0;
           float audioproj_fin_pot_hadc1;
           float audioproj_fin_pot_hadc2;

           // And these are the additional HADC input channels available on the Audio Project headers
           float audioproj_fin_aux_hadc3;
           float audioproj_fin_aux_hadc4;
           float audioproj_fin_aux_hadc5;
           float audioproj_fin_aux_hadc6;

If you wanted to use the value of the Pot connected to HADC 0 on the Audio Project Fin for a delay algorithm running on SHARC Core 1, you could do the following:

.. code:: c


       float delay_feedback = multicore_data->audioproj_fin_pot_hadc0;
       float delay_feedthrough = multicore_data->audioproj_fin_pot_hadc1; 

And to use a button to toggle an effect when SW1/PB1 (Push Button) is pressed, you could do the following:

.. code:: c


       static bool delay_enabled;
       if (multicore_data->audioproj_fin_sw_1_core1_pressed) {
          delay_enabled = !delay_enabled;
          multicore_data->audioproj_fin_sw_1_core1_pressed = 0;
       }

The HADC values are updated by the ARM core once per millisecond in the millisecond tick interrupt service routine. The PB fields are updated in the interrupt service routine for the PBs in the ARM core.

If you want the ARM core to manage a user interface, this is a very easy way to get audio parameters to the SHARCs and it’s also an easy way for the ARM to read back values generated by the SHARC like signal levels.

.. tip::

   Tip: Add multicore_data to the expressions window in CCES. You can halt the ARM core and see the contents of the shared memory structure while the SHARC cores are running.


--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#audio-frameworks
   :alt: Selecting Between HW Platforms#.|Bare Metal Framework#peripheral-and-system-drivers|Using Peripheral and System Drivers
