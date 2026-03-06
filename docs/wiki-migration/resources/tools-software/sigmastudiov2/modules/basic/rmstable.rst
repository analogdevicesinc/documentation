:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

RMS Table
=========

| |rmstable.png|
| |rmstablepopup.png|

Description
-----------

The RMS Table takes an input signal and outputs the interpolated mapped value of the signal, relative to the table, depending on the calculated rms input. The block uses rms average values and maps them to the user-selectable table values, employing linear interpolation in between table values.

Usage
-----

To edit the table values click on the showtable button and it will open the RMS Table Editor window to configure the table values.

Targets Supported
-----------------

========= ========== ================ ============= ================
Name      ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========= ========== ================ ============= ================
RMS Table B/S        B/S              S             B
========= ========== ================ ============= ================

Pins
----

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
Output0 Control Output channel 0
======= ======= ================

Configurable Parameters
-----------------------

+--------------------+------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value    | Range            | Function Description                                                                                                                                                                         |
+====================+==================+==================+==============================================================================================================================================================================================+
| RmsTC              | 70 dB/s          | 10 to 10000 dB/s | Controls the time constant used for calculating the RMS value. This determines how rapidly the gain will adapt to changes in the input level; this is also called the attack time.           |
+--------------------+------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold               | 0 ms             | 0 to 2000 ms     | Controls the time the RMS average holds its current output setting before it detects a lower value and starts ramping down.                                                                  |
+--------------------+------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay              | 4 dB/s           | 0 to 20 dB/s     | Controls the rate at which the output signal returns to a lower detected level. Decay is responsible for releasing the signal at a given rate. This is also referred to as the release time. |
+--------------------+------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TableValues        | All values are 1 | NA               | User-configurable values                                                                                                                                                                     |
+--------------------+------------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                                                                                                                                                 | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+=============================================================================================================================================================================================+========================+===============+
| RmsTC          | Controls the time constant used for calculating the RMS value. This determines how rapidly the gain will adapt to changes in the input level; this is also called the attack time           | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Hold           | Controls the time the RMS average holds its current output setting before it detects a lower value and starts ramping down.                                                                 | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Decay          | Controls the rate at which the output signal returns to a lower detected level. Decay is responsible for releasing the signal at a given rate. This is also referred to as the release time | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| TableValues    | Table Values                                                                                                                                                                                | Float                  | FixPoint8d24  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

| RmsTC = Abs(1-(10)^(RmsTC/(10*(FS+0.000001) )))
| Hold= Hold*FS /1000
| Decay = Decay/ (FS + 0.000001)
| Decay = Decay /(3\* (\_FS + 0.000001)) ( Decay calculation for ADAU145x/146x)

.. |rmstable.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/rmstable.png
.. |rmstablepopup.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/rmstablepopup.png
