:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

ON/OFF Switch
=============

| 
| |onoff.png|

Description
-----------

| 
| The OnOffSwitch block outputs a constant value of either 0.0(OFF) or 1.0(ON).Click the switch control with mouse to toggle the switch 'OFF' or 'ON'.
| ===== Targets Supported =====

+-------------+------------+-----------------------+---------------+------------------+
| Name        | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+=============+============+=======================+===============+==================+
| OnOffSwitch | B/S        | B/S                   | S             | B                |
+-------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

====== ======= ================
Name   Type    Description
====== ======= ================
Enable Control Output channel 0
====== ======= ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------+--------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description           |
+====================+===============+============+================================+
| Switch_Enabled     | False         | True/False | Turn ON or Trun Off the switch |
+--------------------+---------------+------------+--------------------------------+

| 
| ===== DSP Parameters =====

+----------------+--------------------------------+------------------------+---------------+
| Parameter Name | Description                    | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+================================+========================+===============+
| Switch_Enabled | Turn ON or Trun Off the switch | Float                  | Integer32     |
+----------------+--------------------------------+------------------------+---------------+

| 
| ===== DSP Parameter Computation ===== Switch_Enabled = Switch_Enabled? 1: 0

.. |onoff.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/onoff.png
