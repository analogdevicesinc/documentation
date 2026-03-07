:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

FFT
===

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/fft.png
   :alt: fft.png

Description
-----------

.. _fft-1:

FFT
~~~

| N-point FFT is performed on the samples, where N is configurable and should be a power of 2, greater than or equal to 16. The twiddle coefficients are calculated within the code and output is given as PCMx samples, the BlockSize of which is 3 \* Schematic Block Size. The first Schematic BlockSize number of samples in a PCMx output contains the header information to be carried on to the next Module (say in this case IFFT). The header information contains fields such as PCMx type (Windowing done), N, Count (if N>Schematic BlockSize). Since memory size depends on the value of N, downloading the Schematic (Link-Compile-Download) is necessary when N value is changed.
| == FFT Windowed == In the Windowed FFT version, Raised Cosine window is used for windowing samples. Windowing is done for samples before calculating FFT and ‘overlap and add’ is done after IFFT. Here the windowing is done for 2N samples and therefore FFT done for 2N samples.
| == Real FFT == Real FFT is a block processing module which computes the FFT of real signals. It is for reduced memory and Mips.
| == Complex FFT == Complex FFT is a block processing module which performs N point complex FFT of the input signal, where N stands for BlockSize.
| ===== Variants =====

-  FFT
-  FFT Windowed
-  Real FFT
-  Complex FFT

| 
| ===== Targets Supported =====

============ ========== ================ ============= ================
Name         ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============ ========== ================ ============= ================
FFT          NA         B                NA            B
FFT Windowed NA         B                NA            B
Real FFT     NA         NA               B             NA
Complex FFT  NA         NA               B             NA
============ ========== ================ ============= ================

| 
| ===== Pins =====

Input
^^^^^

====== ===== ===========================================
Name   Type  Description
====== ===== ===========================================
Input0 Audio First Input channel (FFT and FFT Windowed)
Input1 Audio Second Input channel (FFT and FFT Windowed)
Input  Audio Input channel (Real FFT and Complex FFT)
====== ===== ===========================================

Output
^^^^^^

======= ======= ============================================
Name    Type    Description
======= ======= ============================================
Output0 PCMx    First Output channel (FFT and FFT Windowed)
Output1 PCMx    Second Output channel (FFT and FFT Windowed)
Output  Audio   Output channel (Real FFT)
Output  Complex Output channel (Complex FFT)
======= ======= ============================================

| 
| ===== Configurable Parameters =====

+----------------+----------------+-----------------------------------+-------------------------------------------------------------------------------------+
| GUI Parameter  | Default        | Range                             | Function Description                                                                |
+================+================+===================================+=====================================================================================+
| N              | 64             | 16 - 1024                         | N-point FFT to be performed. This should be value greater than 16 and a power of 2. |
+----------------+----------------+-----------------------------------+-------------------------------------------------------------------------------------+
| Alpha          | 0.1            | 0.1 - 0.9                         | alpha in the Raised cosine window function                                          |
+----------------+----------------+-----------------------------------+-------------------------------------------------------------------------------------+
| ApplyScaling   | True           | True or False                     | Whether scaling to be applied                                                       |
+----------------+----------------+-----------------------------------+-------------------------------------------------------------------------------------+
| Implementation | Mips Optimized | Mips Optimized / Memory Optimized | Implementation to choose from                                                       |
+----------------+----------------+-----------------------------------+-------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+----------+-------------------------------------------------------------------------------+------------------------+---------------+
| Name     | Description                                                                   | ADSP-214xx/215xx/SC5xx | ADAU145x/146x |
+==========+===============================================================================+========================+===============+
| N        | N-point FFT to be performed                                                   | Integer                | NA            |
+----------+-------------------------------------------------------------------------------+------------------------+---------------+
| InvWS    | 1/(2\*N - 1) needed for calculating window coefficients                       | Float                  | NA            |
+----------+-------------------------------------------------------------------------------+------------------------+---------------+
| Inv1MinA | 1/(1 - alpha) needed for IFFT to get back the original signal based on alpha  | Float                  | NA            |
+----------+-------------------------------------------------------------------------------+------------------------+---------------+
| alpha    | alpha in the Raised cosine window function                                    | Float                  | NA            |
+----------+-------------------------------------------------------------------------------+------------------------+---------------+
