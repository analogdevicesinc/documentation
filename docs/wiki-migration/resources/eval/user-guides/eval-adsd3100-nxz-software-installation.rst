ToF Eval Software Package
=========================

This user guide is to step through installation steps for the EVAL-ADSD3100-NXZ & EVAL-ADTF3175-NXZ software package. Contents such as ADIToFGUI and Data Collect are built from our public sdk : :doc:`SDK development </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-development>`

Evaluation software consists of:

-  :doc:`ADIToFGUI </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`
-  :doc:`Data Collect (Command line interface) </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`
-  :doc:`Depth Compute (Command line interface) </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`

Download Installer
------------------

-  If you are evaluating the ; EVAL-ADSD3100-NXZ or EVAL-ADTF3175-NXZ modules:

   -  Download v2.1.1 installer from here : :git-ToF:`Link <releases/tag/v2.1.1>` (Copy the link and run it on another tab if clicking directly does not work)

-  If you are evaluating the ; EVAL-ADTF3175D-NXZ

   -  Download latest 5.x.x installer from here : :git-ToF:`Link <releases>`

Minimum Software Requirements
-----------------------------

-  Seventh Gen Intel Core i5 Processor @ 2.4GHz , Dual Core
-  8 GB Memory
-  Graphics driver support for openCL 2.0+

Intro
-----

-  Once installer is downloaded, run the application to see this window. Click 'Next'.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/s1.png
   :align: center

License
-------

-  Read through license and select 'I accept the agreement' option. Click 'Next'

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/s2.png
   :align: center

Installation Location
---------------------

-  Select a location to install the package
-  Click 'Next', and click 'Install' on the next page

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/s3.png
   :align: center

Prerequisites Downloads
-----------------------

The installer will prompt the user to install the following pre-reqs if they are not detected on your pc

-  OpenCL 2.0 Runtime
-  Visual Studio 2015 redistributable

Image Download
--------------

-  Once the installer is done, the user will have the option to download the NXP image (Recommended for each install of sdk, backwards compatibility is not guaranteed)

   -  If selected a command prompt will open with download status
   -  The user can find the image in the 'Image' folder at the install location (See next section)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/s5.png
   :align: center

Image Folder Contents
---------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/image_folder.png
   :align: center
   :width: 200px

-  microsd-xxxxxxxx : NXP SOM sd card image

   -  Flashing instructions : :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/flashing_image_instructions>`

-  fwUpdate_X.X.X : This is the ADSD3500 firmware

   -  Update instructions here : :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz-upgrade-firmware>`

-  depth_compute : Contains depth compute binaries

   -  More information : :doc:`Link </wiki-migration/resources/eval/user-guides/eval-adtf3175d-depth-compute-libs>`

.. important::

   Please follow the steps here for correct update procedure : :doc:`eval-adtf3175d-nxz-bringup </wiki-migration/resources/eval/user-guides/eval-adtf3175d-nxz-bringup>`\


Done
----

-  Once installation is done you can navigate to the installation folder to run the following applications:

   -  :doc:`ADIToFGUI </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui>`
   -  :doc:`Data Collect (Command line interface) </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`
   -  :doc:`Depth Compute (Command line interface) </wiki-migration/resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`
