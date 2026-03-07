:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General Eq Blend
================

| 
| |generaleqblend.png|
| |genfiltsettings.png|

Description
-----------

The General (2nd-Order) block gives access to a wide variety of 2nd-order (biquad)filter algorithms.

The available filter types are:

-  Unordered List ItemOrdered List ItemParametric
-  Shelving
-  General High-Pass
-  General Low-Pass
-  General Band-Pass
-  General Band-Stop
-  Butterworth Low-Pass / High-Pass
-  Bessel Low-Pass / High-Pass
-  Tone Control
-  IIR Coefficient (direct coefficient entry)
-  1st-Order Low-Pass / High-Pass
-  All-pass
-  Peaking
-  Notch
-  Chebyshev Low-Pass / High-Pass

| 
| ===== Usage ===== To open the filter control window, click on the icon button. Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.

Targets Supported
-----------------

+----------------------+--------------------+-------------------+-------------------------------+------------------------------+
| Name                 | ADSP-214xx(Sample) | ADSP-214xx(Block) | ADSP-215xx/ADSP-SC5xx(Sample) | ADSP-215xx/ADSP-SC5xx(Block) |
+======================+====================+===================+===============================+==============================+
| General second Order | Yes                | Yes               | Yes                           | Yes                          |
+----------------------+--------------------+-------------------+-------------------------------+------------------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 
| ===== Configurable Parameters =====

================== ============= ============= ======================
GUI Parameter Name Default Value Range         Function Description
================== ============= ============= ======================
Frequency          1000          0 to 96000Hz  Cut-off frequency
Gain               0 dB          -10 to +10 dB Filter Gain
Q                  1.41          1 to 15       Q factor of the filter
================== ============= ============= ======================

| 
| ===== DSP Parameters =====

============== =========== ======================
Parameter Name Description ADSP-214xx/SC5xx/215xx
============== =========== ======================
============== =========== ======================

| 

.. |generaleqblend.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/generaleqblend.png
   :width: 200px
.. |genfiltsettings.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/genfiltsettings.png
