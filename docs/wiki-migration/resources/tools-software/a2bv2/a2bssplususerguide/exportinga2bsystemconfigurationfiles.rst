:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Exporting A2B System Configuration files
========================================

A2B system configuration can be exported to files so that they can be used for configuring A2B system using a microcontroller or from different development environment.

A valid error free A2B schematic can be exported into C programming language and XML formats. The C format configuration files are used in Target software for A2B network configuration. As the configuration is stored in generic C format this file can also be taken to other environments supporting C programming language.

.. note::

   The A2B system configuration files can also be exported using Thrift Automation. For more information, refer to ":doc:`Export A2B System Configuration Files Using Thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`."


The XML format file is more readable and thus enables easy understanding of A2B system configuration flow.

The following options are available for the user to export A2B system configuration. Each option is explained in more detail in Section :doc:`General View Configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` and :doc:`Command List files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`. These files can be used to configure A2B network.

-  General View Configuration Files (C and XML format)
-  I2C/SPI command list Files (XML and C format)

The following steps describe the procedure for exporting A2B system configuration files

-  Create a valid A2B schematic as explained in :doc:`Drawing A2B schematics </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>` (or open an existing A2B Schematic project) in SigmaStudio+.
-  Save and Link the schematics.
-  Select the “Export Import Settings” under project window option as shown in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`.

|image1|

|

.. container:: centeralign

   **Figure :** Exporting system configuration


| A dialog box appears as shown in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`. Export required configuration file using appropriate tab.
| |image2|

.. container:: centeralign

   \ **Figure :** System Configuration File export window


.. note::

   
   -  Manual editing of exported XML is not recommended.
   -  Changes done to the schematic after last Link will not be reflected in the export. Hence schematic shall be always saved and Linked before exporting.
   


General View Configuration files
--------------------------------

The general view configuration files capture A2B system configuration information in more readable form and more functionality based rather than just register values. The information contained in these files correspond to the fields of ‘General View’ tab in the ‘Device Properties’ Window for all the nodes in the system.

Three files *adi_a2b_busconfig.c*, *adi_a2b_busconfig.dat*, *adi_a2b_busconfig.xml* are generated as part of BCF export.

A2B target software uses information in these files to discover, configure nodes and peripherals in the A2B system when using BF527/SHARC as the target processor or on a custom platform implementing A2B software Stack from ADI.

