Precision Converters Firmware Build Guide
=========================================

.. tip::

   NOTE: For Local build (i.e., non-web-based build), the firmware repository needs to be cloned manually into local drive of your computer. For Remote/web/online build (supported by Mbed platform), cloning of the repository is not required.


Clone Precision Converters Firmware repository with the ``--recursive`` flag (not needed if building with web IDE for Mbed platform):

::

   git clone --recursive https://github.com/analogdevicesinc/precision-converters-firmware

If however you've already cloned the repository without the ``--recursive`` flag, you may initialize all the submodules in an existing cloned repo with:

::

   git submodule update --recursive --init

Build Prerequisites
-------------------

Prior to building a firmware project, it is required to set up an environment so that the build process may find the necessary tools (compiler, linker, SDK etc.). Use the following steps to prepare your environment for building firmware projects for respective platform.



.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

XHIDDENSTART STM32 (Click to expand) XHIDDENSTARTSTOP

XHIDDENSTART Build using STM32 IDE (click to expand) XHIDDENSTARTSTOP

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/pcg-fw-stm32-build-pre-requisites#STM Build Pre-requisites&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/pcg-fw-stm32-build-pre-requisites#STM Build Pre-requisites&showfooter=nofooter

.. raw:: html

   </details>


XHIDDENEND



.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

XHIDDENSTART For Web/Online Build (Click to expand) XHIDDENSTARTSTOP

-  Visit Arm Keil website to create an user account for accessing the web based Keil Studio IDE. `Keil Arm <https://www.keil.arm.com/>`_
-  Open `Keil Studio Web IDE <https://studio.keil.arm.com/>`_ with registered user account

.. raw:: html

   </details>




.. raw:: html

   <details><summary>For Make Build (Click to expand)</summary>

-  Install Make in the root of 'C' drive without any spaces in the installation path. The path must be C:\\GnuWin32\\... https://gnuwin32.sourceforge.net/packages/make.htm
-  Add the path of GnuWin32/bin directory into the system environmental path variable (as shown in below screenshot).
-  Install Git https://git-scm.com/downloads
-  Add the path of Git/usr/bin directory into system environmental path variable.
-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html
-  Install GNU Arm Embedded compiler (for the development, 9-2019-q4-major version is used).\ https://developer.arm.com/downloads/-/gnu-rm.
-  Add the path of GNU Arm Embedded Toolchain bin directory to system environmental path variable.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt. For example you can run **mbed config -G GCC_ARM_PATH "C:\\Program Files (x86)\\GNU Tools ARM Embedded\\9 2019-q4-major\\bin"** in command prompt. It will set mentioned compiler path to all the Mbed Projects.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/environmental_variables.png
   :align: center
   :width: 400px

.. raw:: html

   </details>


XHIDDENEND

XHIDDENEND

Building a project
------------------



.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

XHIDDENSTART STM32 (Click to expand) XHIDDENSTARTSTOP

XHIDDENSTART Build using STM32 IDE (click to expand) XHIDDENSTARTSTOP

.. image:: https://wiki.analog.com/_media/section>resources/tools-software/product-support-software/pcg-fw-stm32-build-guide#STM Build&showfooter=nofooter
   :alt: section>resources/tools-software/product-support-software/pcg-fw-stm32-build-guide#STM Build&showfooter=nofooter

.. raw:: html

   </details>


XHIDDENEND



.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

XHIDDENSTART Build Using Web/Online IDE (Click to expand) XHIDDENSTARTSTOP

-  Clone the Precision Converters Firmware repository into Keil Studio using "File->clone..." menu. The link to github repository is here: `precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`_

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/mbed_keil_studio_project_clone.jpg
   :align: center

-  Once the project repository is imported, wait until all library dependencies are imported as shown in below screenshot. Now, open the '.medignore' file present in the root directory of repository. Add comment syntax (two forward slashes) in front of the project name which you want to build. This will ignore all other projects and build only the comment syntax selected project.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/mbedignore_changes.png
   :align: center
   :width: 600px

-  Select the target device (default used for development is SDP-K1) and click on 'Clean build' option to build the project. After a successful build a binary will be downloaded to your computer- store this on your drive. Drag and drop this binary to the USB drive hosted by your controller board to flash the MCU.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/mbed_build.png
   :align: center
   :width: 400px

.. note::

   Note: If you intend to build different project, then modify the .medignore file in the root directory as mentioned in step2 and **clean build** project as mentioned in step3

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Build Using Make (Click to expand)</summary>

-  Open Git bash and change current directory to project directory (eg. "precision-converters-firmware/projects/ad4130_iio" directory) which you want to build.
-  Run **make** command to build the project.
-  After successful build, binary file is created into the Project_Name/build directory.
-  To clean build, run **make reset** command which deletes all generated build files for the given project.

.. tip::

   NOTE: Default TARGET_BOARD is SDP_K1 and COMPILER is GCC_ARM. Current Make based build only support GCC_ARM Compiler.


-  By default project is built for "SDP_K1" Board and "GCC_ARM" Compiler. If you want to build for other Mbed Board, For example If you want to build the project for "DISCO_F769NI" Board then run **make TARGET_BOARD=DISCO_F769NI** command in Command Prompt. Run **make reset TARGET_BOARD=DISCO_F769NI** command in Command Prompt to delete the generated build files for the given project.

.. raw:: html

   </details>


XHIDDENEND

XHIDDENEND

Running a project
-----------------

Once the firmware build is successful and binary file is generated, copy the generated binary into USB drive hosted by your MCU board (e.g. USB drive hosted by SDP-K1 board on windows). This will flash the binary file into MCU present on the controller board.
