:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

FIR Filter Pool
===============

| 
| |firpoolicon.png|
| |firpool.png|
| =====Description===== The Algorithm implements a FIR filter of order N, having N+1 filter taps. Multiple coefficient sets can be added to the module, enabling the routing of multiple inputs through multiple independent FIR filters to a given output selection line. The FIR Filter Pool form has multiple tabs each having a particular routing selection and parameters between the inputs and outputs. The algorithm implements invert functionality which inverts the output samples and Reverse which access the loaded filter coefficient set in reverse for a particular selection.

| The FIR filter delay line can be allocated per input channel or per output channel. The FIR Filter Pool module with delay line at input maintains a FIR delay line per input channel whereas the FIR filter pool module with delay line at output maintains a FIR delay line per output channel. In configurations where the number of inputs are large compared to the number of outputs
| ===== Targets Supported =====

+----------------+------------+------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+==================+===============+==================+
| FIR FilterPool | B          | B                | S             | B                |
+----------------+------------+------------------+---------------+------------------+

Pins
====

Input
-----

======================= ===== =================================
Name                    Type  Description
======================= ===== =================================
Input<fc #ff0000>X</fc> Audio InputChannel X to the Filter Pool
======================= ===== =================================

Output
------

======================== ===== =====================
Name                     Type  Description
======================== ===== =====================
Output<fc #ff0000>X</fc> Audio The filtered output X
======================== ===== =====================

Note:

-  <fc #ff0000>X</fc> - Channel Index

| 
| ===== Configurable Parameters =====

+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| GUI Parameter Name                                             | Default Value | Range                   | Function Description                                                                  |
+================================================================+===============+=========================+=======================================================================================+
| FilterTaps                                                     | 10            | 2 to 10000              | Specifies the number of the coefficients used for FIR filter calculation              |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| NumInputs                                                      | 2             | 1-32                    | Number of input channels. Change in Channels requires re-compilation                  |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| NumOutputs                                                     | 1             | 1-32                    | Number of output channels. Change in Channels requires re-compilation                 |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| NumFilters                                                     | 1             | 1-20                    | Number of Filters available for selection. Change in Channels requires re-compilation |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| SetCount                                                       | 1             | 1-7                     | Number of output channels. Change in Channels requires re-compilation                 |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| InputSelection_Tab<fc #ff0000>X</fc>_Output<fc #ff0000>Y</fc>  | 0             | 0 - NumInputs           | The Input selected for the Yth Output on Tab X                                        |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| FilterSelection_Tab<fc #ff0000>X</fc>_Output<fc #ff0000>Y</fc> | 0             | 0 - NumFilters          | The Filter selected for the Yth Output on Tab X                                       |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| InputSelection_Tab<fc #ff0000>X</fc>_Output<fc #ff0000>Y</fc>  | 0             | 0 - NumInputs           | The Input selected for the Yth Output on Tab X                                        |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| Reverse_Tab<fc #ff0000>X</fc>_Output<fc #ff0000>Y</fc>         | 0             | 0 or 1                  | The Reverse state for the Yth Output on Tab X                                         |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| Inverse_Tab<fc #ff0000>X</fc>_Output<fc #ff0000>Y</fc>         | 1             | 1 or -1                 | The Inverse state for the Yth Output on Tab X                                         |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| InUse_Filter<fc #ff0000>X</fc>                                 | True          | True/False              | Indicates Whether the Filter X is currently in Use                                    |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+
| Coefficients_Filter                                            | 1             | -infinity to + infinity | Coefficients used to calculate the FIR Filter for Filter X                            |
+----------------------------------------------------------------+---------------+-------------------------+---------------------------------------------------------------------------------------+

| 

.. |firpoolicon.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/firpoolicon.png
.. |firpool.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/firpool.png
   :width: 650px
