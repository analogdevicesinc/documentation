.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated. Please check out our latest Build guide at https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html\


Building HDL
============

Please note that ADI only provides the source files necessary to create and build the designs. That means the burden of modifying and building these projects is on you. The build process, obviously, depends on certain software and tools. There are many ways you could use this software and tools. In other words, how you want to build these projects is entirely up to you. The only catch is that if you run into problems, you must use basic diligence in resolving it yourself.

Here we are giving you a quick rundown on how we build things. That is, the steps below are NOT a recommendation, but a suggestion. We use exclusively command line and mostly Linux systems. On Windows, we use Cygwin. Please do not ask any installation and/or setup instructions on these.

Setup and check your environment
--------------------------------

This section contains a guide about how to setup your environment in order to build any HDL project from the repository.

-  Install the required FPGA Design Suite. You can find information about the proper version in the :git-hdl:`release notes <releases>`. Make sure that you're always using the latest release.
-  The proper Vivado/Quartus version can be found in:

   -  Starting with the ``hdl_2021_r1`` release branch: :git-hdl:`scripts/adi_env.tcl`
   -  For ``hdl_2019_r2`` and older: *hdl/projects/scripts/adi_project_xilinx.tcl* for Vivado, and *hdl/projects/scripts/adi_project_intel.tcl* for Quartus.

