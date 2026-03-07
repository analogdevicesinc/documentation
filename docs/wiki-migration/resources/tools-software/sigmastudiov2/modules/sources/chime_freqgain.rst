:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Chime FreqGain
==============

| |chimefreqgain.png|
| |image1|
| |image2|

Description
-----------

The chime algorithm has fully programmable frequency and gain envelopes. The envelopes are accessible by clicking the cell’s icon The length of the chime is controlled by the Maximum Time control, which is set in milliseconds.

The envelope control window has two tabs: Frequency and Gain. Points on the curve can be moved by click-dragging. New points can be added by double-clicking. Points can be removed by right-clicking and selecting “remove point.” In this case, the point closest to the mouse cursor will be removed. Each envelope must have at least 3 points. Point values can be fine-tuned using the text input boxes on the right side of the envelope control window. When the control input goes to 1, the chime begins. When the control input goes to 0, the chime output stops, regardless of whether the envelope has completed or not.

| In the case of the Chime Freq – Gain Continuous Play algorithm, the envelope will loop continuously until the control input goes to 0
| ===== Targets Supported =====

+----------------+------------+------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+==================+===============+==================+
| Chime FreqGain | S          | S                | S             | NA               |
+----------------+------------+------------------+---------------+------------------+

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

======= ======= ==============
Name    Type    Description
======= ======= ==============
Output0 Audio   chime output
Output1 Control chime end flag
======= ======= ==============

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
| GainValue_Point<n>      | -100 dB       | -120 to 24 dB     | Fine tuning of gain values of points in gain graph(<n> point count)           |
+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+
| GainTime(ms)_Point<n>   | 0             | 0 to Maximum Time | Fine tuning of time in ms of points in gain graph(<n> point count)            |
+-------------------------+---------------+-------------------+-------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-----------------+--------------------------------------+------------------------+---------------+
| Parameter Name  | Description                          | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================+======================================+========================+===============+
| Sin_c           | sine coefficient                     | Integer32              | Integer32     |
+-----------------+--------------------------------------+------------------------+---------------+
| Cos_c           | cos coefficient                      | Integer32              | Integer32     |
+-----------------+--------------------------------------+------------------------+---------------+
| FrequencyPoints | Time intervals of frequency points   | Integer32              | Integer32     |
+-----------------+--------------------------------------+------------------------+---------------+
| FrequencySlope  | scales the slope of frequency points | FixPoint2d62           | FixPoint2d62  |
+-----------------+--------------------------------------+------------------------+---------------+
| StartGain       | Initial gain value                   | Float                  | FixPoint8d24  |
+-----------------+--------------------------------------+------------------------+---------------+
| GainPoints      | Time intervals of gain points        | Integer32              | Integer32     |
+-----------------+--------------------------------------+------------------------+---------------+
| GainSlope       | scales the slope of gain points      | Float                  | FixPoint8d24  |
+-----------------+--------------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== sin_c=sin(initialFrequency[0] \* pi))
| cos_c=cos(initialFrequency[0] \* pi))
| StartGain= 10^(GainValue_Point[0] / 20)

.. |chimefreqgain.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/chimefreqgain.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/chimefreqgainwindow.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/chimefreqgain_gainwindow.png
   :width: 600px
