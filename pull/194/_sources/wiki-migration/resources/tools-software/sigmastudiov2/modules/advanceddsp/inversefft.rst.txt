:doc:`Click here to return to the Advanced DSP page </wiki-migration/resources/tools-software/sigmastudiov2/modules/advanceddsp>`

Inverse FFT
===========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/advanceddsp/ifft.png
   :alt: ifft.png

Description
-----------

IFFT
~~~~

| N-point IFFT is performed on the samples, where MaxN is configurable and should be a power of greater than or equal to N mentioned in the preceding FFT. The twiddle coefficients are calculated within the code and input of IFFT are PCMx samples, the BlockSize of which 3 \* Schematic BlockSize. The first Schematic Block Size number of samples in a PCMx input contains the header information carried from the previous Module (say in this case FFT). Only when the PCMx type matches, IFFT is performed and output is given as PCM samples. The header information contains fields such as PCMx type (Windowing done), N, Count (if N>Schematic BlockSize).
| ===IFFT Windowed=== In the Windowed version, windowing is done in the FFT Module for 2N samples. Overlap and add for N samples are done at the IFFT end. Hence the output is delayed by N samples. Since memory size depends on the value of MaxN, downloading the Schematic (Link-Compile-Download) is necessary when MaxN value is changed.
| === Real IFFT === Real IFFT is a block processing module which computes the IFFT of real signals.
| === Complex IFFT === Complex IFFT is a block processing module which performs N point complex IFFT of the input signal, where N stands for BlockSize.
| ===== Variants =====

-  IFFT
-  IFFT Windowed
-  Real IFFT
-  Complex IFFT

| 
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
IFFT          NA         B                NA            B
IFFT Windowed NA         B                NA            B
Real IFFT     NA         NA               B             NA
Complex IFFT  NA         NA               B             NA
============= ========== ================ ============= ================

| 
| ===== Pins =====

Input
^^^^^

====== ======= =============================================
Name   Type    Description
====== ======= =============================================
Input0 PCMx    First Input channel (IFFT and IFFT Windowed)
Input0 PCMx    Second Input channel (IFFT and IFFT Windowed)
Input  Audio   Input channel (Real IFFT)
Input  Complex Input channel (Complex IFFT)
====== ======= =============================================

Output
^^^^^^

======= ===== ==============================================
Name    Type  Description
======= ===== ==============================================
Output0 Audio First Output channel (IFFT and IFFT Windowed)
Output0 Audio Second Output channel (IFFT and IFFT Windowed)
Output  Audio Output channel (Real IFFT and Complex IFFT)
======= ===== ==============================================

| 
| ===== Configurable Parameters =====

+---------------+---------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter | Default | Range     | Function Description                                                                                                                                                           |
+===============+=========+===========+================================================================================================================================================================================+
| Max N         | 64      | 16 - 1024 | Max N-point IFFT to be performed. This should be value greater than "N" mentioned in the preceding FFT Module. This parameter is required by the Module for memory allocation. |
+---------------+---------+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-------+----------------------------------+------------------------+---------------+
| Name  | Description                      | ADSP-214xx/215xx/SC5xx | ADAU145x/146x |
+=======+==================================+========================+===============+
| Max N | Max N-point IFFT to be performed | Integer                | NA            |
+-------+----------------------------------+------------------------+---------------+
