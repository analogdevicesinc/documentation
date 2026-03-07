FFT(ADAU145x)
=============

| 
| :doc:`Click here to return to the Frequency Domain page </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`
| There are two kinds of FFT Algorithms
| 1.Complex FFT
| 2.Real FFT

Complex FFT
-----------

Complex FFT is a block processing module which performs N point complex FFT of the input signal, where N stands for BlockSize.

| 
| |image1|

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
| Pin 0: Output | complex-audio                            | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

| 
| ===== Grow Algorithm ===== Add and Growth are not supported.
| ===== GUI Controls =====
| No Dsp parameters.
| ===== Context Menu=====
| Right-click on the module to open the context menu window. By default, "Normalize Input(Global Setting)" is Enabled. This is a global setting which determines whether the input is normalized. Click on this to enabled/disabled the "Normalize Input(Global Setting)" option. This leads to re-compile the project.
| |image2|
| ===== Algorithm Description =====
| This module computes the Complex FFT of Real input Signals and generates complex FFT output. Output blocksize is double the input Blocksize for this module.
| ===== Example ===== In the example shown below, complex magnitude of the FFT outputs of Inputs 1 and 2 are computed.
| |image3|

Real FFT
========

| Real FFT is a block processing module which computes the FFT of real signals.It is for reduced memory and Mips.
| |image4|
| ===== Input Pins =====

+--------------+------------------------------------------+----------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description       |
+==============+==========================================+============================+
| Pin 0: Input | decimal-audio                            | Input signal to the module |
+--------------+------------------------------------------+----------------------------+

.. _output-pins-1:

Output Pins
-----------

+---------------+------------------------------------------+-------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description          |
+===============+==========================================+===============================+
| Pin 0: Output | complex-audio                            | Output signal from the module |
+---------------+------------------------------------------+-------------------------------+

| 
| ===== Context Menu =====
| Right-click on the module to open the context menu window. By default, "Normalize Input(Global Setting)" is Enabled. This is a global setting which determines whether the input is normalized. Click on this to enabled/disabled the "Normalize Input(Global Setting)" option. This leads to re-compile the project.

| Right-click on the module to open the context menu window, Click on the file type, two options Mips optimized and Memory optimized will be displayed.Select Mips optimized for Mips optimmized algorithm and Select Memory optimized for Memory optimized Algorithm. Change of FFT type leads to re-compile the project.
| |image5|
| ===== Grow Algorithm ===== Add and Growth are not supported.
| ===== DSP Parameter Information =====

================ ============= ====================
GUI Control Name Compiler Name Function Description
================ ============= ====================
================ ============= ====================

Real FFT - Memory optimized:-

== ============ ===================
NA splitCoeffsA Sine coefficients
NA splitCoeffsB Cosine coefficients
== ============ ===================

Real FFT - Mips optimized:-

== ================================================ ===================
NA splitCoeffsA<fc #008000>N<fc #ff0000>*</fc></fc> Sine coefficients
NA splitCoeffsB<fc #008000>N<fc #ff0000>*</fc></fc> Cosine coefficients
== ================================================ ===================

| 
| <fc #9400d3>Note:</fc>N stands for BlockSize/2
| ===== Algorithm Description ===== This module computes the Real FFT of Real input signals for reduced memory and Mips. Since FFT of real signals has complex conjugate symmetry, only first half of the FFT output is computed. Input and output Blocksizes are the same for this module.

| 

Example
-------

| In the example shown below, complex magnitude of the FFT outputs of Real Inputs 1 and 2 are computed.
| |image6|

Supported IC's
--------------

| 1. ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fft_cell.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/context_menurealfft.png
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftexample.png
   :width: 500px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/realfft_cell.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/context_menurealfft.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftexample.png
   :width: 500px
