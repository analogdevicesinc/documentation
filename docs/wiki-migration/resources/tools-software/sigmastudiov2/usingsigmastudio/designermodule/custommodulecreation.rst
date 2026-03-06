:doc:`Return to previous page </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`

1. DLL based Custom Module Creation
===================================

| Algorithm Designer can be launched by selecting **Tools➔ Algorithm Designer** from the menu bar as shown in the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.
| |image1|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Launcher


| The upcoming sections demonstrates how a developer can create custom modules using DLB library file and also by providing source code directly in SigmaStudioPlus Algorithm Designer.
| Here, we are creating a *Mute (No Slew)* module as an example to show DLB method (Both the example project MuteNoSlew and the .dlb file (MuteNoSlew.dlb) generated from CCES are built in Release mode) and *Simple Adder* module to show source code method.
|

.. note::

   The example projects mentioned, Mute (No Slew) and Simple Adder, follow the same procedures in most steps. Therefore, this page will primarily focus on one example, namely Mute (No Slew), to guide developers in creating a custom module using SigmaStudioPlus Algorithm Designer. Any differences in procedure between the Mute (No Slew) and Simple Adder module creation will be noted separately.


| Once the Algorithm Designer window opens, if the developer requires guidance in creating a custom module, there is an 'open book' icon, as shown in the figure below. |image2|

.. container:: centeralign

   \ **Figure:** Algorithm Designer **Help** Link


Clicking on this icon will direct the user to the Algorithm Designer Help Wiki page, where the necessary information and step-by-step guidance are provided.
| ===== 1.1. Mute (No Slew) Module =====
| ==== 1.1.1 Configuration Tab ====
| This section defines the basic configuration of the module to be developed.
| This tab helps the developer to mention the Name of the module, version, processing type etc.
| Make sure that the developer provide the same name as mentioned in the ‘.c’ file containing module algorithm/logic.
| For eg: if the name of API is **BPROCESS_MuteNoSlew** (as per :doc:`Coding convention for Block Process based modules </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/algorithm_designer_coding_conventions>`), the name to be mentioned in the Name section of Configuration tab must be **MuteNoSlew** as shown in the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/configuration_1.png
   :align: center

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Configuration Tab for Mute No Slew module.


| Below are the said configurable parameters:
| ^ **Parameters** ^ **Description** ^

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                         | Name of the module                                                                                                                                                                                                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Version                                      | Version number in a.b.c.d format                                                                                                                                                                                                                      |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Processor                                    | Target processor (ADSP-SC5xx / ADSP-214xx)                                                                                                                                                                                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Processing Type                              | Block or Sample processing                                                                                                                                                                                                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration Properties (Primary/Secondary) | Optional properties (like channels, stages etc.) for end user to configure the behavior of the module (like pins, UI replication etc.). Up to two properties can be enabled. Secondary property can only be enabled when primary property is enabled. |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Enable                                       | Whether property is enabled                                                                                                                                                                                                                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                                         | Name of the property (Predefined properties are FS, NumChannels etc)                                                                                                                                                                                  |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Min                                          | Minimum value of the property                                                                                                                                                                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Max                                          | Maximum value of the property                                                                                                                                                                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   The **Advanced Customization** (Custom UI & Custom Code) options are advanced configuration settings and not be used in the regular designer flow. Developers can contact the support team for more information regarding this configuration.


| Click Next button.

1.1.2 Source and Libraries Tab
------------------------------

| This section is used to define the algorithm source.
| Algorithm source can be in the form of CCES libraries (MuteNoSlew module) and/or C source with headers (SimpleAdder module).
| For MuteNoSlew, we are inserting the CCES library (.dlb file) directly into the Algorithm Designer editor under the "Libraries" tab, as shown in the two figures below. The DLB files to be added can be selected using ‘Browse’ button and added using the '+' button. Use the ‘-’ button to remove the selected file from the list.

When a DLB is added as Embedded Library, the contents of the DLB is embedded into the module DLL generated by Algorithm Designer. The DLB is then no longer required to be present while using the module generated by Algorithm Designer in SigmaStudioPlus.


|image3|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Source and Libraries Tab, Libraries window (Embedded DLB) for Mute No Slew module.


On the other hand, when the DLB is added as Referenced Library, the DLB file should be present along with the DLL, as a reference to the DLB present in the DLL.



|image4|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Source and Libraries Tab, Libraries window (Referenced DLB) for Mute No Slew module.


| Click Next button.

1.1.3 Parameter Definition Tab
------------------------------

| The user can define the module (target) parameters that are required for this particular module.
| Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.

|image5|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Parameter Definition Tab for Mute No Slew module.


| Mention the parameter name under Name, the data format of this particular parameter can be selected from drop down option under Format. If the parameter is a buffer check the Buffer option.
| ^ **Parameters** ^ **Description** ^

