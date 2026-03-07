Creating a Boot Image (Dual-Core ADSP-SC5xx Processors)
=======================================================

CCES supplies pre-built initialization files for the ADSP-SC5xx EZ-KIT Lite, as well as source code which can be modified to support custom boards with other CLKIN values and/or alternative DDR memory. The pre-built files can be found in the **<CCES Root>\\SHARC\\ldr\\** directory. The CCES source code projects are in **<CCES Root>\\SHARC\\ldr\\init_code\\SC57x_init\\**.

.. tip::

   For our example project no code changes are needed so we can use a pre-built initialization file.


Let's start with our existing :doc:`ADSP-SC573 blink application </wiki-migration/resources/tools-software/crosscore/cces/getting-started/led-blink-app>`. The application is made up of three projects, one for each core of our ADSP-SC573 processor. To recap, core 0 is our ARM Cortex-A5 core and cores 1 and 2 are our SHARC+ cores:

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/01_project_setup.png

*Figure 1: Three-core blink example project*

To build the application and create a bootable image:
-----------------------------------------------------

1. In **Project Explorer** select the three projects by holding down the **SHIFT** key and clicking each project's folder. Select **Project → Build Configurations → Set Active → Debug** pull-down menu


|image1|

*Figure 2: Setting the build configuration*

2. In the **Project Explorer** view, right-click the project for the appropriate core (see note) and select **Properties**

.. important::

   The loader image must be built using the last active project in your application. If your application uses only core 0, core 0 must also be used to build the loader image. If you use cores 0 and 1, use core 1. If using cores 0, 1, and 2, use core 2.


3. In the **Properties** window, go to the **Build → Settings** page and select **Build Artifact → Artifact Type → Loader File**

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/03_select_build_artifact_1920.gif

*Figure 3: Specifying loader file as build artifact*

.. tip::

   The **Build Settings** page has several tabs. If not all tabs are visible, use the left/right arrow buttons located beneath the **Manage Configurations...** button to scroll through all available tabs.


4. On the **Tool Settings** tab, go to the **CrossCore SHARC Loader → General** page and select these settings:

-  Boot mode: **SPI Master**
-  Boot format: **Intel Hex**
-  Boot Code: **0x01**

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/04_tool_settings_1920.gif

*Figure 4: Specifying loader properties*

5. Go to the **CrossCore SHARC Loader → Initialization** page and add the pre-built initialization file by clicking **Browse…** and navigating to **<CCES Root>\\SHARC\\ldr\\ezkitSC5XX_initcode_core0**:

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/05_select_initcode_1920.gif

*Figure 5: Specifying an initcode file*

6. Click **Apply and Close**

7. Build your application. Click the hammer icon in the toolbar or press **CTRL-B**

8. In **Project Explorer**, click on the loader file project (core 2 in our example) and select **Properties**

9. On the \*\* Tool Settings*\* tab under **CrossCore SHARC Loader** → **Executable Files**, specify an executable to be run on each of your processor's cores by clicking **Browse...**. CCES automatically opens your operating system's file manager in the root folder of the project associated with each core. The executable should be in the Debug folder. For core 0 (ARM) projects the executable has no file extension. For SHARC cores (1 and 2), the executable has the file extension ``.dxe``

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/06_select_executables_1920.gif

*Figure 6: Specifying executables to be included in loader image*

.. tip::

   The video only shows executables being loaded to cores 0 and 1. Our demo uses all three cores so don't forget to also load an executable for core 2!


10. Rebuild the loader file project to generate the loader image file. In **Project Explorer** right click the core 2 project and select **Build Project**. A ``*_core*.ldr`` file should be generated in the loader project's Debug folder

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/06_loader_file_built.png

*Figure 7: The loader file has been created*

11. Return to the :doc:`previous page </wiki-migration/resources/tools-software/crosscore/cces/getting-started/app>` to learn how to flash your loader file and application to your device.

*Aside:* When an application is loaded to a target using the debugger, the IDE can configure external memory as long as the processor is homogeneous (i.e. it has only SHARC cores). However, for heterogeneous processors, such as the ASDP-SC5xx series, which have an ARM core plus one or two SHARC cores, a *preload file*, equivalent to an initialization file, is required. As with initialization files, pre-built preload files are located in the **<CCES Root>\\SHARC\\ldr\\** directory, and CCES projects for customization can be found in **<CCES Root>\\SHARC\\ldr\\init_code\\SC57x_init\\** directory. The master core is generally the only core that needs a preload file, so a new **Debug Configuration** session automatically includes the preload file as one of the applications that is to be loaded. For an ADSP-SC5xx processor, the preload file is included in the ARM© Core 0 project. More information about proper preload file configuration can be found in CCES Online Help under **CrossCore® Embedded Studio 2.9.0 → Integrated Development Environment → Debugging Targets → Debugging ADSP-SC5xx SHARC Targets → About Preload Files**.

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#boot-app-bf60x
   :alt: Creating a Boot Image (ADSP-BF60x)#.app|Creating Bootable Applications#.app|Creating Bootable Applications

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/01_build_configuration_1920.gif
