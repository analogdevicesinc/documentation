Parameter Read
==============

| :doc:`Click here to return to the Basic DSP. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module can be used to read any parameter in the schematic and get the value in the output pin.
| |image1|

Input Pins
----------

| None
| ===== Output Pins =====

+---------------+------------------------------------+---------------------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description                        |
+===============+====================================+=============================================+
| Pin 0: Output | float- control                     | Read parameter value is sent as float value |
+---------------+------------------------------------+---------------------------------------------+

| 

Grow Algorithm
--------------

| Not supported
| ===== Configurations ===== After adding the module. Press 'Link compile connect' once to ensure all the addresses are proper. Then click on the select button to open the following window.

| 
| |image2|

+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value  | Range          | Function Description                                                                                          |
+==================+================+================+===============================================================================================================+
| Block Name       | Not Applicable | Not Applicable | Name of the module in the schematic                                                                           |
+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| Parameter Name   | Not Applicable | Not Applicable | Name of the parameter in the selected module.                                                                 |
+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| Address          | 0              | Not Applicable | Address of the parameter. If the user wants to enter the address directly click on the checkbox and change it |
+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| Offset           | 0              | Not Applicable | This offset is added to the address, then that is used as the address to read the parameter from              |
+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+
| Data Type        | float          | float/int      | Data type of the parameter.                                                                                   |
+------------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+-------------------------------------------------------------------------+--------------------------+
| GUI Control Name | Compiler Name                                                           | Function Description     |
+==================+=========================================================================+==========================+
| Address          | <fc #008000>ParamReadAlg</fc><fc #ff0000>1</fc><fc #000080>Address</fc> | Address of the parameter |
+------------------+-------------------------------------------------------------------------+--------------------------+
| offset           | <fc #008000>ParamReadAlg</fc><fc #ff0000>1</fc><fc #000080>Offset</fc>  | Offeset from address     |
+------------------+-------------------------------------------------------------------------+--------------------------+
| type             | <fc #008000>ParamReadAlg</fc><fc #ff0000>1</fc><fc #000080>Type</fc>    | 0 - float, 1- int        |
+------------------+-------------------------------------------------------------------------+--------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

Supported ICs
-------------

-  SC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/paramread.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/paramreadwnd.jpg
