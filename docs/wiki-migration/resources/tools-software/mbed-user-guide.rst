Toolchain download and instalation guide:
=========================================

This user guide explains the steps necessary to set up the development environment for a STNucleo board on Windows. The setup for other mbed boards or the Linux is similar. This userguide was created using information from https://github.com/gnuarmeclipse

Step 1 - Analog Devices mbed repository
---------------------------------------

Download or clone the Analog Devices mbed repository from https://github.com/analogdevicesinc/mbed-adi

Step 2 - Download and install compiler
--------------------------------------

Download and install the GNU ARM Embedded Toolchain from https://launchpad.net/gcc-arm-embedded/5.0/5-2015-q4-major

When setup prompts to add path to the environment variables it is recommended to pick yes.

Step 3 - mbed libraries
-----------------------

The Analog Devices mbed repository does not contain the mbed libraries, so in order to compile the projects, you need to download the mbed libraries specific to the board you are using.

The mbed libraries can be built from source or downloading them from the online compiler (much easier but requires creating account).

In order to build from source:

Skip any step where a compatible tool already exists

The following steps are detailed at https://github.com/mbedmicro/mbed

-  Install Python 2.7.9 or above and make sure it's added to path
-  Install Git and make sure it's added to path
-  Install virtualenv in python

To activate and setup the virtual environment

-  venv/Scripts/activate
-  To install all dependencies
-  pip install -r requirements.txt

The following steps are detailed at https://developer.mbed.org/handbook/mbed-tools

Add path to compiler in \\tools\\settings.py. It should be something like this:

-  GCC_ARM_PATH = "c:\\\\Program Files (x86)\\\\GNU Tools ARM Embedded\\\\5.2 2015q4\\\\bin"

In .\\tools run

-  python build.py -h

this will output the help of the build function and make sure everything is installed properly

Run

-  python build.py -m NUCLEO_F411RE -t GCC_ARM

to build the mbed libraries for the Nucleo MCU. If other targets are needed, simply change the NUCLEO_F411RE parameter to the appropriate target. A list of targets can be found in the command help issued before.

When the process finishes, the sources will be available in the \\.build folder. Copy the contents of the folder to the Analog Devices mbed repository.

Steps for downloading libraries from online compiler: The easiest way to get the mbed libraries specific for your board is to download them from the online compiler. In order to do this, you should create an account on https://developer.mbed.org/.

After logging in, go to https://developer.mbed.org/platforms/ , select the board you are using and click "Add to your mbed compiler" button on the right-hand side of the board page. |image1| When the board was added, the "Add to your mbed compiler" button converts to "Open mbed Compiler". Open the mbed compiler and create a new project using the "Blinky LED test" template. |image2| A new project appears in the Program Workspace. In order to get the mbed libraries, rightclick on the project and choose Export Program. In the popup choose GCC(ARM Embedded), and click export. |image3| Extract the downloaded project, and copy the mbed folder from the project to the root of the repository. This will enable using the apropriate libraries in the Analog Devices mbed repository.

Step 4 - Download and install build tools
-----------------------------------------

Download and install GNU ARM Windows Build Tools from https://github.com/gnuarmeclipse/windows-build-tools/releases When finished, add path to the build tools bin folder in environment variables. If install location has not been changed, the default path is C:\\Program Files\\GNU ARM Eclipse\\Build Tools

\\2.6-201507152002\\bin

We should now be able to build a project. In order to test this, go to the Analog devices repository, open a terminal in mbed-adi\\examples\\adxl362_example and run "make all"

If all the paths were set, the build process should conclude with the following message


|image4|

If the mbed board is connected to the PC, a new drive should appear labeled NODE-F411RE(for STNucleo F411RE). Copy the .bin file that was created after running "make all" to this drive. The bin file will be flashed to the board.

|image5|.

The quickest way to do this, after "make all" run the "copy <project_binary_file>.bin <mbed_drive_letter>:"


|image6|

Step 5 - (Nucleo Specific)
--------------------------

Connect the STNucleo board to the PC. Upgrade the firmware using the following guide: https://developer.mbed.org/teams/ST/wiki/Nucleo-Firmware

Step 6 - Download Eclipse and Java Runtime Environment
------------------------------------------------------

Download and install the latest Eclipse version from http://www.eclipse.org/downloads/packages/eclipse-ide-cc-developers/neonr

Download and install the latest version of Java Runtime Environment(if you don't have it already) from http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html

Step 7 - Download and install GNU ARM Eclipse plugins and OpenOCD debugger
--------------------------------------------------------------------------

Open Eclipse, go to Help-> Eclipse Marketplace. Search for GNU ARM Eclipse and click install on the first result. This The options should have the OpenOCD plugin checked. After installation is successful close Eclipse.

Download and install the latest version of OpenOCD debugger for eclipse from https://github.com/gnuarmeclipse/openocd/releases Run Eclipse and in the Eclipse menu, go to (Window →) Preferences → Run/Debug → OpenOCD and click "Restore defaults". This should enable the OpenOCD plugin if it was installed correctly.

Additional information can be found at http://gnuarmeclipse.github.io/debug/openocd/

Step 8 - Importing, building and debugging the project.
-------------------------------------------------------

In order to import a project in eclipse go to File -> Import. In the C/C++ category, select Existing Code as Makefile Project, and navigate to an example project in the mbed-adi repository.

Toolchain for Indexer Settings can be set to <none> After the project was imported, simply rightclick the project in the project explorer(left-hand side) and select Build project. After building, the console view of Eclipse should look like this:

.. image:: https://wiki.analog.com/_media/resources/tools-software/2016-06-28_16_44_45-c_c_-_cn0398_example_libraries_cn0398_cn0398.cpp_-_eclipse.png
   :align: center

In order to debug the project. Go to Run -> Debug configurations. Double click the GDB OpenOCD Debugging to create a new debug configuration. In the C/C\\+\\+ application edit box, navigate to the elf file generated by the build. In the debugger tab, under config options put "-f board/st_nucleo_f4.cfg". This enables debug configuration for the ST Nucleo board.

Other board/target configurations can be found in the openOCD folder in \\scripts\\board and \\scripts\\target. Also change the executable in GDB Client Setup to arm-none-eabi-gdb.

Click debug, and Eclipse should start the debug process

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/2016-06-28_14_53_14-nucleo-f411re_mbed.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/2016-06-28_14_49_54-mbed_compiler.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/2016-06-28_14_52_20-mbed_compiler_nucleo_blink_led.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/2016-10-26_17_07_23-c_windows_system32_cmd.exe.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/2016-10-26_16_37_36-computer.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/2016-10-26_17_04_09-c_windows_system32_cmd.exe.png
