This section presents the steps for developing a software application that will run on the **Renesas Demo Kit for RL78G13** for controlling and monitoring the operation of the **ADI** part.

Two software applications have to be used: **Applilet3 for RL78G13** (a tool that automatically generates device drivers for MCU peripheral functions) and **IAR Embedded Workbench for Renesas RL78** (the integrated development environment).

Step 1 - Applilet3 for RL78G13
==============================

-  Run the **Applilet3 for RL78G13** tool and create a new project for **R5F100LE** processor. Select **IAR Compiler** build tool, a project name, a location for the new project and press **OK**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_01.png
   :align: center

-  Keep the default **Pin assignment** setting and click **Fix settings**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_02.png
   :align: center

-  Now the desired peripherals can be configured and the code can be generated. For example, if the clocked serial interface 10 (**CSI10**) has to be configured, select the **Serial** peripheral, choose for the Channel 2 of Serial Array Unit 0 (**SAU0**) the **CSI10** interface, **Transmit/receive function** option and then go to **CSI10** tab.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_03.png
   :align: center

-  To configure the **CSI10** interface for serial transmissions of 8 bits, with MSB first, with the data captured on clock's rising edge, with a frequency of the clock of 1 MHz and the idle state high, the settings from the following image have to be made.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_04.png
   :align: center

-  After all the desired peripherals are configured click on the **Generate Code** button and a new workspace and a new project for the **IAR Embedded Workbench** will be generated. After the code was generated close the **Applilet3 for RL78G13** tool.

Step 2 - IAR Embedded Workbench for Renesas RL78
================================================

-  Run the **IAR Embedded Workbench** and open the workspace created with the **Applilet3** tool.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_05.png
   :align: center

-  Copy the files extracted from the zip file into the **user_src** folder, located in the project’s folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_06.png
   :align: center

-  The new source files have to be included into the project. Add in the **user_src** group the files from the corresponding folder (Right click on the group and select **Add – Add Files…**). Because a new **Main** file was included the **r_main.c** file from the **applilet_src** group has to be deleted (Right click on the file and select **Remove**).

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_07.png
   :align: center

-  Now the debugger driver has to be selected from the project’s options. Right click on the project name and select **Options**. From the **Debugger** category choose the **TK** Debugger Driver.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_08.png
   :align: center

-  Now, the project is ready to be compiled and downloaded on the board. Press the **F7** key to compile it. Press **CTRL + D** to download and debug the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g13_software_tutorial_09.png
   :align: center