+--------+------------------------------------------------------------------------------------+
| Name   | Parameter name is mentioned here                                                   |
+--------+------------------------------------------------------------------------------------+
| Format | Data format of parameter (Float / Integer / Fixed 8.24 / Fixed 5.27 / Fixed 2.30)  |
+--------+------------------------------------------------------------------------------------+
| Buffer | Enable, when the parameter is a buffer. Disable, when the parameter is a variable. |
+--------+------------------------------------------------------------------------------------+

| Once done, click the + symbol. Repeat the steps for adding next parameter details.
| Click Next button.

1.1.4 I/O Pins Tab
------------------

This section is to define the number of input and output pins this module has. Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.

| |image6|
| Upon entering the name of the input pin, developer have the option to choose the *"direction of data"* via this particular pin, the *"type of data"* its handling, whether the pin has *"dynamic"* capability, i.e. whether this pin supports pin growth during designing phase etc.

| For our particular example, Mute No Slew, we are configuring this pin to be Dynamic as shown in above :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`. Upon clicking the '+' button, that configuration will be added to list and developer can follow the same procedure for output pin as well.
| |image7|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module I/O Pins Tab for Mute No Slew module


+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameters** | **Description**                                                                                                                                                                                    |
+================+====================================================================================================================================================================================================+
| Name           | Name of the pin (ex: input0, output0 etc)                                                                                                                                                          |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Direction      | Indicates whether Input or Output                                                                                                                                                                  |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Data Type      | Indicates the type of the pin (ex: Audio, Control, PCMx).                                                                                                                                          |
|                | Use Audio pins for audio processing (input and output).                                                                                                                                            |
|                | Use PCMx pins if you are handling digital audio streams or interfacing with PCM devices                                                                                                            |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Dynamic        | Indicates whether the pin is Dynamic. If the developer wishes to vary the pin count based on a configurable property, enable this option. Else, leave it disabled and the pin count remains static |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property       | Enabled only when Dynamic is enabled. Indicates the configurable property upon which the pin changes dynamically                                                                                   |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Use '+' button to add pins. Use '-' button to remove selected pin from the list.
| Click Next button.

1.1.5 Variables Tab
-------------------

In Variables tab, the variables that will used during run-time to process the module parameters mentioned in Parameter Definition tab of Designer. Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.


|image8|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Variables Tab for Mute No Slew module


Mention name of variable under Name, the type of the variable (Boolean, Numeric, Numeric array or List). ‘Boolean’ type can be given to variables, which support either 1 or 0 as its value. ‘Numeric’ type can be given to variables that support integer values. ‘Numeric array’ and ‘List’ type can be given to variables which supports a set of numeric values, especially used when designing filter modules. Click ‘+’ to add the variable details. Repeat the steps for other variables. Since, for this particular example, we are creating a Mute No Slew module, we require only one variable of Boolean type to control the module’s ON/OFF functionality.

| Click Next button.

1.1.6 Memory Size Tab
---------------------

In Memory Size tab, we can mention the memory allocated for the module. Based on your module’s memory requirement, developer has to allocate memory in this section. Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.

The user can assign a static value to the memory size or assign a formula which is a function of one or more runtime variables and size of runtime buffers. ‘FS’, ‘NumChannels’ and ‘BlockSize’ are predefined variables and can be used in the formula to represent the ‘Schematic Sampling Rate’, ‘Growth Count’ and ‘Schematic Block Size’ (for block processing Modules) respectively. Ternary operators can also be used to define the size. For example; “1024 + (NumChannels>256?20:10)”. But, for our particular example Mute No Slew, no memory location needs to be allocated in State memory as we have only one runtime parameter (Enable/Disable option).

Click Validate All to validate the memory size configured. The validate icon will turn green if the size definition is valid. If invalid, the icon will turn red.


|image9|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Memory Size Tab for Mute No Slew module


| Click Next.

1.1.7 Parameter Assignment Tab
------------------------------

The Parameter Assignment tab is where we can map the run-time variables mentioned previously in :doc:`1.1.5 Variables Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>` with the parameters of the module mentioned in the :doc:`1.1.3 Parameter Definition Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.


|image10|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Parameter Assignment Tab for Mute No Slew module


+----------------+------------------------------------------------------------------------------------------------------------+
| **Parameters** | **Description**                                                                                            |
+================+============================================================================================================+
| Name           | Name of the parameter                                                                                      |
+----------------+------------------------------------------------------------------------------------------------------------+
| Equation       | This is the field where the values are assigned to the parameters. Refer to below section for more details |
+----------------+------------------------------------------------------------------------------------------------------------+
| Value          | Current value of the parameter                                                                             |
+----------------+------------------------------------------------------------------------------------------------------------+
| Format         | Parameter data format                                                                                      |
+----------------+------------------------------------------------------------------------------------------------------------+
| Safeload       | Indicates whether the parameter to be safeloaded. Explained below.                                         |
+----------------+------------------------------------------------------------------------------------------------------------+
| Group          | Safeload group name. Valid only for safeload parameters. Explained below.                                  |
+----------------+------------------------------------------------------------------------------------------------------------+

