:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

White Noise
===========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/whitenoise.png
   :alt: whitenoise.png

Description
-----------

| 
| The White Noise block generates a signal that contains equal energy per frequency domain(hertz or similar increament).This random time-varying signal can be useful for testing equipment, although for audio situations white noise is commonly run through a pinking filter, to better simulate the behavior and response of the human ear.

A simple on/off toggle (right) controls the cell output.

Targets Supported
-----------------

========== ========== ================ ============= ================
Name       ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
========== ========== ================ ============= ================
WhiteNoise B/S        B/S              S             B
========== ========== ================ ============= ================

Pins
----

Output
~~~~~~

========== ===== ================
Name       Type  Description
========== ===== ================
WhiteNoise Audio Output channel 0
========== ===== ================

Configurable Parameters
-----------------------

+--------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                                                                                            |
+====================+===============+============+=================================================================================================================+
| WhiteNoise_Enabled | False         | True/False | Enabled/Disabled the algorithm, When the algorithm is disabled, the output pin will output a constant value 0.0 |
+--------------------+---------------+------------+-----------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+--------------------+-----------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Parameter Name     | Description                                                                                                     | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+====================+=================================================================================================================+========================+===============+
| WhiteNoise_Enabled | Enabled/Disabled the algorithm, When the algorithm is disabled, the output pin will output a constant value 0.0 | Float                  | FixPoint8d24  |
+--------------------+-----------------------------------------------------------------------------------------------------------------+------------------------+---------------+
| Seed               | Random Value between 0 to 65536                                                                                 | Float                  | Integer32     |
+--------------------+-----------------------------------------------------------------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

WhiteNoise_Enabled = WhiteNoise_Enabled? 1: 0
