:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General First Order Filter
==========================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/gfo.png
   :alt: gfo.png

Description
-----------

The General 1st-Order block allows you to design 1st-order lowpass and highpass filters.

Drag the block into the workspace and it's ready to use. As with other blocks, there's the option to increase the stage count to this algorithm. Observe, however, that with this module adding another stage the algorithm will add another frequency band to the block, which is equivalent to having two filters in series.

| To switch among highpass, lowpass, and flat, click the filter type icon. This can be done in real time, without needing to recompile the project. Enter your desired values in the text fields to set the cutoff frequency and overall gain (sometimes called scale gain) of the filter. Or click the arrows to increment values for these parameters. To increment them very quickly, click and hold.
| ==== Calculating Filter Coefficients ==== Use the following formulas to calculate the coefficients for first order filters.

Variables:

-  frequency = Cutoff frequency
-  gain = Linear Gain
-  fs = Sample Rate
-  PI = π

For lowpass filters,

-  A1 = 2.7^(-2 \* PI \* frequency/fs))
-  B0 = gain \* (1.0 - A1)
-  B1 = 0

For highpass filters,

-  A1 = e^(-2 \* PI \* frequency/fs)) where e = 2.718.....
-  B1 = (1.0 + A1) \* 0.5 \* gain
-  B0 = -B1

For allpass filters,

-  A1 = 2.7^(-2 \* PI \* frequency/fs))
-  B0 = -gain \* A1
-  B1 = gain

| 
| ===== Targets Supported =====

+---------------------+------------+------------------+---------------+------------------+
| Name                | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=====================+============+==================+===============+==================+
| General First Order | NA         | NA               | S             | NA               |
+---------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input channel
===== ===== =============

Output
~~~~~~

====== ===== =============
Name   Type  Description
====== ===== =============
Output Audio Filter Output
====== ===== =============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                                             |
+====================+===============+==============+==================================================================+
| NumStages          | 1             | 1 to 8       | Number of filter stages                                          |
+--------------------+---------------+--------------+------------------------------------------------------------------+
| Gain_StageX        | 0             | -12 to 12 dB | Gain for individual filter stage                                 |
+--------------------+---------------+--------------+------------------------------------------------------------------+
| Frequency_StageX   | 1000          | 1 to 96000   | Filter cutoff frequency of individual filter stage               |
+--------------------+---------------+--------------+------------------------------------------------------------------+
| FilterType_StageX  | 0             | 0 to 2       | LowPass/HighPass/BandPass filter type of individual filter stage |
+--------------------+---------------+--------------+------------------------------------------------------------------+
| Phase_StageX       | true          | true/false   | In phase/out of phase for individual filter stage                |
+--------------------+---------------+--------------+------------------------------------------------------------------+
| Enabled_StageX     | true          | true/false   | Filter Enabled/Bypassed for individual filter stage              |
+--------------------+---------------+--------------+------------------------------------------------------------------+

| Note : \_StageX - Refers to parameters of each stage. X represents the stage index.
| ===== DSP Parameters =====

============== ===================== =============
Parameter Name Description           ADAU145x/146x
============== ===================== =============
B0_StageX      B0 Filter Coefficient 8.24
B1_StageX      B1 Filter Coefficient 8.24
A1_StageX      A1 Filter Coefficient 8.24
============== ===================== =============

| Note: X- Stage Number (Changes for each stage coefficients)
