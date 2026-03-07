| :doc:`Click here to return to the Frequency Domain page </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`

IFFT
====

| 
| This Module performs N-point IFFT on input samples which are in the PCMx format, the BlockSize of which is 3 \* Schematic Block Size. The first Schematic Block Size number of samples in a PCMx input contains the header information carried from the previous Module (say in this case FFT). Only when the PCMx type matches, IFFT is performed and output is given as Linear PCM samples
| |image1|
| ====Input Pins====

+--------------------+------------------------------------+----------------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description             |
+====================+====================================+==================================+
| Pin 0: Input(PCMx) | decimal - Audio                    | Frequency Domain Real Input      |
+--------------------+------------------------------------+----------------------------------+
| Pin 1: Input(PCMx) | decimal - Audio                    | Frequency Domain Imaginary Input |
+--------------------+------------------------------------+----------------------------------+

| 
| ====Output Pins====

+--------------------+------------------------------------+----------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description |
+====================+====================================+======================+
| Pin 0: Output(PCM) | decimal - Audio                    | Real PCM Output      |
+--------------------+------------------------------------+----------------------+
| Pin 1: Output(PCM) | decimal - Audio                    | Imaginary PCM Output |
+--------------------+------------------------------------+----------------------+

| 
| ==== Grow Algorithm ==== The module does not support Growth and Add
| ====Configuration====
| |image2|
| ^GUI Control Name^Default Value^Range^Function Description^

======== == ========== ================
FFT Size 64 16 to 1024 Size of the IFFT
======== == ========== ================

| 
| ====DSP Parameter Information====

+------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                  | Function Description                                                           |
+==================+================================================================================+================================================================================+
| FFT Size         | <fc #008000>Ext_BlockIFFT_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>MaxN</fc> | Size of IFFT(Should be power of 2,greater than or equal to preceding FFT Size) |
+------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== This module performs Complex IFFT on the input samples received in PCMx format. The twiddle coefficients are calculated within the code. IFFT Size should be a power of 2 and greater than or equal to the FFTSize. Link/Compile/Download is necessary whenever the IFFT Size is changed.
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/ifftstandard.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/ifftstandardconfig.jpg
   :width: 100px
