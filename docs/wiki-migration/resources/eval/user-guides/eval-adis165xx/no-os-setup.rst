Evaluating the ADIS165XX Family
===============================

Supported Evaluation Boards
---------------------------

-  :adi:`EVAL-ADIS16500`
-  :adi:`EVAL-ADIS16505`
-  :adi:`EVAL-ADIS16507`
-  :adi:`EVAL-ADIS16575` - TBD: check after it is released
-  :adi:`EVAL-ADIS16576` - TBD: check after it is released
-  :adi:`EVAL-ADIS16577` - TBD: check after it is released

EVAL-ADIS1650X Overview
-----------------------



.. raw:: html

   <details><summary>Click to expand</summary>

The ADIS1650x-x/PCBZ breakout boards device series provide a convenient method for establishing a prototype connection between each ADIS1650X-XBMLZ IMU model and an embedded processor platform. |image1| |image2|


|image3|

.. raw:: html

   </details>


EVAL-ADIS1657X Overview
-----------------------



.. raw:: html

   <details><summary>Click to expand</summary>

- TBD: do after it is released

.. raw:: html

   </details>


Hardware Specifications
-----------------------

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIS165XX eval devices have to be supplied with 3.3V voltage on VDD pin.

Digital Interface
~~~~~~~~~~~~~~~~~

Pin Description
^^^^^^^^^^^^^^^

Please see the following table for the pin assignments for the interface connector (J1).

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

=== ==== =====================================================
PIN NAME DESCRIPTION
=== ==== =====================================================
1   ~RST Reset, Active Low
2   SCLK Serial Clock (Serial Peripheral Interface)
3   ~CS  Chip Select (Serial Peripheral Interface), Active Low
4   DOUT Data Output (Serial Peripheral Interface)
5   DNC  Do not connect
6   DIN  Data Input (Serial Peripheral Interface)
7   GND  Ground
8   GND  Ground
9   GND  Ground
10  VDD  Power Supply, +3.3V
11  VDD  Power Supply, +3.3V
12  VDD  Power Supply, +3.3V
13  DR   Data Ready
14  SYNC Sync Input
15  DNC  Do not connect
16  DNC  Do not connect
=== ==== =====================================================

.. raw:: html

   </details>


ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

- TBD: do after it is released

.. raw:: html

   </details>


Cabling
^^^^^^^

J1 supports connection with the following style of cables: 2.00 mm IDC Ribbon Cable Assembly.

TIP: Use "2.00 mm IDC Ribbon Cable Assembly" as search criteria to find the latest options on the market.

At the time of initial release for these breakout boards, we were most familiar with the `TCSD Series from Samtec <https://www.samtec.com/products/tcsd>`__.

ADI No-OS
---------

The goal of ADI Microcontroller No-OS is to be able to provide reference projects for lower end processors, which can't run Linux, or aren't running a specific operating system, to help those customers using microcontrollers with ADI parts. ADI No-OS offers **generic drivers** which can be used as a base for any microcontroller platform and also **example projects** which are using these drivers on various microcontroller platforms.

For more information about ADI No-OS and supported microcontroller platforms see: :doc:`no-OS </wiki-migration/resources/no-os>`

ADIS Driver
-----------

Information about the ADIS165XX Family driver can be found here: :doc:`ADIS165XX Family Driver </wiki-migration/resources/tools-software/uc-drivers/adis165xx>`

No-OS Supported Platforms
-------------------------

STM32 Platform
~~~~~~~~~~~~~~

Hardware Setup
^^^^^^^^^^^^^^

Required Hardware
"""""""""""""""""

.. _adis1650x-1:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507`
-  :adi:`SDP-K1`
-  ST debugger

.. raw:: html

   </details>


.. _adis1657x-1:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` - TBD: check after it is released
-  :adi:`SDP-K1`
-  ST debugger

.. raw:: html

   </details>


Required Connections
""""""""""""""""""""

The :adi:`SDP-K1`, does not have an interface compatible with the ADIS interface connector J1, but you may use Dupont male-female cables to make the required connections.

.. _adis1650x-2:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` and :adi:`SDP-K1` is realized in this project example.

========================= ================= =================== ========
EVAL-ADIS1650X Pin Number SDP-K1 Pin Number Function            Mnemonic
========================= ================= =================== ========
Pin 3                     DIGITAL 10        Chip Select         CS
Pin 6                     DIGITAL 11        Master Out Slave In MOSI
Pin 4                     DIGITAL 12        Master In Slave Out MISO
Pin 2                     DIGITAL 13        Serial Clock        SCLK
Pin 7                     DIGITAL GND       Digital Ground      DGND
Pin 10                    POWER 3.3V        Digital Power       VDD
Pin 13                    ANALOG IN A0      Data Ready          DRDY
Pin 1                     ANALOG IN A1      Reset               RST
========================= ================= =================== ========

Make sure that the VIO_ADJUST is set to 3.3V on :adi:`SDP-K1`.

The following image shows the connection between :adi:`SDP-K1` and :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the table above.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/sdpk1_adis16505.jpg
   :align: center

.. raw:: html

   </details>


.. _adis1657x-2:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` and :adi:`SDP-K1` is realized in this project example.

========================= ================= =================== ========
EVAL-ADIS1657x Pin Number SDP-K1 Pin Number Function            Mnemonic
========================= ================= =================== ========
Pin 3                     DIGITAL 10        Chip Select         CS
Pin 6                     DIGITAL 11        Master Out Slave In MOSI
Pin 4                     DIGITAL 12        Master In Slave Out MISO
Pin 2                     DIGITAL 13        Serial Clock        SCLK
Pin 7                     DIGITAL GND       Digital Ground      DGND
Pin 10                    POWER 3.3V        Digital Power       VDD
Pin 13                    ANALOG IN A0      Data Ready          DRDY
Pin 1                     ANALOG IN A1      Reset               RST
========================= ================= =================== ========

Make sure that the VIO_ADJUST is set to 3.3V on :adi:`SDP-K1`.

The following image shows the connection between :adi:`SDP-K1` and :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the table above.

TBD

.. raw:: html

   </details>


Maxim Platform
~~~~~~~~~~~~~~

.. _hardware-setup-1:

Hardware Setup
^^^^^^^^^^^^^^

.. _required-hardware-1:

Required Hardware
"""""""""""""""""

.. _adis1650x-3:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507`
-  :adi:`max78000`

.. raw:: html

   </details>


.. _adis1657x-3:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577`
-  :adi:`max78000`

.. raw:: html

   </details>


.. _required-connections-1:

Required Connections
""""""""""""""""""""

The :adi:`max78000`, does not have an interface compatible with the ADIS interface connector J1, but you may use Dupont male-female cables to make the required connections.

.. _adis1650x-4:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` and :adi:`max78000` is realized in this project example.

+---------------------------+---------------------+---------------------+----------+
| EVAL-ADIS1650X Pin Number | MAX78000 Pin Number | Function            | Mnemonic |
+===========================+=====================+=====================+==========+
| Pin 3                     | P0_11               | Chip Select         | CS       |
+---------------------------+---------------------+---------------------+----------+
| Pin 6                     | P0_5                | Master Out Slave In | MOSI     |
+---------------------------+---------------------+---------------------+----------+
| Pin 4                     | P0_6                | Master In Slave Out | MISO     |
+---------------------------+---------------------+---------------------+----------+
| Pin 2                     | P0_7                | Serial Clock        | SCLK     |
+---------------------------+---------------------+---------------------+----------+
| Pin 7                     | GND                 | Digital Ground      | DGND     |
+---------------------------+---------------------+---------------------+----------+
| Pin 10                    | 3V3                 | Digital Power       | VDD      |
+---------------------------+---------------------+---------------------+----------+
| Pin 13                    | P1_6                | Data Ready          | DRDY     |
+---------------------------+---------------------+---------------------+----------+
| Pin 1                     | P0_19               | Reset               | RST      |
+---------------------------+---------------------+---------------------+----------+

The following image shows the connection between :adi:`max78000` and :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the table above.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/max78000_adis16505.jpg
   :align: center

.. raw:: html

   </details>


.. _adis1657x-4:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` and :adi:`max78000` is realized in this project example.

