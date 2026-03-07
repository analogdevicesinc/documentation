:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Toggle Counter
==============

| 
| |toggle_counter_ssp.jpg|
| ===== Description =====
| The Toggle Counter cell counts the number of edges seen on its input pin and outputs the count as a 32.0 integer value. The toggle detection can be set to detect rising or falling edges on the input.
| ===== Usage =====
| The toggle counter increments an internal counter each time an edge is detected on the input. Two algorithms exist: one for detecting and counting rising edges, and one for detecting and counting falling edges.

The rising edge counter starts at zero when the program begins. Each time the input detects a rising edge - in any number format - the counter will increment. After the counter exceeds the maximum count value (which can be configured in the GUI), it will reset to zero and resume counting again.

| The falling edge counter starts at zero when the program begins. Each time the input detects a falling edge - in any number format - the counter will increment. After the counter exceeds the maximum count value (which can be configured in the GUI), it will reset to zero and resume counting again.
| ===== Targets Supported =====

+----------------+------------+-----------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+=======================+===============+==================+
| Toggle Counter | NA         | NA                    | S             | NA               |
+----------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

+--------+---------+------------------------------------------------------------------------------------+
| Name   | Type    | Description                                                                        |
+========+=========+====================================================================================+
| Input0 | Control | Control Signal input that is detected by the toggle counter                        |
+--------+---------+------------------------------------------------------------------------------------+
| Input1 | Logic   | Connected to a software interface register - reads the last count value at startup |
+--------+---------+------------------------------------------------------------------------------------+

Output
------

+---------+---------+------------------------------------------------------------------------------------------------------+
| Name    | Type    | Description                                                                                          |
+=========+=========+======================================================================================================+
| Output0 | Control | Toggle count. Increments by one each time a new edge is detected on the input.                       |
+---------+---------+------------------------------------------------------------------------------------------------------+
| Output1 | Logic   | Other - interface register. Connected to a software interface register - writes the last count value |
+---------+---------+------------------------------------------------------------------------------------------------------+

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                                                                              |
+====================+===============+============+===================================================================================================+
| Gain               | 3             | 3 to 100   | Sets the toggle count at which the counter resets to zero                                         |
+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+
| IsLin              | true          | true/false | Setting this value to true indicates the gain is a decimal value, else the value is entered in dB |
+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------------------------------------------------------------------------------------+-------------------+
| Parameter Name | Description                                                                                                 | ADAU145x/ADAU146x |
+================+=============================================================================================================+===================+
| max            | The maximum value that the counter can reach. When the counter exceeds this value, it will be reset to zero | FixPoint8d24      |
+----------------+-------------------------------------------------------------------------------------------------------------+-------------------+

| 
| ===== DSP Parameter Computation =====
| if IsLin ==true max= Gain else max = 10^ (Gain/20)

.. |toggle_counter_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/toggle_counter_ssp.jpg
