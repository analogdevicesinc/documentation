IIO DEMO project
================

IIO DEMO Overview
-----------------

IIO DEMO project is independent of a physical device and should be used as reference, when creating a new iio application for a new iio device.

IIO DEMO project emulates two devices: 1 16-bit ADC and 1 16-bit DAC by using two emulated drivers: adc_demo and dac_demo.

ADC Demo Driver
---------------

ADC Demo Driver Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for ADC Demo driver can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADC Demo Driver|

   -

   |Implementation of ADC Demo Driver|

ADC Demo Code Driver Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:

-  `ADC Demo Header file <http://analogdevicesinc.github.io/no-OS/adc__demo_8h.html>`_
-  `ADC Demo Source file <http://analogdevicesinc.github.io/no-OS/adc__demo_8c.html>`_

DAC Demo Driver
---------------

DAC Demo Driver Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for DAC Demo driver can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of DAC Demo Driver|

   -

   |Implementation of DAC Demo Driver|

DAC Demo Code Driver Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:

-  `DAC Demo Header file <http://analogdevicesinc.github.io/no-OS/dac__demo_8h.html>`_
-  `DAC Demo Source file <http://analogdevicesinc.github.io/no-OS/dac__demo_8c.html>`_

ADC IIO Demo Driver
-------------------

ADC IIO Demo Driver Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for ADC IIO Demo driver can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of ADC IIO Demo Driver|

   -

   |Implementation of ADC IIO Demo Driver|

   -

   |Implementation of ADC IIO Demo Driver Trigger|

ADC IIO Demo Code Driver Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:

-  `ADC IIO Demo Header file <http://analogdevicesinc.github.io/no-OS/iio__adc__demo_8h.html>`_
-  `ADC IIO Demo Source file <http://analogdevicesinc.github.io/no-OS/iio__adc__demo_8c.html>`_
-  `ADC IIO Demo Trigger Source file <http://analogdevicesinc.github.io/no-OS/iio__adc__demo__trig_8c.html>`_

DAC IIO Demo Driver
-------------------

DAC IIO Demo Driver Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source code for DAC IIO Demo driver can be found here:

.. admonition:: Download
   :class: download

   
   -


   
   |Header file of DAC IIO Demo Driver|

   -

   |Implementation of DAC IIO Demo Driver|

DAC IIO Demo Code Driver Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code documentation for the driver is automatically generated using the Doxygen tool and it is available below:

-  `DAC IIO Demo Header file <http://analogdevicesinc.github.io/no-OS/iio__dac__demo_8h.html>`_
-  `DAC IIO Demo Source file <http://analogdevicesinc.github.io/no-OS/iio__dac__demo_8c.html>`_

No-OS Supported Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~

The following platforms are supported:

-  STM32
-  ADUCM3029
-  XILINX
-  LINUX
-  PICO

No-OS Build Setup
-----------------

No-OS Clone
~~~~~~~~~~~

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof 
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers: 

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

.. _no-os-build-guide-1:

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

.. _build-prerequisites-1:

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


.. _building-a-project-1:

Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

.. _runningdebugging-1:

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers:

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

.. _no-os-build-guide-2:

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

.. _build-prerequisites-2:

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


.. _building-a-project-2:

Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

.. _runningdebugging-2:

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers:

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

++++ Debugging with Vitis 2025.1 (Unified IDE) \|

.. important::

   Starting with Vitis 2023.2, Xilinx transitioned from Eclipse to a Unified IDE architecture. **Vitis 2025.1 now features automatic debug configuration** - no manual setup required!


**Key Changes in Vitis 2025.1:**

-  Debug configuration **automatically generated** by build system
-  Bitstream and initialization files **auto-extracted** from XSA
-  Architecture-specific settings **auto-configured** (ZynqMP, Zynq, MicroBlaze, Versal)
-  Just click **FLOW → Debug** to start debugging!

Prerequisites
-------------

-  Vitis 2025.1 installed
-  Hardware design file (.xsa) in project directory
-  JTAG and UART cables connected to target board

WSL2 Users: One-Time xsdb Fix
-----------------------------

.. important::

   On WSL2, xsdb crashes with "Segmentation fault" due to rlwrap incompatibility. Apply this fix once per machine.


**If you've already applied this fix previously, skip this step.**

**Automated Installation (Recommended):**

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh

**Manual Installation:**

::

   cd /path/to/no-OS

   # Backup original
   sudo cp /xilinx/2025.1/Vitis/bin/xsdb /xilinx/2025.1/Vitis/bin/xsdb.original

   # Install fixed version
   sudo cp tools/scripts/platform/xilinx/xsdb-nowrap /xilinx/2025.1/Vitis/bin/xsdb
   sudo chmod +x /xilinx/2025.1/Vitis/bin/xsdb

**Note:** This is a system-wide fix, only needs to be done once per machine.

Per-Project Setup (First Time Only)
-----------------------------------

Step 1: Build Project
~~~~~~~~~~~~~~~~~~~~~

.. important::

   For optimal debugging, always build with ``DEBUG=1``. This enables proper debug symbols and correct source path mapping.


::

   source /xilinx/2025.1/Vitis/settings64.sh
   cd /path/to/no-OS/projects/your_project
   make clean
   make DEBUG=1

**What happens:**

-  Build runs with debug optimization (``‑O0``, no optimization)
-  Full debug symbols added (``‑g3``)
-  Source path mapping configured (``‑fdebug‑prefix‑map``)
-  First build automatically runs ``make project`` (generates BSP and FSBL)
-  Creates ``build/your_project.elf`` with debug symbols

.. tip::

   **Without DEBUG=1**, you'll experience:

   
   -  Code stepping doesn't work properly (optimized code)
   -  Variables optimized out and not visible
   -  Breakpoints may not hit expected lines
   


Step 2: Open Vitis IDE
~~~~~~~~~~~~~~~~~~~~~~

::

   make sdkopen

**First time only:** When Vitis opens, you'll see "Update Workspace" dialog:

-  Message: "Vitis IDE cannot recognize the workspace version. Click 'Update' to initialize the workspace metadata."
-  Click **"Update"** button
-  This initializes the workspace (one-time setup)

**What happens automatically:**

-  Vitis opens at project root
-  Workspace metadata initialized
-  ``_ide/`` directory created
-  **Bitstream extracted** from XSA to ``_ide/system_top/system_top.bit``
-  **Initialization script extracted** (``psu_init.tcl`` or ``ps_init.tcl``)
-  **Debug configuration generated** (``_ide/launch.json``) with:

   -  Correct architecture settings (ZynqMP/Zynq/MicroBlaze/Versal)
   -  Hardware platform path (XSA file)
   -  FSBL configuration (if applicable)
   -  Application ELF path
   -  Target processor

.. note::

   **No manual configuration needed!** The debug configuration is ready to use immediately.


