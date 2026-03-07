Indirect Parameter Access Table (IPAT) (ADAU146X, ADAU145X, ADAU144X)
=====================================================================

| :doc:`Click here to return to the Using SigmaStudio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| The address of a particular parameter might be changing when new modules are inserted or deleted from the schematic. In some cases, a fixed address is need for a particular parameter irrespective of the changes in the schematic to avoid the need to recompile (and therefore re-validate) micro-controller code. The "Indirect Parameter Access Table" provides a mechanism to maintain a fixed address for selected set of parameters within a schematic.

| This feature can be accessed by right clicking on the IC as shown below. This option is first enabled once a schematic is first compiled. The feature is supported in SigmaStudio 3.13 or above. It is currently supported for the ADAU144x, ADAU145x, and ADAU146x families of SigmaDSP processors.
| This feature allows microcontroller (uC) code to not need to be generated concurrently to a DSP image (Program Memory / Parameter memory). Instead users can develop their uC code independently from the DSP program/parameters being used. Such DSP image can be later placed separate in a known location in EEPROM (or flash) for it to be downloaded by the uC. Doing this will allow independent loading of the DSP schematic without the need to affect the uC code that deals with non-static run-time changes.

.. important::

   Please note that worst-case cycles used by IPAT is not displayed by the output window. It depends on the maximum number of coefficients updated at a time through IPAT. Approximately 10 \* Max(Number of Loads)


| |image1|
| |image2|
| =====GUI Controls=====

+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value          | Range                     | Function Description                                                                                                                |
+==================+========================+===========================+=====================================================================================================================================+
| Table Length     | 5                      | 5 - 1000                  | Number of Parameters in the Table                                                                                                   |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Indirect Address | NA                     | NA                        | Indirect Address to access the parameter. This address is maintained as a fixed value irrespective of any changes in the schematic. |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Module           | NA                     | NA                        | Lists the modules in the schematic                                                                                                  |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Parameter        | NA                     | NA                        | Lists the parameters for the selected module.                                                                                       |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Param Address    | NA                     | NA                        | Actual Parameter Address in the Schematic. This might change when there are changes in the schematic                                |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Format           | 8.24/5.23              | 8.24/5.23/32.0/28.0       | Fixed point format of the parameter                                                                                                 |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Value            | 0                      | Changes depends on Format | Value to be written for the parameter/ Value Read back from the target                                                              |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Enable Read      | false                  | true/false                | To enable the readback for a particular parameter.                                                                                  |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Start Address    | First Indirect Address | Indirect Address range    | Start address for the indirect parameter access                                                                                     |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Number of Loads  | 1                      | Table Length              | Number of sequential loads to be performed from the 'Start Address'                                                                 |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Update           | NA                     | NA                        | Updates the indirect parameter and writes the same to the target                                                                    |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Write            | NA                     | NA                        | Updates the single indirect parameter and writes the single parameter to the target                                                 |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Defragment       | NA                     | NA                        | Defragments the table reordering the table                                                                                          |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Page             | 1                      | 1-100                     | change page option                                                                                                                  |
+------------------+------------------------+---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

| 
| =====Usage===== Indirect Parameter Access Table Can be configured using the following steps.

-  Right-click the target DSP in the Hardware Configuration tab and select \`Advanced Framework Configurations\`. Ensure that the \`Enable 'Indirect Parameter Access Table' and 'Fixed SafeLoad Address'\` and \`Indirect Parameter Access Table to Handle the multiple memory pages\` are checked.


|image3|

   |image4|
-  Link and compile the schematic. This will create a mapping between parameters and DSP memory addresses.
-  Select the 'Indirect Parameter Access Table' option from the IC context menu in the Hardware Configuration window.
-  Update the table by selecting the module, the parameter and the format in the window.
-  To enable readback for a particular parameter check the 'Enable Read' checkbox corresponding to the parameter.
-  Link and compile again to generate code and data with the 'Indirect Parameter Access table' included.

-  Note that any change in the Table requires recompilation.
-  Additional schematic parameters (for example, from a newly added module) will be available in the Indirect Parameter Access Table after recompilation.

Writing the Parameter
---------------------

Follow the steps below to initiate the load using Write option in the SigmaStudio GUI.

-  Update 'Values' column in the 'Indirect Parameter Access Table' window.
-   Click on the Write Button to initiate load

| 
| |image5|

Follow the steps below to initiate the load using Update option in the SigmaStudio GUI.

-  Update 'Values' column in the 'Indirect Parameter Access Table' window.
-  Modify 'Start Address' to the indirect address of the parameter to be loaded.
-  Modify 'Number of Loads and Triggers' to the number of consecutive loads to be done.
-  Press Update to initiate the load.

| 
| |image6|
| A write or update will cause the corresponding value boxes to be highlighted in green.

| 
| Follow the steps below to initiate the load form the external microcontroller.

-  Write the value to the indirect address of the parameter.
-  Write the indirect address to the 'start_address' register.
-  Write the number of parameters to 'num_of_loads_and_trigger' register.

| (e.g.):
| Lets assume the following Indirect Parameter Table. |image7|
| To write the 5 filter coefficients from micro-controller.

-  Write the Filter coefficient values to addresses starting from 24585 to 24589 from the micro-controller.
-  Write the value 24585 (Indirect Address of Filter coefficients) to 'start_address' register. (Address of 'start_address' register can be found export files)
-  Write value 5 (Number of coefficients) to 'num_of_loads' register. (This operation will initiate the copying of parameter values from indirect address to the actual parameter address)

| 

Reading the Parameter
---------------------

| Note that read will work only if the 'Enable Read' button is checked for the particular parameter before the compilation. The parameter values are copied from the actual address to the indirect address (Fixed address) after processing every sample. So the parameter value read has maximum of 1 sample delay.
| Follow the steps below to initiate the read using SigmaStudio GUI.

-  Enable Read is checked.
-  Press the Read button corresponding to the parameter.

| 
| |image8|
| Follow the steps below to initiate the read from the external microcontroller.

-  Read the value from the indirect address of the parameter.

**Note:** Write will not work for a parameter when read is enabled. To implement both write and read of a same parameter, two separate indirect addresses should be used as shown below.

| 
| Here same 'gain' parameter from 'Single1' module is mapped to two indirect addresses, 24585 and 24586. Indirect address 24585 can be used to read gain parameter and 24586 can be used to write the parameter.

Export Files
------------

| The address of 'start_address' and 'num_of_loads' registers can be found from the export files. Indirect Parameter Access Table is placed after the SafeLoad data. Export file also contains all the indirect addresses defined.
| |image9|

Context Menu Options
--------------------

Parameters can be added to the indirect parameter access table by right clicking on the modules after compilation.


|image10|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/indirectparamtable1.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_gui.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/advanced_framework_config_menu.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/advanced_framework_config_options.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_gui_write.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_gui_update.png
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_write_example.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_read.png
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ipat_export.png
.. |image10| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/indirectparam.jpg
