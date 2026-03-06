Build Xilinx Projects
=====================

Windows
-------

create_xilinx_sdk_project.bat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script can be run with no parameters. In this case, you will be asked to introduce the path and the name of the .hdf file and the path and the name of the folder where the project will be created.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers-all/build-xilinx-projects/win_cmd.png
   :width: 400px

For example:

::

   Enter the system_top.hdf location 
   "example => C:/workspace/my_proj1_hdf/system_top.hdf"
   system_top.hdf
   Enter the project build folder 
   "example => C:/my_workspaces Note: use "/" instead of "\""
   fmcomms2_zc706

The parameters that were specified in the previous example, can be passed directly if the script is run from a command line.

For example:

::

   create_xilinx_sdk_project.bat D:/workspace/example_hdf/system_top.hdf D:/workspace/example_project/fmcadc2_zc706

.. tip::

   A default path of the Xilinx SDK installation folder is specified in the script. If you have installed the package in a different location, please modify the script accordingly


Makefile
~~~~~~~~

Using "Xilinx Software Command Line Tool", the projects can be created using the Makefiles.

If no parameters are specified, the default location of the .hdf file and of the folder where the project will be created is the current directory.

For example:

::

   ****** Xilinx Software Commandline Tool (XSCT) v2015.2
     **** Build date : Jun 26 2015-17:09:09
       ** Copyright 1986-2015 Xilinx, Inc. All Rights Reserved.


   Got $XILINX_SDK: C:/Xilinx/SDK/2015.2
   xsct% cd C:/workspace/git/no-os/ad9361
   xsct% dir
    Volume in drive C is DRIVE_C
    Volume Serial Number is CCB3-25B7

    Directory of C:\workspace\git\no-os\ad9361

   02/16/2016  02:57 PM    <DIR>          .
   02/16/2016  02:57 PM    <DIR>          ..
   10/14/2015  01:55 PM    <DIR>          chipscope
   02/16/2016  01:55 PM               574 create_xilinx_sdk_project.bat
   01/05/2016  01:18 PM               768 create_xilinx_sdk_project.sh
   01/05/2016  01:18 PM               823 Makefile
   01/05/2016  01:18 PM               429 README.md
   01/05/2016  01:18 PM    <DIR>          scripts
   02/16/2016  02:54 PM    <DIR>          sdk_project
   01/29/2016  11:59 AM    <DIR>          sw
   02/09/2016  12:15 PM         1,082,772 system_top.hdf
                  5 File(s)      1,085,366 bytes
                  6 Dir(s)  132,785,848,320 bytes free

   xsct% make -f Makefile
   'creating project'
   xsct -s ../build_scripts/xilinx/create_sdk_project.tcl system_top.hdf sdk_project
   Got $XILINX_SDK: C:/Xilinx/SDK/2015.2
   hdf file used: C:/workspace/git/no-OS/ad9361/system_top.hdf
   The build directory is: sdk_project
   C:/workspace/git/no-OS/ad9361/sdk_project was created
   FPGA CPU: ps7_cortexa9_0
   Hardware platform project 'hw' created successfully.
   BSP project 'bsp' created successfully.
   Application project 'sw' created successfully.
   ./sw/
   ./sw/platform_xilinx/
   Building All Projects...
   Building workspace
   Building '/bsp'
   Invoking Make Builder...bsp
   Building '/hw'
   Building '/sw'
   Invoking scanner config builder on project
   Done.
   xsct%

The location of the .hdf file and of the folder where the project will be created can be also specified if it is required.

For example:

::

   make -f Makefile hdf_file=./system_top.hdf project=./fmcomms2_zc706

Linux
-----

create_xilinx_sdk_project.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script can be run with no parameters. In this case, you will be asked to introduce the path and the name of the .hdf file and the path and the name of the folder where the project will be created.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers-all/build-xilinx-projects/linux_cmd.png
   :width: 400px

The parameters that were specified in the previous example, can be passed directly if the script is run from a command line.

For example:

::

   create_xilinx_sdk_project.sh ./system_top.hdf ./fmcomms2_zc706

.. tip::

   A default path of the Xilinx SDK installation folder is specified in the script. If you have installed the package in a different location, please modify the script accordingly


.. _makefile-1:

Makefile
~~~~~~~~

The projects can be created using the Makefiles.

If no parameters are specified, the default location of the .hdf file and of the folder where the project will be created is the current directory.

The location of the .hdf file and of the folder where the project will be created can be also specified if it is required.

Open the created workspace with Xilinx SDK GUI on Windows and Linux
-------------------------------------------------------------------

The workspaces created using the methods described previously, can be also opened using the Xilinx SDK GUI.

Open "Xilinx SDK" and browse for the location of the workspace.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers-all/build-xilinx-projects/sdk_directory.png
   :width: 400px

The prebuilt project is included in the opened workspace.

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers-all/build-xilinx-projects/sdk_workspace.png
   :width: 400px

.. tip::

   All the scripts described previously are dependent of the README.md file, from which the list and the path of the drivers used by each project is obtained. By moving the files to other locations will cause scripts malfunctions.

