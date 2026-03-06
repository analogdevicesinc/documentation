:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

Running Sample Demo ADSP-SC594 as Host
======================================

The sample demo can be run using ADSP-SC594 as the host. In this case the ARM core of host processor controls the discovery and programming of A2B nodes in the system. The following steps shows how to run sample demo

-  Perform hardware modification and jumper setting as per [[:resources:tools-software:a2bv2:quickstartguide:running-sample-demo#hardware_setup]AD2430 jumper setting]. Maintain the hardware configuration for the SOM and SOM-CRR ez kit as per the recommended default configurations of their respective manuals.
-  Open CCES v2.11.0 and click on File → Import → ‘Existing projects into work space’.
-  Browse to the folder C:\\Analog Devices\\ADI_A2B-SSPlus_Software-Relx.y.z\\Target\\examples\\demo\\a2b-adsp-sc59x
-  Build the project using Project → Build Project option.
-  Make all the connections described in section connections.
-  Turn ON power to the SOM-CRR and A2B Main node.
-  Connect the JTAG to PC.
-  \* **Note:** If Emulator is used the first time: Create a new debug configuration using Run- >Debug Configurations, create new session, select ADSP-SC594 and click NEXT, select Emulator and click NEXT, choose In-Circuit Emulator platform (typically: ADSP-SC594 via ICE1000) and click NEXT, then click FINISH.
-  Select a debug configuration and press F5 to run the project.
