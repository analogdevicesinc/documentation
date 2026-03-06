Toggle Counter
==============

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`
| --------------------------------------------------------------------------------------------------------------

+---+---+
| The Toggle Counter cell counts the number of edges seen on its input pin and outputs the count as a 28.0 integer value. The toggle detection can be set to detect rising or falling edges on the input. | GUI Icon\ |image2| |
+---+---+

Input Pins
----------

+-----------------------------+------------------------------------+------------------------------------------------------------------------------------+
| Name                        | Format [int/dec] - [control/audio] | Function Description                                                               |
+=============================+====================================+====================================================================================+
| Pin 0: Detection Input      | integer or decimal - control       | Control Signal input that is detected by the toggle counter                        |
+-----------------------------+------------------------------------+------------------------------------------------------------------------------------+
| Pin 1: Interface read input | other - interface register         | Connected to a software interface register - reads the last count value at startup |
+-----------------------------+------------------------------------+------------------------------------------------------------------------------------+

Output Pins
-----------

+-------------------------------+------------------------------------+--------------------------------------------------------------------------------+
| Name                          | Format [int/dec] - [control/audio] | Function Description                                                           |
+===============================+====================================+================================================================================+
| Pin 0: Toggle count           | integer - control                  | Toggle count. Increments by one each time a new edge is detected on the input. |
+-------------------------------+------------------------------------+--------------------------------------------------------------------------------+
| Pin 1: Interface write output | other - interface register         | Connected to a software interface register - writes the last count value       |
+-------------------------------+------------------------------------+--------------------------------------------------------------------------------+

GUI Controls
------------

+------------------+---------------+----------+-----------------------------------------------------------+
| GUI Control Name | Default Value | Range    | Function Description                                      |
+==================+===============+==========+===========================================================+
| N/A              | 3             | 3 to 100 | Sets the toggle count at which the counter resets to zero |
+------------------+---------------+----------+-----------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+--------------------+--------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name      | Function Description                                                                                         |
+==================+====================+==============================================================================================================+
| N/A              | ToggleCountAlg1max | The maximum value that the counter can reach. When the counter exceeds this value, it will be reset to zero. |
+------------------+--------------------+--------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The toggle counter increments an internal counter each time an edge is detected on the input. Two algorithms exist: one for detecting and counting rising edges, and one for detecting and counting falling edges. In this description, the rising edge algorithm is used as a model.

| The counter starts at zero when the program begins. Each time the input detects a rising edge - in any number format - the counter will increment. After the counter exceeds the maximum count value (which can be configured in the GUI), it will reset to zero and resume counting again. The example below shows a rising edge detection toggle counter with a maximum count of 9. Note that since the counting begins at zero, the resulting "staircase" output repeats itself every 10 rising edges.
| |image3|
| In the example below, the maximum count value is set at 100. The count er will reset after 101 rising edges have been detected on the input.
| |image4|
| Edge detection is done on a sample-by-sample basis. If the current sample exceeds the previous sample, it will be treated as a rising edge, regardless of if the input is really an edge or not.

| The example below illustrates this. This is not recommended for a real application of the algorithm. In real applications, input signals should take on only two values, such as logic switches or square waves.
| |image5|

Example
-------

| This example shows a Toggle Counter counting a 50 Hz square wave's rising edges. Note that the counter starts at zero, so in this case the counter will go from 0 to 99, resetting every 100 rising edges. Since there are 50 rising edges per second, the Toggle Counter will reset itself to zero once every 2 seconds.
| |image6|
| Other cells used in this example - :doc:`Square Wave </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/squarewave>`, :doc:`Interface Read </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/interfaceread>`, :doc:`Interface Write </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/interfacewrite>`, :doc:`DSP ReadBack </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadback>`

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------------------------------------------+
| Toolbox Path               | GPIO Conditioning - PushButton - Index Counter - Rising Edge / Falling Edge - Toggle Counter |
+----------------------------+----------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                                                     |
|                            | ADAU1701                                                                                     |
|                            | ADAU1761                                                                                     |
|                            | ADAU1781                                                                                     |
+----------------------------+----------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+
| Program RAM                | 14                                                                                           |
+----------------------------+----------------------------------------------------------------------------------------------+
| Data RAM                   | 4                                                                                            |
+----------------------------+----------------------------------------------------------------------------------------------+
| Parameter RAM              | 1                                                                                            |
+----------------------------+----------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_gui_icon.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_gui_icon.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_example_1.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_example_2.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_example_3.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/gpioconditioning/toggle_counter_example.jpg