| The Equation field is different for individual parameters and tables.
| • Individual Parameter - The user can either set a static value to the parameter or assign a formula which is a function of one or more runtime variables and size of runtime buffers. To set a formula, the user needs to define one or more runtime variables or runtime buffers. ‘FS’, ‘NumChannels’ and ‘BlockSize’ are predefined variables and can be used in the formula to represent the ‘Schematic Sampling Rate’, ‘Growth Count’ and ‘Schematic Block Size’ (for block processing Modules) respectively. Configuration properties defined in “Configuration” window are also available as variables to be used in the equation. In Legacy SigmaStudio, “NumChannels” is the same as “RepCount”.
| • Tables - The user can set a runtime buffer to the table. Formula or constants are not supported and should not be assigned to Table parameters.
| When it comes to ‘Safeload’ and ‘Safeload Group’, some Algorithms require a set of parameters be updated at once and the update in the parameter memory happens while the Algorithm is not being executed. For example, in a Bi-quad filter, five filter coefficients form the parameter set. To update the parameters of the Bi-quad filter, it is mandatory to satisfy the following conditions:
| • Coefficients are updated while the filter is not being executed.
| • All the five coefficients are updated at once.
| This is to ensure that the filter executes with a set of stable coefficients. If either of the above two conditions are not met, the resultant parameter set used in the Bi-quad filter can be a mix of coefficients from two different parameter sets and this can lead to filter instability. If the ‘Safeload’ checkbox is selected, the Algorithm Designer ensures that the first condition mentioned above is met, i.e. corresponding parameter is updated in the parameter memory while the Algorithm is not being executed.
| “Safeload Group” maps two or more parameters to the same group and ensure that the parameters belonging to the same group are updated at once. Thus, safeload group ensures that the second condition is also met.

| 
| Validate the configuration by clicking Validate All.
| Click Next.

1.1.8 UI Designer Tab
---------------------

UI Designer is used to design and configure the user interface for the module. The developer has the option to create a graphical representation of their custom module by using different options from Toolbox window. Each button has their on specific properties, which we have the privilege to alter under Properties tab. Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.


|image11|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module UI Designer Tab, Properties window for Mute No Slew module


| For this particular example, since mute module requires only an Enable/Disable option from UI, a Checkbox and Label was selected from Toolbox menu. Select the checkbox and the properties of that checkbox can be seen on right hand side under Properties window. Adjusting the size of checkbox adjusts the Width, Height etc. fields in Properties window. Once done with properties, there is an Assignments tab next to it where the run-time variables mentioned previously in :doc:`1.1.5 Variables Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>` section, can be assigned to this checkbox as shown in the below figure.
| |image12|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module UI Designer Tab, Assignments window for Mute No Slew module


Assignments window could be used to assign the runtime variables and buffers to the controls such that assigned runtime variable or buffer could be controlled using the graphical control.

+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameters**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                  |
+==================+==================================================================================================================================================================================================================================================================================================================================================================================================================+
| Control          | Name of the selected control. Name is assigned by Algorithm Designer and is non-editable by user                                                                                                                                                                                                                                                                                                                 |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Control Property | Indicates the property on the control, which could be assigned with a runtime variable                                                                                                                                                                                                                                                                                                                           |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Variable         | Indicates the selected runtime variable. The drop down will list only unassigned variables and variables of the same type as the selected control (Numeric, Boolean etc.). For this particular example, that variable is ‘uservar1’ as per definition done in section :doc:`1.1.5 Variables Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`   |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Assign           | Can be used to assign a variable to the control. Will be active only when there is no active assignment on the control                                                                                                                                                                                                                                                                                           |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unassign         | Can be used to remove an assignment. Will be active only when there is an active assignment on the control                                                                                                                                                                                                                                                                                                       |
+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Click Next.

1.1.9 Settings Tab
------------------

In Settings tab, miscellaneous settings are assigned to the module.

Once the module(s) to be used as SigmaStudioPlus plugins are configured using the Algorithm Designer, it can be converted into a DLL for redistribution and reuse.

Before proceeding, save the designer project as shown in below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/settings_1.png
   :align: center