+---------------------------+---------------------+---------------------+----------+
| EVAL-ADIS1657X Pin Number | MAX78000 Pin Number | Function            | Mnemonic |
+===========================+=====================+=====================+==========+
| Pin 3                     | P0_11               | Chip Select         | CS       |
+---------------------------+---------------------+---------------------+----------+
| Pin 6                     | P0_5                | Master Out Slave In | MOSI     |
+---------------------------+---------------------+---------------------+----------+
| Pin 4                     | P0_6                | Master In Slave Out | MISO     |
+---------------------------+---------------------+---------------------+----------+
| Pin 2                     | P0_7                | Serial Clock        | SCLK     |
+---------------------------+---------------------+---------------------+----------+
| Pin 7                     | GND                 | Digital Ground      | DGND     |
+---------------------------+---------------------+---------------------+----------+
| Pin 10                    | 3V3                 | Digital Power       | VDD      |
+---------------------------+---------------------+---------------------+----------+
| Pin 13                    | P1_6                | Data Ready          | DRDY     |
+---------------------------+---------------------+---------------------+----------+
| Pin 1                     | P0_19               | Reset               | RST      |
+---------------------------+---------------------+---------------------+----------+

The following image shows the connection between :adi:`max78000` and :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the table above.

TBD

.. raw:: html

   </details>


Pico Platform
~~~~~~~~~~~~~

.. _hardware-setup-2:

Hardware Setup
^^^^^^^^^^^^^^

.. _required-hardware-2:

Required Hardware
"""""""""""""""""

.. _adis1650x-5:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507`
-  Raspberry Pi Pico
-  :adi:`ADALM-UARTJTAG` Adapter for Raspberry Pi Pico UART to USB Connection

.. raw:: html

   </details>


.. _adis1657x-5:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

-  :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` - TBD: check after it is released
-  Raspberry Pi Pico
-  :adi:`ADALM-UARTJTAG` Adapter for Raspberry Pi Pico UART to USB Connection

.. raw:: html

   </details>


.. _required-connections-2:

Required Connections
""""""""""""""""""""

The Raspberry Pi Pico, does not have an interface compatible with the ADIS interface connector J1, but you may use Dupont male-female cables to make the required connections.

.. _adis1650x-6:

ADIS1650X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` and Raspberry Pi Pico is realized in this project example.

+---------------------------+------------------------------+---------------------+----------+
| EVAL-ADIS1650X Pin Number | Raspberry Pi Pico Pin Number | Function            | Mnemonic |
+===========================+==============================+=====================+==========+
| Pin 3                     | GP17                         | Chip Select         | CS       |
+---------------------------+------------------------------+---------------------+----------+
| Pin 6                     | GP19                         | Master Out Slave In | MOSI     |
+---------------------------+------------------------------+---------------------+----------+
| Pin 4                     | GP16                         | Master In Slave Out | MISO     |
+---------------------------+------------------------------+---------------------+----------+
| Pin 2                     | GP18                         | Serial Clock        | SCLK     |
+---------------------------+------------------------------+---------------------+----------+
| Pin 7                     | GND                          | Digital Ground      | DGND     |
+---------------------------+------------------------------+---------------------+----------+
| Pin 10                    | 3V3                          | Digital Power       | VDD      |
+---------------------------+------------------------------+---------------------+----------+
| Pin 13                    | GP21                         | Data Ready          | DRDY     |
+---------------------------+------------------------------+---------------------+----------+
| Pin 1                     | GP20                         | Reset               | RST      |
+---------------------------+------------------------------+---------------------+----------+

The following table shows how the connection between :adi:`ADALM-UARTJTAG` and Raspberry Pi Pico is realized in this project example.

========================= ============================ ============
ADALM-UARTJTAG Pin Number Raspberry Pi Pico Pin Number Function
========================= ============================ ============
VIO                       VBUS                         Bus Voltage
GND                       GND                          Ground
TX                        GP1(Pico RX)                 Pico UART RX
RX                        GP0(Pico TX)                 Pico UART TX
========================= ============================ ============

The following image shows the connection between Raspberry Pi Pico and :adi:`EVAL-ADIS16500` \| :adi:`EVAL-ADIS16505` \| :adi:`EVAL-ADIS16507` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the table above.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/pico_adis16505.jpg
   :align: center

.. raw:: html

   </details>


.. _adis1657x-6:

ADIS1657X
"""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

