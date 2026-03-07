Command List files
==================

Command list files enable users to bring up A2B system without having to use the Target software provided with the release package. All that is required to bring up an A2B system using command list is to just have an I2C/SPI driver specific to the controller used for programming A2B Transceivers.

The command list can be exported in C and XML formats and are explained in the following sections.

adi_a2b_commandlist.h
---------------------

\*\* :doc:`Command list header file </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlisth>` \*\* contains sequence of I2C/SPI commands (Write/Read/Delay) to be programmed for discovering and configuring A2B transceiver nodes and peripherals as per the drawn schematic. This file is saved in the form of a C header file so that this can be included and used in any custom project using a different microcontroller/DSP platform for quick evaluation.

An example project using command list for A2B network discovery and configuration is available at .\\Target\\a2b-commandlist.

.. note::

   The adi_a2b_commandlist.h can also be exported using thrift. For more information, you can refer to :doc:`Export of Commandlist Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. note::

   Command list file does not provide A2B interrupt or event/fault handling routines. The software running on the controller shall be responsible for handling such events/faults.


.. note::

   Few SPI A2B commands requires polling of A2B_SPISTAT.SPI_BUSY bit using SPISTAT (0x04) command before issuing new commands. The command list contains a single command with the comment – “/\* **SPI_BUSY_STAT_CHECK:** Read in loop \*/”. The application is expected to issue this command in a loop till SPI is available.


.. note::

   “Delay” in command list file is an alternative to active wait time.


adi_a2b_commandlist.xml
-----------------------

The sequence of SPI/I2C commands is also generated in \*\* :doc:`XML format </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlistxml>` \*\* for easy readability and understanding. The generated XML file can be opened from ‘Sequence window’.

.. note::

   The adi_a2b_commandlist.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Commandlist Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. note::

   Few SPI A2B commands require polling of A2B_SPISTAT.SPI_BUSY using SPISTAT (0x04) command before issuing new commands. The command list contains a single command with the parameter name – “\ **SPI_BUSY_STAT_CHECK:** Read in loop”. The application is expected to issue this command in a loop till SPI is available.


Multi Main Command List
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: centeralign

   \ |image1|\


.. container:: centeralign

   \ **Figure:** Location of Multi-main export configuration


Multi-main export configuration will export a single BCF xml and/or c file for the current multi-main network. This is feature is applicable only for multi-main networks. The multi main command list file is like command list except that multiple A2B mains (parallel A2B Buses) are represented in the single command list.

Command List Utility for Branching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command list utility allows user to merge primary and secondary branch command list into a single command list to support branching when a single Target processors controls multiple A2B network, this option can be used where individual main-sub-node chains are aggregated to form single command list.

.. container:: centeralign

   \ |image2|\


.. container:: centeralign

   \ **Figure:** Command List Merge


-  Generate the command list file from primary branch A2B network schematic.
-  Generate the command list file from secondary branch A2B network schematic.
-  Use the command list merge utility feature to generate the merged command list from primary branch and secondary branch command list files.
-  Click on the CmdLstMerge Tab as indicated above in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`.
-  Select primary branch command list file generated in step 1 in “File path for Primary Branch .XML file”
-  Select secondary branch command list file generated in step 2 in “File path for Secondary Branch .XML file”
-  Provide the file path location for merged command list file in “File path for Merged Branching .XML file”
-  In the “Primary Branch Sub-Node ID” field, enter the sub-node id to which the secondary branch is connected in the primary chain.
-  Select the secondary branch main node address from “Chip Address” drop down box.
-  Click on the Export button to generate merged command list.
-  Use the Sequence window to Discover and configure the Branching network with generated merged command list file.

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ **Figure :** Multi Branch Bus Configuration File export


adi_a2b_mergedCLF.h
-------------------

This file contains sequence of I2C/SPI commands (Write/Read/Delay) to be programmed for discovering and configuring A2B transceiver nodes and peripherals for multiple daisy chains of A2B transceivers. This file is saved in the form of a C header file so that this can be included and used in any custom project using a different microcontroller/DSP platform for quick evaluation.

adi_a2b\_ mergedCLF.xml
-----------------------

The sequence of SPI/I2C commands for multiple daisy chains of A2B transceivers, can also be generated in XML format for easy readability and understanding. The generated XML file can be opened from ‘Sequence window’.

.. note::

   The adi_a2b\_ mergedCLF.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Merged Branch Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/location_of_multi_main.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/command_list_merge.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/cmdlist.png
