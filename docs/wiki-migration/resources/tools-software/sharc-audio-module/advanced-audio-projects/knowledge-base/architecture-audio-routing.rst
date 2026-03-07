Audio Routing
=============

Overview
--------

This article gives a detailed overview of how the audio routing engine within the Audio Starter projects work. This may be helpful for users to better understand to to use the :doc:`routing command </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>` and better understand how data is piped into and out of the DSP.

Details
-------

In general, audio configuration and routing is set up logically according to TDM slot numbers which start at slot 0. TDM slots are accessed by users using the *route* command (see :doc:`route </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>`) with the source and destination offsets. The number of slots accessible by a user is limited to the specific TDM configuration, where applicable, virtual channel configuration, where applicable, and by physical hardware.

Take the following analog audio example on the ADZS-SC589-MINI which shows a potential audio path using a routing command that routes codec input to codec output:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/analogsc589.png

There is a digital connection between the processor (SC589 in this case) and the DAC. This is labeled as LINE OUT TDM in this diagram. There is also an analog connection between the DAC and the LINE OUT, where a speaker may be connected. This is labeled L/R.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample.jpg
   :width: 600px

When we talk about audio routing and source/destination offsets, for example, we are referring to the digital data that resides in a TDM Slot. In this case, the term slots are interchangeable with the term offset when it comes to routing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample2.jpg
   :width: 600px

So when we are creating audio routes to map input audio (sources/src) to output audio (sinks/dst), our offsets tell the router where from the TDM slots to pull from or which slots to place the audio into. So in a routing configuration that contains a destination offset (*dst offset*) of 0 will place any input data into the TDM slot, starting at offset 0 (TDM slot 0):

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/codecout.jpg
   :width: 600px

Similarly, for input clocked sources with a TDM configuration and a physical L/R analog hardware channel, the source offset (*src offset*) is the slot number of the TDM stream where audio will be pulled from.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample3.jpg
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/codecin.jpg
   :width: 600px

So for a routing where the *src offset* parameter is a value of 0, the data that is coming in from the ADC into TDM slot is the starting point of the copy:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/codecin2.jpg
   :width: 600px

Recall that even though the TDM stream may have more slots than the physical hardware, hardware may still limit the number of channels that can actually be input or output. In the above example, hardware in and out is limited to 2 channels but the TDM stream is 8 channels.

**Why is that? Why not just have the same number of TDM slots as physical hardware? :-/**

Well the TDM settings themselves are often dictated by physical clocking parameters used by the system which can be shared/re-used for other audio streams. As a result, the most optimal solution is often applied. Since a TDM stream with 8 channels can cover a physical stream with 1-8 channels, it can be re-used. Any channels not used are often filled with zeroes and/or discarded before reaching their final destination :-).

Revisiting our routing solution then, if we wanted to copy the left and right channels from the analog input and place them into the left and right channels of the analog output, we would use the following command:

*route 0 codec* **0** *codec* **0** *2 20*

The source and destination offsets start mapping from TDM slots 0 with 2 channels of audio:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample4.jpg
   :width: 600px

Or if we want to route the left channel (*src offset = 0*) of the analog input to the right channel (*dst offset = 1*) of the analog output, we could use the following command:

*route 0 codec* **0** *codec* **1** *1 20*

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample5.jpg
   :width: 600px

Noting that the above channels marked in blue are simply filled with zeroes (muted).

Or if we attempt to copy TDM slots beyond the capability of the physical hardware, we will simply hear no audio. For example:

*route 0 codec* **0** *codec* **2** *2 20*

Tries to copy to ADC channels starting at destination offset of 2, which doesn't go anywhere on the hardware. Oops :-D

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/routeexample6.jpg
   :width: 600px

For more information regarding the source/destination offsets and how they may map to physical hardware, refer to the Audio Configuration table for your Audio Starter variant in :doc:`Appendix C </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/appendix-c>`.

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`_
