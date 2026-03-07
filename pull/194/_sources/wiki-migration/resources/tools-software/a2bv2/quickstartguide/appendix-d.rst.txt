:doc:`Click here to return to Using ADSP-21569 EZ-Kit </wiki-migration/resources/tools-software/a2bv2/quickstartguide/adsp-21569_ez-kit>`

Building ADSP-2156x Project
===========================

To build the ADSP-2156x project from the SS+ installer path: “C:\\Analog Devices\\SigmaStudioPlus-Relx.y.z\\Target\\Examples\\Demo\\ADSP-2156x\\ADSP-21569\\SS_App_Core1”, following steps need to be followed.

-  Import the project into CCES
-  Open “Properties” by right clicking on the project and navigate to “C/C++ Build -> Settings”
-  Remove the macro “ADSP_21569_SOM” from the CrossCore Sharc C/C++ Compiler/Preprocessor Menu as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/removal_of_macro_new.png
   :align: center

.. container:: centeralign

   \ **Figure:** Removal of Macro


-  To provide BCLK and Frame Sync to A2B transceiver, navigate to “system.svc” in the project and open “Signal Routing Unit”.
-  Under “DAI0 Pin Buffer” following changes need to be made.

   -  **DAI0_PB03_I** which is routed to PCG0_CRS_CLKC_O by default should be routed removed and **PCG0_CLKA_O should be added**. Final configuration is shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/dai0_pb03_i_configuration.png
   :align: center

.. container:: centeralign

   \ **Figure:** DAI0_PB03_I Configuration


-  **DAI0_PB04_I** which is routed to PCG0_CRS_FSC_O by default should be routed removed and **PCG0_FSA_O should be added**. Final configuration is shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/dai0_pb04_i_configuration.png
   :align: center

.. container:: centeralign

   \ **Figure:** DAI0_PB04_I Configuration


-  In the file “C:\\Analog Devices\\CrossCore Embedded Studio 2.X.Y\\SHARC\\include\\drivers\\sport\\ adi_sport_2156x.h”, the value of **ADI_SPORT_BLOCKING_MODE** must be set to “1u” as shown in below Figure.

.. image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sport_blocking_mode_macro_value_update.png
   :align: center

.. container:: centeralign

   \ **Figure:** SPORT Blocking Mode Macro Value Update


-  Once these changes are made, build the project and copy the generated .dxe file to <<A2B plugin for SigmaStudio+ installation path>>\\Target\\Utility\\LDR folder.
-  Use “LDR_gen.bat” script available in <<A2B plugin for SigmaStudio+ installation path>>\\Target\\Utility folder to generate the LDR and “Flash_LDR.bat” to flash the updated LDR to ADSP-2156x eval board.
