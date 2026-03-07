-  Open **Nios II (Quartus Prime)** and provide the workspace location.

-  Create a new Application Project: go to **File -> New -> Nios II Application and BSP from Template**

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/new_app.png
   :alt: Creating a new application project
   :align: center
   :width: 650px

-  Add a new Hardware Platform: click **...** from the **Target Hardware information** section.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/config_hw_platform.png
   :alt: Creating a new hardware platform
   :align: center
   :width: 450px

-   Specify the already generated Hardware Platform Specification File (more details about the generation: :doc:`/wiki-migration/resources/fpga/docs/build`): in the **SOPC Information File name** section and browse the desired file.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/config_hw_platform_2.png
   :alt: Config HW 2
   :align: center
   :width: 450px

-  Give a name to the project and select the **Blank Project** template and click **Finish**

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/config_new_proj.png
   :alt: Config new project
   :align: center
   :width: 450px

-  The new **Blank project** should look like:

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/blank_proj.png
   :alt: Blank project
   :align: center
   :width: 650px

-  Create a new folder called **src** under **sw** folder

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/new_folder.png
   :alt: New folder
   :align: center
   :width: 650px

-  Copy all the source code files into the **src** directory.

-  The SDK should automatically build the projects and the Console window will display the result of the build. If the build is not done automatically select the **Project -> Build Automatically** menu option.

-  At this point the software project setup is complete, the FPGA can be programmed and the software can be downloaded into the system.

-  You can program the FPGA by opening **Programmer (Quartus Prime)** provided by the Quartus Prime Software Suite. Click the **Auto Detect** button. The detected devices should be displayed now in the device list.

::

    {{ :resources:fpga:altera:programmer.png?650 |Programmer}}
   * Double-click the first device under the **File** column and browser for the **.sof** file required for the project. Make sure the **Program/Configure** column is checked. Press the **Start** button to program the FPGA.
    

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/add_sof.png
   :alt: Empty application project
   :align: center
   :width: 650px

-  After the FPGA was programmed, we need to create a new Run configuration in the Nios II project, by selecting **Run** -> **Run Configurations...**, in the Run Configuration windows select the **Nios II Hardware** and click at the **New Configuration** button at the upper left corner.

.. image:: https://wiki.analog.com/_media/resources/fpga/altera/run_config.png
   :alt: Create new run configuration
   :align: center
   :width: 650px

-  At the **Project** tab define your current project name and application executable. (.elf)

-  On the Target Connection tab, press the **Refresh Connections** button. You may need to expand the window or scroll to the right to see this button.

-  Check the **Ignore mismatched system ID** option.

-  Check the **Ignore mismatched system timestamp** option.

-  The output of the example program can be viewed in the Console Window.

-  When the run configuration is done, the software can be started by clicking the **Run** button.

-  Your new bare metal application should run
