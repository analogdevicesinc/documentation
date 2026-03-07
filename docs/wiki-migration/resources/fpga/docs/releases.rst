Releases
========

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/user_guide/releases.html


The HDL is released as git branches. The release branches are created first and then detailed tested before being made official. That is, the existence of a branch does not mean it is a fully tested release. Also, the release branch is tested ONLY on certain versions of the tools and may NOT work with other versions of the tools. The projects that are tested and supported in a release branch are listed here along with the ADI library cores that are used. The branch may contain other projects that are in development, one must assume these are NOT tested and therefore NOT supported by this release.

All HDL pre-built files are provided to download together with Linux device trees and Kernel images, as a `boot partition archive <https://swdownloads.analog.com/cse/boot_partition_files/2023_r2/latest_boot.txt>`_ (just replace '2023_r2' in above link with other release name to get specific boot files, ex. 2022_r2). All boot files are also part of released :doc:`Kuiper images </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`.

Check :git-hdl:`GitHub Release Notes <releases>` for each release to see the main changes and links to related documentation.

On the other side, the 'main' HDL branch is used for development and regression testing is ran less often on it. This implies that it may not be always stable. Latest pre-build boot files from main are available `here <https://swdownloads.analog.com/cse/boot_partition_files/main/latest_boot.txt>`_.

Porting a release branch to another Tool version
------------------------------------------------

It is possible to port a release branch to another tool version, though not recommended. The ADI libraries should work across different versions of the tools, but the projects may not. The issues are most likely with the Intel and Xilinx cores. If you must still do this, note the following:

First, disable the version check of the scripts.

The ADI build scripts are making sure that the releases are being run on the validated tool version. It will promptly notify the user if he or she trying to use an unsupported version of tools. You need to disable this check by setting the environment variable ADI_IGNORE_VERSION_CHECK.

Second, make Intel and Xilinx IP cores version changes.

The Intel projects should automatically be changed by Quartus. The Xilinx projects are a bit tricky. The GUI automatically updates the cores, but the TCL flow does NOT. So it may be easier to create the project file with the supported version first, then opening it with the new version. After which, update the TCL scripts accordingly.

The versions are specified in the following format.

::

   add_instance sys_cpu altera_nios2_gen2 16.0 
   set sys_mb [create_bd_cell -type ip -vlnv xilinx.com:ip:microblaze:9.5 sys_mb] 

You should now be able to build the design and test things out. In most cases, it should work without much effort. If it doesn't do an incremental update and debug accordingly.

Release Branches
----------------

+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Releases                                                                          | Intel            | Xilinx          | Release Notes                                                                        | List of Supported Projects and IP cores                                    |
+===================================================================================+==================+=================+======================================================================================+============================================================================+
| :git-hdl:`tree/main`                                                              | Quartus Pro 24.2 | Vivado 2024.2   |                                                                                      |                                                                            |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`hdl_2023_r2 Patch1 <tree/hdl_2023_r2>`                                  | Quartus Pro 23.2 | Vivado 2023.2   | :git-hdl:`Release Notes <releases/tag/2023_R2_p1>`                                   | :doc:`2023_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2023_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2023_r2`                                                       | Quartus Pro 23.2 | Vivado 2023.2   | :git-hdl:`Release Notes <releases/tag/2023_R2>`                                      | :doc:`2023_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2023_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`hdl_2022_r2 Patch1 <tree/hdl_2022_r2>`                                  | Quartus Pro 22.4 | Vivado 2022.2   | :git-hdl:`Release Notes <releases/tag/2022_r2_p1>`                                   | :doc:`2022_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2022_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2022_r2`                                                       | Quartus Pro 22.4 | Vivado 2022.2   | :git-hdl:`Release Notes <releases/tag/2022_R2>`                                      | :doc:`2022_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2022_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2021_r2`                                                       | Quartus Pro 21.4 | Vivado 2021.2   | :git-hdl:`Release Notes <releases/tag/2021_R2>`                                      | :doc:`2021_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2021_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2021_r1`                                                       | Quartus Pro 21.2 | Vivado 2021.1   | :git-hdl:`Release Notes <releases/tag/2021_r1>`                                      | :doc:`2021_r1 </wiki-migration/resources/fpga/docs/hdl/downloads_2021_r1>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2019_r2`                                                       | Quartus Pro 19.3 | Vivado 2019.1   | :git-hdl:`Release Notes <releases/tag/hdl_2019_r2>`                                  | :doc:`2019_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2019_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2019_r1`                                                       | Quartus 18.1     | Vivado 2018.3   | :git-hdl:`Release Notes <releases/tag/2019_r1>`                                      | :doc:`2019_r1 </wiki-migration/resources/fpga/docs/hdl/downloads_2019_r1>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2018_r2`                                                       | Quartus 18.0     | Vivado 2018.2   | :git-hdl:`Release Notes <releases/tag/2018_r2>`                                      | :doc:`2018_r2 </wiki-migration/resources/fpga/docs/hdl/downloads_2018_r2>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2018_r1`                                                       | Quartus 17.1.1   | Vivado 2017.4.1 | :git-hdl:`Release Notes <releases/tag/2018_r1>`                                      | :doc:`2018_r1 </wiki-migration/resources/fpga/docs/hdl/downloads_2018_r1>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2017_r1`                                                       | Quartus 16.1     | Vivado 2016.4   | :git-hdl:`Release Notes <releases/tag/2017_r1>`                                      | :doc:`2017_r1 </wiki-migration/resources/fpga/docs/hdl/downloads_2017_r1>` |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2016_r2`                                                       | Quartus 16.0     | Vivado 2016.2   | :git-hdl:`Release Notes <releases/tag/2016_r2>`                                      | :doc:`2016_r2 </wiki-migration/resources/fpga/docs/downloads_2016_r2>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2016_r1`                                                       | Quartus 15.1     | Vivado 2015.4.2 | :git-hdl:`Release Notes <releases/tag/2016_r1>`                                      | :doc:`2016_r1 </wiki-migration/resources/fpga/docs/downloads_2016_r1>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2015_r2`                                                       | Quartus 15.0.2   | Vivado 2015.2   | :git-hdl:`Release Notes <releases/tag/2015_r2>`                                      | :doc:`2015_r2 </wiki-migration/resources/fpga/docs/downloads_2015_r2>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2015_r1`                                                       | Quartus 14.1     | Vivado 2014.4.1 | :git-hdl:`Release Notes <releases/tag/2015_r1>`                                      | :doc:`2015_r1 </wiki-migration/resources/fpga/docs/downloads_2015_r1>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2014_r2`                                                       | Quartus 14.0     | Vivado 2014.2   | :git-hdl:`Release Notes <releases/tag/2014_r2>`                                      | :doc:`2014_r2 </wiki-migration/resources/fpga/docs/downloads_2014_r2>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| :git-hdl:`tree/hdl_2014_r1`                                                       | Quartus 14.0     | Vivado 2013.4   | :git-hdl:`Release Notes <releases/tag/2014_r1>`                                      | :doc:`2014_r1 </wiki-migration/resources/fpga/docs/downloads_2014_r1>`     |
+-----------------------------------------------------------------------------------+------------------+-----------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#git
   :alt: Git Repository#hdl|Main page#build|Building & Generating programming files
