Navigation
==========

You can return to the ACE Application User Guide Homepage here:

-  :doc:`Application User Guide </wiki-migration/resources/tools-software/ace/applicationuserguide>`
-  `Previous (Capture View) <https://wiki.analog.com/resources/tools/software/ace/understandingtheui/captureview.txt>`_

|

.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.


| ===== Tool Views =====

.. container:: centeralign

   \ |image1| *Figure 1. Tool Views*\


The **Tool Views** are a collection of views that add functionality to the main views. The Tool Views is found in the Tools drop-down on the side bar of the main window, as seen in Figure 1. Tool Views that were open when the application is closed will reopen when the application starts up again. The following are the available tools in :doc:`ACE Software </wiki-migration/resources/tools-software/ace>`:

-  :doc:`Macro Tool </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`
-  :doc:`System Explorer </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`
-  :doc:`Register Debugger </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`
-  :doc:`Events </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`
-  FPGA Programmer
-  Firmware Programmer
-  EEPROM Recovery Tool
-  :doc:`SDP-K1 Recovery Tool </wiki-migration/resources/tools/software/ace/understandingtheui/toolviews>`
-  Script Manager
-  Platform API Logger

Macro Tool
----------

.. container:: centeralign

   \ |image2|\ *Figure 2. Macro Tool View*\


The **Macro Tool View**, as seen in Figure 2, allows commands to be recorded and played back.  Macros can be created to configure a chip, to share a series of steps with other users, or to perform common tasks multiple times.

.. container:: centeralign

   \ |image3|\ *Figure 3. Macro Toolbar*\


The **Macro Toolbar**, as seen in Figure 3, can be used to open, record, save, close, or delete Macros. While recording, the **Commands List** will automatically be populated when any interaction with the device is performed. By default, the Commands List is populated with top level commands, and it can be extended to show sub-commands by checking the **Record Sub-Commands** box prior to recording.

.. tip::

   \ ``Sub-commands are denoted by a “>” symbol for each level of the tree.``\


