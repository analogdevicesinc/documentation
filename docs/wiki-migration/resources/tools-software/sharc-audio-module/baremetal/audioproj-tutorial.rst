Using the Audio Project Fin for the SHARC Audio Module
======================================================

The :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>` is an extender board for the SHARC Audio Module that is designed to allow musicians and hobbyists to use the SHARC Audio Module in music and audio projects.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/diy.jpg
   :width: 600px

Audio Project Fin Features
--------------------------

-  1/4" stereo instrument level input and output jacks for connecting guitars, keyboards, amps, etc.
-  MIDI In / Out / Thru DIN connectors
-  3 POTs which connect to the House Keeping ADC (HADC) on the ADSP-SC589
-  4 additional auxiliary analog control inputs that are buffered which run through the remaining HADC channels.
-  4 push buttons
-  8 LEDS (one for each push button and four in a VU configuration)
-  dedicated analog 5V and 9V supplies.
-  circuit prototyping area with 100 mil headers for routing I/O to a panel or chassis

   -  4 additional LEDS
   -  HADC channels
   -  MIDI signals
   -  Four push button signals that can be routed to external push buttons

Audio Project Support in the Baremetal Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The baremetal framework fully supports the various I/O features of the Audio Project Fin.

To enable Audio Project Fin functionalities in the baremetal framework, open up ``/common/audio_system_config.h`` and define the ``SAM_AUDIOPROJ_FIN_BOARD_PRESENT`` macro as ``TRUE``:

.. code:: c

   #define SAM_AUDIOPROJ_FIN_BOARD_PRESENT           TRUE

This field is set to ``TRUE`` by default.

Accessing Audio on the 1/4" Stereo Jacks
----------------------------------------

By default, the ADAU1761 is configured to mix together (in the mixing hardware upstream from the ADC) the audio from its primary and its AUX stereo inputs. The 1/4" input jack plug on the Audio Project Fin is connected to the AUX inputs of the ADAU1761. Thus, stereo signals from the Audio Project Fin 1/4" input jack and from the SHARC Audio Module 1/8" input jack are converted simultaneously in the same ADC channels.

By default, the ADAU1761 is configured to route audio from its DAC to both its headphone (HP) and its primary stereo outputs. The 1/4" output jack plug on the Audio Project Fin is connected to the HP outputs of the ADAU1761. The 1/8" output jack plug on the SHARC Audio Module is connected to the primary outputs of the ADAU1761. Thus, stereo digital audio received by the ADAU1761 is output simultaneously to both the 1/4" jack plug on the Audio Project Fin and the 1/8" jack plug on the SHARC Audio Module board.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/tutorial-diy-adau1761.png
   :alt: ADAU1761 audio routing
   :align: center
   :width: 600px

For this reason, the same audio buffers are used for the 1/8" and the 1/4" audio jacks. Audio processing routines must be written in the SHARC Core 1 and 2 audio callback hooks, i.e. the ``processaudio_callback()`` function of ``${Core_Project}/src/callback_audio_processing.cpp``. See the :doc:`baremetal framework introduction </wiki-migration/resources/tools-software/sharc-audio-module/baremetal>` for more information.

For example, you can write the following code snippet in either core's ``processaudio_callback()`` to increase the gain of the analog input signal, coming from the ADCs, by 50% before routing it out to the DACs:

.. code:: c

   // Increase gain by 50%
   audiochannel_0_left_out[i]  = 1.5\*audiochannel_0_left_in[i];
   audiochannel_0_right_out[i] = 1.5\*audiochannel_0_right_in[i];

.. important::

   You may need to comment out other portions of the function to apply your changes successfully.


Accessing the POTs and Aux HADC/control inputs
----------------------------------------------

The HADC channels connected to the POTs and the auxiliary HADC inputs are polled by the ARM core 1,000 times per second. The results of these measurements are converted to floats and normalized to range between 0.0 and 1.0. These values are then stored in the multicore memory structure (a shared C struct that all three cores can access) found in ``/src/common/multicore_shared_memory.h``. So you can read the value of a POT or an auxiliary HADC channel, in the code of any of the three cores, from the respective field in the multicore memory structure (multicore_data).

For example, you can write the following code snippet in either core's processaudio_callback() to use the first POT as a volume knob for the stereo audio flowing to and from the ADAU1761:

.. code:: c

   // Change gain by value of the first POT (which varies between 0.0 and 1.0)
   float pot0_val = multicore_data->audioproj_fin_pot_hadc0;

   audiochannel_0_left_out[i]  = pot0_val * audiochannel_0_left_in[i];
   audiochannel_0_right_out[i] = pot0_val * audiochannel_0_right_in[i];

Similarly, the other HADC values – also that are updated 1,000 times per second – can be read from the multicore memory structure according to the same naming scheme:

.. code:: c

   // These are the POTS on the Audio Project Fin
   multicore_data->audioproj_fin_pot_hadc0;
   multicore_data->audioproj_fin_pot_hadc1;
   multicore_data->audioproj_fin_pot_hadc2;

   // And these are the additional HADC input channels available on the Audio Project headers
   multicore_data->DIY_Aux_HADC3;
   multicore_data->DIY_Aux_HADC4;
   multicore_data->DIY_Aux_HADC5;
   multicore_data->DIY_Aux_HADC6;

The Aux HADC channels are buffered through a simple op-amp circuit and filtered through a low-pass circuit (≈ 1 KHz cutoff) on the Audio Project Fin.

Accessing the LEDs
------------------

The Audio Project Fin has a number of LEDs that can be accessed through the GPIO simple driver.

Are number of pre-processor macros are defined for LEDs and GPIO pins access in ``/src/common/helper_functions.h`` (source shared between cores). These definitions are shown below.

.. code:: c

   // LEDs by PCB designator
   #define    GPIO_AUDIOPROJ_FIN_LED_3       GPIO_PINPORT(ADI_GPIO_PORT_E, 0)
   #define    GPIO_AUDIOPROJ_FIN_LED_4       GPIO_PINPORT(ADI_GPIO_PORT_E, 1)
   #define    GPIO_AUDIOPROJ_FIN_LED_5       GPIO_PINPORT(ADI_GPIO_PORT_E, 2)
   #define    GPIO_AUDIOPROJ_FIN_LED_6       GPIO_PINPORT(ADI_GPIO_PORT_E, 3)
   #define    GPIO_AUDIOPROJ_FIN_LED_7       GPIO_PINPORT(ADI_GPIO_PORT_E, 4)
   #define    GPIO_AUDIOPROJ_FIN_LED_8       GPIO_PINPORT(ADI_GPIO_PORT_E, 5)
   #define    GPIO_AUDIOPROJ_FIN_LED_9       GPIO_PINPORT(ADI_GPIO_PORT_E, 6)
   #define    GPIO_AUDIOPROJ_FIN_LED_10      GPIO_PINPORT(ADI_GPIO_PORT_E, 7)

   // LEDs beneath the Switches / push buttons
   #define    GPIO_AUDIOPROJ_FIN_LED_SW1     GPIO_PINPORT(ADI_GPIO_PORT_E, 3)
   #define    GPIO_AUDIOPROJ_FIN_LED_SW2     GPIO_PINPORT(ADI_GPIO_PORT_E, 2)
   #define    GPIO_AUDIOPROJ_FIN_LED_SW3     GPIO_PINPORT(ADI_GPIO_PORT_E, 1)
   #define    GPIO_AUDIOPROJ_FIN_LED_SW4     GPIO_PINPORT(ADI_GPIO_PORT_E, 0)

   // Four VU LEDs in center of Audio Project Fin
   #define    GPIO_AUDIOPROJ_FIN_LED_VU1     GPIO_PINPORT(ADI_GPIO_PORT_E, 4)
   #define    GPIO_AUDIOPROJ_FIN_LED_VU2     GPIO_PINPORT(ADI_GPIO_PORT_E, 5)
   #define    GPIO_AUDIOPROJ_FIN_LED_VU3     GPIO_PINPORT(ADI_GPIO_PORT_E, 6)
   #define    GPIO_AUDIOPROJ_FIN_LED_VU4     GPIO_PINPORT(ADI_GPIO_PORT_E, 7)

   // External LED 100mil header (P15-P12)
   #define    GPIO_AUDIOPROJ_FIN_EXT_LED_1   GPIO_PINPORT(ADI_GPIO_PORT_D, 4)
   #define    GPIO_AUDIOPROJ_FIN_EXT_LED_2   GPIO_PINPORT(ADI_GPIO_PORT_D, 5)
   #define    GPIO_AUDIOPROJ_FIN_EXT_LED_3   GPIO_PINPORT(ADI_GPIO_PORT_D, 6)
   #define    GPIO_AUDIOPROJ_FIN_EXT_LED_4   GPIO_PINPORT(ADI_GPIO_PORT_D, 7)

   // Switches / push buttons
   #define    GPIO_AUDIOPROJ_FIN_SW_1        GPIO_PINPORT(ADI_GPIO_PORT_E, 8)
   #define    GPIO_AUDIOPROJ_FIN_SW_2        GPIO_PINPORT(ADI_GPIO_PORT_E, 9)
   #define    GPIO_AUDIOPROJ_FIN_SW_3        GPIO_PINPORT(ADI_GPIO_PORT_E, 10)
   #define    GPIO_AUDIOPROJ_FIN_SW_4        GPIO_PINPORT(ADI_GPIO_PORT_E, 12)

   #define    GPIO_AUDIOPROJ_FIN_PB_1        GPIO_PINPORT(ADI_GPIO_PORT_E, 8)
   #define    GPIO_AUDIOPROJ_FIN_PB_2        GPIO_PINPORT(ADI_GPIO_PORT_E, 9)
   #define    GPIO_AUDIOPROJ_FIN_PB_3        GPIO_PINPORT(ADI_GPIO_PORT_E, 10)
   #define    GPIO_AUDIOPROJ_FIN_PB_4        GPIO_PINPORT(ADI_GPIO_PORT_E, 12)

There are also similar definitions for the LEDs and push-buttons in the SHARC Audio Module source code.

.. code:: c

   // LEDs on SHARC Audio Module
   #define    GPIO_SHARC_SAM_LED10        GPIO_PINPORT(ADI_GPIO_PORT_D, 1)
   #define    GPIO_SHARC_SAM_LED11        GPIO_PINPORT(ADI_GPIO_PORT_D, 2)
   #define    GPIO_SHARC_SAM_LED12        GPIO_PINPORT(ADI_GPIO_PORT_D, 3)

   // Push buttons (PBs) on SHARC Audio Module
   #define    GPIO_SHARC_SAM_PB1          GPIO_PINPORT(ADI_GPIO_PORT_F, 0)
   #define    GPIO_SHARC_SAM_PB2          GPIO_PINPORT(ADI_GPIO_PORT_F, 1)

For example, call the ``gpio_write()`` function to write to any given LED like so:

.. code:: c

   // Turn on the first LED in the VU LED bar
   gpio_write(GPIO_AUDIOPROJ_FIN_LED_VU1, GPIO_HIGH);

   // Turn off the second LED in the VU LED bar
   gpio_write(GPIO_AUDIOPROJ_FIN_LED_VU2, GPIO_LOW);

**Note:** ``gpio_write()`` is defined in ``/src/drivers/gpio_simple/gpio_simple.h`` and implemented in ``/src/drivers/gpio_simple/gpio_simple.c``. You may need to import these files to use them.

Accessing the Push Buttons
--------------------------

The push buttons are routed to GPIO pins and can be used to trigger interrupts on any of the three cores. By default, the push button interrupts are handled by the ARM core. The ARM core sets a boolean variable of the multicore memory structure to true. This enables SHARC cores to poll for push button events.

The interrupt handlers for these push buttons can be found in the ARM core project, at ``${Core_0_Project}/src/Callback_Pushbuttons.cpp``. A comment indicates where custom code can be added safely.

.. code:: c

   // Call back for PB1 on SHARC Audio Module Audio Project Fin
   void pushbutton_callback_external_1( void  * data_object ) {

       static bool sw1_state = false;

       // Toggle the LED below the button to indicate state
       sw1_state = !sw1_state;
       if (sw1_state) {
           gpio_write(GPIO_AUDIOPROJ_FIN_LED_SW1, GPIO_HIGH);
       } else {
           gpio_write(GPIO_AUDIOPROJ_FIN_LED_SW1, GPIO_LOW);
       }

       // Update our multicore structure to let the SHARCs know that a PB has been pressed
       multicore_data->audioproj_fin_sw_1_core1_pressed = true;
       multicore_data->audioproj_fin_sw_1_core2_pressed = true;

       // Add custom code here

   }

Each handler sets a specific boolean value in the multicore memory structure. **Note that once a polling SHARC core has read a 'true' value, it is responsible for setting the variable back to 'false' itself.**

The code snippet below shows an example of how to handle a push button event from SHARC core 1.

.. code:: c

   // Check to see if a push button event has been registered to toggle
   // an audio effect
   if (multicore_data->audioproj_fin_sw_1_core1_pressed) {

       // Set the PB pressed field to false
       multicore_data->audioproj_fin_sw_1_core1_pressed = false;

       // Toggle audio effect
       effectEnabled = !effectEnabled;
   }

Accessing MIDI
--------------

MIDI is enabled when the framework is set to work with a Audio Project Fin and MIDI events are handled by the ARM core.

A MIDI-processing callback hook for can be found in the ARM core project, at ``${Core_0_Project}/src/Callback_MIDI_Message.cpp``. This hook is called each time a new MIDI note arrives. By default, it writes the MIDI note back to the MIDI out interface as shown below. The MIDI driver uses the ``simple_uart driver`` so MIDI notes are read and written with calls to this UART driver.

.. code:: c

   // Create a struct for our MIDI UART driver instance
   BM_UART midi_uart_arm;

   // Callback is called when new MIDI bytes arrive
   void midi_rx_callback_arm( void ) {

       uint8_t val;

       // Keep reading bytes from MIDI FIFO until we have processed all of them
       while (uart_available(&midi_uart_arm)) {

         // Read the new byte
         uart_read_byte(&midi_uart_arm, &val);

         // Write that byte back to MIDI TX
         uart_write_byte(&midi_uart_arm, val);
       }
   }

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#event-logging
   :alt: Using Event Logging#.|Bare Metal Framework#preconfigured-a2b-topology|Using pre-configured A2B topology files
