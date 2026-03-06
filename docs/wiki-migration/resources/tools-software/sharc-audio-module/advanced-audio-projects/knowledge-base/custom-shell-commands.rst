Adding Custom Shell Commands
============================

Overview
--------

This article gives a brief overview of how to add your own custom shell commands. Let's take the following simple example, where we want to add a new shell command called *custom*, that takes a single input value of 0 or 1, performs some error handling and validation checks on the input, and outputs "Hello 0" or "Hello 1" depending on the input parameter or an error message on invalid inputs.

| |image1|
| |image2|
| |image3|

Details
-------

Command Framework
~~~~~~~~~~~~~~~~~

Each shell command consists of the following specifiers, which is required as part of the minimum implementation when adding a new shell command:

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| **Attribute**          | **Description**                                                                                                                                                                                                                                                                                         | **Example** |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Command Name           | This is the command specifier that will be typed/executed in the shell                                                                                                                                                                                                                                  | |image9|    |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Command Summary        | This is a brief summary of what the command does, that will be printed when the command :doc:`help </wiki-migration/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands>` is typed                                                                                                    | |image10|   |
|                        |                                                                                                                                                                                                                                                                                                         | |image11|   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Command Help           | This is the usage that is printed for a given command when the command `help <command> </resources/tools-software/sharc-audio-module/advanced-audio-projects/shell-commands#command-specific_help>`__ is executed. This typically specifies the inputs to the command, the options for each input, etc. | |image12|   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Command Implementation | This is the specific implementation of the command that will be executed                                                                                                                                                                                                                                | |image13|   |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

Adding the Hooks
~~~~~~~~~~~~~~~~

The following instructions detail the minimum code changes to add to achieve the minimum framework as described above. To add a new shell command, the following source code files are typically affected (though this may depend on the project and version):

+--------------+--------------------------------------------------------------------------+------------------------------------------------------+
| \**File \*\* | **Description**                                                          | \**Typical Source Path \*\*                          |
+--------------+--------------------------------------------------------------------------+------------------------------------------------------+
| shell.c      | This contains the core implementation for the shell                      | *<project_root>/<ARM|SHARC0>/src/oss-services/shell* |
+--------------+--------------------------------------------------------------------------+------------------------------------------------------+
| shell_cmds.c | This contains the project specific implementations of the shell commands | *<project_root>/<ARM|SHARC0>/src/oss-services/shell* |
+--------------+--------------------------------------------------------------------------+------------------------------------------------------+

We would follow the steps below:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| **Step**                                                                                                                                                                                                                                                                                                                                                                                                        | **Description** |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| 1. Add shell function prototype in *shell.c*. The name of the new custom shell must be in the following required format:                                                                                                                                                                                                                                                                                        | |image22|       |
| ``SHELL_FUNC( shell_<cmd> );`` Where *<cmd>* is the Command Name identifier.                                                                                                                                                                                                                                                                                                                                    | |image23|       |
| *Note that* **SHELL_FUNC** *is a helper macro that will resolve the function prototype to:*                                                                                                                                                                                                                                                                                                                     |                 |
| ``extern void shell_<cmd>( SHELL_CONTEXT *ctx, int argc, char **argv )``                                                                                                                                                                                                                                                                                                                                        |                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| 2. Add shell function command summary and help summary string attribute variable declarations in *shell.c*. This is done by adding the following instantiation:                                                                                                                                                                                                                                                 | |image24|       |
| ``SHELL_HELP( <cmd> );`` Where *<cmd>* is the Command Name identifier.                                                                                                                                                                                                                                                                                                                                          | |image25|       |
| This is a helper macro which creates two externally declared const array of characters that will be resolved as:                                                                                                                                                                                                                                                                                                |                 |
| ``extern const char shell_help_<cmd>`` and                                                                                                                                                                                                                                                                                                                                                                      |                 |
| ``extern const char shell_help_summary_<cmd>``                                                                                                                                                                                                                                                                                                                                                                  |                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| 3. Add the new shell command to the table ``shell_commands[]`` In the format:                                                                                                                                                                                                                                                                                                                                   | |image26|       |
| ``{"<cmd>", shell_<cmd>},`` This table takes the string associated with the command and the shell command function.                                                                                                                                                                                                                                                                                             | |image27|       |
| This is the lookup table that the core of the shell module uses when a user types in a command into the shell. If users forget to add the new command to this table the shell core will reject it with an *Invalid command* message.                                                                                                                                                                            |                 |
| **Always ensure that new shell commands are never last in the table!**                                                                                                                                                                                                                                                                                                                                          |                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| 4. Add the command help summary to the table ``shell_help_data[]`` In the format:                                                                                                                                                                                                                                                                                                                               | |image28|       |
| ``SHELL_INFO( <cmd> ),`` Note that **SHELL_INFO** is a helper macro that resolves the table input to ``{ <cmd>, shell_help_summary_<cmd>, shell_help_<cmd> }`` This is the lookup table for the *help* and *help <cmd>* shell calls. If the user forgets to fill in this table, the command and summary will not appear in the *help* summary list, and the call to *help <cmd>* will return *Unknown command*. | |image29|       |
| **Always ensure that new shell commands are never last in the table!**                                                                                                                                                                                                                                                                                                                                          |                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

