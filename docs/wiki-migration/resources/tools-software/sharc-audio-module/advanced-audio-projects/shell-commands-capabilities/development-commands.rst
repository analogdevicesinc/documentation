Overview
========

This section describes each of the development and debug related shell commands in detail.

Development and Debug Shell Commands
====================================

edit
----

================= ===================================================
**Description**   Edit a text file
**Inputs**        filename
**Outputs**       Opens a file in editor
\*\* Syntax \*\*  edit <filename>

|image1|

**Example Usage** edit test.txt
:::               HELP: Ctrl-S = save / Ctrl-Q = quit / Ctrl-F = find
================= ===================================================

test
----

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Description**   | test implemented shell command for development and testing purpose. It has to be implemented in the code, built and flashed to be available to run on the shell |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | implementation specific                                                                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | implementation specific                                                                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | test [args...]                                                                                                                                                  |
|                   | |image3|                                                                                                                                                        |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | implementation specific                                                                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

run
---

+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| **Description**   | Runs a command file                                                                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | cmd file/s                                                                                                                  |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | Runs commands from command file and prints output                                                                           |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | run <file1> [<file2> ...]                                                                                                   |
|                   | |image6|                                                                                                                    |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | run test.cmd (where test.cmd is a file in the filesystem with shell commands to be run in sequence, separated by new lines) |
|                   | |image7|                                                                                                                    |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------+

dump
----

+-------------------+--------------------------------------------------------------------------------+
| **Description**   | Hex dump of flash contents                                                     |
+-------------------+--------------------------------------------------------------------------------+
| **Inputs**        | addr - Starting address to dump, len - Number of bytes to dump (default 1)     |
+-------------------+--------------------------------------------------------------------------------+
| **Outputs**       | Displays bytes from memory address                                             |
+-------------------+--------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | dump [addr] <len>                                                              |
+-------------------+--------------------------------------------------------------------------------+
| **Example Usage** | dump 0 5 (where 0 is the staring address in flash memory to dump 5 bytes from) |
+-------------------+--------------------------------------------------------------------------------+
| :::               | Note: Addr is decimal. Refer to the image below for more details               |
|                   | |image9|                                                                       |
+-------------------+--------------------------------------------------------------------------------+

fdump
-----

+-------------------+----------------------------------------------------------+
| **Description**   | Dump the contents of a file in hex                       |
+-------------------+----------------------------------------------------------+
| **Inputs**        | filename, start offset in bytes, size in bytes           |
+-------------------+----------------------------------------------------------+
| **Outputs**       | Displays file content in hex format                      |
+-------------------+----------------------------------------------------------+
| \*\* Syntax \*\*  | fdump <filename> [start offset in bytes] [bytes to dump] |
|                   | |image12|                                                |
+-------------------+----------------------------------------------------------+
| **Example Usage** | fdump test.bin 0x16 32                                   |
|                   | |image13|                                                |
+-------------------+----------------------------------------------------------+

delay
-----

+-------------------+---------------------------------------------------------------------------------------------------+
| **Description**   | Introduce delay in ms                                                                             |
+-------------------+---------------------------------------------------------------------------------------------------+
| **Inputs**        | ms - time in ms                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------------+
| **Outputs**       | Adds delay in ms before running next command or returning to the shell prompt                     |
+-------------------+---------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | delay <ms>                                                                                        |
|                   | |image15|                                                                                         |
+-------------------+---------------------------------------------------------------------------------------------------+
| **Example Usage** | delay 1000 (adds a delay of 1 s)                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------+
| :::               | Note: This shell command can be used in a command file where delay is needed between two commands |
+-------------------+---------------------------------------------------------------------------------------------------+

i2c
---

+-------------------+---------------------------------------------------------------------------------------------------------+
| **Description**   | Executes an I2C write/read transaction                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------------+
| **Inputs**        | i2c_port, i2c_addr , mem_addr , wdata , length , addr_len                                               |
+-------------------+---------------------------------------------------------------------------------------------------------+
| **Outputs**       | Reads from or write to i2c address                                                                      |
+-------------------+---------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | i2c <i2c_port> <i2c_addr> <mem_addr> <wdata> <length> [addr_len]                                        |
|                   | |image18|                                                                                               |
+-------------------+---------------------------------------------------------------------------------------------------------+
| **Example Usage** | i2c 0 0x68 0 "" 4 1 (read 4 bytes from 1 address byte of i2c port 0 device addr 0x68 starting 0th byte) |
|                   | |image19|                                                                                               |
+-------------------+---------------------------------------------------------------------------------------------------------+

+-------------------------------+-----------------------------------------------------------------------------------------+
| \**Inputs to i2c command \*\* | **Description**                                                                         |
+-------------------------------+-----------------------------------------------------------------------------------------+
| i2c_port                      | I2C port to probe                                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------+
| i2c_addr                      | I2C device address                                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------+
| mem_addr                      | Starting memory address                                                                 |
+-------------------------------+-----------------------------------------------------------------------------------------+
| wdata                         | Comma separated string of bytes to write (i.e. "1,0x02,3"). Empty quotes for read only. |
+-------------------------------+-----------------------------------------------------------------------------------------+
| length                        | Number of bytes to read. Zero for write only.                                           |
+-------------------------------+-----------------------------------------------------------------------------------------+
| addr_len                      | Number of address bytes (default 1)                                                     |
+-------------------------------+-----------------------------------------------------------------------------------------+