The following table shows how the connection between :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` and :adi:`max78000` is realized in this project example.

+---------------------------+---------------------+---------------------+----------+
| EVAL-ADIS1657X Pin Number | MAX78000 Pin Number | Function            | Mnemonic |
+===========================+=====================+=====================+==========+
| Pin 3                     | P0_11               | Chip Select         | CS       |
+---------------------------+---------------------+---------------------+----------+
| Pin 6                     | P0_5                | Master Out Slave In | MOSI     |
+---------------------------+---------------------+---------------------+----------+
| Pin 4                     | P0_6                | Master In Slave Out | MISO     |
+---------------------------+---------------------+---------------------+----------+
| Pin 2                     | P0_7                | Serial Clock        | SCLK     |
+---------------------------+---------------------+---------------------+----------+
| Pin 7                     | GND                 | Digital Ground      | DGND     |
+---------------------------+---------------------+---------------------+----------+
| Pin 10                    | 3V3                 | Digital Power       | VDD      |
+---------------------------+---------------------+---------------------+----------+
| Pin 13                    | P1_6                | Data Ready          | DRDY     |
+---------------------------+---------------------+---------------------+----------+
| Pin 1                     | P0_19               | Reset               | RST      |
+---------------------------+---------------------+---------------------+----------+

The following image shows the connection between :adi:`max78000` and :adi:`EVAL-ADIS16575` \| :adi:`EVAL-ADIS16576` \| :adi:`EVAL-ADIS16577` using a modified 2.00 mm IDC Ribbon Cable Assembly with Dupont cables. The connection is realized as described in the tables above.

TBD

.. raw:: html

   </details>


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


No-OS Build Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~

Please follow the steps below for No-OS Setup based on the environment you are using. Make sure you use the information for the specific platform you are using (e.g. STM32, MAXIM).

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



No-OS Build Project
~~~~~~~~~~~~~~~~~~~

ADIS1650X Project Path 

.. raw:: html

   <details><summary>Click to expand</summary>

The path of the project is no-OS/projects/eval-adis1650x/

.. raw:: html

   </details>


| 
| ADIS1657X Project Path 

.. raw:: html

   <details><summary>Click to expand</summary>

The path of the project is no-OS/projects/eval-adis1657x/

.. raw:: html

   </details>


| 
| Go in the project directory that should be built.



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


Example Project Execution
-------------------------

Dummy Project ADIS1650X
~~~~~~~~~~~~~~~~~~~~~~~

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the dummy project make sure you have the following configuration in the no-OS/projects/eval-adis1650x/Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   DUMMY_EXAMPLE = y
   IIO_TRIGGER_EXAMPLE = n

When running make command make sure to specify the platform you want to build the project for.

Project Description
^^^^^^^^^^^^^^^^^^^

The initialization data is taken from no-OS/projects/eval-adis1650x/src/common/common_data.c and no-OS/projects/eval-adis1650x/src/common/common_data.h files:

.. code:: C

   struct no_os_uart_init_param adis1650x_uart_ip = {
       .device_id = UART_DEVICE_ID,
       .irq_id = UART_IRQ_ID,
       .asynchronous_rx = true,
       .baud_rate = UART_BAUDRATE,
       .size = NO_OS_UART_CS_8,
       .parity = NO_OS_UART_PAR_NO,
       .stop = NO_OS_UART_STOP_1_BIT,
       .extra = UART_EXTRA,
       .platform_ops = UART_OPS,
   };

   struct no_os_spi_init_param adis1650x_spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_BAUDRATE,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_3,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
       .extra = SPI_EXTRA,
   };

   struct no_os_gpio_init_param adis1650x_gpio_reset_ip = {
       .port = GPIO_RESET_PORT_NUM,
       .number = GPIO_RESET_PIN_NUM,
       .pull = NO_OS_PULL_NONE,
       .platform_ops = GPIO_OPS,
       .extra = GPIO_EXTRA
   };

   struct adis_init_param adis1650x_ip = {
       .gpio_reset = &adis1650x_gpio_reset_ip,
       .sync_mode = ADIS_SYNC_OUTPUT,
       .dev_id = ADIS16505_2,
   };

The macros used in common_data are defined in platform specific files found in no-OS/projects/eval-adis1650x/src/platform/.

.. _stm32-platform-1:

STM32 platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For STM32 platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/stm32/parameters.h and no-OS/projects/eval-adis1650x/src/platform/stm32/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  5
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &stm32_uart_ops
   #define UART_IRQ_ID     UART5_IRQn

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct stm32_uart_init_param adis1650x_uart_extra_ip = {
       .huart = &huart5,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_BAUDRATE    1000000
   #define SPI_CS          15
   #define SPI_CS_PORT     0
   #define SPI_OPS         &stm32_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct stm32_spi_init_param adis1650x_spi_extra_ip  = {
       .chip_select_port = SPI_CS_PORT,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   4
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS            &stm32_gpio_ops
   #define GPIO_EXTRA          &adis1650x_gpio_reset_extra_ip

Where adis1650x_gpio_reset_extra_ip is:

.. code:: C

   struct stm32_gpio_init_param adis1650x_gpio_reset_extra_ip = {
       .mode = GPIO_MODE_OUTPUT_OD,
       .speed = GPIO_SPEED_FREQ_VERY_HIGH,
   };

.. raw:: html

   </details>


.. _maxim-platform-1:

Maxim Platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Maxim platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/maxim/parameters.h and no-OS/projects/eval-adis1650x/src/platform/maxim/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   57600
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &max_uart_ops
   #define UART_IRQ_ID     UART0_IRQn

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct max_uart_init_param adis1650x_uart_extra_ip = {
       .flow = UART_FLOW_DIS
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_CS          1
   #define SPI_BAUDRATE    1000000
   #define SPI_OPS         &max_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct max_spi_init_param adis1650x_spi_extra_ip  = {
       .num_slaves = 1,
       .polarity = SPI_SS_POL_LOW,
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   19
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &max_gpio_ops
   #define GPIO_EXTRA           &adis1650x_gpio_extra_ip

Where adis1650x_gpio_reset_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis1650x_gpio_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

.. raw:: html

   </details>


.. _pico-platform-1:

Pico platform
"""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Pico platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/pico/parameters.h and no-OS/projects/eval-adis1650x/src/platform/pico/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &pico_uart_ops
   #define UART_IRQ_ID     20

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct pico_uart_init_param adis1650x_uart_extra_ip = {
       .uart_tx_pin = UART_TX_PIN,
       .uart_rx_pin = UART_RX_PIN,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   0
   #define SPI_BAUDRATE    1000000
   #define SPI_CS          SPI0_CS_GP17
   #define SPI_OPS         &pico_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct pico_spi_init_param adis1650x_spi_extra_ip  = {
       .spi_tx_pin = SPI0_TX_GP19,
       .spi_rx_pin = SPI0_RX_GP16,
       .spi_sck_pin = SPI0_SCK_GP18,
       .spi_cs_pin = SPI0_CS_GP17
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   20
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &pico_gpio_ops
   #define GPIO_EXTRA           NULL /* Not used for pico platform */

.. raw:: html

   </details>


| 
| The dummy project contains the generic HAL initialization of the used platform, together with the SPI and UART driver configuration and initialization.

The SPI driver is used to communicate with the EVAL-ADIS1650X device, while the UART driver is used to display on the host machine the measured data.

The dummy project contains the ADIS1650X driver initialization:

.. code:: C

   struct adis_dev *adis1650x_desc;
   int ret;
   int val[7];

   adis1650x_chip_info.ip = &adis1650x_ip;

   ret = adis_init(&adis1650x_desc, &adis1650x_chip_info);
   if (ret)
       goto error;

At this point the device is already performing measurements which are accessed continuously in a while loop at each second.

.. code:: C

   while(1) {
       pr_info ("while loop \n");
       no_os_mdelay(1000);
       ret = adis_read_x_gyro(adis1650x_desc, &val[0]);
       if (ret)
           goto error_remove;
       ret = adis_read_y_gyro(adis1650x_desc, &val[1]);
       if (ret)
           goto error_remove;
       ret = adis_read_z_gyro(adis1650x_desc, &val[2]);
       if (ret)
           goto error_remove;
       ret = adis_read_x_accl(adis1650x_desc, &val[3]);
       if (ret)
           goto error_remove;
       ret = adis_read_y_accl(adis1650x_desc, &val[4]);
       if (ret)
           goto error_remove;
       ret = adis_read_z_accl(adis1650x_desc, &val[5]);
       if (ret)
           goto error_remove;
       ret = adis_read_temp_out(adis1650x_desc, &val[6]);
       if (ret)
           goto error_remove;

       for (uint8_t i = 0; i < 7; i++)
           pr_info("%s %.5f %s \n", output_data[i], val[i]* output_scale[i],
               output_unit[i]);
   }
   error_remove:
       adis_remove(adis1650x_desc);
   error:
       pr_info("Error!\n");
       return 0;

Some global variables are used to be able to print the converted data:

.. code:: C

   static const char * const output_data[] = {
       "angular velocity x axis: ",
       "angular velocity y axis: ",
       "angular velocity z axis: ",
       "acceleration x axis    : ",
       "acceleration y axis    : ",
       "acceleration z axis    : ",
       "temperature            : "
   };

   static const char * const output_unit[] = {
       "rad/s",
       "rad/s",
       "rad/s",
       "m/s^2",
       "m/s^2",
       "m/s^2",
       "°C"
   };

   static const float output_scale[] = {
       1.0/RAD_TO_DEGREE(40 << 16),
       1.0/RAD_TO_DEGREE(40 << 16),
       1.0/RAD_TO_DEGREE(40 << 16),
       78.0/ (32000 << 16),
       78.0/ (32000 << 16),
       78.0/ (32000 << 16),
       1.0/10,
   };

Project Execution
^^^^^^^^^^^^^^^^^

The following UART Output while moving the device:

.. code:: C

   while loop 
   angular velocity x axis:  0.07515 rad/s 
   angular velocity y axis:  0.73120 rad/s 
   angular velocity z axis:  -0.03398 rad/s 
   acceleration x axis    :  -0.61707 m/s^2 
   acceleration y axis    :  0.02541 m/s^2 
   acceleration z axis    :  9.50173 m/s^2 
   temperature            :  29.60000 °C 
   while loop 
   angular velocity x axis:  -0.85897 rad/s 
   angular velocity y axis:  0.32987 rad/s 
   angular velocity z axis:  0.72238 rad/s 
   acceleration x axis    :  -0.85728 m/s^2 
   acceleration y axis    :  4.29819 m/s^2 
   acceleration z axis    :  7.65091 m/s^2 
   temperature            :  29.80000 °C 
   while loop 
   angular velocity x axis:  0.28803 rad/s 
   angular velocity y axis:  -0.97466 rad/s 
   angular velocity z axis:  1.03481 rad/s 
   acceleration x axis    :  5.47902 m/s^2 
   acceleration y axis    :  -3.66836 m/s^2 
   acceleration z axis    :  -0.95155 m/s^2 
   temperature            :  29.90000 °C 
   while loop 
   angular velocity x axis:  0.99855 rad/s 
   angular velocity y axis:  0.01308 rad/s 
   angular velocity z axis:  -0.06914 rad/s 
   acceleration x axis    :  2.43305 m/s^2 
   acceleration y axis    :  1.43012 m/s^2 
   acceleration z axis    :  8.98201 m/s^2 
   temperature            :  29.50000 °C 
   while loop 
   angular velocity x axis:  -0.26499 rad/s 
   angular velocity y axis:  7.31366 rad/s 
   angular velocity z axis:  -1.81494 rad/s 
   acceleration x axis    :  -0.38381 m/s^2 
   acceleration y axis    :  2.33110 m/s^2 
   acceleration z axis    :  13.35730 m/s^2 
   temperature            :  29.70000 °C 
   while loop 
   angular velocity x axis:  -0.75055 rad/s 
   angular velocity y axis:  -1.19145 rad/s 
   angular velocity z axis:  0.45498 rad/s 
   acceleration x axis    :  -2.47404 m/s^2 
   acceleration y axis    :  4.74150 m/s^2 
   acceleration z axis    :  5.27509 m/s^2 
   temperature            :  29.30000 °C 

Dummy Project ADIS1657X
~~~~~~~~~~~~~~~~~~~~~~~

.. _makefile-selection-1:

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the dummy project make sure you have the following configuration in the no-OS/projects/eval-adis1657x/Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   DUMMY_EXAMPLE = y
   IIO_TRIGGER_EXAMPLE = n

When running make command make sure to specify the platform you want to build the project for.

.. _project-description-1:

Project Description
^^^^^^^^^^^^^^^^^^^

The initialization data is taken from no-OS/projects/eval-adis1657x/src/common/common_data.c and no-OS/projects/eval-adis1657x/src/common/common_data.h files:

.. code:: C

   struct no_os_uart_init_param adis1657x_uart_ip = {
       .device_id = UART_DEVICE_ID,
       .irq_id = UART_IRQ_ID,
       .asynchronous_rx = true,
       .baud_rate = UART_BAUDRATE,
       .size = NO_OS_UART_CS_8,
       .parity = NO_OS_UART_PAR_NO,
       .stop = NO_OS_UART_STOP_1_BIT,
       .extra = UART_EXTRA,
       .platform_ops = UART_OPS,
   };

   struct no_os_spi_init_param adis1657x_spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_BAUDRATE,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_3,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
       .extra = SPI_EXTRA,
   };

   struct no_os_gpio_init_param adis1657x_gpio_reset_ip = {
       .port = GPIO_RESET_PORT_NUM,
       .number = GPIO_RESET_PIN_NUM,
       .pull = NO_OS_PULL_NONE,
       .platform_ops = GPIO_OPS,
       .extra = GPIO_EXTRA
   };

   struct adis_init_param adis1657x_ip = {
       .gpio_reset = &adis1657x_gpio_reset_ip,
       .sync_mode = ADIS_SYNC_OUTPUT,
       .dev_id = ADIS16577_3,
   };

The macros used in common_data are defined in platform specific files found in no-OS/projects/eval-adis1657x/src/platform/.

.. _stm32-platform-2:

STM32 platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For STM32 platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/stm32/parameters.h and no-OS/projects/eval-adis1657x/src/platform/stm32/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  5
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &stm32_uart_ops
   #define UART_IRQ_ID     UART5_IRQn

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct stm32_uart_init_param adis1657x_uart_extra_ip = {
       .huart = &huart5,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_BAUDRATE    8000000
   #define SPI_CS          15
   #define SPI_CS_PORT     0
   #define SPI_OPS         &stm32_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct stm32_spi_init_param adis1657x_spi_extra_ip  = {
       .chip_select_port = SPI_CS_PORT,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   4
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS            &stm32_gpio_ops
   #define GPIO_EXTRA          &adis1657x_gpio_reset_extra_ip

Where adis1657x_gpio_reset_extra_ip is:

.. code:: C

   struct stm32_gpio_init_param adis1657x_gpio_reset_extra_ip = {
       .mode = GPIO_MODE_OUTPUT_OD,
       .speed = GPIO_SPEED_FREQ_VERY_HIGH,
   };

.. raw:: html

   </details>


.. _maxim-platform-2:

Maxim Platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Maxim platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/maxim/parameters.h and no-OS/projects/eval-adis1657x/src/platform/maxim/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   57600
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &max_uart_ops
   #define UART_IRQ_ID     UART0_IRQn

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct max_uart_init_param adis1657x_uart_extra_ip = {
       .flow = UART_FLOW_DIS
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_CS          1
   #define SPI_BAUDRATE    8000000
   #define SPI_OPS         &max_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct max_spi_init_param adis1657x_spi_extra_ip  = {
       .num_slaves = 1,
       .polarity = SPI_SS_POL_LOW,
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   19
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &max_gpio_ops
   #define GPIO_EXTRA           &adis1657x_gpio_extra_ip

Where adis1657x_gpio_reset_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis1657x_gpio_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

.. raw:: html

   </details>


.. _pico-platform-2:

Pico platform
"""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Pico platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/pico/parameters.h and no-OS/projects/eval-adis1657x/src/platform/pico/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &pico_uart_ops
   #define UART_IRQ_ID     20

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct pico_uart_init_param adis1657x_uart_extra_ip = {
       .uart_tx_pin = UART_TX_PIN,
       .uart_rx_pin = UART_RX_PIN,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   0
   #define SPI_BAUDRATE    8000000
   #define SPI_CS          SPI0_CS_GP17
   #define SPI_OPS         &pico_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct pico_spi_init_param adis1657x_spi_extra_ip  = {
       .spi_tx_pin = SPI0_TX_GP19,
       .spi_rx_pin = SPI0_RX_GP16,
       .spi_sck_pin = SPI0_SCK_GP18,
       .spi_cs_pin = SPI0_CS_GP17
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   20
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &pico_gpio_ops
   #define GPIO_EXTRA           NULL /* Not used for pico platform */

.. raw:: html

   </details>


| 
| The dummy project contains the generic HAL initialization of the used platform, together with the SPI and UART driver configuration and initialization.

The SPI driver is used to communicate with the EVAL-ADIS1657X device, while the UART driver is used to display on the host machine the measured data.

The dummy project contains the ADIS1657X driver initialization:

.. code:: C

   struct adis_dev *adis1657x_desc;
   int ret;
   int val[7];

   adis1657x_chip_info.ip = &adis1657x_ip;

   ret = adis_init(&adis1657x_desc, &adis1657x_chip_info);
   if (ret)
       goto error;

At this point the device is already performing measurements which are accessed continuously in a while loop at each second.

.. code:: C

   while(1) {
       pr_info ("while loop \n");
       no_os_mdelay(1000);
       ret = adis_read_x_gyro(adis1657x_desc, &val[0]);
       if (ret)
           goto error_remove;
       ret = adis_read_y_gyro(adis1657x_desc, &val[1]);
       if (ret)
           goto error_remove;
       ret = adis_read_z_gyro(adis1657x_desc, &val[2]);
       if (ret)
           goto error_remove;
       ret = adis_read_x_accl(adis1657x_desc, &val[3]);
       if (ret)
           goto error_remove;
       ret = adis_read_y_accl(adis1657x_desc, &val[4]);
       if (ret)
           goto error_remove;
       ret = adis_read_z_accl(adis1657x_desc, &val[5]);
       if (ret)
           goto error_remove;
       ret = adis_read_temp_out(adis1657x_desc, &val[6]);
       if (ret)
           goto error_remove;

       for (uint8_t i = 0; i < 7; i++)
           pr_info("%s %.5f %s \n", output_data[i], val[i]* output_scale[i],
               output_unit[i]);
   }
   error_remove:
       adis_remove(adis1657x_desc);
   error:
       pr_info("Error!\n");
       return 0;

Some global variables are used to be able to print the converted data:

.. code:: C

   static const char * const output_data[] = {
       "angular velocity x axis: ",
       "angular velocity y axis: ",
       "angular velocity z axis: ",
       "acceleration x axis    : ",
       "acceleration y axis    : ",
       "acceleration z axis    : ",
       "temperature            : "
   };

   static const char * const output_unit[] = {
       "rad/s",
       "rad/s",
       "rad/s",
       "m/s^2",
       "m/s^2",
       "m/s^2",
       "°C"
   };

   static const float output_scale[] = {
       1.0/RAD_TO_DEGREE(10 << 16),
       1.0/RAD_TO_DEGREE(10 << 16),
       1.0/RAD_TO_DEGREE(10 << 16),
       1.0/ 5346250,
       1.0/ 5346250,
       1.0/ 5346250,
       1.0/10,
   };

.. _project-execution-1:

Project Execution
^^^^^^^^^^^^^^^^^

The following UART Output while moving the device:

.. code:: C

   while loop 
   angular velocity x axis:  -0.00048 rad/s 
   angular velocity y axis:  0.00084 rad/s 
   angular velocity z axis:  -0.01251 rad/s 
   acceleration x axis    :  -0.04531 m/s^2 
   acceleration y axis    :  -0.00424 m/s^2 
   acceleration z axis    :  9.84555 m/s^2 
   temperature            :  20.20000 °C 
   while loop 
   angular velocity x axis:  0.00861 rad/s 
   angular velocity y axis:  0.00246 rad/s 
   angular velocity z axis:  -0.00015 rad/s 
   acceleration x axis    :  -0.04322 m/s^2 
   acceleration y axis    :  -0.00450 m/s^2 
   acceleration z axis    :  9.75102 m/s^2 
   temperature            :  20.20000 °C 
   while loop 
   angular velocity x axis:  0.02977 rad/s 
   angular velocity y axis:  0.00224 rad/s 
   angular velocity z axis:  0.01734 rad/s 
   acceleration x axis    :  0.02061 m/s^2 
   acceleration y axis    :  -0.06035 m/s^2 
   acceleration z axis    :  9.69272 m/s^2 
   temperature            :  20.20000 °C 
   while loop 
   angular velocity x axis:  -1.61514 rad/s 
   angular velocity y axis:  -5.10347 rad/s 
   angular velocity z axis:  -0.42433 rad/s 
   acceleration x axis    :  10.40941 m/s^2 
   acceleration y axis    :  0.45263 m/s^2 
   acceleration z axis    :  0.03172 m/s^2 
   temperature            :  20.20000 °C 
   while loop 
   angular velocity x axis:  0.00483 rad/s 
   angular velocity y axis:  5.59881 rad/s 
   angular velocity z axis:  0.14357 rad/s 
   acceleration x axis    :  8.94628 m/s^2 
   acceleration y axis    :  0.14112 m/s^2 
   acceleration z axis    :  3.53856 m/s^2 
   temperature            :  20.20000 °C 
   while loop 
   angular velocity x axis:  -0.07343 rad/s 
   angular velocity y axis:  5.84894 rad/s 
   angular velocity z axis:  -0.00271 rad/s 
   acceleration x axis    :  0.90506 m/s^2 
   acceleration y axis    :  -0.02720 m/s^2 
   acceleration z axis    :  9.87480 m/s^2 
   temperature            :  20.20000 °C 

IIO Project ADIS1650X
~~~~~~~~~~~~~~~~~~~~~

.. _makefile-selection-2:

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the IIO project make sure you have the following configuration in the no-OS/projects/eval-adis1650x/Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   DUMMY_EXAMPLE = n
   IIO_TRIGGER_EXAMPLE = y

When running make command make sure to specify the platform you want to build the project for.

.. _project-description-2:

Project Description
^^^^^^^^^^^^^^^^^^^

This project is actually an IIOD demo for EVAL-ADIS1650X device series. The project launches an IIOD server on the board so that the user may connect to it via an IIO client. Using IIO-Oscilloscope, the user can configure the IMU and view the measured data on a plot.

If you are not familiar with ADI IIO Application, please take a look at::doc:`IIO No-OS </wiki-migration/resources/tools-software/no-os-software/iio>`

This IIO Project uses IIO-Oscilloscope as a client. If you are not familiar with ADI IIO-Oscilloscope Client, please take a look at: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The No-OS IIO Application together with the No-OS IIO ADIS driver take care of all the back-end logic needed to setup the IIO server. The user has to initialize the IIO device and call the IIO app as shown below. The read buffer is used for storing data which shall be available on the plot in the IIO Oscilloscope Client.

The measured data is sampled using a hardware trigger (e.g. interrupts). ADIS1650X offers the capability to use DATA_READY pin as a flag which shows when new measurements are available. Thus, DATA_READY pin is used as a hardware trigger. The code maps the DATA_READY pin as GPIO input with interrupt capabilities. When DATA_READY pin transitions from low to high, new data is available and will be read based on is_synchronous flag setting used in adis_iio_trigger_desc. If the flag is set to true, the data will be read immediately, in the interrupt context. If the flag is set to false, the data will be read from application context. In this case some samples might be missed.

The initialization data is taken from no-OS/projects/eval-adis1650x/src/common/common_data.c and no-OS/projects/eval-adis1650x/src/common/common_data.h files:

.. code:: C

   struct no_os_uart_init_param adis1650x_uart_ip = {
       .device_id = UART_DEVICE_ID,
       .irq_id = UART_IRQ_ID,
       .asynchronous_rx = true,
       .baud_rate = UART_BAUDRATE,
       .size = NO_OS_UART_CS_8,
       .parity = NO_OS_UART_PAR_NO,
       .stop = NO_OS_UART_STOP_1_BIT,
       .extra = UART_EXTRA,
       .platform_ops = UART_OPS,
   };

   struct no_os_spi_init_param adis1650x_spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_BAUDRATE,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_3,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
       .extra = SPI_EXTRA,
   };

   struct no_os_gpio_init_param adis1650x_gpio_reset_ip = {
       .port = GPIO_RESET_PORT_NUM,
       .number = GPIO_RESET_PIN_NUM,
       .pull = NO_OS_PULL_NONE,
       .platform_ops = GPIO_OPS,
       .extra = GPIO_EXTRA
   };

   struct adis_init_param adis1650x_ip = {
       .gpio_reset = &adis1650x_gpio_reset_ip,
       .sync_mode = ADIS_SYNC_OUTPUT,
       .dev_id = ADIS16505_2,
   };

   struct no_os_irq_init_param adis1650x_gpio_irq_ip = {
       .irq_ctrl_id = GPIO_IRQ_ID,
       .platform_ops = GPIO_IRQ_OPS,
       .extra = GPIO_IRQ_EXTRA,
   };

   const struct iio_hw_trig_cb_info gpio_cb_info = {
       .event = NO_OS_EVT_GPIO,
       .peripheral = NO_OS_GPIO_IRQ,
       .handle = ADIS1650X_GPIO_CB_HANDLE,
   };

   struct iio_hw_trig_init_param adis1650x_gpio_trig_ip = {
       .irq_id = ADIS1650X_GPIO_TRIG_IRQ_ID,
       .irq_trig_lvl = NO_OS_IRQ_EDGE_RISING,
       .cb_info = gpio_cb_info,
       .name = ADIS1650X_GPIO_TRIG_NAME,
   };

The macros used in common_data are defined in platform specific files found in no-OS/projects/eval-adis1650x/src/platform/.

.. _stm32-platform-3:

STM32 platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For STM32 platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/stm32/parameters.h and no-OS/projects/eval-adis1650x/src/platform/stm32/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  5
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &stm32_uart_ops
   #define UART_IRQ_ID     UART5_IRQn

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct stm32_uart_init_param adis1650x_uart_extra_ip = {
       .huart = &huart5,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_BAUDRATE    1000000
   #define SPI_CS          15
   #define SPI_CS_PORT     0
   #define SPI_OPS         &stm32_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct stm32_spi_init_param adis1650x_spi_extra_ip  = {
       .chip_select_port = SPI_CS_PORT,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   4
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS            &stm32_gpio_ops
   #define GPIO_EXTRA          &adis1650x_gpio_reset_extra_ip

Where adis1650x_gpio_reset_extra_ip is:

.. code:: C

   struct stm32_gpio_init_param adis1650x_gpio_reset_extra_ip = {
       .mode = GPIO_MODE_OUTPUT_OD,
       .speed = GPIO_SPEED_FREQ_VERY_HIGH,
   };

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   2
   #define GPIO_DRDY_PORT_NUM  0

   /* Setting for PortA Pin2 used for DATA_READY.
      Has to be adapted accordingly if another pin is used.
    */
   #define ADIS1650X_GPIO_TRIG_IRQ_ID     0    /* Not used in stm32 platform */
   #define ADIS1650X_GPIO_CB_HANDLE       NULL /* Not used in stm32 platform */

   #define GPIO_IRQ_ID             2 /* Pin 2 */
   #define GPIO_IRQ_OPS            &stm32_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          &adis1650x_gpio_irq_extra_ip

Where adis1650x_gpio_irq_extra_ip is:

.. code:: C

   struct stm32_gpio_irq_init_param adis1650x_gpio_irq_extra_ip = {
       .port_nb = 0, /* Port A */
   };

.. raw:: html

   </details>


.. _maxim-platform-3:

Maxim Platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Maxim platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/maxim/parameters.h and no-OS/projects/eval-adis1650x/src/platform/maxim/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   57600
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &max_uart_ops
   #define UART_IRQ_ID     UART0_IRQn

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct max_uart_init_param adis1650x_uart_extra_ip = {
       .flow = UART_FLOW_DIS
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_CS          1
   #define SPI_BAUDRATE    1000000
   #define SPI_OPS         &max_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct max_spi_init_param adis1650x_spi_extra_ip  = {
       .num_slaves = 1,
       .polarity = SPI_SS_POL_LOW,
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   19
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &max_gpio_ops
   #define GPIO_EXTRA           &adis1650x_gpio_extra_ip

Where adis1650x_gpio_reset_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis1650x_gpio_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   6
   #define GPIO_DRDY_PORT_NUM  1

   #define ADIS1650X_GPIO_TRIG_IRQ_ID    GPIO_DRDY_PIN_NUM
   #define ADIS1650X_GPIO_CB_HANDLE      MXC_GPIO_GET_GPIO(GPIO_DRDY_PORT_NUM)

   #define GPIO_IRQ_ID             GPIO_DRDY_PORT_NUM
   #define GPIO_IRQ_OPS            &max_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          &adis1650x_gpio_drdy_extra_ip

Where adis1650x_gpio_drdy_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis1650x_gpio_drdy_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

.. raw:: html

   </details>


.. _pico-platform-3:

Pico platform
"""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Pico platform the following macros are defined in no-OS/projects/eval-adis1650x/src/platform/pico/parameters.h and no-OS/projects/eval-adis1650x/src/platform/pico/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1650x_uart_extra_ip
   #define UART_OPS        &pico_uart_ops
   #define UART_IRQ_ID     20

Where adis1650x_uart_extra_ip is:

.. code:: C

   struct pico_uart_init_param adis1650x_uart_extra_ip = {
       .uart_tx_pin = UART_TX_PIN,
       .uart_rx_pin = UART_RX_PIN,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   0
   #define SPI_BAUDRATE    1000000
   #define SPI_CS          SPI0_CS_GP17
   #define SPI_OPS         &pico_spi_ops
   #define SPI_EXTRA       &adis1650x_spi_extra_ip

Where adis1650x_spi_extra_ip is:

.. code:: C

   struct pico_spi_init_param adis1650x_spi_extra_ip  = {
       .spi_tx_pin = SPI0_TX_GP19,
       .spi_rx_pin = SPI0_RX_GP16,
       .spi_sck_pin = SPI0_SCK_GP18,
       .spi_cs_pin = SPI0_CS_GP17
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   20
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &pico_gpio_ops
   #define GPIO_EXTRA           NULL /* Not used for pico platform */

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   21
   #define GPIO_DRDY_PORT_NUM  0

   #define ADIS1650X_GPIO_TRIG_IRQ_ID     GPIO_DRDY_PIN_NUM
   #define ADIS1650X_GPIO_CB_HANDLE       NULL /* Not used in pico platform */

   #define GPIO_IRQ_ID             GPIO_DRDY_PIN_NUM
   #define GPIO_IRQ_OPS            &pico_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          NULL /* Not used for pico platform */

.. raw:: html

   </details>


| 
| The following code initializes the IIO ADIS1650X driver, initializes the interrupt controller (needed for IIO trigger to sample the data on DATA_READY rising edge), sets the priority for the DATA_READY interrupt, initializes the IIO hardware trigger, defines the list of IIO devices and the list of IIO triggers and finaly initializes the IIO application and starts it.

.. code:: C

   #define DATA_BUFFER_SIZE 400
   uint8_t iio_data_buffer[DATA_BUFFER_SIZE*14*sizeof(int)];
   struct adis_iio_dev *adis1650x_iio_desc;
    
   struct iio_data_buffer data_buff = {
       .buff = (void *)iio_data_buffer,
       .size = DATA_BUFFER_SIZE*14*sizeof(int)
   };
    
   struct iio_hw_trig *adis1650x_trig_desc;
   struct no_os_irq_ctrl_desc *adis1650x_irq_desc;
   struct iio_app_desc *app;
   struct iio_app_init_param app_init_param = { 0 };
    
   ret = adis1650x_iio_init(&adis1650x_iio_desc, &adis1650x_ip);
   if (ret)
       return ret;
    
   /* Initialize interrupt controller */
   ret = no_os_irq_ctrl_init(&adis1650x_irq_desc, &adis1650x_gpio_irq_ip);
   if (ret)
       goto err_irq_init;
    
   ret = no_os_irq_set_priority(adis1650x_irq_desc, adis1650x_gpio_trig_ip.irq_id, 1);
   if (ret)
       goto err_irq_set_prio;
    
   adis1650x_gpio_trig_ip.irq_ctrl = adis1650x_irq_desc;
    
   /* Initialize hardware trigger */
   ret = iio_hw_trig_init(&adis1650x_trig_desc, &adis1650x_gpio_trig_ip);
   if (ret)
       goto err_irq_set_prio;
    
   /* List of devices */
   struct iio_app_device iio_devices[] = {
       {
           .name = "adis16505-2",
           .dev = adis1650x_iio_desc,
           .dev_descriptor = adis1650x_iio_desc->iio_dev,
           .read_buff = &data_buff,
       }
   };
    
   /* List of triggers */
   struct iio_trigger_init trigs[] = {
       IIO_APP_TRIGGER(ADIS1650X_GPIO_TRIG_NAME, adis1650x_trig_desc, &adis_iio_trig_desc)
   };
    
   app_init_param.devices = iio_devices;
   app_init_param.nb_devices = NO_OS_ARRAY_SIZE(iio_devices);
   app_init_param.uart_init_params = adis1650x_uart_ip;
   app_init_param.trigs = trigs;
   app_init_param.nb_trigs = NO_OS_ARRAY_SIZE(trigs);
   app_init_param.irq_desc = adis1650x_irq_desc;
    
   ret = iio_app_init(&app, app_init_param);
   if (ret)
       goto err_iio_app_init;
    
   /* Update the reference to iio_desc */
   adis1650x_trig_desc->iio_desc = app->iio_desc;
    
   ret = iio_app_run(app);
   if (ret)
       goto iio_app_err;
    
   return 0;
    
   iio_app_err:
       iio_app_remove(app);
   err_iio_app_init:
       iio_hw_trig_remove(adis1650x_trig_desc);
   err_irq_set_prio:
       no_os_irq_ctrl_remove(adis1650x_irq_desc);
   err_irq_init:
       adis1650x_iio_remove(adis1650x_iio_desc);
       pr_info("Error!\n");
       return ret;

.. _project-execution-2:

Project Execution
^^^^^^^^^^^^^^^^^

After flashing and running the application, IIO Oscilloscope can be used to make the desired configuration and obtain the desired data. Below you may find some snippets from IIO Oscilloscope, when running IIO Project.

Bellow you can see the Connection window for IIO Oscilloscope. The handshake is performed and the device is detected over UART. After pressing the Connect button we can see the device in the list, together with its channels and we can see the measured data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis16505_osc_connect.gif
   :align: center

Below you can see the Simple View which contains the read data from the IMU. Observe how the measurements change when the device is moved.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis16505_osc_measurements.gif
   :align: center

Below you can see the Debug View which contains the list of device attributes, channel attributes and debug attributes. In this example, the sampling frequency is set to 1000 Hz, the calibration offset for accelerometer on x axis is set to -10, some other reads are performed and finally a software reset is triggered using the debug attribute command, which resets the values set previously.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis16505_attributes.gif
   :align: center

Below you can see the Plot View for the buffered data. IIO Oscilloscope can be used to capture data using the configured hardware trigger. In order to select the trigger as an impulse generator, right click on the adis16505 device in the plot windows, select Impulse generator and choose adis16505-dev0 trigger. The Plot view shows the raw vales measured by the device. You may observe the spikes in the data due to sudden movement of the device. At the end of the measurement the number of lost samples is read, which in this case was 0, showing that the captured data was continuous.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis16505_capture.gif
   :align: center

IIO Project ADIS1657X
~~~~~~~~~~~~~~~~~~~~~

.. _makefile-selection-3:

Makefile Selection
^^^^^^^^^^^^^^^^^^

In order to build the IIO project make sure you have the following configuration in the no-OS/projects/eval-adis1657x/Makefile:

::

   # Select the example you want to enable by choosing y for enabling and n for disabling
   DUMMY_EXAMPLE = n
   IIO_TRIGGER_EXAMPLE = y

When running make command make sure to specify the platform you want to build the project for.

.. _project-description-3:

Project Description
^^^^^^^^^^^^^^^^^^^

This project is actually an IIOD demo for EVAL-ADIS1657x device. The project launches an IIOD server on the board so that the user may connect to it via an IIO client. Using IIO-Oscilloscope, the user can configure the IMU and view the measured data on a plot.

If you are not familiar with ADI IIO Application, please take a look at::doc:`IIO No-OS </wiki-migration/resources/tools-software/no-os-software/iio>`

This IIO Project uses IIO-Oscilloscope as a client. If you are not familiar with ADI IIO-Oscilloscope Client, please take a look at: :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`

