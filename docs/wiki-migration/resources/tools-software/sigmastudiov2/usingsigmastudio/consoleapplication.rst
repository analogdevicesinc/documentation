| 
| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`
| ====== Console Application ======

.. note::

   This feature is available from SigmaStudio+ 1.2.0


SigmaStudio+ operations can be executed from Windows Command-line using the SS+ console application (SStudioPlusConsole.exe) provided in the Host folder of the installation location. This console application can perform several operations like Link-Compile-Download a project to target platform, updating the parameters, import SigmaStudio projects and many more. SStudio+ console application also supports batch file execution (i.e., multiple of commands can be executed using a batch file).
| ===== Getting Started with SStudio+ ===== SStudio+ console application can be executed from Windows Command-line. Use “\ **--help**\ ” as shown below to get the help or list of available commands. All the available commands will be listed as shown below.
| ``C:\Analog Devices\SigmaStudioPlus-Rel2.3.0\Host>SStudioPlusConsole.exe --help

  Analog Devices, Inc. SigmaStudio+

  SigmaStudio+ 2.3.0.0
  Copyrightc 2024

    lcd               Perform Link Compile download

    update            Update the plugin property

    updateboolean     Update the Boolean type plugin property

    updatestring      Update the String type plugin property

    updatenumeric     Update the Numeric type plugin property

    updatelist        Update the List type plugin property

    read              Read the value from the target

    import            Import SigmaStudio project

    export            Export system files

    activatepreset    Activate specified Preset

    getpresets        Get the list of saved presets

    getproperties     List of available plugin properties

    getshapes         List of all the available shapes inside a parent canvas

    savepreset        Save Preset

    deletepreset      Delete preset

    help              Display more information on a specific command.

    version           Display version information.``
| SStudio+ terminates after executing every command. To avoid terminating the SStudio+ after each command, set the continue property to true as shown below:
| “\ **-c true**\ “ or “\ **--continue true**\ ”. Default value of this property will be 'False'.
| ===Return Values=== Console commands returns integer type values indicating the message as follows:
| 0 - Success
| 1 - Unable to open project
| 2 - Unable to save project
| 3 - Empty project path
| All other return values are specific to the commands. You can find the return values of a command by entering
| **<<command>> --help**
| ===== Example Commands ===== **1. Perform Link-Compile-Download**
| SStudioPlusConsole.exe lcd –p < project file path including project name >
| ``SStudioPlusConsole.exe lcd -p "C:\Users\Test_01.ssprj" --continue true`` The above command will open the project file, perform link-compile-download and display all the messages on the console.
| **2. Update Numeric Property:**
| SStudioPlusConsole.exe updatenumeric –p <project file path including project name> -n <Plugin property name> -v <Property value> -u <shape Uid> -s <save the changes true/false>
| ``SStudioPlusConsole.exe updatenumeric -p "C:\Users\Test_01.ssprj" -n DCValue -u DCInput_0 -v 5 -s true --continue true`` The above command will update the DCValue on DCInput_0 to 5.
|

.. note::

   Command arguments can be provided in any order. If any single argument contains space in between, it can be mentioned inside the double quotation