i2c_probe
---------

+-------------------+------------------------------------------------------------------+
| **Description**   | Probe an I2C port for active devices                             |
+-------------------+------------------------------------------------------------------+
| **Inputs**        | i2c_port - I2C port to probe                                     |
+-------------------+------------------------------------------------------------------+
| **Outputs**       | Displays I2C device addresses for entered I2C port               |
+-------------------+------------------------------------------------------------------+
| \*\* Syntax \*\*  | i2c_probe <i2c_port>                                             |
|                   | |image22|                                                        |
+-------------------+------------------------------------------------------------------+
| **Example Usage** | i2c_probe 0 (displays I2C devices with addresses for I2C port 0) |
|                   | |image23|                                                        |
+-------------------+------------------------------------------------------------------+

stacks
------

================= =============================================
**Description**   Report task stack usage
**Inputs**        None
**Outputs**       Displays stack usage of all the tasks running
\*\* Syntax \*\*  stacks

|image24|

**Example Usage** stacks

|image25|

================= =============================================

cpu
---

+-------------------+-------------------------------------------------------------+
| **Description**   | Report cpu usage                                            |
+-------------------+-------------------------------------------------------------+
| **Inputs**        | None                                                        |
+-------------------+-------------------------------------------------------------+
| **Outputs**       | Displays cpu usage of all cores with current and peak usage |
+-------------------+-------------------------------------------------------------+
| \*\* Syntax \*\*  | cpu                                                         |
|                   | |image28|                                                   |
+-------------------+-------------------------------------------------------------+
| **Example Usage** | cpu                                                         |
|                   | |image29|                                                   |
+-------------------+-------------------------------------------------------------+

syslog
------

================= ========================
**Description**   Show the live system log
**Inputs**        None
**Outputs**       Displays live system log
\*\* Syntax \*\*  syslog

|image30|

**Example Usage** syslog

|image31|

================= ========================

usb
---

+-------------------+------------------------------------------------------------------------------------------------------------------+
| **Description**   | View/set/clear runtime USB settings/metrics. It can be useful while debugging USB audio related tasks or issues. |
+-------------------+------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | None                                                                                                             |
+-------------------+------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | Displays data about Rx and Tx USB packets                                                                        |
+-------------------+------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | usb                                                                                                              |
|                   | |image34|                                                                                                        |
+-------------------+------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | usb                                                                                                              |
|                   | |image35|                                                                                                        |
+-------------------+------------------------------------------------------------------------------------------------------------------+

meminfo
-------

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Description**   | Displays UMM_MALLOC heap statistics                                                                                                                                                  |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | None                                                                                                                                                                                 |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | Displays heap statistics for heap areas UMM_SDRAM_HEAP, UMM_SDRAM_UNCACHED_HEAP, UMM_L2_CACHED_HEAP, UMM_L2_UNCACHED_HEAP along with OS and SHARC audio engine specific memory stats |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | meminfo                                                                                                                                                                              |
|                   | |image38|                                                                                                                                                                            |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | meminfo                                                                                                                                                                              |
|                   | |image39|                                                                                                                                                                            |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

update
------

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Description**   | Updates the firmware via xmodem                                                                                                                                                             |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | Firmware to be updated via xmodem                                                                                                                                                           |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | Prompts about potential issues if power is unplugged. On user input as y/n, goes to receive mode where user needs to transfer the firmware binary over xmodm. Reset on successful transfer. |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | update                                                                                                                                                                                      |
|                   | |image42|                                                                                                                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | update                                                                                                                                                                                      |
|                   | |image43|                                                                                                                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

date
----

+-------------------+-------------------------------------------------------------------------------+
| **Description**   | Get/Set current date and time                                                 |
+-------------------+-------------------------------------------------------------------------------+
| **Inputs**        | None or date/time string in RFC3339 format                                    |
+-------------------+-------------------------------------------------------------------------------+
| **Outputs**       | Displays present set date and time or set date/time based on the input string |
+-------------------+-------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | date <now>                                                                    |
|                   | |image46|                                                                     |
+-------------------+-------------------------------------------------------------------------------+
| **Example Usage** | date 2024-04-01T04:08:53Z                                                     |
|                   | |image47|                                                                     |
+-------------------+-------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/edit_help.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/test_help.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/test_help.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/run_help.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/run.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/run_help.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/run.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/dump.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/dump.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/fdump_help.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/fdump.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/fdump_help.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/fdump.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/delay_help.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/delay_help.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_help.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_help.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_probe_help.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_probe.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_probe_help.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/i2c_probe.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/stacks_help.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/stacks.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cpu_help.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cpu.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cpu_help.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cpu.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/syslog_help.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/syslog.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/usb_help.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/usb.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/usb_help.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/usb.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/meminfo_help.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/meminfo.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/meminfo_help.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/meminfo.png
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/update_help.png
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/update.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/update_help.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/update.png
   :width: 400px
.. |image44| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/date_help.png
   :width: 400px
.. |image45| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/date.png
   :width: 400px
.. |image46| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/date_help.png
   :width: 400px
.. |image47| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/date.png
   :width: 400px
