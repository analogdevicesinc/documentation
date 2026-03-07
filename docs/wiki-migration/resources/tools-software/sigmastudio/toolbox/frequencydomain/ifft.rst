Real IFFT(ADAU145x)
===================

| :doc:`Click here to return to the Frequency Domain page </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`
| |image1|
| Real IFFT is a block processing module which computes the IFFT of real signals

Input Pins
----------

+----------------------+------------------------------------------+----------------------------+
| Name                 | Format [int/dec/float] - [control/audio] | Function Description       |
+======================+==========================================+============================+
| Pin 0: Complex Input | Complex-audio                            | Input signal to the module |
+----------------------+------------------------------------------+----------------------------+

Output Pins
-----------

+-------------------+------------------------------------------+-------------------------------+
| Name              | Format [int/dec/float] - [control/audio] | Function Description          |
+===================+==========================================+===============================+
| Pin 0:Real Output | Decimal-audio                            | Output signal from the module |
+-------------------+------------------------------------------+-------------------------------+

Grow Algorithm
--------------

| Add and Growth are not supported.

DSP Parameter Information
-------------------------

+----------------------------------------+---------------------------+----------------------+
| GUI Control Name                       | Compiler Name             | Function Description |
+========================================+===========================+======================+
| splitCoeffsA(Globally defined in FFT)) | RealFFTBlkAlgsplitCoeffsA | Sine coefficients    |
+----------------------------------------+---------------------------+----------------------+
| splitCoeffsB(Globally defined in FFT)  | RealFFTBlkAlgsplitCoeffsB | Cosine coefficients  |
+----------------------------------------+---------------------------+----------------------+

Algorithm Description
---------------------

| This module computes the IFFT for Real input signals. IFFT is computed from the first half of the FFT output, using the complex conjugate symmetry properties of the FFT output, of real signals.

Example
-------

| In the example shown below, IFFT of the FFT output of a real signal is computed, to retrieve the original signal back in time domain.
| |image2|

Supported IC's
--------------

| 1. ADAU145x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/ifft.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/ifftexample.png
   :width: 500px