+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Tool          | Description                                                                                                                         |
+===============+=====================================================================================================================================+
| Record        | Records all transactions done by the user in the user interface consisting of top-level commands extended with sub-commands         |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Stop          | Stops recording of the macro commands                                                                                               |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Play          | Plays the recorded macro commands or plays the imported macro file                                                                  |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Edit          | Edits the recorded macro commands or edits the imported macro file                                                                  |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Save          | Saves changes to the current opened macro                                                                                           |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Save As       | Saves the recorded macro commands or saves the imported macro file as a new file                                                    |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Open          | Opens the saved macro file                                                                                                          |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Close         | Closes the currently opened macro                                                                                                   |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Delete        | Deletes the currently opened macro                                                                                                  |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Generate Code | Generates scripts that perform the recorded actions in a supported language of choice (C#, ACE Hex, Hex, ACE Macro, MATLAB, Python) |
+---------------+-------------------------------------------------------------------------------------------------------------------------------------+

**Click** the subsections below to expand/collapse the details: 

.. raw:: html

   <details><summary>Record, Save Macro File and Generate Scripts XHIDDENSTARTSTOP Record device configuration and transactions by putting them into a macro file. Once a macro is generated using the Macro Tool, it can then be called again thereby repeating the steps performed in one go. The following steps explain how to generate a macro:

-  Click the **Record** button (Record macro commands) located in the left side icon on the image below, refer to Figure 4.

.. container:: centeralign

   \ |image4|\ *Figure 4. Record Macro button*\


-  Start performing device interaction such as changing parameters, inputting values to registers on the memory map, capturing data, etc. The Commands List window will fill up as the GUI is navigated and interacted with.
-  Once all parameters to be entered are recorded, click the **Stop** button (Stop recording macro Commands).
-  Once a macro file has been recorded, it can then be saved and stored into a macro file **(.acemacro)** using the **Save** button, or be played again to repeat the previously performed steps using **Play** button.
-  Additionally, ACE has a built-in feature to generate scripts that perform the recorded actions in the supported language of choice. Click the **Generate Code** button at the right of the Macro Toolbar to open the script generator window, as seen in Figure 5.

.. container:: centeralign

   \ |image5|\ *Figure 5. Generate Code Button*\


-  Select the desired language among C#, MATLAB or Python

.. container:: centeralign

   \ |image6|\ *Figure 6. Generated Matlab Code*\


This code can then be imported into an IDE for execution, as seen in Figure 6. Using this code as the base, additional features such as instrument control can be added in order to have an automated set of measurements. Apart from supported languages, the remote API can also be used by IDEs that support DLLs like LabVIEW. The DLL is located in the ACE installation directory within the subfolder "Clients".

*Reference:* :doc:`Recording a macro and generating scripts by Luis Beltran </wiki-migration/software-tools/ace/recording-macros>`

XHIDDENEND

XHIDDENSTART See More Details...</summary>

If there is a macro currently open and the **Record** button is selected, a window will pop up giving the options to either record a new macro or to append the recording onto the currently open macro. If a new macro will be created and added to the Macros List, select **Record new macro**. This macro will automatically become the current macro and the transactions will be recorded as components of this new macro. This will have no effect on any other open macros which will still be available in the Macros List. If the next transaction recorded will be added to the Commands List of the currently open macro, select the **Append** option.

When the **Stop** button is pressed, no further transactions will be recorded and the **Macros View** will open in the main application view area. From there, the macro commands can be played, modified, or deleted. Right-clicking on any command in the grid will open a **Context Menu**, wherein the order of execution of commands can be altered by promoting and demoting individual commands. The user can delete commands individually, or all the commands at once by selecting the **Clear all** button in the main application view area.

Commands can also be skipped by selecting the checkbox for that command in the **Skip** column. Similarly, you can insert a break after a particular command by selecting the checkbox in the **Break** column. When a break is added, the macro will run all commands up to and including the selected command before waiting for the user’s input to continue. Alternatively, a **delay** can be added to a command so that the macro pauses but does not stop after a command is executed. A delay can be added through the commands Context Menu for periods ranging from 10 milliseconds to 10 seconds.

The **Context** column allows the subsystem which the commands are being executed on to be set based on the list of compatible subsystems in the drop-down menu. This step may need to be carried out if the current session differs from the session when the Macro was recorded.

The **Comment** column allows the user to record non-executable comments about the operation performed.

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Macro Command Format and Supported Transactions</summary>

**MACRO COMMAND FORMAT**

``Format: <Context Path>: <TransactionName>; //Command line``

+----------------+---------------------------------------+-------------------------------------------------------------------+
| Component      | Symbol/Example                        | Description                                                       |
+================+=======================================+===================================================================+
| Context Path   | @Subsystem_1.AD9144 Eval Board.AD9144 | Path is made up of Subsystem number, Board Name and/or Chip Name. |
+----------------+---------------------------------------+-------------------------------------------------------------------+
| Path Separator | : (Colon)                             | To separate Path and Transaction                                  |
+----------------+---------------------------------------+-------------------------------------------------------------------+
| Transaction    | @TransactionName                      | To execute Transaction                                            |
+----------------+---------------------------------------+-------------------------------------------------------------------+
| Terminator     | ; (Semi-colon)                        | To separate one transaction line to other.                        |
+----------------+---------------------------------------+-------------------------------------------------------------------+
| Comment        | // or #                               | To create a comment line section                                  |
+----------------+---------------------------------------+-------------------------------------------------------------------+

**COMMONLY USED TRANSACTIONS**

+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Name               | Transaction                         | Arguments                                 | Description                                                              |
+====================+=====================================+===========================================+==========================================================================+
| Write Register     | Evaluation.Control.WriteRegister    | Address, Value                            | Writes the register value to hardware.                                   |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Read Register      | Evaluation.Control.ReadRegister     | Address                                   | Reads the specified register.                                            |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Write Register Map | Evaluation.Control.WriteRegisterMap | MapName                                   | Writes software values in the map to part, or all maps if not specified. |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Read Register Map  | Evaluation.Control.ReadRegisterMap  | MapName                                   | Reads the registers in the memory map, or all maps if not specified.     |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Select Page        | Evaluation.Control.SelectPage       | PageGroupName, pageIndex                  | Sets the current index for a page group.                                 |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Write Bitfield     | Evaluation.Control.WriteBitfield    | BitfieldName, Value, (optional) pageIndex | Writes the bitfield value to hardware.                                   |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Read Bitfield      | Evaluation.Control.ReadBitfield     | BitfieldName, (optional) pageIndex        | Reads the specified bitfield value.                                      |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+
| Reset              | @Reset()                            | -                                         | Resets the part.                                                         |
+--------------------+-------------------------------------+-------------------------------------------+--------------------------------------------------------------------------+

.. container:: hide

   \| Apply Settings \| @ApplySettings() \| - \| Applies ACE values to the part. \| \| Read Settings \| @ReadSettings() \| - \| Reads values from the part. \|

.. raw:: html

   </details>




.. raw:: html

   <details><summary>Creating and Loading Macro File to ACE Macro Tool</summary>

**CREATE AND LOAD MACRO FILE**

.. container:: centeralign

   \ |image7|\ *Figure 7. Open Macro File*\


-  Open any text editor, such as Notepad, to create a macro file.
-  Create a macro command sequence following the previous subsection (**Macro Command Format and Supported Transactions**)
-  After creating macro commands, you can save the text file using the acemacro format **(.acemacro)**.
-  In the **Macro Tool**, click the **Open Macro** button to import the created macro file, as seen in Figure 7.
-  The imported macro file will be listed under **Macros**.
-  Click the **Play Macro** button to play all or selected commands from the imported macro.

**SAMPLE MACRO CODE**

``A sample macro to configure AD9122-M5375-EBZ by setting the NCO modulation frequency to 30MHz. The DAC frequency is set to 500MHz with an interpolation value of 4.``

::

   @Subsystem_1.AD9122-M5375-EBZ.AD9122: @Reset(); //Resetting the AD9122 Chip.
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x1C, 0x00);  //Enable Half Band Filter 1
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x1D, 0x00);  //Enable Half Band Filter 2
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x1E, 0x01);  //Disable Half Band Filter 3
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x30, 0xEC);  //Writing FTW_0 with data 0xCD
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x31, 0x51);  //Writing FTW_1 with data 0xCC
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x32, 0xB8);  //Writing FTW_2 with data 0xCC
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteRegister(0x33, 0x1E);  //Writing FTW_3 with data 0x4C
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteBitfield("Bypass_NCO", 0);  //Enabling NCO Mode
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.WriteBitfield("Update_FTW_request", 1);  //Updating FTW
   UI.pause(300);                                                                //Delays the macro for 300 ms before executing next command
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.ReadRegister(0x36);  //Reading data from NCO_FTW_update
   @Subsystem_1.AD9122-M5375-EBZ.AD9122: Evaluation.Control.ReadRegisterMap();  //Reading all registers data

