Parameter Update
================

| :doc:`Click here to return to the Basic DSP section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| The parameter update block allows user to update the module's parameter value dynamically. The selected parameters are updated with the value coming from the input pins.
| |image1|
| ===== Input Pins =====

+-------------------+------------------------------------+-----------------------------------------------+
| Name              | Format [int/dec] - [control/audio] | Function Description                          |
+===================+====================================+===============================================+
| Pin 0: Input Data | decimal - control                  | Value to be updated in the selected parameter |
+-------------------+------------------------------------+-----------------------------------------------+

| 
| ===== Output Pins ===== NA
| ===== Grow Algorithm ===== The module support the algorithm growth up to 16. The input pin will be added for each algorithm instance and user has to select the parameter for all the algorithm instances. If parameter is not selected for any of the instance then the module will not update any parameter.
| ===== Configurations ===== The selection of the parameter will be enabled only when the schematic compilation is completed successfully. The user can select the module for which the parameter needs to be updated. After selecting the module, the parameter within the module should be selected for which value should be updated. The value of the selected parameter will be updated with the given input value for each sample once the schematic is downloaded. User can also change the parameter selection when the schematic is downloaded. It will start updating the newly selected parameter once the parameter selection window is closed.

| 
| ==== Parameter Selection for ADAU145x ====
| |image2|
| The selection window lists the parameters of the modules used in the ADAU145x schematic. It allows user to select the parameters from DM0 or DM1.
| ==== Parameter Selection for ADAU144x ==== |image3|
| The selection window lists the parameters of the modules used in the ADAU144x schematic. It allows user to select the parameters from Coefficient or Nonmodulo data.

Parameter Selection for ADSP-SC5XX/ADSP-215xx
---------------------------------------------

After adding the module. Press 'Link compile connect' once to ensure all the addresses are proper. Then click on the select button to open the following window.

| 
| |image4|

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

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/parameterupdate.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/selectparam.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/selectparamadau144x.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/paramreadwnd.jpg
