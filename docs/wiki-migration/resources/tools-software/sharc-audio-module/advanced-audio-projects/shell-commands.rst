Sharc Audio Module - Shell Commands
===================================

Overview
--------

The purpose of the shell commands is to provide a command line interface for users to communicate with the system. On the Audio Starter Framework, these commands are broken up by features. These shell commands are categorized for documentation purpose based on their usage. This documentation details the superset list of all of the commands that exist for all of the Audio Starters. To find the specific commands for your particular hardware platform and specific branch, you can type *help* in the shell to view your specific sub-set.

*Note that not all terminal programs are created equal as it relates to using the Audio Starters. While you are free to use your Terminal program of choice, it's possible that not all commands will work on all programs due to limitations with character sets, etc. Therefore, we recommend following the setup guide for the preferred :doc:`Terminal Program </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/prerequisites>` to get the best experience for shell interaction with the Audio Starter.*

| Review the following knowledge base articles for various options for establishing a shell connection:
| 1. :doc:`USB OTG Shell Session </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/usb-otg-session>` 2. :doc:`Telnet Session </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/telnet-session>`

--------------

Help
----

The purpose of the *help* command is to provide the list of all available commands for a particular hardware platform as well as a summary of what each command is responsible for.

|image1| **Example List of Shell Commands**

--------------

Command-Specific Help
---------------------

Each specific command has a set of inputs (with ranges) for the command. These inputs are used to change the functionality of each command, noting that some commands have no inputs. The format of the command can be retrieved by typing in *<help> <command>*, where *<command>* is one of the valid commands from the list printed by the *help* command.

For example, the command *a2b*, takes an input: *cmd*, where the range for *cmd* is a *string* type taking either *main* or *sub*:

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/help_a2b.png
   :width: 400px

As seen displayed by the shell by typing *help a2b* as seen above, for example. An exhaustive list of shell commands can be found below.

--------------

Command List
------------

*Below is the exhaustive list of commands - with grouping by feature type. This can be helpful for better understanding what sort of support is available for a particular feature. Please click the links below directly to access further details about these commands.*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| **Feature**                                                                                                                                                     | **Description**                                                                                                    | **Relevant Shell Commands**                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :doc:`Audio Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/audio-commands>`                       | The goal of these commands is to help users to configure the audio related capabilities of the Audio Starter       | route, wav, vban, rtp, vu, adc, signal, asrc                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :doc:`A2B Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/a2b-commands>`                           | The goal of these commands is to help users to configure the A2B related capabilities of the Audio Starter         | a2b, discover, cmdlist, tdm                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :doc:`Filesystem Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/filesystem-commands>`             | These commands are implemented to help users to configure the filesystem related capabilities of the Audio Starter | drive, ls, format, df, rm, cat, cp, recv, send, fsck, cmp, sdtest, date                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :doc:`Network Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/network-commands>`                   | These commands are used for network related configuration of the Audio Starter                                     | eth                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| :doc:`Development and Debug Commands </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands/development-commands>` | Shell commands used for development and debug purposes                                                             | edit, test, run, dump, fdump, delay, i2c, i2c_probe, syslog, stacks, cpu, usb, update, meminfo, resize, syslog, ver, shell, echo |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+


.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/navigation_advanced_audio_projects
   :alt: Advanced Audio Projects#.examples-signal-generator|Application Examples - Signal Generator#.|Advanced Audio Projects#.debug-session|Setting up a Debug Session

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/help-cmd.png
   :width: 400px