Command Hook Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that the above instantiations are in place, we can add the help summary, command help and implementation specific details for our project following the steps below.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 1. Open *shell_cmds.c* or whichever command file is being used for project specific implementations and add the following: ``const char shell_help_<cmd>[] = "<cmd_usage>\n";`` Where *<cmd_usage>* gives a brief explanation of the input parameters and their range/meaning. This is the string that will be printed when the user types *help <cmd>*. | |image33| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 2. Underneath the command usage, add the following: ``const char shell_help_summary_<cmd>[] = "<cmd_summary>";`` Where *<cmd_summary>* is a brief summary of what the command does. This is the string that will be printed when the user types *help* and is also printed when the user types *help <cmd>*.                                             | |image34| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 3. Add the empty function for the command which matches the format: ``extern void shell_<cmd>( SHELL_CONTEXT *ctx, int argc, char **argv )``                                                                                                                                                                                                             | |image35| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| 4. At this point you have enough framework in place for compilation, so now is a good time to compile the code, resolve any compiler errors and verify that your new shell command meets the minimum command framework requirements that were previously described.                                                                                      |           |
| ✔ Code compiles and runs                                                                                                                                                                                                                                                                                                                                 |           |
| ✔ Command appears in help summary                                                                                                                                                                                                                                                                                                                        |           |
| ✔ *help <cmd>* runs and displays properly                                                                                                                                                                                                                                                                                                                |           |
| ✔ Command executes (even if left empty)                                                                                                                                                                                                                                                                                                                  |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Command Implementation
~~~~~~~~~~~~~~~~~~~~~~

Now that all of the framework hooks are in place, we can start filling in the implementation details of the shell command. Realistically, this implementation will be based on your own project specific needs but we'll go over our specific implementation. But before we do this, let's go over the input parameters in a little more detail.

Shell Context (SHELL_CONTEXT \* ctx)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the current state of the shell context.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase35.jpg
   :width: 600px

It is largely used for the core of the shell implementation, but when used within the context of a shell command, it is mainly used for polling for incoming characters that a specific shell command might use to escape or complete a sequence.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase36.jpg
   :width: 600px

Number of input arguments (int argc)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the number of inputs the shell command will be able to parse, including the command. For example, if one command has one input, *argc* will be *2*, with the first input being the command and the second input being the commands first input:

*custom 1* -> *argc = 2*, where *custom* is the first argument and *1* is the second argument.

This is useful for input validation to ensure the command is not attempting to parse more than the number of commands that it is expecting to receive and to ensure that the *argv* parameter is not accessed outside of its bounds.

Array of input arguments (char \**argv)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is an array of strings (array of characters) that hold all of the inputs to the shell command. The <cmd> parameter plus their inputs are accessible by array index notation, starting from index 0:

| *<cmd> <input1> <input2>...* *argv[0] = <cmd>, argv[1] = <input1>, argv[2] = <input2>...* and so on.
| Then for our specific case:

| *custom 1*-> *argv[0] = custom* and *argv[1] = 1*
| Noting again that these are fed to the shell command as strings (array of chars). Any inputs that are numerical must be converted as such when used in this form.

With this information provided above, this gives us the following example implementation for our custom shell function:

::

   void shell_custom(SHELL_CONTEXT *ctx, int argc, char **argv)
   {
       uint8_t input;
       
       /* Validate number of arguments */
       if (argc != 2 ) {
           printf( "Invalid arguments. Type help [<command>] for usage.\n" );
           return;
       }
       
       /* Convert second input to an integer */
       input = strtoul(argv[1], NULL, 0);
       
       /* Print expected output when the input matches our expectations */
       if (input == 0 ) {
           printf("Hello 0\n");
       } else if (input == 1) {
           printf("Hello 1\n");
       } else {
           printf("Invalid input parameter. Type help [<command>] for usage.\n");
       }
   }

And of course, each shell command implementation will be implemented differently depending on the intended use of the function. As always, it is highly recommended to validate the input parameters to avoid unexpected errors and array overflows from occurring (which can crash the program!).

--------------

`Knowledge Base#.|Knowledge Base#.|Knowledge Base <https://wiki.analog.com/_media/navigation Knowledge Base#.>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase26.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase27.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase28.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase18.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase16.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase19.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase17.jpg
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase15.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase18.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase16.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase19.jpg
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase17.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase15.jpg
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase20.jpg
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase21.jpg
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase22.jpg
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase23.jpg
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase24.jpg
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase25.jpg
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase29.jpg
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase30.jpg
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase20.jpg
   :width: 400px
.. |image23| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase21.jpg
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase22.jpg
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase23.jpg
   :width: 600px
.. |image26| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase24.jpg
   :width: 600px
.. |image27| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase25.jpg
   :width: 600px
.. |image28| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase29.jpg
   :width: 600px
.. |image29| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase30.jpg
   :width: 600px
.. |image30| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase32.jpg
   :width: 600px
.. |image31| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase33.jpg
   :width: 600px
.. |image32| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase34.jpg
   :width: 600px
.. |image33| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase32.jpg
   :width: 600px
.. |image34| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase33.jpg
   :width: 600px
.. |image35| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/knowledge-base/knowledgebase34.jpg
   :width: 600px
