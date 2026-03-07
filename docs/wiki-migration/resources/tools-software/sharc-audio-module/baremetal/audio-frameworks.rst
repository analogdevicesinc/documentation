Supporting and Selecting Between Different Hardware Platforms
=============================================================

The baremetal framework is designed to be portable and to support multiple / different hardware platforms. The baremetal framework contains a pair of files on each core which contain all of the platform-specific code and functionality. These files are known as audio frameworks. The baremetal framework offers several “audio frameworks”. These can be found under ``src/audio_frameworks`` in each core's project directory tree. A single framework is used at any given time, selected via the ``audio_system_config.h`` file described above.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/baremetal/framework_layers.png
   :alt: Audio Frameworks Provide Hardware Platform Specific Code

These framework file pairs are responsible for managing the audio plumbing and abstract the processor and framework-specific aspects of the audio processing. When you switch audio frameworks or framework options (e.g. migrating from single core processing to dual core processing), you don’t need to change your audio processing code in the callbacks.

These frameworks are similar and each really serves as an example of how various types of audio plumbing can be done on the SHARC.

-  The 8 channel framework is the standard audio processing framework for the SHARC Audio Module board (and when the Audio Project Fin is connected)
-  The 16 channel framework is designed to support automotive customers that use the automotive Fin and is an example of how to support hardware beyond what is on the SHARC Audio Module board.
-  The Bypass framework is used to test A2B topologies

The frameworks have a very light processing footprint, usually on the order of a 3-15MHz on Core 1 (of the 450Mhz available) and less than 1 Mhz on Core 2.

--------------

.. image:: https://wiki.analog.com/_media/navigation SHARC Audio Module#processing-audio
   :alt: Processing Audio within the Framework#.|Bare Metal Framework#using-shared-memory-structure|Sharing Data Between Cores
