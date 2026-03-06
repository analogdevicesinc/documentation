:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

State Variable
==============

| 
| |statevariablefilter.png| |statevariablewithq.png| |image1|

Description
-----------

| The State Variable filter can generate three types of filters: low pass, high pass, and bandpass. The low pass and high pass outputs are inverted in phase while the band pass maintains the phase. The three output pins let you choose among LP, HP, BP filters. The nature of this algorithm is to compute the coefficients for all filter types, giving you access to all of the filters simultaneously.
| StateVaribale (Q input & Q/F Input): Frequency and Q values are controlled using input pins.
| ===== Variants =====

-  State Variables
-  State Variable w/External Q input
-  State Variable Q / F Input

| 
| ===== Targets Supported =====

+-----------------------------------+------------+------------------+---------------+------------------+
| Name                              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================================+============+==================+===============+==================+
| State Variable                    | B/S        | B/S              | S             | B                |
+-----------------------------------+------------+------------------+---------------+------------------+
| State Variable w/External Q input | B/S        | B/S              | S             | B                |
+-----------------------------------+------------+------------------+---------------+------------------+
| State Variable Q / F Input        | NA         | NA               | S             | NA               |
+-----------------------------------+------------+------------------+---------------+------------------+

Pins
----

Input
~~~~~

+----------------+---------+-----------------------------------------------------------------------------+
| Name           | Type    | Description                                                                 |
+================+=========+=============================================================================+
| Input          | Audio   | Input Channel 0                                                             |
+----------------+---------+-----------------------------------------------------------------------------+
| QInput         | Control | External control over Q ( not applicable for State Variable)                |
+----------------+---------+-----------------------------------------------------------------------------+
| FrequencyInput | Control | External control over Frequency (applicable for State Variable Q / F Input) |
+----------------+---------+-----------------------------------------------------------------------------+

Output
~~~~~~

=============== ===== ================
Name            Type  Description
=============== ===== ================
LowPass_Output  Audio Output channel 0
HighPass_Output Audio Output channel 1
BandPass_Output Audio Output channel 2
=============== ===== ================

| 
| ===== Configurable Parameters =====

================== ============= ============= ======================
GUI Parameter Name Default Value Range         Function Description
================== ============= ============= ======================
Frequency          73            0 to 19148 Hz Cut-off frequency
OneOverQ           0.71          0.5 to 10     Q factor of the filter
================== ============= ============= ======================

| 
| ===== DSP Parameters =====

+----------------+------------------------+------------------------+---------------+
| Parameter Name | Description            | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+========================+========================+===============+
| Frequency      | Cut-off frequency      | Float                  | FixPoint8d24  |
+----------------+------------------------+------------------------+---------------+
| OneOverQ       | Q factor of the filter | Float                  | FixPoint8d24  |
+----------------+------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

Frequency = 2.0 - 2.0*Cos(2 \*PI \* Frequency/FS)

.. |statevariablefilter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/statevariablefilter.png
.. |statevariablewithq.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/statevariablewithq.png
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/qfinput.png
