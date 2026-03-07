Baremetal Framework Project Structure
=====================================

.. image:: https://wiki.analog.com/_media/youtube>uAER53AcOco
   :alt: youtube>uAER53AcOco

There are three distinct Project folders which each correspond to the code running on a distinct processor core of the ADSP-SC589. Furthermore, there are some folders which contain code that is shared between the three cores.

-  ``sam_baremetal_framework_core0`` - Code for ARM code
-  ``sam_baremetal_framework_core1`` - Code for SHARC Core 1
-  ``sam_baremetal_framework_core2`` - Code for SHARC Core 2
-  ``drivers`` - bare metal drivers for internal peripherals and external devices (e.g. ADCs, DACs, etc.)
-  ``common`` - files that are included in the three projects (ARM, SHARC Core 1, and SHARC Core 2). These files include a shared memory structure and project configuration.

Functions of each core
----------------------

sam_baremetal_framework_core0 (ARM Core)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ARM core is responsible for the following:

-  Initializing any external components (ADCs, DACS, codecs, SigmaDSPs, A2B controllers)
-  Selecting the right SRU / DAI configuration to route data from these components to the right SPORTs within this chip
-  Managing the audio sampling rate

Once the ARM core has initialized the various components of the system, it strobes ``LED10`` on the SHARC Audio Module board once per second. This serves as a visual indication that all of the initialization code completed successfully on the ARM core.

sam_baremetal_framework_core1 (SHARC Core 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHARC Core 1 is responsible for the following:

-  Setting up the DMA to move audio data between memory and the SPORTs (serial / I2S ports)
-  Managing the flow of data between core 1 and core 2 (shared memory or memory DMA)
-  Setting up the interrupts needed to let core 2 know audio data is ready
-  Calling the user’s audio callback function

The framework can be configured for single-core processing or dual-core processing.

When the framework is configured for single-core processing, the processing flow works as such:

``ADC`` -> ``SHARC Core 1`` -> ``DACs``

And when the framework is configure for dual-core processing, SHARC Core 1 still manages the flow of audio data to and from the ADCs and DACs.

``ADC`` -> ``SHARC Core 1 [processing]`` -> ``SHARC Core 2 [processing]`` -> ``SHARC Core 1 [final data transfer]`` -> ``DACs``

sam_baremetal_framework_core2 (SHARC Core 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHARC Core 2 is only responsible for processing audio.

Project Folder Structure
------------------------

All three projects have a few key folders:

\* ``src/``

-  ``audio_frameworks/`` - this folder contains a number of .c/.h file pairs that are used to configure and operate specific audio processing configurations. These essentially manage the audio plumbing and abstract away the underlying DMAs, interrupts, etc. Based on the overall project configuration (described in the next section), .c files are enabled through pre-processor variables. This allows us to have a common set of calling conventions (while sticking with C) and swap out modular frameworks without changing our audio processing.
-  ``drivers/`` - Device drivers used to initialize and control on-chip peripherals and external CODECs / ADCs / DACs, etc.
-  ``common/`` - files that are shared between all three cores
-  ``faust/`` - if you have generated source files using the Faust synthesis tool, place these files here

Each core also has one or more callbacks which is where your custom audio processing (or MIDI processing) resides. These callbacks have been architected such that all of the underlying mechanics of the audio movement and event generation have been abstracted so they are hardware platform agnostic.

-  ``Callback_Audio_Processing.cpp`` - add your C or C++ audio processing functions to this file
-  ``Callback_MIDI_Message.cpp`` - add any MIDI processing functions to this file
-  ``Callback_Pushbuttons.cpp`` - add any code to respond to push button events to this file

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#configuring-cces
   :alt: Configuring CCES#.|Bare Metal Framework#configuring-the-framework|Configuring the Framework
