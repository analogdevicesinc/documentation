-  Open Xilinx Software Development Kit (XSDK) and provide the workspace location.

-  Create a new Application Project: go to **File -> New -> Application Project**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_app_project.png
   :alt: Creating a new application project
   :align: center
   :width: 650px

-  Create a new Hardware Platform: click **New** from the **Target Hardware** section

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_new_hardware.png
   :alt: Creating a new hardware platform
   :align: center
   :width: 450px

-  Specify the already generated Hardware Platform Specification File (more details about the generation: :doc:`/wiki-migration/resources/fpga/docs/build`): in the **Target Hardware Specification** section browse the desired file

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_hw_project.png
   :alt: Import hardware description file
   :align: center
   :width: 450px

-  Give a name to the project and to the board support package and click **Next**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/create_app_project.png
   :alt: Application project settings
   :align: center
   :width: 450px

-  Select the **Empty Application** templeta and click **Finish**

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/project_templates.png
   :alt: Choose application template
   :align: center
   :width: 450px

-  The new **Empty Application project** should look like:


|Empty application project|

.. important::

   Some applications (e.g. FMCOMMSx), when a Microblaze processor is used, requires an increased HEAP size for dynamic memory allocation. Make sure the HEAP size is at least **0x100000**.


   |image1|

-  Copy the source code files into the **src** directory
-  Make sure you uncomment the the required carrier vendor and CPU architecture from the **app_config.h** (or **config.h**) header file.

-  Example for choosing the Altera carrier in the **app_config.h** header file:

::

   //#define XILINX
   #define ALTERA

-  If there are multiple folders present in in the src one, include all the paths of the folders: go to the settings of the project and in the **C/C++ Build -> Settings -> Tool Settings -> gcc compiler -> Directories** section and add the paths of all the folders.

-  The SDK should automatically build the projects and the Console window will display the result of the build. If the build is not done automatically select the **Project -> Build Automatically** menu option.

-  At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system. You can program the FPGA by clicking on **Xilinx Tools -> Program FPGA**

-  After the FPGA was programmed, we need to create a new Run configuration, by selecting **Run** -> **Run Configurations...**, in the Run Configuration windows select the Xilinx C/C++ application (System Debugger) and click at the **New Configuration** button at the upper left corner.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/new_run_configurations.png
   :alt: Create new run configuration
   :align: center
   :width: 650px

-  If your target carrier has a Zync SoC, make sure, that you specify the **Initialization file**, and select the **Run ps7_init** and **Run ps7_post_config** options.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/zynq_init_file.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

-  At the **Application** tab define your current project name and application executable. (.elf)

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/elf_app.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

-  The output of the example program can be viewed in the SDK console by enabling the Connect STDIO Console option and setting the baud rate of the UART port to 115200.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/stdio_config.png
   :alt: Define Zynq initialization file
   :align: center
   :width: 650px

::

     * As an alternative a UART terminal can be used to capture the output of the example program. The number of used UART port depends on the computer's configuration. The following settings must be used in the UART terminal:
     * **Baud Rate:** 115200bps
     * **Data:** 8 bit
     * **Parity:** None
     * **Stop bits:** 1 bit
     * **Flow Control:** none

-  When the run configuration is done, the software can be started by clicking the **Run** button.

-  Your new bare metal application should run

.. |Empty application project| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/empty_project.png
   :width: 650px
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/ad9361_no_os_microblaze_heap_size.png
