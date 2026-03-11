FIR Filter Pool
===============

:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


| The FIR Filter Pool module is an enhanced version of the standard FIR filter allowing users to select an input and a FIR coefficient set and route the selected input through the coefficient set to a particular output. It also enables the user to invert the output and reverse the coefficient set. The module also enables the user to define custom filter and input labels using the filter pool form. |

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| |image1| |image2|

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/gui_fir_pool1.png
   :width: 500px

Input Pins
----------

+--------------+------------------------------------------+-----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description        |
+==============+==========================================+=============================+
| Pin 0: Input | decimal(ADAU145x)- audio                 | Input signal to be filtered |
|              | float(214xx) - audio                     |                             |
+--------------+------------------------------------------+-----------------------------+

Output Pins
-----------

+---------------+------------------------------------------+----------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description |
+===============+==========================================+======================+
| Pin 0: Output | decimal(ADAU145x)- audio                 | The filtered output  |
|               | float(214xx) - audio                     |                      |
+---------------+------------------------------------------+----------------------+

Grow Algorithm
--------------

The module supports growth functionality. Add is not supported.

GUI Controls
------------

+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name           | Default Value | Range    | Function Description                                                                                                                                                                              |
+============================+===============+==========+===================================================================================================================================================================================================+
| Tap Size                   | 10            | 10-10000 | This pre/post scalar determines the number of taps of the FIR filter                                                                                                                              |
+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Selection Combo box  | 0             | 0-31     | This pre/post scalar determines the selected input for a particular output                                                                                                                        |
+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Selection Combo box | 0             | 0-15     | This pre/post scalar determines the selected FIR filter coefficient set for a particular output                                                                                                   |
+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reverse Selection          | 0             | 0/1      | This pre/post scalar determines the if the selected FIR filter coefficient set for a particular output is to be reversed, the set is accessed in reverse order when the tiny circle is enabled(1) |
+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Invert Selection           | 0             | 0/1      | This pre/post scalar determines the if the particular output is to be inverted, the output is inverted(-output) when the tiny circle is enabled(1)                                                |
+----------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                     | Function Description                                                                                |
+==================+===================================================================================+=====================================================================================================+
| NumFilt          | ModFirFiltPoolS300Alg1Numfilt_1(ADAU145x) FIRFiltPoolModBlkAlg1Numfilt_1(214xx)   | The Number of filter coefficient sets                                                               |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| TapSize          | ModFirFiltPoolS300Alg1TapSize_1(ADAU145x) FIRFiltPoolModBlkAlg1TapSize_1          | The Number of filter taps in each coefficient set                                                   |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| InIndx           | ModFirFiltPoolS300Alg1InIndx_1(ADAU145x) FIRFiltPoolModBlkAlg1InIndx_1(214xx)     | The selected input index                                                                            |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| FiltIndx         | ModFirFiltPoolS300Alg1FIltIndx_1(ADAU145x) FIRFiltPoolModBlkAlg1FiltIndx_1(214xx) | The Selected filter coefficient set index                                                           |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| RevIndx          | ModFirFiltPoolS300Alg1RevIndx_1(ADAU145x) FIRFiltPoolModBlkAlg1RevIndx_1(214xx)   | The Selected Reverse Index, if set(value=1), the coefficient access order for filtering is reversed |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| InvIndx          | ModFirFiltPoolS300Alg1InvIndx_1(ADAU145x) FIRFiltPoolModBlkAlg1InvIndx_1(214xx)   | The Selected Invert Index, if set(value=1), the output value is negated                             |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| FirCoeff         | ModFirFiltPoolS300Alg1FirCoeff1(ADAU145x) FIRFiltPoolModBlkAlg1FirCoeff1(214xx)   | The Selected Filter Coefficient set                                                                 |
+------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name
-   Brown - Stage number

Note: The algorithm names for different 214xx algorithms for this module are:

1.FIRFiltPoolModBlkAlg( for delay line location at outputs)

2.FIRFiltPoolIpBlkAlg(for delay line location at inputs)

Algorithm Description
---------------------

FIR Filter Pool(ADAU145x)
~~~~~~~~~~~~~~~~~~~~~~~~~

The Algorithm implements a FIR filter of order N, having N+1 filter taps. Multiple coefficient sets can be added to the module, enabling the routing of multiple inputs through multiple independent FIR filters to a given output selection line. The FIR Filter Pool form has multiple tabs each having a particular routing selection and parameters between the inputs and outputs. The algorithm implements invert functionality which inverts the output samples and Reverse which access the loaded filter coefficient set in reverse for a particular selection.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/form_fir_pool.png
   :width: 600px

The module also features options which allow the following configurations

-  The FIR filter delay line can be allocated per input channel or per output channel. Right click on the cell to select this option, by default the delay lines are maintained per input. In configurations where the number of inputs are large compared to the number of outputs, the delay lines can be maintained per output by selecting this option.
-  The FIR filter algorithm has a trade off between the memory and mips. The Optimize for MIPS/Memory option allows the algorithm to be optimized for either one of the parameters. By default the algorithm is optimized for MIPS.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_145x_module.png
   :align: left

FIR Filter Pool(ADSP-214xx, ADSP-SC5xx)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Algorithm implements a FIR filter of order N, having N+1 filter taps. Multiple coefficient sets can be added to the module, enabling the routing of multiple inputs through multiple independent FIR filters to a given output selection line. The FIR Filter Pool form has multiple tabs each having a particular routing selection and parameters between the inputs and outputs. The algorithm implements invert functionality which inverts the output samples and Reverse which access the loaded filter coefficient set in reverse for a particular selection.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/form_fir_pool.png
   :width: 600px

The module has two variants as shown below

The FIR filter delay line can be allocated per input channel or per output channel.The FIR Filter Pool module with delay line at input maintains a FIR delay line per input channel whereas the FIR filter pool module with delay line at output maintains a FIR delay line per output channel.In configurations where the number of inputs are large compared to the number of outputs, the delay lines can be maintained per output by choosing the module.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_214xx_module.png

Example
-------

The example shows The module configured to two inputs and three output channels with three independent FIR Filter coefficient sets. The three coefficients are Low pass FIR filters with cutoffs 2.4KHz,4.8kHz and 7.2KHz. The output plots for the configuration are shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/example_fir_pool_3.png
   :width: 600px

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/output_fir_pool.png
   :width: 800px

Supported IC's
--------------

1. ADAU145x 2. ADSP-214XX 3. ADSP-213xx 4. ADSP-SC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_delayline_sc58x.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_delayline_.png
   :width: 200px
