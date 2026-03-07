DSP Parameter Read
==================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| \|\| This module can be used to read any parameter/array of parameter values from schematic. Also it can write the read values to the file periodically.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspparamread.jpg
   :align: center

Input Pins
----------

| None
| ===== Output Pins ===== None

Grow Algorithm
--------------

| The module currently does not support grow/add functionality.
| ===== Configurations ===== The DSP param readback module contains controls to initiate single read/continuous read. |image1|

+------------------------+---------------+-------+---------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name       | Default Value | Range | Function Description                                                                                                                        |
+========================+===============+=======+=============================================================================================================================================+
| Read Button            | -             | -     | Click on this button to initiate single read.                                                                                               |
+------------------------+---------------+-------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Continuous Read Circle | -             | -     | Click on this circle to initiate continious read. This will be visible only if the continuous read is enabled in the readback configuration |
+------------------------+---------------+-------+---------------------------------------------------------------------------------------------------------------------------------------------+

| After Link Compile Download right click on the module then select 'Configure...' to configure the parameter read options. After configuring, press read button/continuous read circle to initiate the read.
| |image2|
| |image3|
| ^GUI Control Name^Default Value^Range^Function Description^

+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Block Name                           | -           | All the modules name in the current schematic                   | Lists all the modules in the current schematic.                                                                                |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                       | -           | All the parameter in the module selected in 'Block Name' field. | Lists all the parameter in the module selected in 'Block Name' field.                                                          |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Address Enable Checkbox              | Not Checked | Checked/Not Checked                                             | Enables the address field editable. When address field is editable 'Block Name' and 'Parameter Name' fields can not be edited. |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Address                              | -           | -                                                               | Address from which the data to be read from the target.                                                                        |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Parameter Length                     | 1           | 1-65536                                                         | Number of values to be read from the parameter Address.                                                                        |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Enable Continuous Read Back Checkbox | Not Checked | Checked/Not Checked                                             | Enables the continuous readback button in the module                                                                           |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Readback Period                      | 500 ms      | 500 - 2000 ms                                                   | Period at which read back to be initiated in continuous reaback mode                                                           |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Output File Enable Checkbox          | Not Checked | Checked/Not Checked                                             | Enables the output file write option.                                                                                          |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Output File                          | -           | -                                                               | File to which the data to be written.                                                                                          |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| File Write Duration                  | 1           | 1-5                                                             | Duration for which file write operation occurs.                                                                                |
+--------------------------------------+-------------+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

**Notes:**

-  Output file write is supported only if the continuous read is enabled.
-  Once the file write is completed the continuous read will be stopped.
-  Any change in the schematic requires a new Link compile download for the updated parameters to appear in the configuration window.

Supported ICs
-------------

-  ADAU145x
-  213xx
-  214xx
-  SC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspparamcell.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspparamreadcontext.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/dspparamreadform.jpg
