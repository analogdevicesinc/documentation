Clipping Detection
==================

| 
| :doc:`Click here to return to the Non Linear Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors>`

Description
-----------

The clipping detection module can be used to identify whether there is a clipping in a particular wave form. It indicates the signal reaching the onset of its maximum permitted peak-to-peak voltage value before an overload is occurring. This will help in preventing severe, audible distortion to be generated through the audio signal chain.

| |image1|
| ===== Targets Supported =====

================== ========== ================ =============
Name               ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x
================== ========== ================ =============
Clipping Detection NA         Block            NA
================== ========== ================ =============

| 
| ===== Pins =====

Input
~~~~~

====== ===== ==============
Name   Type  Description
====== ===== ==============
Input0 Audio Input channel0
====== ===== ==============

Output
~~~~~~

============ ======= =======================
Name         Type    Description
============ ======= =======================
Output0      Audio   Output channel0
ClippingFlag Control Clipping detection flag
============ ======= =======================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+--------------+------------------------------------------+
| GUI Parameter Name | Default Value | Range        | Function Description                     |
+====================+===============+==============+==========================================+
| Enable             | False         | True / False | Enable or disable the clipping detection |
+--------------------+---------------+--------------+------------------------------------------+
| Delay              | 64            | 8 to 1024    | Scales the delay factor                  |
+--------------------+---------------+--------------+------------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+----------------------------------+------------------------+---------------+
| Parameter Name | Description                      | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+==================================+========================+===============+
| Enable         | zero or one depends on the state | Integer32              | NA            |
+----------------+----------------------------------+------------------------+---------------+
| Delay          | Delay Factor                     | Integer32              | NA            |
+----------------+----------------------------------+------------------------+---------------+

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/nonlinearprocessors/clipping_detc1.jpg
   :width: 400px
