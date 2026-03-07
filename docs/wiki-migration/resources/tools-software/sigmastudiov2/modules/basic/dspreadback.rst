:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

DSP Readback
============

| 
| |dspreadadau.png| |readcomplex.png|

Description
-----------

The DSP Readback block lets you read values back from the DSP at any point in your schematic design. The number displayed onscreen is the data value sent back from the DSP considering all the blocks to the left of the Readback block. Every time you click Read, this value will be updated with the latest from the DSP. By displaying the output value from any block, in any format desired, Readback is used chiefly for debugging, and probably will prove very handy.

Values can be read back in either hex or decimal. For the latter, you must specify what format you want the number to be displayed in. Any changes to this format will shift the decimal value of the number displayed.

| 
| The DSP Readback(Complex) block lets you read complex values back from the DSP at any point in your schematic design.

Usage
-----

| The DSP Readback cell can be configured to read back from the target DSP repeatedly at regular intervals. To enable this mode, right-click the cell and select ReadValue.
| ===== Variants =====

-  DSP ReadBack
-  Generic DSP ReadBack
-  DSP Readback (Complex)

Targets Supported
-----------------

+------------------------+------------+------------------+---------------+------------------+
| Name                   | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+========================+============+==================+===============+==================+
| DSP Readback           | B/S        | B/S              | S             | B                |
+------------------------+------------+------------------+---------------+------------------+
| Generic DSP ReadBack   | B          | B                | NA            | B                |
+------------------------+------------+------------------+---------------+------------------+
| DSP Readback (Complex) | NA         | NA               | S             | NA               |
+------------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ======================================= ===============
Name   Type                                    Description
====== ======================================= ===============
Input0 Audio(Complex Pin for Complex ReadBack) Input Channel 0
====== ======================================= ===============

Output
~~~~~~

======= ======================================= ================
Name    Type                                    Description
======= ======================================= ================
Output0 Audio(Complex Pin for Complex ReadBack) Output channel 0
======= ======================================= ================

| 
| ===== Configurable Parameters =====

+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+
| GUI Parameter   | Default Value | Range            | Function Description                                                                |
+=================+===============+==================+=====================================================================================+
| Read Button     | NA            | NA               | Click on this 'Read' button to read the value from target                           |
+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+
| Continuous Read | Disabled      | Enable / Disable | Enable or disable the continuous read from the target                               |
+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+
| Dbl/Hex         | Dbl           | NA               | Display the read back value in hex or double                                        |
+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+
| Sample          | 1             | 1 to BlockSize   | Sample to read from the target from block of samples(Only for Generic DSP ReadBack) |
+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+
| Format          | 8.24          | 1.31 to 32.0     | This control decides the range(supports in ADAU145x/146x)                           |
+-----------------+---------------+------------------+-------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+------------------------------+------------------------+----------------+
| Parameter Name | Description                  | ADSP-214xx/SC5xx/215xx | ADAU145x/146x  |
+================+==============================+========================+================+
| Value          | Read back value from the DSP | Float                  | FixedPoint8d24 |
+----------------+------------------------------+------------------------+----------------+
| Sample         | reads the sample from target | Float                  | NA             |
+----------------+------------------------------+------------------------+----------------+

| 

.. |dspreadadau.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/dspreadadau.png
.. |readcomplex.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/readcomplex.png
