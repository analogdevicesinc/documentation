:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

FIR Filter
==========

| 
| |firfilt.png|
| |firfilttable.png|

Description
-----------

| The FIR Filter block lets you design any FIR filter desired.Frequency response can be shaped by specifying the appropriate coefficients.
| ===== Usage ===== This block has numeric textbox to edit the tap size for number of coefficients to be used for FIR Filter calcualtion. Click on 'table' button to open the table editor window to enter the calculated coefficients as per desired filter requirement.
| ===== Targets Supported =====

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
FIR Filter B/S        B/S              S             B
========== ========== ================ ============= ================

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-------------------------+---------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                   | Function Description                                                            |
+====================+===============+=========================+=================================================================================+
| NoOfTableValues    | 10            | 2 to 10000              | Specifies the number of the coefficients used for FIR filter calculation        |
+--------------------+---------------+-------------------------+---------------------------------------------------------------------------------+
| ByPassEnable       | False         | True/False              | Enabled/Disabled the FIR filter algorithm                                       |
+--------------------+---------------+-------------------------+---------------------------------------------------------------------------------+
| TableValues        |               | -infinity to + infinity | Coefficients used to calcualte the FIR Filter                                   |
+--------------------+---------------+-------------------------+---------------------------------------------------------------------------------+
| NumChannels        | 1             | 20                      | Number of input and output channels. Change in Channels requires re-compilation |
+--------------------+---------------+-------------------------+---------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-----------------+--------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name  | Description                                                              | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================+==========================================================================+========================+===============+
| NoOfTableValues | Specifies the number of the coefficients used for FIR filter calculation | Integer32              | Integer32     |
+-----------------+--------------------------------------------------------------------------+------------------------+---------------+
| TableValues     | Coefficients used to calcualte the FIR Filter                            | Float                  | FixPoint8d24  |
+-----------------+--------------------------------------------------------------------------+------------------------+---------------+

| 

.. |firfilt.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/firfilt.png
.. |firfilttable.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/firfilttable.png
