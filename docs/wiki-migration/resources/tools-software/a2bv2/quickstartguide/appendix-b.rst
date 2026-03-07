:doc:`Click here to return to the QSG homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide>`

APPENDIX B: Stream and Export Configurations
============================================

In addition to supporting standard platforms and custom platform, A2B plugin for SS+ provides options for configuring A2B streams in the network, allows export of bus config and Commandlist files.

Navigating to Stream and Export Configuration in SS+
----------------------------------------------------

The A2B Stream Configuration can be found in the “Project” view under A2B Channel in SS+ as shown in :doc:`Figure 62 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/navigating_to_stream_network_and_export_configurations.png
   :width: 200px

**Figure 62 :** Navigating to Stream, Network and Export Configurations

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

:doc:`Figure 63 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>` shows the Audio Stream Definition tab in stream configurations.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/audio_stream_definition.png
   :width: 500px

**Figure 63 :** Audio Stream Definition

Audio Stream Assignment
~~~~~~~~~~~~~~~~~~~~~~~

Audio stream assignment tab allows user to change the stream source and stream destinations of streams in the network.

:doc:`Figure 64 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>` shows the Audio Stream Definition tab in stream configurations

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/audio_stream_assignment.png
   :width: 500px

**Figure 64 :** Audio Stream Assignment

.. note::

   Stream configuration window is enabled after schematic’s Link Compile is successful.


Data Tunnel Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Data Tunnel Configuration tab in Stream Configuration allows user to add, edit and delete data tunnels in the network.

.. note::

   Only AD243x(excluding AD2430 and AD2438) nodes can be part of the data tunnel.


   |image1|

**Figure 65:** Data Tunnel Configuration

Multi-Main Stream Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is one A2B channel per main-node chain and each A2B channel has one stream configuration. For instance, the schematic available at C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Rel1.1.0\\Schematics\\PC\\ adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj has two A2B channels and hence two stream configurations as shown in :doc:`Figure 66 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>` , :doc:`Figure 67 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_network_to_stream_mapping.png
   :width: 500px

**Figure 66:** Multi-main network to stream mapping. Red is A2B Channel 0 and Green is A2B Channel 1

For a multi-main system such as the one described in this schematic, the audio sources at main nodes are outputs from the DSP and sinks are inputs to the DSP. For instance in the A2B_4 stream configuration shown in :doc:`Figure 67 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`, cyan bubble at main-node is an input to the DSP and in the A2B_5 stream configuration shown in :doc:`Figure 67 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`, the dark grey bubble at main-node is an output from the DSP.

The example schematics provided with this installer adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj and adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj have pre-defined audio input and audio output configuration for the DSP ADSP-21569. The audio-in is a TDM2 24bit datastream sampled at 48kHz for which SPORT0A of the DSP is used. The audio-out is a TDM8 32bit datastream sampled at 48kHz for which SPORT5A is used. Changing these configurations is out of scope for this quick start guide.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_channel_to_stream_mapping.png
   :width: 500px

**Figure 67:** Multi-main channel to stream mapping. Red is A2B Channel 0 and sending audio to the DSP. Green is A2B channel 1 and receiving audio from the DSP.

Export Configuration
--------------------

Export settings window as shown in :doc:`Figure 68 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>` provides options to export BusConfig.c, Commandlist.h and Commandlist.xml files which can be used in Target Mode.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/export-import.png
   :width: 600px

**Figure 68 :** Export Settings

.. note::

   The exported files can be used with the stack and target examples in the 19.10.0 version of the software. The target demo examples can be found at <<A2B software 19.10.0 installation path>>\\Target\\examples\\demo.


Storing Network Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In SigmaStudio Plus, one can store the network configuration information into a memory device by saving the Schematic into an EEPROM connected to ECU. This can be done by navigating to “Export Import Settings” under “Networks -> A2B” as shown in :doc:`Figure 62 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`.

Also, there is a provision to export the information into an XML/ Dat file as shown in :doc:`Figure 69 </wiki-migration/resources/tools-software/a2bv2/quickstartguide/appendix-b>`. These files can be input to custom EEPROM programming utilities, specifically .dat file can be converted to hex/.s37 format for ease of flashing.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/schematic_dump_as_xml.png
   :width: 500px

**Figure 69:** Schematic Dump as XML

Loading Network Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To specify A2B stack running on the Target processor can load the network wide configuration from EEPROM ensure to define the macro ‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING ’ and ‘A2B_BCF_FROM_SOC_EEPROM’ and undefined ‘ADI_SIGMASTUDIO_BCF’ in ADI_A2B_Software-RelX.Y.Z\\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\platform\\a2b\\features.h.

Alternatively, network wide configuration can be sourced to target software from .dat file via the local file system.

Loading Network Configuration from .DAT file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file stores network configuration as binary file. The order of bytes in the file is same as the format specified for “Storing Networking Configuration in EEPROM”.

Follow the following steps to use this binary file as input to A2B target software.

-  Define path for the binary file - A2B_CONF_BINARY_BCF_FILE_URL in a2bapp_defs.h

   -  (<<A2B software 19.10.0 installation path>>\\Target\\examples\\demo\\a2b-xx\\app\\a2bapp_defs.h)

-  Define macro ‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING’ and ‘A2B_BCF_FROM_FILE_IO’ in feature.h ((<<A2B software 19.10.0 installation path>>\\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\a2b\\feature.h)
-  Ensure that ADI_SIGMASTUDIO_BCF is not defined (in feature.h)

The advantage of binary file is that network configuration doesn’t have compile time dependency with the target software.

Multi-main export configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/location_of_multi-main_export_configuration.png
   :width: 500px

**Figure 70:** Location of Multi-main export configuration

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/multi-main_export_configuration.png
   :width: 500px

**Figure 71:** Multi-main export configuration

Multi-main export configuration will export a single BCF xml and/or c file for the current multi-main network. This is feature is applicable only for multi-main networks.

Command List Utility
~~~~~~~~~~~~~~~~~~~~

Command list utility allows user to merge primary and secondary branch command list into a single command list to support branching.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/command_list_merge.png
   :width: 600px

**Figure:** Command List Merge

-  Generate the command list file from primary branch A2B network schematic.
-  Generate the command list file from secondary branch A2B network schematic.
-  Use the command list merge utility feature to generate the merged command list from primary branch and secondary branch command list files.
-  Click on the CmdLstMerge Tab as indicated above in Figure.
-  Select primary branch command list file generated in step 1 in “File path for Primary Branch .XML file”
-  Select secondary branch command list file generated in step 2 in “File path for Secondary Branch .XML file”
-  Provide the file path location for merged command list file in “File path for Merged Branching .XML file”
-  In the “Primary Branch Sub-Node ID” field, enter the sub-node id to which the secondary branch is connected in the primary chain.
-  Select the secondary branch main node address from “Chip Address” drop down box.
-  Click on the Export button to generate merged command list.
-  Use the Sequence window to Discover and configure the Branching network with generated merged command list file.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/data_tunnel_configuration.png
   :width: 500px