Step 3: Verify Configuration (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to verify or customize the auto-generated configuration:

#. In Vitis Explorer, expand ``_ide`` folder
#. Open ``launch.json`` to view the configuration
#. Configuration named ``<project_name>_app_hw_1`` is ready to use

The configuration is automatically regenerated each time you run ``make sdkopen``.

Debugging Your Project
----------------------

Hardware Setup
~~~~~~~~~~~~~~

-  Connect JTAG cable to your board
-  Connect UART cable (for console output)
-  Power on the board

Start Debugging
~~~~~~~~~~~~~~~

**In Vitis IDE:**

#. Make sure you've built with ``make DEBUG=1``
#. Click **FLOW** panel (left side) → Click **"Debug"**
#. Debug session starts immediately!

.. warning::

   The **Start Debugging (F5)** button in the Debug panel does not currently work for Vitis 2025.1. Always use **FLOW → Debug** button.


**What happens:**

#. Vitis connects to board via JTAG
#. Programs FPGA with bitstream
#. Runs FSBL to initialize processor (ZynqMP/Zynq only)
#. Loads your application ELF
#. Stops at entry point - ready to debug!

**Debug Features:**

-  Set breakpoints (click left margin in code)
-  Step through code (F5=Step Into, F6=Step Over, F7=Step Return, F8=Resume)
-  Inspect variables, registers, call stack
-  Watch expressions
-  View memory and disassembly

Daily Development Workflow
--------------------------

After initial setup:

::

   # 1. Edit code

   # 2. Build with debug symbols
   make clean
   make DEBUG=1

   # 3. Open Vitis and debug
   make sdkopen
   # Click FLOW → Debug → Debugging starts immediately!

.. tip::

   For production builds (no debugging), use ``make`` without ``DEBUG=1`` to get optimized code.


Architecture-Specific Notes
---------------------------

The build system automatically detects your hardware architecture and configures debug settings appropriately.

**ZynqMP (Cortex-A53/R5):**

-  Processor: ``psu_cortexa53_0`` or ``psu_cortexr5_0``
-  Debug Type: ``baremetal-zu``
-  FSBL Required: Yes (auto-configured)
-  Init Script: ``psu_init.tcl``

**Zynq-7000 (Cortex-A9):**

-  Processor: ``ps7_cortexa9_0``
-  Debug Type: ``baremetal-zynq``
-  FSBL Required: Yes (auto-configured)
-  Init Script: ``ps_init.tcl``

**MicroBlaze:**

-  Processor: ``microblaze_0``
-  Debug Type: ``baremetal-mb``
-  FSBL Required: No (auto-configured)

**Versal (Cortex-A72):**

-  Processor: ``psv_cortexa72_0``
-  Debug Type: ``baremetal-versal``
-  Uses PLM (Platform Loader Manager) instead of FSBL (auto-configured)

Troubleshooting
---------------

**"Segmentation fault" when debugging:**

-  Solution: Install xsdb WSL2 fix (see above)

**Debug doesn't start / "undefined" connection errors:**

-  Make sure you clicked "Update" on first workspace open
-  Verify ``_ide/launch.json`` exists
-  Try ``make sdkopen`` again to regenerate configuration

**Stepping doesn't work / variables optimized out:**

-  Solution: Rebuild with ``make clean && make DEBUG=1``

**For complete documentation, see:** :git-no-OS:`Xilinx Vitis Debugging Guide <doc/sphinx/source/build_guides/build_xilinx_vitis2025.rst>`

++++

++++ Debugging with Vitis 2023.2-2024.x (Classic Eclipse IDE) \|

.. important::

   The ``make sdkopen`` command automatically detects Vitis 2023.2-2024.x and launches the **Classic Eclipse IDE** (using the ``-classic`` flag) instead of the Unified IDE. This provides better stability and complete debug configuration support for makefile-based projects.


.. warning::

   **Manual debug configuration required** for Classic Eclipse mode. For automatic configuration, upgrade to Vitis 2025.1+.


**Why Classic Mode for Vitis 2023.2-2024.x?**

-  Vitis 2023.2 introduced the Unified IDE, but the User Managed Mode (required for makefile-based projects) has incomplete debug configuration support
-  The classic Eclipse mode provides a mature, fully-functional debugging experience

.. _prerequisites-1:

Prerequisites
-------------

-  Vitis 2023.2, 2023.2, 2024.1, or 2024.2 installed
-  Hardware design file (.xsa) in project directory
-  JTAG and UART cables connected to target board

.. _wsl2-users-one-time-xsdb-fix-1:

WSL2 Users: One-Time xsdb Fix
-----------------------------

.. important::

   On WSL2, xsdb crashes with "Segmentation fault" due to rlwrap incompatibility. Apply this fix once per machine.


**If you've already applied this fix previously, skip this step.**

**Automated Installation (Recommended):**

For default Vitis installation (``/xilinx/<version>/Vitis``):

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh

For custom Vitis installation location:

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /custom/path/to/Vitis/bin

**Examples:**

::

   # Vitis 2024.2 at default location
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /xilinx/2024.2/Vitis/bin

   # Vitis 2023.2 at custom location
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /opt/Xilinx/Vitis/2023.2/bin

   # Vitis on Windows drive (WSL)
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /mnt/c/Xilinx/Vitis/2024.1/bin

**Note:** This is a system-wide fix, only needs to be done once per machine.

.. _per-project-setup-first-time-only-1:

Per-Project Setup (First Time Only)
-----------------------------------

.. _step-1-build-project-1:

Step 1: Build Project
~~~~~~~~~~~~~~~~~~~~~

.. important::

   For optimal debugging, always build with ``DEBUG=1``. This enables proper debug symbols and correct source path mapping.


::

   source /path/to/xilinx/Vitis/2023.2/settings64.sh
   cd /path/to/no-OS/projects/your_project
   make clean
   make DEBUG=1

**What happens:**

-  Build runs with debug optimization (``‑O0``, no optimization)
-  Full debug symbols added (``‑g3``)
-  Source path mapping configured
-  First build automatically runs ``make project`` (generates BSP and FSBL)
-  Creates ``build/your_project.elf`` with debug symbols

Step 2: Open Vitis Classic Eclipse IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   make sdkopen

**What happens:**

-  The command automatically detects Vitis 2023.2-2024.x
-  Launches the **Classic Eclipse IDE** (not the Unified IDE)
-  Workspace opens at ``build/`` directory
-  Standard Eclipse workspace with ``.metadata/`` directory

Step 3: Create and Configure Debug (Manual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   Classic Eclipse requires manual debug configuration. This is a one-time setup per project.


**A. Open Debug Configurations Dialog:**

In the Vitis IDE menu bar:

-  Go to **Run** → **Debug Configurations...**
-  Or click the **Debug** toolbar button dropdown → **Debug Configurations...**

The "Debug Configurations" dialog will open.

**B. Create New Configuration:**

#. In the left panel, expand **"Single Application Debug"**
#. Click the **"New Configuration"** button (first icon in the toolbar - looks like a document with a star/plus)
#. A new configuration will be created (e.g., ``Debugger_-Default``)
#. You can rename it if desired (e.g., ``adrv904x-debug``)

**C. Configure Main Tab:**

The **"Main"** tab should be selected by default.

**Debug Type:**

-  Select **"Standalone Application Debug"** from the dropdown
-  (Not "Attach to running target" - we want to reset and program the system)

**Connection:**

-  Leave as **"Local"** (debugging via local JTAG connection)

**D. Configure Target Setup Tab:**

Click the **"Target Setup"** tab at the top.

**Hardware Platform:**

-  Should auto-populate with the path to your ``.xsa`` file
-  If empty, click **"Browse..."** and select ``system_top.xsa`` from your project root

**Bitstream File:**

-  Auto-populated from the XSA file
-  Path will be similar to: ``.../projects/your_project/system_top.bit``

**FSBL Configuration** (ZynqMP/Zynq-7000 only):

Check these boxes:

-  ☑ **Use FSBL flow for initialization**
-  ☑ **Reset entire system**
-  ☑ **Program FPGA**
-  ☑ **Initialize using FSBL**

**FSBL File:**

Browse to or enter the FSBL path:

::

   build/tmp/output/hw0/export/hw0/sw/hw0/boot/fsbl.elf

.. note::

   For MicroBlaze: Uncheck "Use FSBL flow for initialization" - MicroBlaze doesn't use FSBL


**Summary Panel:**

After configuration, the Summary panel on the right shows the debug sequence:

#. Reset system and clear FPGA
#. Program FPGA with bitstream
#. Initialize PS using FSBL
#. Load application and suspend processors

**E. Configure Application Tab:**

Click the **"Application"** tab at the top.

**Processor Selection:**

The IDE shows a table with available processors. Check the box next to your target processor:

-  **ZynqMP**: ``psu_cortexa53_0`` (or ``psu_cortexr5_0`` for R5)
-  **Zynq-7000**: ``ps7_cortexa9_0``
-  **MicroBlaze**: ``microblaze_0``
-  **Versal**: ``psv_cortexa72_0``

**Project and Application:**

The IDE typically auto-populates these fields:

-  **Project**: Should show your project name (e.g., ``adrv904x``)
-  **Application**: Should point to your ELF file: ``build/your_project.elf``

.. tip::

   If the Application field is empty, click **"Search..."** and browse to ``build/your_project.elf``\


**Stop at 'main':**

-  Check this box to have the debugger stop at the ``main()`` function (recommended)

**F. Save and Apply:**

#. Click **"Apply"** to save the configuration
#. Click **"Debug"** to start debugging immediately, or **"Close"** to save for later

The configuration is now saved and ready to use!

.. _debugging-your-project-1:

Debugging Your Project
----------------------

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

-  Connect JTAG cable to your board
-  Connect UART cable (for console output)
-  Power on the board

.. _start-debugging-1:

Start Debugging
~~~~~~~~~~~~~~~

**In Vitis Classic Eclipse IDE:**

#. Make sure you've built with ``make DEBUG=1``
#. Go to **Run** → **Debug Configurations...**
#. Select your debug configuration (e.g., "adrv904x-debug")
#. Click **"Debug"** button
#. The Debug perspective will open automatically

**What happens:**

#. Vitis connects to board via JTAG
#. Programs FPGA with bitstream
#. Runs FSBL to initialize processor (ZynqMP/Zynq only)
#. Loads your application ELF
#. Stops at entry point (usually ``main()``) - ready to debug!

**Debug Features:**

-  Set breakpoints (click left margin in code)
-  Step through code (F5=Step Into, F6=Step Over, F7=Step Return, F8=Resume)
-  Inspect variables, registers, call stack
-  Watch expressions
-  View memory and disassembly

.. _daily-development-workflow-1:

Daily Development Workflow
--------------------------

After initial setup:

::

   # 1. Edit code

   # 2. Build with debug symbols
   make clean
   make DEBUG=1

   # 3. Debug
   make sdkopen
   # In Vitis Eclipse: Run → Debug Configurations → Select your config → Debug

.. _architecture-specific-notes-1:

Architecture-Specific Notes
---------------------------

**ZynqMP (Cortex-A53/R5):**

-  Processor: ``psu_cortexa53_0`` or ``psu_cortexr5_0``
-  FSBL Required: Yes
-  FSBL Path: ``build/tmp/output/hw0/export/hw0/sw/hw0/boot/fsbl.elf``

**Zynq-7000 (Cortex-A9):**

-  Processor: ``ps7_cortexa9_0``
-  FSBL Required: Yes
-  FSBL Path: Same as ZynqMP

**MicroBlaze:**

-  Processor: ``microblaze_0``
-  FSBL Required: No (soft processor)
-  In debug config: Uncheck "Use FSBL flow for initialization"

**Versal (Cortex-A72):**

-  Processor: ``psv_cortexa72_0``
-  Uses PLM (Platform Loader Manager) instead of FSBL

.. _troubleshooting-1:

Troubleshooting
---------------

**"Segmentation fault" when debugging:**

-  Solution: Install xsdb WSL2 fix (see above)

**Stepping doesn't work / variables optimized out:**

-  Solution: Rebuild with ``make clean && make DEBUG=1``

**IDE doesn't open or wrong IDE opens:**

-  Verify you're using Vitis 2023.2-2024.x
-  The Classic Eclipse IDE should open (not the Unified IDE)
-  If Unified IDE opens, the version detection may be incorrect

**For complete documentation, see:** :git-no-OS:`Xilinx Vitis Debugging Guide <doc/sphinx/source/build_guides/build_xilinx_vitis2025.rst>`

++++


No-OS Build Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~

Please follow the steps below for No-OS Setup based on the environment you are using. Make sure you use the information for the specific platform you are using (e.g. STM32, ADUCM3029, etc.).

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>



No-OS Build Project
~~~~~~~~~~~~~~~~~~~

The path of the project is no-OS/projects/iio_demo/

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof 
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp


Debug
~~~~~

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof 
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers: 

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

.. _no-os-build-guide-1:

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

.. _build-prerequisites-1:

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


.. _building-a-project-1:

Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

.. _runningdebugging-1:

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers:

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

.. _no-os-build-guide-2:

No-OS Build Guide
=================

Clone NO-OS with the ``--recursive`` flag:

::

   git clone --recursive https://github.com/analogdevicesinc/no-OS

If however you've already cloned NO-OS without the ``--recursive`` flag, you may initialize all the submodules in an existing NO-OS clone with:

::

   git submodule update --recursive --init

.. _build-prerequisites-2:

Build Prerequisites
-------------------

Prior to building a no-OS project, it is required to set up some environment variables so that the build process may find the necessary tools (compiler, linker, SDK etc.).

Use the following commands to prepare your environment for building no-OS projects: 

.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

.. important::

   Make sure the GNU Make version you are using is >= 4.2.




.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Assuming the SDK is installed at this path:

::

   /path/to/intel
   └── intelFPGA
       └── 18.1

Run:

::

   $ source no-OS/tools/scripts/platform/intel/environment.sh /path/to/intel/intelFPGA 18.1

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   /path/to/xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

Run:

::

   $ source /path/to/xilinx/Vitis/2022.2/settings64.sh

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`_.
-  Set the MAXIM_LIBRARIES environment variable to the MaximSDK/Libraries path (the default should be ~/MaximSDK/Libraries).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Install Mbed CLI 1 as per guide here: https://os.mbed.com/docs/mbed-os/v6.15/build-tools/install-and-set-up.html .Usually the following steps should be sufficient: ``sudo apt install python3 python3-pip git mercurial gcc-arm-none-eabi`` and ``sudo python3 -m pip install mbed-cli pyelftools==0.29``.
-  Configure the compiler location with Mbed CLI. This can be carried out by running the "mbed config -G GCC_ARM_PATH "path-to-your-gcc-compiler"" in Command Prompt.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`_.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.

.. important::

   Please install all the necessary packs locally and then manually import them in CrossCore


Common Issues with environment setup:

-  Makefiles searches for the CCES_HOME in its default installation directory. It may happen that multiple version are installed and may not work. To select a ``CCES_HOME`` run ``export CCES_HOME=/opt/analog/cces/2.10.0``

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Open up a Git Bash as Administrator once and run the ``tools/scripts/git-bash.sh`` script. Close the window. You only need to do this once per Git Bash installation.


.. important::

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`_.


.. important::

   Use Git Bash (unelevated) for the rest of your development.




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Assuming the Vitis 2022.2 is installed at this path:

::

   C:\Xilinx
   ├── DocNav
   ├── Downloads
   └── Vitis
       └── 2022.2

From the no-OS root directory, run:

::

   $ source tools/scripts/git-bash-paths.sh /c/Xilinx/Vitis/2022.2/settings64.sh

Or alternatively, work only with the desired paths:

::

   $ export PATH=/c/Xilinx/Vitis/2022.2/bin:/c/Xilinx/Vitis/2022.2/gnu/aarch64/nt/aarch64-none/bin/:$PATH

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`_ to a path without whitespaces like ``C:\MaximSDK``.
-  Set the MAXIM_LIBRARIES environment variable by running: ``export MAXIM_LIBRARIES=/c/MaximSDK/Libraries``.
-  (Optional) For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

-  Initialize the mbed submodule in no-OS by running <code> $ git submodule update init mbed-os </code> and <code> $ git submodule update mbed-os </code>
-  Install Python 3.11.2 (https://www.python.org/downloads/release/python-3112/)
-  Install the virtual environment package by running from the Git Terminal ``$ pip install venv`` or ``$ pip install virtualenv``
-  Create a virtual environment by running the command ``$ python -m venv <name_of_virtual_environment>`` This will create a virtual environment with the set name in the current directory of the Git Terminal.
-  Activate environment by running ``$ source <location_and_name_of_virtual_environment>/Scripts/activate``
-  Install GNU Arm Embedded Compiler (version: **9-2019-q4-major**) from https://developer.arm.com/downloads/-/gnu-rm.
-  Remove line 20 of **requirements.txt** inside the mbed-os folder ("*hidapi>=0.7.99,<0.8.0;platform_system!="Linux"* ")
-  Install the requirements by running ``$ <location_and_name_of_virtual_environment>/Scripts/pip install -r requirements.txt`` Doing this will run the pip command using the python script inside our virtual environment.
-  Install the previously removed line from **requirements.txt** by running <code> $ <location_and_name_of_virtual_environment>/Scripts/pip install "cython<3.0.0" && <location_and_name_of_virtual_environment>/Scripts/pip install "hidapi>=0.7.99,<0.8.0;platform_system!='Linux'" </code>
-  Install mbed cli using ``$ <location_and_name_of_virtual_environment>/Scripts/pip install mbed-cli``
-  Configure the compiler location with Mbed CLI. This can be carried out by running in Git Terminal: <code> $ mbed config -G GCC_ARM_PATH <path_to_your_gcc_compiler</code>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`_) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`_)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`_ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`_ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

.. raw:: html

   </details>

.. raw:: html

   </details>


.. _building-a-project-2:

Building a project
------------------

Go in the project directory that should be built.



.. raw:: html

   <details><summary>Linux (Click to expand)</summary>

::

   $ cd no-OS/projects/project_name/
   $ tree
   .
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Intel (Click to expand)</summary>

Copy the **.sof** and **.sopcinfo** to the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk  system_bd.sopcinfo  adrv9009_a10gx.sof
   $ make

   # Alternatively you may select a .sopcinfo file explicitly by:
   $ make HARDWARE=path/to/system_bd.sopcinfo

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** in the project folder.

::

   $ ls
   Makefile  profiles  src  src.mk system_top.xsa
   $ make

   # Alternatively you may select an .xsa file explicitly by:
   $ make HARDWARE=path/to/file.xsa

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Pico (Click to expand)</summary>

To build a project, type:

::

   make PLATFORM=pico

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

The ADuCM3029 projects also contain a ``pinmux_config.c`` file which contains pin configuration instructions.

::

   # build an ADuCM3029-only project
   $ make

   # if the platform autodetection picks the wrong platform, explicitly specify the PLATFORM
   $ make PLATFORM=aducm3029

.. raw:: html

   </details>

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Windows (Click to expand)</summary>

.. important::

   Use Git Bash to run these commands.


::

   $ cd no-OS/projects/project_name

It should contain make-related files and source files:

::

   ./no-OS/projects/project_name
   ├── builds.json
   ├── Makefile
   ├── src
   └── src.mk



.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

Copy the **.xsa** to the project folder and run:

::

   ./no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   ├── src
   ├── src.mk
   └── system_top.xsa

   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To build a project, type:

::

   $ make PLATFORM=maxim TARGET=...

The ``TARGET`` specifies the chip for which the project is built. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Mbed (Click to expand)</summary>

.. important::

   Make sure that the virtual environment is activated (environment name enclosed in parenthesis appears in the git terminal) and that the packages from prerequisites were installed.


To build a project, type:

::

   make PLATFORM=mbed TARGET_BOARD=...

The ``TARGET_BOARD`` specifies the board for which the project is built. If not specified, it defaults to ``SDP-K1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

::

   $ export PLATFORM=aducm3029
   $ make

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

Assuming you've installed STM32CubeMX at C:\\stm32cubemx and STM32CubeIDE to C:\\stm32cubeide, run these commands prior to building to let the build system know where they are installed:

::

   $ export STM32CUBEMX=/c/stm32cubemx
   $ export STM32CUBEIDE=/c/stm32cubeide

Make sure you have the .ioc file in the project directory, then type:

::

   $ make PLATFORM=stm32

If during the project generation you get a dialog saying that you are using an .ioc file generated with an old CubeMX version, click ``Continue``. ``Migrate`` is also a valid option but only if you know what you are doing.

If you're trying to use an .ioc file generated with a newer CubeMX than the one installed on your machine, you will get a prompt that asks you to upgrade your installation to the new version, there is no other choice than to click ``OK`` and then manually upgrade.

.. raw:: html

   </details>

.. raw:: html

   </details>


The build process creates a **build** directory in the project folder:

::

   build
   ├── app
   ├── bsp
   ├── obj
   ├── project_name.elf
   └── tmp

.. _runningdebugging-2:

Running/Debugging
-----------------

Once the ``.elf``, ``.hex`` or ``.bin`` file has been generated, make sure the board is powered on, JTAG cable connected and use the following commands to upload the program to the board or debug.

Uploading the binary to target is achieved with:

::

   $ make run

This feature is not implemented for some platform-OS combinations. Instead, use the following command to launch the IDE to handle flashing and debugging:

::

   $ make sdkopen



.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

To debug a project, type:

::

   make PLATFORM=maxim TARGET=... run

The ``TARGET`` specifies the chip for which the project is built and run. If it is missing, ``max32660`` will be used. At the moment, the available targets are: ``max32650``, ``max32655``, ``max32660``, ``max32665``, ``max32670``, ``max32690`` and ``max78000``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Xilinx (Click to expand)</summary>

**Booting from SD Card**

You may also boot a Xilinx project from an SD card, copy the generated build/BOOT.BIN file onto the first partition of the card, ensuring it is formatted as FAT32. Insert the card, set the jumpers for SD boot, and power on the system.

**Remote host**

For Xilinx project you can flash the board connected to a remote host. On the remote host make sure to start \`hw_server\`. On your development environment run

::

   $ export XSCT_REMOTE_HOST=<remote host ip>
   $ export XSCT_REMOTE_PORT=<remote host hw_server port>
   $ make run

By default the \`hw_server\` port should be 3121.

.. raw:: html

   </details>


Use the following command to launch the SDK associated to the used platform in order to be able to debug graphically by clicking the debug button:

::

   $ make sdkopen

Fore more details about the available make rules, :doc:`check out this page </wiki-migration/resources/no-os/make>`.

++++ Running/Debugging in WSL \|

If you use WSL you can not test the boards on Linux because it does not support USB. If you will try to load the binary into the target with the command **make run**, you will encounter the following error:

.. important::

   no targets found with "name =~ "APU\*" && jtag_cable_name =~ "\*\ :math:`::jtagtarget*"". available targets: none while executing "error "no targets found with \"`\ params(filter)\\". available targets:$target_list""...


If you use WSL (Ubuntu) and want to connect to JTAG with a board, you have to switch the USB device from Windows to WSL. To do this, the following steps must be followed:

::

    * It is recommended to have a version of Windows 10 or 11.
    * You must have all updates installed in WSL.
        To be able to see the kernel version, the WSL version, and other features, in WSL (Ubuntu) you can enter the command:

::

   :~$ uname -a
   Linux 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

WSL should have a kernel version of 5.10.60.1 or later. You also need to run WSL2.Testing was done on version 22.4 of Ubuntu.

::

    * You need to install the [[https://github.com/dorssel/usbipd-win/releases|usbipd-win]] project. Installation can be done manually, with a few clicks.
    * You need to install from WSL, the user space tools for USB/IP and a database of USB hardware identifiers:

::

   :~$ sudo apt upgrade
   :~$ sudo apt update
   :~$ sudo apt install linux-tools-virtual hwdata
   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip $(command -v ls /usr/lib/linux-tools/*/usbip | tail -n1) 20

If the last command does not work, try:

::

   :~$ sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip


   | tail -n1` 20

If there is a device connected to the USB port, it can be checked from the Device Manager. When connecting via JTAG, in Device Manager, the device will appear in the Universal serial Bus controllers section as USB Serial Converter.

To attach the JTAG (or any USB device) from Windows to WSL we must do the following:

::

    * Open Command Prompt in Administrator mode and enter the command:

::

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Not attached
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

For this command, a list of all connected USB devices will be displayed in Windows, a brief description of them and their status: If they are/are not attached to the WSL instance. The JTAG appears in the cmd list but is not attached to a WSL instance.

In WSL enter the following command:

::

   :~$ lsusb
   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

A list of all attached USB devices will be displayed here. At this moment we will only see roots hubs.

::

    * To attach a USB device to WSL enter the following command in Command Prompt:

::

   > usbipd wsl attach -b <BUSID>

BUSID represents the ID for the USB device for which we want to attach it in WSL.

::

   > usbipd wsl attach -b 10-1

   C:\Windows\system32> usbipd wsl list
   BUSID  VID:PID    DEVICE                                                        STATE
   2-6    0c45:6732  Integrated Webcam, Integrated IR Webcam                       Not attached
   2-9    27c6:63ac  Goodix MOC Fingerprint                                        Not attached
   2-10   8087:0033  Intel(R) Wireless Bluetooth(R)                                Not attached
   5-4    0bda:8153  Realtek USB GbE Family Controller #2                          Not attached
   7-1    413c:4503  USB Input Device                                              Not attached
   7-2    413c:b080  Dell DA20 Adapter                                             Not attached
   9-5    413c:b06e  USB Input Device                                              Not attached
   10-1   0403:6014  USB Serial Converter                                          Attached - Ubuntu
   10-2   045e:0837  Microsoft Modern USB Headset, USB Input Device                Not attached
   10-3   04b4:0008  USB Serial Device (COM17)                                     Not attached
   10-5   413c:b06f  USB Input Device                                              Not attached

After running usbipd wsl list, it can be seen that the JTAG is now attached in WSL.

In WSL if you run: **lsusb** we have:

::

   Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 005: ID 0403:6014 Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub\

If Device Manager checks the USB device attached in WSL, it will no longer appear in the list of devices.

::

    * If you want to return to the initial settings (the USB device must be attached to Windows): The USB device must be disconnected and connected to the computer or in Command Prompt, run the following command:

::

   > usbipd wsl detach -b <BUSID>

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`_ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`_ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`_.
-  In PowerShell, set the variables below, correcting with the absolute paths of your stm32cubeide install:

::

     $stm32cubeide="C:\ST\STM32CubeIDE_1.16.1\STM32CubeIDE"
   $openocd_bin="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.externaltools.openocd.win32_2.3.200.202404091248\tools\bin\openocd.exe"
     $openocd_scripts="$stm32cubeide\plugins\com.st.stm32cube.ide.mcu.debug.openocd_2.2.100.202406131243\resources\openocd\st_scripts"

-  Extract the pair of deliverables (e.g., **some_project.elf.openocd**, **project.elf**) in a folder.

   -  The **.openocd** will be the same regardless of the Makefile configuration.

-  Navigate to the folder in PowerShell

::

     cd ~\path\to\my_project

-  Set the **<project>.elf.openocd** **<project>.elf** (yes, the slashes are correct)

::

     $openocd_cmd=".\some_project.elf.openocd"
     $openocd_elf="./some_project.elf"

-  And run:

::

     &"$openocd_bin" -s "$openocd_scripts" -f $openocd_cmd -c "program $openocd_elf verify reset exit"

.. raw:: html

   </details>


++++

++++ Debugging with Vitis 2025.1 (Unified IDE) \|

.. important::

   Starting with Vitis 2023.2, Xilinx transitioned from Eclipse to a Unified IDE architecture. **Vitis 2025.1 now features automatic debug configuration** - no manual setup required!


**Key Changes in Vitis 2025.1:**

-  Debug configuration **automatically generated** by build system
-  Bitstream and initialization files **auto-extracted** from XSA
-  Architecture-specific settings **auto-configured** (ZynqMP, Zynq, MicroBlaze, Versal)
-  Just click **FLOW → Debug** to start debugging!

Prerequisites
-------------

-  Vitis 2025.1 installed
-  Hardware design file (.xsa) in project directory
-  JTAG and UART cables connected to target board

WSL2 Users: One-Time xsdb Fix
-----------------------------

.. important::

   On WSL2, xsdb crashes with "Segmentation fault" due to rlwrap incompatibility. Apply this fix once per machine.


**If you've already applied this fix previously, skip this step.**

**Automated Installation (Recommended):**

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh

**Manual Installation:**

::

   cd /path/to/no-OS

   # Backup original
   sudo cp /xilinx/2025.1/Vitis/bin/xsdb /xilinx/2025.1/Vitis/bin/xsdb.original

   # Install fixed version
   sudo cp tools/scripts/platform/xilinx/xsdb-nowrap /xilinx/2025.1/Vitis/bin/xsdb
   sudo chmod +x /xilinx/2025.1/Vitis/bin/xsdb

**Note:** This is a system-wide fix, only needs to be done once per machine.

Per-Project Setup (First Time Only)
-----------------------------------

Step 1: Build Project
~~~~~~~~~~~~~~~~~~~~~

.. important::

   For optimal debugging, always build with ``DEBUG=1``. This enables proper debug symbols and correct source path mapping.


::

   source /xilinx/2025.1/Vitis/settings64.sh
   cd /path/to/no-OS/projects/your_project
   make clean
   make DEBUG=1

**What happens:**

-  Build runs with debug optimization (``‑O0``, no optimization)
-  Full debug symbols added (``‑g3``)
-  Source path mapping configured (``‑fdebug‑prefix‑map``)
-  First build automatically runs ``make project`` (generates BSP and FSBL)
-  Creates ``build/your_project.elf`` with debug symbols

.. tip::

   **Without DEBUG=1**, you'll experience:

   
   -  Code stepping doesn't work properly (optimized code)
   -  Variables optimized out and not visible
   -  Breakpoints may not hit expected lines
   


Step 2: Open Vitis IDE
~~~~~~~~~~~~~~~~~~~~~~

::

   make sdkopen

**First time only:** When Vitis opens, you'll see "Update Workspace" dialog:

-  Message: "Vitis IDE cannot recognize the workspace version. Click 'Update' to initialize the workspace metadata."
-  Click **"Update"** button
-  This initializes the workspace (one-time setup)

**What happens automatically:**

-  Vitis opens at project root
-  Workspace metadata initialized
-  ``_ide/`` directory created
-  **Bitstream extracted** from XSA to ``_ide/system_top/system_top.bit``
-  **Initialization script extracted** (``psu_init.tcl`` or ``ps_init.tcl``)
-  **Debug configuration generated** (``_ide/launch.json``) with:

   -  Correct architecture settings (ZynqMP/Zynq/MicroBlaze/Versal)
   -  Hardware platform path (XSA file)
   -  FSBL configuration (if applicable)
   -  Application ELF path
   -  Target processor

.. note::

   **No manual configuration needed!** The debug configuration is ready to use immediately.


Step 3: Verify Configuration (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to verify or customize the auto-generated configuration:

#. In Vitis Explorer, expand ``_ide`` folder
#. Open ``launch.json`` to view the configuration
#. Configuration named ``<project_name>_app_hw_1`` is ready to use

The configuration is automatically regenerated each time you run ``make sdkopen``.

Debugging Your Project
----------------------

Hardware Setup
~~~~~~~~~~~~~~

-  Connect JTAG cable to your board
-  Connect UART cable (for console output)
-  Power on the board

Start Debugging
~~~~~~~~~~~~~~~

**In Vitis IDE:**

#. Make sure you've built with ``make DEBUG=1``
#. Click **FLOW** panel (left side) → Click **"Debug"**
#. Debug session starts immediately!

.. warning::

   The **Start Debugging (F5)** button in the Debug panel does not currently work for Vitis 2025.1. Always use **FLOW → Debug** button.


**What happens:**

#. Vitis connects to board via JTAG
#. Programs FPGA with bitstream
#. Runs FSBL to initialize processor (ZynqMP/Zynq only)
#. Loads your application ELF
#. Stops at entry point - ready to debug!

**Debug Features:**

-  Set breakpoints (click left margin in code)
-  Step through code (F5=Step Into, F6=Step Over, F7=Step Return, F8=Resume)
-  Inspect variables, registers, call stack
-  Watch expressions
-  View memory and disassembly

Daily Development Workflow
--------------------------

After initial setup:

::

   # 1. Edit code

   # 2. Build with debug symbols
   make clean
   make DEBUG=1

   # 3. Open Vitis and debug
   make sdkopen
   # Click FLOW → Debug → Debugging starts immediately!

.. tip::

   For production builds (no debugging), use ``make`` without ``DEBUG=1`` to get optimized code.


Architecture-Specific Notes
---------------------------

The build system automatically detects your hardware architecture and configures debug settings appropriately.

**ZynqMP (Cortex-A53/R5):**

-  Processor: ``psu_cortexa53_0`` or ``psu_cortexr5_0``
-  Debug Type: ``baremetal-zu``
-  FSBL Required: Yes (auto-configured)
-  Init Script: ``psu_init.tcl``

**Zynq-7000 (Cortex-A9):**

-  Processor: ``ps7_cortexa9_0``
-  Debug Type: ``baremetal-zynq``
-  FSBL Required: Yes (auto-configured)
-  Init Script: ``ps_init.tcl``

**MicroBlaze:**

-  Processor: ``microblaze_0``
-  Debug Type: ``baremetal-mb``
-  FSBL Required: No (auto-configured)

**Versal (Cortex-A72):**

-  Processor: ``psv_cortexa72_0``
-  Debug Type: ``baremetal-versal``
-  Uses PLM (Platform Loader Manager) instead of FSBL (auto-configured)

Troubleshooting
---------------

**"Segmentation fault" when debugging:**

-  Solution: Install xsdb WSL2 fix (see above)

**Debug doesn't start / "undefined" connection errors:**

-  Make sure you clicked "Update" on first workspace open
-  Verify ``_ide/launch.json`` exists
-  Try ``make sdkopen`` again to regenerate configuration

**Stepping doesn't work / variables optimized out:**

-  Solution: Rebuild with ``make clean && make DEBUG=1``

**For complete documentation, see:** :git-no-OS:`Xilinx Vitis Debugging Guide <doc/sphinx/source/build_guides/build_xilinx_vitis2025.rst>`

++++

++++ Debugging with Vitis 2023.2-2024.x (Classic Eclipse IDE) \|

.. important::

   The ``make sdkopen`` command automatically detects Vitis 2023.2-2024.x and launches the **Classic Eclipse IDE** (using the ``-classic`` flag) instead of the Unified IDE. This provides better stability and complete debug configuration support for makefile-based projects.


.. warning::

   **Manual debug configuration required** for Classic Eclipse mode. For automatic configuration, upgrade to Vitis 2025.1+.


**Why Classic Mode for Vitis 2023.2-2024.x?**

-  Vitis 2023.2 introduced the Unified IDE, but the User Managed Mode (required for makefile-based projects) has incomplete debug configuration support
-  The classic Eclipse mode provides a mature, fully-functional debugging experience

.. _prerequisites-1:

Prerequisites
-------------

-  Vitis 2023.2, 2023.2, 2024.1, or 2024.2 installed
-  Hardware design file (.xsa) in project directory
-  JTAG and UART cables connected to target board

.. _wsl2-users-one-time-xsdb-fix-1:

WSL2 Users: One-Time xsdb Fix
-----------------------------

.. important::

   On WSL2, xsdb crashes with "Segmentation fault" due to rlwrap incompatibility. Apply this fix once per machine.


**If you've already applied this fix previously, skip this step.**

**Automated Installation (Recommended):**

For default Vitis installation (``/xilinx/<version>/Vitis``):

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh

For custom Vitis installation location:

::

   cd /path/to/no-OS
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /custom/path/to/Vitis/bin

**Examples:**

::

   # Vitis 2024.2 at default location
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /xilinx/2024.2/Vitis/bin

   # Vitis 2023.2 at custom location
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /opt/Xilinx/Vitis/2023.2/bin

   # Vitis on Windows drive (WSL)
   sudo tools/scripts/platform/xilinx/install_xsdb_wsl2_fix.sh /mnt/c/Xilinx/Vitis/2024.1/bin

**Note:** This is a system-wide fix, only needs to be done once per machine.

.. _per-project-setup-first-time-only-1:

Per-Project Setup (First Time Only)
-----------------------------------

.. _step-1-build-project-1:

Step 1: Build Project
~~~~~~~~~~~~~~~~~~~~~

.. important::

   For optimal debugging, always build with ``DEBUG=1``. This enables proper debug symbols and correct source path mapping.


::

   source /path/to/xilinx/Vitis/2023.2/settings64.sh
   cd /path/to/no-OS/projects/your_project
   make clean
   make DEBUG=1

**What happens:**

-  Build runs with debug optimization (``‑O0``, no optimization)
-  Full debug symbols added (``‑g3``)
-  Source path mapping configured
-  First build automatically runs ``make project`` (generates BSP and FSBL)
-  Creates ``build/your_project.elf`` with debug symbols

Step 2: Open Vitis Classic Eclipse IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   make sdkopen

**What happens:**

-  The command automatically detects Vitis 2023.2-2024.x
-  Launches the **Classic Eclipse IDE** (not the Unified IDE)
-  Workspace opens at ``build/`` directory
-  Standard Eclipse workspace with ``.metadata/`` directory

Step 3: Create and Configure Debug (Manual)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   Classic Eclipse requires manual debug configuration. This is a one-time setup per project.


**A. Open Debug Configurations Dialog:**

In the Vitis IDE menu bar:

-  Go to **Run** → **Debug Configurations...**
-  Or click the **Debug** toolbar button dropdown → **Debug Configurations...**

The "Debug Configurations" dialog will open.

**B. Create New Configuration:**

#. In the left panel, expand **"Single Application Debug"**
#. Click the **"New Configuration"** button (first icon in the toolbar - looks like a document with a star/plus)
#. A new configuration will be created (e.g., ``Debugger_-Default``)
#. You can rename it if desired (e.g., ``adrv904x-debug``)

**C. Configure Main Tab:**

The **"Main"** tab should be selected by default.

**Debug Type:**

-  Select **"Standalone Application Debug"** from the dropdown
-  (Not "Attach to running target" - we want to reset and program the system)

**Connection:**

-  Leave as **"Local"** (debugging via local JTAG connection)

**D. Configure Target Setup Tab:**

Click the **"Target Setup"** tab at the top.

**Hardware Platform:**

-  Should auto-populate with the path to your ``.xsa`` file
-  If empty, click **"Browse..."** and select ``system_top.xsa`` from your project root

**Bitstream File:**

-  Auto-populated from the XSA file
-  Path will be similar to: ``.../projects/your_project/system_top.bit``

**FSBL Configuration** (ZynqMP/Zynq-7000 only):

Check these boxes:

-  ☑ **Use FSBL flow for initialization**
-  ☑ **Reset entire system**
-  ☑ **Program FPGA**
-  ☑ **Initialize using FSBL**

**FSBL File:**

Browse to or enter the FSBL path:

::

   build/tmp/output/hw0/export/hw0/sw/hw0/boot/fsbl.elf

.. note::

   For MicroBlaze: Uncheck "Use FSBL flow for initialization" - MicroBlaze doesn't use FSBL


**Summary Panel:**

After configuration, the Summary panel on the right shows the debug sequence:

#. Reset system and clear FPGA
#. Program FPGA with bitstream
#. Initialize PS using FSBL
#. Load application and suspend processors

**E. Configure Application Tab:**

Click the **"Application"** tab at the top.

**Processor Selection:**

The IDE shows a table with available processors. Check the box next to your target processor:

-  **ZynqMP**: ``psu_cortexa53_0`` (or ``psu_cortexr5_0`` for R5)
-  **Zynq-7000**: ``ps7_cortexa9_0``
-  **MicroBlaze**: ``microblaze_0``
-  **Versal**: ``psv_cortexa72_0``

**Project and Application:**

The IDE typically auto-populates these fields:

-  **Project**: Should show your project name (e.g., ``adrv904x``)
-  **Application**: Should point to your ELF file: ``build/your_project.elf``

.. tip::

   If the Application field is empty, click **"Search..."** and browse to ``build/your_project.elf``\


**Stop at 'main':**

-  Check this box to have the debugger stop at the ``main()`` function (recommended)

**F. Save and Apply:**

#. Click **"Apply"** to save the configuration
#. Click **"Debug"** to start debugging immediately, or **"Close"** to save for later

The configuration is now saved and ready to use!

.. _debugging-your-project-1:

Debugging Your Project
----------------------

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

-  Connect JTAG cable to your board
-  Connect UART cable (for console output)
-  Power on the board

.. _start-debugging-1:

Start Debugging
~~~~~~~~~~~~~~~

**In Vitis Classic Eclipse IDE:**

#. Make sure you've built with ``make DEBUG=1``
#. Go to **Run** → **Debug Configurations...**
#. Select your debug configuration (e.g., "adrv904x-debug")
#. Click **"Debug"** button
#. The Debug perspective will open automatically

**What happens:**

#. Vitis connects to board via JTAG
#. Programs FPGA with bitstream
#. Runs FSBL to initialize processor (ZynqMP/Zynq only)
#. Loads your application ELF
#. Stops at entry point (usually ``main()``) - ready to debug!

**Debug Features:**

-  Set breakpoints (click left margin in code)
-  Step through code (F5=Step Into, F6=Step Over, F7=Step Return, F8=Resume)
-  Inspect variables, registers, call stack
-  Watch expressions
-  View memory and disassembly

.. _daily-development-workflow-1:

Daily Development Workflow
--------------------------

After initial setup:

::

   # 1. Edit code

   # 2. Build with debug symbols
   make clean
   make DEBUG=1

   # 3. Debug
   make sdkopen
   # In Vitis Eclipse: Run → Debug Configurations → Select your config → Debug

.. _architecture-specific-notes-1:

Architecture-Specific Notes
---------------------------

**ZynqMP (Cortex-A53/R5):**

-  Processor: ``psu_cortexa53_0`` or ``psu_cortexr5_0``
-  FSBL Required: Yes
-  FSBL Path: ``build/tmp/output/hw0/export/hw0/sw/hw0/boot/fsbl.elf``

**Zynq-7000 (Cortex-A9):**

-  Processor: ``ps7_cortexa9_0``
-  FSBL Required: Yes
-  FSBL Path: Same as ZynqMP

**MicroBlaze:**

-  Processor: ``microblaze_0``
-  FSBL Required: No (soft processor)
-  In debug config: Uncheck "Use FSBL flow for initialization"

**Versal (Cortex-A72):**

-  Processor: ``psv_cortexa72_0``
-  Uses PLM (Platform Loader Manager) instead of FSBL

.. _troubleshooting-1:

Troubleshooting
---------------

**"Segmentation fault" when debugging:**

-  Solution: Install xsdb WSL2 fix (see above)

**Stepping doesn't work / variables optimized out:**

-  Solution: Rebuild with ``make clean && make DEBUG=1``

**IDE doesn't open or wrong IDE opens:**

-  Verify you're using Vitis 2023.2-2024.x
-  The Classic Eclipse IDE should open (not the Unified IDE)
-  If Unified IDE opens, the version detection may be incorrect

**For complete documentation, see:** :git-no-OS:`Xilinx Vitis Debugging Guide <doc/sphinx/source/build_guides/build_xilinx_vitis2025.rst>`

++++


Example Project Execution on Linux
----------------------------------

IIO Example
~~~~~~~~~~~

Because this project does not require any hardware, it can be run also locally on your Linux OS.

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the IIO example project for a specific platform make sure you have the following configuration in the Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   IIO_EXAMPLE = y
   IIO_TRIGGER_EXAMPLE = n

When running make command, specify the platform you want to build it for, as shown below:

::

   // ADUCM platform
   make PLATFORM=aducm3029
   // Linux platform
   make PLATFORM=linux
   // STM32 platform
   make PLATFORM=stm32
   // XILINX platform
   make PLATFORM=xilinx
   // PICO platform
   make PLATFORM=pico

In this case, we are going to build the project for Linux platform, using the command:

::

   no-OS/projects/iio_demo$ make PLATFORM=linux

Project Execution
^^^^^^^^^^^^^^^^^

After the build is successful we can run the application, using the command:

::

   no-OS/projects/iio_demo$ ./build/iio_demo.out 

Now, by running iio_info in the Linux terminal, we can see the emulated IIO devices, as shown below:

::

   no-OS/projects/iio_demo$ iio_info -u ip:127.0.0.1
   Library version: 0.24 (git tag: 735ac65)
   Compiled with backends: local xml ip usb serial
   IIO context created with network backend.
   Backend version: 1.1 (git tag: 0000000)
   Backend description string: 127.0.0.1 no-OS analog 1.1.0-g0000000 #1 Tue Nov 26 09:52:32 IST 2019 armv7l
   IIO context has 3 attributes:
       no-OS: 1.1.0-g0000000
       ip,ip-addr: 127.0.0.1
       uri: ip:127.0.0.1
   IIO context has 2 devices:
       iio:device0: adc_demo (buffer capable)
           2 channels found:
               voltage0: adc_in_ch0 (input, index: 0, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: adc_channel_attr value: 1111
               voltage1: adc_in_ch1 (input, index: 1, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: adc_channel_attr value: 1112
           1 device-specific attributes found:
                   attr  0: adc_global_attr value: 3333
           1 debug attributes found:
                   debug attr  0: direct_reg_access value: 0
   ERROR: checking for trigger : Invalid argument (22)
       iio:device1: dac_demo (buffer capable)
           2 channels found:
               voltage0: dac_out_ch0 (output, index: 0, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: dac_channel_attr value: 1111
               voltage1: dac_out_ch1 (output, index: 1, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: dac_channel_attr value: 1112
           1 device-specific attributes found:
                   attr  0: dac_global_attr value: 4444
           1 debug attributes found:
                   debug attr  0: direct_reg_access value: 0
   ERROR: checking for trigger : Invalid argument (22)

It can be observed that two iio_devices are found: **adc_demo** and **dac_demo**. Each device has a device specific attribute (adc_demo: **adc_global_attr** and dac_demo: **dac_global_attr**) and a debug attribute for direct register access.

It can also be observed that each device has two voltage-type channels and each channel has a channel specific attribute:

-  adc_demo: adc_in_ch0, adc_in_ch1
-  dac_demo: dac_out_ch0, dac_out_ch1

If ENABLE_LOOPBACK is not defined in src/app_config.h, then a sine loop will be returned when reading a buffer from adc_demo device. This can be achieved using iio_readdev command or using IIO Osc.

::

   iio_readdev -u ip:127.0.0.1 -b 400 -s 400 adc_demo > samples.dat

For IIO Osc, connect to the device and use the plot functionality to view the data, as shown below:


|image1|

If ENABLE_LOOPBACK is defined in src/app_config.h, then the dac_demo device can also be used to upload data to the buffer used by adc_demo (the data given to the dac will be looped back to the adc device). If no data is loaded, the default data will be shown, which is 0. In order to write data to dac_demo, you can use either iio_writedev command or DAC Data Manager plugin from IIO Osc. When using iio_writedev, we can use iio_readdev to read back the data we wrote, as shown below:

::

   // write 400 samples to dac
   cat sample_sine.dat | iio_writedev -u ip:127.0.0.1 -b 400 -s 400   dac_demo
   // read 400 samples from adc -> should be the same as the one we wrote previously 
   iio_readdev -u ip:127.0.0.1 -b 400 -s 400 adc_demo > dac_samples.dat

For IIO Osc, connect to the device and use the DAC Data Manager to load data. Then use the plot functionality to view the loaded data. It can be seen how plotted data is changing when new data is loaded:


|image2|

IIO Trigger Example
~~~~~~~~~~~~~~~~~~~

.. _makefile-selection-1:

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the IIO trigger example project for a specific platform make sure you have the following configuration in the Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   IIO_EXAMPLE = n
   IIO_TRIGGER_EXAMPLE = y

The following steps are perform on Linux platform.

By running iio_info, we can see the emulated IIO devices, as shown below:

::

   no-OS/projects/iio_demo$ iio_info -u ip:127.0.0.1
   Library version: 0.24 (git tag: 735ac65)
   Compiled with backends: local xml ip usb serial
   IIO context created with network backend.
   Backend version: 1.1 (git tag: 0000000)
   Backend description string: 127.0.0.1 no-OS analog 1.1.0-g0000000 #1 Tue Nov 26 09:52:32 IST 2019 armv7l
   IIO context has 3 attributes:
       no-OS: 1.1.0-g0000000
       ip,ip-addr: 127.0.0.1
       uri: ip:127.0.0.1
   IIO context has 3 devices:
       iio:device0: adc_demo (buffer capable)
           2 channels found:
               voltage0: adc_in_ch0 (input, index: 0, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: adc_channel_attr value: 1111
               voltage1: adc_in_ch1 (input, index: 1, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: adc_channel_attr value: 1112
           1 device-specific attributes found:
                   attr  0: adc_global_attr value: 3333
           1 debug attributes found:
                   debug attr  0: direct_reg_access value: 0
           No trigger assigned to device
       iio:device1: dac_demo (buffer capable)
           2 channels found:
               voltage0: dac_out_ch0 (output, index: 0, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: dac_channel_attr value: 1111
               voltage1: dac_out_ch1 (output, index: 1, format: le:S16/16>>0)
               1 channel-specific attributes found:
                   attr  0: dac_channel_attr value: 1112
           1 device-specific attributes found:
                   attr  0: dac_global_attr value: 4444
           1 debug attributes found:
                   debug attr  0: direct_reg_access value: 0
           No trigger assigned to device
       trigger0: adc-demo-sw-trig
           0 channels found:
           1 device-specific attributes found:
                   attr  0: trigger_now ERROR: No such file or directory (2)
   ERROR: checking for trigger : No such device (19)

It can be observed, that in this case a new device is available, adc-demo-sw-trig. This device can be used as a trigger to sample data from adc_demo device. This is a software trigger, meaning that the trigger is activated by software, when performing writes to its attribute. In this case the name of the attribute is trigger_now.

The writing to the trigger_now attribute can be performed using the iio_attr command as follows:

::

   iio_attr -u ip:127.0.0.1 -d trigger0 trigger_now 1

This command will write the value 1 to the trigger_now attribute of trigger0 device and it will activate the trigger one time. If we want to obtain 10 samples, we need to run the command 10 times.

The following python script can be used to send automatically the iio_attr command:

::

   import sys
   import os

   my_uri = sys.argv[1] if len(sys.argv) >= 3 else "ip:127.0.0.1"
   my_samples = sys.argv[2] if len(sys.argv) >= 3 else 200

   print("Executing trigger_now attribute for trigger0");
   print("for uri: " + str(my_uri))
   print("for " + str(my_samples) + " samples\n");
   i = 0
   while i < int(my_samples):
       i+=1
       os.system("iio_attr -u "+my_uri+" -d trigger0 trigger_now 1 \n")
       print("triggered "+str(i)+" times\n" )

Below, you can see an example with software trigger usage:


|image3|

.. |Header file of ADC Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/adc/adc_demo/adc_demo`.h
.. |Implementation of ADC Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/adc/adc_demo/adc_demo`.c
.. |Header file of DAC Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/dac/dac_demo/dac_demo`.h
.. |Implementation of DAC Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/dac/dac_demo/dac_demo`.c
.. |Header file of ADC IIO Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/adc/adc_demo/iio_adc_demo`.h
.. |Implementation of ADC IIO Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/adc/adc_demo/iio_adc_demo`.c
.. |Implementation of ADC IIO Demo Driver Trigger| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/adc/adc_demo/iio_adc_demo_trig`.c
.. |Header file of DAC IIO Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/dac/dac_demo/iio_dac_demo`.h
.. |Implementation of DAC IIO Demo Driver| image:: https://wiki.analog.com/_media/:git-no-OS:`drivers/dac/dac_demo/iio_dac_demo`.c
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/iio_demo/iio_demo_plot.gif
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/iio_demo/iio_demo_loopback.gif
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/iio_demo/plot_sw_trigger.gif
