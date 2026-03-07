CCES Project
============

Overview
--------

| This section provides an overview of the required configurations to build the SAM Audio Starter project using CrossCore Embedded Studio.
| ===== Details =====

Create a new project
~~~~~~~~~~~~~~~~~~~~

| 1. Open CrossCore Embedded Studio and create a new Workspace.
| 2. Create a new project by going to: **File > New > CrossCore Project**
| 3. Set a *Project Name*
| |1.jpg|
| 4. Select **Processor Type** and **Silicon Revision**
| |1-2.jpg|
| 5. Click on the first processor's **Configure Project** button.
| |1-3.jpg|
| 6. In the **Add-In Selection** tab, uncheck all **Recommended Add-ins**.
| |1-4.jpg|
| 7. In the **Template Code** tab, uncheck the first option.
| |1-5.jpg|
| 8. Repeat steps **5** through **7** for all processors.
| ==== General Settings ====

Project References
^^^^^^^^^^^^^^^^^^

| 1. Open *ARM/Core0* **Properties** window. Go to **C/C++ General > Project References** section. Check *SHARC0/Core1* and *SHARC1/Core2*.
| 2. Open *SHARC0/Core1* **Properties** window. Go to **C/C++ General > Project References** section. Uncheck all options.
| 3. Open *SHARC1/Core2* **Properties** window. Go to **C/C++ General > Project References** section. Uncheck all options.
| |2-3.jpg|
| === Rename Project (Optional) === 1. In Project View, rename Projects with more meaningful names.
| |2-1.jpg|
| === Enable Parallel Build === 1. For each one of the projects, right click and go to **Properties**. Go to **C/C++ Build** section. Then to **Behavior** tab.
| 2. Check the **Enable parallel build** option and select the desired option.
| |2-2.jpg|
| ==== Source Locations ==== 1. Open **Properties** window. Go to **C/C++ General > Paths and Symbols** section. Then to **Source Location** tab. |3-1.jpg|
| 2. Click on **Link folder...** button. Enter a **Folder name** and check the **Link to folder in the file system** box. Either browse for the folder or give a relative path. Repeat this step for each processor and source location according to the tables below.
| |3-2.jpg|

ARM/Core0
^^^^^^^^^

=========== ==============================
Folder Name Path
=========== ==============================
src         **<project root>**/ARM/src
include     **<project root>**/ARM/include
ALL         **<project root>**/ALL
=========== ==============================

SHARC0/Core1
^^^^^^^^^^^^

=========== =====================================
Folder Name Path
=========== =====================================
src         **<project root>**/SHARC0/src
startup_ldf **<project root>**/SHARC0/startup_ldf
ALL         **<project root>**/ALL
=========== =====================================

SHARC1/Core2
^^^^^^^^^^^^

=========== =====================================
Folder Name Path
=========== =====================================
src         **<project root>**/SHARC1/src
startup_ldf **<project root>**/SHARC1/startup_ldf
ALL         **<project root>**/ALL
=========== =====================================

| **Note:** Add any missing folder locations if the project has been modified.
| 3. In the **Project Explorer** window, select the folders listed below (multiple folders may be selected at once), right click and select **Resource Configuration > Exclude Folder**. Click on **Select All** and **OK**.
| \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/CCES/osal
| \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/CCES/ARM_CA5/osal
| \* **<project root>**/ARM/src/oss-services/lwip/apps/altcp_tls
| \* **<project root>**/ARM/src/oss-services/lwip/apps/http
| \* **<project root>**/ARM/src/oss-services/lwip/apps/lwiperf
| \* **<project root>**/ARM/src/oss-services/lwip/apps/mqtt
| \* **<project root>**/ARM/src/oss-services/lwip/apps/netbiosns
| \* **<project root>**/ARM/src/oss-services/lwip/apps/smtp
| \* **<project root>**/ARM/src/oss-services/lwip/apps/snmp
| \* **<project root>**/ARM/src/oss-services/lwip/apps/sntp
| \* **<project root>**/ARM/src/oss-services/lwip/apps/tftp
| \* **<project root>**/ARM/src/oss-services/lwip/core/ipv6
| \* **<project root>**/ARM/src/oss-services/lwip/netif/ppp
| |3-3.jpg|
| ==== Includes ==== 1. Open **Properties** window. Go to **C/C++ General > Paths and Symbols** section. Then to **Includes** tab. In the **Language** list select **C/C++ with ADI extensions**.
| |4-1.jpg|
| 2. Click on **Add...** and input the include directories of the project. Repeat this step for each processor and include folder according to the lists below.
| |4-2.jpg|
| === ARM/Core0 ===

