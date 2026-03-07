NLMS Adaptive Filter
====================

| :doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters>`
| The Normalized Least Mean Squares (NLMS) adaptive filter is an FIR based adaptive filter. The filter update equation is given by
| w(n+1) = w(n) +[(μ \* e(n) \* x(n)) / Eng]
| Where:

::

        w(n+1) = New filter coefficient set
        w(n) = Current filter coefficient set
        μ      = Learning rate
        x(n)  = Input signal
        e(n)  = Error  = d(n)-y(n)
        d(n)  = Desired signal
        y(n)  = Output signal
        Eng = Average energy over the duration of the filter = (1/M)*Σx(m) <sup>2</sup>      

| |image1|
| |image2|

Input Pins
----------

+--------------+------------------------------------------+----------------------------------------------------------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description                                                       |
+==============+==========================================+============================================================================+
| Pin 0: Input | Float- audio                             | Input signal to FIR filter                                                 |
+--------------+------------------------------------------+----------------------------------------------------------------------------+
| Pin 1: Input | Float- audio                             | The desired audio output signal                                            |
+--------------+------------------------------------------+----------------------------------------------------------------------------+
| Pin 2: Input | Float- control                           | Signal which indicates whether FIR filter weights are to be updated or not |
+--------------+------------------------------------------+----------------------------------------------------------------------------+

Output Pins
-----------

+---------------+------------------------------------------+---------------------------------------------------------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description                                                            |
+===============+==========================================+=================================================================================+
| Pin 0: Output | Float - audio                            | The filtered output                                                             |
+---------------+------------------------------------------+---------------------------------------------------------------------------------+
| Pin 1: Output | Float - control                          | Error Signal - Difference signal between desired signal and the filtered output |
+---------------+------------------------------------------+---------------------------------------------------------------------------------+

Grow Algorithm
--------------

| The module does not support growth and add functionality.

GUI Controls
------------

+------------------+---------------+-----------------------------------+----------------------+
| GUI Control Name | Default Value | Range                             | Function Description |
+==================+===============+===================================+======================+
| Alpha            | 0.1           | 0.000001-1.0 in steps of 0.000001 | Filter learning rate |
+------------------+---------------+-----------------------------------+----------------------+

DSP Parameter Information
-------------------------

+------------------+-----------------------------------------------------------------------------+----------------------+
| GUI Control Name | Compiler Name                                                               | Function Description |
+==================+=============================================================================+======================+
| Alpha            | <fc #008000>NLMSFiltBlkAlg</fc><fc #ff0000>1</fc><fc #000080>lms_alpha</fc> | Filter learning rate |
+------------------+-----------------------------------------------------------------------------+----------------------+

Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

Algorithm Description
---------------------

This implementation of NLMS is a block based implementation. The weight update happens at the end of every processing block. The weight update equation is given below:

| w(m+1) = w(m) + μ \* Err \* x(m) / Eng
| Where:

::

             w(m+1) = New filter coefficient set
             w(m) = Current filter coefficient set
             μ      = Learning rate
             Err = RMS error over the block duration = sqrt(∑e(n)2/N)
                 e(n) = d(n)-y(n)
                 d(n)  = Desired signal
                 y(n)  = Output signal
            x(m)  = Samples within the filter state
            Eng = Average energy over the duration of the filter = Σx(m)2/M

Note:

::

     N = Block Size and n varies over 0-(N-1)
     M = Filter tap length and m varies over 0-(M-1)
     

Supported IC's
--------------

| 1. ADSP-213xx
| 2. ADSP-214xx
| 3. ADSP-215xx
| 4. ADSP-SC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/nlms.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/filters/nlms_cell.png
   :width: 100px
