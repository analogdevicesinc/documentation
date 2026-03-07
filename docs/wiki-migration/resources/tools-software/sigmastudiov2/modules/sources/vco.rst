:doc:`Click here to return to the Source page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Voltage Controlled Oscillator
=============================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/vco.png
   :alt: vco.png

Description
-----------

| 
| The Voltage Controlled Oscillator block, typically used for modulation applications. Takes the control input and generates a sine tone at particular frequency.

Usage
-----

| 
| The input to the control pin could be varied from 0 to 1. VCO linearly interpolates its derived value into frequency from 0Hz (when input is 0) to FS/2(when input is 1). Where FS is the sampling frequency. If the input applied is greater than 1, the derived output value will fold back to frequencies below fs/2.

Targets Supported
-----------------

==== ========== ================ ============= ================
Name ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
==== ========== ================ ============= ================
VCO  B/S        B/S              S             B
==== ========== ================ ============= ================

Pins
----

Input
~~~~~

============== ======= ======================================
Name           Type    Description
============== ======= ======================================
ControlVoltage Control Controls the frequency of the sinetone
============== ======= ======================================

Output
~~~~~~

================ ======= ================
Name             Type    Description
================ ======= ================
OscillatorOutput Control Output channel 0
================ ======= ================

Configurable Parameters
-----------------------

No Configurable parameters

DSP Parameters
--------------

No DSP parameters
