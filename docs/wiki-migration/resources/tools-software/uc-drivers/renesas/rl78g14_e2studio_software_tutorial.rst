This section presents the steps for developing a software application that will run on the **Renesas Demo Kit for RL78G14** for controlling and monitoring the operation of the **ADI** part.

-  Run the **e2studio** integrated development environment.
-  Choose to create a new project (**File – New –C Project**).
-  Select **Executable (Renesas) - Sample Project** type and the **KPIT GNURL78-ELF** toolchain.
-  Name the project(**ADIEvalBoard** for example) and click **Next**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_1.jpg
   :align: center

-  In the **Select Target** field select **RL78G14-R5F104PJ-R5F104PJ** device, ensure that all the other settings are the same as in the picture below and click **Finish**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_2.jpg
   :align: center

-  Click OK to generate the project when the Project Summary window appears.
-  Open the project’s options window (**Project – Properties**).
-  Select **Settings** from the **C/C++ Build** category. In the **Tool Settings** tab, locate **Debug level** field and select **Level3: Maximum. Allows Macro Debugging(-g3)** and set the **Debug format** field to **DWARF**. Click **OK**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_3.jpg
   :align: center

-  Extract the files from the ADIDriver.zip archive and drag the folder with the files to the existing **src** folder in the Project Explorer. Delete the automatically generated C file: **ADIEvalBoard.c** from the project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_4.jpg
   :align: center
   :width: 850px

-  Before building the project there is one more step that needs to be done. Communication and TIME drivers use interrupts that have the service routines defined in the **interrupt_handlers.c** file. Open the file, declare **IICA0_Flag** as a char type and **overflowCounter** as a short type.

   -  Fill the **void INT_IICA0 (void)** with the following line: **IICA0_Flag = 1;**
   -  Fill the **void INT_TM00 (void)** with the following line: **overflowCounter++;**

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_5.jpg
   :align: center

-  The project is ready to be built. This can be done from the menu: select **Project-BuildProject**.
-  To download and debug the project select **Run-Debug Configurations…**, click on **Renesas GDB Hardware Debbugging** and select **ADIEvalBoard**, then click **Debug**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/renesas/rl78g14_e2studio_6.jpg
   :align: center