-  **<project root>**/ARM/src
   \* **<project root>**/ARM/include
   \* **<project root>**/ALL/include
   \* **<project root>**/ALL/src/sae
   \* **<project root>**/ARM/src/adi-drivers/rsi
   \* **<project root>**/ARM/src/simple-drivers
   \* **<project root>**/ARM/src/simple-services/adau1761
   \* **<project root>**/ARM/src/simple-services/syslog
   \* **<project root>**/ARM/src/simple-services/buffer-track
   \* **<project root>**/ARM/src/simple-services/a2b-xml
   \* **<project root>**/ARM/src/simple-services/adi-a2b-cmdlist
   \* **<project root>**/ARM/src/simple-services/FreeRTOS-cpu-load
   \* **<project root>**/ARM/src/simple-services/a2b-to-sport-cfg
   \* **<project root>**/ARM/src/adi-drivers/ethernet/common
   \* **<project root>**/ARM/src/adi-drivers/ethernet/gemac
   \* **<project root>**/ARM/src/simple-services/adi-osal-minimal
   \* **<project root>**/ARM/src/simple-services/uac2-cdc-soundcard
   \* **<project root>**/ARM/src/simple-services/fs-dev
   \* **<project root>**/ARM/src/simple-services/rtp-stream
   \* **<project root>**/ARM/src/simple-services/vban-stream
   \* **<project root>**/ARM/src/simple-services/wav-file
   \* **<project root>**/ARM/src/simple-services/telnet
   \* **<project root>**/ARM/src/oss-services/lwip/core
   \* **<project root>**/ARM/src/oss-services/lwip/core/ipv4
   \* **<project root>**/ARM/src/oss-services/lwip/netif
   \* **<project root>**/ARM/src/oss-services/lwip/api
   \* **<project root>**/ARM/src/oss-services/lwip/arch
   \* **<project root>**/ARM/src/oss-services/lwip/apps/mdns
   \* **<project root>**/ARM/src/oss-services/umm_malloc
   \* **<project root>**/ARM/src/oss-services/shell
   \* **<project root>**/ARM/src/oss-services/crc
   \* **<project root>**/ARM/src/oss-services/xmodem
   \* **<project root>**/ARM/src/oss-services/yxml
   \* **<project root>**/ARM/src/oss-services/pa-ringbuffer
   \* **<project root>**/ARM/src/oss-services/spiffs
   \* **<project root>**/ARM/src/oss-services/libtelnet
   \* **<project root>**/ARM/src/oss-services/kilo
   \* **<project root>**/ARM/src/oss-services/getline
   \* **<project root>**/ARM/src/oss-services/getopt
   \* **<project root>**/ARM/src/oss-services/printf
   \* **<project root>**/ARM/src/oss-services/c-timestamp
   \* **<project root>**/ARM/src/oss-services/FatFs
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/MemMang
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/CCES/osal
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/CCES/ARM_CA5
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/CCES/ARM_CA5/osal
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/portable/GCC/ARM_CA9
   \* **<project root>**/ARM/src/adi-drivers/ethernet/include
   \* **<project root>**/ARM/src/oss-services/lwip
   \* **<project root>**/ARM/src/oss-services/lwip/include
   \* **<project root>**/ARM/src/oss-services/FreeRTOS-ARM/include
   === SHARC0/Core1 ===
