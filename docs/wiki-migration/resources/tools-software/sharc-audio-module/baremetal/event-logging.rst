Event Logging
=============

The Bare Metal framework includes an event logging system that is more suitable for real-time telemetry. The event logging system stores time stamped events from all three cores in a single, circular buffer on the ARM core. These events are also sent to the UART and can be accessed via a simple USB-to-UART device connected to connector P8 on the SHARC Audio Module.

Event logging is provided via the bm_event_logging.c/.h file pair. The system uses a few locations in shared L2 memory to pass messages from the SHARC cores to the ARM core. This file pair is designed to be portable and can be used outside of the baremetal framework.

Configuring Event Logging
-------------------------

Configuring Event Logging on the ARM Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below configures the event logging system on the ARM core.

The ``event_logging_initialize_arm`` function takes pointers to locations in shared memory which will be used to receive messages from the two SHARC cores. Within the Bare Metal framework, we'll place a few variables in our multicore memory structure to support this functionality. However, outside of the framework, these can point to any locations in shared memory. This function also takes the core clock frequency of the ADSP-SC589 as an argument which will be used to calculate time stamps.

The ``event_logging_connect_uart`` function will configure the event logging system to send all events to the UART (P8 connector on SHARC Audio Module) and configure the UART for 115200 BAUD and 8N1 (no hardware flow control is used).

Finally, the ``event_logging_set_error_callback`` allows us to provide a callback when an ERROR or FATAL event is logged.

.. code:: c

       // Initialize event log
       event_logging_initialize_arm(   (char*)     &multicore_data->sharc_core1_event_message,
                                       (char*)     &multicore_data->sharc_core2_event_message,
                                       (uint32_t*) &multicore_data->sharc_core1_event_emuclk,
                                       (uint32_t*) &multicore_data->sharc_core2_event_emuclk,
                                       (uint32_t*) &multicore_data->sharc_core1_event_emuclk2,
                                       (uint32_t*) &multicore_data->sharc_core2_event_emuclk2,
                                       (uint32_t*) &multicore_data->sharc_core1_event_level,
                                       (uint32_t*) &multicore_data->sharc_core2_event_level,
                                       (uint32_t*) &multicore_data->sharc_core1_new_message_ready,
                                       (uint32_t*) &multicore_data->sharc_core2_new_message_ready,
                                       (float) CORE_CLOCK_FREQ_HZ );

       // Send logged events to UART0 (p8 connector on the SHARC Audio Module)
       event_logging_connect_uart(     UART_BAUD_RATE_115200,
                                       UART_SERIAL_8N1,
                                       UART_SAM_DEVICE_FTDI );

       // Set a callback for our fatal and error messages
       event_logging_set_error_callback( event_logging_error_callback );

Configuring Event Logging on the SHARC Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Event logging is configured in a similar manner on each SHARC core. The ``event_logging_initialize_sharc_core`` function takes pointers into shared memory as arguments. As mentioned above, we're using the shared multicore memory structure for this within the framework but these can be arbitrary 32-bit locations in shared L2 memory.

.. code:: c


       // Set up event logging
       event_logging_initialize_sharc_core(    (char *) multicore_data->sharc_core1_event_message,
                                               (uint32_t *) &multicore_data->sharc_core1_event_emuclk,
                                               (uint32_t *) &multicore_data->sharc_core1_event_emuclk2,
                                               (uint32_t *) &multicore_data->sharc_core1_event_level,
                                               (uint32_t *) &multicore_data->sharc_core1_new_message_ready);

Servicing the event logger
--------------------------

A service routine is provided for both ARM and SHARC cores which should be periodically called to process new events. The Bare Metal framework currently uses a 1ms timer interrupt on all three cores.

Servicing the Event Logger on the ARM Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below shows a 1ms timer tick that is enabled by default on the ARM core. Within the audio_framework code, we have a callback to the 1ms tick event and within this, we are servicing the event logging system via the ``event_logging_poll_sharc_cores_for_new_message`` function call.

.. code:: c

   void    ms_tick_event_callback() {

       // Copy the latest read vales from the HADC into our shared memory struct
       // so SHARC cores can access too
       multicore_data->audioproj_fin_pot_hadc0 = hadc_read_float(SAM_AUDIOPROJ_FIN_POT_HADC0);
       multicore_data->audioproj_fin_pot_hadc1 = hadc_read_float(SAM_AUDIOPROJ_FIN_POT_HADC1);
       multicore_data->audioproj_fin_pot_hadc2 = hadc_read_float(SAM_AUDIOPROJ_FIN_POT_HADC2);
       multicore_data->audioproj_fin_aux_hadc3 = hadc_read_float(SAM_AUDIOPROJ_FIN_AUX_HADC3);
       multicore_data->audioproj_fin_aux_hadc4 = hadc_read_float(SAM_AUDIOPROJ_FIN_AUX_HADC4);
       multicore_data->audioproj_fin_aux_hadc5 = hadc_read_float(SAM_AUDIOPROJ_FIN_AUX_HADC5);
       multicore_data->audioproj_fin_aux_hadc6 = hadc_read_float(SAM_AUDIOPROJ_FIN_AUX_HADC6);

       // Check to see if there are any event messages from the SHARC cores
       event_logging_poll_sharc_cores_for_new_message();

   }

Servicing the Event Logger on the SHARC Cores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code snippet below shows a 1ms timer tick service routine using the ``simple_sysctrl_set_1ms_callback()`` function provided in the sysctrl_simple driver. Within this 1ms tick, we're calling ``event_logging_process_queue_sharc_core()`` which will move new events over to the ARM core via the shared memory. If we've encountered any dropped audio frames, we'll report the number of dropped frames once per second.

.. code:: c


   // SHARC timer callback
   void    timer_tick_callback() {

       char message[128];
       static uint32_t dropped_audio_frames = 0;
       static uint32_t second_counter = 0;

       // If we have any messages queued up, send them
       event_logging_process_queue_sharc_core();

       // This is also a good place to alert us if we're dropping audio frames because our
       // callback processing is taking too long.
       if (second_counter++ % 1000 == 0) {
           if (multicore_data->sharc_core1_dropped_audio_frames != dropped_audio_frames) {
               sprintf(message, "SHARC core 1 dropped %d audio frame(s) in the last second",
                       multicore_data->sharc_core1_dropped_audio_frames - dropped_audio_frames);
               log_event(EVENT_WARN, message);
               dropped_audio_frames = multicore_data->sharc_core1_dropped_audio_frames;
           }
       }
   }

Logging an event
----------------

The ``log_event()`` function is used to log a new event on all three cores. This function takes two arguments.

The first argument is the level of the event and relies on a start syslog naming convention:

-  ``EVENT_INFO``
-  ``EVENT_DEBUG``
-  ``EVENT_WARN``
-  ``EVENT_ERROR``
-  ``EVENT_FATAL``

These are defined as an enum in bm_event_logging.h.

The second argument is a string of the event. The max string length is 128 characters.

The code snippet below shows how to log an event

.. code:: c

       log_event(EVENT_INFO, "Bare Metal Framework for the ADI SHARC Audio Module");

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#peripheral-and-system-drivers
   :alt: Using Peripheral and System Drivers#.|Bare Metal Framework#audioproj-tutorial|Using the Audio Project Fin
