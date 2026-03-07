:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Signal Invert
=============

| 
| |invert.png|

Description
-----------

| The SignalInvert block inverts the polarity of the incoming signal.Signal invert entails a 180-degree phase shift, making the positive components of waveform to negative and negative components of waveform to positive.
| ===== Usage ===== Check the box to enable this block.
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
Signal Invert B/S        B/S              S             B
============= ========== ================ ============= ================

Pins
----

Input
~~~~~

===== ===== ===============
Name  Type  Description
===== ===== ===============
Input Audio Input channel 0
===== ===== ===============

Output
~~~~~~

====== ======= ================
Name   Type    Description
====== ======= ================
Output Control Output channel 0
====== ======= ================

Configurable Parameters
-----------------------

+--------------------+---------------+------------+-----------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description              |
+====================+===============+============+===================================+
| IsInverted         | False         | True/False | Inverts the input signal polarity |
+--------------------+---------------+------------+-----------------------------------+

DSP Parameters
--------------

============== =================================
Parameter Name Description
============== =================================
IsInverted     Inverts the input signal polarity
============== =================================

DSP Parameter Computation
-------------------------

Output = IsInverted? -Input:Input

.. |invert.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/invert.png
