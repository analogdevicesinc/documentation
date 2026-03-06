| 
| :doc:`Click here to return to the Frequency Domain page </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`

FFT(ADSP-SC5xx/ADSP-215xx)
==========================

| 
| This Module performs N-point FFT on PCM samples. The FFT Output is given in the form of PCMx samples, the Blocksize of which is 3 \* Schematic BlockSize.The first Schematic Block Size number of samples in a PCMx output contains the header information to be carried on to the next Module (say in this case IFFT). The header information contains fields such as PCMx type (Standard - No processing done), N.
| |image1|
| ====Input Pins====

============ ================================== =====================
Name         Format [int/dec] - [control/audio] Function Description
============ ================================== =====================
Pin 0: Input decimal - Audio                    Real Audio Input
Pin 1: Input decimal - Audio                    Imaginary Audio Input
============ ================================== =====================

| 
| ====Output Pins====

+---------------------+------------------------------------+----------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description |
+=====================+====================================+======================+
| Pin 0: Output(PCMx) | decimal - Audio                    | Real FFT Output      |
+---------------------+------------------------------------+----------------------+
| Pin 1: Output(PCMx) | decimal - Audio                    | Imaginary FFT Output |
+---------------------+------------------------------------+----------------------+

| 
| ==== Grow Algorithm ==== The module does not support Growth and Add
| ====Configuration====
| |image2|

| 
| ^GUI Control Name^Default Value^Range^Function Description^

======== == ========== ===============
FFT Size 64 16 to 1024 Size of the FFT
======== == ========== ===============

| 
| ====DSP Parameter Information====

+------------------+---------------------------------------------------------------------------+----------------------+
| GUI Control Name | Compiler Name                                                             | Function Description |
+==================+===========================================================================+======================+
| FFT Size         | <fc #008000>Ext_FFTAlgo_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>N</fc> | FFT Size             |
+------------------+---------------------------------------------------------------------------+----------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== This module computes the Complex FFT of the input. Twiddle factors are computed within the module. FFT output(N Real/Imaginary samples) is packed in the PCMx format with 3 \* Schematic BlockSize number of samples. Since memory size depends on the value of N, downloading the Schematic (Link-Compile-Download) is necessary when N value is changed.
| ==== Example Schematic ==== |image3|

Shown above is an example schematic with Standard FFT/IFFT along with the PCM to PCMx and PCMx to PCM modules. FFT produces N real/imaginary samples. If the PCMx to PCM is grown to R, only the first half will have data while the remaining will have zeroes or junk data and should be ignored for processing.

\*Note: Since FFT- Window produces 2*N real/imaginary samples, all the outputs of the PCMx to PCM module will have valid data. The above schematic has to be modified to use all the outputs of PCMx to PCM for FFT with windowing.

Supported ICs
-------------

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftstandard.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftstandardconfig.jpg
   :width: 200px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftstandard_exampleschematic.jpg
   :width: 800px
