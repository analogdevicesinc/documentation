ADRV9009/ADRV9008 No-OS System Level Design Setup
=================================================

Supported devices
-----------------

-  :adi:`ADRV9008-1`
-  :adi:`ADRV9008-2`
-  :adi:`ADRV9009`

Supported evaluation boards
---------------------------

-  :adi:`EVAL-ADRV9008-9009`
-  :adi:`ADRV9009-ZU11EG`
-  :adi:`AD-FMCOMMS8-EBZ`

Supported carriers
------------------

-  `Intel Arria 10 GX FPGA Development Kit <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`__
-  `ZC706 <https://www.xilinx.com/ZC706>`__
-  `ZCU102 <https://www.xilinx.com/ZCU102>`__
-  :adi:`ADRV2CRR-FMC`

Project layout
--------------

The project is located under ``no-OS/projects/adrv9009`` and has the following layout, with source code under the ``src`` subdirectory and reference profiles obtained with TES software under ``profiles`` subdirectory.

::

   $ tree
   no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   │   ├── tx_bw100_ir122p88_rx_bw100_or122p88_orx_bw100_or122p88_dc122p88
   │   │   ├── talise_config_ad9528.h
   │   │   ├── talise_config.c
   │   │   └── talise_config.h
   │   ├── tx_bw200_ir245p76_rx_bw200_or245p76_orx_bw200_or245p76_dc245p76
   │   │   ├── talise_config_ad9528.h
   │   │   ├── talise_config.c
   │   │   └── talise_config.h
   │   └── tx_bw400_ir491p52_rx_bw200_or245p76_orx_bw400_or491p52_dc245p76
   │       ├── talise_config_ad9528.h
   │       ├── talise_config.c
   │       └── talise_config.h
   ├── src
   │   ├── app
   │   │   ├── app_clocking.c
   │   │   ├── app_clocking.h
   │   │   ├── app_config.h
   │   │   ├── app_jesd.c
   │   │   ├── app_jesd.h
   │   │   ├── app_talise.c
   │   │   ├── app_talise.h
   │   │   ├── app_transceiver.c
   │   │   ├── app_transceiver.h
   │   │   └── headless.c
   │   ├── devices
   │   │   └── adi_hal
   │   │       ├── adi_hal.h
   │   │       ├── common.h
   │   │       ├── LICENSE.txt
   │   │       ├── no_os_hal.c
   │   │       └── parameters.h
   │   └── README
   └── src.mk

The ADRV9009 driver may be found under ``no-OS/drivers/rf-transceiver/talise/api`` and the firmware files under ``no-OS/drivers/rf-transceiver/talise/firmware``.

TES artefacts
-------------

You may use the :ez:`\|TES software <wide-band-rf-transceivers/tes-gui-software-support-adrv9009-adrv9008-1-adrv9008-2/w/documents/13807/tes-gui-api-software-support-adrv9009->` to generate profiles and corresponding Stream Binary by graphically selecting ``Tools -> Create Script -> Init .c Files``. This will generate a directory containing the following files:

::

   ├── headless.c
   ├── headless.h
   ├── talise_config_ad9528.h
   ├── talise_config.c
   ├── talise_config.h
   └── TaliseStream.bin

Profiles
~~~~~~~~

Using the new profile can be achieved by creating a new directory under ``no-OS/adrv9009/profiles`` directory and copying the 3 ``talise_config*`` files to it and selecting it in the build system.

Let's say our profile directory is called ``new_profile``, we may select it for build by making sure the ``PROFILE`` make variable in ``src.mk`` file points to it:

::

   PROFILE = new_profile

Stream binary
~~~~~~~~~~~~~

After obtaining a ``TaliseStream.bin`` file from the TES GUI, this can be converted to a header file via this Linux command.

::

   $ xxd -i TaliseStream.bin > talise_stream_binary.h

Should you want to use this generated file, replace ``no-OS/drivers/rf-transceiver/talise/firmware/talise_stream_binary.h`` with it.

