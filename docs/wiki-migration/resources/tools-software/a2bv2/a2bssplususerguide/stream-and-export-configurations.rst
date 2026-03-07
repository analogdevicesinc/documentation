:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Stream Configurations
=====================

In addition to supporting standard platforms and custom platform, A2B plugin for SigmaStudio+ provides options for configuring A2B streams in the network, allows export of bus config and Commandlist files.

Navigating to Stream Configuration in SS+
-----------------------------------------

The A2B Stream Configuration can be found in the “Project” view under A2B Channel in SS+ as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`.

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** Navigating to Stream, Network and Export Configurations


Stream Configuration
--------------------

Stream configuration is a window that enables the user the capability in

-  Adding a stream to the network
-  Editing an added stream
-  Deleting a stream
-  Source and destination node selection for the streams
-  Export and import of streams

Audio Stream Definition
~~~~~~~~~~~~~~~~~~~~~~~

Audio stream definition tab allows user to Add, Remove, Delete Streams, Move up and Down a stream, Import and Export streams.

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>` shows the Audio Stream Definition tab in stream configurations.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ **Figure:** Audio Stream Definition


Audio Stream Assignment
~~~~~~~~~~~~~~~~~~~~~~~

Audio stream assignment tab allows user to change the stream source and stream destinations of streams in the network.

:doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>` shows the Audio Stream Definition tab in stream configurations

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ **Figure:** Audio Stream Assignment


.. note::

   Stream configuration window is enabled after schematic’s Link Compile is successful.


Data Tunnel Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Data Tunnel Configuration tab in Stream Configuration allows user to add, edit and delete data tunnels in the network.

.. note::

   Only AD243x(excluding AD2430 and AD2438) nodes can be part of the data tunnel.


.. container:: centeralign

   \ |image4|\


.. container:: centeralign

   \ **Figure:** Data Tunnel Configuration


Multi-Main Stream Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is one A2B channel per main-node chain and each A2B channel has one stream configuration. For instance, the schematic available at C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Rel1.1.0\\Schematics\\PC\\ adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj has two A2B channels and hence two stream configurations as shown in below images.

.. container:: centeralign

   \ |image5|\


.. container:: centeralign

   \ **Figure:** Multi-main network to stream mapping. Red is A2B Channel 0 and Green is A2B Channel 1


For a multi-main system such as the one described in this schematic, the audio sources at main nodes are outputs from the DSP and sinks are inputs to the DSP. For instance in the A2B_4 stream configuration shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`, cyan bubble at main-node is an input to the DSP and in the A2B_5 stream configuration shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`, the dark grey bubble at main-node is an output from the DSP.

The example schematics provided with this installer adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj and adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj have pre-defined audio input and audio output configuration for the DSP ADSP-21569. The audio-in is a TDM2 24bit datastream sampled at 48kHz for which SPORT0A of the DSP is used. The audio-out is a TDM8 32bit datastream sampled at 48kHz for which SPORT5A is used. Changing these configurations is out of scope for this quick start guide.

.. container:: centeralign

   \ |image6|\


.. container:: centeralign

   \ **Figure:** Multi-main channel to stream mapping. Red is A2B Channel 0 and sending audio to the DSP. Green is A2B channel 1 and receiving audio from the DSP.


Methods for stream configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A2B offers two distinct approaches to manage how audio and data channels are allocated across the bus: Stream Design using the Stream Configuration Tool and Manual Slot Configuration. Each method provides a different level of control and flexibility, catering to both automated and fine-tuned design needs.

-  :doc:`Stream design using Stream configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations/streamconfig-network>`
-  :doc:`Manual Slot Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations/slot-config>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/streamconfig.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_definition.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/stream_assignment.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/data_tunnel.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/multimain.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/multimain_channel_streammapping.png
