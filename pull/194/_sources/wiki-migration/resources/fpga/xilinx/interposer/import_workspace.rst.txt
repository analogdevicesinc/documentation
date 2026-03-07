The hardware platform for each reference projects with FMC-SDP interposer and KC705 evaluation board is common. The next steps should be followed to recreate the software project of the reference design:

-  First download the **KC705 Reference project** from Github on your computer. You can do this by clonning this repository: https://github.com/analogdevicesinc/fpgahdl_xilinx.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/github_repository_folder.jpg
   :alt: Github Repository
   :width: 200px

-  From this entire repository you will use **cf_sdp_kc705** folder. This is common for all KC705 projects.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/edk_kc705_project_folder.jpg
   :alt: EDK KC705 project
   :width: 200px

-  Open the Xilinx SDK. When the SDK starts, it asks you to provide a folder where to store the workspace. Any folder can be provided. Make sure that the path where it is located does not contain any spaces.
-  In the SDK select the **File->Import** menu option to import the software projects into the workspace.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/file_import.png
   :alt: Import Projects
   :width: 200px

-  In the *Import* window select the **General->Existing Projects into Workspace** option.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/existing_project_import.png
   :alt: Existing Projects Import
   :width: 200px

-  In the *Import Projects* window select the **cf_sdp_kc705** folder as root directory and check the **Copy projects into workspace** option. After the root directory is chosen the projects that reside in that directory will appear in the *Projects* list. Press *Finish* to finalize the import process.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/projects_import.png
   :alt: Projects Import
   :width: 200px

-  The *Project Explorer* window now shows the projects that exist in the workspace without software files.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/project_explorer.jpg
   :alt: Project Explorer
   :width: 200px

-  Now the software must be added in your project. For downloading the software, you must use 3 links from Github given in **Downloads** section. From there you'll download the specific driver, the specific commands and the Xilinx Boards Common Drivers(which are commons for all Xilinx boards). All the software files downloaded must be copied in **src** folder from sw folder.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/project_complete.jpg
   :alt: Project complete
   :width: 200px

.. important::

   
   -  Before compilation in the file called **Communication.h** you have to uncomment the name of the device that you currently use. In the picture below there is an example of this, which works only with AD5629R project. For another device, uncomment only the respective name. You can have one driver working on multiple devices, so the drivers's name and the uncommented name may not be the same for every project.


   
   |Communication.h|

-  The SDK should automatically build the project and the *Console* window will display the result of the build. If the build is not done automatically, select the **Project->Build Automatically** menu option.
-  If the project was built without any errors, you can program the FPGA and run the software application.

.. |Communication.h| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad9739a_ebz/uncomment_com_file.jpg
   :width: 200px
