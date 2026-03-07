:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Software debounce
=================

| 
| |software_debounce_ssp.jpg|
| ===== Description =====
| The contacts of mechanical switches and encoders can "bounce" when changing positions; meaning the voltage may fluctuate between states several times during the transition period. When the transition is not clean erroneous states can be set in your system. This block debounces (removes the transition ripple) from a signal, by waiting a specified amount of time between sampling periods. This provides a clean transition signal to the output.
| ===== Usage =====
| Typically, this block is used to debounce a GPIO input signal. To use this block, drag it into the schematic and connect the input to a GPIO signal. The debounce time control sets the time constant for the debouncer, in samples; the default is 20. For best results adjust the value by trial and error for whatever hardware is connected to the GPIO input.

Targets Supported
-----------------

+-------------------+------------+-----------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+=======================+===============+==================+
| Software debounce | NA         | NA                    | Sample        | NA               |
+-------------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

====== ===== ====================================
Name   Type  Description
====== ===== ====================================
Input0 Audio Audio input to the software debounce
====== ===== ====================================

Output
~~~~~~

======= ===== =======================================
Name    Type  Description
======= ===== =======================================
Output0 Audio Audio output from the software debounce
======= ===== =======================================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+-----------+------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range     | Function Description                                       |
+====================+===============+===========+============================================================+
| CountMax           | 20            | [0, 1000] | Sample counter for the Debounce time on the Rotary Encoder |
+--------------------+---------------+-----------+------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== =============================== =================
Parameter Name Description                     ADAU145x/ADAU146x
============== =============================== =================
countmax       Time constant for the debouncer Integer32
============== =============================== =================

| 
| ===== DSP Parameter Computation =====
| Not applicable

.. |software_debounce_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/software_debounce_ssp.jpg
