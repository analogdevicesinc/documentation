Debugging Applications
======================

When you are ready to start debugging your application, you must first build your projects. To do so, use the **Project → Build All** pull-down. Once the application is built, you can then go into the **Debug** perspective by clicking **Debug** in the top right of the CCES window.

To debug your application, make sure you have selected the project for Core 0 (for multi-core projects) in the left-side **Project Explorer** window and select the **Run → Debug** pull-down to connect to your target processor. If you have not set up a **Debug Configuration** yet, go **to Run → Debug As → Application with CrossCore Debugger** and create a new **Debug Configuration** using the **Session Wizard**. In the **Select Processor** window, select the processor and click **Next**.

The next window asks you to select the environment in which you want to connect to your processor, whether it is via an **Emulator**, as an **EZ-Kit Lite**, or (for processors that support it) as a functional **Simulator**. You need to pick the environment suitable for your configuration, then click **Next**.

The next window is the **Select Platform** window, which will vary depending on the previous selection. For Debug Agent targets, there would be only one platform to pick here but for simulators and emulators, there may be multiple platforms to choose from. Select the one appropriate for your emulator, then click **Finish**.

.. image:: https://wiki.analog.com/_media/resources/tools-software/crosscore/cces/getting-started/debugging.gif

*Figure 1. Running a Debug Configuration*

Launch Configuration
--------------------

The launch configuration allows for some additional options during the debugging of the processor depending on the processor being used.

Since the ADSP-SC573 processor has 3 cores, users have the option to load applications to all 3 cores. Users can also load multiple applications to the same core which is often the case for the ADSP-SC5xx processor. By default, a pre-load file is loaded first which will setup anything needed prior to loading the actual application on the booting core. The pre-load file normally will setup external memory but really could be used for anything the user wants prior to loading their application. There are additional options available to change for each core that are discussed in the CCES online help system.

Here are a few of the important tabs that are part of the launch configuration window:

-  **Automatic Breakpoints** - Manage user-defined automatic breakpoints and select system-defined and user-defined automatic breakpoints to set after loading a program
-  **Target Options** - Allows users some additional control such as halting a core after connecting to the target board or halting peripherals when suspending the core
-  **Custom Board Support** - Used to override default register reset values with custom memory-mapped registers

.. warning::

   Before proceeding, make sure your target board is powered and properly connected to the PC (via Debug Agent or Emulator).


Once all necessary options have been updated and hardware power and connections are confirmed, click **Debug** in the **Debug Configurations** window or the Debug icon in the main window to launch the Debug perspective and connect to your processor.

Once the processor has connected, the program will run to main() and halt. The **Run** pull-down contains the functions for running, stopping, pausing and stepping through your application (Figure 2).

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/run_menu.png
   :width: 200px

*Figure 2. Run Menu*

Note that these functions operate on the processor’s individual cores – the core to be affected can be selected from the tree structure in the **Debug** view (Figure 6). The **Run** pull-down also contains analogous **MP** commands that affect all cores in a multi-core processor.

Setting Breakpoints
-------------------

One of the most important features of debugging an application is being able to set breakpoints within your code. CCES provides you with two types of breakpoints, hardware breakpoints and software breakpoints.

**Software breakpoints** are handled in emulator/debug agent firmware. Essentially, the emulator keeps a record of all the places software breakpoints are established and replaces those instructions in memory with a private instruction with special bit encodings so that execution can stop at the breakpoint, at which point the emulator swaps back in the actual instruction that should be run when the program is resumed from the breakpoint.

**Hardware breakpoints** allow much greater flexibility than software breakpoints and require much more design thought and resources within the processor. At the simplest level, hardware breakpoints are helpful when debugging ROM code, where software breakpoints are not possible due to the need to write the instruction memory dynamically to support the breakpoint. As hardware breakpoint unit capabilities are increased, so are the benefits to the developer. At a minimum, an effective hardware breakpoint unit will have the capability to trigger a break on load, store, and fetch activities. Additionally, address ranges, both inclusive (bounded) and exclusive (unbounded) should be included.

To set a breakpoint, go to the desired line of code and right-click on the gutter to the left of the Editor view (the blue shaded area). Then select **Toggle Breakpoint**, **Toggle Hardware Breakpoint** or **Toggle Software Breakpoint**, as shown in Figure 3. Once a breakpoint is set, this same toggle will remove the breakpoint, and control of the software breakpoints is also available in the **Breakpoint** view.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/breakpoint.png
   :width: 200px

*Figure 3. Setting a Breakpoint*

After you have placed your breakpoints, you can then resume the debug session via the **Run → Resume** pull-down, by striking the **F5** key, or by clicking the green resume arrow in the **Debug** view toolbar.

Viewing Variable Values
-----------------------

We can also find the value of a variable in our application. Go to the **Expressions** view, which can be found in **Window → Show View → Expressions**. Click on *Add new expression*, type the variable name in the new expression text box. Hit Enter, and you will see the **Expressions** view populate the **Type** and **Value** columns for the variable, as shown in Figure 4.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/expression_view.png
   :width: 400px

*Figure 4. Expression View of Example Variable x*

Note that any value that has changed since the last suspension point will be highlighted in yellow. This is extremely useful if you are trying to debug multiple variables at the same time. Additionally, note that each core has its own set of variables, so the value of an expression can change or become invalid when a different processor is selected.

Other Debugging Views
---------------------

Some other useful views that aid in debugging that can be found under **Window → Show View** include:

-  The **Memory Browser** view allows you to see the contents at each of the memory locations in your processor and any mapped memory. If you have the SPI memory mapped on your processor, you can also use this tool to view the SPI flash memory.

-  The **Register Browser** allows you to view the status and values of all the registers within the target processor. This is extremely useful when debugging peripherals and determining the state of each register.

-  If you are working with image processing, the **Image Viewer** view allows you to view images stored on your PC and images stored in memory on your target processor while connected to an Emulator session. This tool is extremely useful when using ADI’s Image Processing Tool Kits and when working with the Pipeline Vision Processor (PVP) on the ADSP-BF60x processors.

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#help
   :alt: Online Help & Example Browser#.|CCES Getting Started#bsp|Board Support Packages
