`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

Parameter Address Calculation
=============================

IIR Filters
-----------

| Coefficient arrangement in SHARC memory of IIR fitters is different for Type 1 and Type 2 filters.
| Type1 Cascaded 3 stage filter
| |image1|
| Type 1 Filter, nth stage (where n is 1, 2 or 3 for 3 stage cascaded filter)
| <fc #cd5c5c>\ *b2*\ </fc> -> GenSecOrderFiltBlk1<fc #cd5c5c>\ *2B*\ </fc>n -> c[n-1][0]
| <fc #cd5c5c>\ *b1*\ </fc> -> GenSecOrderFiltBlk1<fc #cd5c5c>\ *1B*\ </fc>n -> c[n-1][1]
| <fc #cd5c5c>\ *b0*\ </fc> -> GenSecOrderFiltBlk1<fc #cd5c5c>\ *0B*\ </fc>n -> c[n-1][2]
| <fc #cd5c5c>\ *a2*\ </fc> -> GenSecOrderFiltBlk1<fc #cd5c5c>\ *2A*\ </fc>n -> c[n-1][3]
| <fc #cd5c5c>\ *a1*\ </fc> -> GenSecOrderFiltBlk1<fc #cd5c5c>\ *1A*\ </fc>n -> c[n-1][4]
| Type2 Cascaded 3 stage filter
| |image2| Type 2 Filter, nth stage (where n is 1, 2 or 3 for 3 stage cascaded filter)
| b’0 -> GenSecOrderFilt<fc #cd5c5c>\ *T2*\ </fc>Blk10Bn -> c[4*number of stages]
| b’1 -> GenSecOrderFilt<fc #cd5c5c>\ *T2*\ </fc>Blk11Bn -> c[n-1][3]
| b’2 -> GenSecOrderFilt<fc #cd5c5c>\ *T2*\ </fc>Blk12Bn -> c[n-1][2]
| a’1 -> GenSecOrderFilt<fc #cd5c5c>\ *T2*\ </fc>Blk11An -> c[n-1][1]
| a’2 -> GenSecOrderFilt<fc #cd5c5c>\ *T2*\ </fc>Blk12An -> c[n-1][0]
| For Type2 IIR, b0 coefficient is same for all the stages. The offset values for b0 is the same for all the stages.
| ^Implementation ^0B^ 1B^ 2B^ 1A^ 2A^

+--------+--------------------------------------+-------------+-------------+----------+----------+
| Type 1 | b0                                   | b1          | b2          | -a1      | -a2      |
+--------+--------------------------------------+-------------+-------------+----------+----------+
| Type 2 | Product of b0 of all cascaded stages | b1’ = b1/b0 | b2’ = b2/b0 | a1’ = a1 | a2’ = a2 |
+--------+--------------------------------------+-------------+-------------+----------+----------+

| Table 4: Filter Coefficient Computation
| Parameter arrangement of Type1 cascaded filters in memory
| |image3|
| |image4|
| |image5|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_eq1.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_eq2.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_7.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_8.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller/hostcontroller_9.jpg