**SAMPLE MACRO CODE WITH PAGE SELECTOR**

``A sample macro to enable the digital gain and inverse sinc of AD9136-FMC-EBZ. DAC0 and DAC1 share the same register address (0x111). In order to write bits in the registers of each DAC, select the PageIndx (DIGITAL_DAC_PAGING) corresponding to each DAC channel.``

.. code:: xml

   @Subsystem_1.AD9136-FMC-EBZ.AD9136: Evaluation.Control.SelectPage("DIGITAL_DAC_PAGING", 0);  //Selecting Page 0 to configure DAC0
   @Subsystem_1.AD9136-FMC-EBZ.AD9136: Evaluation.Control.WriteRegister(0x111, 0xA0);  //Enabling Digital Gain and Inverse Sinc
   @Subsystem_1.AD9136-FMC-EBZ.AD9136: Evaluation.Control.SelectPage("DIGITAL_DAC_PAGING", 1);  //Selecting Page 0 to configure DAC1
   @Subsystem_1.AD9136-FMC-EBZ.AD9136: Evaluation.Control.WriteRegister(0x111, 0xA0);  //Enabling Digital Gain and Inverse Sinc
   @Subsystem_1.AD9136-FMC-EBZ.AD9136: Evaluation.Control.ReadRegisterMap();  //Reading all registers data

