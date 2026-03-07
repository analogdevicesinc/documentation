:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Counter
=======

| 
| |counter.png| |counterwint.png|

Description
-----------

| The Counter block can be used with a State Machine to process your input at a particular time interval, in ms. The counter starts from 0 by default or any other user-defined value if specified.
| The Counter with Interval module has 2 input pins. First input is for Start/Hold the Counter and second input is used to Reset the counter value.

Varaints
--------

::

   -Counter
   -Counter with Interval

Targets Supported
-----------------

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Counter               | B/S        | B/S              | S             | B                |
+-----------------------+------------+------------------+---------------+------------------+
| Counter with Interval | NA         | NA               | S             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+-----------------------------------------------+---------+-----------------------------+
| Name                                          | Type    | Description                 |
+===============================================+=========+=============================+
| Start / Hold (only for Counter with Interval) | Control | Counter start or hold input |
+-----------------------------------------------+---------+-----------------------------+
| Reset (only for Counter with Interval)        | Control | Counter Reset input         |
+-----------------------------------------------+---------+-----------------------------+

Output
~~~~~~

====== ================================================ ==============
Name   Type                                             Description
====== ================================================ ==============
Output Control (Only for Counter with Interval) / Audio Output channel
====== ================================================ ==============

Configurable Parameters
-----------------------

+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range          | Function Description                                                                                                                                                                                                                                                  |
+====================+===============+================+=======================================================================================================================================================================================================================================================================+
| Max                | 134217727     | 0 to 134217727 | This is the maximum value for the counter. If the counter reaches the maximum value, its output will stay at that value until it is reset. The value can be changed by clicking in the text field and typing a new value, or by clicking the adjacent up/down arrows. |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| step               | 1             | 1 to 10000     | This controls the rate at which the counter increments. The counter value will increase by the value in this field at the end of every audio sample. The value can be changed by entering the desired value in the text field or using the adjacent up/down arrows.   |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Init               | 0             | 0 to 268435456 | This is the initial value of the counter, which is the starting value for the counter when it is reset. Enter the start count value in the Init field, or use the adjacent up/down arrows.                                                                            |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reset              | False         | True / False   | Resets the counter value to initial value                                                                                                                                                                                                                             |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pause              | False         | True / False   | Starts or stops the counter increment. If the counter is stopped in mid-operation, its output value will freeze at its most recent value.                                                                                                                             |
+--------------------+---------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+-------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================================================================+========================+===============+
| Max            | This is the maximum value for the counter                                     | Float                  | FixPoint8d24  |
+----------------+-------------------------------------------------------------------------------+------------------------+---------------+
| step           | The counter value will increase by the value at the end of every audio sample | Float                  | FixPoint8d24  |
+----------------+-------------------------------------------------------------------------------+------------------------+---------------+
| Init           | This is the starting value for the counter when it is reset                   | Float                  | FixPoint8d24  |
+----------------+-------------------------------------------------------------------------------+------------------------+---------------+
| Pause          | Starts or stops the counter increment                                         | Float                  | FixPoint8d24  |
+----------------+-------------------------------------------------------------------------------+------------------------+---------------+
| Reset          | Resets the counter value to initial value                                     | Float                  | FixPoint8d24  |
+----------------+-------------------------------------------------------------------------------+------------------------+---------------+

.. |counter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/counter.png
.. |counterwint.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/counterwint.png
