:doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

Block Scalar Addition(ADAU145x)
===============================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaradd.png
   :align: center

Scalar Addition is a block processing module which adds a constant scalar value to each of the input samples in block of input samples

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaraddcell.png
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
| Pin 0: Output | decimal-audio- audio                     | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

Grow Algorithm
--------------

The module supports growth functionality, the number of channels to the module can be grown. Add is not supported.

GUI Controls
------------

+------------------+---------------+-------------+------------------------------------------------------------+
| GUI Control Name | Default Value | Range       | Function Description                                       |
+==================+===============+=============+============================================================+
| Scalar           | 1             | -128-127.99 | Scalar Value used for addition with input block of samples |
+------------------+---------------+-------------+------------------------------------------------------------+

| 
| ===== DSP Parameter Information =====

================ =========================== =========================
GUI Control Name Compiler Name               Function Description
================ =========================== =========================
Scalar           ScalarAdditionBlkAlg1Scalar Scalar Value for Addition
================ =========================== =========================


| Here,

-   Green - Algorithm Name
-   Red - Instance Number (Changes for each instance)
-   Blue - Parameter Name

Algorithm Description
---------------------

This module adds the scalar value specified in the textbox to each of the input samples in an input block.

Example
-------

In the example shown below, scalar value 110 is added to each of the DC block input samples of value 10

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/basicdsp/scalaraddexample.png
   :align: center

Supported IC's
--------------

1. ADAU145x