Build
-----

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

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`__.
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

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`__.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`__
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
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

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`__.


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

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`__ to a path without whitespaces like ``C:\MaximSDK``.
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

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`__ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

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

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`__ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`__ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__.
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

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`__.
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

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`__.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`__
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
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

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`__.


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

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`__ to a path without whitespaces like ``C:\MaximSDK``.
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

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`__ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

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

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`__ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`__ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__.
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

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to default location ``/opt/stm32cubeide``. If you'd rather install it at a different location, run ``export STM32CUBEIDE=/path/to/your/stm32cubeide`` in the terminal used for building.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to default location ``/opt/stm32cubemx``. If you'd rather install it at a different location, run ``export STM32CUBEMX=/path/to/your/stm32cubemx`` in the terminal used for building.
-  Install python (if not already present) and make sure python command executes Python3 (not Python2). This can be easily achieved by running the following command ``sudo apt install python-is-python3``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Maxim (Click to expand)</summary>

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0018720A>`__.
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

-  Clone the `Raspberry Pico SDK <https://github.com/raspberrypi/pico-sdk>`__.
-  Set the PICO_SDK_PATH environment variable to the pico-sdk cloned repository path.
-  Install the `J-Link software <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`__
-  Set the JLINK_SERVER_PATH environment variable to the JLinkGDBServerCLExe path (the default path should be /opt/SEGGER/JLink/JLinkGDBServerCLExe).
-  For visual debugging and building, install ``Visual Studio Code``, and the ``Cortex-Debug`` extension.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>ADuCM3029 (Click to expand)</summary>

-  Install the CrossCore Embedded Studio 2.10 (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__)
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
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

   Activate `Windows Developer Mode <https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development#activate-developer-mode>`__.


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

-  Install the `Maxim Micros SDK <https://www.maximintegrated.com/en/design/software-description.html/swpart=SFW0010820A>`__ to a path without whitespaces like ``C:\MaximSDK``.
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

