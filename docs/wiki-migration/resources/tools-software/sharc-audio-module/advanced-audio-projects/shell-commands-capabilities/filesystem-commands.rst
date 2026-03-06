Overview
========

This section describes each of the filesystem related shell commands in detail.

--------------

Filesystem Shell Commands
=========================

drive
-----

+-------------------+----------------------------------------------------------------------------------------------------+
| **Description**   | Configures the audio routing table                                                                 |
+-------------------+----------------------------------------------------------------------------------------------------+
| **Inputs**        | Shows/supports filesystem device information                                                       |
+-------------------+----------------------------------------------------------------------------------------------------+
| **Outputs**       | When no inputs, lists name of the default device. Otherwise sets default device to the given input |
+-------------------+----------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | drive [<device> <action>]                                                                          |
|                   | |image3|                                                                                           |
+-------------------+----------------------------------------------------------------------------------------------------+
| **Example Usage** | drive (list default device)                                                                        |
+-------------------+----------------------------------------------------------------------------------------------------+
| :::               | drive sd default (set sd as default device)                                                        |
|                   | |image4|                                                                                           |
+-------------------+----------------------------------------------------------------------------------------------------+

+---------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------+
| \**Inputs to drive command \*\* | **Description**                                                       | \*\* Acceptable Values \*\*                                       |
+---------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------+
| none                            | Lists default device when no inputs                                   | N/A                                                               |
+---------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------+
| device                          | Name of the device to perform action on                               | sf: or sd: (This is platform specific, run help drive for options |
+---------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------+
| action                          | action to be performed (for now, default is the only supported action | default (This is platform specific, run help drive for options    |
+---------------------------------+-----------------------------------------------------------------------+-------------------------------------------------------------------+

--------------

ls
--

================= =============================
**Description**   lists the files in the device
**Inputs**        none
**Outputs**       lists the file in the device
\*\* Syntax \*\*  ls

|image5|

**Example Usage** ls

|image6|

================= =============================

--------------

cat
---

+-------------------+-----------------------------------------------------------------+
| **Description**   | Display the content of the file entered as input to the command |
+-------------------+-----------------------------------------------------------------+
| **Inputs**        | filename                                                        |
+-------------------+-----------------------------------------------------------------+
| **Outputs**       | Displays the file content on the shell                          |
+-------------------+-----------------------------------------------------------------+
| \*\* Syntax \*\*  | cat <filename>                                                  |
|                   | |image8|                                                        |
+-------------------+-----------------------------------------------------------------+
| **Example Usage** | cat <filename>                                                  |
+-------------------+-----------------------------------------------------------------+

--------------

format
------

+-------------------+-----------------------------------------------------------------+
| **Description**   | Format an internal flash filesystem                             |
+-------------------+-----------------------------------------------------------------+
| **Inputs**        | device name                                                     |
+-------------------+-----------------------------------------------------------------+
| **Outputs**       | Performs format action on the device and erases all its content |
+-------------------+-----------------------------------------------------------------+
| \*\* Syntax \*\*  | format <devicename>                                             |
|                   | |image11|                                                       |
+-------------------+-----------------------------------------------------------------+
| **Example Usage** | format sf:                                                      |
|                   | |image12|                                                       |
+-------------------+-----------------------------------------------------------------+

df
--

+-------------------+---------------------------------------------------------+
| **Description**   | Shows internal filesystem disk full status              |
+-------------------+---------------------------------------------------------+
| **Inputs**        | none or device name                                     |
+-------------------+---------------------------------------------------------+
| **Outputs**       | Shows total size, used and available size of the device |
+-------------------+---------------------------------------------------------+
| \*\* Syntax \*\*  | df [sf: / sd:]                                          |
|                   | |image15|                                               |
+-------------------+---------------------------------------------------------+
| **Example Usage** | df (when no inputs, displays disk status                |
+-------------------+---------------------------------------------------------+
| :::               | df sf: (displays disk status of sf: filesystem)         |
+-------------------+---------------------------------------------------------+
| :::               | df sd: (displays disk status of sdcard)                 |
|                   | |image16|                                               |
+-------------------+---------------------------------------------------------+

--------------

rm
--

================= ==========================================
**Description**   Removes a file or files
**Inputs**        filename/s to be removed
**Outputs**       removes entered file/s from the silesystem
\*\* Syntax \*\*  rm <file1> [<file2> ...]

|image17|

**Example Usage** rm file.xml
:::               rm file1.xls file2.xml file3.xml
================= ==========================================

--------------

cp
--

+-------------------+-------------------------------------------------------------------------------------------------------------------+
| **Description**   | Copy source file <src> to <dst>                                                                                   |
+-------------------+-------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | source and destination file names to be copied from and to                                                        |
+-------------------+-------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | copies entered file/s from the filesystem to destination file. If destination file does not exist, it creates one |
+-------------------+-------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | cp <file1> <file2>                                                                                                |
|                   | |image19|                                                                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | cp file1.xml file2.xml                                                                                            |
+-------------------+-------------------------------------------------------------------------------------------------------------------+

--------------

recv
----

+-------------------+----------------------------------------------------------------------------------------------------------+
| **Description**   | Receive a file via XMODEM                                                                                |
+-------------------+----------------------------------------------------------------------------------------------------------+
| **Inputs**        | Name of the file to receive via XMODEM                                                                   |
+-------------------+----------------------------------------------------------------------------------------------------------+
| **Outputs**       | receives entered file from the PC host over XMODEM using the terminal program such as tera term or putty |
+-------------------+----------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | recv <file>                                                                                              |
|                   | |image22|                                                                                                |
+-------------------+----------------------------------------------------------------------------------------------------------+
| **Example Usage** | recv test1.wav (while it waits, send test1.wav from XMODEM using terminal program)                       |
|                   | |image23|                                                                                                |
+-------------------+----------------------------------------------------------------------------------------------------------+

--------------

send
----

+-------------------+---------------------------------------------------------------------------------------------------------------------------+
| **Description**   | Send files via YMODEM                                                                                                     |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+
| **Inputs**        | Name/s of the file/s to send via YMODEM                                                                                   |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+
| **Outputs**       | sends entered file/s from the filesystem to the PC host over YMODEM using the terminal program such as tera term or putty |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+
| \*\* Syntax \*\*  | send <file1> [<file2> ...]                                                                                                |
|                   | |image26|                                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+
| **Example Usage** | recv test1.wav (while it waits, send test1.wav from XMODEM using terminal program)                                        |
|                   | |image27|                                                                                                                 |
+-------------------+---------------------------------------------------------------------------------------------------------------------------+

--------------

sdtest
------

+-------------------+------------------------------------------------------------------------+
| **Description**   | Test the write/read speed of the SD card                               |
+-------------------+------------------------------------------------------------------------+
| **Inputs**        | Number of milliseconds to read/write (default 5000)                    |
+-------------------+------------------------------------------------------------------------+
| **Outputs**       | Test write/read speed for the SD card and displays the results in KB/s |
+-------------------+------------------------------------------------------------------------+
| \*\* Syntax \*\*  | sdtest [ms]                                                            |
|                   | |image30|                                                              |
+-------------------+------------------------------------------------------------------------+
| **Example Usage** | sdtest (test for 5000 ms                                               |
+-------------------+------------------------------------------------------------------------+
| :::               | sdtet 1000 (test for 1000 ms)                                          |
|                   | |image31|                                                              |
+-------------------+------------------------------------------------------------------------+

--------------

.. image:: https://wiki.analog.com/_media/navigation Filesystem Commands
   :alt: Audio Commands#.audio-commands|Audio Commands#.|Shell Commands#.network-commands|Network Commands

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/drive_help.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/drive.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/drive_help.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/drive.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/ls_help.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/ls.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cat_help.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cat_help.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/format_help.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/format.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/format_help.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/format.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/df_help.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/df.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/df_help.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/df.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/rm_help.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cp_help.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/cp_help.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/recv_help.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/recv2.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/recv_help.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/recv2.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/send_help.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/send2.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/send_help.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/send2.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/sdtest_help.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/sdtest.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/sdtest_help.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/sdtest.png
   :width: 400px
