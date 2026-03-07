Creating a boot image (single-core processors)
==============================================

CCES supplies the project for the initialization requirements for the ADSP-BF707 EZ-Kit Lite, which can be modified to support custom boards with other CLKIN values and/or alternative DDR memory. The project can be found in the **\\Blackfin\\ldr\\init_code\\BF707_init\\BF707_init_vxx** directory, where the xx indicates the board revision being used. For this exercise of generating a loader file, no modifications to the code are necessary, but the DXE file will need to be built if it hasn’t been built before. To do this, open the BF707_init_vxx project and build it. After it builds, the **BF707_init_vxx.dxe** file will be generated in the **\\Debug** directory of the project. Note the path to this DXE file, as it will be required later.

With the initialization DXE generated and the application DXE finalized, the loader file must be created:

1. Select the **Project → Build Configurations → Set Active → Debug** pull-down menu

2. In the **Project Explorer** view, right-click on the project name and select **Properties**

3. In the **Properties** window, go to the **C/C++ Build → Settings** page and select the **Build Artifact** tab. Under **Artifact Type**, select **Loader File**.

4. On the **Tool Settings** tab, go to the **CrossCore Blackfin Loader → General** page and input the settings as follows:

-  Boot mode: **SPI0 Master**
-  Boot format: **Intel Hex**
-  Output width: **16 bits**
-  Boot Code: **0x01**
-  Make sure **Use default start address** is checked
-  Add the initialization file by clicking **Browse…** and navigating to
   <CCES Root> \\Blackfin\\ldr\\init_code\\BF707_init\\BF707_init_v00\\Debug\\BF707_init_v00.dxe
-  The window should now resemble Figure 28. Click **OK.**

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/loader_file_settings.png
   :width: 600px

*Figure 2. Loader File Settings in Project Properties*

6. Use the **Project → Build Project** pull-down menu to generate the LDR file for the project.

With the loader image generated, it is ready to be programmed into the boot source memory, which will require use of the **Command-Line Device Programmer (CLDP)**.

--------------

`Creating Bootable Applications#.app|Creating Bootable Applications#boot-app-bf60x|Creating a Boot Image (ADSP-BF60x) <https://wiki.analog.com/_media/navigation CCES Getting Started#.app>`_
