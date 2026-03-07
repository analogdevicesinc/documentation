:doc:`Click here to return to the Filters page </wiki-migration/resources/tools-software/sigmastudiov2/modules/filters>`

General FIR Filter
==================

| 
| |generalfirfilter.png|

Description
-----------

The General FIR Filter block gives access to a below Filter type algorithms and Window types:

::

   Filter Types:
   * High-Pass
   * Low-Pass
   * Band-Pass
   * Band-Stop
   Window Types:
   * Hamming
   * Rectangular
   * Hamming
   * Blackman

| 
| ===== Usage ===== To open the filter control window, click on the icon button. Select the desired filter type from the drop-down combo-box list. The filter controls and the icon button image will change to reflect the selected filter type.
| ===== Targets Supported =====

+--------------------+------------+------------------+---------------+------------------+
| Name               | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+====================+============+==================+===============+==================+
| General FIR Filter | NA         | NA               | S             | NA               |
+--------------------+------------+------------------+---------------+------------------+

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

======= ===== ================
Name    Type  Description
======= ===== ================
Output0 Audio Output channel 0
======= ===== ================

| 

.. |generalfirfilter.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/filters/generalfirfilter.png
