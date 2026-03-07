:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Square Wave
===========

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/sqaure.png
   :alt: sqaure.png

Description
-----------

| 
| The Square Wave block generates a square wave at a constant level and at different frequencies.

Usage
-----

| 
| This block has checkbox to enabled or disabled the algorithm. Check the box to enable this algorithm. It has the numeric text box to edit the frequency to generate the square wave at different frequencies.

Targets Supported
-----------------

=========== ========== ================ ============= ================
Name        ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
=========== ========== ================ ============= ================
Square Wave B/S        B/S              S             B
=========== ========== ================ ============= ================

Pins
----

Output
~~~~~~

======= ======= ================
Name    Type    Description
======= ======= ================
Output0 Control Output channel 0
======= ======= ================

Configurable Parameters
-----------------------

+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range                  | Function Description                                                                                                            |
+====================+===============+========================+=================================================================================================================================+
| Frequency          | 500           | 0 to 0.5\* sample rate | Sets the frequency for square wave                                                                                              |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| OnOff              | False         | True/False             | Enabled/Disabled the algorithm for the channel, When the algorithm is disabled, the output pin will output a constant value 0.0 |
+--------------------+---------------+------------------------+---------------------------------------------------------------------------------------------------------------------------------+

DSP Parameters
--------------

+----------------+----------------------------------------------------------------+------------------------+---------------+
| Parameter Name | Description                                                    | ADSP-214xx/SC5xx/215xx | ADAU145x/146x |
+================+================================================================+========================+===============+
| Sin            | Sin value for generating a square wave at particular frequency | FixPoint2d30           | FixPoint8d24  |
+----------------+----------------------------------------------------------------+------------------------+---------------+
| Cos            | Cos value for generating a square wave at particular frequency | FixPoint2d30           | FixPoint8d24  |
+----------------+----------------------------------------------------------------+------------------------+---------------+
| OnOff          | Enabled/Disabled the algorithm                                 | FixPoint2d30           | FixPoint8d24  |
+----------------+----------------------------------------------------------------+------------------------+---------------+

DSP Parameter Computation
-------------------------

| Sin = sin⁡(2\*π*fs/FS)
| Cos = cos⁡(2\*π*fs/FS)
| Where fs is frequency and FS is the sampling rate
