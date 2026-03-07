:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Param Read or Write
===================

| |paramread.png| |paramwrite.png|
| |paramreadpopup.png|

Description
-----------

| The parameter Read module can be used to read any parameter in the schematic and get the value in the output pin. The parameter Write block allows user to update the module's parameter value dynamically. The selected parameters are updated with the value coming from the input pins
| ===== Configuration ===== The selection of the parameter will be enabled only when the schematic compilation is completed successfully. The user can select the module for which the parameter needs to be updated/Read. After selecting the module, the parameter within the module should be selected for which value should be updated. The value of the selected parameter will be updated with the given input value for each sample once the schematic is downloaded. User can also change the parameter selection when the schematic is downloaded. It will start updating/Read the newly selected parameter once the parameter selection window is closed.

Variants
--------

-  Parameter Read
-  Parameter Write

| 
| ===== Targets Supported =====

=========== ========== ================ ============= ================
Name        ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
=========== ========== ================ ============= ================
Param Read  B          B                NA            B
Param Write B          B                NA            B
=========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

===== ======= ===================================
Name  Type    Description
===== ======= ===================================
Input Control Input Channel (Only for ParamWrite)
===== ======= ===================================

Output
~~~~~~

====== ======= ===================================
Name   Type    Description
====== ======= ===================================
Output Control Output Channel (Only for ParamRead)
====== ======= ===================================

| 
| ===== Configurable Parameters =====

+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value | Range               | Function Description                                                                              |
+===============+===============+=====================+===================================================================================================+
| Module        | NA            | NA                  | Name of the module in the schematic                                                               |
+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+
| Parameter     | NA            | NA                  | Name of the parameter in the selected module                                                      |
+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+
| Address       | 0             | NA                  | Address of the parameter. If the user wants to enter the address directly Select the Address mode |
+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+
| Mode          | Parameter     | Parameter / Address | User can select the mode                                                                          |
+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+
| Format        | Float         | Float / Int32       | Data type of the parameter                                                                        |
+---------------+---------------+---------------------+---------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================================================================================+========================+===============+
| Address        | Address of the parameter                                                                         | Integer32              | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| Offset         | This offset is added to the address, then that is used as the address to read the parameter from | Integer32              | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| Type           | Data type of the parameter                                                                       | Integer32              | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+
| BaseOffset     | Used to calculate the address                                                                    | Integer32              | NA            |
+----------------+--------------------------------------------------------------------------------------------------+------------------------+---------------+

.. |paramread.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/paramread.png
.. |paramwrite.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/paramwrite.png
.. |paramreadpopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/paramreadpopup.png
