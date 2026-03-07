:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Index LookUp Table
==================

| 
| |lookuptable.png| |indexlookupstandard.png|
| |lookuptableeditor.png|

Description
-----------

| The Index Lookup Table block lets you access values stored in a lookup table (LUT). They're accessible through a table index input pin.
| For this algorithm, the input is the index value into the LUT. By default the module expect the index to be in integer format (32.0 or 28.0 depends on the SigmaDSP). The input format can be changed to fractional (8.24 depends on the SigmaDSP) by clicking the Green color circle in the module. Zero (0) will index the first value in the table. Recompiling is required when the input format is changed.

Usage
-----

click Table to open the Table Editor window. There are two ways to enter values:

-  Enter them directly and use Save table value.
-  Use Load table value to load data from a file.

The first option lets you enter maximum value(s).

Variants
--------

-  Index Look-Up Table
-  Index Look-Up Table Standard
-  Log Look-Up Table

Targets Supported
-----------------

+------------------------------+------------+------------------+---------------+------------------+
| Name                         | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+==============================+============+==================+===============+==================+
| Index LookUp Table           | B/S        | B/S              | NA            | B                |
+------------------------------+------------+------------------+---------------+------------------+
| Index Look-Up Table Standard | NA         | NA               | S             | NA               |
+------------------------------+------------+------------------+---------------+------------------+
| Log Look-Up Table            | NA         | B                | S             | B                |
+------------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

========== ======= =============================
Name       Type    Description
========== ======= =============================
TableIndex Control Used to access the LUT values
========== ======= =============================

Output
~~~~~~

======= ======= =============================
Name    Type    Description
======= ======= =============================
Output0 Control LUT value for the Table index
======= ======= =============================

| 
| ===== Configurable Parameters =====

+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value       | Range            | Function Description                                                                   |
+====================+=====================+==================+========================================================================================+
| NoOfTableValues    | 33                  | 2 to 800         | Controls the Maximum lookup table values. Change in this value requires re-compilation |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| IsDB               | False               | True / False     | Controls the tables values either be in linear or dB                                   |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| TableValues        | All 33 values are 1 | -                | Table Values                                                                           |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| Fixed Address      | False               | True / False     | Enable or disable the Fixed Address mode(only in Log LUT for ADSP-215xx/SC5xx)         |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| IntegerInput       | Enable              | Enable / Disable | Input index format (Only for Index Look-Up Table Standard)                             |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+
| IntegerOutput      | Disable             | Enable / Disable | Output data format (Only for Index Look-Up Table Standard)                             |
+--------------------+---------------------+------------------+----------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------+------------------------+---------------+
| Parameter Name | Description              | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==========================+========================+===============+
| MaxIndex       | Size of the table values | Float                  | FixPoint8d24  |
+----------------+--------------------------+------------------------+---------------+
| TableValues    | Table values             | Float                  | FixPoint8d24  |
+----------------+--------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== MaxIndex = NoOfTableValues - 1

.. |lookuptable.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/lookuptable.png
.. |indexlookupstandard.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/indexlookupstandard.png
.. |lookuptableeditor.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/lookuptableeditor.png
