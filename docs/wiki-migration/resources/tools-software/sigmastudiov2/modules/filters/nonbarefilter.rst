:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

Non-Bare Filter
===============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/nonbarefilter.png
   :alt: nonbarefilter.png

Description
-----------

| NonBare filters are second order filters which take the parameters directly. The filter parameters are converted to filter coefficients by the Module itself. Regalia-Mitra algorithm is used for this implementation.
| ===== Targets Supported =====

+-----------------+------------+------------------+---------------+------------------+
| Name            | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=================+============+==================+===============+==================+
| Non-Bare Filter | B          | B                | NA            | B                |
+-----------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

===== ===== =============
Name  Type  Description
===== ===== =============
Input Audio Input Channel
===== ===== =============

Output
~~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Output Audio Output channel
====== ===== ==============

| 
| ===== Configurable Parameters =====

+--------------------+---------------+---------------+----------------------------------------+
| GUI Parameter Name | Default Value | Range         | Function Description                   |
+====================+===============+===============+========================================+
| Gain               | 0dB           | -15 to 15dB   | Gain of the filter in DB               |
+--------------------+---------------+---------------+----------------------------------------+
| Qvalue             | 1.71          | 0.2 to 15     | Quiscent factor of the filter          |
+--------------------+---------------+---------------+----------------------------------------+
| K                  | 1             | 0 to 2        | K values as described in the algorithm |
+--------------------+---------------+---------------+----------------------------------------+
| Frequency          | 1000          | 1 to 24000 Hz | Cut-off frequency of the filter        |
+--------------------+---------------+---------------+----------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------------+------------------------+---------------+
| Parameter Name | Description                            | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+========================================+========================+===============+
| Frequency      | Cut-off frequency of the filter        | Float                  | NA            |
+----------------+----------------------------------------+------------------------+---------------+
| Omega          | Quiscent factor of the filter          | Float                  | NA            |
+----------------+----------------------------------------+------------------------+---------------+
| Gain           | Gain of the filter in DB               | Float                  | NA            |
+----------------+----------------------------------------+------------------------+---------------+
| K              | K values as described in the algorithm | Float                  | NA            |
+----------------+----------------------------------------+------------------------+---------------+
