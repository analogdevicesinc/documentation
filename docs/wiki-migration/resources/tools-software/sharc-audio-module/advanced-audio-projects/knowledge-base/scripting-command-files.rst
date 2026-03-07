Creating and Executing Script Files
===================================

Overview
--------

The purpose of this article is to give an overview of how to perform automated scripting to execute a series of shell commands either at startup or on-demand via another shell commands, or the pushbuttons. This can be helpful for testing when a series of commands is known, automate complex routing schemes, dump debug info and to share established commands with other engineers.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase9.jpg
   :width: 600px

There are several methods for creating or putting script files in the file-system and there are also several methods for executing these script files as well. See below for more details on each method.

Getting your script in the filesystem
-------------------------------------

Script files, typically in the filename format of *<filename>.cmd* typically reside in one of the available filesystems within the Audio Starter. This could be an SD Card, a SPIFFS filesystem (on-board flash), eMMC or something else that is available depending on the hardware and software supported. Users can verify which filesystems are available by executing the :doc:`drive </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` command in the shell. Use one of the options below to get the command file on your filesystem.

+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option # | Command                                                                                                                                         | Description                                                                                                                                                                                  |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1        | :doc:`edit </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>`           | Direct creation/edit within the shell. Follow the example usage in the edit command to create a *<filename>.cmd* file.                                                                       |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2        | :doc:`recv </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>`            | Use the *recv* command linked to transfer an existing *<filename>.cmd* file onto your filesystem, via XMODEM, from your PC.                                                                  |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3        | :doc:`cp </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>`              | If you already have a *<filename>.cmd* file on your SD Card that you transferred from your PC to your SD Card, you can use the copy command to move the file from one filesystem to another. |
+----------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--------------

--------------

Executing Script Commands
-------------------------

There are a few different methods for executing script commands: Automatically at startup, via the :doc:`run </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>` command or via the available pushbuttons. Some of these scripts have naming and filesystem location requirements, while others do not. See below for each type.

Startup Script
~~~~~~~~~~~~~~

=============== ======================= ==================
**Script Name** **Required Filesystem** **Execution Type**
*shell.cmd*     SPIFFS (*sf:*)          On Reset or POR
=============== ======================= ==================

This script allows you to execute a set of commands, automatically at startup. This script MUST be called *shell.cmd* and must reside in the *sf:* filesystem. If you created this file and it resides on your SD Card, you can copy it over from your SD Card to *sf:* by typing in the shell:

*cp <filename>.cmd sf:shell.cmd*

Below is a simple example to set up a route, turn on a wav recording, record for 30 seconds, then stop and close the file.

| |image1|
| |image2|

.. important::

   Startup script may be aborted halfway through its execution by pressing **CTRL+C** like any other shell script. However, user must be aware that depending on system timing some commands may be executed before terminal is connected to SAM and startup script is able to be aborted.


If you find yourself in the above sticky situation, where you are blocked for too long, or you file has become corrupted such that the shell cannot boot any longer, you will need a way to remove the *sf:shell.cmd* file. You can do this by establishing a connection via :doc:`telent </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/telnet-session>`, assuming you have the Audio Starter IP Address, and remove the offending file. A system reset after this will allow you to boot properly.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase12.jpg
   :width: 600px

If you don't have your Audio Starter IP address, you can run a command like *arp -a* to see the list of IP Addresses on the network (for DHCP supported Audio Starters):

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase13.jpg
   :width: 400px

It is highly recommended that you perform some validation on your startup scripts using the :doc:`run </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>` command prior to putting them in the SPIFFS file system to avoid the above scenario.

--------------

--------------

Pushbutton Scripts
~~~~~~~~~~~~~~~~~~

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| **Script Name** | **Required Filesystem**                                                                                                                                                                                                      | **Execution Type** |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| *pushbtn1.cmd*  | *Default* - See :doc:`drive </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` command to get the default filesystem (SD Card is typical).            | On PB1 Press       |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| *pushbtn2.cmd*  | *Default* - See :doc:`drive </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` command to get the default filesystem (SD Card is typical).            | On PB2 Press       |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+

These scripts allow you to execute a set of commands, on physical press of one of the buttons listed below . This script MUST be called one of the names listed above and must reside in the default filesystem.

The following examples display the current :doc:`wav </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>` configuration in the :doc:`syslog </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>`, when pressed:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase14.jpg
   :width: 400px

Note that if the file with the exact names don't exist, this will be reported in the system log that the file could not be opened.

--------------

--------------

Run Command Scripts
~~~~~~~~~~~~~~~~~~~

+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Script Name** | **Required Filesystem**                                                                                                                                                                  | **Execution Type**                                                                                                                                                                          |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *<any>*         | Any filesystem available - See :doc:`drive </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>` command.            | On shell execution of :doc:`run </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>` command.                         |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The run command works similarly to the pushbutton commands, except that you can specify the command name of your choosing, filesystem of your choosing and you execute it via the shell, rather than using physical hardware.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands-capabilities/run.png
   :width: 400px

--------------

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase10.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase11.jpg
   :width: 400px
