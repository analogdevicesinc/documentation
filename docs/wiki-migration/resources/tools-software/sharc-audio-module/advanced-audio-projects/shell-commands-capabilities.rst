Familiarize with additional capabilities of the shell command
=============================================================

*This section will take you through different shell commands that are available to be run from the serial terminal of the SAM board.* \| **Shell Command** \| **Used for** \| **Syntax** \| **Example Output** \| \| help \| Print all the implemented shell commands or get help on a shell command \| help - shell help Usage: help <command>. Without arguments it shows a summary of all the shell commands. \| |image1| \| \| help <cmd> \| Print the usage of shell cmd \| help <cmd> \| |image2| \| \| ver \| Show version information \| ver \| |image3| \| \| i2c \| Executes an I2C write/read transaction \| i2c <i2c_port> <i2c_addr> <mem_addr> <wdata> <length> [addr_len] \| |image4| \| \| i2c_probe \| Probe an I2C port for active devices \| i2c_probe <i2c_port> \| |image5| \| \| syslog \| Show the live system log \| syslog \| |image6| \| \| ls \| Shows a device directory listing \| ls [device] \| |image7| \| \| format \| Formats an internal flash filesystem \| format [dev] \| |image8| \| \| fsck \| Check the internal filesystem \| fsck [dev] \| |image9| \| \| discover \| Discovers an A2B network \| discover <a2b.xml> <verbose> <i2c_port> <i2c_addr> \| |image10| \| \| df \| Shows internal filesystem disk full status \| df [dev:] \| |image11| \| \| rm \| Removes a file \| rm <file1> [<file2> ...] \| \| \| cat \| Print file on standard output \| cat <file> \| \| \| cp \| Copy source file <src> to <dst> \| cp <src> <dst> \| \| \| stacks \| Report task stack usage \| stacks \| |image12| \| \| cpu \| Report cpu usage \| cpu \| |image13| \| \| usb \| View/set/clear runtime USB settings/metrics \| usb \| |image14| \| \| recv \| Receive a file via XMODEM \| recv <file> \| |image15| |image16| \| \| send \| Send files via YMODEM \| send <file> \| |image17| |image18| \| \| update \| Updates the firmware via xmodem \| update \| |image19| |image20| \| \| meminfo\| Displays UMM_MALLOC heap statistics \| meminfo \| |image21| \| \| test \| Test command \| test \| This is a developers only feature that allows implementing a test command and running on the shell \| \| sdtest \| Test the write/read speed of the SD card \| sdtest [Number of milliseconds to read/write (default 5000)] \| |image22| \| \| route \| Configures the audio routing table \| route [ <idx> <src> <src offset> <dst> <dst offset> <channels> [attenuation] [mix or set] ] \| |image23| |image24| \| \| run \| Runs a command file \| run <file1> [<file2> ...] \| |image25| \| \| wav \| Manages wave file source/sink \| wav <src or sink> <on or off> [file] [channels] [bits] \| |image26| \|\


|image27|

+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| cmp     | Compare <file1> to <file2>                               | cmp <file1> <file2>                                       | |image36| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| a2b     | Set/get A2B mode                                         | a2b [main or sub]                                         | |image37| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| rtp     | Manages RTP stream Rx/Tx                                 | rtp <rx or tx> <on or off> <ip> [port] [channels] [bits]  | |image38| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| vban    | Manages VBAN stream Rx/Tx                                | vban <rx or tx> <on or off> <ip> [port] [channels] [bits] | |image39| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| cmdlist | Plays a SigmaStudio XML command list                     | cmdlist <cmdlist.xml> <verbose> <i2c_port>                | |image40| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| drive   | Shows/supports filesystem device information             | drive <device> <action>                                   | |image41| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| delay   | Adds delay to command files. Ref. to 'run' shell command | delay <ms>                                                |           |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| dump    | Hex dump of flash contents                               | dump [addr] <len>                                         |           |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| vu      | Show VU (volume unit) meters                             | vu                                                        | TODO      |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| eth     | Report ethernet status                                   | eth                                                       | |image42| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| resize  | Resize/Sync terminal window                              | resize [columns [lines]]                                  |           |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+
| date    | Get/Set current date and time                            | date <now>                                                | |image43| |
+---------+----------------------------------------------------------+-----------------------------------------------------------+-----------+

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/help-cmd.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/help-cmd-2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ver.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/i2c.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/i2c_probe.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/syslog.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/ls.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/format.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/fsck.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/discover.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/df.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/stacks.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cpu.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/usb.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/recv.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/recv2.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/send.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/send2.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/update.png
   :width: 400px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/update2.png
   :width: 400px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/meminfo.png
   :width: 400px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sdtest.png
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route.png
   :width: 400px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/route3.png
   :width: 400px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/run.png
   :width: 400px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/wav.png
   :width: 400px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b.png
   :width: 400px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cmp.png
   :width: 400px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b.png
   :width: 400px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/rtp.png
   :width: 400px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban.png
   :width: 400px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cmdlist.png
   :width: 400px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/drive.png
   :width: 400px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/eth.png
   :width: 400px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/date.png
   :width: 400px
.. |image36| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cmp.png
   :width: 400px
.. |image37| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/a2b.png
   :width: 400px
.. |image38| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/rtp.png
   :width: 400px
.. |image39| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/vban.png
   :width: 400px
.. |image40| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/cmdlist.png
   :width: 400px
.. |image41| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/drive.png
   :width: 400px
.. |image42| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/eth.png
   :width: 400px
.. |image43| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/date.png
   :width: 400px
