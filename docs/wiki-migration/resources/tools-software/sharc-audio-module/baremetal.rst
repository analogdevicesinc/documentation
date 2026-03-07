Bare Metal Framework Overview
=============================

The :adi:`SHARC Audio Module <sharcaudiomodule>` Bare Metal framework is a light-weight C / C++ framework designed for efficient audio signal processing using the :adi:`ADSP-SC589 <sc58x>` processor on the :doc:`SHARC Audio Module main board </wiki-migration/resources/tools-software/sharc-audio-module/hardware>`.

This framework is block-based and double-buffered. All audio processing is done in 32-bit floating point. The framework consumes just a few MHz of the 450MHz :adi:`sharc` DSPs. This includes managing the movement of audio data, performing fixed / floating point conversion and triggering various user-call backs for audio processing.

This framework supports the :doc:`Audio Project Fin </wiki-migration/resources/tools-software/sharc-audio-module/hardware/audioproj-fin>` using the expansion connector. It also supports other hardware connected over the :adi:`a2b` bus.

The framework relies on a modular architecture which makes it easy to swap in/out different audio configurations, Fin board support, A2B module support, etc. without needing to modify your audio processing routines.

The framework is easily configurable via a shared header file that is used to set up system-wide audio processing configurations (e.g. single or dual core processing, audio block size, audio sample rate, presence of daughter boards, which audio framework to use, etc.)

The framework includes a very simple and efficient multi-core memory sharing mechanism which simplifies passing parameters and sharing state information between cores.

The framework also includes a library of audio processing and audio effects code that can be used to create interesting effects pedals, musical instruments, etc.

The bare metal framework is designed to be easy to use and understand. There are no “black boxes” in this code. The code has been heavily commented so it can be modified and customized. The majority of the drivers are written to be simple and rely on direct control register reads and writes. This framework is designed to serve as an example of how to use some of the advanced functionality on the ADSP-SC589 to efficiently process audio using C and C++ algorithms.

Framework Documentation
-----------------------

-  :doc:`Bare Metal Project Wizard </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/project-wizard>`
-  :doc:`Opening the Framework in CCES </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/downloading-and-installing>`
-  :doc:`Configuring CCES for Development and Debug of the Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/configuring-cces>`
-  :doc:`Framework Architecture and Project Structure </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/baremetal-framework-architecture>`
-  :doc:`Configuring the Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/configuring-the-framework>`
-  :doc:`Processing Audio within the Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/processing-audio>`
-  :doc:`Selecting Between Different Hardware Platforms </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/audio-frameworks>`
-  :doc:`Sharing Data Between Cores / System Telemetry </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/using-shared-memory-structure>`
-  :doc:`Using Peripheral and System Drivers </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/peripheral-and-system-drivers>`
-  :doc:`Using the Event Logging Feature </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/event-logging>`
-  :doc:`Using the Audio Project Fin for the SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/audioproj-tutorial>`
-  :doc:`Using Pre-configured A2B Topology Files </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/preconfigured-a2b-topology>`
-  :doc:`Custom A2B Configuration for SHARC Audio Module </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/custom-a2b-topology>`
-  :doc:`Creating Drivers for New Audio Components </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/driver-creation-tutorial>`
-  :doc:`Porting the Bare Metal Framework to a Different Hardware Platform </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/porting-to-new-hardware-tutorial>`
-  :doc:`Programming BM Framework to Flash </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/flashing>`
-  :doc:`Troubleshooting </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/troubleshooting>`

Tutorials
---------

Follow these tutorials to become familiar with bare metal audio framework and the various audio processing features and capabilities.

Basic Audio Processing
~~~~~~~~~~~~~~~~~~~~~~

These tutorials present the basic concepts of processing audio in real time using the bare metal audio framework.

-  :doc:`Tutorial: Audio Processing Basics with One or Two Cores </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/using-both-cores>`
-  :doc:`Tutorial: Implementing a Tremolo Effect from Scratch with Tap-to-Set-Tempo Feature </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/tremelo-effect-tutorial>`
-  :doc:`Tutorial: Implementing a Ring Modulator Effect from Scratch </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/ring-modulator-effect-tutorial>`
-  :doc:`Tutorial: Implementing a Delay(Echo) Effect from Scratch </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/delay-effect-tutorial>`

Working with the "Audio Elements" and "Audio Effects" Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These tutorials will show users how to use the various audio elements and audio effects within the bare metal audio framework.

-  :doc:`Introduction to the "Audio Elements" and "Audio Effects" </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/audio-elements>`
-  :doc:`Tutorial: Programming a Volume Control with the Audio Elements </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/volume-control-tutorial>`
-  :doc:`Tutorial: Chaining Audio Elements and Audio Effects </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/chaining-audio-elements>`
-  :doc:`Tutorial: Building a 2.1 amplifier with the Class-D board </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/class-d-2-1-amp>`
-  :doc:`Tutorial: A Simple MIDI Synthesizer </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/simple-midi-synth>`

Using MATLAB Generated Code in the Bare Metal Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`Using a MATLAB Volume Control Function in the Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/matlab_volume_control>`
-  :doc:`Using a MATLAB Pitch Shift Algorithm in the Framework </wiki-migration/resources/tools-software/sharc-audio-module/baremetal/matlab_pitchshift>`

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#gettingstarted
   :alt: Getting Started#.|SHARC Audio Module#.hardware|Hardware Reference
