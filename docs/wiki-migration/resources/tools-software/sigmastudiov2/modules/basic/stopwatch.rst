:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Stop Watch
==========

| 
| |stopwatchext.png| |stopwatchwreset.png|

Description
-----------

| The StopWatch block is used to know how long something takes (i.e. how many samples have passed between start and stop event). A control signal greater than zero to Start pin triggers the Stopwatch counter, While the control signal to Stop pin is zero. A control signal greater than zero to Stop pin stops the counter increment regardless of the control signal to the Start pin. Reset button(pin for External Reset, the control signal is high) resets the counter value to zero.
| ===== Variants =====

-  StopWatch
-  StopWatchExtReset

| 
| ===== Targets Supported =====

+-------------------+------------+------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+==================+===============+==================+
| StopWatch         | B/S        | B/S              | S             | NA               |
+-------------------+------------+------------------+---------------+------------------+
| StopWatchExtReset | B/S        | B/S              | S             | B                |
+-------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+------------------------------------+---------+-------------------------------------------------------------------+
| Name                               | Type    | Description                                                       |
+====================================+=========+===================================================================+
| Start                              | Audio   | Starts the counter of the stop watch                              |
+------------------------------------+---------+-------------------------------------------------------------------+
| Stop                               | Audio   | Stops the counter of the stop watch                               |
+------------------------------------+---------+-------------------------------------------------------------------+
| Reset (Only for StopWatchExtReset) | Control | Resets the counter of the stop watch (only for StopWatchExtReset) |
+------------------------------------+---------+-------------------------------------------------------------------+

Output
~~~~~~

====== ======= =========================
Name   Type    Description
====== ======= =========================
Output Control Stop Watch counter output
====== ======= =========================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+-------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                  |
+====================+===============+==============+=======================================================+
| Reset              | False         | True / False | Resets the counter value to zero (Only for StopWatch) |
+--------------------+---------------+--------------+-------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                            | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+========================================================+========================+===============+
| Reset          | Resets the counter result to zero (Only for StopWatch) | Float                  | FixPoint8d24  |
+----------------+--------------------------------------------------------+------------------------+---------------+

| 

.. |stopwatchext.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/stopwatchext.png
.. |stopwatchwreset.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/stopwatchwreset.png
