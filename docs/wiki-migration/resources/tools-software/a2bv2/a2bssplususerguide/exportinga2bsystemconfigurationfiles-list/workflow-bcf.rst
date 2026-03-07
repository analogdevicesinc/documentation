:doc:`Click here to return Exporting A2B System Configuration files </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list>`

Working with Configuration XML files
====================================

The following sub-sections describe the workflow associated with using different configuration XML files, exported from SigmaStudio+, when building an A2B System.

Workflow using BCF files
------------------------

The below :doc:`Figure </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>` shows a typical workflow between A2B node suppliers and system architects/integrators when building an A2B system using Shape file and BCF.

A node supplier is responsible for designing the node’s functionality/TDM interfaces and verifying the design on SigmaStudio+. A verified node’s configuration, exported as shape file, shall be provided to A2B system integrator who would import individual node configuration files to build the final A2B system schematic on SigmaStudio+. A BCF .C file exported from such a verified schematic shall be used in the Target software.

Note that Custom Node Identifier needs to be set for nodes if node configuration is to be applied only upon Custom Node ID authentication as explained in :doc:`Custom Node ID based Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiversetting>`.


|image1|

.. container:: centeralign

   \ **Figure :** Work flow using Node Configuration and BCF


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/work_flow_using_ncfs_and_bcf.png