-  Download the tools from the following links (it will take a lot of time and space):

   -  `Xilinx tools <https://www.xilinx.com/support/download.html>`_ (make sure you're downloading the proper installer! For full installation, it is better to choose the one that downloads and installs both Vivado and Vitis at the same time)
   -  `Intel tools <https://wiki.analog.com/https/www.intel.com/content/www/us/en/programmable/downloads/download-center.html>`_

-  After you have installed the above mentioned tools, you will need the paths to those directories in the following steps, so have them in a note
-  We are using `git <https://git-scm.com/>`_ for version control and `GNU Make <https://www.gnu.org/software/make/>`_ to build the projects. Depending on what OS you're using, you have these options:

++++ For Windows environment with Cygwin \|

Because GNU Make is not supported on Windows, you need to install `Cygwin <https://www.cygwin.com/>`_, which is a UNIX-like environment and command-line interface for Microsoft Windows. You do not need to install any special package, other than **git** and **make**.

After you installed Cygwin, you need to add your FPGA Design Tools installation directory to your PATH environment variable. You can do that by modifying your **~/.bashrc** file, by adding the following lines **changed accordingly to your installation directories**. For example:

::

   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vivado_HLS/202x.x/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/gnu/arm/nt/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_be/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_le/bin
   export PATH=$PATH:/cygdrive/path_to/Xilinx/Vitis/202x.x/gnu/aarch32/nt/gcc-arm-none-eabi/bin
   export PATH=$PATH:/cygdrive/path_to/intelFPGA_pro/2x.x/quartus/bin

<fc #fa8072>Replace the **path_to** string with your path to the installation folder and the **tools version** with the proper one!</fc>

++++

++++ For Windows environment with WSL \| You can also install `WSL <https://learn.microsoft.com/en-us/windows/wsl/install/>`_ (Windows Subsystem for Linux) which is both a UNIX-like environment and a command-line interface for Microsoft Windows. In order to be able to access the GUI, WSL2 is recommended. This can be done if we open PowerShell or Windows Command Prompt in Administrator mode. In the link above you can find the installation guide for wsl on windows.

.. note::

   When installing wsl, the Ubuntu distribution will be installed by default


If not, after installing wsl, write in the terminal:

::

   >wsl --update
   >wsl --install -d ubuntu

If you want to check the version for wsl, you can use the Windows Command Prompt command:

::

   >wsl -l -v
     NAME      STATE           VERSION
   * Ubuntu    Running         2

If you want to check the version for wsl and Ubuntu, you can use the following commands in Ubuntu:

::

   :~$ uname -r
   5.15.90.1-microsoft-standard-WSL2

   :~$ lsb_release -a
   No LSB modules are available.
   Distributor ID: Ubuntu
   Description:    Ubuntu 22.04.2 LTS
   Release:        22.04
   Codename:       jammy

If you want to become root, you can use the following command:

::

   :~$ sudo -i
   [sudo] password for username:
   root@HYB-0FPP35J6CsI:~# exit
   logout

Here the paths will look like this if the tools will be installed in the Windows file system:

::

   export PATH=$PATH:/mnt/path_to/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vivado_HLS/202x.x/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/gnu/arm/nt/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_be/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_le/bin
   export PATH=$PATH:/mnt/path_to/Xilinx/Vitis/202x.x/gnu/aarch32/nt/gcc-arm-none-eabi/bin
   export PATH=$PATH:/mnt/path_to/intelFPGA_pro/2x.x/quartus/bin

<fc #fa8072>Replace the **path_to** string with your path to the installation folder and the **tools version** with the proper one!</fc>

.. important::

   Before building any project, it is necessary to install the Linux version for Vivado (see :doc:`How to install Vivado on wsl section </wiki-migration/resources/fpga/docs/build>` ) and Quartus because on the Ubuntu distribution on `WSL <https://learn.microsoft.com/en-us/windows/wsl/install/>`_ you cannot run projects on the Windows version of them. When you have to choose the installation path, choose the location where wsl is installed (\\\\wsl.localhost\\Ubuntu\\opt). Also, to get the best performance, you must clone your hdl repository in the WSL file system. For example: (\\\\wsl.localhost\\Ubuntu\\home\\username\\hdl)


For more information you can consult the following link: `WSLStorage <https://learn.microsoft.com/en-us/windows/wsl/filesystems#file-storage-and-performance-across-file-systems>`_.

Then the paths will look like this:

::

   export PATH=$PATH:/opt/path_to/Xilinx/Vivado/202x.x/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vivado_HLS/202x.x/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/nt/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/gnu/arm/nt/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_be/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/gnu/microblaze/linux_toolchain/nt64_le/bin
   export PATH=$PATH:/opt/path_to/Xilinx/Vitis/202x.x/gnu/aarch32/nt/gcc-arm-none-eabi/bin
   export PATH=$PATH:/opt/path_to/intelFPGA_pro/2x.x/quartus/bin

<fc #fa8072>Replace the **path_to** string with your path to the installation folder and the **tools version** with the proper one!</fc>

++++

++++ For Linux environment \| Because, in general, both **git** and **make** are native tools in Linux, you do not need to do any special setup. If you don't have these, install them.

Further more, you need to add your FPGA Design Tools installation directory to your PATH environment variable. For Xilinx tools, you can run the **settings64.sh** script, which is located in your installation directory. Or you can add the required paths to your **~/.bashrc** file. For example:

::

   export PATH=$PATH:"/opt/Xilinx/Vivado/202x.x/bin"
   export PATH=$PATH:"/opt/Xilinx/Vitis/202x.x/bin"
   export PATH=$PATH:"/opt/intelFPGA_pro/2x.x/quartus/bin"

<fc #fa8072>Replace the **path_to** string with your path to the installation folder and the **tools version** with the proper one!</fc> ++++

++++ How to install Vivado on WSL \| Installing the linux kit for Vivado can be done from Ubuntu:

-  Go to the path where the installation kit for Vivado is located.
-  Make it executable

::

   :~$ chmod +x Xilinx_Vivado installation kit.bin
   :~$ ./Xilinx_Vivado installation kit.bin

::

   If you unzip the installation kit in Ubuntu, go to the Xilinx_Vivado installation kit and run .xsetup file. Make sure you have the following libraries installed:

::

   :~$ sudo apt-get install locales && sudo localedef -i en_US -f UTF-8 en_US.UTF-8
   :~$ sudo ./installLibs.sh
   :~$ sudo apt-get install libxrender1 libxtst6 libxi6

You must create a .bashrc file with the paths corresponding to the version of Vivado installed. ++++

++++ How to verify your environment setup \| Run any of the following commands. These commands will return a valid path if your setup is good.

::

   [~] which git
   [~] which make
   [~] which vivado
   [~] which quartus

++++

Setup the HDL repository
------------------------

If you completed the above steps, next thing to do is clone the repository. This is the best method to get the sources. Here, I am cloning the repository inside a directory called **adi**. Please refer to the :doc:`Git Repository </wiki-migration/resources/fpga/docs/git>` section for more details.

::

   [~] mkdir adi
   [~] cd adi
   [~] git clone git@github.com:analogdevicesinc/hdl.git

.. note::

   Cloning the HDL repository is done now using SSH, because of GitHub security reasons. Check out this documentation on `how to deal with SSH keys in GitHub <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_. Both for `Cygwin <https://www.cygwin.com/>`_ and `WSL <https://learn.microsoft.com/en-us/windows/wsl/install/>`_ it is necessary to create a unique SSH key. If you use WSL,to get the best performance, you must clone your hdl repository in the WSL file system. For example: (\\\\wsl.localhost\\Ubuntu\\home\\username\\hdl)


The above command clones the 'default' branch, which is the 'master' for HDL. The 'master' branch always points to the latest stable release branch, but it also has features **that are not fully tested**. If you want to switch to any other branch you need to checkout that branch:

::

   [~] cd hdl/
   [~] git status
   [~] git checkout hdl_2021_r1

If this is your first time cloning, you have all the latest source files. If it has been a while, you can simply pull the latest sources using **git pull** or **git rebase** if you have local changes.

::

   [~] git fetch origin               # this shows you what changes will be pulled on your local copy
   [~] git rebase origin/hdl_2021_r1  # this updates your local copy

++++ Screenshots: \| |image1| ++++

Building the projects
---------------------

.. important::

   Before building any project, you must have the environment prepared and the proper tools. See :doc:`Tools </wiki-migration/resources/fpga/docs/build>` section on what you need to download and :doc:`Environment </wiki-migration/resources/fpga/docs/build>` section on how to set-up your environment.


Building an Intel project
~~~~~~~~~~~~~~~~~~~~~~~~~

An Intel project build is relatively easy. There is no need to build any library components. However, the flow is the same, run 'make' to build your project of interest. In this example, I am only interested in the 'ADRV9371X' project on the 'A10SOC' carrier.

::

   cd projects/adrv9371x/a10soc
   make

++++ Screen shots: \| |image2| ++++

This assumes that you have the tools and licenses setup correctly. If you don't get to the last line, the make failed to build the project. There is nothing you can gather from the 'make' output (other than the build failed or not), the actual failure is in a log file. So let's see how to analyze the build log files and results.

.. important::

   If you want to use a NIOS-II based project with no-OS software, you have to turn off the MMU feature of the NIOS_II processor. In that case, the make will get an additional attribute: ``make NIOS2_MMU=0``\


Intel: checking the build and analyzing results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you look closely at the 'rule' for this target, you see it is just calling 'quartus_sh' with the project TCL file and redirecting the output to a log file. In this case 'adrv9371_a10soc_quartus.log' and is inside the 'projects/adrv9371x/a10soc' directory.

::

   make: Entering directory '/home/RKutty/gitadi/hdl/projects/adrv9371x/a10soc'
   rm -rf *.log *_INFO.txt *_dump.txt db *.asm.rpt *.done *.eda.rpt *.fit.* *.map.* *.sta.* *.qsf *.qpf           *.qws *.sof *.cdf *.sld *.qdf hc_output system_bd hps_isw_handoff hps_sdram_*.csv *ddr3_*.csv increme          ntal_db reconfig_mif *.sopcinfo *.jdi *.pin *_summary.csv *.dpf
   quartus_sh --64bit -t  system_project.tcl  >> adrv9371x_a10soc_quartus.log 2>&1
   make: Leaving directory '/home/RKutty/gitadi/hdl/projects/adrv9371x/a10soc'

Quick (or detailed) check on files. If you are seeking support from us, this is the most relevant information you can provide (do NOT copy-paste 'make' command line text).

::

   ls -ltr projects/adrv9371x/a10soc
   tail projects/adrv9371x/a10soc/adrv9371x_a10soc_quartus.log

++++ Screenshots: \| |image3| ++++ ++++ Screenshots: \| |image4| ++++

And finally, if the project build is successful, the **.sopcinfo** and **.sof** files should be in the same folder.

::

   ls -ltr projects/adrv9371x/a10soc/*.sopcinfo
   ls -ltr projects/adrv9371x/a10soc/*.sof

++++ Screenshots: \| |image5| ++++

You may now use this 'sopcinfo' file as the input to your no-OS and/or Linux build. The 'sof' file is used to program the device.

++++ Building an Intel project in WSL - known issues \| For a10Soc and s10Soc projects it is very possible to face the following error when you make a build:

.. important::

   Current module quartus_fit was unexpectedly terminated by signal 9. This may be because some system resource has been exhausted, or quartus_fit performed an illegal operation.


It can also happen that "**make**" get stuck when synthesizing some ips. This errors may appear because your device does not have enough RAM memory to build your FPGA design. This problem can be solved if it is created a linux Swap file. You can find more information about what a swap file is in the next link:`SwapFile <https://linuxize.com/post/create-a-linux-swap-file/>`_. Depending on the size of the project, more or less virtual memory must be allocated. If you type in the search bar **System Information**, you can see Total Physical Memory and Total Virtual Memory of your system. For example for the AD9213 with s10Soc project, it was necessary to allocate 15 GB of virtual memory, to be able to make a build for the project. To create a swap file you can use the following commands:

::

   :~$ sudo fallocate -l "memory size (e.g 1G, 2G, 8G, etc.)" /swapfile
   :~$ sudo chmod 600 /swapfile
   :~$ sudo mkswap /swapfile
   :~$ sudo swapon /swapfile

If you want to make the change permanent:

::

    in /etc/fstab file type the command:
   /swapfile swap swap defaults 0 0

If you want to deactivate the swap memory:

::

   :~$ sudo swapoff -v /swapfile

++++

Building a Xilinx project
~~~~~~~~~~~~~~~~~~~~~~~~~

A Xilinx project is built the same way as an 'Intel' project. The only exception is that there are a few 'sub-make(s)' for the library components. The way of building a project in Cygwin and WSL is the same, with small differences. In this example, it is building the 'DAQ2' project on the 'ZC706' carrier.

::

   cd projects/daq2/zc706
   make

++++ Screenshots: \| |image6| ++++ ++++ Screenshots: \| |image7| ++++

The **make** builds all the libraries first and then builds the project. This assumes that you have the tools and licenses setup correctly. If you don't get to the last line, the make failed to build one or more targets: it could be a library component or the project itself. There is nothing you can gather from the 'make' output (other than which one failed). The actual failure is in a log file, so let's see how to analyze the build log files and results.

Enabling Out-of-Context synthesis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can opt in for out-of-context synthesis during the build by defining the **ADI_USE_OOC_SYNTHESIS** system variable. By setting the **ADI_MAX_OOC_JOBS** system variable you can adjust the number of maximum parallel out-of-context synthesis jobs. If not set, the default parallel job number is set to 4.

::

   export ADI_USE_OOC_SYNTHESIS=y
   export ADI_MAX_OOC_JOBS=8
   cd projects/daq2/zc706
   make

This will synthesize each IP from the block design individually and will store it in a common cache for future re-use. The cache is located in the **ipcache** folder and is common for all the projects, this way speeding up re-compile of the same project or compile time of common blocks used in base designs. Example: a MicroBlaze base design for VCU118 once compiled, it will be reused on other projects. Using the IP cache will speed up the re-compiles of every project in OOC mode since the cache is not cleared as with normal compile flow.

.. important::

   Starting with Vivado 2020.2, Out-of-Context is the default mode. There is no need to set ADI_USE_OOC_SYNTHESIS variable.

   
   Set:
   
   ::
   
      export ADI_USE_OOC_SYNTHESIS=n
   
   only in case you want to use Project Mode.


Xilinx: checking the build and analyzing results of library components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you look closely, you see what it is actually doing. It enters a library component folder then calls 'Vivado' in batch mode. The IP commands are in the source 'Tcl' file and output is redirected to a log file. In the below example that is 'axi_ad9144_ip.log' inside the 'library/axi_ad9144' directory.

::

   make[1]: Entering directory '/home/RKutty/gitadi/hdl/library/axi_ad9144'
   rm -rf *.cache *.data *.xpr *.log component.xml *.jou xgui *.ip_user_files *.srcs *.hw *.sim .Xil
   vivado -mode batch -source axi_ad9144_ip.tcl  >> axi_ad9144_ip.log 2>&1

If you see 'make' returns an error (and stops), **you must first check the contents of this log file** before going crazy on us. You may also do a sanity checking just to see what are the generated files and the log file contents.

::

   ls -ltr library/axi_ad9144
   tail library/axi_ad9144/axi_ad9144_ip.log

++++ Screenshots: \| |image8| ++++ ++++ Screenshots: \| |image9| ++++

Xilinx: checking the build and analyzing results of projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last thing make does in this above example is building the project. It is exactly the same 'rule' as the library component. The log file, in this example, is called 'daq2_zc706_vivado.log' and is inside the 'projects/daq2/zc706' directory.

::

   rm -rf *.cache *.data *.xpr *.log *.jou xgui *.runs *.srcs *.sdk *.hw *.sim .Xil *.ip_user_files
   vivado -mode batch -source system_project.tcl >> daq2_zc706_vivado.log 2>&1
   make: Leaving directory '/home/RKutty/gitadi/hdl/projects/daq2/zc706'

Quick (or detailed) check on files.

::

   ls -ltr projects/daq2/zc706
   tail projects/daq2/zc706/daq2_zc706_vivado.log

++++ Screenshots: \| |image10| ++++ ++++ Screenshots: \| |image11| ++++

And finally, if the project build is successful, the hdf file should be in the 'sdk' folder.

::

   ls -ltr projects/daq2/zc706/daq2_zc706.sdk

++++ Screenshots: \| |image12| ++++

You may now use this 'hdf' file as the input to your no-OS and/or Linux build. Starting with Vivado 2019.3, output file extension got change from .hdf to .xsa.

++++ Building a Xilinx project in WSL - known issues \| For some projects it is very possible to face the following error when you make a build:

.. important::

   :math:`RDI_PROG" "`\ @" crash" "Killed ":math:`RDI_PROG" "`\ @"


This error may appear because your device does not have enough RAM memory to build your FPGA design. For example, the project AD-FMCDAQ3-EBZ with Virtex UltraScale+ VCU118 (XCVU9P device) requires 20 GB (typical memory) and a peak of 32 GB memory RAM. The next link shows the typical and peak Vivado memory usage per target device:`MemoryUsage <https://www.xilinx.com/products/design-tools/vivado/vivado-ml.html#memory>`_. This problem can be solved if it is created a linux Swap file. You can find more information about what a swap file is in the next link:`SwapFile <https://linuxize.com/post/create-a-linux-swap-file/>`_ To create a swap file you can use the following commands:

::

   :~$ sudo fallocate -l "memory size (e.g 1G, 2G, 8G, etc.)" /swapfile
   :~$ sudo chmod 600 /swapfile
   :~$ sudo mkswap /swapfile
   :~$ sudo swapon /swapfile

If you want to make the change permanent:

::

    in /etc/fstab file type the command:
   /swapfile swap swap defaults 0 0

If you want to deactivate the swap memory:

::

   :~$ sudo swapoff -v /swapfile

++++

Tools and Tool versions
=======================

Tools
-----

ADI provides reference designs for both Intel and Xilinx. Please note that we have no preference over Intel or Xilinx, if possible we try to port the designs on both platforms. However, there are a few things you should be aware of when building the projects. This is NOT a comparison (generic or otherwise)- this is what you should expect and understand when using ADI HDL repository on these tools. A red text indicates that you must pay extra attention.

+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Notes                                     | Intel                                                                                                                                                                                                                                                                                             | Xilinx                                                                                                                                                                                                                                                                           |
+===========================================+===================================================================================================================================================================================================================================================================================================+==================================================================================================================================================================================================================================================================================+
| Main Tools                                | Quartus                                                                                                                                                                                                                                                                                           | Vivado                                                                                                                                                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EDK Tools                                 | QSys                                                                                                                                                                                                                                                                                              | IP Integrator                                                                                                                                                                                                                                                                    |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK Tools                                 | Eclipse-Nios, Eclipse-DS5                                                                                                                                                                                                                                                                         | Eclipse                                                                                                                                                                                                                                                                          |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Building Library                          | <fc #008000>Do nothing. Quartus only need the \_hw.tcl and QSys parses them whenever invoked.</fc>                                                                                                                                                                                                | <fc #FF0000>Need to build each and every library component. Vivado has its own way of identifying library components. This means you must build ALL the library components first before starting the project. You must re-run these scripts if there are any modifications.</fc> |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Building the project                      | Source the system_project.tcl file.                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                  |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Timing Analysis                           | The projects are usually tested and should be free of timing errors. There is no straightforward method to verify a timing pass (it usually involves writing a TCL proc by itself) on both the tools. The make build will fail and return with an error if the timing is not met (on both tools). |                                                                                                                                                                                                                                                                                  |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK (Microblaze/Nios)                     | Use SOPCINFO and SOF files.                                                                                                                                                                                                                                                                       | Use XSA file.                                                                                                                                                                                                                                                                    |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK (ARM/FPGA combo)                      | <fc #FF0000>Not so well-thought procedure. Need to run different tools, manually edit build files etc. The steps involved are running bsp-editor, running make, modifying linker scripts, makefiles and sources, importing to SDK.</fc>                                                           | <fc #008000>Same procedure as Microblaze.</fc>                                                                                                                                                                                                                                   |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Upgrading/Version changes (non-ADI cores) | <fc #008000>Quartus automatically updates the cores. Almost hassle-free for most of the cores.</fc>                                                                                                                                                                                               | <fc #FF0000>Vivado does not automatically update the revisions in TCL flow (it does on GUI). It will stop at the first version mismatch (a rather slow and frustrating process).</fc>                                                                                            |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Tool versions
-------------

Though the ADI libraries work across different versions of the tools, the projects we provide may not. The Xilinx and Intel IPs may or may not work across versions. We can only assure you that they are tested and works only for the versions we provide. The projects are usually upgraded to the latest tools after they are publicly released. The information about the version of the used tools can be found in the :git-hdl:`README.md` file of each branch. The script, which builds the project always double check the used tool version, and notifies the user, if he or she trying to use an unsupported version of tools.

.. note::

   There are several ways to find out which tool version you should use. The easiest way is to check the :git-hdl:`release notes <releases>`. You may also check out or browse the desired branch, and verify the tool version in the base Tcl script (:git-hdl:`./hdl/projects/scripts/adi_project_xilinx.tcl <projects/scripts/adi_project_xilinx.tcl#L4>`) or (:git-hdl:`./hdl/projects/scripts/adi_project_intel.tcl <projects/scripts/adi_project_intel.tcl#L5>`), which build the projects.


Environment
===========

As said above, our recommended build flow is to use **make** and the command line versions of the tools. This method highly facilitates our overall build and release process as it automatically builds the required libraries and dependencies.

Linux environment setup
-----------------------

All major distributions should have 'make' installed by default. If not if you try the command it should tell you how to install them with the package name. You may have to install 'git' (sudo apt-get install git)and the Intel and Xilinx tools. These tools come with certain 'settings\*.sh' scripts that you may source in your '.bashrc' file to set up the environment. You may also do this manually (for better or worse), the following snippet is from a **.bashrc** file. Please note that unless you are an expert at manipulating these things, leave it to the tools to set up the environment.

::

   export PATH=$PATH:/opt/Xilinx/Vivado/202x.x/bin:/opt/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/opt/intelFPGA_pro/2x.x/quartus/bin

Windows environment setup
-------------------------

The best option on Windows is to use `Cygwin <https://www.cygwin.com>`_. When installing it, select the 'make' and 'git' packages. The manual changes to your '.bashrc' do a lot look like that of the Linux environment.

::

   export PATH=$PATH:/cygdrive/d/Xilinx/Vivado/202x.x/bin:/cygdrive/d/Xilinx/Vitis/202x.x/bin
   export PATH=$PATH:/cygdrive/d/intelFPGA_pro/2x.x/quartus/bin64

A very good alternative to Cygwin is `WSL <https://learn.microsoft.com/en-us/windows/wsl/install/>`_. The manual changes to your '.bashrc' looks like:

::

   export PATH=$PATH:/opt/path_to/Vivado/202x.x/bin:/opt/Vitis/202x.x/bin
   export PATH=$PATH:/opt/path_to/quartus/bin

If you do not want to install Cygwin, there may still be some alternatives. There are 'make' alternatives for 'windows command prompt', minimalist GNU for Windows ('MinGW'), or the 'cygwin' variations installed by the tools itself. Some of these may not be fully functional with our scripts and/or projects. If you are an Intel user, the "Nios II Command Shell" do support make. If you are a Xilinx user, use the 'gnuwin' installed as part of the SDK, usually C:\\Xilinx\\Vitis\\202x.x\\gnuwin\\bin.

Make: supported targets
=======================

.. tip::

   `Make <https://www.gnu.org/software/make/manual/make.html>`_ is a build automation tool, which uses **Makefile(s)** to define a set of directives ('rules') about how to compile and/or link a program ('targets').


In general, always run 'make' within a project folder such as 'hdl/projects/daq2/a10soc' or 'hdl/projects/daq2/zc706'. There should not be a need for you to run 'make' inside the library or root folders. The 'make' framework passes the top level 'targets' to any sub-makes inside its sub-folders. What this means is that if you run 'make' inside 'hdl/projects/daq2', it builds all the carriers ('kc705', 'a10soc', 'kcu105', 'zc706' to 'zcu102') which is an overkill.

The following 'targets' are supported.

+------------------+--------------------------------------------------------------------------------------------------------------------+
| argument         | description                                                                                                        |
+==================+====================================================================================================================+
| all              | This builds everything in the current folder and its sub-folders, see context examples below.                      |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C library/axi_ad9122 all; ## build AD9122 library component (Xilinx only).                                   |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C library all; ## build **ALL** library components inside 'library' (Xilinx only).                           |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C projects/daq2/zc706 all; ## build DAQ2_ZC706 (Xilinx) project.                                             |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C projects/daq2/a10soc all; ## build DAQ2_A10SOC(Intel) project.                                             |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C projects/daq2 all; ## build DAQ2 **ALL** carrier (including Intel & Xilinx) projects.                      |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make -C projects all; ## build **ALL** projects (something you really should NOT do).                              |
+------------------+--------------------------------------------------------------------------------------------------------------------+
| clean            | This removes all tool and temporary files in the current folder and its sub-folders, same context as above.        |
+------------------+--------------------------------------------------------------------------------------------------------------------+
| clean-all        | This removes more things (?) same context as above.                                                                |
+------------------+--------------------------------------------------------------------------------------------------------------------+
| lib              | This is same as 'all' in the library folder, ignored inside project folders.                                       |
+------------------+--------------------------------------------------------------------------------------------------------------------+
| project.platform | This is a special target available only in the 'hdl' root folder and is ignored everywhere else, see syntax below. |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make daq2.a10soc ; ## build projects/daq2/a10soc.                                                                  |
+------------------+--------------------------------------------------------------------------------------------------------------------+
|                  | make daq2.zc706 ; ## build projects/daq2/zc706.                                                                    |
+------------------+--------------------------------------------------------------------------------------------------------------------+

Xilinx auto Tcl build
=====================

.. warning::

   We do not recommend using this flow (created mostly for Windows users that can't use GNU make). The benefit of this flow is that a user can build all desired libraries without manually building each library. The disadvantage comparing with make is that the script will rebuild an IP regardless if its sources were modified or not (timestamp comparison).


**Open Vivado GUI, and in the Tcl console type:**

::

   cd c:/github/hdl/projects/daq2/zc706
   source ../../scripts/adi_make.tcl

This will get you access to:

-  adi_make::lib
-  adi_make::boot_bin

Building the libraries (adi_make::lib)
--------------------------------------

This command allows you to build the desired libraries directly from the target project folder location. It accepts as arguments "all" or you can specify a specific library name.

.. code:: bash

     # How to use:
     adi_make::lib all # builds all libraries on which the project is depending on
     adi_make::lib axi_dmac # builds only the axi_dmac IP (and its dependencies)
     adi_make::lib jesd204/jesd204_rx

Building the project itself
---------------------------

After all required libraries are built, run **source ./system_project.tcl** in the Tcl console of Vivado, to build the project.

::

   source ./system_project.tcl

Preparing the SD card
---------------------

Firstly, you have to check this :doc:`tutorial </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>` on how to put the Linux image on your SD card. Once you are done with that, you can go on with the following steps.

On the BOOT partition recently created, you will find folders for each carrier that we support, and each of these folders contain an archive called **bootgen_sysfiles.tgz**. These have all the files needed to generate the BOOT.BIN.

Copy the corresponding archive (checking for the name of your carrier and components) into the root folder of your project, unzip it twice, and there you will find the files that are needed to generate the BOOT.BIN. Copy them to be in the root directory.

-  fsbl.elf
-  zynq.bif
-  u-boot.elf
-  and if you're using ZCU102, then bl31.elf and pmu.elf

Next, what your project needs, is the **uImage**\ (for zynq based carriers), **Image** (for zynq ultrascale - ZCU102 and adrv9009-zu11eg carriers) or zImage (for Intel based carriers) file that you will find in the **zynq-common / zynqmp-common / socfpga_arria10_common / socfpga_cyclone5_common** on your BOOT partition. Copy this file also in the root directory of your project.

More info on how to generate this files you will find in the :doc:`References </wiki-migration/resources/fpga/docs/build>` section or on ReadMe.txt file from boot partition.

++++ How to build the boot image BOOT.BIN in WSL \| After obtaining .xsa file, you must be sure that you have done source for Vivado and Vitis. To create boot.bin is recommended to run build_boot_bin.sh in terminal.To do this, the file can be called in the following form:

::

     chmod +x build_boot_bin.sh
     usage: build_boot_bin.sh system_top.xsa u-boot.elf [output-archive]

You can download the script by accessing the following link: `build_boot_bin.sh <:doc:`/wiki-migration/resources/tools-software/linux-software/build-the-zynq-boot-image`>`_.

++++

Make the BOOT.BIN (adi_make::boot_bin)
--------------------------------------

.. warning::

   Not for Linux users. To build the BOOT.BIN in Linux see the :doc:`References </wiki-migration/resources/fpga/docs/build>` section.


As the name states, this procedure will build the "BOOT.BIN". It does not require any arguments.

::

     adi_make::boot_bin

Building manually
=================

.. warning::

   We do not recommend using this flow, in general people are losing a lot of valuable time and nerve during this process.


Intel: Building manually on Quartus
-----------------------------------

There is no need to build any library for Quartus. However, you do need to specify the IP search path for QSYS. This is a global property, so only need to do it once. If you have multiple paths simply add to it. You get to this menu from the **Tools->Options**. The tool then parses these directories and picks up a **\_hw.tcl** file (e.g. axi_ad9250_hw.tcl). The peripherals should show up on QSYS library.

++++ Screen shots: \| |image13| ++++

You may now run the project (generate the sof and software hand-off files) on Quartus. Open the GUI and select TCL console. At the prompt change the directory to where the project is, and source the **system_project.tcl** file.

::

   cd c:/github/hdl/projects/fmcjesdadc1/a5gt
   source ./system_project.tcl

You will see commands being executed, the script uses a board design in QSYS, generate all the IP targets, synthesize the netlist and implementation.

++++ Screen shots: \| |image14| |image15| ++++

Xilinx: Building manually on Vivado
-----------------------------------

In Vivado (Xilinx projects), you must build all the required libraries for your targeted project. Open the GUI and at the TCL console change the directory to where the libraries are, then source the '\_ip.tcl' file.

::

   cd c:/github/hdl/library/axi_ad9122
   source ./axi_ad9122_ip.tcl

You will see commands being executed, and the GUI will change into a project window. There is nothing to do here, you could browse the source if you prefer to do synthesis as stand-alone and such things. After you're done, quit and change the directory to the next library and continue the process.

++++ Screen shots: \| |image16| |image17| ++++

After you built all the required libraries for your project, you can run the project (generate bitstream and export the design to SDK). This is the same procedure as above except for changes in path and Tcl file names:

::

   cd c:/github/hdl/projects/fmcomms1/zc706
   source ./system_project.tcl

Same behavior as above, the GUI will change into a project window. The script will create a board design in IPI, generate all the IP targets, synthesize the netlist and implementation.

++++ Screen shots: \| |image18| |image19| ++++

References
==========

-  :doc:`How to build the Zynq boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynq-boot-image>`
-  :doc:`How to build the ZynqMP boot image BOOT.BIN </wiki-migration/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`
-  :doc:`Building the ADI Linux kernel </wiki-migration/resources/tools-software/linux-drivers-all>`

Errors, Warnings and Notes
==========================

Assuming the right to make an honest comment, the tools (both Quartus and Vivado) are not that useful or friendly when it comes to messages. In most cases, you may see 'hacked-in' debugging 'printf' sort of messages (Xilinx notoriously ranks high in this regard). So you are going to see a lot of 'warnings' and some 'critical-warnings' (critical to what could be hard to answer). Here are some of the commonly asked EngineerZone questions and its explanations.

Xilinx: Vivado
--------------

<fc #ffa500> ERROR: [BD 5-216] VLNV <analog.com:user:axi_clkgen:1.0> is not supported for the current part.

::

   ERROR: [Common 17-39] 'create_bd_cell' failed due to earlier errors.
        while executing 
   "create_bd_cell -type ip -vlnv analog.com:user:axi_clkgen:1.0 axi_hdmi_clkgen" invoked from within 
   "set axi_hdmi_clkgen [create_bd_cell -type ip -vlnv analog.com:user:axi_clkgen:1.0 axi_hdmi_clkgen]" (file "../../../projects/common/zc706/zc706_system_bd.tcl" line 57)</fc>

You haven't generated the library component or have the wrong user IP repository setting. If you were using the GUI flow, now is a good time to evaluate the 'make' flow.

<fc #ffa500>CRITICAL WARNING: [IP_Flow 19-459] IP file 'C:/Git/hdl/library/common/ad_pnmon.v' appears to be outside of the project area 'C:/Git/hdl/library/axi_ad9467'. You can use the ipx::package_project -import_files option to copy remote files into the IP directory.</fc>

These warnings appear because the libraries are using common modules which are located under the **./library/common/**. These warnings can be ignored, they won't affect the functionality of the IP or the project. However, you may not be able to 'archive' these projects. The irony is that it does copy these files to the project area, but ignores them.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#releases
   :alt: Releases and supported tool versions#hdl|Main page#run|Running on hardware

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_4.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_12.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_13.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_15.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_14.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_5.png
   :width: 800px
.. |image7| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_6.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_7.png
   :width: 800px
.. |image9| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_8.png
   :width: 800px
.. |image10| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_9.png
   :width: 800px
.. |image11| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_10.png
   :width: 800px
.. |image12| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/hdl_cygwin_11.png
   :width: 800px
.. |image13| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/altera_qsys_1.jpg
   :width: 800px
.. |image14| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/altera_quartus_1.jpg
   :width: 800px
.. |image15| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/altera_quartus_2.jpg
   :width: 800px
.. |image16| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/vivado_library_1.jpg
   :width: 800px
.. |image17| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/vivado_library_2.jpg
   :width: 800px
.. |image18| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/vivado_projects_1.jpg
   :width: 800px
.. |image19| image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/vivado_projects_2.jpg
   :width: 800px
