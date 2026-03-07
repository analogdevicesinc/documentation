:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General 2nd Order with Var Param Lookup Slew
============================================

| |gsoicon.png|
| |gso.png|
| =====Description===== The General (2nd-Order / Lookup) block gives access to a wide variety of 2nd-order IIR (infinite impulse response) filter algorithms. See General 2nd-Order Filters (in Algorithm Information) for details about the algorithms driving these blocks.

The filters available are: Tone Peaking General LP/HP Butterworth LP/HP Bessel LP/HP Chebyshev LP/HP

The block is simply a double-precision biquad filter that has stored a set of coefficients in tables in the DSP. To select curves (lookup), use an Index Lookup Table, a Counter block, or a DC Input block in your design and connect it to the red pin.

Usage
=====

Click the icon button:. The curve is defined using the Tone Control window (shown above).

Enter the number of curves desired in the # Curves field. Enter Boosts, (overall) Gain, and Q in their fields. Enter the desired cutoff or center (peaking filters) frequency in the Frequency fields. Other parameters to enter will vary with filter type.

| The variety and range of filters are remarkable, as can be seen from the many examples in the General (2nd-Order / Lookup) topic page.
| ===== Targets Supported =====

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
Parametric EQ B/S        B/S              S             NA
============= ========== ================ ============= ================

Pins
====

Input
-----

============ ======= ======================
Name         Type    Description
============ ======= ======================
ControlInput Control Filter Index Selection
Input0       Audio   Input to the filter
============ ======= ======================

Output
------

======= ===== ===================
Name    Type  Description
======= ===== ===================
Output0 Audio The filtered output
======= ===== ===================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range         | Function Description                                                                                                                                                                                     |
+====================+===============+===============+==========================================================================================================================================================================================================+
| NumCurves          | 4             | 2 to 50       | The number of curves desired from which a particular filter can be selected                                                                                                                              |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FilterType         | 0             | 0 to 5        | Select the type of filter                                                                                                                                                                                |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SubType            | 0             | 0 and 1       | The “Sub Type” section is only available for butterworth, chebyshev and bessel filter types. The subtype selects either high or low pass.                                                                |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BoostMax           | -10 dB        | -20 to +20 dB | Set the maximum value for boost                                                                                                                                                                          |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BoostMin           | 10 dB         | -20 to +20 dB | Set the minimum value for boost                                                                                                                                                                          |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FrequencyMax       | 100 Hz        | 0 to 96kHz    | The maximum value of frequency                                                                                                                                                                           |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| FrequencyMin       | 300 Hz        | 0 to 96kHz    | The minimum value of frequency                                                                                                                                                                           |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Gain               | -5 dB         | -20 to +20 dB | Filter Gain                                                                                                                                                                                              |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| QFactor            | 0.707         | 0.01 to 10    | Q factor of the filter                                                                                                                                                                                   |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ripple             | 0.1           | 0.1 to 5      | Set the Ripple factor for filter. Available only for Chebyshev type                                                                                                                                      |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumChannels        | 1             | 1 to 20       | Number of input and output channels. Change in this value requires re-compilation                                                                                                                        |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SlewPoints         | 12            | 5 to 22       | The “Slew Points” control sets how many transition points the algorithm uses to transition from one selected filter curve to another, increasing the number of points will provide smoother transitions. |
+--------------------+---------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

+-------------------------+----------------------------------------------------------------+------------------------+---------------+
| Parameter Name          | Description                                                    | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=========================+================================================================+========================+===============+
| FilterCoefficientsArray | Filter Coefficient Array consisting of all filter coefficients | Float                  | FixPoint8d24  |
|                         | along with slew rate values                                    |                        |               |
+-------------------------+----------------------------------------------------------------+------------------------+---------------+
| slew_mode               | Filter Slew Value                                              | NA                     | Integer32     |
+-------------------------+----------------------------------------------------------------+------------------------+---------------+

.. |gsoicon.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/gsoicon.png
.. |gso.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/gso.png