The developer can mention the name with which it should appear in the SigmaStudioPlus application under ToolBox Caption. Please refer the below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>` to understand the settings mentioned for this example.


|image13|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Settings Tab for Mute No Slew module


+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameters**         | **Description**                                                                                                                                                                                                   |
+========================+===================================================================================================================================================================================================================+
| Toolbox Caption        | Indicates the caption to be used in the toolbox                                                                                                                                                                   |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Toolbox Hierarchy      | Indicates the toolbox hierarchy. Hierarchy levels should be separated using '.'                                                                                                                                   |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI Caption             | Indicates the caption to be displayed on SigmaStudioPlus UI                                                                                                                                                       |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Description            | Description of the module                                                                                                                                                                                         |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Documentation URL      | Any documentation URL to be mentioned here while displaying the help contents of that particular module                                                                                                           |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Restrict Addins-Window | By enabling this option, after DLL generation and providing path to that DLL in SigmaStudioPlus, the created module will not be listed under SigmaStudioPlus Toolbox during audio system’s schematic design phase |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| Click the 'Build Plugin' button on bottom right corner of Algorithm Designer window as shown in the figure. The build window will open up and list all the modules in the current Algorithm Designer Project.

1.1.10 Configuring Plugin DLL and its Generation
------------------------------------------------

| As final stage of custom module creation, developer can choose to include one or more modules in the DLL. For each of the module, the user may choose whether to include the Algorithm, Parameter Computation and UI. Whenever UI or Parameter Computation is not selected, the plugin name of the external UI or Parameter computation plugin to be referenced should be mentioned.
| |image14|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Configure Plugin DLL Tab for Mute No Slew module


| The assembly information of this particular module can be mentioned under Assembly Information. At the bottom right corner of this tab, there is an option to Generate the DLL file for this particular module. Choose the path where the DLL needs to be saved as per the developer’s requirement and click save.

1.1.11 Including generated DLL to SigmaStudioPlus Add-ins
---------------------------------------------------------

Open Tools-> Add-ins Browser.


|image15|

.. container:: centeralign

   \ **Figure:** SigmaStudioPlus Add-ins Browser


In Add-ins Browser, click the '+' to add the path of the recently created ‘.dll’ files as shown in below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.



|image16|

.. container:: centeralign

   \ **Figure:** Adding DLL file


| Upon creating a new project, when it comes to adding audio processing modules from Toolbox tree, a separate section called **Custom Modules** can be seen, under which the recently created Mute No Slew module will be present.
| |image17|

.. container:: centeralign

   \ **Figure:** SigmaStudioPlus Schematic Design with Custom created Mute (No Slew) module


| 
| ===== 1.2 Simple Adder Module ===== Please refer section :doc:`1.1.1 Configuration Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`, the procedure is same.
| |image18|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Configuration Tab for Simple Adder


.. note::

   The **Advanced Customization** (Custom UI & Custom Code) options are advanced configuration settings and not be used in the regular designer flow. Developers can contact the support team for more information regarding this configuration.


.. _source-and-libraries-tab-1:

1.2.1 Source and Libraries Tab
------------------------------

For SimpleAdder, we are giving the C source code directly in Algorithm Designer’s editor under “Source Code” tab as shown in below :doc:`figure </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`.


|image19|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Source and Libraries Tab, Source Code window for Simple Adder


The ‘Header Files’ tab is used to load the header files included in the source code. Header files to be added can be selected using ‘Browse’ button and added using the '+' button as shown below.



|image20|

.. container:: centeralign

   \ **Figure:** Algorithm Designer Module Source and Libraries Tab, Header Files window for Simple Adder


| Use the ‘-’ button to remove the selected header file from the list.
| The header file added in this Simple Adder module can be found in **C:\\Analog Devices\\SigmaStudioPlus-Rel2.x.x\\Target\\Include** path. The source entered in the editor and header files selected will get saved in the Algorithm Designer project. Source code entered in the Algorithm Designer Module’s source editor is not supported for sample processing schematics.

| Rest of the procedure is same. Hence please refer the following sections to create the module as per your module's logic and generate DLL:
| :doc:`1.1.3 Parameter Definition Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.4 I/O Pins Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.5 Variables Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.6 Memory Size Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.7 Parameter Assignment Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.8 UI Designer Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.9 Settings Tab </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.10 Configuring Plugin DLL and its Generation </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`
| :doc:`1.1.11 Including generated DLL to SigmaStudioPlus Add-ins </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/custommodulecreation>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/algodesigner.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/algdesigner_help.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/srclib_embdlib.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/srclib_reflib.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/paramdef.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/io_init.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/io_final.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/variablestab.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/memtab.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/paramassign.png
.. |image11| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/ui_1.png
.. |image12| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/ui_2.png
.. |image13| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/settings_2.png
.. |image14| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/dll_generation.png
.. |image15| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/addinbrowser.png
.. |image16| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/addinbrowser_2.png
.. |image17| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/muteinschema.png
.. |image18| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/simpleadderconfig.png
.. |image19| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/simpleaddersource.png
.. |image20| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule/simpleadderheader.png
