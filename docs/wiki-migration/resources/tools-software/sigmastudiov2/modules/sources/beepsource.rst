:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Beep Generator
==============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/beep.png
   :alt: beep.png

Description
-----------

| The Beep Generator module uses an internal oscillator to generate tones. Set the frequency in the text field and click on the Beep button to enable the tone generator. This tone is only active while the beep button is pressed.
| ===== Targets Supported =====

+----------------+------------+-----------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+=======================+===============+==================+
| Beep Generator | B/S        | B/S                   | S             | B                |
+----------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Output
~~~~~~

====== ======= ================
Name   Type    Description
====== ======= ================
Output Control Output channel 0
====== ======= ================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------+-----------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                    |
+====================+===============+============+=========================================+
| BeepPressed        | False         | True/False | This control enables the tone generator |
+--------------------+---------------+------------+-----------------------------------------+
| Frequency          | 1000          | 0 to 20000 | frequency of the tone generator         |
+--------------------+---------------+------------+-----------------------------------------+

| 
| ===== DSP Parameters =====

+----------------+-------------------------------+------------------------+---------------+
| Parameter Name | Description                   | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+===============================+========================+===============+
| BeepPressed    | Enables the tone generator    | Integer32              | FixPoint8d24  |
+----------------+-------------------------------+------------------------+---------------+
| Cos            | Cosine value of the frequency | FixPoint2d30           | FixPoint8d24  |
+----------------+-------------------------------+------------------------+---------------+
| Sin            | Sine value of the frequency   | FixPoint2d30           | FixPoint8d24  |
+----------------+-------------------------------+------------------------+---------------+

| 