Bus Configuration Files (BCF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

adi_a2b_busconfig.c
^^^^^^^^^^^^^^^^^^^

This file stores A2B schematic as function-based settings instead of register values. The target software internally parses this file to get the register settings for each node in an A2B network. BCF also contains node level stream information (up to 32 streams).

This file shall be exported to *.\\Target\\examples\\demo\\a2b-xx\\app path*. If the compressed BCF is exported then, ensure that the macro ‘ADI_A2B_BCF_COMPRESSED’ is defined (*.\\Target\\examples\\demo\\a2b-xx\\app\\a2bapp_defs.h*)

.. note::

   The adi_a2b_busconfig.c can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


adi_a2b_busconfig.xml
^^^^^^^^^^^^^^^^^^^^^

This file has schematic information in :doc:`XML format </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>` which can be imported back. This allows user to apply different configurations to A2B system and verify the system behavior.

.. note::

   The adi_a2b_busconfig.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. note::

   Manual editing of exported XML file is not recommended as the signature will be corrupted.


Command List files
------------------

Command list files enable users to bring up A2B system without having to use the Target software provided with the release package. All that is required to bring up an A2B system using command list is to just have an I2C/SPI driver specific to the controller used for programming A2B Transceivers.

The command list can be exported in C and XML formats and are explained in the following sections.

adi_a2b_commandlist.h
^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^

The sequence of SPI/I2C commands is also generated in \*\* :doc:`XML format </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlistxml>` \*\* for easy readability and understanding. The generated XML file can be opened from ‘Sequence window’.

.. note::

   The adi_a2b_commandlist.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Commandlist Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. note::

   Few SPI A2B commands require polling of A2B_SPISTAT.SPI_BUSY using SPISTAT (0x04) command before issuing new commands. The command list contains a single command with the parameter name – “\ **SPI_BUSY_STAT_CHECK:** Read in loop”. The application is expected to issue this command in a loop till SPI is available.


Multi Main Command List
~~~~~~~~~~~~~~~~~~~~~~~

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   \ **Figure:** Location of Multi-main export configuration


Multi-main export configuration will export a single BCF xml and/or c file for the current multi-main network. This is feature is applicable only for multi-main networks. The multi main command list file is like command list except that multiple A2B mains (parallel A2B Buses) are represented in the single command list.

Command List Utility for Branching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command list utility allows user to merge primary and secondary branch command list into a single command list to support branching when a single Target processors controls multiple A2B network, this option can be used where individual main-sub-node chains are aggregated to form single command list.

.. container:: centeralign

   \ |image4|\


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

   \ |image5|\


.. container:: centeralign

   \ **Figure :** Multi Branch Bus Configuration File export


adi_a2b_mergedCLF.h
^^^^^^^^^^^^^^^^^^^

This file contains sequence of I2C/SPI commands (Write/Read/Delay) to be programmed for discovering and configuring A2B transceiver nodes and peripherals for multiple daisy chains of A2B transceivers. This file is saved in the form of a C header file so that this can be included and used in any custom project using a different microcontroller/DSP platform for quick evaluation.

adi_a2b\_ mergedCLF.xml
^^^^^^^^^^^^^^^^^^^^^^^

The sequence of SPI/I2C commands for multiple daisy chains of A2B transceivers, can also be generated in XML format for easy readability and understanding. The generated XML file can be opened from ‘Sequence window’.

.. note::

   The adi_a2b\_ mergedCLF.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Merged Branch Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


Working with Configuration XML files
------------------------------------

The following sub-sections describe the workflow associated with using different configuration XML files, exported from SigmaStudio+, when building an A2B System.

Workflow using BCF files
~~~~~~~~~~~~~~~~~~~~~~~~

The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` shows a typical workflow between A2B node suppliers and system architects/integrators when building an A2B system using Shape file and BCF.

A node supplier is responsible for designing the node’s functionality/TDM interfaces and verifying the design on SigmaStudio+. A verified node’s configuration, exported as shape file, shall be provided to A2B system integrator who would import individual node configuration files to build the final A2B system schematic on SigmaStudio+. A BCF .C file exported from such a verified schematic shall be used in the Target software.

Note that Custom Node Identifier needs to be set for nodes if node configuration is to be applied only upon Custom Node ID authentication as explained in :doc:`Custom Node ID based Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiversetting>`.


|image6|

.. container:: centeralign

   \ **Figure :** Work flow using Node Configuration and BCF


Export Configuration
--------------------

Export settings window as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` provides options to export BusConfig.c, Commandlist.h and Commandlist.xml files which can be used in Target Mode.

.. container:: centeralign

   \ |image7|\


.. container:: centeralign

   \ **Figure :** Export Settings


.. note::

   The exported files can be used with the stack and target examples in the the software. The target demo examples can be found at <<A2B software 1.x.y installation path>>\\Target\\examples\\demo.


Loading Network Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To specify A2B stack running on the Target processor can load the network wide configuration from EEPROM ensure to define the macro ‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING ’ and ‘A2B_BCF_FROM_SOC_EEPROM’ and undefined ‘ADI_SIGMASTUDIO_BCF’ in ADI_A2B_Software-RelX.Y.Z\\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\platform\\a2b\\features.h.

Alternatively, network wide configuration can be sourced to target software from .dat file via the local file system.

Loading Network Configuration from .DAT file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file stores network configuration as binary file. The order of bytes in the file is same as the format specified for “Storing Networking Configuration in EEPROM”.

adi_a2b_busconfig.dat
^^^^^^^^^^^^^^^^^^^^^

This file stores network configuration as binary file. The order of bytes in the file is same as the format specified for ‘Network Save in EEPROM’.

.. container:: centeralign

   \ |image8|\


.. container:: centeralign

   |image9|\


.. container:: centeralign

   \ |image10|\


Follow the following steps to use this binary file as input to A2B target software.

-  Define path for the binary file - **A2B_CONF_BINARY_BCF_FILE_URL** in a2bapp_defs.h (. \\Target\\examples\\demo\\a2b-xx\\app\\a2bapp_defs.h)
-  Define macro **‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING’** and **‘A2B_BCF_FROM_FILE_IO’** in feature.h (. \\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\a2b\\feature.h)
-  Ensure that **ADI_SIGMASTUDIO_BCF** is not defined (in feature.h)

The advantage of binary file is that network configuration doesn’t have compile time dependency with the target software.

Target application can choose file IO operations or memory read operations to access the .dat file when it is stored on Host PC.

.. note::

   The A2b_System_Autoconfig.dat can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


Auto Configuration
------------------

In the Auto configuration scheme, a host processor can automatically configure a A2B sub-node and its peripherals or a complete A2B network without prior knowledge of the topology. Typically, a non-volatile memory device like EEPROM is used to store the configuration information. Following sections describe the Auto configuration options in detail.

Auto Configuration of Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A complete A2B network can be configured using the information stored in a memory device that is directly connected to the Host processor via I2C. Such memory device shall use device address 0x50 (7-bit) and accessible directly to the Host processor over I2C. Upon boot, the host processor can read this information to automatically configure the complete A2B network i.e., main and sub-node A2B Transceivers, network and sub-node peripheral devices without any prior knowledge of the network.

.. note::

   The Auto configuration of Network .dat file can also be exported using Thrift Automation. For more information, refer to “\ :doc:`Export A2B Auto Configuration Files Using Thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.”


Storing Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In SigmaStudio+, one can store the network configuration information into a memory device by saving the Schematic into an EEPROM connected to ECU. This can be done by right clicking the master node. It also can be access from the project window.

.. container:: centeralign

   \ |image11|\


.. container:: centeralign

   \ **Figure:** Saving Schematic to EEPROM


Also, there is a provision to export the information into an XML/ Dat file as shown in :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`. These files can be input to custom EEPROM programming utilities, specifically .dat file can be converted to hex/.s37 format for ease of flashing.

.. container:: centeralign

   \ |image12|\


.. container:: centeralign

   \ **Figure:** Schematic Dump as XML


.. _loading-network-configuration-1:

Loading Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alternatively, network wide configuration can be sourced to target software from .dat file via the local file system. Refer :doc:`adi_a2b_busconfig.dat </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` section for more details. (.dat file from EEPROM window and adi_a2b_busconfig.dat file is essentially same)

The Stream information of A2B network is exported to binary file/EEPROM if ‘Include Stream info to dat file’ checkbox is enabled. Stream Information of A2B network is stored in the EEPROM/binary file as shown below.

.. container:: centeralign

   \ |image13|\


.. container:: centeralign

   \ **Figure:** A2B Network Stream Information Schematic for EEPROM/DAT File


In EEPROM/Binary file 6th byte (EEPROM Byte Address is 0x05) indicates that the Stream information is exported if the value is 0x01. Addresses mentioned in the Stream Information :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` are just for representation and they are not the actual address. Stream information address would be defined by the value at 0x18 (MSB) and 0x19 (LSB) in EEPROM/Binary (DAT) File.

For optimized discovery flow, configure the A2B stack to program the peripherals in multiple jobs instead of serial peripheral processing. This can be done by setting the macro ‘A2B_CONSECUTIVE_PERIPHERAL_CFGBLOCKS’ to a non-zero value in case of EEPROM usage.

Custom Node Information
^^^^^^^^^^^^^^^^^^^^^^^

The Custom Node Information is stored in .DAT in the format specified in below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`.

.. container:: centeralign

   \ |image14|\


.. container:: centeralign

   \ **Figure:** A2B Network Custom Node Information for EEPROM/DAT File


Specifications of Export files from A2B plugin for SigmaStudio+
===============================================================

| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlistxml>` for the Command List XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlisth>` for the Command List header specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/peripheralxml>` for the Peripheral XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>` for the A2B BCF XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfc>` for the A2B BCF.c specification

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportimport.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/system_config.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/location_of_multi_main.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/command_list_merge.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/cmdlist.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/work_flow_using_ncfs_and_bcf.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/export-import.png
.. |image8| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image1_dat.png
.. |image9| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image2_dat.png
.. |image10| image:: https://wiki.analog.com/_media/function_ns_e_t_n_qo_e_t/var_r_i/t_wv_si_sr_r.basetypesource_t_wv_t_wv_si_sr_r_t_qe_t_i_t_qe_wo/t_qe_xi_t_qe_r_i_xi_t_en_r_i_z_n_xo_r_n/var_o_t_qe_rr_a_new_si_e_o_r_i_s_new_zo_si_sr_a/return_jo_e_si_zo_t_s/image3_dat.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/save_schematic_eeprom.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/schematic_dump_as_xml.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_network_stream_information_schematic_for_eeprom_dat_file.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/l5updated.png
