Value Cross Detection
=====================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| --------------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| The Value Cross Detection outputs a pulse every time the input signal has crossed the value specified in the cell. As a default this cell acts as a zero-cross detector, but it can compare the signal to any threshold value. | |valuepic1.png| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

Input Pins
----------

+---------------------+------------------------------------+-------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description    |
+=====================+====================================+=========================+
| Pin 0: Input Signal | dec - audio                        | Input Signal to monitor |
+---------------------+------------------------------------+-------------------------+

Output Pins
-----------

+---------------------+------------------------------------+-----------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description        |
+=====================+====================================+=============================+
| Pin 0: Pulse Output | decimal - control                  | Pulse output in 5.23 format |
+---------------------+------------------------------------+-----------------------------+

GUI Control
-----------

+------------------+---------------+---------+-------------------------------------------------------------------+
| GUI Control Name | Default Value | Range   | Function Description                                              |
+==================+===============+=========+===================================================================+
| Value Threshold  | 0             | -15, 15 | This is the threshold value that the input signal is compared to. |
+------------------+---------------+---------+-------------------------------------------------------------------+

DSP parameter Information
-------------------------

+------------------+---------------------+------------------------------------------------------------------------+
| GUI Control Name | Compiler Name       | Function Description                                                   |
+==================+=====================+========================================================================+
| Value Threshold  | CrossValueCrossAlg1 | When the value threshold is changed, it is written directly to the DSP |
+------------------+---------------------+------------------------------------------------------------------------+

Algorithm Description
---------------------

| The Input signal is compared to the Value Threshold. Each time the input signal crosses this value (whether rising or falling) the output of the cell goes high. Otherwise the output of the cell is low. Below is a sample of the algorithm doing zero-cross detection, which is the default state of the block.
| |valuepic2.png|

Example
-------

| In some applications it is useful not just to know when there is a value cross, but also count the number of times that this happens during a specified time. Using the Value-Cross Detection block along with the :doc:`Pulse Counter </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/pulsecounter>`, allows the number of value-crosses to be counted. The following image uses a :doc:`sine tone </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/sinetone>` input, :doc:`on/off switches </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/onoffswitch>`, Pulse Counter, :doc:`Readback </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/dspreadback>` cell, and :doc:`GPIO output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeoutput>`.
| |valuepic3.png|

Algorithm Details
-----------------

========================== =========================================
Toolbox Path               Basic DSP - Logic - Value Cross Detection
Cores Supported            AD1940
                           ADAU170x
                           ADAU144x
                           ADAU176x
                           ADAU178x
"Grow Algorithm" Supported no
"Add Algorithm" Supported  yes - see Algorithm Addition Information
Subroutine/Loop Based      no
Program RAM                15\*
Data RAM                   3\*
Parameter RAM              1\*
========================== =========================================

\*Numbers are based on one instance of the algorithm with no additional "add"

Algorithm Addition Information
------------------------------

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| Description              | When you add an algorithm, a new set of input/output pins are generated, but the control stays the same. The Value Threshold is repeated, but the same value is used for all "adds" of the algorithm | |valuepic4.png| |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| Program RAM Repetition   | 15 per add                                                                                                                                                                                           |                 |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| Data RAM Repetition      | 3 per add                                                                                                                                                                                            |                 |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+
| Parameter RAM Repetition | 1 per add                                                                                                                                                                                            |                 |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+

.. |valuepic1.png| image:: https://wiki.analog.com/_media/valuepic1.png
.. |valuepic2.png| image:: https://wiki.analog.com/_media/valuepic2.png
.. |valuepic3.png| image:: https://wiki.analog.com/_media/valuepic3.png
.. |valuepic4.png| image:: https://wiki.analog.com/_media/valuepic4.png
