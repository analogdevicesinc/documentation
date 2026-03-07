Using pre-configured topology files in the bare metal framework
===============================================================

The bare metal framework provides configuration files to initialize various A2B topologies. Presently supported configurations – between distinct SHARC Audio Modules, and optionally a Class D amplifier board – are described below.

Over time, additional configuration files will be made available to download on this page and import into the framework.

Current fixed A2B topology configurations available
---------------------------------------------------

+----------------------------------------+------------------------------------------------------------------------------------------------------+------------------------+
| Configuration                          | Functionality                                                                                        | Example Wizard Support |
+========================================+======================================================================================================+========================+
| A2B_TOPOLOGY_TDM8_SAM_to_SAM_2up_2down | Passes stereo audio between two SHARC audio modules (upstream and downstream)                        | Yes                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------+------------------------+
| A2B_TOPOLOGY_TDM8_SAM_to_CLASSD_4down  | A SHARC Audio Module sends two stereo pairs to a downstream Class D board, to both Class D amp chips | Yes                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------+------------------------+


.. note::

   SigmaStudio® projects for the fixed A2B topologies can be found in the ..\\extras\\sigmastudio-projects folder of the SHARC Audio Module Bare Metal SDK 2.1.1


--------------

Connecting A2B boards
---------------------

The SHARC Audio Module and the Class D board are equipped with two A2B connectors each: one labeled 'Master' and a second labeled 'Slave'. The 'Slave' connector connects to A2B nodes further downstream. The 'Master' connector connects to A2B nodes further upstream. The SHARC Audio Module is typically the master. Thus to connect a SHARC Audio Module (master node) to a Class D board (slave node), connect the A2B cable to the *slave* port on the SHARC Audio Module (i.e. towards the slave) and to the *master* port on the Class D board (i.e. towards the master).

.. note::

   other boards with A2B connectivity may label the A2B ports as 'A' and 'B'. In this case 'A' is the Master port (i.e. connects to upstream nodes, towards the master) and 'B' is the Slave port (i.e. connects downstream, towards downstream slave nodes).


Selecting an A2B network configuration in audio_system_config.h
---------------------------------------------------------------

The baremetal framework presently ships with three A2B initialization files / configurations. To set up the framework to configure A2B network support for one of the fixed topologies available, modify ``audio_system_config.h``. About half way down, the preprocessor macro ``ENABLE_A2B`` should be set to true. The ``A2B_ROLE_MASTER`` macro should also be set to true. Finally, set one of the three configurations to true. In the example below, we've selected the first configuration (two SHARC Audio Modules).

.. code:: c

   #define ENABLE_A2B                                      TRUE

   #if (ENABLE_A2B)

       // If A2B is enabled, select the role that this SHARC Audio Module board will play
       // TRUE = master node, FALSE = slave node
       #define A2B_ROLE_MASTER                             TRUE

       // If this SHARC Audio Module board is a master, select an A2B topology to use for initialization (select only one)
       #if (A2B_ROLE_MASTER)

           // Note that these topologies are created in SigmaStudio and stored within drivers/a2b_simple/a2b_topologies
           // See documentation for a full description of these configurations
           // SET ONLY ONE TO TRUE
           #define A2B_TOPOLOGY_TDM8_SAM_to_SAM_2up_2down                       TRUE
           #define A2B_TOPOLOGY_TDM8_SAM_to_CLASSD_4down                        FALSE

          // Add your own pre-processor variables for custom A2B topologies here
          
       #endif  // A2B_ROLE_MASTER

   #endif  // ENABLE_A2B

Using a configuration with a SHARC Audio Module as a slave node
---------------------------------------------------------------

Two of the A2B configurations provided with the baremetal framework can use a second SHARC Audio Module as a slave node in the A2B network.

If you want these nodes to simply pass audio, you can use the flash programming utility to program the boards as slave nodes. They will be set up to boot & operate as A2B slave nodes.

If you wish to run the baremetal framework and process audio on the *slave* SHARC Audio Module, set the ``ENABLE_A2B`` preprocessor macro mentioned above to ``TRUE`` and the ``A2B_ROLE_MASTER`` macro to ``FALSE``. In this case, the SHARC Audio Module will not attempt to initialize the A2B bus but will still be capable of sending and receiving audio from the A2B bus.

Routing audio to and from A2B within the baremetal framework
------------------------------------------------------------

As noted above, each A2B configuration describes a set of audio streams which may flow upstream (from slaves to master) and/or downstream (from master to slaves) over the A2B bus. The baremetal framework includes a set of A2B receive buffers (data arriving at the processor over the A2B bus) and A2B transmit buffers (data that will be sent over the A2B bus). Thus we read/write to the A2B bus by copying audio samples to/from these buffers in the audio callback.

Expand first SHARC core (Core 1) project and browse to ``${Core_1_Project}/src/callback_audio_processing.cpp``. Scroll down to the ``processaudio_output_routing()`` function. This function routes output audio to the various peripherals.

We can send audio into the A2B bus by writing to the ``audiochannel_a2b_[N]_[Right/Left]_out`` buffer. Similarly, we can read audio from the A2B bus by reading the corresponding ``_in`` buffers, e.g. within ``processaudio_callback()``.

To access the four channels on the Class D amp, use the first four buffers associated with Class D. These are by default configured to send out the first four output channels from Core 2 (which in turn mirror the first four output channels from Core 1).

.. code:: c

   audiochannel_a2b_0_left_out[i]  = audiochannel_from_sharc_core2_0_left[i];
   audiochannel_a2b_0_right_out[i] = audiochannel_from_sharc_core2_0_right[i];

   /*
     * Note - this code below is slightly different than the default A2B code in the audio callback file.
     * We are copying audio from audiochannel_from_sharc_core2_0_left, not audiochannel_from_sharc_core2_1_left. 
     * Audio coming in from the ADC is only on the first stereo pair so we'll copy this stereo
     * Audio to both stereo class D amps.
    */

   audiochannel_a2b_1_left_out[i]  = audiochannel_from_sharc_core2_0_left[i];
   audiochannel_a2b_1_right_out[i] = audiochannel_from_sharc_core2_0_right[i];

As mentioned above, if we are using an A2B configuration that sends four channels of audio (two stereo pairs) from the SHARC Audio Module to the Class D board, these will always be the first four channels.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#audioproj-tutorial
   :alt: Using the Audio Project Fin#.|Bare Metal Framework#custom-a2b-topology|Adding Custom A2B Configurations
