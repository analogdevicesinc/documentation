:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Chime Frequency
===============

| |chimelin.png|
| |chimelinwindow.png|

Description
-----------

The chime Frequency algorithm has fully programmable frequency envelopes. The envelopes are accessible by clicking the cell’s icon The length of the chime is controlled by the Maximum Time control, which is set in milliseconds. In Chime frequency envelope window points on the curve can be moved by click-dragging. New points can be added by double-clicking. Points can be removed by right-clicking and selecting “remove point.” In this case, the point closest to the mouse cursor will be removed. Chime Frequency window must have at least 3 points. Point values can be fine-tuned using the text input boxes on the right side of the envelope control window. When the control input goes to 1, the chime begins. When the control input goes to 0, the chime output stops, regardless of whether the envelope has completed or not.

| 
| ===== Variants =====

-  Chime FrequencyLin
-  Chime FrequencyLog

| 
| ===== Targets Supported =====

+-----------------------+------------+-----------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+=======================+===============+==================+
| Chime FrequencyLinear | B/S        | B/S                   | S             | NA               |
+-----------------------+------------+-----------------------+---------------+------------------+
| Chime FrequencyLog    | S          | S                     | S             | NA               |
+-----------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

==================== ======= =============
Name                 Type    Description
==================== ======= =============
Enable/Disable chime Control Control Input
==================== ======= =============

| 
| ==== Output ====

======= ======= ===============================
Name    Type    Description
======= ======= ===============================
Output0 Audio   chime output
Output1 Control chime end flag (only for SHARC)
======= ======= ===============================

| 
| ===== Configurable Parameters =====

+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+
| GUI Parameter Name      | Default Value | Range             | Function Description                                                          |
+=========================+===============+===================+===============================================================================+
| Maximum Time            | 1104 ms       | 10 to 4400 ms     | Time interval in ms                                                           |
+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+
| FrequencyValue_Point<n> | 80            | 20 to 20000 Hz    | Fine tuning of frequency values of points in frequency graph(<n> point count) |
+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+
| FreqTime(ms)_Point<n>   | 0             | 0 to Maximum Time | Fine tuning of time in ms of points in frequency graph(<n> point count)       |
+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-----------------+------------------------------------------------------------------+------------------------+---------------+
| Parameter Name  | Description                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================+==================================================================+========================+===============+
| Sin_c           | sine coefficient(only for ChimeFrequencyLin)                     | Integer32              | Integer32     |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| Cos_c           | cos coefficient(only for ChimeFrequencyLin)                      | Integer32              | Integer32     |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| FrequencyPoints | Time intervals of frequency points                               | Integer32              | Integer32     |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| FrequencySlope  | scales the slope of frequency points(only for ChimeFrequencyLin) | FixPoint2d62           | FixPoint2d62  |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| PhaseInc        | Phase increment(only for ChimeFrequencyLog)                      | Float                  | FixPoint8d24  |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| 2Pi             | Mathematical constant pi*2(only for ChimeFrequencyLog)           | Float                  | FixPoint8d24  |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| FrequencyRatio  | Frequency and time ratio(only for ChimeFrequencyLog)             | Float                  | FixPoint8d24  |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| SinCosTable     | combined cos and sin coefficients(only for ChimeFrequencyLog)    | Float                  | FixPoint8d24  |
+-----------------+------------------------------------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== sin_c=sin(initialFrequency[0] \* pi))
| cos_c=cos(initialFrequency[0] \* pi))
| PhaseInc=initialFrequency[0] \* 2.0 / fs

.. |chimelin.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/chimelin.png
.. |chimelinwindow.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/chimelinwindow.png
   :width: 600px
