:doc:`Click here to return to Building Target software for a custom platform </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication-list/target>`

Apply A2B Network configuration
===============================

After completing all steps as mentioned in Section "**Porting A2B Software Stack to a custom platform**", the next step is to apply bus configuration to the Target software.

1. In the Target platform project, include the validated bus configuration file (**adi_a2b_busconfig.c**), exported by following Section ":doc:`Designing A2B Schematic on SigmaStudioPlus </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/customa2bapplication>`".

-  Replace the existing in **.\\Target\\a2bstack\\demo\\<a2b-xx>\\app.**

2. Optionally, if the bus configuration is read from a binary file, replace the exported .dat format of the bus configuration file into the file system path (A2B_CONF_BINARY_BCF_FILE_URL).

3. Optionally, the audio routing table (.\\app\\adi_a2b_audioroutingtable.c) may need to be modified if the audio streams are to be routed by the audio host.

-  In case where the A2B controller is also the audio host for the network then modify the audio routing table as explained in :doc:`System Requirements </wiki-migration/resources/tools-software/a2bv2/quickstartguide/systemrequirements>`. Otherwise, the routing has to be modified in the audio host. :doc:`Running the Sample Demo </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo>` explains this process when using ADAU1452 as an audio host on ADI A2B evaluation boards such as EVAL-AD2425WDZ and EVAL-AD2428WD1BZ.

.. note::

   This step is not required if stream definition and the routing is defined in SigmaStudioPlus where streams are sourced and consumed within A2B nodes and not routed by the Audio Host.


4. Build and Run the Target project.

-  Use the build/flash tools provided by your development environment (IDE) to build and run the executable image.
-  A2B Network should get discovered and configured as per the added bus configuration file. Refer to Section ":doc:`Post-Discovery APIs </wiki-migration/resources/tools-software/a2bv2/a2bssplusstackuserguide/applicationintegration>`" for Debugging help.
