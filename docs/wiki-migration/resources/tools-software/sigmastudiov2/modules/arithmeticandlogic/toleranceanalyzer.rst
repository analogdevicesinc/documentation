:doc:`Click here to return to the Arithmetic and Logic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic>`

Tolerance Analyzer
==================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/arithmeticandlogic/toleranceanalyser.png
   :alt: toleranceanalyser.png

Description
-----------

| This block is for any application where you need to verify a given value's tolerance limits. It is especially useful for testing environments where the Sigma DSP needs to perform system diagnostics. The Tolerance Analyzer outputs either one or zero based on input level: if the level falls within the limits specified, it outputs one at the output pin; otherwise it outputs zero.
| \**Values in the controls are integer (32.0 or 28.0) format. Audio data is not directly compatible with these inputs

Targets Supported
-----------------

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| Tolerance Analyzer | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input channel 0
====== ===== ===============

Output
~~~~~~

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

Configurable Parameters
-----------------------

+--------------------------------------+---------------+---------+-----------------------------------------------------------------+
| GUI Parameter Name                   | Default Value | Range   | Function Description                                            |
+======================================+===============+=========+=================================================================+
| NumChannels                          | 1             | 15      | Number of input channels .Change in this requires recompilation |
+--------------------------------------+---------------+---------+-----------------------------------------------------------------+
| LowerLimit_Channel<fc #ff0000>x</fc> | INT_MIN       | INT_MAX | Lower Limit channel threshold                                   |
+--------------------------------------+---------------+---------+-----------------------------------------------------------------+
| UpperLimit_Channel<fc #ff0000>x</fc> | INT_MIN       | INT_MAX | Upper Limit channel threshold                                   |
+--------------------------------------+---------------+---------+-----------------------------------------------------------------+

\\\\\* Note: <fc #ff0000>x</fc> represents the channel number in the above table.

DSP Parameters
--------------

+----------------+------------------------------------------+------------------------+-------------+
| Parameter Name | Description                              | ADSP-214xx/215xx/SC5xx | ADAU145x/6x |
+================+==========================================+========================+=============+
| lower          | Compute the output value based on limits | NA                     | 8.24 format |
+----------------+------------------------------------------+------------------------+-------------+

As long as the input remains within the limit, the module outputs 1. When the signal is out of (above or below) the limit, the block outputs 0
