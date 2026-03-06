:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Tracking Filter
===============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/trackingfilter.png
   :alt: trackingfilter.png

Description
-----------

| Tracking Filters are useful for dynamic shifting of filtering. The tracking filter allows for the center frequency to be determined by an external input. Control Input is calculated as (2*fc)/fs, where fc is the center frequency and fs is the Schematic Sampling Rate
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Tracking Filter | NA         | B                | S             | B                |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

+---------------------------+---------+------------------------------------------------------------------------------------------------------------+
| Name                      | Type    | Description                                                                                                |
+===========================+=========+============================================================================================================+
| Input                     | Audio   | Input Signal                                                                                               |
+---------------------------+---------+------------------------------------------------------------------------------------------------------------+
| NormalizedCentreFrequency | Control | Control Input(should be (2*fc)/fs, where fc is the centre frequency and fs is the Schematic Sampling Rate) |
+---------------------------+---------+------------------------------------------------------------------------------------------------------------+

Output
~~~~~~

============== ===== ======================
Name           Type  Description
============== ===== ======================
FilteredOutput Audio Filtered Output Signal
============== ===== ======================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+---------------+-------------------------------+
| GUI Parameter Name | Default Value | Range         | Function Description          |
+====================+===============+===============+===============================+
| Gain               | 0             | -15dB to 15dB | Gain of the filter in DB      |
+--------------------+---------------+---------------+-------------------------------+
| QValue             | 1.71          | 0 to 16       | Quiescent value of the filter |
+--------------------+---------------+---------------+-------------------------------+
| Boost              | -15           | -15dB to 15dB | Filter boost value in DB      |
+--------------------+---------------+---------------+-------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------+------------------------+--------------------+
| Parameter Name | Description                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x      |
+================+===============================+========================+====================+
| GainLin        | Array of coefficients         | NA                     | FixPoint8d24 array |
+----------------+-------------------------------+------------------------+--------------------+
| Gain           | Gain of the filter in DB      | Float                  | NA                 |
+----------------+-------------------------------+------------------------+--------------------+
| QValue         | Quiescent value of the filter | Float                  | NA                 |
+----------------+-------------------------------+------------------------+--------------------+
| Boost          | Filter boost value in DB      | Float                  | NA                 |
+----------------+-------------------------------+------------------------+--------------------+

DSP Parameter Computation
-------------------------

| Gain = 10^(Gain / 20)
| Boost = 10^(Boost / 40)
