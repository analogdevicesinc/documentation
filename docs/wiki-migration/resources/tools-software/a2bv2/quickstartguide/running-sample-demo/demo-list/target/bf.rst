:doc:`Click here to return to Running sample Demo: Target as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/target>`

To run BF with AD2433 setup
===========================

-  Open "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC\\adi_a2b_AD2433WA1BZ.ssprj" in SigmaStudio+
-  Link compile the project and navigate to **Export Import Setting** under Network-> A2BNetwork->A2B_x in **Project**
-  Select the File path in Bus Config.c file and export the file.
-  Replace / copy the exported file to "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\app" folder.
-  Select the File path in .Dat and export the file.
-  Replace / copy the .dat file to "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf".
-  :doc:`AD2433WA1BZ jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` and :doc:`AD2433WB1BZ jumper setting </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` must be done.
-  :doc:`Hardware setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad243x-standard-power>` must be done.
-  Refer :doc:`loading network configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list>` to run target example from either .dat or .bcf
-  Refer :doc:`Running sample demo with BF as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/bf-as-host>` to run the demo

To run BF with AD2428 setup
===========================

-  Open "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Schematics\\PC\\adi_a2b_AD2428WD1BZ.ssprj" in SigmaStudio+
-  Link compile the project and navigate to **Export Import Setting** under Network-> A2BNetwork->A2B_x in **Project**
-  Select the File path in Bus Config.c file and export the file.
-  Replace / copy the exported file to "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf\\app" folder.
-  Select the File path in .Dat and export the file.
-  Replace / copy the .dat file to "C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-bf".
-  :doc:`AD2428WD1BZ jumper settings </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` must be done.
-  :doc:`Hardware setup </wiki-migration/resources/tools-software/a2bv2/quickstartguide/hardware-setup/ad242x-standard-power>` must be done.
-  Refer :doc:`loading network configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles-list>` to run target example from either .dat or .bcf
-  Refer :doc:`Running sample demo with BF as Host </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/bf-as-host>` to run the demo