The No-OS IIO Application together with the No-OS IIO ADIS driver take care of all the back-end logic needed to setup the IIO server. The user has to initialize the IIO device and call the IIO app as shown below. The read buffer is used for storing data which shall be available on the plot in the IIO Oscilloscope Client.

The measured data is sampled using a hardware trigger (e.g. interrupts). ADIS1657x offers the capability to use DATA_READY pin as a flag which shows when new measurements are available. Thus, DATA_READY pin is used as a hardware trigger. The code maps the DATA_READY pin as GPIO input with interrupt capabilities. When DATA_READY pin transitions from low to high, new data is available and will be read based on is_synchronous flag setting used in adis_iio_trigger_desc. If the flag is set to true, the data will be read immediately, in the interrupt context. If the flag is set to false, the data will be read from application context. In this case some samples might be missed.

The initialization data is taken from no-OS/projects/eval-adis1657x/src/common/common_data.c and no-OS/projects/eval-adis1657x/src/common/common_data.h files:

.. code:: C

   struct no_os_uart_init_param adis1657x_uart_ip = {
       .device_id = UART_DEVICE_ID,
       .irq_id = UART_IRQ_ID,
       .asynchronous_rx = true,
       .baud_rate = UART_BAUDRATE,
       .size = NO_OS_UART_CS_8,
       .parity = NO_OS_UART_PAR_NO,
       .stop = NO_OS_UART_STOP_1_BIT,
       .extra = UART_EXTRA,
       .platform_ops = UART_OPS,
   };

   struct no_os_spi_init_param adis1657x_spi_ip = {
       .device_id = SPI_DEVICE_ID,
       .max_speed_hz = SPI_BAUDRATE,
       .bit_order = NO_OS_SPI_BIT_ORDER_MSB_FIRST,
       .mode = NO_OS_SPI_MODE_3,
       .platform_ops = SPI_OPS,
       .chip_select = SPI_CS,
       .extra = SPI_EXTRA,
   };

   struct no_os_gpio_init_param adis1657x_gpio_reset_ip = {
       .port = GPIO_RESET_PORT_NUM,
       .number = GPIO_RESET_PIN_NUM,
       .pull = NO_OS_PULL_NONE,
       .platform_ops = GPIO_OPS,
       .extra = GPIO_EXTRA
   };

   struct adis_init_param adis1657x_ip = {
       .gpio_reset = &adis1657x_gpio_reset_ip,
       .sync_mode = ADIS_SYNC_OUTPUT,
       .dev_id = ADIS16577_3,
   };

   struct no_os_irq_init_param adis1657x_gpio_irq_ip = {
       .irq_ctrl_id = GPIO_IRQ_ID,
       .platform_ops = GPIO_IRQ_OPS,
       .extra = GPIO_IRQ_EXTRA,
   };

   const struct iio_hw_trig_cb_info gpio_cb_info = {
       .event = NO_OS_EVT_GPIO,
       .peripheral = NO_OS_GPIO_IRQ,
       .handle = ADIS1657X_GPIO_CB_HANDLE,
   };

   struct iio_hw_trig_init_param adis1657x_gpio_trig_ip = {
       .irq_id = ADIS1657X_GPIO_TRIG_IRQ_ID,
       .irq_trig_lvl = NO_OS_IRQ_EDGE_RISING,
       .cb_info = gpio_cb_info,
       .name = ADIS1657X_GPIO_TRIG_NAME,
   };

