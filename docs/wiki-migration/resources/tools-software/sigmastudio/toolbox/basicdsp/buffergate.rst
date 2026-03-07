Buffer Gate
===========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| -------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| The Buffer Gate is a logic block that takes any input and compares the value to 0. If the input signal is zero, the output will be zero. If the input is non-zero, the output will be a "1" in the bit position designated by the drop-down box. This is the opposite output result as the Zero Comparator block. This block is not an audio buffer; this block follows the gate logic of a buffer which acts as a double inversion. | |buffergatepic1.png| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

Input Pins
----------

+--------------+------------------------------------+----------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description             |
+==============+====================================+==================================+
| Pin 0: Input | any - any                          | The input signal to compare to 0 |
+--------------+------------------------------------+----------------------------------+

Output Pins
-----------

+---------------+------------------------------------+------------------------------------------------------------+
| Name          | Format [int/dec] - [control/audio] | Function Description                                       |
+===============+====================================+============================================================+
| Pin 0: Output | int - control                      | The output signal of 0 or 1 in the designated bit position |
+---------------+------------------------------------+------------------------------------------------------------+

GUI Controls
------------

+------------------------+---------------+--------------+---------------------------------------------------------------------------------------------+
| GUI Control Name       | Default Value | Range        | Function Description                                                                        |
+========================+===============+==============+=============================================================================================+
| Output Bit Designation | 28            | [28.0 Bit26] | Sets bit position of the output "1" flag. 28.0 is the default values which represents 1LSB. |
+------------------------+---------------+--------------+---------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name       | Compiler Name     | Function Description                                                                                                         |
+========================+===================+==============================================================================================================================+
| Output Bit Designation | BufferAlg1output1 | Actual value written to DSP from the representation of the drop-down menu to select the bit position of the output "1" flag. |
+------------------------+-------------------+------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The following table shows what the data output value will be for given input values, based on the selection from the Drop Down Display.

================== ================= ===================
Input Pin Value    Drop Down Display Output Pin Value
================== ================= ===================
0                  Any Selection     0x00 0x00 0x00 0x00
Any non-zero Value 28                0x00 0x00 0x00 0x01
Any non-zero Value Bit: 1            0x00 0x00 0x00 0x02
Any non-zero Value Bit: 2            0x00 0x00 0x00 0x04
Any non-zero Value Bit: 3            0x00 0x00 0x00 0x08
...                ...               ...
Any non-zero Value 5.23              0x00 0x80 0x00 0x00
Any non-zero Value Bit: 24           0x01 0x00 0x00 0x00
Any non-zero Value Bit: 25           0x02 0x00 0x00 0x00
Any non-zero Value Bit: 26           0x04 0x00 0x00 0x00
================== ================= ===================

Example
-------

| The following schematic image shows both the Buffer and the :doc:`Zero Comparator </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/zerocomparator>` for a non-zero and zero input. There results of the algorithm are captured in the :doc:`DSP Readback </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadback>` cell.
| |buffergatepic2.png|

Algorithm Details
-----------------

========================== ========================================
Toolbox Path               Basic DSP - Logic - Invert - Buffer
Cores Supported            ADAU144x
                           ADAU176x
                           ADAU178x
                           ADAU170x
                           AD1940
"Grow Algorithm" Supported yes - see Algorithm Growth Information
"Add Algorithm" Supported  yes - see Algorithm Addition Information
Subroutine/Loop Based      no
Program RAM                4\*
Data RAM                   1\*
Parameter RAM              1\*
========================== ========================================

Algorithm Growth Information
----------------------------

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Description              | When the Buffer algorithm is grown, a new pair of input/output pins is added to the control. The algorithm behavior is the same, and the drop-down menu selection applies to all the input signal comparisons. | |buffergatepic3.png| |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Program RAM Repetition   | 4 per growth                                                                                                                                                                                                   |                      |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Data RAM Repetition      | 1 per growth                                                                                                                                                                                                   |                      |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Parameter RAM Repetition | 0                                                                                                                                                                                                              |                      |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

Algorithm Addition Information
------------------------------

+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Description              | When the Buffer algorithm is added, a new control is stacked vertically. The newly added drop-down menu selection applies to the newly added input/output pair. | |buffergatepic4.png| |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Program RAM Repetition   | 4 per add                                                                                                                                                       |                      |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Data RAM Repetition      | 2 per add                                                                                                                                                       |                      |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+
| Parameter RAM Repetition | 1 per add                                                                                                                                                       |                      |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+

.. |buffergatepic1.png| image:: https://wiki.analog.com/_media/buffergatepic1.png
.. |buffergatepic2.png| image:: https://wiki.analog.com/_media/buffergatepic2.png
.. |buffergatepic3.png| image:: https://wiki.analog.com/_media/buffergatepic3.png
.. |buffergatepic4.png| image:: https://wiki.analog.com/_media/buffergatepic4.png