-  **<project root>**/ARM/include
   \* **<project root>**/ALL/src/sae
   === SHARC1/Core2 ===
-  **<project root>**/ARM/include
   \* **<project root>**/ALL/src/sae
   ==== Symbols ====

| 1. Open **Properties** window. Go to **C/C++ General > Paths and Symbols** section. Then to **Symbols** tab. In the **Language** list select **C/C++ with ADI extensions**.
| |5-1.jpg|
| 2. Click on **Add...** and input the macros to be defined during compile time. Repeat this step for each processor and symbol in the tables below.
| |5-2.jpg|
| === ARM/Core0 ===

================== =====
Name               Value
================== =====
\_DEBUG            *N/A*
CORE0              *N/A*
\__SAM_V1\_\_      *N/A*
FEATURE_CPU_LOAD   *N/A*
USB_CDC_STDIO      *N/A*
SHARC_AUDIO_ENABLE *N/A*
SAE_IPC            *N/A*
FREE_RTOS          *N/A*
================== =====

**Note:** *N/A* means don't input any value.

.. _sharc0core1-1:

SHARC0/Core1
^^^^^^^^^^^^

======= =====
Name    Value
======= =====
\_DEBUG *N/A*
CORE1   *N/A*
======= =====

**Note:** *N/A* means don't input any value.

.. _sharc1core2-1:

SHARC1/Core2
^^^^^^^^^^^^

======= =====
Name    Value
======= =====
\_DEBUG *N/A*
CORE2   *N/A*
======= =====

**Note:** *N/A* means don't input any value.

--------------

Libraries
~~~~~~~~~

| 1. Open **Properties** window. Go to **C/C++ General > Paths and Symbols** section. Then to **Library Paths** tab.
| |6-1.jpg|
| 2. Click on **Add...** and input the library directories of the project. Repeat this step for each processor and library path in the lists below.
| |6-2.jpg|
| === ARM/Core0 ===

-  **<project root>**/ARM/lib
   === SHARC0/Core1 ===
-  N/A
   === SHARC1/Core2 ===
-  N/A
   3. Without closing the **Properties** window, go to the **Libraries** tab.

   |6-3.jpg|

   4. Click on **Add...** and input the libraries of the project. Repeat this step for each processor and library in the lists below.

   |6-4.jpg|

   === ARM/Core0 ===
-  cld_sc58x_audio_2_0_w_cdc_lib_Core0.a
   === SHARC0/Core1 ===
-  N/A
   === SHARC1/Core2 ===
-  N/A
   ----

ARM Compiler/Linker Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1. Open *ARM/Core0* **Properties** window. Go to **C/C++ Build > Settings** section. In the **Tool Settings** tab, go to **CrossCore ARM Bare Metal C Compiler > Additional Options**.
| 2. Click on the add icon and add the following options:
| \* -madi-threads
| |7-1.jpg|
| 3. Also, in the **Tool Settings** tab, go to **CrossCore ARM Bare Metal C Linker > General**.
| 4. In the **Custom linker script (-T)** text box specify the path to the linker script in **<project root>**\ */build/ARM-SAM-Audio-Starter.ld*
| |7-2.jpg|
| 5. Also, in the **Tool Settings** tab, go to **CrossCore ARM Bare Metal C Linker > Additional Options**.
| 6. Click on the add icon and add the following options:
| \* -madi-threads
| |7-3.jpg|
| ----

