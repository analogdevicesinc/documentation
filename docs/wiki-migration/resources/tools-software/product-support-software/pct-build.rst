Precision Converters Firmware Build Guide for Mbed Platform
===========================================================

Building Using Keil Studio Web IDE
----------------------------------

-  Clone the Precision Converters Firmware repository into Keil Studio using "File->clone..." menu. The link to github repository is here: `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/mbed_keil_studio_project_clone.jpg
   :align: center

-  Once the project repository is imported, wait until all library dependencies are imported as shown in below screenshot. Now, open the '.medignore' file present in the root directory of repository. Add comment syntax (two forward slashes) in front of the project name which you want to build. This will ignore all other projects and build only the comment syntax selected project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/lib_import_mbedignore_change.jpg
   :align: center

-  Select the target device (default used for development is SDP-K1) and click on 'Clean build' option to build the project. After a successful compile a binary will be downloaded to your computer- store this on your drive. Drag and drop this binary to the USB drive hosted by your controller board to flash the MCU.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/mbed_clean_build.jpg
   :align: center
   :width: 300px

.. note::

   Note: If you intend to build different project, then modify the .medignore file in the root directory as mentioned in step2 and clan build project as mentioned in step3


Building Using Make
-------------------

Clone Precision Converter Repository into local drive of your PC:

::

   git clone https://github.com/analogdevicesinc/precision-converters-firmware

Build Prerequisites
~~~~~~~~~~~~~~~~~~~

Prior to building a Precision Converter project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Necessary tools and configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Install Make.\ https://gnuwin32.sourceforge.net/packages/make.htm
-  Add the path of Make into system environmental variables.

|image1|\ |image2|

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html
-  Install GNU Arm Embedded compiler (for the development, 9-2019-q4-major version is used).\ https://developer.arm.com/downloads/-/gnu-rm.
-  Add the path of GNU Arm Embedded Toolchain to system environmental variables.

|image3|\ |image4|

-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

Building a project
~~~~~~~~~~~~~~~~~~

-  Open Command Prompt and change current directory to project directory which you want to build.
-  Run "make" command in the project directory. If you want to clean the previous build files and rebuild project, then run "make clean" followed with "make" command in Command Prompt.
-  After successful build, binary file is created into the Project_Name/build/TARGET_Name/COMPILER_Name directory.

.. tip::

   NOTE: Default TARGET_Name is SDP_K1 and COMPILER_Name is GCC_ARM.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/make_installed_directory.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/make_install_path_setting.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/arm_gcc_folder.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/arm_gcc_environ_variable.png
   :width: 400px
