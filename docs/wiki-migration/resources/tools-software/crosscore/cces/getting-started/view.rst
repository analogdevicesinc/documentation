Perspectives & Views in CCES
============================

A *Perspective* is an instantiation of the CCES IDE dedicated to a specific collection of tasks. It consists of a unique set of windows/panes called *Views*. The primary perspectives in CCES are the **C/C++**, **Debug** and **Graphical Editor** perspectives.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/open_perspectives.png
   :width: 800px

*Figure 1. Available Perspectives*

Information and documentation on these perspectives & views, and others, is located in the CCES Online Help.

C/C++ Perspective
-----------------

The **C/C++** perspective is where you actually develop the code for your application (Figure 2). In this perspective, you create your source and header files, and then edit, save and compile them into executable files (DXE), static libraries (DLB), or loader images (LDR).

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/c_c_perspective.png
   :width: 600px

*Figure 2. C/C++ Perspective*

In the **C/C++** perspective, there are many **Views** that are available, such as the **Project Explorer**, **Editor** and **Console** views. The full list of **Views** is available via the **WindowShow View** pull-down.

-  The **Project Explorer** view contains the directories of all the projects currently open in CCES. Here, you can open individual *resources* (source and header files) associated with your projects.

-  The **Editor** view is where you make changes to resources that are opened in CCES. The editing features built into CCES will dynamically change text color depending on if it’s a recognized API, system variable, instruction, data type, or comment. This is called syntax coloring in Eclipse.

-  The **Console** view is where the tool chain outputs to when building your project. Standard I/O from library functions like printf() also output to the **Console** view.

-  The **Outline** view to the right provides a skeletal mapping of the open resource showing included header files and any defined macros, functions, and global data, which allows for easy navigation within the resource to where the label is defined/used within the file.

Besides these default views, a number of others are also available via the **Window → Show View** pull-down to be added to the perspective and managed. Online Help can be consulted for specific guidance as to what the views are and how to use them.

Debug Perspective
-----------------

The **Debug** perspective (Figure 3) is available when you are ready to run your code on a hardware target or in the simulator (if there is simulator support for the processor you are targeting). In this perspective, you can set breakpoints, step through code, and access different views that assist greatly during development efforts, like memory and register browsers.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/debug_perspective.png
   :width: 600px

*Figure 3. Debug Perspective*

-  The **Debug** view will show you each core of your target processor session (which can be a single processor featuring one core, a single processor with multiple cores, or a scan path comprised of any combination of the two) and the application loaded into that core.

-  The **Disassembly** view shows the compiled code in Assembly, after it has been downloaded to your target processor. In this view, you can place breakpoints and step through your application in assembly code. Editing of the disassembly source is also possible by right-clicking a specific address and selecting **Edit OpCode…**

-  The **Editor** view in the center functions similarly to the same view in the C/C++ perspective, but in the Debug perspective, breakpoints can be set in the C source files.

-  The **Console** view at the bottom also functions similarly to the same view in the C/C++ perspective, except run-time console output from functions such as printf() will also appear here.

The open space to the upper right is a tabbed-area view where numerous low-level views can be opened to support specific debug tasks, all of which are available via the **Window → Show View**. Some useful views include:

-  The **Memory Browser** view allows you to see the contents at each of the memory locations in your processor and any mapped memory. If you have the SPI memory mapped on your processor, you can also use this tool to view the SPI flash memory.

-  The **Register Browser** allows you to view the status and values of all the registers within the target processor. This is extremely useful when debugging peripherals and determining the state of each register.

-  The **Expressions** view can be used to give you quick access to specific global data (including contents and addressing) and registers.

-  If you are working with image processing, the **Image Viewer** view allows you to view images stored on your PC and images stored in memory on your target processor while connected to an Emulator session. This tool is extremely useful when using ADI’s Image Processing Tool Kits and when working with the Pipeline Vision Processor (PVP) on the ADSP-BF60x processors.

Further information about these views and the others available is located in CCES Online Help.

Graphical Editor Perspective
----------------------------

The **Graphical Editor** perspective was designed for use with GUI Add-ins, such as the PVP Programmer for the ADSP-BF60x series processor, which is intended to provide a graphical environment for code generation. In order to use this perspective, users must be actively debugging the processor.

-  The **Pipeline Viewer** is a new view that allows you to observe the contents of a processor’s instruction pipeline over time, using a Cycle-Accurate Simulator (not a Functional Simulator) as the target. With this view, you can view how much pipeline your program is using, and with this information further optimize your application code.

-  The **Profiling View** is used to observe where a program spends most of its time executing code. You can analyze the profiling data and optimize your code to eliminate the bottlenecks.

Further information about these views and the others available is located in CCES Online Help.

--------------

.. image:: https://wiki.analog.com/_media/navigation CCES Getting Started#config
   :alt: System & Project Configuration#.|CCES Getting Started#help|Online Help & Example Browser