.. raw:: html

   </details>


System Explorer
---------------

The **System Explorer**, as seen in Figure 8, is used to navigate and show all the subsystems that have been added by the user to the system. By definition, a subsystem is a unit that represents a placeholder for hardware components grouped together under a system. It represents a group of physically connected boards. A subsystem can consist of just a single component at a minimum.

Subsystem details include **boards**, **chips** (or components), **chip memory maps**, **controllers**, **FPGA memory maps**, and **interposers**. Memory maps to both the chip and FPGA can be accessed using System Explorer where you can write, read, or reset register settings.

.. container:: centeralign

   \ |image8|\ *Figure 8. System Explorer View*\


Register Debugger
-----------------

|image9| The **Register Debugger**, as seen in Figure 9, is used to perform raw register writes to and reads from the chip.

The **Register Address Dropdown** is populated with a list of all registers in the chip where the user can write or read from. When the **Write** button is selected, the hexadecimal value in the Write Data Textbox will be written to the selected register and this action added to the history grid.

Similarly when the **Read** button is selected, the selected register is read from and its value populates the Read Data Textbox. It is important to note that since this view preforms raw writes, there is no write verification step, so the value on the hardware after the write may not match the value that was written.

| The **History Grid** shows previous writes and reads performed from within this view. These writes and reads can be repeated by selecting the step to be repeated and clicking the **Repeat** button. All previous actions can be removed from the **History Grid** using the **Clear** button.
| *Figure 9. Register Debugger View*

Events
------

.. container:: centeralign

   \ |Events.png|\ *Figure 10. Event Logs*\


The **Events Tool View**, as seen in Figure 10, contains a list of event logs including error and warnings generated within the application software. Messages are divided into the following sections:

-  **Level** – Severity of the message.
-  **Source** – Generator of the message.
-  **Name** – Property of event source generating the message.
-  **Type** – Category of the message. Each message is categorized into one of the following:

   -  **Unspecified** – Informational message.
   -  **ValueRequired** – Value must be supplied.
   -  **ValueInvalid** – Value is invalid.
   -  **ValueOutOfRange** – Value supplied is not within acceptable range.
   -  **ConverterNotAvailable** – An attempt was made to convert the value to the required type, but no such converter exists.
   -  **ValueTypeInvalid** – Incorrect type of value; no attempt at conversion/coercion was made.
   -  **UnknownProperty** – No property was found with the specified name/binding.
   -  **Coerced** – Value supplied is invalid and is coerced to the nearest valid value.
   -  **FileNotFound** – File path was not found in the file system.

-  **Description** – Details about why the message appeared.

| 
| ==== SDP-K1 Recovery Tool View ==== The **SDP-K1 Recovery Tool** is used to recover the firmware loaded to the SDP-K1 Controller Board. The SDP-K1 board is designed to be used in conjunction with various ADI evaluation boards as part of a customer evaluation environment. To know more about SDP-K1, refer to `SDP-K1 <https://wiki.analog.com/resources/eval/sdp/sdp-k1>`_ wiki page.

To use the SDP-K1 Recovery Tool, refer to Figure 11 and follow the steps below:

-  Select **SDP-K1 Recovery Tool** under Tool Views drop-down list.
-  Click the **Search** button to detect SDP-K1 boards connected to the PC.
-  Select **Standard** firmware.
-  **Flash** the firmware. The daughter board connected to the SDP-K1 board must be detected in ACE under **Attached Hardware** once the firmware flashing is done.

.. container:: centeralign

   \ |image10|\ *Figure 11. SDP-K1 Recovery Tool View*\


.. |image1| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/ace_toolviews.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/macro_tool_view.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/macro_tool_toolbar.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/software-tools/ace/ace-record_icon.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/software-tools/ace/ace-generate_icon.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/software-tools/ace/ace-generated-code-editor.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/macro_tool_openmacro.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/system_explorer_view.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/registerdebugger.png
   :width: 180px
.. |Events.png| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/Events.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools/software/ace/understandingtheui/sdp-k1_recovery_tool.png
   :width: 900px
