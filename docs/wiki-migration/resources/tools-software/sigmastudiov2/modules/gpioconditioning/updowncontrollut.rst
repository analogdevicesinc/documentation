:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Up Down Control LUT
===================

| |up_down_lut_ssp.jpg|
| ===== Description =====
| This block takes in two inputs, one up and one down, and uses them to generate an index for a lookup table. The starting index is pre-loaded into an interface register and the up/down inputs increment or decrement the value.
| ===== Usage =====
| \* Drag the block into your schematic.

-  Connect the red control inputs to GPIOs that have been conditioned by Push and Hold, or to the outputs of the Rotary Encoder.
-  Connect the yellow input pin to an Interface Read block.
-  Connect the yellow output to an Interface Write block, with the same register selected for both the interface read and write blocks.
-  The output will be the value in the table corresponding to the index.

| 
| ===== Targets Supported =====

+---------------------+------------+-----------------------+---------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=====================+============+=======================+===============+==================+
| Up Down Control LUT | NA         | NA                    | S             | NA               |
+---------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

+--------+---------+-------------------------------------------------------------------------------------+
| Name   | Type    | Description                                                                         |
+========+=========+=====================================================================================+
| Input0 | Control | increment input (up)                                                                |
+--------+---------+-------------------------------------------------------------------------------------+
| Input1 | Control | decrement input (down)                                                              |
+--------+---------+-------------------------------------------------------------------------------------+
| Input2 | Logic   | Connected to a software interface register - reads the last stored value at startup |
+--------+---------+-------------------------------------------------------------------------------------+

Output
------

+---------+---------+---------------------------------------------------------------------------+
| Name    | Type    | Description                                                               |
+=========+=========+===========================================================================+
| Output0 | Control | Output signal                                                             |
+---------+---------+---------------------------------------------------------------------------+
| Output1 | Logic   | Connected to a software interface register - writes the last output value |
+---------+---------+---------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                                                                                                                                                                                                                     |
+====================+===============+================+==========================================================================================================================================================================================================================================================================================================================================+
| ByPassEnable       | disable       | enable/disable | bypasses the LUT value looked up                                                                                                                                                                                                                                                                                                         |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NoOfTableValues    | 33 pts        | [2, 800]       | Sets the table size: the  number of points used in the volume table curve.                                                                                                                                                                                                                                                               |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableValues        | 1             | [-16, 15.99]   | The table points are the actual gain values for the volume curve in linear representation. Although the range supports the full values of [-16, 15.99] the table values should generally be between [0, 1] for proper gain adjustments. The user has full control in this table to add a linear, logarithmic of custom gain volume curve |
+--------------------+---------------+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------------------------------------------------+-------------------+
| Parameter Name | Description                                                                    | ADAU145x/ADAU146x |
+================+================================================================================+===================+
| maxindex       | maxnumber of table points                                                      | Integer32         |
+----------------+--------------------------------------------------------------------------------+-------------------+
| table_p0       | All the points in the table are written to the DSP in their linear gain format | FixPoint8d24      |
+----------------+--------------------------------------------------------------------------------+-------------------+

| 
| ===== DSP Parameter Computation =====
| Not applicable

.. |up_down_lut_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/up_down_lut_ssp.jpg