SHARC Compiler/Linker Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1. Open *SHARC0/Core1* and *SHARC1/Core2* **Properties** window. Go to **C/C++ Build > Settings** section. In the **Tool Settings** tab, go to **CrossCore SHARC C/C++ Compiler > Additional Options**.
| 2. Click on the add icon and add the following options:
| \* -gnu-style-dependencies
| |8-1.jpg|
| 3. Open **Properties** window. Go to **C/C++ Build > Settings** section. In the **Tool Settings** tab, go to **CrossCore SHARC Linker > General**.
| 4. In the **Custom LDF** text box, specify the path to the linker script in **<project root>**\ */build/SHARC0-SAM-Audio-Starter.ldf* and **<project root>**\ */build/SHARC1-SAM-Audio-Starter.ldf*, respectively.
| 5. Check the **Individually map functions and data items (-ip)**.
| |8-2.jpg|
| ----

Post-Build Loader Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1. Open *ARM/Core0* **Properties** window. Go to **C/C++ Build > Settings** section. Then to **Build Artifact** tab.
| 2. In **Artifact Type** select **Loader File**.
| |9-1.jpg|
| 3. In the **Tool Settings** tab, go to **CrossCore ARM Loader > General**.
| 4. Choose the following settings:
| \* **Boot Mode (-b)**: SPI Flash

-  **Boot format (-f)**: Binary
-  **Boot code (-bcode)**: 0x1

| |9-2.jpg|
| 5. Also in **Tool Settings** tab, go to **CrossCore ARM Loader > Initialziation**.
| 6. In the **Initialization file (-init)** text box, specify the path to **ezkitSC589_initcode_core0_v10** within *CrossCore Embedded Studio* installation folder (*CrossCore Embedded Studio\\SHARC\\ldr\\ezkitSC589_initcode_core0_v10*).
| |9-3.jpg|
| 7. Also in **Tool Settings** tab, go to **CrossCore ARM Loader > Executable Files**.
| 8. Select the following options:
| ^ Field ^ Core ^ Executable ^ -NoFinalTag ^

+--------------+---------------+--------------------------------------------+----------+
| Booting Core | Core0         | **<workspace>**\\ARM\\Debug\\ARM           | Enabled  |
+--------------+---------------+--------------------------------------------+----------+
| Core         | Core1 (SHARC) | **<workspace>**\\SHARC0\\Debug\\SHARC0.dxe | Enabled  |
+--------------+---------------+--------------------------------------------+----------+
| Core         | Core2 (SHARC) | **<workspace>**\\SHARC1\\Debug\\SHARC1.dxe | Disabled |
+--------------+---------------+--------------------------------------------+----------+

| |9-4.jpg|

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`_

.. |1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/1.jpg
   :width: 400px
.. |1-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/1-2.jpg
   :width: 400px
.. |1-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/1-3.jpg
   :width: 400px
.. |1-4.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/1-4.jpg
   :width: 400px
.. |1-5.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/1-5.jpg
   :width: 400px
.. |2-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/2-3.jpg
   :width: 400px
.. |2-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/2-1.jpg
   :width: 400px
.. |2-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/2-2.jpg
   :width: 400px
.. |3-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/3-1.jpg
   :width: 400px
.. |3-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/3-2.jpg
   :width: 400px
.. |3-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/3-3.jpg
   :width: 400px
.. |4-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/4-1.jpg
   :width: 400px
.. |4-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/4-2.jpg
   :width: 400px
.. |5-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/5-1.jpg
   :width: 400px
.. |5-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/5-2.jpg
   :width: 400px
.. |6-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/6-1.jpg
   :width: 400px
.. |6-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/6-2.jpg
   :width: 400px
.. |6-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/6-3.jpg
   :width: 400px
.. |6-4.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/6-4.jpg
   :width: 400px
.. |7-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/7-1.jpg
   :width: 400px
.. |7-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/7-2.jpg
   :width: 400px
.. |7-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/7-3.jpg
   :width: 400px
.. |8-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/8-1.jpg
   :width: 400px
.. |8-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/8-2.jpg
   :width: 400px
.. |9-1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/9-1.jpg
   :width: 400px
.. |9-2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/9-2.jpg
   :width: 400px
.. |9-3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/9-3.jpg
   :width: 400px
.. |9-4.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/cces-project/9-4.jpg
   :width: 400px
