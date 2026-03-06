:doc:`Click here to return to the Gain page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gain>`

Gain Envelope
=============

| |gainenvelope.png|
| |gainenvelopewindow.png|

Description
-----------

The Generic Gain Envelope algorithm has a fully programmable gain envelope. The envelope is accessible by clicking the cell’s icon. The length of the envelope is controlled by the Maximum Time control, which is set in milliseconds. Points on the curve can be moved by click-dragging. New points can be added by double-clicking. Points can be removed by right-clicking and selecting “remove point.” In this case, the point closest to the mouse cursor will be removed. The envelope must have at least 3 points. Point values can be fine-tuned using the text input boxes on the right side of the envelope control window. In Generic Gain Envelope, when the control input goes to 1, the gain envelope begins. When the control input goes to 0, the gain envelope stops, regardless of whether the envelope has completed or not.

| In the case of the Generic Gain Envelope Alg EndlessLoop algorithm, the envelope will loop continuously until the control input goes to 0.
| ===== Variants ===== Selected Gain Envelope Type

-  Generic Gain Envelope
-  Gain Envelope EndlessLoop

Targets Supported
-----------------

+---------------------------+------------+------------------+---------------+------------------+
| Name                      | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===========================+============+==================+===============+==================+
| Gain Envelope             | B/S        | B/S              | S             | B                |
+---------------------------+------------+------------------+---------------+------------------+
| Gain Envelope EndlessLoop | B/S        | B/S              | S             | B                |
+---------------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

======================= ======= ===============
Name                    Type    Description
======================= ======= ===============
EnvelopeControl         Control Control Input
Input<fc #ff0000>X</fc> Audio   Input channel X
======================= ======= ===============

Output
~~~~~~

========================= ===== ================
Name                      Type  Description
========================= ===== ================
Output <fc #ff0000>X</fc> Audio Output channel X
========================= ===== ================

Note:

-  <fc #ff0000>X</fc> - Channel Index

Configurable Parameters
-----------------------

+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+
| GUI Parameter Name                | Default Value         | Range             | Function Description                                                          |
+===================================+=======================+===================+===============================================================================+
| Maximum Time                      | 1104 ms               | 10 to 4400 ms     | Time interval in ms                                                           |
+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+
| GainValue_Point<fc #ff0000>N</fc> | -100 dB               | -120 to 24 dB     | Fine tuning of gain values of points in graph(<fc #ff0000>N</fc> point count) |
+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+
| Time(ms)_Point<fc #ff0000>N</fc>  | 0                     | 0 to Maximum Time | Fine tuning of time in ms of points in graph(<fc #ff0000>N</fc> point count)  |
+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+
| NumChannels                       | 2                     | 20                | Number of input channels. Change in this value requires re-compilation        |
+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+
| GainEnvelopeType                  | Generic Gain Envelope | NA                | Gain Envelope types. Change in this value requires re-compilation             |
+-----------------------------------+-----------------------+-------------------+-------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+--------------------+---------------------------------+------------------------+---------------+
| Parameter Name     | Description                     | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+====================+=================================+========================+===============+
| StartGain          | Initial gain value              | Float                  | FixPoint8d24  |
+--------------------+---------------------------------+------------------------+---------------+
| GainPoints         | Time intervals of gain points   | Integer32              | Integer32     |
+--------------------+---------------------------------+------------------------+---------------+
| GainSlope          | scales the slope of gain points | Float                  | FixPoint8d24  |
+--------------------+---------------------------------+------------------------+---------------+
| numberofgainpoints | gain points count               | NA                     | Integer32     |
+--------------------+---------------------------------+------------------------+---------------+
| lowestgain         | lowest gain value               | NA                     | FixPoint8d24  |
+--------------------+---------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation =====

================== =========================================
StartGain          = Math.Pow(10, (GainValue_Point[0] / 20))
lowestgain         =0.00000025
numberofgainpoints = GainPoints count - 1
================== =========================================

| 

.. |gainenvelope.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/gainenvelope.png
.. |gainenvelopewindow.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gain/gainenvelopewindow.png
   :width: 600px