The macros used in common_data are defined in platform specific files found in no-OS/projects/eval-adis1657x/src/platform/.

.. _stm32-platform-4:

STM32 platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For STM32 platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/stm32/parameters.h and no-OS/projects/eval-adis1657x/src/platform/stm32/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  5
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &stm32_uart_ops
   #define UART_IRQ_ID     UART5_IRQn

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct stm32_uart_init_param adis1657x_uart_extra_ip = {
       .huart = &huart5,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_BAUDRATE    8000000
   #define SPI_CS          15
   #define SPI_CS_PORT     0
   #define SPI_OPS         &stm32_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct stm32_spi_init_param adis1657x_spi_extra_ip  = {
       .chip_select_port = SPI_CS_PORT,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   4
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS            &stm32_gpio_ops
   #define GPIO_EXTRA          &adis1657x_gpio_reset_extra_ip

Where adis1657x_gpio_reset_extra_ip is:

.. code:: C

   struct stm32_gpio_init_param adis1657x_gpio_reset_extra_ip = {
       .mode = GPIO_MODE_OUTPUT_OD,
       .speed = GPIO_SPEED_FREQ_VERY_HIGH,
   };

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   2
   #define GPIO_DRDY_PORT_NUM  0

   /* Setting for PortA Pin2 used for DATA_READY.
      Has to be adapted accordingly if another pin is used.
    */
   #define ADIS1657X_GPIO_TRIG_IRQ_ID     0    /* Not used in stm32 platform */
   #define ADIS1657X_GPIO_CB_HANDLE       NULL /* Not used in stm32 platform */

   #define GPIO_IRQ_ID             2 /* Pin 2 */
   #define GPIO_IRQ_OPS            &stm32_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          &adis1657x_gpio_irq_extra_ip

Where adis1657x_gpio_irq_extra_ip is:

.. code:: C

   struct stm32_gpio_irq_init_param adis1657x_gpio_irq_extra_ip = {
       .port_nb = 0, /* Port A */
   };

.. raw:: html

   </details>


.. _maxim-platform-4:

Maxim Platform
""""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Maxim platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/maxim/parameters.h and no-OS/projects/eval-adis1657x/src/platform/maxim/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   57600
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &max_uart_ops
   #define UART_IRQ_ID     UART0_IRQn

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct max_uart_init_param adis1657x_uart_extra_ip = {
       .flow = UART_FLOW_DIS
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   1
   #define SPI_CS          1
   #define SPI_BAUDRATE    8000000
   #define SPI_OPS         &max_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct max_spi_init_param adis1657x_spi_extra_ip  = {
       .num_slaves = 1,
       .polarity = SPI_SS_POL_LOW,
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   19
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS             &max_gpio_ops
   #define GPIO_EXTRA           &adis1657x_gpio_extra_ip

Where adis1657x_gpio_reset_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis1657x_gpio_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   6
   #define GPIO_DRDY_PORT_NUM  1

   #define ADIS1657X_GPIO_TRIG_IRQ_ID    GPIO_DRDY_PIN_NUM
   #define ADIS1657X_GPIO_CB_HANDLE      MXC_GPIO_GET_GPIO(GPIO_DRDY_PORT_NUM)

   #define GPIO_IRQ_ID             GPIO_DRDY_PORT_NUM
   #define GPIO_IRQ_OPS            &max_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          &adis1657x_gpio_drdy_extra_ip

Where adis1657x_gpio_drdy_extra_ip is:

.. code:: C

   struct max_gpio_init_param adis_gpio_drdy_extra_ip = {
       .vssel = MXC_GPIO_VSSEL_VDDIOH,
   };

.. raw:: html

   </details>


.. _pico-platform-4:

Pico platform
"""""""""""""



.. raw:: html

   <details><summary>Click to expand</summary>

For Pico platform the following macros are defined in no-OS/projects/eval-adis1657x/src/platform/pico/parameters.h and no-OS/projects/eval-adis1657x/src/platform/pico/parameters.c files: For UART:

.. code:: C

   #define UART_DEVICE_ID  0
   #define UART_BAUDRATE   115200
   #define UART_EXTRA      &adis1657x_uart_extra_ip
   #define UART_OPS        &pico_uart_ops
   #define UART_IRQ_ID     20

Where adis1657x_uart_extra_ip is:

.. code:: C

   struct pico_uart_init_param adis1657x_uart_extra_ip = {
       .uart_tx_pin = UART_TX_PIN,
       .uart_rx_pin = UART_RX_PIN,
   };

For SPI:

.. code:: C

   #define SPI_DEVICE_ID   0
   #define SPI_BAUDRATE    8000000
   #define SPI_CS          SPI0_CS_GP17
   #define SPI_OPS         &pico_spi_ops
   #define SPI_EXTRA       &adis1657x_spi_extra_ip

Where adis1657x_spi_extra_ip is:

.. code:: C

   struct pico_spi_init_param adis1657x_spi_extra_ip  = {
       .spi_tx_pin = SPI0_TX_GP19,
       .spi_rx_pin = SPI0_RX_GP16,
       .spi_sck_pin = SPI0_SCK_GP18,
       .spi_cs_pin = SPI0_CS_GP17
   };

For GPIO:

.. code:: C

   #define GPIO_RESET_PIN_NUM   20
   #define GPIO_RESET_PORT_NUM  0
   #define GPIO_OPS            &pico_gpio_ops
   #define GPIO_EXTRA          NULL /* Not used for pico platform */

For trigger:

.. code:: C

   #define GPIO_DRDY_PIN_NUM   21
   #define GPIO_DRDY_PORT_NUM  0

   #define ADIS1657X_GPIO_TRIG_IRQ_ID     GPIO_DRDY_PIN_NUM
   #define ADIS1657X_GPIO_CB_HANDLE       NULL /* Not used in pico platform */

   #define GPIO_IRQ_ID             GPIO_DRDY_PIN_NUM
   #define GPIO_IRQ_OPS            &pico_gpio_irq_ops
   #define GPIO_IRQ_EXTRA          NULL /* Not used for pico platform */

.. raw:: html

   </details>


| 
| The following code initializes the IIO ADIS1657X driver, initializes the interrupt controller (needed for IIO trigger to sample the data on DATA_READY rising edge), sets the priority for the DATA_READY interrupt, initializes the IIO hardware trigger, defines the list of IIO devices and the list of IIO triggers and finaly initializes the IIO application and starts it.

.. code:: C

   #define DATA_BUFFER_SIZE 400
   uint8_t iio_data_buffer[DATA_BUFFER_SIZE*14*sizeof(int)];
   struct adis_iio_dev *adis1657x_iio_desc;
    
   struct iio_data_buffer data_buff = {
       .buff = (void *)iio_data_buffer,
       .size = DATA_BUFFER_SIZE*14*sizeof(int)
   };
    
   struct iio_hw_trig *adis1657x_trig_desc;
   struct no_os_irq_ctrl_desc *adis1657x_irq_desc;
   struct iio_app_desc *app;
   struct iio_app_init_param app_init_param = { 0 };
    
   ret = adis1657x_iio_init(&adis1657x_iio_desc, &adis1657x_ip);
   if (ret)
       return ret;
    
   /* Initialize interrupt controller */
   ret = no_os_irq_ctrl_init(&adis1657x_irq_desc, &adis1657x_gpio_irq_ip);
   if (ret)
       goto err_irq_init;
    
   ret = no_os_irq_set_priority(adis1657x_irq_desc, adis1657x_gpio_trig_ip.irq_id, 1);
   if (ret)
       goto err_irq_set_prio;
    
   adis1657x_gpio_trig_ip.irq_ctrl = adis1657x_irq_desc;
    
   /* Initialize hardware trigger */
   ret = iio_hw_trig_init(&adis1657x_trig_desc, &adis1657x_gpio_trig_ip);
   if (ret)
       goto err_irq_set_prio;
    
   /* List of devices */
   struct iio_app_device iio_devices[] = {
       {
           .name = "adis16577-3",
           .dev = adis1657x_iio_desc,
           .dev_descriptor = adis1657x_iio_desc->iio_dev,
           .read_buff = &data_buff,
       }
   };
    
   /* List of triggers */
   struct iio_trigger_init trigs[] = {
       IIO_APP_TRIGGER(ADIS1657X_GPIO_TRIG_NAME, adis1657x_trig_desc, &adis_iio_trig_desc)
   };
    
   app_init_param.devices = iio_devices;
   app_init_param.nb_devices = NO_OS_ARRAY_SIZE(iio_devices);
   app_init_param.uart_init_params = adis1657x_uart_ip;
   app_init_param.trigs = trigs;
   app_init_param.nb_trigs = NO_OS_ARRAY_SIZE(trigs);
   app_init_param.irq_desc = adis1657x_irq_desc;
    
   ret = iio_app_init(&app, app_init_param);
   if (ret)
       goto err_iio_app_init;
    
   /* Update the reference to iio_desc */
   adis1657x_trig_desc->iio_desc = app->iio_desc;
    
   ret = iio_app_run(app);
   if (ret)
       goto iio_app_err;
    
   return 0;
    
   iio_app_err:
       iio_app_remove(app);
   err_iio_app_init:
       iio_hw_trig_remove(adis1657x_trig_desc);
   err_irq_set_prio:
       no_os_irq_ctrl_remove(adis1657x_irq_desc);
   err_irq_init:
       adis1657x_iio_remove(adis1657x_iio_desc);
       pr_info("Error!\n");
       return ret;

.. _project-execution-3:

Project Execution
^^^^^^^^^^^^^^^^^

After flashing and running the application, IIO Oscilloscope can be used to make the desired configuration and obtain the desired data. Below you may find some snippets from IIO Oscilloscope, when running IIO Project.

Bellow you can see the Connection window for IIO Oscilloscope. The handshake is performed and the device is detected over UART. After pressing the Connect button we can see the device in the list, together with its channels and we can see the measured data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis1657x_osc_connect.gif
   :align: center

Below you can see the Simple View which contains the read data from the IMU. Observe how the measurements change when the device is moved.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis1657x_osc_measurements.gif
   :align: center

Below you can see the Debug View which contains the list of device attributes, channel attributes and debug attributes. In this example, the sampling frequency is set to 1000 Hz, the calibration offset for accelerometer on x axis is set to -10, some other reads are performed and finally a software reset is triggered using the debug attribute command, which resets the values set previously.\


|image4|

Below you can see the Plot View for the buffered data. IIO Oscilloscope can be used to capture data using the configured hardware trigger. In order to select the trigger as an impulse generator, right click on the adis1657x device in the plot windows, select Impulse generator and choose adis1657x-dev0 trigger. The Plot view shows the raw vales measured by the device. You may observe the spikes in the data due to sudden movement of the device. At the end of the measurement the number of lost samples is read, which in this case was 0, showing that the captured data was continuous.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis1657x_capture.gif
   :align: center

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1650x/adis16500_pcbzangle-web.gif
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1650x/adis16500_pcbztop-web.gif
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1650x/adis16500_pcbzbottom-web.gif
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adis165x/adis165x_attributes.gif
