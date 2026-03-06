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
   


Here are different configuration files that can be exported

-  :doc:`General View configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/generalview-config>`
-  :doc:`Command list files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/commadlist-config>`

Working with Configuration files
--------------------------------

The following sub-sections describe the workflow associated with using different configuration XML files, exported from SigmaStudio+, when building an A2B System. :doc:`Working with Configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/workflow-bcf>`

Loading Network Configuration
-----------------------------

To specify A2B stack running on the Target processor can load the network wide configuration from EEPROM ensure to define the macro ‘A2B_FEATURE_EEPROM_OR_FILE_PROCESSING ’ and ‘A2B_BCF_FROM_SOC_EEPROM’ and undefined ‘ADI_SIGMASTUDIO_BCF’ in ADI_A2B_Software-RelX.Y.Z\\Target\\examples\\demo\\a2b-xx\\a2bstack-pal\\platform\\a2b\\features.h.

Alternatively, network wide configuration can be sourced to target software from .dat file via the local file system. This is explained in :doc:`Loading Network Configuration from .DAT file </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/dat>`

Auto Configuration
------------------

In the Auto configuration scheme, a host processor can automatically configure a A2B sub-node and its peripherals or a complete A2B network without prior knowledge of the topology. Typically, a non-volatile memory device like EEPROM is used to store the configuration information. Following sections describe the :doc:`Auto configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/autoconfig>` options in detail.

Specifications of Export files from A2B plugin for SigmaStudio+
---------------------------------------------------------------

| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlistxml>` for the Command List XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/cmdlisth>` for the Command List header specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/peripheralxml>` for the Peripheral XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>` for the A2B BCF XML specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfc>` for the A2B BCF.c specification
| :doc:`click here </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list/dat>` for the DAT specification

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/exportimport.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/system_config.png
