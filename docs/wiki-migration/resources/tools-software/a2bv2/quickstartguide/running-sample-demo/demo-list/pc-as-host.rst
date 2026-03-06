:doc:`Click here to return to the Demo list </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list>`

Running sample Demo: PC as Host
===============================

Here is the list of examples schematic provided in the package:

-  :doc:`adi_a2b_3NodeRTMDemoConfig.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_3nodertmdemoconfig>`
-  :doc:`adi_a2b_AD2328WD1BZ_LPS_Custom.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2428wd1bz_lps_custom>`
-  :doc:`adi_a2b_AD2428WD1BZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2428wd1bz>`
-  :doc:`adi_a2b_AD2428WD1BZ_LPS_Custom.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2428wd1bz_lps_custom>`
-  :doc:`adi_a2b_AD2430WD1BZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2430wd1bz>`
-  :doc:`adi_a2b_AD2433WA1BZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2433wa1bz>`
-  :doc:`adi_a2b_AD2435WA3LZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2435wa3lz>`
-  :doc:`adi_a2b_AD2437A1MZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2437a1mz>`
-  :doc:`adi_a2b_AD2437A1MZ_sigmaDSP.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2437a1mz>`
-  :doc:`adi_a2b_AD2437A1NZ.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2437a1nz>`
-  :doc:`adi_a2b_ADSP21569Demo.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_adsp21569demo>`
-  :doc:`adi_a2b_ADZS2433MINI_ADSP21569_Multi_Main.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_adzs2433mini_adsp21569_multi_main>`
-  :doc:`adi_a2b_ADZS2435MINI_ADSP21569_Multi_Main.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_adzs2435mini_adsp21569_multi_main>`
-  :doc:`SigmaDSP_Integration.ssprj </wiki-migration/resources/tools-software/a2bv2/quickstartguide/running-sample-demo/demo-list/pc-as-host/adi_a2b_ad2428wd1bz>`

Steps to run demo in PC mode
============================

The following steps describe the procedure to run a sample demo in PC mode

-  Open an A2B schematic from (<A2B plugin for SigmaStudio+ installation path>>\\Schematics\\PC).


|image1|

.. container:: centeralign

   \ **Figure:** Sample demo schematic in PC mode


-  Make sure that .xml files are provided for programming on main and sub A2B evaluation boards, the procedure to find the peripheral settings window is as follows:

   -  Open the platform view either by double clicking on the platform or by clicking on “Canvas” option under the platform in the Project tree as shown in figure.


   |image2|

.. container:: centeralign

   \ **Figure:** Platform view in SigmaStudio+


-  The peripheral settings can be opened by double clicking on the peripheral or by clicking on the “Settings” option under the peripheral in project tree and select the xml as shown in figure.



|image3|

.. container:: centeralign

   \ **Figure:** Peripheral Settings window


-  **Note:** The adi_a2b_main_ADAU1452.xml, adi_a2b_main_ADAU1761.xml, adi_a2b_sub_ADAU1961.xml files are available in <A2B plugin for SigmaStudio+ installation path>>\\Schematics\\PC\\xml folder

-  Make sure that USBi cable is connected to eval board as shown in figure and the board is powered on.
-  Click on “LinkCompileDownload” icon in SigmaStudio+ as shown in figure. This will start the discovery and configuration of A2B nodes and peripheral devices as per the schematic.

|image4|

.. container:: centeralign

   \ **Figure:** Link-Compile-Download option in SigmaStudio+


-  After successful discovery and initialization audio routing can be observed as per the sample demo configuration.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/sample_demo_schematic_in_pc_mode.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/platform_view_in_sigmastudio_.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/peripheral_window_new.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/quickstartguide/link_compile_download.png
