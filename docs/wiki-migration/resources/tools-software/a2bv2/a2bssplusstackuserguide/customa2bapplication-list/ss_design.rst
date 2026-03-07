:doc:`Click here to return to Building on A2B Application </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication-list>`

Designing A2B Schematic on SigmaStudioPlus
==========================================

This step is required to create a bus configuration file that stores the complete A2B network information required by the Target software running on the custom platform. An A2B schematic, corresponding to the Targeted application shall be designed and validated on SigmaStudioPlus before exporting the bus configuration file. The steps involved in this process are as follows

1. Build an A2B Schematic on SigmaStudioPlus matching your final A2B system

-  Refer :doc:`Drawing A2B Schematics </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/drawinga2bschematics>` for drawing an A2B schematic on SigmaStudioPlus. Ensure

   -  Audio streams are defined and assigned for the network.
   -  Configuration is provided for all A2B nodes and connected peripheral devices.

2. Validate the A2B Schematic using the PC as the host processor

-  Refer to the example in :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` to discover an A2B network using a PC as a Host
-  Link-compile-download and confirm successful network discovery, configuration, and audio routing.
-  Debug discovery issues (if any) using ‘Tracing’, ‘Sequence Chart’, and other features.

3. Perform Network analysis to ensure the drawn schematic matches the requirements of the end system

-  Check for Bandwidth usage per Node/Network.
-  Run Bit error Test for the network.
-  Check Power usage for the network.

4. Define application response to line faults (if required)

-  Auto-rediscovery upon faults, no. of attempts, etc.
-  Verify line fault handling/rediscovery upon line faults.

5. After successful validation, export **Bus Configuration.C** file for the validated A2B schematic.

6. Bus configuration file can also be exported as a binary file using the “\ **Dump as .dat**\ ” option.

NOTE
----

MACROS to enable/disable based on the type of file used for configuration of the A2B Network.


|image1|

.. container:: centeralign

   \ **Table:** MACRO Information


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplusstackuserguide/macros_stack.png
