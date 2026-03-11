:doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Block Scalar Multiplication(ADAU145x)
=====================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalarmulttoolbox.png
   :align: center

Scalar Multiplication is a block processing module which multiplies scalar values specified in a table with the input block of samples.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalarmultcell.png
   :align: center

Input Pins
----------

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal-audio                            | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

Output Pins
-----------

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | decimal- audio                           | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
--------------

The module supports growth functionality, the number of channels to the module can be grown. Add is not supported.

GUI Controls
------------

+-----------------------------+------------------+---------------+------------------------------------------------------------------+
| GUI Control Name            | Default Value    | Range         | Function Description                                             |
+=============================+==================+===============+==================================================================+
| Multiplication Coefficients | 1..1[Block Size] | NA            | Scalar Value used for Multiplication with input block of samples |
+-----------------------------+------------------+---------------+------------------------------------------------------------------+
| Enable Multiplication       | Enabled          | Enable/Bypass | Decides whether Scalar Multiplication is performed or bypassed   |
+-----------------------------+------------------+---------------+------------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

+------------------+--------------------------------------------+----------------------------------+
| GUI Control Name | Compiler Name                              | Function Description             |
+==================+============================================+==================================+
| Coefficients     | ScalarMultiplicationBlkAlg1scalarmultcoeff | Scalar Values for Multiplication |
+------------------+--------------------------------------------+----------------------------------+

| 
| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This module multiplies the input block of samples with scalar values specified in the table at their respective indexes. The size of the table will be equal to the block size set for the schematic. Multiplication can be enabled or bypassed using the Enable/Bypass button present on the cell.

Example
-------

In the example shown below, block output of the DC block [1,1,1...,blocksize times] is multiplied by the scalar values in the table [1,2,3,.....,blocksize] at their respective indices.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalarmultexample.png
   :align: center

On Clicking the bypass option, the scalar values are bypassed and the input signal is passed to the output as is.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalarmultexbypass.png
   :align: center

Supported IC's
--------------

1. ADAU145x
