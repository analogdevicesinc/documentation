:doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudiov2/modules/adialgorithms>`

General Second Order Coefficient Calculation
============================================

| |gsocoeffcalc.png|
| ===== Description ===== General Second Order Coefficient Calculation module is functionally similar to :doc:`General 2nd Order Filter </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters/generalsecondorder>`. They both share the configurable parameters and pins. The difference lies in the computation of biquad filter coefficients. In General 2nd Order Filter, the coefficients are computed on the host and the computed biquad coefficients are used by the algorithm running on target to perform filtering. On the other hand, in General Second Order Coefficient Calculation module, the coefficient computation is also handled by the algorithm running on the target.

Following are the supported filter types:

-  Parametric
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  All-pass
-  Peaking
-  Notch
-  Chebyshev Low-Pass / High-Pass

| 
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| GSP Coeff Calculation | NA         | NA               | S             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

| 
| ===== DSP Parameters =====

+-------------------------------------+--------------------------------+----------------+
| Parameter Name                      | Description                    | ADAU145x/146x  |
+=====================================+================================+================+
| FREQ_DSP_CALC<stage index>          | Frequency of the stage         | Integer Format |
+-------------------------------------+--------------------------------+----------------+
| Q_DSP_CALC<stage index>             | Q factor of the stage          | 8.24 Format    |
+-------------------------------------+--------------------------------+----------------+
| GAIN_DSP_CALC<stage index>          | Gain of stage                  | 8.24 Format    |
+-------------------------------------+--------------------------------+----------------+
| ONE_BY_FS_DSP_CALC<stage index>     | 1/FS                           | 8.24 Format    |
+-------------------------------------+--------------------------------+----------------+
| FILTER_TYPE<stage index>            | Filter Type index of the stage | Integer Format |
+-------------------------------------+--------------------------------+----------------+
| INVERT<stage index>                 | Whether phase inverted         | Integer Format |
+-------------------------------------+--------------------------------+----------------+
| BOOST<stage index>                  | Boost of the stage             | 8.24 Format    |
+-------------------------------------+--------------------------------+----------------+
| MEM_SELECTION_DSP_CALC<stage index> | Memory selection               | Integer Format |
+-------------------------------------+--------------------------------+----------------+
| ADDRESS_DSP_CALC<stage index>       | Parameter address              | Integer Format |
+-------------------------------------+--------------------------------+----------------+

.. |gsocoeffcalc.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/gsocoeffcalc.png
