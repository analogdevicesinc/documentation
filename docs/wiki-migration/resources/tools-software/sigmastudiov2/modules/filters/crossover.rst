:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Crossover Filters
=================

| 
| |crossover3wayicon.png|
| |crossover3way.png|
| |crossover2wayicon.png|
| |crossover2way.png|

Description
-----------

The Crossover block includes 2-way and 3-way crossover filters, typically used in loudspeaker systems to split the audio signal into separate frequency bands.

| This filter provides: 2-way or 3-way crossover filtering. Graphical design of crossover response. Selectable crossover types: Linkwitz-Riley, Butterworth, Bessel. Selectable filter orders: 2nd, 3rd, 4th, 6th, and 8th
| ===== Usage =====
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Crossover 3 Way | NA         | B/S              | S             | B                |
+-----------------+------------+------------------+---------------+------------------+
| Crossover 2 Way | NA         | B/S              | S             | B                |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ===============
Name   Type  Description
====== ===== ===============
Input0 Audio Input Channel 0
====== ===== ===============

Output
~~~~~~

============================== ===== ================
Name                           Type  Description
============================== ===== ================
Output0                        Audio Output channel 0
Output1                        Audio Output channel 1
Output2 (CrossOver 3 Way Only) Audio Output channel 2
============================== ===== ================

| 
| ===== Configurable Parameters =====

+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value  | Range         | Function Description                                                                       |
+====================+================+===============+============================================================================================+
| LowFrequency       | 250            | 3 to 30 KHz   | Cut-off frequency for Low Filter                                                           |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidLowFrequency    | 250            | 3 to 30 KHz   | Cut-off frequency for Mid-Low filter                                                       |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidHighFrequency   | 3000           | 3 to 30 KHz   | Cut-off frequency for Mid-High Filter                                                      |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| HighFrequency      | 3000           | 3 to 30 KHz   | Cut-off frequency for High Filter                                                          |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| LowGain            | 0 dB           | -10 to +10 dB | Filter Gain for Low Filter                                                                 |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidLowGain         | 0 dB           | -10 to +10 dB | Filter Gain for Mid-Low Filter                                                             |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidHighGain        | 0 dB           | -10 to +10 dB | Filter Gain for Mid-High Filter                                                            |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| HighGain           | 0 dB           | -10 to +10 dB | Filter Gain for High Filter                                                                |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| LowFilterType      | Linkwitz-Riley | Filters List  | Used to select the filter type for Low Filter                                              |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidLowFilterType   | Linkwitz-Riley | Filters List  | Used to select the filter type for Mid-Low Filter                                          |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| MidHighFilterType  | Linkwitz-Riley | Filters List  | Used to select the filter type for Mid-High Filter                                         |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| HighFilterType     | Linkwitz-Riley | Filters List  | Used to select the filter type for High Filter                                             |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| LowInvertPolarity  | False          | True/False    | Invert polarity of Low Filter                                                              |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| HighInvertPolarity | False          | True/False    | Invert Polarity of High Filter                                                             |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| LinkLowMidFilters  | False          | True/False    | Link the low and mid low filters to ensure frequency changes in the two filters are same   |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+
| LinkMidHighFilters | False          | True/False    | Link the high and mid high filters to ensure frequency changes in the two filters are same |
+--------------------+----------------+---------------+--------------------------------------------------------------------------------------------+

| 
| Note : Mid Low and Mid High filters and their parameters are only applicable for Crossover 3 Way Filters.

DSP Parameters
--------------

+-----------------+------------------------------------------------------------------+------------------------+---------------+
| Parameter Name  | Description                                                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+=================+==================================================================+========================+===============+
| LowPolarity     | Polarity Inversion Status of Low Filter                          | FixInt32               | FixInt32      |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| HighPolarity    | Polarity Inversion Status of High Filter                         | FixInt32               | FixInt32      |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| LowFilterCount  | Number of bi-quads for Low Filter Type                           | FixInt32               | FixInt32      |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| MidFilterCount  | Number of bi-quads for Mid Filter Type                           | FixInt32               | FixInt32      |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| HighFilterCount | Number of bi-quads for High Filter Type                          | FixInt32               | FixInt32      |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| A1_FilterType   | Filter coefficient A1 of bi-quad stage X Mid/Low/High FilterType | Float                  | Float         |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| A2_FilterType   | Filter coefficient A2 of bi-quad stage X Mid/Low/High FilterType | Float                  | Float         |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| B0_FilterType   | Filter coefficient B0 of bi-quad stage X Mid/Low/High FilterType | Float                  | Float         |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| B1_FilterType   | Filter coefficient B1 of bi-quad stage X Mid/Low/High FilterType | Float                  | Float         |
+-----------------+------------------------------------------------------------------+------------------------+---------------+
| B2_FilterType   | Filter coefficient B2 of bi-quad stage X Mid/Low/High FilterType | Float                  | Float         |
+-----------------+------------------------------------------------------------------+------------------------+---------------+

| 
| Note FilterType Refers to Low, Mid-Low, Mid-High and High.

.. |crossover3wayicon.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/crossover3wayicon.png
.. |crossover3way.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/crossover3way.png
   :width: 550px
.. |crossover2wayicon.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/crossover2wayicon.png
.. |crossover2way.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/crossover2way.png
   :width: 550px
