| :doc:`Click here to return to the Frequency Domain page </wiki-migration/resources/tools-software/sigmastudio/toolbox/frequencydomain>`

FFT with Windowing
==================

| 
| This Module performs N-point FFT on PCM samples with Windowing. The FFT Output is given in the form of PCMx samples, the Blocksize of which is 3 \* Schematic BlockSize.The first Schematic Block Size number of samples in a PCMx output contains the header information to be carried on to the next Module (say in this case IFFT). The header information contains fields such as PCMx type (to indicate Windowing), N.Since memory size depends on the value of N, downloading the Schematic (Link-Compile-Download) is necessary when N value is changed.
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

+--------------+-----+------------+---------------------------------------------------------------------+
| FFT Size (N) | 64  | 16 to 1024 | Size of the FFT(Should be a power of 2,greater than or equal to 16) |
+--------------+-----+------------+---------------------------------------------------------------------+
| Alpha        | 0.1 | 0.1 to 0.9 | Alpha in the Raised Cosine window function                          |
+--------------+-----+------------+---------------------------------------------------------------------+

| 
| ====DSP Parameter Information====

+------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                         | Function Description                                          |
+==================+=======================================================================================+===============================================================+
| FFT Size         | <fc #008000>Ext_FFTProc_Algo_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>N</fc>        | FFT Size                                                      |
+------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------+
| InvWS            | <fc #008000>Ext_FFTProc_Algo_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>InvWS</fc>    | Used for Calculating window coefficients                      |
+------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Inv1MinA         | <fc #008000>Ext_FFTProc_Algo_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Inv1MinA</fc> | Needed for IFFT to get back the orginal signal based on Alpha |
+------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Alpha            | <fc #008000>Ext_FFTProc_Algo_SC5xxAlg</fc><fc #ff0000>1</fc><fc #000080>Alpha</fc>    | Alpha in the Raised Cosine window function                    |
+------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

| 
| ==== Algorithm Description ==== The input samples to the module are windowed first using a Raised cosine Window. IFFT is computed after the windowing for 2N samples where N corresponds to the Size set in the GUI. The twiddle coefficients are calculated within the code and output is given as PCMx samples.

| 
| ==== Supported ICs ====

-  ADSP215xx
-  ADSPSC5xx

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftwindow.jpg
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/frequencydomain/fftwindowconfig.jpg
   :width: 100px
