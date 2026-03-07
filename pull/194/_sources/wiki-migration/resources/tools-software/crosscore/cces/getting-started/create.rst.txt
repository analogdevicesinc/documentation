Creating Projects in CCES
=========================

Workspace and Projects
----------------------

A CCES workspace is a folder (e.g. c:\\Users\\anon\\cces\\x.y.z) that contains project resources and metadata. When projects are created or imported, details about that project are stored in the workspace. The workspace metadata also includes preferences set through the CCES Preferences dialog box and IDE window layouts. By default, CCES creates new projects within your workspace folder.

Each time you start CCES, you will be prompted for a workspace location. You can opt to default to a workspace directory by choosing to use a workspace directory as your default. You will not be prompted the next time you open CCES.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/tools/360_workspace.jpg
   :width: 600px

Creating a New Project
----------------------

Launch the New Project Wizard using the **File → New → CrossCore Project** pull-down (Figure 1). If this is the first time CCES is being opened, a window will appear asking where to create the default *Workspace* on the host machine. The workspace is where all newly created projects and sub-directories will be stored on the PC. Select the desired pathname, and check the box to remember that location.

.. tip::

   If the Example Browser or Import Wizard were exercised during the reading of this Getting Started Guide, this process occurred when the first project was opened.


.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/create_a_project.gif
   :width: 800px

*Figure 1. New CrossCore Project*

The **General Project Information** window will appear (Figure 2). This is where a name is given to the project being created. Then click **Next**.

The next window is for **Processor Type**, which is where the processor being programmed is configured. Once the **Processor type** and its **Silicon revision** (branded on the processor package itself) have been set appropriately, click **Next**. Figure 2 depicts this window populated for a project targeting silicon revision 0.0 of the ADSP-SC573 SHARC processor.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/project_information.gif
   :width: 500px

*Figure 2. Project Information*

Now the **Project and Settings** window appears (Figure 3). In this window, you can add the different add-ins, communications, device drivers and system services, and middleware such as a RTOS kernel. *A separate project will appear for each processor core if using a multi-core processor.* Click on*\* Configure Project*\* to select your **Add-Ins** and **Template Code** – note that these options are distinct for each processor core. To see a summary of the add-ins and template code for each core, expand the **Configuration Summary** text box.

If you click on **Configure Project** for a processor core, the **Core Settings** window will appear. There are two tabs at the top of the window, **Add-In Selection** and*\* Template Code*\*.

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/project_configuration.gif
   :width: 600px

*Figure 3. Project Settings and Configuration*

In the*\* Add-In tab*\* you can select the add-ins desired for your project. *Add-ins* are preconfigured software that is available for the target processor, including code-generation GUI tools (e.g., Startup Code/LDF, Pin Multiplexing, PVP Programmer, etc.) and middleware libraries supporting device drivers, system services, USB/Ethernet stacks, and operating systems.

In the **Template Code** tab you are given the option to have CCES generate default code for getting you started in **C or C++**. You can also choose to have the generated code commented.

Once you are done in **Core Settings**, click **OK**, and then click **Finish** in the **Projects and Settings** window. Now your new project will appear along with all of the generated code, system services, and device drivers you have requested.

Importing a Project
-------------------

To import a project, use the **File → Import** pull-down, as shown in Figure 4:

.. image:: https://wiki.analog.com/_media/resources/tools-software/cces-gsg/import.gif
   :width: 600px

*Figure 4. Importing A Project*

In the **Select** window that comes up, under the **General** folder, select **Existing Projects into Workspace** and click **Next**.

In the **Import Projects** window, click **Browse…** next to the **Select root directory** text box and navigate to the root folder of the project you want to import. Once the root is selected, any projects in that directory (or any sub-directory) will appear in the **Projects** box. Check the box for the project(s) you want to import. Then click **Finish**.

.. important::

   Make sure the **Copy projects into workspace** option is selected if you want to preserve the original project and make a local copy to make edits to. **NOTE:** Files outside of the project folder will not be copied.


--------------

`CCES Getting Started#.|CCES Getting Started#config|System & Project Configuration <https://wiki.analog.com/_media/navigation CCES Getting Started#.>`_
