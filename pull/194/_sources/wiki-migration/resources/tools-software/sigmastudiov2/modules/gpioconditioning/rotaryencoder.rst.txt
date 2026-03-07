:doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudiov2/modules/gpioconditioning>`

Rotary Encoder
==============

| 
| |rotary_encoder_ssp.jpg|
| ===== Description =====
| The Rotary Encoder block processes the inputs from a rotary encoder and outputs an “up” and a “down” signal. The algorithm also incorporates a software "de-bouncer" for each of the inputs.
| ===== Usage =====
| 1) Drag the block into the schematic.
| 2) Connect the inputs to two GPIOs. These would correspond to the 2 out-of-phase output pins of a rotary encoder. In hardware configuration, set the GPIOs to “no debounce.”

| The value in the field sets the time constant (in samples) for the debouncer. Adjust this value by trial and error using the rotary encoder in your end system.
| ===== Targets Supported =====

+----------------+------------+-----------------------+---------------+------------------+
| Name           | ADSP-214xx | ADSP-215xx/ADSP-SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+================+============+=======================+===============+==================+
| Rotary Encoder | NA         | NA                    | S             | NA               |
+----------------+------------+-----------------------+---------------+------------------+

| 
| ===== Pins =====

Input
-----

====== ======= ==============================
Name   Type    Description
====== ======= ==============================
Input0 Control GPIO rotary up input control
Input1 Control GPIO rotary down input control
====== ======= ==============================

Output
------

======= ======= ===============================
Name    Type    Description
======= ======= ===============================
Output0 Control GPIO rotary up output control
Output1 Control GPIO rotary down output control
======= ======= ===============================

| 
| ===== Configurable Parameters =====

+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+
| GUI Parameter Name | Default Value | Range      | Function Description                                                                              |
+====================+===============+============+===================================================================================================+
| Gain               | 20            | 3 to 100   | Time constant for debounce                                                                        |
+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+
| IsLin              | true          | true/false | Setting this value to true indicates the gain is a decimal value, else the value is entered in dB |
+--------------------+---------------+------------+---------------------------------------------------------------------------------------------------+

| 
| ===== DSP Parameters =====

============== ========================== =================
Parameter Name Description                ADAU145x/ADAU146x
============== ========================== =================
countmax       Time constant for debounce Integer32
============== ========================== =================

| 
| ===== DSP Parameter Computation =====
| if IsLin ==true max= Gain else max = 10^ (Gain/20)

.. |rotary_encoder_ssp.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/gpioconditioning/rotary_encoder_ssp.jpg