-  Install the CrossCore Embedded Studio (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide <resources/eval/user-guides/eval-adicup3029/tools/cces_setup_guide>`__) to a path without whitespaces such as ``C:\ADI\cces2.11.1``.
-  Manually Install ``ADuCM302x Device Family Pack (DFP3.2.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Manually Install ``ARM.CMSIS pack (5.7.0+)`` (refer to `resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces <resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_install_or_upgrade_packs_for_cces>`__)
-  Make sure you don't have multiple versions of ADuCM302x DFP and ARM CMSIS packs installed.
-  Set the CCES_HOME environment variable to point to the CrossCore Embedded Studio installation directory: ``export CCES_HOME=/c/ADI/cces2.11.1``.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__ (latest version) to your desired location like ``C:\stm32cubeide``.
-  Install `stm32cubemx <https://www.st.com/en/development-tools/stm32cubemx.html>`__ version 6.5.0 to your desired location like ``C:\stm32cubemx``.
-  Install `python <https://www.python.org/downloads/>`__ and make sure it's available in Git Bash by adding it to the Windows Path, if needed.

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

For more information you can access the links: `USB_devices_to_WSL <https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/>`__ , `USB/IP_client_tools <https://github.com/dorssel/usbipd-win/wiki/WSL-support#usbip-client-tools>`__ ++++

++++ Running in Windows with PowerShell \|

.. important::

   This guide is to run built no-OS projects "as native as possible" under Windows.




.. raw:: html

   <details><summary>STM32 (Click to expand)</summary>

-  Install `stm32cubeide <https://www.st.com/en/development-tools/stm32cubeide.html>`__.
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


Build Switches
~~~~~~~~~~~~~~

The project builds by default for ADRV9009-W/PCBZ with whatever carrier is specified in the hardware files (.hdf or .sopcinfo/.sof).

:adi:`AD-FMCOMMS8-EBZ` support on `ZCU102 <https://www.xilinx.com/ZCU102>`__ may be enabled by adding ``-DFMCOMMS8_ZCU102`` compiler flag or uncommenting the define in ``src/app/app_config.h``.

:adi:`ADRV9009-ZU11EG` support on :adi:`ADRV2CRR-FMC` may be enabled by adding ``-DZU11EG`` compiler flag or uncommenting the define in ``src/app/app_config.h``.

Legacy build instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

We strongly recommend you use the command line build instructions above but if you would like to perform a manual and graphical project configuration, you may follow the following legacy build guides for :doc:`Intel platforms </wiki-migration/resources/fpga/altera/software_setup>` or :doc:`Xilinx platforms </wiki-migration/resources/fpga/xilinx/software_setup>`.

Demo Applications
-----------------

Make sure to connect your adrv9002 evaluation board to the correct FMC connector or the carrier you use:

-  :doc:`ADRV9009-W on ZCU102 </wiki-migration/resources/eval/user-guides/adrv9009/quickstart/zynqmp>`
-  :doc:`ADRV9009-W on ZC706 </wiki-migration/resources/eval/user-guides/adrv9009/quickstart/zc706>`
-  :doc:`ADRV9009ZU11EG on ADRV2CRRFMC </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`
-  :doc:`FMCOMMS8 on ZCU102 </wiki-migration/resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`

DMA_EXAMPLE demo
----------------

DMA_EXAMPLE is a standard example that sends a sinewave on Tx channels using DMA from a lookup table. If you physically loopback a Tx channel to an Rx channel via an electrical wire, you may run the DMA_EXAMPLE and read the received data at Rx from particular memory address.

To build the DMA_EXAMPLE demo, edit the Makefile and add **-DDMA_EXAMPLE** to CFLAGS and rebuild. Alternatively, you may simply add a **#define DMA_EXAMPLE** in a suitable place in code and rebuild.

To run the DMA_EXAMPLE, you simply need to run the application as usual by:

-   making sure it was built with the **DMA_EXAMPLE** flag, as already mentioned
-   monitoring the serial terminal for messages printed by the application

The application will eventually print something like this:

::

   DMA_EXAMPLE: address=0x7f170 samples=65536 channels=4 bits=16

This means that the memory address where the data at Rx is stored is 0x7f170, there are in total 65536 samples, 16-bit wide across 4 channels, which is equivalent to 16384, 16-bit samples per channel.

At this point you may use a Tcl script to retrieve data from memory and store it into .csv files for processing. In the terminal where you built the project, run the following command while being in the no-OS/projects\ */project_name* folder

::

   for Zynq-7000:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl ZYNQ_PS7 0x7f170 65536 4 16

   for ZynqMP:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl ZYNQ_PSU 0x7f170 65536 4 16

   for Versal:
   xsct ../../tools/scripts/platform/xilinx/capture.tcl VERSAL 0x7f170 65536 4 16

After running the xsct command, some .csv files will be created in your directory. Now you need to run the Python script for plotting, specifying the number of channels you want to plot, like this:

::

   python3 ../../tools/scripts/platform/xilinx/plot.py 4

and a plot window will open showing the Rx channels.


IIOD demo
=========

IIOD demo is a standard example, provided in most no-OS projects, that launches a IIOD server on the board so that the user may connect to it via an IIO client. Using **iio-oscilloscope**, the user can configure the DAC and view the ADC data on a plot.

To build the IIOD demo, add the following flag when invoking make which will build the IIOD server and the IIO section of the driver.

::

   make IIOD=y

To run the IIOD demo, first connect to the board via UART to see the runtime output messages with the following settings:

::

   Baud Rate: 115200bps
   Data: 8 bit
   Parity: None
   Stop bits: 1 bit
   Flow Control: none

Please note that for proper message display, you may need to convert all LF characters to CRLF, if your serial terminal supports it.

With a serial terminal correctly configured and listening to incoming messages, launch the application (``make run`` or click the debug button in your SDK). Runtime messages specific to the application will apear on your serial terminal screen, and eventually the following message is printed:

::

   Running IIOD server...
   If successful, you may connect an IIO client application by:
   1. Disconnecting the serial terminal you use to view this message.
   2. Connecting the IIO client application using the serial backend configured as shown:
       Baudrate: 921600
       Data size: 8 bits
       Parity: none
       Stop bits: 1
       Flow control: none

This message implies a IIOD server is being run and you may connect to it using a serial-backend enabled `iio-oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope>`__ and with the settings indicated at the serial terminal.

