2D Index Lookup Table
=====================

| :doc:`Click here to return to the Level Detectors Lookup Tables </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables>`

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| This block functions like the :doc:`Index Lookup Table </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/indexlookuptable>`, except now there is a matrix of values in the table. The size of the table is user determined. There are two inputs, one for the Y index and one for the X index. | |2dlookup1.png| |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

| 
| Here is an example of a 4x4 table.
| |2dlookup2.png|

Description: For this algorithm, the inputs are the index value X(column) and index value Y(row) into the LUT. By default the module expect the index to be in integer format 32.0. [0][0] will index the first value in the table. The default output format is fractional 8.24.

There are two versions of this algorithm.

-  With Limit Protection: Checks if the index at the input is greater than the maximum index and, if so, indexes the last value in the table. Similarly, if the index is below zero, it will select the first value in the table.
-  Without Limit Protection: It does not compare the index to max and min index values.

.. |2dlookup1.png| image:: https://wiki.analog.com/_media/2dlookup1.png
.. |2dlookup2.png| image:: https://wiki.analog.com/_media/2dlookup2.png
