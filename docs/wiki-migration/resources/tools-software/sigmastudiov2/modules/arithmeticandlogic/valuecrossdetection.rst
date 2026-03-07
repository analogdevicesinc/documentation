:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Value Cross Detection
=====================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/valuecrossdetect.png
   :alt: valuecrossdetect.png

Description
-----------

| The Value Cross Detection outputs a pulse every time the input signal has crossed the value specified in the cell. As a default this cell acts as a zero-cross detector, but it can compare the signal to any threshold value.
| ===== Targets Supported =====

+-----------------------+------------+------------------+---------------+------------------+
| Name                  | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=======================+============+==================+===============+==================+
| Value Cross Detection | NA         | B                | S             | NA               |
+-----------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

===== ===== =======================
Name  Type  Description
===== ===== =======================
Input Audio Input Signal to Monitor
===== ===== =======================

Output
~~~~~~

========== ======= ===========================
Name       Type    Description
========== ======= ===========================
FlagOutput Control Pulse output in 5.23 format
========== ======= ===========================

Configurable parameters
~~~~~~~~~~~~~~~~~~~~~~~

+------------------+---------------+------------+--------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range      | Function Description                                                           |
+==================+===============+============+================================================================================+
| ThresholdValue   | 0             | -15, 15    | This is the threshold value that the input signal is compared to.              |
+------------------+---------------+------------+--------------------------------------------------------------------------------+
| IsDB             | flase         | true/false | This is the boolean value that indicates how the input signal is displayed in. |
+------------------+---------------+------------+--------------------------------------------------------------------------------+

DSP parameter Information
~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+---------------------+------------------------------------------------------------------------+
| GUI Control Name | Compiler Name       | Function Description                                                   |
+==================+=====================+========================================================================+
| ThresholdValue   | CrossValueCrossAlg1 | When the value threshold is changed, it is written directly to the DSP |
+------------------+---------------------+------------------------------------------------------------------------+

Algorithm Description
~~~~~~~~~~~~~~~~~~~~~

The Input signal is compared to the Value Threshold. Each time the input signal crosses this value (whether rising or falling) the output of the cell goes high. Otherwise the output of the cell is low.
