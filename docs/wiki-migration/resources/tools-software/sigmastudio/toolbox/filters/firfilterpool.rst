FIR Filter Pool
===============

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| \|The FIR Filter Pool module is an enhanced version of the standard FIR filter allowing users to select an input and a FIR coefficient set and route the selected input through the coefficient set to a particular output. It also enables the user to invert the output and reverse the coefficient set. The module also enables the user to define custom filter and input labels using the filter pool form.\|
| |image1| |image2|
| |image3|

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

| The module supports growth functionality. Add is not supported.
| ===== GUI Controls =====
| ^GUI Control Name^Default Value^Range^Function Description^

+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Tap Size                   | 10 | 10-10000 | This pre/post scalar determines the number of taps of the FIR filter                                                                                                                              |
+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Input Selection Combo box  | 0  | 0-31     | This pre/post scalar determines the selected input for a particular output                                                                                                                        |
+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter Selection Combo box | 0  | 0-15     | This pre/post scalar determines the selected FIR filter coefficient set for a particular output                                                                                                   |
+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Reverse Selection          | 0  | 0/1      | This pre/post scalar determines the if the selected FIR filter coefficient set for a particular output is to be reversed, the set is accessed in reverse order when the tiny circle is enabled(1) |
+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Invert Selection           | 0  | 0/1      | This pre/post scalar determines the if the particular output is to be inverted, the output is inverted(-output) when the tiny circle is enabled(1)                                                |
+----------------------------+----+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                                                                                                                                                             | Function Description                                                                                |
+==================+===========================================================================================================================================================================================================================+=====================================================================================================+
| NumFilt          | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>Numfilt</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>Numfilt</fc><fc #800000>_1</fc>(214xx)   | The Number of filter coefficient sets                                                               |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| TapSize          | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>TapSize</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>TapSize</fc><fc #800000>_1</fc>          | The Number of filter taps in each coefficient set                                                   |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| InIndx           | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>InIndx</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>InIndx</fc><fc #800000>_1</fc>(214xx)     | The selected input index                                                                            |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| FiltIndx         | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>FIltIndx</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>FiltIndx</fc><fc #800000>_1</fc>(214xx) | The Selected filter coefficient set index                                                           |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| RevIndx          | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>RevIndx</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>RevIndx</fc><fc #800000>_1</fc>(214xx)   | The Selected Reverse Index, if set(value=1), the coefficient access order for filtering is reversed |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| InvIndx          | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>InvIndx</fc><fc #800000>_1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>InvIndx</fc><fc #800000>_1</fc>(214xx)   | The Selected Invert Index, if set(value=1), the output value is negated                             |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| FirCoeff         | <fc #008000>ModFirFiltPoolS300Alg</fc><fc #ff0000>1</fc><fc #000080>FirCoeff</fc><fc #800000>1</fc>(ADAU145x) <fc #008000>FIRFiltPoolModBlkAlg</fc><fc #ff0000>1</fc><fc #000080>FirCoeff</fc><fc #800000>1</fc>(214xx)   | The Selected Filter Coefficient set                                                                 |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name
-  <fc #800000> Brown</fc> - Stage number

| Note: The algorithm names for different 214xx algorithms for this module are:
| 1.FIRFiltPoolModBlkAlg( for delay line location at outputs)
| 2.FIRFiltPoolIpBlkAlg(for delay line location at inputs)

Algorithm Description
---------------------

| 
| ====FIR Filter Pool(ADAU145x) ====

| The Algorithm implements a FIR filter of order N, having N+1 filter taps. Multiple coefficient sets can be added to the module, enabling the routing of multiple inputs through multiple independent FIR filters to a given output selection line. The FIR Filter Pool form has multiple tabs each having a particular routing selection and parameters between the inputs and outputs. The algorithm implements invert functionality which inverts the output samples and Reverse which access the loaded filter coefficient set in reverse for a particular selection.
| |image4|
| The module also features options which allow the following configurations
| \* The FIR filter delay line can be allocated per input channel or per output channel. Right click on the cell to select this option, by default the delay lines are maintained per input. In configurations where the number of inputs are large compared to the number of outputs, the delay lines can be maintained per output by selecting this option.

-  The FIR filter algorithm has a trade off between the memory and mips. The Optimize for MIPS/Memory option allows the algorithm to be optimized for either one of the parameters. By default the algorithm is optimized for MIPS.

| 
| |image5|
| ====FIR Filter Pool(ADSP-214xx, ADSP-SC5xx)==== The Algorithm implements a FIR filter of order N, having N+1 filter taps. Multiple coefficient sets can be added to the module, enabling the routing of multiple inputs through multiple independent FIR filters to a given output selection line. The FIR Filter Pool form has multiple tabs each having a particular routing selection and parameters between the inputs and outputs. The algorithm implements invert functionality which inverts the output samples and Reverse which access the loaded filter coefficient set in reverse for a particular selection.
| |image6|
| The module has two variants as shown below
| The FIR filter delay line can be allocated per input channel or per output channel.The FIR Filter Pool module with delay line at input maintains a FIR delay line per input channel whereas the FIR filter pool module with delay line at output maintains a FIR delay line per output channel.In configurations where the number of inputs are large compared to the number of outputs, the delay lines can be maintained per output by choosing the module.
| |image7|
| ===== Example =====
| The example shows The module configured to two inputs and three output channels with three independent FIR Filter coefficient sets. The three coefficients are Low pass FIR filters with cutoffs 2.4KHz,4.8kHz and 7.2KHz. The output plots for the configuration are shown below.
| |image8|
| |image9|

Supported IC's
--------------

| 1. ADAU145x
| 2. ADSP-214XX
| 3. ADSP-213xx
| 4. ADSP-SC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_delayline_sc58x.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_delayline_.png
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/gui_fir_pool1.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/form_fir_pool.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_145x_module.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/form_fir_pool.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/fir_pool_214xx_module.png
.. |image8| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/example_fir_pool_3.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/output_fir_pool.png
   :width: 800px
