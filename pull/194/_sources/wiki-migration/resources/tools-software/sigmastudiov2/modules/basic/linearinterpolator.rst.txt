:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Linear Interpolator
===================

| |interpolator.png|
| |lippopup.png|

Description
-----------

The Linear Interpolator maps an input function to a set of data points that are stored in an index table. If the input function does not align exactly with a table point, the output value will be approximated using a linear interpolant, or a line drawn between the two closest points on the index table. Linear interpolation is a common calculation for a variety of computing applications such as computer graphics. In SigmaStudio, it can be used to make an input-to-output transfer function for audio or control signals without requiring many table points or calculations

| 
| The linear interpolation cell performs interpolation of a data set. The input of the linear interpolation cell must lie between a set minimum and maximum value. The input values between the min and max input values are mapped linearly to an index number between 0 and n, with n representing the maximum index. For example, if input = min, then index 0 is selected. If input = max, then index n is selected. If the input lies halfway between two indices, then the output will be the average of the two corresponding points in the data set.

Targets Supported
-----------------

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| LinearInterPolator | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

======================= ===== ===============
Name                    Type  Description
======================= ===== ===============
Input<fc #ff0000>X</fc> Audio Input Channel X
======================= ===== ===============

Output
~~~~~~

======================== ===== ================
Name                     Type  Description
======================== ===== ================
Output<fc #ff0000>X</fc> Audio Output Channel X
======================== ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+
| GUI Parameter | Default Value   | Range                      | Function Description                                                                               |
+===============+=================+============================+====================================================================================================+
| NumChannels   | 1               | 1 to 24                    | Number of channels. Applicable to Nx1 modules. Change in this value requires re-compilation        |
+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+
| Max           | 5               | -15.99 to 15.99            | The maximum allowable input value. For full-scale audio, use 1                                     |
+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+
| Min           | -0.06           | -15.99 to Max values 15.99 | The minimum allowable input value. For full-scale audio, use -1.                                   |
+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+
| Points        | 5               | 2 to 100                   | The number of points in the linear interpolation function                                          |
+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+
| Table         | [1, 2, 3, 4, 5] | -16 to 15.9999999          | The points in the linear interpolation function. The input signal will be mapped to this data set. |
+---------------+-----------------+----------------------------+----------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-----------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                               | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===========================================================+========================+===============+
| Maximum        | The maximum allowable input value                         | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------+------------------------+---------------+
| Minimum        | The minimum allowable input value                         | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------+------------------------+---------------+
| Points         | The values of points in the linear interpolation function | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------+------------------------+---------------+
| Q              | Q Factor                                                  | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------+------------------------+---------------+
| Number         | The number of points in the linear interpolation function | NA                     | FixPoint8d24  |
+----------------+-----------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

| Number = (Number of points - 1.0) \* 2^-24
| Q = 1.0 / (Max- Min)
| MinQ = Min \* Q

.. |interpolator.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/interpolator.png
.. |lippopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/lippopup.png
