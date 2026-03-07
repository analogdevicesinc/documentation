Standard Cubic
==============

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| The Standard Cubic block is a soft clipper that uses a cubic function to clip the level of the input signal. As the input signal reaches the clip threshold, the algorithm rounds the edges for a smoother clipped output. | |image2| |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

Input Pins
----------

+--------------+------------------------------------+----------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description       |
+==============+====================================+============================+
| Pin 0: Input | decimal - audio                    | Input signal to be clipped |
+--------------+------------------------------------+----------------------------+

Output Pins
-----------

============= ================================== =======================
Name          Format [int/dec] - [control/audio] Function Description
============= ================================== =======================
Pin 0: Output decimal - audio                    The soft-clipped output
============= ================================== =======================

GUI Controls
------------

+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range    | Function Description                                                                                                                                                                                                                 |
+==================+===============+==========+======================================================================================================================================================================================================================================+
| Alpha            | 1             | 0.1 - 10 | This pre/post scalar determines the amount of clipping that will occur. Although this influences the threshold value of the clipper, this is not the value at which clipping occurs. [See the function in the Algorithm Description] |
+------------------+---------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name       | Function Description                                                                                                                                                                                                                                                                   |
+==================+=====================+========================================================================================================================================================================================================================================================================================+
| Alpha            | SoftClipAlg1alpha   | When the Alpha value is changed in the GUI window, two parameters are downloaded to the DSP. The alpha value is written directly to the DSP as well as the inverse 1/alpha is written to the DSP. Both values need to be written in order to ensure proper operation of the algorithm. |
|                  | SoftClipAlg1alpham1 |                                                                                                                                                                                                                                                                                        |
+------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Note: There are other fixed parameters used for this algorithm, but they do not need to be updated when the alpha value is changed.

Algorithm Description
---------------------

The Standard Cubic block clips portions of signal voltages according to a cubic soft clip function. The pre/post scalar alpha makes the soft clip more or less severe. This block limits the range of the output signal according to the following formulas:

| 
| |image3|
| Thus for the default value of Alpha = 1, the signal range will be from [-2/3, 2/3]. Changing the value of alpha will affect the output range of the signal. The following graphs show the relationship between changing values of alpha and obtaining different signal ranges.

| 
| |image4|

Example
-------

The following image shows the Soft Clipper, being compared to a Hard Clipper and also the direct signal coming from the Inputs. A stereo switch mux allows for selection of the processing type, and then the signals are routed to the Outputs.

| 
| |image5|
| The Hard Clipper and Soft Clipper are set with corresponding Alpha and threshold values so that their clip behavior occurs at the same time. However, you will notice in the following output comparison graph, the Soft Clipper has rounded smoother edges on the output where clipping begins to occur which has a more pleasing auditory effect.

| 
| |image6|

Algorithm Details
-----------------

+----------------------------+---------------------------------------------------------------+
| Toolbox Path               | Non Linear Processors - Clippers - Soft Clip - Standard Cubic |
+----------------------------+---------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                      |
|                            | ADAU176x                                                      |
|                            | ADAU178x                                                      |
+----------------------------+---------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                        |
+----------------------------+---------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                            |
+----------------------------+---------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                            |
+----------------------------+---------------------------------------------------------------+
| Program RAM                | 21\*                                                          |
+----------------------------+---------------------------------------------------------------+
| Data RAM                   | 2\*                                                           |
+----------------------------+---------------------------------------------------------------+
| Parameter RAM              | 5\*                                                           |
+----------------------------+---------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Description              | When the SoftClip algorithm is grown, an extra pair of input/output pints is added to the control. The same Alpha parameter affects the clipping on grown Input pins. | |image8| |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Program RAM Repetition   | 21 per growth                                                                                                                                                         |          |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Data RAM Repetition      | 1 per growth                                                                                                                                                          |          |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Parameter RAM Repetition | none                                                                                                                                                                  |          |
+--------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic001.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic001.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic002.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic003.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic004.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic005.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocesses/standardcubic006.jpg
