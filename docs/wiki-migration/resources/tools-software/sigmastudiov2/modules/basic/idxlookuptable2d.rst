:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

2D Index LookUp Table
=====================

| 
| |lut2d.png|
| |lut2dpopup.png|

Description
-----------

| The Index Lookup Table block allows you to access values stored in a lookup table (LUT). The table contains a matrix of values, with its size determined by the user. It has two inputs: one for the X index and one for the Y index. Click ‘OpenGrid’ to open the Table Editor window. Values can be entered in linear and dB scale. Table values can be saved to and restored from file using "Save Table" and "Load Table" options on the table editor.
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Index LookUp Table 2D | B          | B                | S             | B                |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ======= ===================
Name   Type    Description
====== ======= ===================
IndexX Control Input X index value
IndexY Control Input Y index value
====== ======= ===================

| 
| ==== Output ====

======= ======= ===========
Name    Type    Description
======= ======= ===========
Output0 Control Table value
======= ======= ===========

| 
| ===== Configurable Parameters =====

================== ============= ======= ==============================
GUI Parameter Name Default Value Range   Function Description
================== ============= ======= ==============================
Index X            1             1 to 15 Number of columns of the table
Index Y            1             1 to 15 Number of rows of the table
================== ============= ======= ==============================

| 
| ===== DSP Parameters =====

============== ================= ====================== =============
Parameter Name Description       ADSP-214xx/SC5xx/215xx ADAU145x/146x
============== ================= ====================== =============
MaxIndex Y     Number of Rows    Integer32              Integer32
MaxIndex X     Number of Columns Integer32              Integer32
TableArray     Table values      Float                  FixPoint8d24
============== ================= ====================== =============

| 

.. |lut2d.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/lut2d.png
.. |lut2dpopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/lut2dpopup.png
