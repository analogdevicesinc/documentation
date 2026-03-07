This section presents the steps for developing a software application that will run on the **Renesas Demo Kit for RL78G13** for controlling and monitoring the operation of the **ADI** part.

-  Run the **IAR Embedded Workbench for Renesas RL78** integrated development environment.
-  Choose to create a new project (**Project – Create New Project**).
-  Select the **RL78** tool chain, **the Empty project** template and click **OK**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_01.png
   :align: center

-  Select a location and a name for the project (**ADIEvalBoard** for example) and click **Save**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_02.png
   :align: center

-  Open the project’s options window (**Project – Options**).
-  From the **Target tab** of the **General Options** category select the **RL78 – R5F100LE** device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_03.png
   :align: center

-  From the **Setup** tab of the **Debugger** category select the **TK** driver and click **OK**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_04.png
   :align: center

-  Extract the files from the lab .zip archive and copy them into the project’s folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_05.png
   :align: center

-  The new source files have to be included into the project. Open the **Add Files…** window (**Project – Add Files…**), select all the copied files and click open.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_06.png
   :align: center

-  At this moment, all the files are included into the project.
-  The project is ready to be compiled and downloaded on the board. Press the F7 key to compile it. Press CTRL + D to download and debug the project.
-  A window will appear asking to configure the emulator. Keep the default settings and press OK.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_07.png
   :align: center

-  To run the project press F5.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_without_applilet3_08.png
   :align: center
