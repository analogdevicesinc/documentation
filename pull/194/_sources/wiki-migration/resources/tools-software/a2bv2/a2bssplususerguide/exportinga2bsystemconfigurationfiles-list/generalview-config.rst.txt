:doc:`Click here to return Exporting A2B System Configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list>`

General View Configuration files
================================

The general view configuration files capture A2B system configuration information in more readable form and more functionality based rather than just register values. The information contained in these files correspond to the fields of ‘General View’ tab in the ‘Device Properties’ Window for all the nodes in the system.

Three files *adi_a2b_busconfig.c*, *adi_a2b_busconfig.dat*, *adi_a2b_busconfig.xml* are generated as part of BCF export.

A2B target software uses information in these files to discover, configure nodes and peripherals in the A2B system when using BF527/SHARC as the target processor or on a custom platform implementing A2B software Stack from ADI.

Bus Configuration Files (BCF)
-----------------------------

adi_a2b_busconfig.c
~~~~~~~~~~~~~~~~~~~

This file stores A2B schematic as function-based settings instead of register values. The target software internally parses this file to get the register settings for each node in an A2B network. BCF also contains node level stream information (up to 32 streams).

This file shall be exported to *.\\Target\\examples\\demo\\a2b-xx\\app path*. If the compressed BCF is exported then, ensure that the macro ‘ADI_A2B_BCF_COMPRESSED’ is defined (*.\\Target\\examples\\demo\\a2b-xx\\app\\a2bapp_defs.h*)

.. note::

   The adi_a2b_busconfig.c can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


adi_a2b_busconfig.xml
~~~~~~~~~~~~~~~~~~~~~

This file has schematic information in :doc:`XML format </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles/bcfxml>` which can be imported back. This allows user to apply different configurations to A2B system and verify the system behavior.

.. note::

   The adi_a2b_busconfig.xml can also be exported using thrift. For more information, you can refer to :doc:`Export of Busconfig Files using thrift </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`.


.. note::

   Manual editing of exported XML file is not recommended as the signature will be corrupted.

